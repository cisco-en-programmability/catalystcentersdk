"""Cisco Catalyst Center GetConfigurationsForASpecificInstanceOfAApTagConfigFeatureOnAWirelessControl
ler data model.

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


class JSONSchemaValidatorBfbfc09895054914E8Bcb9Dcb277C:
    """GetConfigurationsForASpecificInstanceOfAApTagConfigFeatureOnAWirel
    essController request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "oneOf": [
                                {
                                    "allOf": [
                                        {
                                            "properties": {
                                                "id": {
                                                    "type": "string"
                                                }
                                            },
                                            "type": "object"
                                        },
                                        {
                                            "properties": {
                                                "apMac": {
                                                    "type": "string"
                                                },
                                                "configType": {
                                                    "default": "AP_TAG",
                                                    "enum": [
                                                        "AP_TAG"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.12",
                                                    "type": "string"
                                                },
                                                "policyTag": {
                                                    "default": "default-policy-tag",
                                                    "type": "string"
                                                },
                                                "primingProfile": {
                                                    "type": "string"
                                                },
                                                "rfTag": {
                                                    "default": "default-rf-tag",
                                                    "type": "string"
                                                },
                                                "siteTag": {
                                                    "default": "default-site-tag",
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "apMac",
                                                "deviceVersion"
                                            ]
                                        }
                                    ],
                                    "type": "object"
                                },
                                {
                                    "allOf": [
                                        {
                                            "properties": {
                                                "id": {
                                                    "type": "string"
                                                }
                                            },
                                            "type": "object"
                                        },
                                        {
                                            "properties": {
                                                "apMac": {
                                                    "type": "string"
                                                },
                                                "configType": {
                                                    "default": "AP_TAG",
                                                    "enum": [
                                                        "AP_TAG"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.13",
                                                    "type": "string"
                                                },
                                                "policyTag": {
                                                    "default": "default-policy-tag",
                                                    "type": "string"
                                                },
                                                "primingProfile": {
                                                    "type": "string"
                                                },
                                                "rfTag": {
                                                    "default": "default-rf-tag",
                                                    "type": "string"
                                                },
                                                "siteTag": {
                                                    "default": "default-site-tag",
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "apMac",
                                                "deviceVersion"
                                            ]
                                        }
                                    ],
                                    "type": "object"
                                },
                                {
                                    "allOf": [
                                        {
                                            "properties": {
                                                "id": {
                                                    "type": "string"
                                                }
                                            },
                                            "type": "object"
                                        },
                                        {
                                            "properties": {
                                                "apMac": {
                                                    "type": "string"
                                                },
                                                "configType": {
                                                    "default": "AP_TAG",
                                                    "enum": [
                                                        "AP_TAG"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.14",
                                                    "type": "string"
                                                },
                                                "policyTag": {
                                                    "default": "default-policy-tag",
                                                    "type": "string"
                                                },
                                                "primingProfile": {
                                                    "type": "string"
                                                },
                                                "rfTag": {
                                                    "default": "default-rf-tag",
                                                    "type": "string"
                                                },
                                                "siteTag": {
                                                    "default": "default-site-tag",
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "apMac",
                                                "deviceVersion"
                                            ]
                                        }
                                    ],
                                    "type": "object"
                                },
                                {
                                    "allOf": [
                                        {
                                            "properties": {
                                                "id": {
                                                    "type": "string"
                                                }
                                            },
                                            "type": "object"
                                        },
                                        {
                                            "properties": {
                                                "apMac": {
                                                    "type": "string"
                                                },
                                                "configType": {
                                                    "default": "AP_TAG",
                                                    "enum": [
                                                        "AP_TAG"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.15",
                                                    "type": "string"
                                                },
                                                "policyTag": {
                                                    "default": "default-policy-tag",
                                                    "type": "string"
                                                },
                                                "primingProfile": {
                                                    "type": "string"
                                                },
                                                "rfTag": {
                                                    "default": "default-rf-tag",
                                                    "type": "string"
                                                },
                                                "siteTag": {
                                                    "default": "default-site-tag",
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "apMac",
                                                "deviceVersion"
                                            ]
                                        }
                                    ],
                                    "type": "object"
                                },
                                {
                                    "allOf": [
                                        {
                                            "properties": {
                                                "id": {
                                                    "type": "string"
                                                }
                                            },
                                            "type": "object"
                                        },
                                        {
                                            "properties": {
                                                "apMac": {
                                                    "type": "string"
                                                },
                                                "configType": {
                                                    "default": "AP_TAG",
                                                    "enum": [
                                                        "AP_TAG"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.16",
                                                    "type": "string"
                                                },
                                                "policyTag": {
                                                    "default": "default-policy-tag",
                                                    "type": "string"
                                                },
                                                "primingProfile": {
                                                    "type": "string"
                                                },
                                                "rfTag": {
                                                    "default": "default-rf-tag",
                                                    "type": "string"
                                                },
                                                "siteTag": {
                                                    "default": "default-site-tag",
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "apMac",
                                                "deviceVersion"
                                            ]
                                        }
                                    ],
                                    "type": "object"
                                },
                                {
                                    "allOf": [
                                        {
                                            "properties": {
                                                "id": {
                                                    "type": "string"
                                                }
                                            },
                                            "type": "object"
                                        },
                                        {
                                            "properties": {
                                                "apMac": {
                                                    "type": "string"
                                                },
                                                "configType": {
                                                    "default": "AP_TAG",
                                                    "enum": [
                                                        "AP_TAG"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.17",
                                                    "type": "string"
                                                },
                                                "policyTag": {
                                                    "default": "default-policy-tag",
                                                    "type": "string"
                                                },
                                                "primingProfile": {
                                                    "type": "string"
                                                },
                                                "rfTag": {
                                                    "default": "default-rf-tag",
                                                    "type": "string"
                                                },
                                                "siteTag": {
                                                    "default": "default-site-tag",
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "apMac",
                                                "deviceVersion"
                                            ]
                                        }
                                    ],
                                    "type": "object"
                                },
                                {
                                    "allOf": [
                                        {
                                            "properties": {
                                                "id": {
                                                    "type": "string"
                                                }
                                            },
                                            "type": "object"
                                        },
                                        {
                                            "properties": {
                                                "apMac": {
                                                    "type": "string"
                                                },
                                                "configType": {
                                                    "default": "AP_TAG",
                                                    "enum": [
                                                        "AP_TAG"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.18",
                                                    "type": "string"
                                                },
                                                "policyTag": {
                                                    "default": "default-policy-tag",
                                                    "type": "string"
                                                },
                                                "primingProfile": {
                                                    "type": "string"
                                                },
                                                "rfTag": {
                                                    "default": "default-rf-tag",
                                                    "type": "string"
                                                },
                                                "siteTag": {
                                                    "default": "default-site-tag",
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "apMac",
                                                "deviceVersion"
                                            ]
                                        }
                                    ],
                                    "type": "object"
                                },
                                {
                                    "allOf": [
                                        {
                                            "properties": {
                                                "id": {
                                                    "type": "string"
                                                }
                                            },
                                            "type": "object"
                                        },
                                        {
                                            "properties": {
                                                "apMac": {
                                                    "type": "string"
                                                },
                                                "apTagApName": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "configType": {
                                                    "default": "AP_TAG",
                                                    "enum": [
                                                        "AP_TAG"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "26.01",
                                                    "type": "string"
                                                },
                                                "policyTag": {
                                                    "type": "string"
                                                },
                                                "primingProfile": {
                                                    "type": "string"
                                                },
                                                "rfTag": {
                                                    "type": "string"
                                                },
                                                "siteTag": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "apMac",
                                                "deviceVersion"
                                            ]
                                        }
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
