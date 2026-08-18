"""Cisco Catalyst Center GetConfigurationsForMeshProfileFeatureOnAWirelessController data model.

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


class JSONSchemaValidatorA99646B29677575599F9C24Bf68Abea0:
    """GetConfigurationsForMeshProfileFeatureOnAWirelessController
    request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "items": {
                                "properties": {
                                    "aggregatedMsduEnabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "authenticationMethod": {
                                        "type": "string"
                                    },
                                    "authorizationMethod": {
                                        "type": "string"
                                    },
                                    "backgroundScanEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "backhaulClientAccessEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "batteryStateEnabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "bgnStrictMatchEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "bhaulTxRateDot11BgType": {
                                        "default": "MESH_BHAUL_RATE_AUTO",
                                        "enum": [
                                            "MESH_BHAUL_RATE_AUTO",
                                            "MESH_BHAUL_RATE_TYPE_DOT11ABG",
                                            "MESH_BHAUL_RATE_TYPE_DOT11AC",
                                            "MESH_BHAUL_RATE_TYPE_DOT11AX",
                                            "MESH_BHAUL_RATE_TYPE_DOT11N"
                                        ],
                                        "type": "string"
                                    },
                                    "configType": {
                                        "default": "MESH_PROFILE",
                                        "enum": [
                                            "MESH_PROFILE"
                                        ],
                                        "type": "string"
                                    },
                                    "deviceVersion": {
                                        "default": "26.01",
                                        "type": "string"
                                    },
                                    "dot11ADot11AxSpatialStreamA": {
                                        "default": 1,
                                        "maximum": 8,
                                        "minimum": 1,
                                        "type": "integer"
                                    },
                                    "dot11AcMcsIdx": {
                                        "default": 0,
                                        "maximum": 9,
                                        "minimum": 0,
                                        "type": "integer"
                                    },
                                    "dot11AxSpatialStreamA": {
                                        "default": 1,
                                        "maximum": 8,
                                        "minimum": 1,
                                        "type": "integer"
                                    },
                                    "dot11AxSpatialStreamBg": {
                                        "default": 1,
                                        "maximum": 4,
                                        "minimum": 1,
                                        "type": "integer"
                                    },
                                    "dot11BgDot11AxMcsIdx": {
                                        "default": 0,
                                        "maximum": 11,
                                        "minimum": 0,
                                        "type": "integer"
                                    },
                                    "dot11BgDot11AxSpatialStreamBg": {
                                        "default": 1,
                                        "maximum": 4,
                                        "minimum": 1,
                                        "type": "integer"
                                    },
                                    "fastTeardownEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "fastTeardownInterval": {
                                        "default": 1,
                                        "maximum": 10,
                                        "minimum": 1,
                                        "type": "integer"
                                    },
                                    "fastTeardownLatencyThresh": {
                                        "default": 10,
                                        "maximum": 500,
                                        "minimum": 1,
                                        "type": "integer"
                                    },
                                    "fastTeardownRetries": {
                                        "default": 4,
                                        "maximum": 10,
                                        "minimum": 1,
                                        "type": "integer"
                                    },
                                    "id": {
                                        "type": "string"
                                    },
                                    "latExcdThreshold": {
                                        "default": 8,
                                        "maximum": 30,
                                        "minimum": 1,
                                        "type": "integer"
                                    },
                                    "meshProfBridgegroupname": {
                                        "type": "string"
                                    },
                                    "meshProfCcnMode": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "meshProfConvMethod": {
                                        "default": "MESH_CONVERGENCE_STANDARD",
                                        "enum": [
                                            "MESH_CONVERGENCE_FAST",
                                            "MESH_CONVERGENCE_NOISE_TOLERANT_FAST",
                                            "MESH_CONVERGENCE_STANDARD",
                                            "MESH_CONVERGENCE_VERYFAST"
                                        ],
                                        "type": "string"
                                    },
                                    "meshProfDescription": {
                                        "type": "string"
                                    },
                                    "meshProfEthBridgingEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "meshProfEthVlanTransparent": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "meshProfFullSectorDfs": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "meshProfIdsStateEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "meshProfLscOnlyAuth": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "meshProfMapFastAncestorFind": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "meshProfMulticastMode": {
                                        "default": "MESH_MULTICAST_MODE_INOUT",
                                        "enum": [
                                            "MESH_MULTICAST_MODE_IN",
                                            "MESH_MULTICAST_MODE_INOUT",
                                            "MESH_MULTICAST_MODE_REGULAR"
                                        ],
                                        "type": "string"
                                    },
                                    "meshProfRange": {
                                        "default": 12000,
                                        "maximum": 132000,
                                        "minimum": 150,
                                        "type": "integer"
                                    },
                                    "meshProfRapEthDaisychain": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "meshProfSecurityMode": {
                                        "default": "MESH_SECURITY_MODE_EAP",
                                        "enum": [
                                            "MESH_SECURITY_MODE_EAP",
                                            "MESH_SECURITY_MODE_PSK"
                                        ],
                                        "type": "string"
                                    },
                                    "meshProfileName": {
                                        "maxLength": 32,
                                        "minLength": 0,
                                        "type": "string"
                                    },
                                    "profDaisychainStpRedundancy": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "scanChannelWidth": {
                                        "default": 20,
                                        "type": "integer"
                                    },
                                    "scanEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "scanUnii3Bias": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "scanUseUnii2": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "teardownKeepWirelessConn": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "teardownUplinkRecovInterval": {
                                        "default": 60,
                                        "maximum": 3600,
                                        "minimum": 1,
                                        "type": "integer"
                                    },
                                    "txRateDot11ADot11AxMcsIdx": {
                                        "default": 0,
                                        "maximum": 11,
                                        "minimum": 0,
                                        "type": "integer"
                                    },
                                    "txRateDot11aDot11acMcsIndex": {
                                        "default": 0,
                                        "maximum": 9,
                                        "minimum": 0,
                                        "type": "integer"
                                    },
                                    "txRateDot11aDot11nMcsIndex": {
                                        "default": 0,
                                        "maximum": 31,
                                        "minimum": 0,
                                        "type": "integer"
                                    },
                                    "txRateDot11aRate": {
                                        "default": "DATA_RATE_AUTO",
                                        "enum": [
                                            "DATA_RATE_11MBPS",
                                            "DATA_RATE_12MBPS",
                                            "DATA_RATE_18MBPS",
                                            "DATA_RATE_1MBPS",
                                            "DATA_RATE_24MBPS",
                                            "DATA_RATE_2ABPSM",
                                            "DATA_RATE_36MBPS",
                                            "DATA_RATE_48MBPS",
                                            "DATA_RATE_54MBPS",
                                            "DATA_RATE_5DOT5MBPS",
                                            "DATA_RATE_6MBPS",
                                            "DATA_RATE_9MBPS",
                                            "DATA_RATE_AUTO"
                                        ],
                                        "type": "string"
                                    },
                                    "txRateDot11aSpatialStream": {
                                        "default": 1,
                                        "maximum": 4,
                                        "minimum": 1,
                                        "type": "integer"
                                    },
                                    "txRateDot11aType": {
                                        "default": "MESH_BHAUL_RATE_AUTO",
                                        "enum": [
                                            "MESH_BHAUL_RATE_AUTO",
                                            "MESH_BHAUL_RATE_TYPE_DOT11ABG",
                                            "MESH_BHAUL_RATE_TYPE_DOT11AC",
                                            "MESH_BHAUL_RATE_TYPE_DOT11AX",
                                            "MESH_BHAUL_RATE_TYPE_DOT11N"
                                        ],
                                        "type": "string"
                                    },
                                    "txRateDot11bgDot11nMcsIndex": {
                                        "default": 0,
                                        "maximum": 31,
                                        "minimum": 0,
                                        "type": "integer"
                                    },
                                    "txRateDot11bgRate": {
                                        "default": "DATA_RATE_AUTO",
                                        "enum": [
                                            "DATA_RATE_11MBPS",
                                            "DATA_RATE_12MBPS",
                                            "DATA_RATE_18MBPS",
                                            "DATA_RATE_1MBPS",
                                            "DATA_RATE_24MBPS",
                                            "DATA_RATE_2ABPSM",
                                            "DATA_RATE_36MBPS",
                                            "DATA_RATE_48MBPS",
                                            "DATA_RATE_54MBPS",
                                            "DATA_RATE_5DOT5MBPS",
                                            "DATA_RATE_6MBPS",
                                            "DATA_RATE_9MBPS",
                                            "DATA_RATE_AUTO"
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
