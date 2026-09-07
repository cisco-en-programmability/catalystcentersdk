"""CatalystCenterAPI backup backward-compatibility alias tests.

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

from catalystcentersdk.api.v3_2_3_0.backup import Backup

# Names used by callers written against v3_1_3_0 and v3_1_6_0. See issue #64.
ALIASES = [
    ("get_all_n_f_s_configurations", "get_all_nfs_configurations"),
    ("create_n_f_s_configuration", "create_nfs_configuration"),
    ("delete_n_f_s_configuration", "delete_nfs_configuration"),
]


@pytest.mark.parametrize("alias,canonical", ALIASES)
def test_nfs_alias_resolves_to_canonical(alias, canonical):
    assert getattr(Backup, alias) is getattr(Backup, canonical)


def test_nfs_family_is_consistently_collapsed():
    for verb, name in (("get_all", "configurations"), ("create", "configuration")):
        assert hasattr(Backup, f"{verb}_nfs_{name}"), verb
    assert hasattr(Backup, "delete_nfs_configuration")
