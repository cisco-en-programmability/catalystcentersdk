"""Cisco Catalyst Center RetrievesGlobalIPAddressPools data model.

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


class JSONSchemaValidatorC6B166895678Be157Ab0D389C0C6:
    """RetrievesGlobalIPAddressPools request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "items": {
                                "properties": {
                                    "addressSpace": {
                                        "oneOf": [
                                            {
                                                "allOf": [
                                                    {
                                                        "properties": {
                                                            "assignedAddresses": {
                                                                "maxLength": 39,
                                                                "type": "string"
                                                            },
                                                            "defaultAssignedAddresses": {
                                                                "maxLength": 39,
                                                                "type": "string"
                                                            },
                                                            "totalAddresses": {
                                                                "maxLength": 39,
                                                                "type": "string"
                                                            },
                                                            "unassignableAddresses": {
                                                                "maxLength": 39,
                                                                "type": "string"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    {
                                                        "properties": {
                                                            "prefixLength": {
                                                                "maximum": 30,
                                                                "minimum": 8,
                                                                "type": "integer"
                                                            },
                                                            "subnet": {
                                                                "allOf": [
                                                                    {
                                                                        "type": "string"
                                                                    },
                                                                    {}
                                                                ]
                                                            }
                                                        },
                                                        "required": [
                                                            "prefixLength",
                                                            "subnet"
                                                        ]
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "properties": {
                                                                    "dhcpServers": {
                                                                        "items": {
                                                                            "type": "string"
                                                                        },
                                                                        "maxItems": 10,
                                                                        "type": "array"
                                                                    },
                                                                    "dnsServers": {
                                                                        "items": {
                                                                            "type": "string"
                                                                        },
                                                                        "maxItems": 10,
                                                                        "type": "array"
                                                                    },
                                                                    "gatewayIpAddress": {
                                                                        "allOf": [
                                                                            {
                                                                                "type": "string"
                                                                            },
                                                                            {}
                                                                        ]
                                                                    }
                                                                }
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "properties": {
                                                            "assignedAddresses": {
                                                                "maxLength": 39,
                                                                "type": "string"
                                                            },
                                                            "defaultAssignedAddresses": {
                                                                "maxLength": 39,
                                                                "type": "string"
                                                            },
                                                            "totalAddresses": {
                                                                "maxLength": 39,
                                                                "type": "string"
                                                            },
                                                            "unassignableAddresses": {
                                                                "maxLength": 39,
                                                                "type": "string"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    {
                                                        "properties": {
                                                            "prefixLength": {
                                                                "maximum": 120,
                                                                "minimum": 36,
                                                                "type": "number"
                                                            },
                                                            "subnet": {
                                                                "allOf": [
                                                                    {
                                                                        "type": "string"
                                                                    },
                                                                    {}
                                                                ]
                                                            }
                                                        },
                                                        "required": [
                                                            "prefixLength",
                                                            "subnet"
                                                        ]
                                                    },
                                                    {
                                                        "allOf": [
                                                            {
                                                                "properties": {
                                                                    "dhcpServers": {
                                                                        "items": {
                                                                            "type": "string"
                                                                        },
                                                                        "maxItems": 10,
                                                                        "type": "array"
                                                                    },
                                                                    "dnsServers": {
                                                                        "items": {
                                                                            "type": "string"
                                                                        },
                                                                        "maxItems": 10,
                                                                        "type": "array"
                                                                    },
                                                                    "gatewayIpAddress": {
                                                                        "allOf": [
                                                                            {
                                                                                "type": "string"
                                                                            },
                                                                            {}
                                                                        ]
                                                                    },
                                                                    "slaacSupport": {
                                                                        "type": "boolean"
                                                                    }
                                                                }
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    "id": {
                                        "type": "string"
                                    },
                                    "name": {
                                        "allOf": [
                                            {
                                                "type": "string"
                                            },
                                            {}
                                        ]
                                    },
                                    "poolType": {
                                        "enum": [
                                            "Generic",
                                            "Tunnel"
                                        ],
                                        "type": "string"
                                    }
                                },
                                "required": [
                                    "addressSpace",
                                    "id",
                                    "name",
                                    "poolType"
                                ],
                                "type": "object"
                            },
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
