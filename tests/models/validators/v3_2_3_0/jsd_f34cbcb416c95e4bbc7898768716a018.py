"""Cisco Catalyst Center FetchNetworkDeviceWithImageDetails data model.

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


class JSONSchemaValidatorF34Cbcb416C95E4BBc7898768716A018:
    """FetchNetworkDeviceWithImageDetails request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "properties": {
                                "compatibleFeatures": {
                                    "items": {
                                        "properties": {
                                            "key": {
                                                "type": "string"
                                            },
                                            "value": {
                                                "enum": [
                                                    "ENABLE",
                                                    "DISABLE"
                                                ],
                                                "type": "string"
                                            }
                                        },
                                        "type": "object"
                                    },
                                    "type": "array"
                                },
                                "goldenImages": {
                                    "items": {
                                        "properties": {
                                            "goldenTaggingDetails": {
                                                "properties": {
                                                    "deviceRoles": {
                                                        "enum": [
                                                            "CORE",
                                                            "DISTRIBUTION",
                                                            "UNKNOWN",
                                                            "ACCESS",
                                                            "BORDER_ROUTER"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "deviceTags": {
                                                        "type": "string"
                                                    },
                                                    "isInherited": {
                                                        "type": "boolean"
                                                    },
                                                    "nameHierarchy": {
                                                        "type": "string"
                                                    },
                                                    "siteId": {
                                                        "type": "string"
                                                    },
                                                    "siteName": {
                                                        "type": "string"
                                                    }
                                                },
                                                "type": "object"
                                            },
                                            "id": {
                                                "type": "string"
                                            },
                                            "imageType": {
                                                "enum": [
                                                    "SYSTEM",
                                                    "SMU",
                                                    "PSIRT_SMU",
                                                    "SUBPACKAGE",
                                                    "ROMMON_SW",
                                                    "APDP",
                                                    "APSP"
                                                ],
                                                "type": "string"
                                            },
                                            "name": {
                                                "type": "string"
                                            },
                                            "version": {
                                                "type": "string"
                                            }
                                        },
                                        "required": [
                                            "id",
                                            "imageType",
                                            "name",
                                            "version"
                                        ],
                                        "type": "object"
                                    },
                                    "type": "array"
                                },
                                "id": {
                                    "type": "string"
                                },
                                "incompatibleAppDetails": {
                                    "items": {
                                        "properties": {
                                            "appName": {
                                                "type": "string"
                                            },
                                            "compatibleImages": {
                                                "items": {
                                                    "properties": {
                                                        "imageName": {
                                                            "type": "string"
                                                        },
                                                        "imageType": {
                                                            "enum": [
                                                                "SYSTEM",
                                                                "SMU",
                                                                "PSIRT_SMU",
                                                                "SUBPACKAGE",
                                                                "ROMMON_SW",
                                                                "APDP",
                                                                "APSP"
                                                            ],
                                                            "type": "string"
                                                        },
                                                        "imageVersion": {
                                                            "type": "string"
                                                        },
                                                        "recommended": {
                                                            "type": "boolean"
                                                        }
                                                    },
                                                    "type": "object"
                                                },
                                                "type": "array"
                                            },
                                            "incompatibleWith": {
                                                "items": {
                                                    "enum": [
                                                        "RUNNING_IMAGE",
                                                        "GOLDEN_IMAGE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "type": "array"
                                            }
                                        },
                                        "type": "object"
                                    },
                                    "type": "array"
                                },
                                "installedImages": {
                                    "items": {
                                        "properties": {
                                            "id": {
                                                "type": "string"
                                            },
                                            "imageType": {
                                                "enum": [
                                                    "SYSTEM",
                                                    "SMU",
                                                    "PSIRT_SMU",
                                                    "SUBPACKAGE",
                                                    "ROMMON_SW",
                                                    "APDP",
                                                    "APSP"
                                                ],
                                                "type": "string"
                                            },
                                            "name": {
                                                "type": "string"
                                            },
                                            "version": {
                                                "type": "string"
                                            }
                                        },
                                        "required": [
                                            "name"
                                        ],
                                        "type": "object"
                                    },
                                    "type": "array"
                                },
                                "managementAddress": {
                                    "type": "string"
                                },
                                "networkDevice": {
                                    "properties": {
                                        "id": {
                                            "type": "string"
                                        },
                                        "productName": {
                                            "type": "string"
                                        },
                                        "productNameOrdinal": {
                                            "type": "number"
                                        },
                                        "supervisorProductName": {
                                            "type": "string"
                                        },
                                        "supervisorProductNameOrdinal": {
                                            "type": "number"
                                        }
                                    },
                                    "required": [
                                        "id"
                                    ],
                                    "type": "object"
                                },
                                "networkDeviceImageCompatibilityStatus": {
                                    "enum": [
                                        "COMPATIBLE",
                                        "IN_COMPATIBLE",
                                        "UNKNOWN"
                                    ],
                                    "type": "string"
                                },
                                "networkDeviceImageStatus": {
                                    "enum": [
                                        "OUTDATED",
                                        "UP_TO_DATE",
                                        "UNKNOWN",
                                        "CONFLICTED",
                                        "UNSUPPORTED"
                                    ],
                                    "type": "string"
                                },
                                "networkDeviceUpdateStatus": {
                                    "enum": [
                                        "DISTRIBUTION_PENDING",
                                        "DISTRIBUTION_IN_PROGRESS",
                                        "DISTRIBUTION_FAILED",
                                        "ACTIVATION_PENDING",
                                        "ACTIVATION_IN_PROGRESS",
                                        "ACTIVATION_FAILED",
                                        "DEVICE_UP_TO_DATE",
                                        "UNKNOWN"
                                    ],
                                    "type": "string"
                                }
                            },
                            "required": [
                                "id"
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
