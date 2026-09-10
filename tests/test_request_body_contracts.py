"""CatalystCenterAPI request-body contract tests.

Copyright (c) 2026 Cisco Systems.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import ast
import importlib
from pathlib import Path

import pytest

NAMESPACES = ["v2_3_7_6_1", "v2_3_7_9", "v3_1_3_0", "v3_1_6_0", "v3_2_3_0"]


class RecordingSession:
    """Captures the request an API method hands to the session."""

    headers = {}

    def __init__(self):
        self.calls = []

    def _record(self, url, **kwargs):
        self.calls.append(kwargs)
        return {}

    get = _record
    post = _record
    put = _record


def build(namespace, module, cls_name):
    cls = getattr(
        importlib.import_module(f"catalystcentersdk.api.{namespace}.{module}"), cls_name
    )
    # Built without __init__ so no live RestSession is needed.
    api = cls.__new__(cls)
    api._session = RecordingSession()
    api._object_factory = lambda key, data: data
    api._request_validator = None
    return api


def forwarding_mismatches(namespace):
    """Alias methods whose forwarded keywords the target does not declare.

    Such a keyword is swallowed by the target's **request_parameters and sent as
    a query parameter, so the field silently never reaches the request body.
    """
    mismatches = []
    for path in sorted(Path(f"catalystcentersdk/api/{namespace}").glob("*.py")):
        if path.name == "__init__.py":
            continue
        for cls in [
            n for n in ast.parse(path.read_text()).body if isinstance(n, ast.ClassDef)
        ]:
            methods = {n.name: n for n in cls.body if isinstance(n, ast.FunctionDef)}
            for name, node in methods.items():
                if "e_url" in ast.unparse(node):
                    continue
                call = next(
                    (
                        n.value
                        for n in ast.walk(node)
                        if isinstance(n, ast.Return)
                        and isinstance(n.value, ast.Call)
                        and isinstance(getattr(n.value.func, "value", None), ast.Name)
                        and n.value.func.value.id == "self"
                    ),
                    None,
                )
                if call is None or call.func.attr not in methods:
                    continue
                declared = {a.arg for a in methods[call.func.attr].args.args}
                lost = sorted({k.arg for k in call.keywords if k.arg} - declared)
                if lost:
                    mismatches.append(f"{path.stem}.{name} -> {call.func.attr}: {lost}")
    return mismatches


@pytest.mark.parametrize("namespace", NAMESPACES)
def test_alias_methods_forward_names_their_target_declares(namespace):
    assert forwarding_mismatches(namespace) == []


# Aliases that used to forward snake_case names to a camelCase target.
ALIAS_CALLS = [
    (
        "network_settings",
        "NetworkSettings",
        "create_network_v2",
        {"site_id": "site-1", "settings": {"dhcpServer": ["192.0.2.1"]}},
    ),
    (
        "network_settings",
        "NetworkSettings",
        "assign_device_credential_to_site_v2",
        {"site_id": "site-1", "cliId": "cred-1"},
    ),
    (
        "wireless",
        "Wireless",
        "configure_access_points_connectivity_v2",
        {"apList": [{"apName": "ap-1"}], "adminStatus": True},
    ),
    (
        "discovery",
        "Discovery",
        "create_global_credentials_v2",
        {"cliCredential": [{"username": "admin"}]},
    ),
    (
        "site_design",
        "SiteDesign",
        "creates_a_floor_v2",
        {"name": "Floor 1", "parentId": "site-1", "rfModel": "Cubes And Ceiling Mount"},
    ),
    (
        "configuration_templates",
        "ConfigurationTemplates",
        "deploy_template_v2",
        {"templateId": "template-1"},
    ),
]


@pytest.mark.parametrize("module,cls_name,method,kwargs", ALIAS_CALLS)
def test_alias_sends_a_request_body_not_query_parameters(
    module, cls_name, method, kwargs
):
    api = build("v3_2_3_0", module, cls_name)
    getattr(api, method)(active_validation=False, **kwargs)
    sent = api._session.calls[0]
    assert sent.get("json"), f"{method} sent an empty body"
    assert not sent.get("params"), f"{method} leaked fields into the query string"


# Fields added for StackSwitch claims, which the 3.2.3.0 regeneration had dropped.
PNP_FIELDS = ("licenseLevel", "topOfStackSerialNumber", "cablingScheme")


@pytest.mark.parametrize("namespace", NAMESPACES)
def test_pnp_claim_carries_the_stackswitch_fields(namespace):
    api = build(namespace, "device_onboarding_pnp", "DeviceOnboardingPnp")
    api.claim_a_device_to_a_site(
        deviceId="device-1",
        siteId="site-1",
        type="StackSwitch",
        licenseLevel="advantage",
        topOfStackSerialNumber="FOC1234X56Y",
        cablingScheme="A",
        active_validation=False,
    )
    body = api._session.calls[0]["json"]
    for field in PNP_FIELDS:
        assert field in body, f"{namespace} dropped {field} from the request body"
