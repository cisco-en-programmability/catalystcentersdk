"""CatalystCenterAPI sites v1/v2 binding tests.

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

import catalystcentersdk.api.v3_2_3_0.sites as module

SOURCE = Path(module.__file__).read_text()

# The plain name is the v1 operation, as it was up to 3.1.6.0.7; the v2 operation
# is the `_v2` name. See issue #61.
ENDPOINTS = [
    ("get_site", "/dna/intent/api/v1/site"),
    ("get_site_v2", "/dna/intent/api/v2/site"),
    ("get_site_count", "/dna/intent/api/v1/site/count"),
    ("get_site_count_v2", "/dna/intent/api/v2/site/count"),
]

# The filter keywords each operation accepts. A caller that passes `name` to the
# v2 operation gets it absorbed by **request_parameters and dropped by the
# endpoint, which is what made the repointing silent.
FILTERS = [
    ("get_site", ["name", "site_id"]),
    ("get_site_v2", ["group_name_hierarchy", "id"]),
    ("get_site_count", ["site_id"]),
    ("get_site_count_v2", ["id"]),
]


def endpoint_of(method_name):
    """The e_url a method builds, read out of the generated source."""
    body = SOURCE[SOURCE.index(f"    def {method_name}(") :]
    chunk = body[body.index("e_url = ") : body.index("endpoint_full_url")]
    return "".join(re.findall(r'"([^"]*)"', chunk))


@pytest.mark.parametrize("method,endpoint", ENDPOINTS)
def test_method_calls_expected_endpoint(method, endpoint):
    assert endpoint_of(method) == endpoint


@pytest.mark.parametrize("method,filters", FILTERS)
def test_method_declares_its_filter_keywords(method, filters):
    params = inspect.signature(getattr(module.Sites, method)).parameters
    for name in filters:
        assert name in params, f"{method} should accept {name}"


def test_v2_filters_are_not_silently_accepted_by_name():
    """`name` and `site_id` belong to v1 only, `group_name_hierarchy` to v2 only."""
    v1 = inspect.signature(module.Sites.get_site).parameters
    v2 = inspect.signature(module.Sites.get_site_v2).parameters
    assert "group_name_hierarchy" not in v1
    assert "name" not in v2
    assert "site_id" not in v2
