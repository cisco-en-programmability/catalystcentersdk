"""Cisco Catalyst Center GetConfigurationsForPolicyProfileFeatureOnAWirelessController data model.

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


class JSONSchemaValidatorA550088518B5A5FBe71B20178Ada6E7:
    """GetConfigurationsForPolicyProfileFeatureOnAWirelessController
    request schema definition."""

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
                                    "aaaPolicyNacEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "aaaPolicyNacType": {
                                        "enum": [
                                            "NAC_SUPPORT_RADIUS",
                                            "NAC_SUPPORT_XWF"
                                        ],
                                        "type": "string"
                                    },
                                    "aaaPolicyName": {
                                        "default": "default-aaa-policy",
                                        "type": "string"
                                    },
                                    "aaaPolicyVlanFallbackEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "accountingList": {
                                        "type": "string"
                                    },
                                    "apEthmacEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "arpProxyStatusEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "arpRateNoneEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "autoqosProfileMode": {
                                        "default": "AUTOQOS_DISABLED",
                                        "enum": [
                                            "AUTOQOS_DISABLED",
                                            "AUTOQOS_ENTERPRISE",
                                            "AUTOQOS_FASTLANE",
                                            "AUTOQOS_GUEST",
                                            "AUTOQOS_VOICE"
                                        ],
                                        "type": "string"
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
                                    "callSnoopEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "centralAuthEnabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "centralDhcpEnabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "centralSwitchingEnabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "configType": {
                                        "default": "POLICY_PROFILE",
                                        "enum": [
                                            "POLICY_PROFILE"
                                        ],
                                        "type": "string"
                                    },
                                    "ctsPolicySgaclEnforceEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "deviceClassified": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "deviceVersion": {
                                        "default": "26.01",
                                        "type": "string"
                                    },
                                    "dhcpDnsOptionEnabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "dhcpEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "dhcpOpt82AsciiEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "dhcpOpt82Enabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "dhcpOpt82RidEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "dhcpOpt82VrfEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "dhcpOptionNoneEnabled": {
                                        "type": "boolean"
                                    },
                                    "dhcpParamsApLocation": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "dhcpParamsApNameEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "dhcpParamsPolicyTagEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "dhcpServerIpv4Addr": {
                                        "default": "0.0.0.0",
                                        "type": "string"
                                    },
                                    "dhcpServerVrfName": {
                                        "type": "string"
                                    },
                                    "dhcpTlvCachingEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "dot11TlvAcctEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "etAnalyticsTviEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "guestLanSessionTimeoutEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "hotspotAnqpServer": {
                                        "maxLength": 200,
                                        "minLength": 0,
                                        "type": "string"
                                    },
                                    "httpTlvCachingEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "id": {
                                        "type": "string"
                                    },
                                    "interfaceName": {
                                        "default": "1",
                                        "type": "string"
                                    },
                                    "ipMacBinding": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "ipv4AclName": {
                                        "type": "string"
                                    },
                                    "ipv6AclPolicyName": {
                                        "type": "string"
                                    },
                                    "isWlanPolicyDhcpApmacEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "l3AccessEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "linkLocalBridgingEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "mdnsServicePolicyName": {
                                        "default": "default-mdns-service-policy",
                                        "maxLength": 164,
                                        "type": "string"
                                    },
                                    "mobilityAnchorEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "multicastFiltered": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "multicastVlanId": {
                                        "maximum": 4094,
                                        "minimum": 1,
                                        "type": "integer"
                                    },
                                    "nbarProtocolDiscoveryEnabled": {
                                        "default": false,
                                        "type": "boolean"
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
                                    "ndpRatePps": {
                                        "default": 100,
                                        "maximum": 1500,
                                        "minimum": 15,
                                        "type": "integer"
                                    },
                                    "overrideNatPatEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "passiveClientEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "perClientQosEgressSvcName": {
                                        "maxLength": 80,
                                        "minLength": 0,
                                        "type": "string"
                                    },
                                    "perClientQosIngressServiceName": {
                                        "maxLength": 80,
                                        "minLength": 0,
                                        "type": "string"
                                    },
                                    "perSsidQosEgressServiceName": {
                                        "maxLength": 80,
                                        "minLength": 0,
                                        "type": "string"
                                    },
                                    "perSsidQosIngressServiceName": {
                                        "maxLength": 80,
                                        "minLength": 0,
                                        "type": "string"
                                    },
                                    "policyProfileName": {
                                        "type": "string"
                                    },
                                    "postAuthUrlFilterList": {
                                        "type": "string"
                                    },
                                    "preAuthUrlFilterList": {
                                        "type": "string"
                                    },
                                    "radiusProfilingEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "reanchorClassmapName": {
                                        "type": "string"
                                    },
                                    "sessionTimeOut": {
                                        "default": 28800,
                                        "maximum": 86400,
                                        "minimum": 0,
                                        "type": "integer"
                                    },
                                    "sipCacSend486BusyEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "sipCacSendDisAssoc": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "statusEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "subscriberPolicyName": {
                                        "type": "string"
                                    },
                                    "tunnelProfileName": {
                                        "maxLength": 128,
                                        "minLength": 0,
                                        "type": "string"
                                    },
                                    "umbrellaFlexModeForced": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "umbrellaParamMapName": {
                                        "type": "string"
                                    },
                                    "upnRestrictEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "upnUnicastDisabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "vlanCentralSwitching": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "wgbPolicyBroadcastTagging": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "wgbPolicyMulticastFw": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "wgbPolicyVlanEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "wlanAcctInterimEnabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "wlanArpBurstInterval": {
                                        "default": 5,
                                        "maximum": 255,
                                        "minimum": 3,
                                        "type": "integer"
                                    },
                                    "wlanArpRatePps": {
                                        "default": 100,
                                        "maximum": 1500,
                                        "minimum": 15,
                                        "type": "integer"
                                    },
                                    "wlanEncryptionVlanOsen": {
                                        "maxLength": 8,
                                        "minLength": 0,
                                        "type": "string"
                                    },
                                    "wlanFabricProfileName": {
                                        "type": "string"
                                    },
                                    "wlanFlexPolicySplitMacAcl": {
                                        "type": "string"
                                    },
                                    "wlanIdleThreshold": {
                                        "default": 0,
                                        "maximum": 4294967295,
                                        "minimum": 0,
                                        "type": "integer"
                                    },
                                    "wlanIdleTimeoutValue": {
                                        "default": 300,
                                        "maximum": 100000,
                                        "minimum": 15,
                                        "type": "integer"
                                    },
                                    "wlanInlineTaggingEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "wlanIpv6ProxyEnabled": {
                                        "default": "NO_PROXY",
                                        "enum": [
                                            "DAD_PROXY",
                                            "FULL_PROXY",
                                            "NO_PROXY"
                                        ],
                                        "type": "string"
                                    },
                                    "wlanLayer2AclPolicyName": {
                                        "type": "string"
                                    },
                                    "wlanPolicyClientCount": {
                                        "maximum": 200,
                                        "minimum": 0,
                                        "type": "integer"
                                    },
                                    "wlanPolicyDescription": {
                                        "type": "string"
                                    },
                                    "wlanPolicyDhcpSsidEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "wlanPolicyQbssLoad": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "wlanPolicySgt": {
                                        "maximum": 65519,
                                        "minimum": 2,
                                        "type": "integer"
                                    },
                                    "wlanPolicyVlanId": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "wlanStaticIpMobility": {
                                        "default": false,
                                        "type": "boolean"
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
