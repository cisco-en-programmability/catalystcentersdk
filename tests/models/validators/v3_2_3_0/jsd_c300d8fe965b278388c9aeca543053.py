"""Cisco Catalyst Center GETSSIDBYID data model.

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


class JSONSchemaValidatorC300D8Fe965B278388C9Aeca543053:
    """GETSSIDBYID request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "properties": {
                                "aaaOverride": {
                                    "type": "boolean"
                                },
                                "acctServers": {
                                    "items": {
                                        "type": "string"
                                    },
                                    "maxLength": 6,
                                    "type": "array"
                                },
                                "aclName": {
                                    "type": "string"
                                },
                                "authServer": {
                                    "enum": [
                                        "auth_ise",
                                        "auth_internal",
                                        "auth_external"
                                    ],
                                    "type": "string"
                                },
                                "authServers": {
                                    "items": {
                                        "type": "string"
                                    },
                                    "maxLength": 6,
                                    "type": "array"
                                },
                                "authType": {
                                    "enum": [
                                        "WPA2_ENTERPRISE",
                                        "WPA2_PERSONAL",
                                        "OPEN",
                                        "WPA3_ENTERPRISE",
                                        "WPA3_PERSONAL",
                                        "WPA2_WPA3_PERSONAL",
                                        "WPA2_WPA3_ENTERPRISE",
                                        "OPEN-SECURED"
                                    ],
                                    "type": "string"
                                },
                                "basicServiceSetClientIdleTimeout": {
                                    "default": 300,
                                    "maximum": 100000,
                                    "type": "integer"
                                },
                                "basicServiceSetMaxIdleEnable": {
                                    "type": "boolean"
                                },
                                "cckmTsfTolerance": {
                                    "maximum": 5000,
                                    "minimum": 1000,
                                    "type": "integer"
                                },
                                "clientExclusionEnable": {
                                    "type": "boolean"
                                },
                                "clientExclusionTimeout": {
                                    "default": 180,
                                    "maximum": 2147483647,
                                    "minimum": 0,
                                    "type": "integer"
                                },
                                "clientRateLimit": {
                                    "maximum": 100000000000,
                                    "minimum": 8000,
                                    "type": "integer"
                                },
                                "coverageHoleDetectionEnable": {
                                    "type": "boolean"
                                },
                                "directedMulticastServiceEnable": {
                                    "type": "boolean"
                                },
                                "egressQos": {
                                    "enum": [
                                        "PLATINUM",
                                        "SILVER",
                                        "GOLD",
                                        "BRONZE"
                                    ],
                                    "type": "string"
                                },
                                "externalAuthIpAddress": {
                                    "type": "string"
                                },
                                "fastTransition": {
                                    "enum": [
                                        "ADAPTIVE",
                                        "ENABLE",
                                        "DISABLE"
                                    ],
                                    "type": "string"
                                },
                                "fastTransitionOverTheDistributedSystemEnable": {
                                    "type": "boolean"
                                },
                                "ghz24Policy": {
                                    "enum": [
                                        "dot11-bg-only",
                                        "dot11-g-only"
                                    ],
                                    "type": "string"
                                },
                                "ghz6PolicyClientSteering": {
                                    "type": "boolean"
                                },
                                "id": {
                                    "type": "string"
                                },
                                "ingressQos": {
                                    "enum": [
                                        "PLATINUM-UP",
                                        "SILVER-UP",
                                        "GOLD-UP",
                                        "BRONZE-UP"
                                    ],
                                    "type": "string"
                                },
                                "inheritedSiteName": {
                                    "type": "string"
                                },
                                "inheritedSiteUUID": {
                                    "type": "string"
                                },
                                "ipv6AclName": {
                                    "type": "string"
                                },
                                "isApBeaconProtectionEnabled": {
                                    "type": "boolean"
                                },
                                "isAuthKey8021x": {
                                    "type": "boolean"
                                },
                                "isAuthKey8021xPlusFT": {
                                    "type": "boolean"
                                },
                                "isAuthKey8021x_SHA256": {
                                    "type": "boolean"
                                },
                                "isAuthKeyEasyPSK": {
                                    "type": "boolean"
                                },
                                "isAuthKeyOWE": {
                                    "type": "boolean"
                                },
                                "isAuthKeyPSK": {
                                    "type": "boolean"
                                },
                                "isAuthKeyPSKPlusFT": {
                                    "type": "boolean"
                                },
                                "isAuthKeyPSKSHA256": {
                                    "type": "boolean"
                                },
                                "isAuthKeySae": {
                                    "type": "boolean"
                                },
                                "isAuthKeySaeExt": {
                                    "type": "boolean"
                                },
                                "isAuthKeySaeExtPlusFT": {
                                    "type": "boolean"
                                },
                                "isAuthKeySaePlusFT": {
                                    "type": "boolean"
                                },
                                "isAuthKeySuiteB1921x": {
                                    "type": "boolean"
                                },
                                "isAuthKeySuiteB1x": {
                                    "type": "boolean"
                                },
                                "isBroadcastSSID": {
                                    "type": "boolean"
                                },
                                "isCckmEnabled": {
                                    "type": "boolean"
                                },
                                "isCustomNasIdOptions": {
                                    "type": "boolean"
                                },
                                "isEnabled": {
                                    "type": "boolean"
                                },
                                "isFastLaneEnabled": {
                                    "type": "boolean"
                                },
                                "isHex": {
                                    "type": "boolean"
                                },
                                "isLoadBalancingEnabledForAcctGroup": {
                                    "default": false,
                                    "type": "boolean"
                                },
                                "isLoadBalancingEnabledForAuthGroup": {
                                    "default": false,
                                    "type": "boolean"
                                },
                                "isMacFilteringEnabled": {
                                    "type": "boolean"
                                },
                                "isPosturingEnabled": {
                                    "type": "boolean"
                                },
                                "isRadiusProfilingEnabled": {
                                    "type": "boolean"
                                },
                                "isRandomMacFilterEnabled": {
                                    "type": "boolean"
                                },
                                "l3AuthType": {
                                    "enum": [
                                        "open",
                                        "web_auth"
                                    ],
                                    "type": "string"
                                },
                                "managementFrameProtectionClientprotection": {
                                    "enum": [
                                        "OPTIONAL",
                                        "DISABLED",
                                        "REQUIRED"
                                    ],
                                    "type": "string"
                                },
                                "multiPSKSettings": {
                                    "items": {
                                        "properties": {
                                            "passphrase": {
                                                "maxLength": 63,
                                                "minLength": 8,
                                                "type": "string"
                                            },
                                            "passphraseType": {
                                                "enum": [
                                                    "ASCII",
                                                    "HEX"
                                                ],
                                                "type": "string"
                                            },
                                            "priority": {
                                                "maximum": 4,
                                                "minimum": 0,
                                                "type": "integer"
                                            }
                                        },
                                        "type": "object"
                                    },
                                    "type": "array"
                                },
                                "nasOptions": {
                                    "items": {
                                        "enum": [
                                            "AP ETH Mac Address",
                                            "AP IP Address",
                                            "AP Location",
                                            "AP MAC Address",
                                            "AP Name",
                                            "AP Policy Tag",
                                            "AP Site Tag",
                                            "SSID",
                                            "System IP Address",
                                            "System MAC Address",
                                            "System Name",
                                            "Custom-NAS-Option"
                                        ],
                                        "type": "string"
                                    },
                                    "maxLength": 3,
                                    "type": "array"
                                },
                                "neighborListEnable": {
                                    "type": "boolean"
                                },
                                "openSsid": {
                                    "type": "string"
                                },
                                "passphrase": {
                                    "maxLength": 63,
                                    "minLength": 8,
                                    "type": "string"
                                },
                                "policyProfileName": {
                                    "maxLength": 32,
                                    "type": "string"
                                },
                                "profileName": {
                                    "maxLength": 32,
                                    "type": "string"
                                },
                                "protectedManagementFrame": {
                                    "enum": [
                                        "OPTIONAL",
                                        "DISABLED",
                                        "REQUIRED"
                                    ],
                                    "type": "string"
                                },
                                "rsnCipherSuiteCcmp128": {
                                    "type": "boolean"
                                },
                                "rsnCipherSuiteCcmp256": {
                                    "type": "boolean"
                                },
                                "rsnCipherSuiteGcmp128": {
                                    "type": "boolean"
                                },
                                "rsnCipherSuiteGcmp256": {
                                    "type": "boolean"
                                },
                                "sessionTimeOut": {
                                    "default": 1800,
                                    "maximum": 86400,
                                    "minimum": 1,
                                    "type": "integer"
                                },
                                "sessionTimeOutEnable": {
                                    "type": "boolean"
                                },
                                "sleepingClientEnable": {
                                    "type": "boolean"
                                },
                                "sleepingClientTimeout": {
                                    "default": 720,
                                    "maximum": 43200,
                                    "minimum": 10,
                                    "type": "integer"
                                },
                                "ssid": {
                                    "maxLength": 32,
                                    "type": "string"
                                },
                                "ssidRadioType": {
                                    "enum": [
                                        "Triple band operation(2.4GHz, 5GHz and 6GHz)",
                                        "5GHz only",
                                        "2.4GHz only",
                                        "6GHz only",
                                        "2.4 and 5 GHz",
                                        "2.4 and 6 GHz",
                                        "5 and 6 GHz"
                                    ],
                                    "type": "string"
                                },
                                "urlAclName": {
                                    "type": "string"
                                },
                                "webPassthrough": {
                                    "type": "boolean"
                                },
                                "wlanBandSelectEnable": {
                                    "type": "boolean"
                                },
                                "wlanType": {
                                    "enum": [
                                        "Enterprise",
                                        "Guest"
                                    ],
                                    "type": "string"
                                }
                            },
                            "required": [
                                "authType",
                                "ssid",
                                "wlanType"
                            ],
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
