"""CatalystCenterAPI network_settings backward-compatibility alias tests.

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

import pytest

from catalystcentersdk.api.v3_2_3_0.network_settings import NetworkSettings

# Names used by callers written against 3.1.6.0.x, mapped to their 3.2.3.0
# canonical method. See issue #58.
ALIASES = [
    ("retrieve_d_h_c_p_settings_for_a_site", "retrieve_dhcp_settings_for_a_site"),
    ("retrieve_d_n_s_settings_for_a_site", "retrieve_dns_settings_for_a_site"),
    ("retrieve_n_t_p_settings_for_a_site", "retrieve_ntp_settings_for_a_site"),
    ("set_d_n_s_settings_for_a_site", "set_dns_settings_for_a_site"),
    ("set_n_t_p_settings_for_a_site", "set_ntp_settings_for_a_site"),
]


@pytest.mark.parametrize("alias,canonical", ALIASES)
def test_network_settings_alias_resolves_to_canonical(alias, canonical):
    assert getattr(NetworkSettings, alias) is getattr(NetworkSettings, canonical)


def test_site_settings_family_naming_is_consistent():
    for protocol in ("dhcp", "dns", "ntp"):
        assert hasattr(NetworkSettings, f"retrieve_{protocol}_settings_for_a_site")
        assert hasattr(NetworkSettings, f"set_{protocol}_settings_for_a_site")
