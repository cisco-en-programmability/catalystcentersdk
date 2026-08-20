"""Cisco Catalyst Center GetConfigurationsForASpecificInstanceOfAUrwbProfileFeatureOnAWirelessControl
ler data model.

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


class JSONSchemaValidatorAbd5AcfF7C455E98CaaDd9F1Cdc3815:
    """GetConfigurationsForASpecificInstanceOfAUrwbProfileFeatureOnAWirel
    essController request schema definition."""

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
                                                    "default": "URWB_PROFILE",
                                                    "enum": [
                                                        "URWB_PROFILE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.18",
                                                    "type": "string"
                                                },
                                                "mobBackhaulCheckCoordinator": {
                                                    "default": "URWB_MBCC_DIS",
                                                    "enum": [
                                                        "URWB_MBCC_DIS",
                                                        "URWB_MBCC_HO_INH",
                                                        "URWB_MBCC_REL_SW"
                                                    ],
                                                    "type": "string"
                                                },
                                                "mobBackhaulCheckEthernet": {
                                                    "default": "URWB_MBCE_DIS",
                                                    "enum": [
                                                        "URWB_MBCE_DIS",
                                                        "URWB_MBCE_HO_INH",
                                                        "URWB_MBCE_REL_SW"
                                                    ],
                                                    "type": "string"
                                                },
                                                "mobRole": {
                                                    "default": "URWB_MOB_BASE",
                                                    "enum": [
                                                        "URWB_MOB_BASE",
                                                        "URWB_MOB_CLIENT",
                                                        "URWB_MOB_RELAY"
                                                    ],
                                                    "type": "string"
                                                },
                                                "mobRouteAdRedundancy": {
                                                    "default": 1,
                                                    "maximum": 5,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "mobRssiDeltaHigh": {
                                                    "default": 6,
                                                    "maximum": 96,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "mobRssiDeltaLow": {
                                                    "default": 3,
                                                    "maximum": 96,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "mobRssiDeltaThreshold": {
                                                    "default": 35,
                                                    "maximum": 96,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "mobScanAfter": {
                                                    "default": 0,
                                                    "maximum": 65535,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "mobScanIdle": {
                                                    "default": 0,
                                                    "maximum": 65535,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "mobScanRssiThreshold": {
                                                    "default": 0,
                                                    "maximum": 96,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "mobTimeout": {
                                                    "default": 800,
                                                    "type": "integer"
                                                },
                                                "mobWarmup": {
                                                    "default": 30000,
                                                    "maximum": 300000,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "mplsEth1FrameForwardingEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "mplsEthFilterMethod": {
                                                    "default": "URWB_EFM_NONE",
                                                    "enum": [
                                                        "URWB_EFM_ALL",
                                                        "URWB_EFM_LIST",
                                                        "URWB_EFM_NONE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "mplsHighAvailabilityEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "mplsHighAvailabilityTimeout": {
                                                    "default": 100,
                                                    "type": "integer"
                                                },
                                                "mplsUnicastFloodEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "mplsUnicastFloodLimits": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "mpoClassOfService": {
                                                    "default": 6,
                                                    "maximum": 7,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "mpoMaxLinks": {
                                                    "default": 2,
                                                    "maximum": 4,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "mpoMinRssi": {
                                                    "default": 20,
                                                    "maximum": 96,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "mpoStatus": {
                                                    "default": "URWB_MPO_DIS",
                                                    "enum": [
                                                        "URWB_MPO_DIS",
                                                        "URWB_MPO_RX",
                                                        "URWB_MPO_TXRX"
                                                    ],
                                                    "type": "string"
                                                },
                                                "mpoTelemetryEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "urwbProfileDescription": {
                                                    "maxLength": 128,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "urwbProfileEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "urwbProfileMcast": {
                                                    "default": "URWB_MCAST_DIS",
                                                    "enum": [
                                                        "URWB_MCAST_BCAST",
                                                        "URWB_MCAST_COORD_ONLY",
                                                        "URWB_MCAST_DIS"
                                                    ],
                                                    "type": "string"
                                                },
                                                "urwbProfileName": {
                                                    "maxLength": 128,
                                                    "minLength": 1,
                                                    "type": "string"
                                                },
                                                "urwbProfilePassphrase": {
                                                    "maxLength": 64,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "urwbProfileStrongNetkeyEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                }
                                            },
                                            "required": [
                                                "deviceVersion",
                                                "urwbProfileName"
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
                                                    "default": "URWB_PROFILE",
                                                    "enum": [
                                                        "URWB_PROFILE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "deviceVersion": {
                                                    "default": "26.01",
                                                    "type": "string"
                                                },
                                                "gratuitousArp": {
                                                    "default": "URWB_GRAT_ARP_DISABLE",
                                                    "enum": [
                                                        "URWB_GRAT_ARP_DELAY",
                                                        "URWB_GRAT_ARP_DISABLE",
                                                        "URWB_GRAT_ARP_ENABLE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "gratuitousArpDelay": {
                                                    "default": 150,
                                                    "maximum": 2147483647,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "mobBackhaulCheckCoordinator": {
                                                    "default": "URWB_MBCC_DIS",
                                                    "enum": [
                                                        "URWB_MBCC_DIS",
                                                        "URWB_MBCC_HO_INH",
                                                        "URWB_MBCC_REL_SW"
                                                    ],
                                                    "type": "string"
                                                },
                                                "mobBackhaulCheckEthernet": {
                                                    "default": "URWB_MBCE_DIS",
                                                    "enum": [
                                                        "URWB_MBCE_DIS",
                                                        "URWB_MBCE_HO_INH",
                                                        "URWB_MBCE_REL_SW"
                                                    ],
                                                    "type": "string"
                                                },
                                                "mobFastDrop": {
                                                    "default": 0,
                                                    "maximum": 65535,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "mobRole": {
                                                    "default": "URWB_MOB_BASE",
                                                    "enum": [
                                                        "URWB_MOB_BASE",
                                                        "URWB_MOB_CLIENT",
                                                        "URWB_MOB_RELAY"
                                                    ],
                                                    "type": "string"
                                                },
                                                "mobRouteAdRedundancy": {
                                                    "default": 1,
                                                    "maximum": 5,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "mobRssiDeltaHigh": {
                                                    "default": 6,
                                                    "maximum": 96,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "mobRssiDeltaLow": {
                                                    "default": 3,
                                                    "maximum": 96,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "mobRssiDeltaThreshold": {
                                                    "default": 35,
                                                    "maximum": 96,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "mobScanAfter": {
                                                    "default": 0,
                                                    "maximum": 65535,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "mobScanIdle": {
                                                    "default": 0,
                                                    "maximum": 65535,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "mobScanRssiThreshold": {
                                                    "default": 0,
                                                    "maximum": 96,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "mobTimeout": {
                                                    "default": 800,
                                                    "type": "integer"
                                                },
                                                "mobWarmup": {
                                                    "default": 30000,
                                                    "maximum": 300000,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "mplsEth1FrameForwardingEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "mplsEthFilterMethod": {
                                                    "default": "URWB_EFM_NONE",
                                                    "enum": [
                                                        "URWB_EFM_ALL",
                                                        "URWB_EFM_LIST",
                                                        "URWB_EFM_NONE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "mplsHighAvailabilityEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "mplsHighAvailabilityTimeout": {
                                                    "default": 100,
                                                    "type": "integer"
                                                },
                                                "mplsUnicastFloodEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "mplsUnicastFloodLimits": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "mpoClassOfService": {
                                                    "default": 6,
                                                    "maximum": 7,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "mpoMaxLinks": {
                                                    "default": 2,
                                                    "maximum": 4,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "mpoMinRssi": {
                                                    "default": 20,
                                                    "maximum": 96,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "mpoStatus": {
                                                    "default": "URWB_MPO_DIS",
                                                    "enum": [
                                                        "URWB_MPO_DIS",
                                                        "URWB_MPO_RX",
                                                        "URWB_MPO_TXRX"
                                                    ],
                                                    "type": "string"
                                                },
                                                "mpoTelemetryEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "qosmapPriority0": {
                                                    "default": 0,
                                                    "maximum": 7,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "qosmapPriority1": {
                                                    "default": 1,
                                                    "maximum": 7,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "qosmapPriority2": {
                                                    "default": 2,
                                                    "maximum": 7,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "qosmapPriority3": {
                                                    "default": 3,
                                                    "maximum": 7,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "qosmapPriority4": {
                                                    "default": 4,
                                                    "maximum": 7,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "qosmapPriority5": {
                                                    "default": 5,
                                                    "maximum": 7,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "qosmapPriority6": {
                                                    "default": 6,
                                                    "maximum": 7,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "qosmapPriority7": {
                                                    "default": 7,
                                                    "maximum": 7,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "urwbProfileDescription": {
                                                    "maxLength": 128,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "urwbProfileEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "urwbProfileMcast": {
                                                    "default": "URWB_MCAST_DIS",
                                                    "enum": [
                                                        "URWB_MCAST_BCAST",
                                                        "URWB_MCAST_COORD_ONLY",
                                                        "URWB_MCAST_DIS"
                                                    ],
                                                    "type": "string"
                                                },
                                                "urwbProfileName": {
                                                    "maxLength": 128,
                                                    "minLength": 1,
                                                    "type": "string"
                                                },
                                                "urwbProfilePassphrase": {
                                                    "maxLength": 64,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "urwbProfileStrongNetkeyEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                }
                                            },
                                            "required": [
                                                "deviceVersion",
                                                "urwbProfileName"
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
