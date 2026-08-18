"""Cisco Catalyst Center GetConfigurationsForASpecificInstanceOfADeployedDot11BeProfileFeatureOnAWire
lessController data model.

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


class JSONSchemaValidatorB493495AD7C65A75B41715A47C3B1Ff5:
    """GetConfigurationsForASpecificInstanceOfADeployedDot11BeProfileFeat
    ureOnAWirelessController request schema definition."""

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
                                                "configType": {
                                                    "default": "DOT11BE_PROFILE",
                                                    "enum": [
                                                        "DOT11BE_PROFILE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "description":
                 {
                                                    "maxLength": 64,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.15",
                                                    "type": "string"
                                                },
                                                "muMimoDownLink": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "muMimoUpLink": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "ofdmaDownLinkEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "ofdmaMultiRuEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "ofdmaUplinkEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "profileName": {
                                                    "maxLength": 31,
                                                    "minLength": 0,
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "deviceVersion",
                                                "profileName"
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
                                                "configType": {
                                                    "default": "DOT11BE_PROFILE",
                                                    "enum": [
                                                        "DOT11BE_PROFILE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "description":
                 {
                                                    "maxLength": 64,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.16",
                                                    "type": "string"
                                                },
                                                "muMimoDownLink": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "muMimoUpLink": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "ofdmaDownLinkEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "ofdmaMultiRuEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "ofdmaUplinkEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "profileName": {
                                                    "maxLength": 31,
                                                    "minLength": 0,
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "deviceVersion",
                                                "profileName"
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
                                                "configType": {
                                                    "default": "DOT11BE_PROFILE",
                                                    "enum": [
                                                        "DOT11BE_PROFILE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "description":
                 {
                                                    "maxLength": 64,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.17",
                                                    "type": "string"
                                                },
                                                "muMimoDownLink": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "muMimoUpLink": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "ofdmaDownLinkEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "ofdmaMultiRuEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "ofdmaUplinkEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "profileName": {
                                                    "maxLength": 31,
                                                    "minLength": 0,
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "deviceVersion",
                                                "profileName"
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
                                                "configType": {
                                                    "default": "DOT11BE_PROFILE",
                                                    "enum": [
                                                        "DOT11BE_PROFILE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "description":
                 {
                                                    "maxLength": 64,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.18",
                                                    "type": "string"
                                                },
                                                "dot11beProfileMlo24ghz": {
                                                    "enum": [
                                                        "ENUM_24GHZ_DISABLE",
                                                        "ENUM_24GHZ_ENABLE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "dot11beProfileMlo5ghz": {
                                                    "enum": [
                                                        "ENUM_5GHZ_DISABLE",
                                                        "ENUM_5GHZ_ENABLE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "dot11beProfileMlo6Ghz": {
                                                    "enum": [
                                                        "ENUM_6GHZ_DISABLE",
                                                        "ENUM_6GHZ_ENABLE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "mlo5ghzSec": {
                                                    "enum": [
                                                        "ENUM_5GHZ_SEC_DISABLE",
                                                        "ENUM_5GHZ_SEC_ENABLE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "muMimoDownLink": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "muMimoUpLink": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "ofdmaDownLinkEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "ofdmaMultiRuEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "ofdmaUplinkEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "profileName": {
                                                    "maxLength": 32,
                                                    "minLength": 1,
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "deviceVersion",
                                                "profileName"
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
                                                "configType": {
                                                    "default": "DOT11BE_PROFILE",
                                                    "enum": [
                                                        "DOT11BE_PROFILE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "description":
                 {
                                                    "maxLength": 64,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "26.01",
                                                    "type": "string"
                                                },
                                                "dot11beProfileMlo24ghz": {
                                                    "enum": [
                                                        "ENUM_24GHZ_DISABLE",
                                                        "ENUM_24GHZ_ENABLE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "dot11beProfileMlo5ghz": {
                                                    "enum": [
                                                        "ENUM_5GHZ_DISABLE",
                                                        "ENUM_5GHZ_ENABLE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "dot11beProfileMlo6Ghz": {
                                                    "enum": [
                                                        "ENUM_6GHZ_DISABLE",
                                                        "ENUM_6GHZ_ENABLE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "mlo5ghzSec": {
                                                    "enum": [
                                                        "ENUM_5GHZ_SEC_DISABLE",
                                                        "ENUM_5GHZ_SEC_ENABLE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "muMimoDownLink": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "muMimoUpLink": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "ofdmaDownLinkEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "ofdmaMultiRuEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "ofdmaUplinkEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "profileName": {
                                                    "maxLength": 32,
                                                    "minLength": 1,
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "deviceVersion",
                                                "profileName"
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
