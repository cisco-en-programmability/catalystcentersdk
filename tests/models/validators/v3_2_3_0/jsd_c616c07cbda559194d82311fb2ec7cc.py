"""Cisco Catalyst Center RetrievesTheListOfPathTracesForTheGivenThousandEyesTestResult data model.

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


class JSONSchemaValidatorC616C07Cbda559194D82311Fb2Ec7Cc:
    """RetrievesTheListOfPathTracesForTheGivenThousandEyesTestResult
    request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "appLink": {
                            "type": "string"
                        },
                        "response": {
                            "items": {
                                "properties": {
                                    "hops": {
                                        "items": {
                                            "properties": {
                                                "healthScore": {
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "identifier": {
                                                    "type": "string"
                                                },
                                                "index": {
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "ipAddress": {
                                                    "type": "string"
                                                },
                                                "jitter": {
                                                    "type": "number"
                                                },
                                                "location": {
                                                    "type": "string"
                                                },
                                                "name": {
                                                    "type": "string"
                                                },
                                                "network": {
                                                    "type": "string"
                                                },
                                                "responseTime": {
                                                    "type": "integer"
                                                },
                                                "traceTerminated": {
                                                    "type": "boolean"
                                                },
                                                "type": {
                                                    "enum": [
                                                        "CLIENT",
                                                        "AP",
                                                        "AGENT",
                                                        "SWITCH",
                                                        "ROUTER",
                                                        "WLC",
                                                        "EXTERNAL",
                                                        "TARGET",
                                                        "UNKNOWN"
                                                    ],
                                                    "type": "string"
                                                },
                                                "wlcId": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "index",
                                                "type"
                                            ],
                                            "type": "object"
                                        },
                                        "type": "array"
                                    },
                                    "id": {
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
