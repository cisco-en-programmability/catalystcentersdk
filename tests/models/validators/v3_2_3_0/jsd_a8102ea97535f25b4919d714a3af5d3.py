"""Cisco Catalyst Center RetrievesTheListOfClientsMetricsForTheGivenApplication data model.

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


class JSONSchemaValidatorA8102Ea97535F25B4919D714A3Af5D3:
    """RetrievesTheListOfClientsMetricsForTheGivenApplication request
    schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "page": {
                            "properties": {
                                "count": {
                                    "type": "integer"
                                },
                                "limit": {
                                    "default": 100,
                                    "maximum": 500,
                                    "minimum": 1,
                                    "type": "integer"
                                },
                                "offset": {
                                    "default": 1,
                                    "minimum": 1,
                                    "type": "integer"
                                },
                                "sortBy": {
                                    "items": {
                                        "properties": {
                                            "name": {
                                                "enum": [
                                                    "macAddress",
                                                    "exporterNetworkDeviceId"
                                                ],
                                                "type": "string"
                                            },
                                            "order": {
                                                "enum": [
                                                    "asc",
                                                    "desc"
                                                ],
                                                "type": "string"
                                            }
                                        },
                                        "type": "object"
                                    },
                                    "type": "array"
                                }
                            },
                            "type": "object"
                        },
                        "response": {
                            "items": {
                                "properties": {
                                    "appHealthScore": {
                                        "maximum": 10,
                                        "minimum": 1,
                                        "type": "integer"
                                    },
                                    "clientHealthScore": {
                                        "maximum": 10,
                                        "minimum": 1,
                                        "type": "integer"
                                    },
                                    "connectedNetworkDeviceId": {
                                        "type": "string"
                                    },
                                    "connectedNetworkDeviceName": {
                                        "type": "string"
                                    },
                                    "exporterNetworkDeviceId": {
                                        "type": "string"
                                    },
                                    "id": {
                                        "type": "string"
                                    },
                                    "ipv4Address": {
                                        "type": "string"
                                    },
                                    "ipv6Addresses": {
                                        "items": {
                                            "type": "string"
                                        },
                                        "type": "array"
                                    },
                                    "macAddress": {
                                        "type": "string"
                                    },
                                    "name": {
                                        "type": "string"
                                    },
                                    "osType": {
                                        "type": "string"
                                    },
                                    "siteId": {
                                        "type": "string"
                                    },
                                    "siteName": {
                                        "type": "string"
                                    },
                                    "type": {
                                        "enum": [
                                            "Wired",
                                            "Wireless"
                                        ],
                                        "type": "string"
                                    },
                                    "usage": {
                                        "type": "integer"
                                    },
                                    "vlanId": {
                                        "type": "string"
                                    }
                                },
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
