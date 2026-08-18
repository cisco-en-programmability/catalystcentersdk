"""Cisco Catalyst Center UpdateApplicationHealthScoreDefinitionForTheGivenId data model.

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


class JSONSchemaValidatorA776C50Bb5Fb397E47D3E5F63A371:
    """UpdateApplicationHealthScoreDefinitionForTheGivenId request schema
    definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "properties": {
                                "badDefaultValue": {
                                    "type": "number"
                                },
                                "badMaxValue": {
                                    "type": "number"
                                },
                                "badMinValue": {
                                    "type": "number"
                                },
                                "badValue": {
                                    "type": "number"
                                },
                                "definitionType": {
                                    "default": "DEFAULT",
                                    "enum": [
                                        "CUSTOM",
                                        "DEFAULT"
                                    ],
                                    "type": "string"
                                },
                                "goodDefaultValue": {
                                    "type": "number"
                                },
                                "goodMaxValue": {
                                    "type": "number"
                                },
                                "goodMinValue": {
                                    "type": "number"
                                },
                                "goodValue": {
                                    "type": "number"
                                },
                                "greatDefaultValue": {
                                    "type": "number"
                                },
                                "greatMaxValue": {
                                    "type": "number"
                                },
                                "greatMinValue": {
                                    "type": "number"
                                },
                                "greatValue": {
                                    "type": "number"
                                },
                                "id": {
                                    "type": "string"
                                },
                                "includeForHealthScore": {
                                    "type": "boolean"
                                },
                                "includeForHealthScoreDefault": {
                                    "type": "boolean"
                                },
                                "kpiName": {
                                    "enum": [
                                        "packetLoss",
                                        "jitter",
                                        "latency",
                                        "appDelay"
                                    ],
                                    "type": "string"
                                },
                                "lastModified": {
                                    "type": "integer"
                                },
                                "poorDefaultValue": {
                                    "type": "number"
                                },
                                "poorMaxValue": {
                                    "type": "number"
                                },
                                "poorMinValue": {
                                    "type": "number"
                                },
                                "poorValue": {
                                    "type": "number"
                                },
                                "trafficClass": {
                                    "enum": [
                                        "voip-telephony",
                                        "multimedia-conferencing",
                                        "multimedia-streaming",
                                        "real-time-interactive",
                                        "broadcast-video",
                                        "signaling",
                                        "network-control",
                                        "ops-admin-mgmt",
                                        "transactional-data",
                                        "bulk-data"
                                    ],
                                    "type": "string"
                                },
                                "unit": {
                                    "enum": [
                                        "sec",
                                        "msec",
                                        "percent"
                                    ],
                                    "type": "string"
                                },
                                "weightDefaultValue": {
                                    "maximum": 10,
                                    "minimum": 1,
                                    "type": "integer"
                                },
                                "weightValue": {
                                    "maximum": 10,
                                    "minimum": 1,
                                    "type": "integer"
                                }
                            },
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
