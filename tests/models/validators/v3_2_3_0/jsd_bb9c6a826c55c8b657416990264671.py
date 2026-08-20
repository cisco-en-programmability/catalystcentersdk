"""Cisco Catalyst Center GetConfigurationsForASpecificInstanceOfAIfNameVlanIdConfigFeatureOnAWireless
Controller data model.

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

import json

import fastjsonschema

from catalystcentersdk.exceptions import MalformedRequest


class JSONSchemaValidatorBb9C6A826C55C8B657416990264671:
    """GetConfigurationsForASpecificInstanceOfAIfNameVlanIdConfigFeatureO
    nAWirelessController request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "oneOf": [
                                {
                                    "allOf": [
                                        {
                                            "properties": {
                                                "id": {
                                                    "type": "string"
                                                }
                                            },
                                            "type": "object"
                                        },
                                        {
                                            "properties": {
                                                "configType": {
                                                    "default": "INTERFACE_NAME_VLAN_ID",
                                                    "enum": [
                                                        "INTERFACE_NAME_VLAN_ID"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.12",
                                                    "type": "string"
                                                },
                                                "flexPolicyName": {
                                                    "type": "string"
                                                },
                                                "ifNameVlanId": {
                                                    "default": 1,
                                                    "maximum": 4096,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "ifNameVlanIdAclName": {
                                                    "type": "string"
                                                },
                                                "ifNameVlanIdAclNameIn": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "ifNameVlanIdAclNameOut": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "ifNameVlanIdInterfaceName": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "deviceVersion",
                                                "flexPolicyName",
                                                "ifNameVlanIdInterfaceName"
                                            ]
                                        }
                                    ],
                                    "type": "object"
                                },
                                {
                                    "allOf": [
                                        {
                                            "properties": {
                                                "id": {
                                                    "type": "string"
                                                }
                                            },
                                            "type": "object"
                                        },
                                        {
                                            "properties": {
                                                "configType": {
                                                    "default": "INTERFACE_NAME_VLAN_ID",
                                                    "enum": [
                                                        "INTERFACE_NAME_VLAN_ID"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.13",
                                                    "type": "string"
                                                },
                                                "flexPolicyName": {
                                                    "type": "string"
                                                },
                                                "ifNameVlanId": {
                                                    "default": 1,
                                                    "maximum": 4096,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "ifNameVlanIdAclName": {
                                                    "type": "string"
                                                },
                                                "ifNameVlanIdAclNameIn": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "ifNameVlanIdAclNameOut": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "ifNameVlanIdInterfaceName": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "deviceVersion",
                                                "flexPolicyName",
                                                "ifNameVlanIdInterfaceName"
                                            ]
                                        }
                                    ],
                                    "type": "object"
                                },
                                {
                                    "allOf": [
                                        {
                                            "properties": {
                                                "id": {
                                                    "type": "string"
                                                }
                                            },
                                            "type": "object"
                                        },
                                        {
                                            "properties": {
                                                "configType": {
                                                    "default": "INTERFACE_NAME_VLAN_ID",
                                                    "enum": [
                                                        "INTERFACE_NAME_VLAN_ID"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.14",
                                                    "type": "string"
                                                },
                                                "flexPolicyName": {
                                                    "type": "string"
                                                },
                                                "ifNameVlanId": {
                                                    "default": 1,
                                                    "maximum": 4096,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "ifNameVlanIdAclName": {
                                                    "type": "string"
                                                },
                                                "ifNameVlanIdAclNameIn": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "ifNameVlanIdAclNameOut": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "ifNameVlanIdInterfaceName": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "deviceVersion",
                                                "flexPolicyName",
                                                "ifNameVlanIdInterfaceName"
                                            ]
                                        }
                                    ],
                                    "type": "object"
                                },
                                {
                                    "allOf": [
                                        {
                                            "properties": {
                                                "id": {
                                                    "type": "string"
                                                }
                                            },
                                            "type": "object"
                                        },
                                        {
                                            "properties": {
                                                "configType": {
                                                    "default": "INTERFACE_NAME_VLAN_ID",
                                                    "enum": [
                                                        "INTERFACE_NAME_VLAN_ID"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.15",
                                                    "type": "string"
                                                },
                                                "flexPolicyName": {
                                                    "type": "string"
                                                },
                                                "ifNameVlanId": {
                                                    "default": 1,
                                                    "maximum": 4096,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "ifNameVlanIdAclName": {
                                                    "type": "string"
                                                },
                                                "ifNameVlanIdAclNameIn": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "ifNameVlanIdAclNameOut": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "ifNameVlanIdInterfaceName": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "deviceVersion",
                                                "flexPolicyName",
                                                "ifNameVlanIdInterfaceName"
                                            ]
                                        }
                                    ],
                                    "type": "object"
                                },
                                {
                                    "allOf": [
                                        {
                                            "properties": {
                                                "id": {
                                                    "type": "string"
                                                }
                                            },
                                            "type": "object"
                                        },
                                        {
                                            "properties": {
                                                "configType": {
                                                    "default": "INTERFACE_NAME_VLAN_ID",
                                                    "enum": [
                                                        "INTERFACE_NAME_VLAN_ID"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.16",
                                                    "type": "string"
                                                },
                                                "flexPolicyName": {
                                                    "type": "string"
                                                },
                                                "ifNameVlanId": {
                                                    "default": 1,
                                                    "maximum": 4096,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "ifNameVlanIdAclName": {
                                                    "type": "string"
                                                },
                                                "ifNameVlanIdAclNameIn": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "ifNameVlanIdAclNameOut": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "ifNameVlanIdInterfaceName": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "deviceVersion",
                                                "flexPolicyName",
                                                "ifNameVlanIdInterfaceName"
                                            ]
                                        }
                                    ],
                                    "type": "object"
                                },
                                {
                                    "allOf": [
                                        {
                                            "properties": {
                                                "id": {
                                                    "type": "string"
                                                }
                                            },
                                            "type": "object"
                                        },
                                        {
                                            "properties": {
                                                "configType": {
                                                    "default": "INTERFACE_NAME_VLAN_ID",
                                                    "enum": [
                                                        "INTERFACE_NAME_VLAN_ID"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.17",
                                                    "type": "string"
                                                },
                                                "flexPolicyName": {
                                                    "type": "string"
                                                },
                                                "ifNameVlanId": {
                                                    "default": 1,
                                                    "maximum": 4096,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "ifNameVlanIdAclName": {
                                                    "type": "string"
                                                },
                                                "ifNameVlanIdAclNameIn": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "ifNameVlanIdAclNameOut": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "ifNameVlanIdInterfaceName": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "deviceVersion",
                                                "flexPolicyName",
                                                "ifNameVlanIdInterfaceName"
                                            ]
                                        }
                                    ],
                                    "type": "object"
                                },
                                {
                                    "allOf": [
                                        {
                                            "properties": {
                                                "id": {
                                                    "type": "string"
                                                }
                                            },
                                            "type": "object"
                                        },
                                        {
                                            "properties": {
                                                "configType": {
                                                    "default": "INTERFACE_NAME_VLAN_ID",
                                                    "enum": [
                                                        "INTERFACE_NAME_VLAN_ID"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.18",
                                                    "type": "string"
                                                },
                                                "flexPolicyName": {
                                                    "type": "string"
                                                },
                                                "ifNameVlanId": {
                                                    "default": 1,
                                                    "maximum": 4096,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "ifNameVlanIdAclName": {
                                                    "type": "string"
                                                },
                                                "ifNameVlanIdAclNameIn": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "ifNameVlanIdAclNameOut": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "ifNameVlanIdInterfaceName": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "deviceVersion",
                                                "flexPolicyName",
                                                "ifNameVlanIdInterfaceName"
                                            ]
                                        }
                                    ],
                                    "type": "object"
                                },
                                {
                                    "allOf": [
                                        {
                                            "properties": {
                                                "id": {
                                                    "type": "string"
                                                }
                                            },
                                            "type": "object"
                                        },
                                        {
                                            "properties": {
                                                "configType": {
                                                    "default": "INTERFACE_NAME_VLAN_ID",
                                                    "enum": [
                                                        "INTERFACE_NAME_VLAN_ID"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "26.01",
                                                    "type": "string"
                                                },
                                                "flexPolicyName": {
                                                    "type": "string"
                                                },
                                                "ifNameVlanId": {
                                                    "default": 1,
                                                    "maximum": 4096,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "ifNameVlanIdAclName": {
                                                    "type": "string"
                                                },
                                                "ifNameVlanIdAclNameIn": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "ifNameVlanIdAclNameOut": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "ifNameVlanIdInterfaceName": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "deviceVersion",
                                                "flexPolicyName",
                                                "ifNameVlanIdInterfaceName"
                                            ]
                                        }
                                    ],
                                    "type": "object"
                                }
                            ]
                        },
                        "version": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "response",
                        "version"
                    ],
                    "type": "object"
                }""".replace("\n" + " " * 16, "")))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                "{} is invalid. Reason: {}".format(request, e.message)
            )
