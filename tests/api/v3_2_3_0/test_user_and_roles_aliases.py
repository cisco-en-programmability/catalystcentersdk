"""CatalystCenterAPI user_and_roles backward-compatibility alias tests.

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

from catalystcentersdk.api.v3_2_3_0 import user_and_roles

# The short spellings v3_1_6_0 introduced, kept as aliases of the `_api` names
# the family has carried since v2_3_7_6_1. See issue #62.
ALIASES = [
    ("get_users", "get_users_api"),
    ("add_user", "add_user_api"),
    ("update_user", "update_user_api"),
]


@pytest.mark.parametrize("alias,canonical", ALIASES)
def test_user_alias_resolves_to_canonical(alias, canonical):
    cls = user_and_roles.UserAndRoles
    assert getattr(cls, alias) is getattr(cls, canonical)


def test_old_class_spelling_is_the_class():
    assert user_and_roles.UserandRoles is user_and_roles.UserAndRoles


def test_user_family_keeps_both_spellings():
    """Every operation is reachable by both spellings, delete excepted."""
    cls = user_and_roles.UserAndRoles
    for name in (
        "get_users",
        "get_users_api",
        "add_user",
        "add_user_api",
        "update_user",
        "update_user_api",
        "delete_user_api",
    ):
        assert hasattr(cls, name), name
