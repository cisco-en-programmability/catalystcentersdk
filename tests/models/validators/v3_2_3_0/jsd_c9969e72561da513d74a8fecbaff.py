"""Cisco Catalyst Center GetApProfileByID data model.

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


class JSONSchemaValidatorC9969E72561DA513D74A8Fecbaff:
    """GetApProfileByID request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "profile": {
                            "properties": {
                                "apPowerProfileName": {
                                    "default": "default_power_profile",
                                    "type": "string"
                                },
                                "apProfileName": {
                                    "default": "default_ap_profile",
                                    "maxLength": 32,
                                    "minLength": 1,
                                    "type": "string"
                                },
                                "awipsEnabled": {
                                    "default": false,
                                    "type": "boolean"
                                },
                                "awipsForensicEnabled": {
                                    "default": false,
                                    "type": "boolean"
                                },
                                "calendarPowerProfiles": {
                                    "default": [],
                                    "items": {
                                        "properties": {
                                            "apPowerProfileName": {
                                                "default": "Default AP Power Profile",
                                                "type": "string"
                                            },
                                            "calendarProfileName": {
                                                "default": "Default Calendar Profile",
                                                "type": "string"
                                            },
                                            "duration": {
                                                "properties": {
                                                    "schedulerDate": {
                                                        "items": {
                                                            "type": "string"
                                                        },
                                                        "type": "array"
                                                    },
                                                    "schedulerDay": {
                                                        "items": {
                                                            "type": "string"
                                                        },
                                                        "type": "array"
                                                    },
                                                    "schedulerEndTime": {
                                                        "type": "string"
                                                    },
                                                    "schedulerStartTime": {
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "schedulerEndTime",
                                                    "schedulerStartTime"
                                                ],
                                                "type": "object"
                                            },
                                            "schedulerType": {
                                                "default": "DAILY",
                                                "enum": [
                                                    "DAILY",
                                                    "WEEKLY",
                                                    "MONTHLY"
                                                ],
                                                "type": "string"
                                            }
                                        },
                                        "required": [
                                            "apPowerProfileName",
                                            "calendarProfileName",
                                            "duration",
                                            "schedulerType"
                                        ],
                                        "type": "object"
                                    },
                                    "type": "array"
                                },
                                "clientLimit": {
                                    "default": 100,
                                    "type": "integer"
                                },
                                "countryCode": {
                                    "maxLength": 2,
                                    "minLength": 2,
                                    "type": "string"
                                },
                                "description":
                 {
                                    "maxLength": 241,
                                    "minLength": 0,
                                    "type": "string"
                                },
                                "id": {
                                    "default": "Default_Id",
                                    "type": "string"
                                },
                                "managementSetting": {
                                    "properties": {
                                        "authType": {
                                            "default": "NO-AUTH",
                                            "enum": [
                                                "NO-AUTH",
                                                "EAP-TLS",
                                                "EAP-PEAP",
                                                "EAP-FAST"
                                            ],
                                            "type": "string"
                                        },
                                        "cdpState": {
                                            "default": true,
                                            "type": "boolean"
                                        },
                                        "dot1xPassword": {
                                            "default": "default_password",
                                            "maxLength": 120,
                                            "maximum": 120,
                                            "minLength": 8,
                                            "type": "string"
                                        },
                                        "dot1xUsername": {
                                            "default": "default_username",
                                            "type": "string"
                                        },
                                        "managementEnablePassword": {
                                            "default": "default_enable_password",
                                            "type": "string"
                                        },
                                        "managementPassword": {
                                            "default": "default_management_password",
                                            "type": "string"
                                        },
                                        "managementUserName": {
                                            "default": "Cisco",
                                            "type": "string"
                                        },
                                        "sshEnabled": {
                                            "default": false,
                                            "type": "boolean"
                                        },
                                        "telnetEnabled": {
                                            "default": false,
                                            "type": "boolean"
                                        }
                                    },
                                    "type": "object"
                                },
                                "meshEnabled": {
                                    "default": true,
                                    "type": "boolean"
                                },
                                "meshSetting": {
                                    "properties": {
                                        "backhaulClientAccess": {
                                            "default": false,
                                            "type": "boolean"
                                        },
                                        "bridgeGroupName": {
                                            "default": "default",
                                            "maximum": 10,
                                            "minimum": 1,
                                            "type": "string"
                                        },
                                        "ghz24BackhaulDataRates": {
                                            "default": "auto",
                                            "enum": [
                                                "auto",
                                                "802.11abg",
                                                "802.11ax",
                                                "802.11n"
                                            ],
                                            "type": "string"
                                        },
                                        "ghz5BackhaulDataRates": {
                                            "default": "auto",
                                            "enum": [
                                                "auto",
                                                "802.11abg",
                                                "802.12ac",
                                                "802.11ax",
                                                "802.11n"
                                            ],
                                            "type": "string"
                                        },
                                        "range": {
                                            "maximum": 132000,
                                            "minimum": 150,
                                            "type": "integer"
                                        },
                                        "rapDownlinkBackhaul": {
                                            "default": "5 GHz",
                                            "enum": [
                                                "5 GHz",
                                                "2.4 GHz"
                                            ],
                                            "type": "string"
                                        }
                                    },
                                    "type": "object"
                                },
                                "pmfDenialEnabled": {
                                    "default": false,
                                    "type": "boolean"
                                },
                                "remoteWorkerEnabled": {
                                    "default": false,
                                    "type": "boolean"
                                },
                                "rogueDetectionSetting": {
                                    "properties": {
                                        "rogueDetection": {
                                            "default": true,
                                            "type": "boolean"
                                        },
                                        "rogueDetectionMinRssi": {
                                            "type": "integer"
                                        },
                                        "rogueDetectionReportInterval": {
                                            "default": 10,
                                            "type": "integer"
                                        },
                                        "rogueDetectionTransientInterval": {
                                            "default": 5,
                                            "type": "integer"
                                        }
                                    },
                                    "type": "object"
                                },
                                "timeZone": {
                                    "default": "Not Configured",
                                    "enum": [
                                        "Not Configured",
                                        "Controller",
                                        "Delta from Controller"
                                    ],
                                    "type": "string"
                                },
                                "timeZoneOffsetHour": {
                                    "default": 0,
                                    "type": "integer"
                                },
                                "timeZoneOffsetMinutes": {
                                    "default": 0,
                                    "type": "integer"
                                }
                            },
                            "required": [
                                "apProfileName"
                            ],
                            "type": "object"
                        },
                        "version": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "profile"
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
