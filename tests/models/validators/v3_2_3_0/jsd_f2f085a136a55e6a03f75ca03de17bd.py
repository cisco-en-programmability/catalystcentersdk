"""Cisco Catalyst Center GetsAFloor data model.

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


class JSONSchemaValidatorF2F085A136A55E6A03F75Ca03De17Bd:
    """GetsAFloor request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "allOf": [
                                {
                                    "properties": {
                                        "id": {
                                            "type": "string"
                                        },
                                        "nameHierarchy": {
                                            "minLength": 8,
                                            "type": "string"
                                        },
                                        "parentId": {
                                            "type": "string"
                                        },
                                        "siteHierarchyId": {
                                            "type": "string"
                                        },
                                        "type": {
                                            "enum": [
                                                "floor"
                                            ],
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "parentId"
                                    ],
                                    "type": "object"
                                },
                                {
                                    "properties": {
                                        "floorNumber": {
                                            "type": "integer"
                                        },
                                        "height": {
                                            "type": "number"
                                        },
                                        "length": {
                                            "type": "number"
                                        },
                                        "name": {
                                            "minLength": 1,
                                            "type": "string"
                                        },
                                        "rfModel": {
                                            "enum": [
                                                "Free Space",
                                                "Outdoor Open Space",
                                                "Cubes And Walled Offices",
                                                "Indoor High Ceiling",
                                                "Drywall Office Only"
                                            ],
                                            "type": "string"
                                        },
                                        "unitsOfMeasure": {
                                            "allOf": [
                                                {
                                                    "enum": [
                                                        "feet",
                                                        "meters"
                                                    ],
                                                    "type": "string"
                                                },
                                                {
                                                    "default": "feet"
                                                }
                                            ]
                                        },
                                        "width": {
                                            "type": "number"
                                        }
                                    },
                                    "required": [
                                        "floorNumber",
                                        "height",
                                        "length",
                                        "name",
                                        "rfModel",
                                        "width"
                                    ],
                                    "type": "object"
                                }
                            ]
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
