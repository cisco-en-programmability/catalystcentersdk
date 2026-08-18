"""Cisco Catalyst Center GetPlannedAccessPointsPositions data model.

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


class JSONSchemaValidatorD37C716018De59689125Cab5C7832A38:
    """GetPlannedAccessPointsPositions request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "items": {
                                "properties": {
                                    "id": {
                                        "type": "string"
                                    },
                                    "macAddress": {
                                        "type": "string"
                                    },
                                    "name": {
                                        "type": "string"
                                    },
                                    "position": {
                                        "properties": {
                                            "x": {
                                                "type": "number"
                                            },
                                            "y": {
                                                "type": "number"
                                            },
                                            "z": {
                                                "type": "number"
                                            }
                                        },
                                        "required": [
                                            "x",
                                            "y",
                                            "z"
                                        ],
                                        "type": "object"
                                    },
                                    "radios": {
                                        "items": {
                                            "properties": {
                                                "antenna": {
                                                    "properties": {
                                                        "azimuth": {
                                                            "maximum": 360,
                                                            "minimum": 0,
                                                            "type": "integer"
                                                        },
                                                        "elevation": {
                                                            "maximum": 180,
                                                            "minimum": -180,
                                                            "type": "integer"
                                                        },
                                                        "name": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "azimuth",
                                                        "elevation",
                                                        "name"
                                                    ],
                                                    "type": "object"
                                                },
                                                "bands": {
                                                    "items": {
                                                        "enum": [
                                                            2.4,
                                                            5,
                                                            6
                                                        ],
                                                        "type": "number"
                                                    },
                                                    "maxItems": 3,
                                                    "minItems": 1,
                                                    "type": "array",
                                                    "uniqueItems": true
                                                },
                                                "channel": {
                                                    "type": "integer"
                                                },
                                                "id": {
                                                    "type": "string"
                                                },
                                                "txPower": {
                                                    "type": "integer"
                                                }
                                            },
                                            "required": [
                                                "antenna",
                                                "bands",
                                                "channel",
                                                "id",
                                                "txPower"
                                            ],
                                            "type": "object"
                                        },
                                        "maxItems": 4,
                                        "minItems": 1,
                                        "type": "array"
                                    },
                                    "type": {
                                        "type": "string"
                                    }
                                },
                                "required": [
                                    "id",
                                    "name",
                                    "position",
                                    "radios",
                                    "type"
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
