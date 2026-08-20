"""Cisco Catalyst Center GetConfigurationsForWlanProfileFeatureOnAWirelessController data model.

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


class JSONSchemaValidatorA91951D7A4E5F53Aff9E189F52409Ab:
    """GetConfigurationsForWlanProfileFeatureOnAWirelessController
    request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "items": {
                                "properties": {
                                    "adminStatusEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "advertiseApNameEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "apLocationAdvertisementEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "apfVapDot11vDisassocImminent": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "apfVapIdDot11aDtim": {
                                        "default": 1,
                                        "maximum": 255,
                                        "minimum": 1,
                                        "type": "integer"
                                    },
                                    "apfVapIdDot11bDtim": {
                                        "default": 1,
                                        "maximum": 255,
                                        "minimum": 1,
                                        "type": "integer"
                                    },
                                    "asrEnabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "authKeyMgmtCckmEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "authKeyMgmtDot1xEnabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "authKeyMgmtDot1xSha256Enabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "authKeyMgmtEasyPskEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "authKeyMgmtEasyPskSha256Enabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "authKeyMgmtFtDot1xEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "authKeyMgmtFtPskEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "authKeyMgmtFtSaeEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "authKeyMgmtFtSaeExtKeyEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "authKeyMgmtOweEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "authKeyMgmtPskEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "authKeyMgmtSaeEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "authKeyMgmtSaeExtKeyEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "authKeyMgmtSuiteB1921xEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "authKeyMgmtSuiteB1xEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "beaconProtectionEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "broadcastSsidEnabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "cckmTsfTolerance": {
                                        "default": 1000,
                                        "maximum": 5000,
                                        "minimum": 1000,
                                        "type": "integer"
                                    },
                                    "ccxAironetIeEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "chdEnabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "clientSteeringEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "configType": {
                                        "default": "WLAN_PROFILE",
                                        "enum": [
                                            "WLAN_PROFILE"
                                        ],
                                        "type": "string"
                                    },
                                    "deferPriority1Enabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "deferPriority4Enabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "deferPriority6Enabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "deferPriority7Enabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "deferTime": {
                                        "default": 100,
                                        "maximum": 60000,
                                        "minimum": 0,
                                        "type": "integer"
                                    },
                                    "deviceAnalyticsExportEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "deviceAnalyticsSupported": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "deviceVersion": {
                                        "default": "26.01",
                                        "type": "string"
                                    },
                                    "dot11AuthenticationType": {
                                        "default": "APF_VAP_80211_AUTH_OPEN",
                                        "enum": [
                                            "APF_AUTH_ALG_CISCO_LEAP",
                                            "APF_VAP_80211_AUTH_CCKM_8021X",
                                            "APF_VAP_80211_AUTH_OPEN",
                                            "APF_VAP_80211_AUTH_SHARED_KEY",
                                            "APF_VAP_80211_AUTH_WPA_8021X",
                                            "APF_VAP_80211_AUTH_WPA_PSK"
                                        ],
                                        "type": "string"
                                    },
                                    "dot11AxBssColor": {
                                        "default": 0,
                                        "maximum": 255,
                                        "minimum": 0,
                                        "type": "integer"
                                    },
                                    "dot11AxHeTwtEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "dot11AxIeEnabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "dot11BeProfileName": {
                                        "default": "default-dot11be-profile",
                                        "maxLength": 31,
                                        "minLength": 0,
                                        "type": "string"
                                    },
                                    "dot11BgPolicy": {
                                        "default": "DOT11_BG_ONLY",
                                        "enum": [
                                            "DOT11_BG_ONLY",
                                            "DOT11_G_ONLY"
                                        ],
                                        "type": "string"
                                    },
                                    "dot11VDualListEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "dot11axMuMimoDownlinkEnabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "dot11axTwtBroadcastSupportEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "dot11kBeaconMeasOnRoamEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "dot11kRmBeaconMeasRequest": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "dot11vBssMaxIdle": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "dot11vBssMaxIdleProtected": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "dot11vBssTransitionEnabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "dot11vDisassocTimer": {
                                        "default": 200,
                                        "maximum": 3000,
                                        "minimum": 0,
                                        "type": "integer"
                                    },
                                    "dot11vDisassocTimerOptRoam": {
                                        "default": 40,
                                        "maximum": 40,
                                        "minimum": 0,
                                        "type": "integer"
                                    },
                                    "dot11vDmsEnabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "dot11vTfsEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "dot11vWnmSleepModeEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "dualBand11kNeighborListEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "fastTransition": {
                                        "default": "DOT11R_ADAPTIVE_ENABLED",
                                        "enum": [
                                            "DOT11R_ADAPTIVE_ENABLED",
                                            "DOT11R_DISABLED",
                                            "DOT11R_ENABLED"
                                        ],
                                        "type": "string"
                                    },
                                    "fastTransitionOverDsEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "fineTimeMeasResponderEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "ftReassocTimeout": {
                                        "default": 20,
                                        "maximum": 100,
                                        "minimum": 1,
                                        "type": "integer"
                                    },
                                    "gtkRandomizeEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "heBssColorEnabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "heBssPartialColorEnabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "heMumimoUplinkEnabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "heOfdmaDownlinkEnabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "heOfdmaUplinkEnabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "id": {
                                        "type": "string"
                                    },
                                    "ignoreRsnIeLenEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "ipSourceGuardEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "laaClientDenialEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "latencyMaEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "localEapEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "localEapProfileName": {
                                        "type": "string"
                                    },
                                    "macFilteringList": {
                                        "type": "string"
                                    },
                                    "macOverrideAuthzList": {
                                        "type": "string"
                                    },
                                    "maxClientsAllowed": {
                                        "default": 0,
                                        "type": "integer"
                                    },
                                    "maxClientsPerApPerWlan": {
                                        "default": 0,
                                        "maximum": 1200,
                                        "minimum": 0,
                                        "type": "integer"
                                    },
                                    "maxClientsPerRadioWlan": {
                                        "default": 200,
                                        "maximum": 500,
                                        "minimum": 0,
                                        "type": "integer"
                                    },
                                    "mboEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "mpskEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "muMimoEnabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "multicastBufferEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "okcEnabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "passphrase": {
                                        "type": "string"
                                    },
                                    "pcAnalyticsSupportEnabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "peerToPeerBlockAction": {
                                        "default": "P2P_BLOCKING_ACTION_NONE",
                                        "enum": [
                                            "P2P_BLOCKING_ACTION_ALLOW_PRIVATE_GROUP",
                                            "P2P_BLOCKING_ACTION_DROP",
                                            "P2P_BLOCKING_ACTION_FWDUP",
                                            "P2P_BLOCKING_ACTION_NONE"
                                        ],
                                        "type": "string"
                                    },
                                    "pmfAssocComebackTimeout": {
                                        "default": 1,
                                        "maximum": 20,
                                        "minimum": 1,
                                        "type": "integer"
                                    },
                                    "pmfSaQueryRetryTimeout": {
                                        "default": 200,
                                        "maximum": 500,
                                        "minimum": 100,
                                        "type": "integer"
                                    },
                                    "profileName": {
                                        "maxLength": 32,
                                        "minLength": 0,
                                        "type": "string"
                                    },
                                    "protectedManagementFrameOptions": {
                                        "default": "APF_VAP_PMF_DISABLED",
                                        "enum": [
                                            "APF_VAP_PMF_DISABLED",
                                            "APF_VAP_PMF_OPTIONAL",
                                            "APF_VAP_PMF_REQUIRED"
                                        ],
                                        "type": "string"
                                    },
                                    "reAnchorRoamClientsEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "rsnCcmp256Enabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "rsnCipherSuiteGcmp128Enabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "rsnCipherSuiteGcmp256Enabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "saeAntiClogThreshold": {
                                        "default": 1500,
                                        "maximum": 3000,
                                        "minimum": 0,
                                        "type": "integer"
                                    },
                                    "saeMaxRetries": {
                                        "default": 5,
                                        "maximum": 10,
                                        "minimum": 1,
                                        "type": "integer"
                                    },
                                    "saePweModeType": {
                                        "default": "BOTH_H2E_HNP",
                                        "enum": [
                                            "BOTH_H2E_HNP",
                                            "HASH_TO_ELEMENT_ONLY",
                                            "HUNTING_AND_PECKING_ONLY"
                                        ],
                                        "type": "string"
                                    },
                                    "saeRetransmitTimeoutMs": {
                                        "default": 400,
                                        "maximum": 10000,
                                        "minimum": 1,
                                        "type": "integer"
                                    },
                                    "ssid": {
                                        "maxLength": 32,
                                        "minLength": 0,
                                        "type": "string"
                                    },
                                    "transitionDisabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "transitionModeWlanId": {
                                        "default": 0,
                                        "maximum": 4096,
                                        "minimum": 0,
                                        "type": "integer"
                                    },
                                    "universalApAdminEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "webAuthOnMacAuthFail": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "webAuthParamMap": {
                                        "type": "string"
                                    },
                                    "webauthEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "webauthIpv4PreauthAcl": {
                                        "maxLength": 32,
                                        "minLength": 0,
                                        "type": "string"
                                    },
                                    "webauthIpv6PreauthAcl": {
                                        "maxLength": 32,
                                        "minLength": 0,
                                        "type": "string"
                                    },
                                    "wepEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "wepKey": {
                                        "type": "string"
                                    },
                                    "wepKeyFormat": {
                                        "default": "KEY_HEX",
                                        "enum": [
                                            "KEY_ASCII",
                                            "KEY_HEX",
                                            "KEY_INVALID"
                                        ],
                                        "type": "string"
                                    },
                                    "wepKeyIndex": {
                                        "maximum": 4,
                                        "minimum": 1,
                                        "type": "integer"
                                    },
                                    "wepKeySize80211Encryption": {
                                        "default": "APF_VAP_80211_ENCRYP_WEP104",
                                        "enum": [
                                            "APF_VAP_80211_ENCRYP_WEP104",
                                            "APF_VAP_80211_ENCRYP_WEP40"
                                        ],
                                        "type": "string"
                                    },
                                    "wepKeyType": {
                                        "default": "CLEAR",
                                        "enum": [
                                            "AES",
                                            "CLEAR",
                                            "CLEAR_TO_AES",
                                            "CLEAR_TO_IKE_AES",
                                            "CLEAR_TO_MD5",
                                            "CLEAR_TO_SHA",
                                            "CLEAR_TO_TYPE7",
                                            "IKE_AES",
                                            "MD5",
                                            "SHA",
                                            "TYPE7"
                                        ],
                                        "type": "string"
                                    },
                                    "wifiDirectClientPolicy": {
                                        "default": "APF_VAP_WIFIDIRECT_DISABLE",
                                        "enum": [
                                            "APF_VAP_WIFIDIRECT_ALLOWED",
                                            "APF_VAP_WIFIDIRECT_DISABLE",
                                            "APF_VAP_WIFIDIRECT_INVALID",
                                            "APF_VAP_WIFIDIRECT_NOT_ALLOWED",
                                            "APF_VAP_WIFIDIRECT_NOT_ALLOWED_XC"
                                        ],
                                        "type": "string"
                                    },
                                    "wifiToCellularSteeringEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "wlan11kAssistedRoamingEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "wlan11kNeighborListEnabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "wlanAuthenticationList": {
                                        "type": "string"
                                    },
                                    "wlanAuthorizationList": {
                                        "type": "string"
                                    },
                                    "wlanBandSelectEnable": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "wlanCfgEntryOsenEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "wlanDeferPriority0Enabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "wlanDeferPriority2Enabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "wlanDeferPriority3Enabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "wlanDeferPriority5Enabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "wlanDescription": {
                                        "type": "string"
                                    },
                                    "wlanId": {
                                        "maximum": 4096,
                                        "minimum": 1,
                                        "type": "integer"
                                    },
                                    "wlanLoadBalanceEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "wlanMcDirectEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "wlanMdnsSdModeConfig": {
                                        "default": "MDNS_SD_BRIDGING",
                                        "enum": [
                                            "MDNS_SD_BRIDGING",
                                            "MDNS_SD_DROP",
                                            "MDNS_SD_GATEWAY"
                                        ],
                                        "type": "string"
                                    },
                                    "wlanMin24GhzDataRate": {
                                        "default": "RATE_1M",
                                        "enum": [
                                            "RATE_11M",
                                            "RATE_12M",
                                            "RATE_18M",
                                            "RATE_1M",
                                            "RATE_24M",
                                            "RATE_2M",
                                            "RATE_36M",
                                            "RATE_48M",
                                            "RATE_54M",
                                            "RATE_55M",
                                            "RATE_6M",
                                            "RATE_9M"
                                        ],
                                        "type": "string"
                                    },
                                    "wlanMin5GhzDataRate": {
                                        "default": "RATE_6M",
                                        "enum": [
                                            "RATE_11M",
                                            "RATE_12M",
                                            "RATE_18M",
                                            "RATE_1M",
                                            "RATE_24M",
                                            "RATE_2M",
                                            "RATE_36M",
                                            "RATE_48M",
                                            "RATE_54M",
                                            "RATE_55M",
                                            "RATE_6M",
                                            "RATE_9M"
                                        ],
                                        "type": "string"
                                    },
                                    "wlanMulticastBufferValue": {
                                        "maximum": 60,
                                        "minimum": 30,
                                        "type": "integer"
                                    },
                                    "wlanPskKeyType": {
                                        "default": "KEY_ASCII",
                                        "enum": [
                                            "KEY_ASCII",
                                            "KEY_HEX",
                                            "KEY_INVALID"
                                        ],
                                        "type": "string"
                                    },
                                    "wlanPskTypeCrypt": {
                                        "default": "CLEAR",
                                        "enum": [
                                            "AES",
                                            "CLEAR",
                                            "CLEAR_TO_AES",
                                            "CLEAR_TO_IKE_AES",
                                            "CLEAR_TO_MD5",
                                            "CLEAR_TO_SHA",
                                            "CLEAR_TO_TYPE7",
                                            "IKE_AES",
                                            "MD5",
                                            "SHA",
                                            "TYPE7"
                                        ],
                                        "type": "string"
                                    },
                                    "wlanQosWmmEnabled": {
                                        "default": "APF_VAP_WME_ALLOWED",
                                        "enum": [
                                            "APF_VAP_WME_ALLOWED",
                                            "APF_VAP_WME_DISABLED",
                                            "APF_VAP_WME_INVALID",
                                            "APF_VAP_WME_REQUIRED"
                                        ],
                                        "type": "string"
                                    },
                                    "wlanSecurityWpaEnabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "wlanSplashWebRedirect": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "wlanStaticIpTunnelingEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "wlanUapsdCompliant": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "wlanWebAuthcList": {
                                        "type": "string"
                                    },
                                    "wlanWebAuthzList": {
                                        "type": "string"
                                    },
                                    "wpa1AesEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "wpa1Enabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "wpa1TkipEnabled": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "wpa2AesEnabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "wpa2Enabled": {
                                        "default": true,
                                        "type": "boolean"
                                    },
                                    "wpa3Enabled": {
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
