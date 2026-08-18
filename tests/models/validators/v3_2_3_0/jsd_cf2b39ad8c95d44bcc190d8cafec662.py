"""Cisco Catalyst Center GetConfigurationsForApPrimingConfigFeatureOnAWirelessController data model.

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


class JSONSchemaValidatorCf2B39AD8C95D44Bcc190D8Cafec662:
    """GetConfigurationsForApPrimingConfigFeatureOnAWirelessController
    request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "items": {
                                "properties": {
                                    "apPrimingProfileDescription": {
                                        "type": "string"
                                    },
                                    "apPrimingProfileHeight": {
                                        "default": 0,
                                        "maximum": 1000,
                                        "minimum": -100,
                                        "type": "integer"
                                    },
                                    "apPrimingProfileHeightType": {
                                        "default": "GEO_AFC_HEIGHT_UNKNOWN",
                                        "enum": [
                                            "GEO_AFC_HEIGHT_AGL",
                                            "GEO_AFC_HEIGHT_UNKNOWN"
                                        ],
                                        "type": "string"
                                    },
                                    "apPrimingProfileName": {
                                        "maxLength": 32,
                                        "minLength": 1,
                                        "type": "string"
                                    },
                                    "configType": {
                                        "default": "AP_PRIMING",
                                        "enum": [
                                            "AP_PRIMING"
                                        ],
                                        "type": "string"
                                    },
                                    "deviceVersion": {
                                        "default": "26.01",
                                        "type": "string"
                                    },
                                    "heightUncertainty": {
                                        "default": 1,
                                        "maximum": 100,
                                        "minimum": 1,
                                        "type": "integer"
                                    },
                                    "id": {
                                        "type": "string"
                                    },
                                    "overrideExistingPriming": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "primaryWlcIpAddress": {
                                        "default": "0.0.0.0",
                                        "type": "string"
                                    },
                                    "primaryWlcName": {
                                        "type": "string"
                                    },
                                    "secondaryWlcIpAddress": {
                                        "default": "0.0.0.0",
                                        "type": "string"
                                    },
                                    "secondaryWlcName": {
                                        "type": "string"
                                    },
                                    "tertiaryWlcIpAddress": {
                                        "default": "0.0.0.0",
                                        "type": "string"
                                    },
                                    "tertiaryWlcName": {
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
