"""Cisco Catalyst Center GetConfigurationsForRadioPolicyConfigFeatureOnAWirelessController data
model.

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


class JSONSchemaValidatorC6555Be8Cd845014B692Db82C1A9A928:
    """GetConfigurationsForRadioPolicyConfigFeatureOnAWirelessController
    request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "items": {
                                "properties": {
                                    "configType": {
                                        "default": "RADIO_POLICY",
                                        "enum": [
                                            "RADIO_POLICY"
                                        ],
                                        "type": "string"
                                    },
                                    "deviceVersion": {
                                        "default": "26.01",
                                        "type": "string"
                                    },
                                    "id": {
                                        "type": "string"
                                    },
                                    "profileName": {
                                        "maxLength": 32,
                                        "minLength": 0,
                                        "type": "string"
                                    },
                                    "radioPolicyBand": {
                                        "enum": [
                                            "DOT11_2_DOT_4_GHZ_BAND",
                                            "DOT11_5_GHZ_BAND",
                                            "DOT11_6_GHZ_BAND",
                                            "DOT11_INVALID_BAND"
                                        ],
                                        "type": "string"
                                    },
                                    "radioPolicySlot2Enabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "slot0Enabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "slot1Enabled": {
                                        "default": false,
                                        "type": "boolean"
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
