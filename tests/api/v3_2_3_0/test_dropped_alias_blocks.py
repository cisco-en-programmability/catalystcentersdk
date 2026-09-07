"""CatalystCenterAPI tests for the alias blocks v3_2_3_0 had dropped.

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

import importlib
import re
from pathlib import Path

import pytest

# Names v3_1_6_0 kept in its `# Alias Functions` blocks and v3_2_3_0 dropped.
# See issue #62.
ALIASES = [
    (
        "cisco_imc",
        "CiscoIMC",
        "retrieves_cisco_i_m_c_configurations_for_catalyst_center_nodes",
        "retrieves_cisco_imc_configurations_for_catalyst_center_nodes",
    ),
    (
        "cisco_imc",
        "CiscoIMC",
        "adds_cisco_i_m_c_configuration_to_a_catalyst_center_node",
        "adds_cisco_imc_configuration_to_a_catalyst_center_node",
    ),
    (
        "cisco_imc",
        "CiscoIMC",
        "deletes_the_cisco_i_m_c_configuration_for_a_catalyst_center_node",
        "deletes_the_cisco_imc_configuration_for_a_catalyst_center_node",
    ),
    (
        "cisco_imc",
        "CiscoIMC",
        "retrieves_the_cisco_i_m_c_configuration_for_a_catalyst_center_node",
        "retrieves_the_cisco_imc_configuration_for_a_catalyst_center_node",
    ),
    (
        "cisco_imc",
        "CiscoIMC",
        "updates_the_cisco_i_m_c_configuration_for_a_catalyst_center_node",
        "updates_the_cisco_imc_configuration_for_a_catalyst_center_node",
    ),
    (
        "event_management",
        "EventManagement",
        "get_eventartifacts",
        "get_event_artifacts",
    ),
    ("sda", "Sda", "get_port_channels", "get_port_channels_connectivity"),
    (
        "software_image_management_swim",
        "SoftwareImageManagementSwim",
        "initiates_sync_of_software_images_from_cisco_com_v1",
        "initiates_sync_of_software_images_from_cisco_com",
    ),
    (
        "site_design",
        "SiteDesign",
        "edit_planned_access_points_positions_on_the_map",
        "edit_planned_access_points_positions",
    ),
]


def klass(module, name):
    return getattr(
        importlib.import_module(f"catalystcentersdk.api.v3_2_3_0.{module}"), name
    )


@pytest.mark.parametrize("module,cls,alias,canonical", ALIASES)
def test_alias_resolves_to_canonical(module, cls, alias, canonical):
    c = klass(module, cls)
    assert getattr(c, alias) is getattr(c, canonical)


@pytest.mark.parametrize("module,cls,alias,canonical", ALIASES)
def test_canonical_is_a_method_definition(module, cls, alias, canonical):
    """No chains: every alias target is a real def, not another alias."""
    source = Path(
        importlib.import_module(f"catalystcentersdk.api.v3_2_3_0.{module}").__file__
    ).read_text()
    assert re.search(rf"^    def {canonical}\(", source, re.M)


def test_planned_access_point_positions_family_shares_one_name():
    """The edit method carries the name its three siblings carry."""
    c = klass("site_design", "SiteDesign")
    for verb in ("add", "edit", "get"):
        assert hasattr(c, f"{verb}_planned_access_points_positions"), verb
