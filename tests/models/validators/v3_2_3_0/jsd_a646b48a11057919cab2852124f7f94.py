"""Cisco Catalyst Center GetConfigurationsForRlanPolicyFeatureOnAWirelessControllerConnectivity data
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


class JSONSchemaValidatorA646B48A11057919Cab2852124F7F94:
    """GetConfigurationsForRlanPolicyFeatureOnAWirelessControllerConnecti
    vity request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "items": {
                                "properties": {
                                    "aaaOverrideEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "arpRateNoneEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "arprateBurstInterval": {
                                        "default": 5,
                                        "maximum": 255,
                                        "minimum": 3,
                                        "type": "integer"
                                    },
                                    "arprateParamsRatePps": {
                                        "default": 100,
                                        "maximum": 1500,
                                        "minimum": 15,
                                        "type": "integer"
                                    },
                                    "blocklistEnabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "blocklistTimeout": {
                                        "default": 60,
                                        "maximum": 2147483647,
                                        "minimum": 0,
                                        "type": "integer"
                                    },
                                    "centralDhcpEnabled": {
                                        "type": "boolean"
                                    },
                                    "centralSwitchingEnabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "configType": {
                                        "default": "RLAN_POLICY",
                                        "enum": [
                                            "RLAN_POLICY"
                                        ],
                                        "type": "string"
                                    },
                                    "deviceVersion": {
                                        "default": "26.01",
                                        "type": "string"
                                    },
                                    "dhcpEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "dhcpServerVrfName": {
                                        "type": "string"
                                    },
                                    "hostModeDataVlanId": {
                                        "type": "integer"
                                    },
                                    "id": {
                                        "type": "string"
                                    },
                                    "ndpRateNoneEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "ndpRateParamsBurstInterval": {
                                        "default": 5,
                                        "maximum": 255,
                                        "minimum": 3,
                                        "type": "integer"
                                    },
                                    "ndpRatePpsLimit": {
                                        "default": 100,
                                        "maximum": 1500,
                                        "minimum": 15,
                                        "type": "integer"
                                    },
                                    "poeEnabled": {
                                        "type": "boolean"
                                    },
                                    "preAuthEnabled": {
                                        "type": "boolean"
                                    },
                                    "rlanAaaPolicyName": {
                                        "default": "default-aaa-policy",
                                        "type": "string"
                                    },
                                    "rlanFabricProfileName": {
                                        "type": "string"
                                    },
                                    "rlanPolicyAcctList": {
                                        "type": "string"
                                    },
                                    "rlanPolicyDhcpServerIpv4": {
                                        "type": "string"
                                    },
                                    "rlanPolicyIpv4AclName": {
                                        "maxLength": 31,
                                        "minLength": 0,
                                        "type": "string"
                                    },
                                    "rlanPolicyIpv6AclName": {
                                        "maxLength": 31,
                                        "minLength": 0,
                                        "type": "string"
                                    },
                                    "rlanPolicyMdnsPolicyName": {
                                        "default": "default-mdns-service-policy",
                                        "type": "string"
                                    },
                                    "rlanPolicyPowerLevelId": {
                                        "default": 4,
                                        "maximum": 4,
                                        "minimum": 1,
                                        "type": "integer"
                                    },
                                    "rlanPolicyProfileDesc": {
                                        "type": "string"
                                    },
                                    "rlanPolicyProfileHostMode": {
                                        "default": "SINGLE_HOST_MODE",
                                        "enum": [
                                            "MULTI_DOMAIN_MODE",
                                            "MULTI_HOST_MODE",
                                            "SINGLE_HOST_MODE"
                                        ],
                                        "type": "string"
                                    },
                                    "rlanPolicyProfileIntfName": {
                                        "default": "1",
                                        "type": "string"
                                    },
                                    "rlanPolicyProfileName": {
                                        "maxLength": 32,
                                        "minLength": 1,
                                        "type": "string"
                                    },
                                    "rlanPolicySessionTimeout": {
                                        "default": 28800,
                                        "maximum": 86400,
                                        "minimum": 0,
                                        "type": "integer"
                                    },
                                    "rlanViolationMode": {
                                        "enum": [
                                            "VIOLATION_MODE_PROTECT",
                                            "VIOLATION_MODE_REPLACE",
                                            "VIOLATION_MODE_SHUTDOWN"
                                        ],
                                        "type": "string"
                                    },
                                    "splitTunnelAclName": {
                                        "maxLength": 31,
                                        "minLength": 0,
                                        "type": "string"
                                    },
                                    "splitTunnelEnabled": {
                                        "type": "boolean"
                                    },
                                    "statusEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "upnRestrictEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "upnUnicastDisabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "voiceVlanId": {
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
                    "type": "object"
                }""".replace("\n" + " " * 16, "")))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                "{} is invalid. Reason: {}".format(request, e.message)
            )
