"""Cisco Catalyst Center LANAutomationStatusById data model.

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


class JSONSchemaValidatorD5727C4BDb1056308Cd10E99Dff2Acb8:
    """LANAutomationStatusById request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "items": {
                                "properties": {
                                    "action": {
                                        "type": "string"
                                    },
                                    "advertiseLANAutomationRoutesIntoBGP": {
                                        "type": "boolean"
                                    },
                                    "areaId": {
                                        "maximum": 2147483647,
                                        "minimum": 0,
                                        "type": "integer"
                                    },
                                    "authenticationKey": {
                                        "maxLength": 100,
                                        "minLength": 0,
                                        "type": "string"
                                    },
                                    "creationTime": {
                                        "type": "string"
                                    },
                                    "discoveredDeviceList": {
                                        "items": {
                                            "properties": {
                                                "ipAddressInUseList": {
                                                    "items": {
                                                        "type": "string"
                                                    },
                                                    "type": "array"
                                                },
                                                "name": {
                                                    "type": "string"
                                                },
                                                "serialNumber": {
                                                    "type": "string"
                                                },
                                                "state": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "name",
                                                "serialNumber",
                                                "state"
                                            ],
                                            "type": "object"
                                        },
                                        "type": "array"
                                    },
                                    "discoveredDeviceSiteNameHierarchy": {
                                        "type": "string"
                                    },
                                    "discoveryDevices": {
                                        "items": {
                                            "properties": {
                                                "deviceHostName": {
                                                    "type": "string"
                                                },
                                                "deviceManagementIPAddress": {
                                                    "type": "string"
                                                },
                                                "deviceSerialNumber": {
                                                    "type": "string"
                                                },
                                                "deviceSiteId": {
                                                    "type": "string"
                                                },
                                                "deviceSiteNameHierarchy": {
                                                    "type": "string"
                                                },
                                                "isDeviceDiscovered": {
                                                    "type": "boolean"
                                                },
                                                "isIPAllocated": {
                                                    "type": "boolean"
                                                },
                                                "isIPAssigned": {
                                                    "type": "boolean"
                                                },
                                                "pnpDeviceId": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "deviceManagementIPAddress"
                                            ],
                                            "type": "object"
                                        },
                                        "type": "array"
                                    },
                                    "discoveryLevel": {
                                        "type": "integer"
                                    },
                                    "discoveryTimeout": {
                                        "type": "integer"
                                    },
                                    "hostNameFileId": {
                                        "type": "string"
                                    },
                                    "hostNamePrefix": {
                                        "type": "string"
                                    },
                                    "id": {
                                        "type": "string"
                                    },
                                    "ipPools": {
                                        "items": {
                                            "properties": {
                                                "ipPoolName": {
                                                    "type": "string"
                                                },
                                                "ipPoolRole": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "ipPoolName",
                                                "ipPoolRole"
                                            ],
                                            "type": "object"
                                        },
                                        "type": "array"
                                    },
                                    "ipV6Only": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "multicastEnabled": {
                                        "type": "boolean"
                                    },
                                    "peerDeviceManagmentIPAddress": {
                                        "type": "string"
                                    },
                                    "primaryDeviceInterfaceNames": {
                                        "items": {
                                            "type": "string"
                                        },
                                        "type": "array"
                                    },
                                    "primaryDeviceManagmentIPAddress": {
                                        "type": "string"
                                    },
                                    "processId": {
                                        "maximum": 65535,
                                        "minimum": 1,
                                        "type": "integer"
                                    },
                                    "redistributeIsisToBgp": {
                                        "type": "boolean"
                                    },
                                    "routingProtocol": {
                                        "enum": [
                                            "ISIS",
                                            "OSPF"
                                        ]
                                    },
                                    "status": {
                                        "type": "string"
                                    },
                                    "useP2PLinkLocalAddress": {
                                        "default": false,
                                        "type": "boolean"
                                    }
                                },
                                "required": [
                                    "id",
                                    "discoveredDeviceSiteNameHierarchy",
                                    "primaryDeviceManagmentIPAddress",
                                    "ipPools",
                                    "primaryDeviceInterfaceNames",
                                    "status",
                                    "action",
                                    "creationTime"
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
