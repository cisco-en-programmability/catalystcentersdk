"""Cisco Catalyst Center GetConfigurationsForASpecificInstanceOfARfMcsConfigFeatureOnAWirelessControl
lerConnectivity data model.

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


class JSONSchemaValidatorC46F4D3356Ba568DAbbdE4Ca2A1A1506:
    """GetConfigurationsForASpecificInstanceOfARfMcsConfigFeatureOnAWirel
    essControllerConnectivity request schema definition."""

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
                                                    "default": "RF_MCS",
                                                    "enum": [
                                                        "RF_MCS"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.12",
                                                    "type": "string"
                                                },
                                                "rfMcsEntryRf80211NMcsEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "rfMcsEntryRfIndex": {
                                                    "maximum": 31,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "rfProfileName": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "deviceVersion",
                                                "rfMcsEntryRfIndex",
                                                "rfProfileName"
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
                                                    "default": "RF_MCS",
                                                    "enum": [
                                                        "RF_MCS"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.13",
                                                    "type": "string"
                                                },
                                                "rfMcsEntryRf80211NMcsEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "rfMcsEntryRfIndex": {
                                                    "maximum": 31,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "rfProfileName": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "deviceVersion",
                                                "rfMcsEntryRfIndex",
                                                "rfProfileName"
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
                                                    "default": "RF_MCS",
                                                    "enum": [
                                                        "RF_MCS"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.14",
                                                    "type": "string"
                                                },
                                                "rfMcsEntryRf80211NMcsEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "rfMcsEntryRfIndex": {
                                                    "maximum": 31,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "rfProfileName": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "deviceVersion",
                                                "rfMcsEntryRfIndex",
                                                "rfProfileName"
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
                                                    "default": "RF_MCS",
                                                    "enum": [
                                                        "RF_MCS"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.15",
                                                    "type": "string"
                                                },
                                                "rfMcsEntryRf80211NMcsEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "rfMcsEntryRfIndex": {
                                                    "maximum": 31,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "rfProfileName": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "deviceVersion",
                                                "rfMcsEntryRfIndex",
                                                "rfProfileName"
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
                                                    "default": "RF_MCS",
                                                    "enum": [
                                                        "RF_MCS"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.16",
                                                    "type": "string"
                                                },
                                                "rfMcsEntryRf80211NMcsEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "rfMcsEntryRfIndex": {
                                                    "maximum": 31,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "rfProfileName": {
                                                    "maxLength": 32,
                                                    "minLength": 1,
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "deviceVersion",
                                                "rfMcsEntryRfIndex",
                                                "rfProfileName"
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
                                                    "default": "RF_MCS",
                                                    "enum": [
                                                        "RF_MCS"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.17",
                                                    "type": "string"
                                                },
                                                "rfMcsEntryRf80211NMcsEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "rfMcsEntryRfIndex": {
                                                    "maximum": 31,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "rfProfileName": {
                                                    "maxLength": 32,
                                                    "minLength": 1,
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "deviceVersion",
                                                "rfMcsEntryRfIndex",
                                                "rfProfileName"
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
                                                    "default": "RF_MCS",
                                                    "enum": [
                                                        "RF_MCS"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.18",
                                                    "type": "string"
                                                },
                                                "rfMcsEntryRf80211NMcsEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "rfMcsEntryRfIndex": {
                                                    "maximum": 31,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "rfProfileName": {
                                                    "maxLength": 32,
                                                    "minLength": 1,
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "deviceVersion",
                                                "rfMcsEntryRfIndex",
                                                "rfProfileName"
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
                                                    "default": "RF_MCS",
                                                    "enum": [
                                                        "RF_MCS"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "26.01",
                                                    "type": "string"
                                                },
                                                "rfMcsEntryRf80211NMcsEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "rfMcsEntryRfIndex": {
                                                    "maximum": 31,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "rfProfileName": {
                                                    "maxLength": 32,
                                                    "minLength": 1,
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "deviceVersion",
                                                "rfMcsEntryRfIndex",
                                                "rfProfileName"
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
