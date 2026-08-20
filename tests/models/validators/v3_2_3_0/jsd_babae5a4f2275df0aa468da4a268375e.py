"""Cisco Catalyst Center RetrieveTheStatusOfDeviceReplacementWorkflowThatReplacesAFaultyDeviceWithARe
placementDevice data model.

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


class JSONSchemaValidatorBabae5A4F2275Df0Aa468Da4A268375E:
    """RetrieveTheStatusOfDeviceReplacementWorkflowThatReplacesAFaultyDev
    iceWithAReplacementDevice request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "properties": {
                                "configureSso": {
                                    "type": "boolean"
                                },
                                "creationTime": {
                                    "allOf": [
                                        {
                                            "minimum": 0,
                                            "type": "integer"
                                        }
                                    ]
                                },
                                "family": {
                                    "type": "string"
                                },
                                "faultyDeviceId": {
                                    "type": "string"
                                },
                                "faultyDeviceName": {
                                    "type": "string"
                                },
                                "faultyDevicePlatform": {
                                    "type": "string"
                                },
                                "faultyDeviceSerialNumber": {
                                    "type": "string"
                                },
                                "haSsoDetail": {
                                    "properties": {
                                        "haInterfaceName": {
                                            "type": "string"
                                        },
                                        "localRedundancyIp": {
                                            "type": "string"
                                        },
                                        "peerDeviceSerialNumber": {
                                            "type": "string"
                                        },
                                        "peerHaInterfaceName": {
                                            "type": "string"
                                        },
                                        "redundancyIp": {
                                            "type": "string"
                                        }
                                    },
                                    "type": "object"
                                },
                                "id": {
                                    "type": "string"
                                },
                                "neighborDeviceId": {
                                    "type": "string"
                                },
                                "outOfBand": {
                                    "default": false,
                                    "type": "boolean"
                                },
                                "primaryGatewayIp": {
                                    "type": "string"
                                },
                                "primaryIpInterfaceName": {
                                    "type": "string"
                                },
                                "primaryNetmask": {
                                    "type": "string"
                                },
                                "primaryVlanId": {
                                    "type": "integer"
                                },
                                "primaryWirelessManagementIp": {
                                    "type": "string"
                                },
                                "replacementDevicePlatform": {
                                    "type": "string"
                                },
                                "replacementDeviceSerialNumber": {
                                    "type": "string"
                                },
                                "replacementStatus": {
                                    "allOf": [
                                        {
                                            "enum": [
                                                "MARKED_FOR_REPLACEMENT",
                                                "NETWORK_READINESS_REQUESTED",
                                                "NETWORK_READINESS_FAILED",
                                                "READY_FOR_REPLACEMENT",
                                                "REPLACEMENT_SCHEDULED",
                                                "REPLACEMENT_IN_PROGRESS",
                                                "REPLACED",
                                                "ERROR"
                                            ],
                                            "type": "string"
                                        }
                                    ]
                                },
                                "replacementTime": {
                                    "allOf": [
                                        {
                                            "minimum": 0,
                                            "type": "integer"
                                        }
                                    ]
                                },
                                "secondaryGatewayIp": {
                                    "type": "string"
                                },
                                "secondaryIpInterfaceName": {
                                    "type": "string"
                                },
                                "secondaryNetmask": {
                                    "type": "string"
                                },
                                "secondaryVlanId": {
                                    "type": "integer"
                                },
                                "secondaryWirelessManagementIp": {
                                    "type": "string"
                                },
                                "workflow": {
                                    "properties": {
                                        "endTime": {
                                            "allOf": [
                                                {
                                                    "minimum": 0,
                                                    "type": "integer"
                                                }
                                            ]
                                        },
                                        "id": {
                                            "type": "string"
                                        },
                                        "name": {
                                            "type": "string"
                                        },
                                        "startTime": {
                                            "allOf": [
                                                {
                                                    "minimum": 0,
                                                    "type": "integer"
                                                }
                                            ]
                                        },
                                        "steps": {
                                            "items": {
                                                "properties": {
                                                    "endTime": {
                                                        "allOf": [
                                                            {
                                                                "minimum": 0,
                                                                "type": "integer"
                                                            }
                                                        ]
                                                    },
                                                    "name": {
                                                        "type": "string"
                                                    },
                                                    "startTime": {
                                                        "allOf": [
                                                            {
                                                                "minimum": 0,
                                                                "type": "integer"
                                                            }
                                                        ]
                                                    },
                                                    "status": {
                                                        "enum": [
                                                            "INIT",
                                                            "RUNNING",
                                                            "SUCCESS",
                                                            "FAILED",
                                                            "ABORTED",
                                                            "TIMEOUT"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "statusMessage": {
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "name",
                                                    "startTime",
                                                    "status",
                                                    "statusMessage"
                                                ],
                                                "type": "object"
                                            },
                                            "type": "array"
                                        },
                                        "workflowStatus": {
                                            "enum": [
                                                "RUNNING",
                                                "SUCCESS",
                                                "FAILED"
                                            ],
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "id",
                                        "name",
                                        "startTime",
                                        "steps",
                                        "workflowStatus"
                                    ],
                                    "type": "object"
                                }
                            },
                            "required": [
                                "creationTime",
                                "family",
                                "faultyDeviceId",
                                "faultyDeviceName",
                                "faultyDevicePlatform",
                                "faultyDeviceSerialNumber",
                                "id",
                                "replacementStatus"
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
