"""Cisco Catalyst Center GetConfigurationsForASpecificInstanceOfAHaloBleConfigFeatureOnAWirelessContr
oller data model.

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


class JSONSchemaValidatorA72314057E835199A2Bb4F837674A2C6:
    """GetConfigurationsForASpecificInstanceOfAHaloBleConfigFeatureOnAWir
    elessController request schema definition."""

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
                                                "apCfgProfileName": {
                                                    "type": "string"
                                                },
                                                "configType": {
                                                    "default": "HALO_BLE",
                                                    "enum": [
                                                        "HALO_BLE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.12",
                                                    "type": "string"
                                                },
                                                "haloBleEntryBeaconId": {
                                                    "maximum": 4,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "haloBleEntryEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "haloBleEntryTxpower": {
                                                    "default": 0,
                                                    "maximum": 52,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "haloBleEntryUuid": {
                                                    "default": "00000000-0000-0000-0000-000000000000",
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "apCfgProfileName",
                                                "deviceVersion",
                                                "haloBleEntryBeaconId"
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
                                                "apCfgProfileName": {
                                                    "type": "string"
                                                },
                                                "configType": {
                                                    "default": "HALO_BLE",
                                                    "enum": [
                                                        "HALO_BLE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.13",
                                                    "type": "string"
                                                },
                                                "haloBleEntryBeaconId": {
                                                    "maximum": 4,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "haloBleEntryEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "haloBleEntryTxpower": {
                                                    "default": 0,
                                                    "maximum": 52,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "haloBleEntryUuid": {
                                                    "default": "00000000-0000-0000-0000-000000000000",
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "apCfgProfileName",
                                                "deviceVersion",
                                                "haloBleEntryBeaconId"
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
                                                "apCfgProfileName": {
                                                    "type": "string"
                                                },
                                                "configType": {
                                                    "default": "HALO_BLE",
                                                    "enum": [
                                                        "HALO_BLE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.14",
                                                    "type": "string"
                                                },
                                                "haloBleEntryBeaconId": {
                                                    "maximum": 4,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "haloBleEntryEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "haloBleEntryTxpower": {
                                                    "default": 0,
                                                    "maximum": 52,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "haloBleEntryUuid": {
                                                    "default": "00000000-0000-0000-0000-000000000000",
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "apCfgProfileName",
                                                "deviceVersion",
                                                "haloBleEntryBeaconId"
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
                                                "apCfgProfileName": {
                                                    "type": "string"
                                                },
                                                "configType": {
                                                    "default": "HALO_BLE",
                                                    "enum": [
                                                        "HALO_BLE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.15",
                                                    "type": "string"
                                                },
                                                "haloBleEntryBeaconId": {
                                                    "maximum": 4,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "haloBleEntryEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "haloBleEntryTxpower": {
                                                    "default": 0,
                                                    "maximum": 52,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "haloBleEntryUuid": {
                                                    "default": "00000000-0000-0000-0000-000000000000",
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "apCfgProfileName",
                                                "deviceVersion",
                                                "haloBleEntryBeaconId"
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
                                                "apCfgProfileName": {
                                                    "type": "string"
                                                },
                                                "configType": {
                                                    "default": "HALO_BLE",
                                                    "enum": [
                                                        "HALO_BLE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.16",
                                                    "type": "string"
                                                },
                                                "haloBleEntryBeaconId": {
                                                    "maximum": 4,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "haloBleEntryEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "haloBleEntryTxpower": {
                                                    "default": 0,
                                                    "maximum": 52,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "haloBleEntryUuid": {
                                                    "default": "00000000-0000-0000-0000-000000000000",
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "apCfgProfileName",
                                                "deviceVersion",
                                                "haloBleEntryBeaconId"
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
                                                "apCfgProfileName": {
                                                    "type": "string"
                                                },
                                                "configType": {
                                                    "default": "HALO_BLE",
                                                    "enum": [
                                                        "HALO_BLE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.17",
                                                    "type": "string"
                                                },
                                                "haloBleEntryBeaconId": {
                                                    "maximum": 4,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "haloBleEntryEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "haloBleEntryTxpower": {
                                                    "default": 0,
                                                    "maximum": 52,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "haloBleEntryUuid": {
                                                    "default": "00000000-0000-0000-0000-000000000000",
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "apCfgProfileName",
                                                "deviceVersion",
                                                "haloBleEntryBeaconId"
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
                                                "apCfgProfileName": {
                                                    "type": "string"
                                                },
                                                "configType": {
                                                    "default": "HALO_BLE",
                                                    "enum": [
                                                        "HALO_BLE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.18",
                                                    "type": "string"
                                                },
                                                "haloBleEntryBeaconId": {
                                                    "maximum": 4,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "haloBleEntryEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "haloBleEntryTxpower": {
                                                    "default": 0,
                                                    "maximum": 52,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "haloBleEntryUuid": {
                                                    "default": "00000000-0000-0000-0000-000000000000",
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "apCfgProfileName",
                                                "deviceVersion",
                                                "haloBleEntryBeaconId"
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
                                                "apCfgProfileName": {
                                                    "type": "string"
                                                },
                                                "configType": {
                                                    "default": "HALO_BLE",
                                                    "enum": [
                                                        "HALO_BLE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "26.01",
                                                    "type": "string"
                                                },
                                                "haloBleEntryBeaconId": {
                                                    "maximum": 4,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "haloBleEntryEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "haloBleEntryTxpower": {
                                                    "default": 0,
                                                    "maximum": 52,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "haloBleEntryUuid": {
                                                    "default": "00000000-0000-0000-0000-000000000000",
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "apCfgProfileName",
                                                "deviceVersion",
                                                "haloBleEntryBeaconId"
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
