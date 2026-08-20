"""Cisco Catalyst Center RetrieveTelemetrySettingsForASite data model.

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


class JSONSchemaValidatorAf4B3C5D1Dc6505CAdd13Bf41C894700:
    """RetrieveTelemetrySettingsForASite request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "properties": {
                                "applicationVisibility": {
                                    "allOf": [
                                        {
                                            "properties": {
                                                "inheritedSiteId": {
                                                    "type": "string"
                                                },
                                                "inheritedSiteName": {
                                                    "type": "string"
                                                }
                                            },
                                            "type": "object"
                                        },
                                        {
                                            "properties": {
                                                "collector": {
                                                    "allOf": [
                                                        {
                                                            "type": "object"
                                                        },
                                                        {
                                                            "oneOf": [
                                                                {
                                                                    "properties": {
                                                                        "collectorType": {
                                                                            "type": "string"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "collectorType"
                                                                    ],
                                                                    "type": "object"
                                                                },
                                                                {
                                                                    "properties": {
                                                                        "address": {
                                                                            "oneOf": [
                                                                                {
                                                                                    "type": "string"
                                                                                },
                                                                                {
                                                                                    "type": "string"
                                                                                }
                                                                            ]
                                                                        },
                                                                        "collectorType": {
                                                                            "type": "string"
                                                                        },
                                                                        "port": {
                                                                            "maximum": 65535,
                                                                            "minimum": 1,
                                                                            "type": "integer"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "address",
                                                                        "collectorType",
                                                                        "port"
                                                                    ],
                                                                    "type": "object"
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                },
                                                "enableOnWiredAccessDevices": {
                                                    "type": "boolean"
                                                }
                                            },
                                            "required": [
                                                "collector",
                                                "enableOnWiredAccessDevices"
                                            ],
                                            "type": [
                                                "object",
                                                "null"
                                            ]
                                        }
                                    ]
                                },
                                "snmpTraps": {
                                    "allOf": [
                                        {
                                            "properties": {
                                                "inheritedSiteId": {
                                                    "type": "string"
                                                },
                                                "inheritedSiteName": {
                                                    "type": "string"
                                                }
                                            },
                                            "type": "object"
                                        },
                                        {
                                            "properties": {
                                                "externalTrapServers": {
                                                    "items": {
                                                        "oneOf": [
                                                            {
                                                                "type": "string"
                                                            },
                                                            {
                                                                "type": "string"
                                                            }
                                                        ]
                                                    },
                                                    "type": "array"
                                                },
                                                "useBuiltinTrapServer": {
                                                    "type": "boolean"
                                                }
                                            },
                                            "required": [
                                                "useBuiltinTrapServer"
                                            ],
                                            "type": [
                                                "object",
                                                "null"
                                            ]
                                        }
                                    ]
                                },
                                "syslogs": {
                                    "allOf": [
                                        {
                                            "properties": {
                                                "inheritedSiteId": {
                                                    "type": "string"
                                                },
                                                "inheritedSiteName": {
                                                    "type": "string"
                                                }
                                            },
                                            "type": "object"
                                        },
                                        {
                                            "properties": {
                                                "externalSyslogServers": {
                                                    "items": {
                                                        "oneOf": [
                                                            {
                                                                "type": "string"
                                                            },
                                                            {
                                                                "type": "string"
                                                            }
                                                        ]
                                                    },
                                                    "type": "array"
                                                },
                                                "useBuiltinSyslogServer": {
                                                    "type": "boolean"
                                                }
                                            },
                                            "required": [
                                                "useBuiltinSyslogServer"
                                            ],
                                            "type": [
                                                "object",
                                                "null"
                                            ]
                                        }
                                    ]
                                },
                                "wiredDataCollection": {
                                    "allOf": [
                                        {
                                            "properties": {
                                                "inheritedSiteId": {
                                                    "type": "string"
                                                },
                                                "inheritedSiteName": {
                                                    "type": "string"
                                                }
                                            },
                                            "type": "object"
                                        },
                                        {
                                            "properties": {
                                                "enableWiredDataCollection": {
                                                    "type": "boolean"
                                                }
                                            },
                                            "required": [
                                                "enableWiredDataCollection"
                                            ],
                                            "type": [
                                                "object",
                                                "null"
                                            ]
                                        }
                                    ]
                                },
                                "wirelessTelemetry": {
                                    "allOf": [
                                        {
                                            "properties": {
                                                "inheritedSiteId": {
                                                    "type": "string"
                                                },
                                                "inheritedSiteName": {
                                                    "type": "string"
                                                }
                                            },
                                            "type": "object"
                                        },
                                        {
                                            "properties": {
                                                "enableWirelessTelemetry": {
                                                    "type": "boolean"
                                                }
                                            },
                                            "required": [
                                                "enableWirelessTelemetry"
                                            ],
                                            "type": [
                                                "object",
                                                "null"
                                            ]
                                        }
                                    ]
                                }
                            },
                            "required": [
                                "applicationVisibility",
                                "snmpTraps",
                                "syslogs",
                                "wiredDataCollection",
                                "wirelessTelemetry"
                            ],
                            "type": "object"
                        },
                        "version": {
                            "type": "string"
                        }
                    },
                    "type": "object"
                }""".replace("\n" + " " * 16, "")))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                "{} is invalid. Reason: {}".format(request, e.message)
            )
