"""Cisco Catalyst Center GetConfigurationsForAccessPointFeatureOnAWirelessControllerApPpeConfigs data
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


class JSONSchemaValidatorAa6Bd35D6B85F5FBb6D38Abd0A02283:
    """GetConfigurationsForAccessPointFeatureOnAWirelessControllerApPpeCo
    nfigs request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "items": {
                                "properties": {
                                    "apPowerProfileName": {
                                        "maxLength": 128,
                                        "minLength": 1,
                                        "type": "string"
                                    },
                                    "apPpeInterfaceUnset": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "apPpeSequenceNumber": {
                                        "maximum": 4294967295,
                                        "minimum": 0,
                                        "type": "integer"
                                    },
                                    "configType": {
                                        "default": "AP_PPE",
                                        "enum": [
                                            "AP_PPE"
                                        ],
                                        "type": "string"
                                    },
                                    "deviceVersion": {
                                        "default": "26.01",
                                        "type": "string"
                                    },
                                    "ethernetId": {
                                        "enum": [
                                            "AP_PP_INTF_GB_ETH_0",
                                            "AP_PP_INTF_GB_ETH_1",
                                            "AP_PP_INTF_LAN_PORT_1",
                                            "AP_PP_INTF_LAN_PORT_2",
                                            "AP_PP_INTF_LAN_PORT_3"
                                        ],
                                        "type": "string"
                                    },
                                    "ethernetSpeed": {
                                        "enum": [
                                            "ETH_SPEED_100_MBPS",
                                            "ETH_SPEED_1000_MBPS",
                                            "ETH_SPEED_2500_MBPS",
                                            "ETH_SPEED_5000_MBPS"
                                        ],
                                        "type": "string"
                                    },
                                    "ethernetState": {
                                        "enum": [
                                            "AP_PP_STATE_DOWN"
                                        ],
                                        "type": "string"
                                    },
                                    "id": {
                                        "type": "string"
                                    },
                                    "radioId": {
                                        "enum": [
                                            "AP_PP_INTF_RADIO_24_GHZ",
                                            "AP_PP_INTF_RADIO_5_GHZ",
                                            "AP_PP_INTF_RADIO_6_GHZ",
                                            "AP_PP_INTF_RADIO_SEC_5_GHZ"
                                        ],
                                        "type": "string"
                                    },
                                    "radioSpatialStream": {
                                        "enum": [
                                            "RADIO_SPATIAL_STREAM_1",
                                            "RADIO_SPATIAL_STREAM_2",
                                            "RADIO_SPATIAL_STREAM_3",
                                            "RADIO_SPATIAL_STREAM_4",
                                            "RADIO_SPATIAL_STREAM_8"
                                        ],
                                        "type": "string"
                                    },
                                    "radioState": {
                                        "enum": [
                                            "AP_PP_STATE_DOWN"
                                        ],
                                        "type": "string"
                                    },
                                    "usbId": {
                                        "enum": [
                                            "AP_PP_INTF_USB_0"
                                        ],
                                        "type": "string"
                                    },
                                    "usbState": {
                                        "enum": [
                                            "AP_PP_STATE_DOWN"
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
