"""CatalystCenterAPI application_policy v1/v2 binding tests.

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

import inspect
import re
from pathlib import Path

import pytest

import catalystcentersdk.api.v3_2_3_0.application_policy as module

SOURCE = Path(module.__file__).read_text()

# The plain name is the v1 operation, as it was up to 3.1.6.0.7; the v2 operation
# is the `_v2` name. See issue #59.
ENDPOINTS = [
    ("get_application_sets", "/dna/intent/api/v1/application-policy-application-set"),
    (
        "get_application_sets_v2",
        "/dna/intent/api/v2/application-policy-application-set",
    ),
    ("get_applications", "/dna/intent/api/v1/applications"),
    ("get_applications_v2", "/dna/intent/api/v2/applications"),
    (
        "delete_application_set",
        "/dna/intent/api/v1/application-policy-application-set",
    ),
    (
        "delete_application_set_v2",
        "/dna/intent/api/v2/application-policy-application-set/{id}",
    ),
    ("delete_application", "/dna/intent/api/v1/applications"),
    ("delete_application_v2", "/dna/intent/api/v2/applications/{id}"),
]


def endpoint_of(method_name):
    """The e_url a method builds, read out of the generated source."""
    body = SOURCE[SOURCE.index(f"    def {method_name}(") :]
    chunk = body[body.index("e_url = ") : body.index("endpoint_full_url")]
    return "".join(re.findall(r'"([^"]*)"', chunk))


@pytest.mark.parametrize("method,endpoint", ENDPOINTS)
def test_method_calls_expected_endpoint(method, endpoint):
    assert endpoint_of(method) == endpoint


@pytest.mark.parametrize("method", ["get_application_sets", "get_applications"])
def test_plain_get_takes_no_required_arguments(method):
    params = inspect.signature(getattr(module.ApplicationPolicy, method)).parameters
    required = [
        name
        for name, p in params.items()
        if name != "self"
        and p.default is inspect.Parameter.empty
        and p.kind is not inspect.Parameter.VAR_KEYWORD
    ]
    assert required == []
    assert "attributes" not in params


@pytest.mark.parametrize("method", ["get_application_sets_v2", "get_applications_v2"])
def test_v2_get_takes_the_v2_arguments(method):
    params = inspect.signature(getattr(module.ApplicationPolicy, method)).parameters
    for name in ("attributes", "limit", "offset"):
        assert params[name].default is inspect.Parameter.empty
