"""Cisco Catalyst Center GetAuthenticationProfiles data model.

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


class JSONSchemaValidatorE6713A34508993B3E9F6837Dd690:
    """GetAuthenticationProfiles request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "properties": {
                        "response": {
                            "items": {
                                "properties": {
                                    "authenticationOrder": {
                                        "enum": [
                                            "dot1x",
                                            "mac"
                                        ],
                                        "type": "string"
                                    },
                                    "authenticationProfileName": {
                                        "enum": [
                                            "Low Impact",
                                            "Open Authentication",
                                            "Closed Authentication"
                                        ],
                                        "type": "string"
                                    },
                                    "dot1xToMabFallbackTimeout": {
                                        "maximum": 120,
                                        "minimum": 3,
                                        "type": "integer"
                                    },
                                    "fabricId": {
                                        "type": "string"
                                    },
                                    "id": {
                                        "type": "string"
                                    },
                                    "isBpduGuardEnabled": {
                                        "type": "boolean"
                                    },
                                    "isVoiceVlanEnabled": {
                                        "type": "boolean"
                                    },
                                    "numberOfHosts": {
                                        "enum": [
                                            "Single",
                                            "Unlimited"
                                        ],
                                        "type": "string"
                                    },
                                    "preAuthAcl": {
                                        "allOf": [
                                            {
                                                "properties": {
                                                    "enabled": {
                                                        "type": "boolean"
                                                    }
                                                },
                                                "type": "object"
                                            },
                                            {
                                                "properties": {
                                                    "accessContracts": {
                                                        "items": {
                                                            "properties": {
                                                                "action": {
                                                                    "enum": [
                                                                        "PERMIT",
                                                                        "DENY"
                                                                    ],
                                                                    "type": "string"
                                                                },
                                                                "port": {
                                                                    "enum": [
                                                                        "DOMAIN",
                                                                        "BOOTPC",
                                                                        "BOOTPS"
                                                                    ],
                                                                    "type": "string"
                                                                },
                                                                "protocol": {
                                                                    "enum": [
                                                                        "UDP",
                                                                        "TCP",
                                                                        "TCP_UDP"
                                                                    ],
                                                                    "type": "string"
                                                                }
                                                            },
                                                            "type": "object"
                                                        },
                                                        "maxItems": 3,
                                                        "type": "array"
                                                    },
                                                    "description":
                 {
                                                        "type": "string"
                                                    },
                                                    "implicitAction": {
                                                        "enum": [
                                                            "PERMIT",
                                                            "DENY"
                                                        ],
                                                        "type": "string"
                                                    }
                                                },
                                                "type": "object"
                                            }
                                        ]
                                    },
                                    "preAuthAclIpV6": {
                                        "allOf": [
                                            {
                                                "properties": {
                                                    "accessContracts": {
                                                        "items": {
                                                            "properties": {
                                                                "action": {
                                                                    "enum": [
                                                                        "PERMIT",
                                                                        "DENY"
                                                                    ],
                                                                    "type": "string"
                                                                },
                                                                "port": {
                                                                    "enum": [
                                                                        "DOMAIN",
                                                                        "BOOTPC",
                                                                        "BOOTPS"
                                                                    ],
                                                                    "type": "string"
                                                                },
                                                                "protocol": {
                                                                    "enum": [
                                                                        "UDP",
                                                                        "TCP",
                                                                        "TCP_UDP"
                                                                    ],
                                                                    "type": "string"
                                                                }
                                                            },
                                                            "type": "object"
                                                        },
                                                        "maxItems": 3,
                                                        "type": "array"
                                                    },
                                                    "description":
                 {
                                                        "type": "string"
                                                    },
                                                    "implicitAction": {
                                                        "enum": [
                                                            "PERMIT",
                                                            "DENY"
                                                        ],
                                                        "type": "string"
                                                    }
                                                },
                                                "type": "object"
                                            },
                                            {
                                                "properties": {
                                                    "accessContracts": {
                                                        "items": {
                                                            "properties": {
                                                                "action": {
                                                                    "enum": [
                                                                        "PERMIT",
                                                                        "DENY"
                                                                    ],
                                                                    "type": "string"
                                                                },
                                                                "port": {
                                                                    "enum": [
                                                                        "DOMAIN",
                                                                        "ND_NS",
                                                                        "ND_NA",
                                                                        "ROUTER_SOLICITATION",
                                                                        "ROUTER_ADVERTISEMENT",
                                                                        "REDIRECT",
                                                                        "547"
                                                                    ],
                                                                    "type": "string"
                                                                },
                                                                "protocol": {
                                                                    "enum": [
                                                                        "UDP",
                                                                        "TCP",
                                                                        "ICMP"
                                                                    ],
                                                                    "type": "string"
                                                                }
                                                            },
                                                            "type": "object"
                                                        },
                                                        "maxItems": 8,
                                                        "type": "array"
                                                    }
                                                },
                                                "type": "object"
                                            }
                                        ]
                                    },
                                    "wakeOnLan": {
                                        "type": "boolean"
                                    }
                                },
                                "type": "object"
                            },
                            "maxItems": 500,
                            "minItems": 0,
                            "type": "array"
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
