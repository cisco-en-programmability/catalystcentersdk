"""Cisco Catalyst Center GetConfigurationsForRfTagFeatureOnAWirelessController data model.

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


class JSONSchemaValidatorF2965A923C56Fd9412B09Bea4De13D:
    """GetConfigurationsForRfTagFeatureOnAWirelessController request
    schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "items": {
                                "properties": {
                                    "apBeamState": {
                                        "default": "AP_BEAM_STATE_BORESIGHT",
                                        "enum": [
                                            "AP_BEAM_STATE_BORESIGHT",
                                            "AP_BEAM_STATE_FRONT_BACK",
                                            "AP_BEAM_STATE_INVALID",
                                            "AP_BEAM_STATE_WIDE"
                                        ],
                                        "type": "string"
                                    },
                                    "configType": {
                                        "default": "RF_TAG",
                                        "enum": [
                                            "RF_TAG"
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
                                    "rfTagDescription": {
                                        "type": "string"
                                    },
                                    "rfTagDot116GhzRfProfName": {
                                        "default": "default-rf-profile-6ghz",
                                        "type": "string"
                                    },
                                    "rfTagDot11ARfProfileName": {
                                        "default": "default_rf_5gh",
                                        "type": "string"
                                    },
                                    "rfTagDot11BRfProfileName": {
                                        "default": "default_rf_24gh",
                                        "type": "string"
                                    },
                                    "rfTagTagName": {
                                        "type": "string"
                                    },
                                    "rfTagUrwbProfileName": {
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
