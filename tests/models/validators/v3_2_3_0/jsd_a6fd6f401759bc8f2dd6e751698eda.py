"""Cisco Catalyst Center RetrievesLicenseDetailsOfANetworkDevice data model.

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


class JSONSchemaValidatorA6Fd6F401759Bc8F2DD6E751698Eda:
    """RetrievesLicenseDetailsOfANetworkDevice request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "allOf": [
                                {},
                                {
                                    "properties": {
                                        "authCodeStatus": {
                                            "enum": [
                                                "INSTALLED",
                                                "NOT_INSTALLED",
                                                "NA"
                                            ],
                                            "type": "string"
                                        },
                                        "authorizationStatus": {
                                            "enum": [
                                                "AUTHORIZED",
                                                "EVALUATION_MODE",
                                                "OUT_OF_COMPLIANCE",
                                                "EVALUATION_EXPIRED",
                                                "AUTHORIZATION_EXPIRED",
                                                "NOT_AUTHORIZED",
                                                "AUTHORIZED_RESERVED",
                                                "NA",
                                                "UNKNOWN"
                                            ],
                                            "type": "string"
                                        },
                                        "changeWirelessLicense": {
                                            "default": false,
                                            "type": "boolean"
                                        },
                                        "customerTags": {
                                            "properties": {
                                                "tag1": {
                                                    "type": "string"
                                                },
                                                "tag2": {
                                                    "type": "string"
                                                },
                                                "tag3": {
                                                    "type": "string"
                                                },
                                                "tag4": {
                                                    "type": "string"
                                                }
                                            },
                                            "type": "object"
                                        },
                                        "family": {
                                            "enum": [
                                                "ROUTERS",
                                                "SWITCHES_AND_HUBS",
                                                "WIRELESS_CONTROLLER",
                                                "UNIFIED_AP"
                                            ],
                                            "type": "string"
                                        },
                                        "hostname": {
                                            "type": "string"
                                        },
                                        "id": {
                                            "type": "string"
                                        },
                                        "lastSuccessfulUsageReportingTime": {
                                            "allOf": [
                                                {
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                {}
                                            ]
                                        },
                                        "licenseLevel": {
                                            "enum": [
                                                "ESSENTIALS",
                                                "ADVANTAGE",
                                                "NONE"
                                            ],
                                            "type": "string"
                                        },
                                        "licenseManagedBy": {
                                            "type": "string"
                                        },
                                        "licenseMode": {
                                            "enum": [
                                                "SMART_LICENSE",
                                                "RIGHT_TO_USE",
                                                "UNKNOWN"
                                            ],
                                            "type": "string"
                                        },
                                        "licenses": {
                                            "items": {
                                                "properties": {
                                                    "count": {
                                                        "type": "integer"
                                                    },
                                                    "evaluationExpiryTime": {
                                                        "allOf": [
                                                            {
                                                                "minimum": 0,
                                                                "type": "integer"
                                                            },
                                                            {}
                                                        ]
                                                    },
                                                    "name": {
                                                        "type": "string"
                                                    },
                                                    "owned": {
                                                        "type": "boolean"
                                                    },
                                                    "status": {
                                                        "enum": [
                                                            "IN_USE",
                                                            "NOT_IN_USE",
                                                            "EXPIRED_IN_USE",
                                                            "EXPIRED_NOT_IN_USE",
                                                            "USAGE_COUNT_CONSUMED",
                                                            "OUT_OF_COMPLIANCE",
                                                            "EVALUATION_IN_USE",
                                                            "INACTIVE"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "type": {
                                                        "enum": [
                                                            "NETWORK_ESSENTIALS",
                                                            "NETWORK_ADVANTAGE",
                                                            "AIR_NETWORK_ESSENTIALS",
                                                            "AIR_NETWORK_ADVANTAGE",
                                                            "DNA_ESSENTIALS",
                                                            "DNA_ADVANTAGE",
                                                            "AIR_DNA_ESSENTIALS",
                                                            "AIR_DNA_ADVANTAGE",
                                                            "CNS_ESSENTIALS",
                                                            "CNS_ADVANTAGE",
                                                            "OTHER"
                                                        ],
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "type"
                                                ],
                                                "type": "object"
                                            },
                                            "type": "array"
                                        },
                                        "managementAddress": {
                                            "allOf": [
                                                {},
                                                {
                                                    "oneOf": [
                                                        {
                                                            "type": "string"
                                                        },
                                                        {
                                                            "oneOf": [
                                                                {
                                                                    "type": "string"
                                                                },
                                                                {
                                                                    "type": "string"
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        "networkDeviceId": {
                                            "type": "string"
                                        },
                                        "registrationStatus": {
                                            "enum": [
                                                "REGISTERED",
                                                "UNREGISTERED",
                                                "REGISTRATION_EXPIRED",
                                                "RESERVATION_IN_PROGRESS",
                                                "REGISTERED_SLR",
                                                "REGISTERED_PLR",
                                                "REGISTERED_SATELLITE",
                                                "NA",
                                                "UNKNOWN"
                                            ],
                                            "type": "string"
                                        },
                                        "series": {
                                            "type": "string"
                                        },
                                        "siteHierarchy": {
                                            "type": "string"
                                        },
                                        "smartAccountId": {
                                            "type": "string"
                                        },
                                        "softwareVersion": {
                                            "type": "string"
                                        },
                                        "throughputValue": {
                                            "type": "string"
                                        },
                                        "triggerReboot": {
                                            "default": true,
                                            "type": "boolean"
                                        },
                                        "virtualAccountId": {
                                            "type": "string"
                                        },
                                        "wirelessCapable": {
                                            "type": "boolean"
                                        }
                                    },
                                    "required": [
                                        "id",
                                        "licenseLevel"
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
