"""Cisco Catalyst Center GetConfigurationsForRadioProfileFeatureOnAWirelessControllerConnectivity
data model.

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


class JSONSchemaValidatorAb3Dfd193D350B2Bca510099D5875E9:
    """GetConfigurationsForRadioProfileFeatureOnAWirelessControllerConnec
    tivity request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "items": {
                                "properties": {
                                    "clusterID": {
                                        "default": "CiscoURWB",
                                        "type": "string"
                                    },
                                    "configType": {
                                        "default": "RADIO_ANTENNA_PROFILE",
                                        "enum": [
                                            "RADIO_ANTENNA_PROFILE"
                                        ],
                                        "type": "string"
                                    },
                                    "deviceVersion": {
                                        "default": "26.01",
                                        "type": "string"
                                    },
                                    "dtimPeriod": {
                                        "default": 1,
                                        "maximum": 255,
                                        "minimum": 1,
                                        "type": "integer"
                                    },
                                    "id": {
                                        "type": "string"
                                    },
                                    "keyControlRotationTimeOut": {
                                        "default": 15,
                                        "type": "integer"
                                    },
                                    "meshBackhaul": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "meshDesignatedDownlink": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "numAntEnabled": {
                                        "default": 0,
                                        "maximum": 8,
                                        "minimum": 0,
                                        "type": "integer"
                                    },
                                    "radioProfileBand": {
                                        "default": "DOT11_INVALID_BAND",
                                        "enum": [
                                            "DOT11_2_DOT_4_GHZ_BAND",
                                            "DOT11_5_GHZ_BAND",
                                            "DOT11_6_GHZ_BAND",
                                            "DOT11_INVALID_BAND"
                                        ],
                                        "type": "string"
                                    },
                                    "radioProfileBeamSteerMode": {
                                        "enum": [
                                            "BEAM_SELECT_NARROW",
                                            "BEAM_SELECT_NARROW_10",
                                            "BEAM_SELECT_NARROW_20",
                                            "BEAM_SELECT_NO_CONFIG",
                                            "BEAM_SELECT_WIDE"
                                        ],
                                        "type": "string"
                                    },
                                    "radioProfileDesc": {
                                        "maxLength": 64,
                                        "minLength": 0,
                                        "type": "string"
                                    },
                                    "radioProfileName": {
                                        "maxLength": 32,
                                        "minLength": 1,
                                        "type": "string"
                                    },
                                    "towerID": {
                                        "type": "string"
                                    },
                                    "urwbAutoscanEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "urwbChannel": {
                                        "default": 1,
                                        "maximum": 233,
                                        "minimum": 1,
                                        "type": "integer"
                                    },
                                    "urwbChannelWidth": {
                                        "default": "RRM_CHANNEL_WIDTH_20_MHZ",
                                        "enum": [
                                            "RRM_CHANNEL_WIDTH_160_MHZ",
                                            "RRM_CHANNEL_WIDTH_20_MHZ",
                                            "RRM_CHANNEL_WIDTH_320_MHZ",
                                            "RRM_CHANNEL_WIDTH_40_MHZ",
                                            "RRM_CHANNEL_WIDTH_80_80_MHZ",
                                            "RRM_CHANNEL_WIDTH_80_MHZ"
                                        ],
                                        "type": "string"
                                    },
                                    "urwbCrypto": {
                                        "default": "URWB_RAD_CRYPT_FXKEY",
                                        "enum": [
                                            "URWB_RAD_CRYPT_FXKEY",
                                            "URWB_RAD_CRYPT_NONE",
                                            "URWB_RAD_CRYPT_ROTKEY"
                                        ],
                                        "type": "string"
                                    },
                                    "urwbDot11AcMaxMcs": {
                                        "default": 9,
                                        "maximum": 9,
                                        "minimum": 0,
                                        "type": "integer"
                                    },
                                    "urwbDot11AxMaxMcs": {
                                        "default": 9,
                                        "maximum": 11,
                                        "minimum": 0,
                                        "type": "integer"
                                    },
                                    "urwbDot11NMaxMcs": {
                                        "default": 7,
                                        "maximum": 7,
                                        "minimum": 0,
                                        "type": "integer"
                                    },
                                    "urwbMaxLinkDistance": {
                                        "default": 3,
                                        "maximum": 99,
                                        "minimum": 0,
                                        "type": "integer"
                                    },
                                    "urwbMcsDot11Type": {
                                        "default": "URWB_80211_NONE",
                                        "enum": [
                                            "URWB_80211_NONE",
                                            "URWB_80211AC",
                                            "URWB_80211AX",
                                            "URWB_80211N"
                                        ],
                                        "type": "string"
                                    },
                                    "urwbPktRetries": {
                                        "default": 32,
                                        "maximum": 32,
                                        "minimum": 0,
                                        "type": "integer"
                                    },
                                    "urwbRole": {
                                        "default": "URWB_RAD_ROLE_NONE",
                                        "enum": [
                                            "URWB_RAD_FIXED",
                                            "URWB_RAD_MOB",
                                            "URWB_RAD_PTMP",
                                            "URWB_RAD_ROLE_NONE"
                                        ],
                                        "type": "string"
                                    },
                                    "urwbRssiThreshold": {
                                        "default": 0,
                                        "maximum": 96,
                                        "minimum": 0,
                                        "type": "integer"
                                    },
                                    "watRadioAdminState": {
                                        "default": "WAT_DISABLED",
                                        "enum": [
                                            "WAT_ALWAYS",
                                            "WAT_DISABLED"
                                        ],
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
