"""Cisco Catalyst Center RetrieveASpecificNetworkDevice data model.

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


class JSONSchemaValidatorDbdcdf7D6B5Af88C18F481D713F90C:
    """RetrieveASpecificNetworkDevice request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "properties": {
                                "apEthernetMacAddress": {
                                    "type": "string"
                                },
                                "apManagerInterfaceIpAddress": {
                                    "allOf": [
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
                                },
                                "apWlcIpAddress": {
                                    "allOf": [
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
                                },
                                "bootTime": {
                                    "allOf": [
                                        {
                                            "minimum": 0,
                                            "type": "integer"
                                        }
                                    ]
                                },
                                "deviceSupportLevel": {
                                    "enum": [
                                        "SUPPORTED",
                                        "LIMITED",
                                        "THIRD_PARTY",
                                        "UNSUPPORTED"
                                    ],
                                    "type": "string"
                                },
                                "dnsResolvedManagementIpAddress": {
                                    "allOf": [
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
                                },
                                "family": {
                                    "type": "string"
                                },
                                "hostname": {
                                    "type": "string"
                                },
                                "id": {
                                    "type": "string"
                                },
                                "macAddress": {
                                    "type": "string"
                                },
                                "managementAddress": {
                                    "allOf": [
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
                                "platformIds": {
                                    "type": "string"
                                },
                                "role": {
                                    "enum": [
                                        "BORDER_ROUTER",
                                        "CORE",
                                        "DISTRIBUTION",
                                        "ACCESS",
                                        "UNKNOWN"
                                    ],
                                    "type": "string"
                                },
                                "roleSource": {
                                    "enum": [
                                        "AUTO",
                                        "MANUAL"
                                    ],
                                    "type": "string"
                                },
                                "serialNumbers": {
                                    "items": {
                                        "type": "string"
                                    },
                                    "maxItems": 50,
                                    "type": "array"
                                },
                                "series": {
                                    "type": "string"
                                },
                                "snmpContact": {
                                    "type": "string"
                                },
                                "snmpLocation": {
                                    "type": "string"
                                },
                                "softwareType": {
                                    "type": "string"
                                },
                                "softwareVersion": {
                                    "type": "string"
                                },
                                "stackDevice": {
                                    "type": "boolean"
                                },
                                "status": {
                                    "enum": [
                                        "MANAGED",
                                        "SYNC_NOT_STARTED",
                                        "SYNC_INIT_FAILED",
                                        "SYNC_PRECHECK_FAILED",
                                        "SYNC_IN_PROGRESS",
                                        "SYNC_INTERNAL_ERROR",
                                        "SYNC_DISABLED",
                                        "DELETING_DEVICE",
                                        "UNDER_MAINTENANCE",
                                        "QUARANTINED",
                                        "UNASSOCIATED",
                                        "UNREACHABLE",
                                        "UNKNOWN"
                                    ],
                                    "type": "string"
                                },
                                "type": {
                                    "type": "string"
                                },
                                "vendor": {
                                    "type": "string"
                                }
                            },
                            "type": "object"
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
