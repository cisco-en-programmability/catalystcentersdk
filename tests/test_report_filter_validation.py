"""CatalystCenterAPI report filter request-validation tests.

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

import copy
import importlib

import pytest

from catalystcentersdk.exceptions import MalformedRequest
from catalystcentersdk.models.schema_validator import SchemaValidator

# A report view filter carries a different `value` shape per filter type:
# MULTI_SELECT_TREE sends an array, TIME_RANGE sends an object. See issue #69.
VERSIONS = [
    ("2.3.7.6", "v2_3_7_6_1"),
    ("2.3.7.9", "v2_3_7_9"),
    ("3.1.3.0", "v3_1_3_0"),
    ("3.1.6.0", "v3_1_6_0"),
    ("3.2.3.0", "v3_2_3_0"),
]

# Versions whose request validator constrains the filter value. The others ship
# no constraint for it, so they accept any shape.
TYPED_VERSIONS = [v for v in VERSIONS if v[0] in ("2.3.7.6", "2.3.7.9", "3.1.3.0")]

LOCATION_FILTER = {
    "name": "Location",
    "displayName": "Location",
    "type": "MULTI_SELECT_TREE",
    "value": [
        {
            "value": "010cddb2-b24b-41e1-a114-2fc0a46c6016",
            "displayValue": "Global/India/Bengaluru",
        },
    ],
}
TIME_RANGE_FILTER = {
    "name": "TimeRange",
    "displayName": "Time Range",
    "type": "TIME_RANGE",
    "value": {
        "timeRangeOption": "LAST_7_DAYS",
        "startDateTime": 0,
        "endDateTime": 0,
        "timeZoneId": "Asia/Calcutta",
    },
}

REPORT = {
    "dataCategory": "AP",
    "deliveries": [{"type": "DOWNLOAD"}],
    "name": "test_ap_report",
    "schedule": {"type": "SCHEDULE_NOW", "timeZoneId": "Asia/Calcutta"},
    "tags": [],
    "view": {
        "name": "AP",
        "viewId": "8ce6-4c1d-9d88-1f52d3b1c0d2",
        "fieldGroups": [],
        "filters": [LOCATION_FILTER, TIME_RANGE_FILTER],
        "format": {"name": "CSV", "formatType": "CSV"},
    },
    "viewGroupId": "f2d7c1a4-4b7a-4b7a-9d88-1f52d3b1c0d2",
    "viewGroupVersion": "2.0.0",
}


class RecordingSession:
    """Captures the request an API method hands to the session."""

    headers = {}

    def __init__(self):
        self.calls = []

    def post(self, url, **kwargs):
        self.calls.append((url, kwargs))
        return {}


def reports_api(version, namespace):
    cls = importlib.import_module(f"catalystcentersdk.api.{namespace}.reports").Reports
    # Built without __init__ so no live RestSession is needed.
    api = cls.__new__(cls)
    api._session = RecordingSession()
    api._object_factory = lambda key, data: data
    api._request_validator = SchemaValidator(version).json_schema_validate
    return api


def create(api, report):
    return api.create_or_schedule_a_report(active_validation=True, **report)


@pytest.mark.parametrize("version,namespace", VERSIONS)
def test_multi_select_tree_filter_is_accepted(version, namespace):
    """An array-valued filter used to raise MalformedRequest before the POST."""
    api = reports_api(version, namespace)
    create(api, copy.deepcopy(REPORT))
    url, kwargs = api._session.calls[0]
    assert url == "/dna/intent/api/v1/data/reports"
    filters = kwargs["json"]["view"]["filters"]
    assert filters[0]["value"] == LOCATION_FILTER["value"]
    assert filters[1]["value"] == TIME_RANGE_FILTER["value"]


@pytest.mark.parametrize("version,namespace", VERSIONS)
def test_object_valued_filter_is_still_accepted(version, namespace):
    report = copy.deepcopy(REPORT)
    report["view"]["filters"] = [TIME_RANGE_FILTER]
    api = reports_api(version, namespace)
    create(api, report)
    assert api._session.calls


@pytest.mark.parametrize("version,namespace", TYPED_VERSIONS)
def test_filter_value_of_another_type_is_rejected(version, namespace):
    """Widening the schema must not turn it into an anything-goes schema."""
    report = copy.deepcopy(REPORT)
    report["view"]["filters"] = [
        {
            "name": "Location",
            "type": "MULTI_SELECT_TREE",
            "value": "010cddb2-b24b-41e1-a114-2fc0a46c6016",
        }
    ]
    api = reports_api(version, namespace)
    with pytest.raises(MalformedRequest):
        create(api, report)
    assert not api._session.calls
