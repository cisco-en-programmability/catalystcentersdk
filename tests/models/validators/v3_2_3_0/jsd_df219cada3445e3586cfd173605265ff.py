"""Cisco Catalyst Center GetConfigurationsForFlexProfileFeatureOnAWirelessControllerConnectivity data
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


class JSONSchemaValidatorDf219CadA3445E3586CfD173605265Ff:
    """GetConfigurationsForFlexProfileFeatureOnAWirelessControllerConnect
    ivity request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "items": {
                                "properties": {
                                    "acctRadiusServerGrpName": {
                                        "maxLength": 32,
                                        "type": "string"
                                    },
                                    "arpCaching": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "configType": {
                                        "default": "FLEX_PROFILE",
                                        "enum": [
                                            "FLEX_PROFILE"
                                        ],
                                        "type": "string"
                                    },
                                    "ctsInlineTagging": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "ctsProfileName": {
                                        "default": "default-sxp-profile",
                                        "type": "string"
                                    },
                                    "ctsRolebasedEnforce": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "deviceVersion": {
                                        "default": "26.01",
                                        "type": "string"
                                    },
                                    "eapFastProfileName": {
                                        "type": "string"
                                    },
                                    "efficientApUpgradeEnabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "fallbackRadioShut": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "flexOverlapIpEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "flexPolicyDescription": {
                                        "type": "string"
                                    },
                                    "flexPolicyDhcpBroadcast": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "flexPolicyHttpProxyIp": {
                                        "default": "0.0.0.0",
                                        "type": "string"
                                    },
                                    "flexPolicyHttpProxyPort": {
                                        "default": 0,
                                        "maximum": 65535,
                                        "minimum": 0,
                                        "type": "integer"
                                    },
                                    "flexPolicyJoinMinLatency": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "flexPolicyMdnsProfileName": {
                                        "type": "string"
                                    },
                                    "flexPolicyName": {
                                        "type": "string"
                                    },
                                    "flexPolicyNativeVlanId": {
                                        "default": 1,
                                        "maximum": 4094,
                                        "minimum": 1,
                                        "type": "integer"
                                    },
                                    "flexPolicyPmkDistMethod": {
                                        "enum": [
                                            "PMK_DIST_AP_TO_AP",
                                            "PMK_DIST_DCDS",
                                            "PMK_DIST_WLC_TO_AP"
                                        ],
                                        "type": "string"
                                    },
                                    "flexPolicyRadiusEnabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "flexPolicyRadiusServerGrpName": {
                                        "type": "string"
                                    },
                                    "flexPolicySecurityLeapEnabled": {
                                        "type": "boolean"
                                    },
                                    "flexPolicySecurityPeapEnabled": {
                                        "type": "boolean"
                                    },
                                    "flexPolicySecurityTlsEnabled": {
                                        "type": "boolean"
                                    },
                                    "homeApEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "id": {
                                        "type": "string"
                                    },
                                    "localRoamingEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "resilientMode": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "slaveMaxRetryCount": {
                                        "default": 0,
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
