"""Cisco Catalyst Center GetConfigurationsForRlanProfileFeatureOnAWirelessController data model.

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


class JSONSchemaValidatorCb16D44FD52D5C02B299587A2E1860F0:
    """GetConfigurationsForRlanProfileFeatureOnAWirelessController
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
                                        "default": "RLAN_PROFILE",
                                        "enum": [
                                            "RLAN_PROFILE"
                                        ],
                                        "type": "string"
                                    },
                                    "deviceVersion": {
                                        "default": "26.01",
                                        "type": "string"
                                    },
                                    "dot1xEapIdRetrySettingEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "dot1xEapReqMaxRetries": {
                                        "maximum": 20,
                                        "minimum": 0,
                                        "type": "integer"
                                    },
                                    "dot1xEapReqTimeout": {
                                        "maximum": 120,
                                        "minimum": 1,
                                        "type": "integer"
                                    },
                                    "dot1xEapRetrySettingEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "dot1xEapidReqRetries": {
                                        "maximum": 20,
                                        "minimum": 1,
                                        "type": "integer"
                                    },
                                    "dot1xEapidReqTimeout": {
                                        "maximum": 120,
                                        "minimum": 1,
                                        "type": "integer"
                                    },
                                    "dot1xEnabled": {
                                        "type": "boolean"
                                    },
                                    "id": {
                                        "type": "string"
                                    },
                                    "localAuthEapProfileName": {
                                        "type": "string"
                                    },
                                    "localEapAuthEnabled": {
                                        "type": "boolean"
                                    },
                                    "maxAssociatedClients": {
                                        "default": 0,
                                        "maximum": 64000,
                                        "minimum": 0,
                                        "type": "integer"
                                    },
                                    "mdnsSdMode": {
                                        "default": "MDNS_SD_BRIDGING",
                                        "enum": [
                                            "MDNS_SD_BRIDGING",
                                            "MDNS_SD_DROP",
                                            "MDNS_SD_GATEWAY"
                                        ],
                                        "type": "string"
                                    },
                                    "rlanConfigAuthList": {
                                        "type": "string"
                                    },
                                    "rlanConfigAuthListDot1x": {
                                        "type": "string"
                                    },
                                    "rlanConfigId": {
                                        "maximum": 128,
                                        "minimum": 1,
                                        "type": "integer"
                                    },
                                    "rlanConfigProfileName": {
                                        "type": "string"
                                    },
                                    "rlanFallbackType": {
                                        "default": "RLAN_AUTH_FBACK_NONE",
                                        "enum": [
                                            "RLAN_AUTH_FBACK_DOT1X",
                                            "RLAN_AUTH_FBACK_MACFILTER",
                                            "RLAN_AUTH_FBACK_NONE"
                                        ],
                                        "type": "string"
                                    },
                                    "rlanMacFilteringConfig": {
                                        "type": "string"
                                    },
                                    "statusEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "webAuthEnabled": {
                                        "type": "boolean"
                                    },
                                    "webAuthParamMap": {
                                        "type": "string"
                                    },
                                    "webPreAuthAclIpv6": {
                                        "maxLength": 31,
                                        "minLength": 0,
                                        "type": "string"
                                    },
                                    "webPreAuthAclV4": {
                                        "maxLength": 31,
                                        "minLength": 0,
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
