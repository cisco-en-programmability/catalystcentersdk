"""Cisco Catalyst Center GetConfigurationsForApTraceProfileFeatureOnAWirelessController data model.

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


class JSONSchemaValidatorA21707E95B95A8AA45C391A8Fde8753:
    """GetConfigurationsForApTraceProfileFeatureOnAWirelessController
    request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "items": {
                                "properties": {
                                    "apTraceClientConsoleLog": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "apTraceClientFilterArp": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "apTraceClientFilterAssoc": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "apTraceClientFilterAuth": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "apTraceClientFilterDhcp": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "apTraceClientFilterEap": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "apTraceClientFilterIcmp": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "apTraceClientFilterNdp": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "apTraceClientFilterProbeEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "apTraceProfileDescription": {
                                        "type": "string"
                                    },
                                    "apTraceProfileName": {
                                        "type": "string"
                                    },
                                    "configType": {
                                        "default": "AP_TRACE_PROFILE",
                                        "enum": [
                                            "AP_TRACE_PROFILE"
                                        ],
                                        "type": "string"
                                    },
                                    "deviceVersion": {
                                        "default": "26.01",
                                        "type": "string"
                                    },
                                    "id": {
                                        "type": "string"
                                    }
                                },
                                "type": "object"
                            },
                            "maxItems": 4094,
                            "minItems": 1,
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
