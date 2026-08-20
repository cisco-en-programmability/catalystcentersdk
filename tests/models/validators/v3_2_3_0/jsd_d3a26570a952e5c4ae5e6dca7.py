"""Cisco Catalyst Center GetConfigurationsForUrwbChannelListConfigFeatureOnAWirelessController data
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


class JSONSchemaValidatorD3A26570A952E5C4Ae5E6Dca7:
    """GetConfigurationsForUrwbChannelListConfigFeatureOnAWirelessControl
    ler request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "items": {
                                "properties": {
                                    "configType": {
                                        "default": "URWB_CHANNEL_LIST",
                                        "enum": [
                                            "URWB_CHANNEL_LIST"
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
                                    "radioProfileName": {
                                        "maxLength": 32,
                                        "minLength": 1,
                                        "type": "string"
                                    },
                                    "urwbChannelNumber": {
                                        "maximum": 233,
                                        "minimum": 1,
                                        "type": "integer"
                                    },
                                    "urwbChannelPriority": {
                                        "default": 0,
                                        "maximum": 65535,
                                        "minimum": 0,
                                        "type": "integer"
                                    },
                                    "urwbChannelWidth": {
                                        "type": "integer"
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
