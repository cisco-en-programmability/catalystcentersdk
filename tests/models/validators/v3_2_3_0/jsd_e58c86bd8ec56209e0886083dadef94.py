"""Cisco Catalyst Center RetrieveAccessPointDetails data model.

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


class JSONSchemaValidatorE58C86BD8Ec56209E0886083Dadef94:
    """RetrieveAccessPointDetails request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "allOf": [
                                {
                                    "properties": {
                                        "accessPointConfigurations": {
                                            "items": {
                                                "properties": {
                                                    "accelerometerConfiguration": {
                                                        "properties": {
                                                            "apTiltAngle": {
                                                                "type": "integer"
                                                            },
                                                            "xCoordinate": {
                                                                "type": "integer"
                                                            },
                                                            "yCoordinate": {
                                                                "type": "integer"
                                                            },
                                                            "zCoordinate": {
                                                                "type": "integer"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "accelerometerStateEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "accessPointCertificateExpiryTime": {
                                                        "type": [
                                                            "integer",
                                                            "null"
                                                        ]
                                                    },
                                                    "accessPointCertificateUsage": {
                                                        "type": [
                                                            "string",
                                                            "null"
                                                        ]
                                                    },
                                                    "accessPointJoinProfile": {
                                                        "type": [
                                                            "string",
                                                            "null"
                                                        ]
                                                    },
                                                    "adminStatus": {
                                                        "type": "boolean"
                                                    },
                                                    "cleanAirSI24": {
                                                        "type": "string"
                                                    },
                                                    "cleanAirSI5": {
                                                        "type": "string"
                                                    },
                                                    "cleanAirSI6": {
                                                        "type": "string"
                                                    },
                                                    "deviceId": {
                                                        "type": "string"
                                                    },
                                                    "dnsIpAddress": {
                                                        "oneOf": [
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "type": "string"
                                                                    },
                                                                    {}
                                                                ]
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "type": "string"
                                                                    },
                                                                    {}
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    "domainName": {
                                                        "type": [
                                                            "string",
                                                            "null"
                                                        ]
                                                    },
                                                    "ethernetMac": {
                                                        "type": "string"
                                                    },
                                                    "failoverPriority": {
                                                        "enum": [
                                                            "LOW",
                                                            "MEDIUM",
                                                            "HIGH",
                                                            "CRITICAL"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "flexProfile": {
                                                        "type": [
                                                            "string",
                                                            "null"
                                                        ]
                                                    },
                                                    "geolocationConfiguration": {
                                                        "properties": {
                                                            "cableLength": {
                                                                "type": "integer"
                                                            },
                                                            "cableLengthSupported": {
                                                                "type": "boolean"
                                                            },
                                                            "geolocationHeight": {
                                                                "type": [
                                                                    "integer",
                                                                    "null"
                                                                ]
                                                            },
                                                            "geolocationHeightUncertainty": {
                                                                "type": [
                                                                    "integer",
                                                                    "null"
                                                                ]
                                                            },
                                                            "geolocationSupported": {
                                                                "type": "boolean"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "lanPortConfigurations": {
                                                        "items": {
                                                            "properties": {
                                                                "poeStatus": {
                                                                    "type": "boolean"
                                                                },
                                                                "portId": {
                                                                    "type": "integer"
                                                                },
                                                                "portStatus": {
                                                                    "type": "boolean"
                                                                }
                                                            },
                                                            "type": "object"
                                                        },
                                                        "maxItems": 3,
                                                        "type": "array"
                                                    },
                                                    "ledBrightnessLevel": {
                                                        "type": "integer"
                                                    },
                                                    "ledStatus": {
                                                        "type": "boolean"
                                                    },
                                                    "location": {
                                                        "type": [
                                                            "string",
                                                            "null"
                                                        ]
                                                    },
                                                    "locationHierarchy": {
                                                        "type": "string"
                                                    },
                                                    "macAddress": {
                                                        "type": "string"
                                                    },
                                                    "managementIpAddress": {
                                                        "oneOf": [
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "type": "string"
                                                                    },
                                                                    {}
                                                                ]
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "type": "string"
                                                                    },
                                                                    {}
                                                                ]
                                                            },
                                                            {
                                                                "type": "null"
                                                            }
                                                        ]
                                                    },
                                                    "meshConfigurations": {
                                                        "properties": {
                                                            "backhaulClientAccess": {
                                                                "type": "boolean"
                                                            },
                                                            "backhaulRate24Ghz": {
                                                                "type": "string"
                                                            },
                                                            "backhaulRate5Ghz": {
                                                                "type": "string"
                                                            },
                                                            "meshGroupName": {
                                                                "type": "string"
                                                            },
                                                            "meshNativeVlanId": {
                                                                "type": "integer"
                                                            },
                                                            "meshRole": {
                                                                "type": "string"
                                                            },
                                                            "meshVlan": {
                                                                "type": "boolean"
                                                            },
                                                            "range": {
                                                                "type": "string"
                                                            },
                                                            "rapDownlinkBackhaul": {
                                                                "type": "string"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "mode": {
                                                        "enum": [
                                                            "LOCAL",
                                                            "MONITOR",
                                                            "FLEXCONNECT",
                                                            "ROGUE_DETECTOR",
                                                            "SNIFFER",
                                                            "BRIDGE",
                                                            "SE_CONNECT",
                                                            "FLEX_BRIDGE",
                                                            "REMOTE_HYBRID",
                                                            "SENSOR",
                                                            "FLEX_LOCAL",
                                                            "UNKNOWN"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "model": {
                                                        "type": "string"
                                                    },
                                                    "name": {
                                                        "type": [
                                                            "string",
                                                            "null"
                                                        ]
                                                    },
                                                    "policyTag": {
                                                        "type": [
                                                            "string",
                                                            "null"
                                                        ]
                                                    },
                                                    "primaryControllerIpAddress": {
                                                        "oneOf": [
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "type": "string"
                                                                    },
                                                                    {}
                                                                ]
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "type": "string"
                                                                    },
                                                                    {}
                                                                ]
                                                            },
                                                            {
                                                                "type": "null"
                                                            }
                                                        ]
                                                    },
                                                    "primaryControllerName": {
                                                        "type": [
                                                            "string",
                                                            "null"
                                                        ]
                                                    },
                                                    "provisioningStatus": {
                                                        "type": [
                                                            "boolean",
                                                            "null"
                                                        ]
                                                    },
                                                    "radioConfigurations": {
                                                        "items": {
                                                            "properties": {
                                                                "adminStatus": {
                                                                    "type": "boolean"
                                                                },
                                                                "antennaGain": {
                                                                    "type": "integer"
                                                                },
                                                                "antennaName": {
                                                                    "type": [
                                                                        "string",
                                                                        "null"
                                                                    ]
                                                                },
                                                                "bssColor": {
                                                                    "type": "integer"
                                                                },
                                                                "bssColorAssignmentMode": {
                                                                    "enum": [
                                                                        "Global",
                                                                        "Custom",
                                                                        "Unknown"
                                                                    ],
                                                                    "type": "string"
                                                                },
                                                                "bssColorRadioAdminStatus": {
                                                                    "type": "boolean"
                                                                },
                                                                "channelAssignmentMode": {
                                                                    "enum": [
                                                                        "Global",
                                                                        "Custom",
                                                                        "Unknown"
                                                                    ],
                                                                    "type": "string"
                                                                },
                                                                "channelNumber": {
                                                                    "type": "integer"
                                                                },
                                                                "channelWidth": {
                                                                    "enum": [
                                                                        "20 MHz",
                                                                        "40 MHz",
                                                                        "80 MHz",
                                                                        "160 MHz",
                                                                        "320 MHz",
                                                                        "Unknown"
                                                                    ],
                                                                    "type": [
                                                                        "string",
                                                                        "null"
                                                                    ]
                                                                },
                                                                "dualRadioMode": {
                                                                    "enum": [
                                                                        "Auto",
                                                                        "Enabled",
                                                                        "Disabled"
                                                                    ],
                                                                    "type": [
                                                                        "string",
                                                                        "null"
                                                                    ]
                                                                },
                                                                "macAddress": {
                                                                    "type": "string"
                                                                },
                                                                "powerAssignmentMode": {
                                                                    "enum": [
                                                                        "Global",
                                                                        "Custom",
                                                                        "Unknown"
                                                                    ],
                                                                    "type": "string"
                                                                },
                                                                "powerLevel": {
                                                                    "type": "integer"
                                                                },
                                                                "radioBand": {
                                                                    "enum": [
                                                                        "2.4 GHz",
                                                                        "5 GHz",
                                                                        "6 GHz",
                                                                        "Unknown"
                                                                    ],
                                                                    "type": [
                                                                        "string",
                                                                        "null"
                                                                    ]
                                                                },
                                                                "radioRoleAssignment": {
                                                                    "enum": [
                                                                        "Auto",
                                                                        "Client-Serving",
                                                                        "Monitor",
                                                                        "Sniffer",
                                                                        "URWB",
                                                                        "Unknown"
                                                                    ],
                                                                    "type": "string"
                                                                },
                                                                "radioType": {
                                                                    "type": "string"
                                                                },
                                                                "slotId": {
                                                                    "type": "integer"
                                                                }
                                                            },
                                                            "type": "object"
                                                        },
                                                        "maxItems": 5,
                                                        "type": "array"
                                                    },
                                                    "reachabilityStatus": {
                                                        "type": [
                                                            "boolean",
                                                            "null"
                                                        ]
                                                    },
                                                    "rfTag": {
                                                        "type": [
                                                            "string",
                                                            "null"
                                                        ]
                                                    },
                                                    "secondaryControllerIpAddress": {
                                                        "oneOf": [
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "type": "string"
                                                                    },
                                                                    {}
                                                                ]
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "type": "string"
                                                                    },
                                                                    {}
                                                                ]
                                                            },
                                                            {
                                                                "type": "null"
                                                            }
                                                        ]
                                                    },
                                                    "secondaryControllerName": {
                                                        "type": [
                                                            "string",
                                                            "null"
                                                        ]
                                                    },
                                                    "siteId": {
                                                        "type": "string"
                                                    },
                                                    "siteTag": {
                                                        "type": [
                                                            "string",
                                                            "null"
                                                        ]
                                                    },
                                                    "tertiaryControllerIpAddress": {
                                                        "oneOf": [
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "type": "string"
                                                                    },
                                                                    {}
                                                                ]
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "type": "string"
                                                                    },
                                                                    {}
                                                                ]
                                                            },
                                                            {
                                                                "type": "null"
                                                            }
                                                        ]
                                                    },
                                                    "tertiaryControllerName": {
                                                        "type": [
                                                            "string",
                                                            "null"
                                                        ]
                                                    },
                                                    "vlanTagId": {
                                                        "type": "integer"
                                                    },
                                                    "vlanTagStatus": {
                                                        "type": "boolean"
                                                    },
                                                    "wlcIpAddress": {
                                                        "oneOf": [
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "type": "string"
                                                                    },
                                                                    {}
                                                                ]
                                                            },
                                                            {
                                                                "allOf": [
                                                                    {
                                                                        "type": "string"
                                                                    },
                                                                    {}
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                },
                                                "type": "object"
                                            },
                                            "type": "array"
                                        }
                                    },
                                    "type": "object"
                                }
                            ]
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
