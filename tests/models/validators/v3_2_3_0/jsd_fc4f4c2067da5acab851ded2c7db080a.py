"""Cisco Catalyst Center GetConfigurationsForASpecificInstanceOfADeployedRfProfileFeatureOnAWirelessC
ontroller data model.

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


class JSONSchemaValidatorFc4F4C2067Da5AcaB851Ded2C7Db080A:
    """GetConfigurationsForASpecificInstanceOfADeployedRfProfileFeatureOn
    AWirelessController request schema definition."""

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
                                                "bandSelectAgeOutDualBand": {
                                                    "default": 60,
                                                    "maximum": 300,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "bandSelectAgeOutSuppression": {
                                                    "default": 20,
                                                    "maximum": 200,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "bandSelectClientMidRssi": {
                                                    "default": -80,
                                                    "maximum": -20,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                },
                                                "bandSelectClientRssi": {
                                                    "default": -80,
                                                    "maximum": -20,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                },
                                                "bandSelectCycleCount": {
                                                    "default": 2,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "bandSelectCycleThreshold": {
                                                    "default": 200,
                                                    "maximum": 1000,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "bandSelectProbeResponse": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "clientNetworkPreference": {
                                                    "default": "DEFAULT",
                                                    "enum": [
                                                        "CONNECTIVITY",
                                                        "DEFAULT",
                                                        "THROUGHPUT"
                                                    ],
                                                    "type": "string"
                                                },
                                                "clientResetThresh6Ghz": {
                                                    "default": 5,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "clientResetThreshold": {
                                                    "default": 5,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "clientSelectThreshold": {
                                                    "default": 50,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "configType": {
                                                    "default": "RF_PROFILE",
                                                    "enum": [
                                                        "RF_PROFILE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "coverageDataPacketRssiThreshold": {
                                                    "default": -80,
                                                    "maximum": -60,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                },
                                                "coverageVoicePacketRssiThreshold": {
                                                    "default": -80,
                                                    "maximum": -60,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                },
                                                "dcaContributionInterference": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.12",
                                                    "type": "string"
                                                },
                                                "dot11axBcastProbeRespIntvl": {
                                                    "default": 20,
                                                    "maximum": 25,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "loadBalancingDenialCount": {
                                                    "default": 3,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "optRoamRssiCheckEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileAirtimeAllocation": {
                                                    "default": 5,
                                                    "maximum": 90,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "rfProfileAtfOperMode": {
                                                    "default": "APF_ATF_MODE_DISABLE",
                                                    "enum": [
                                                        "APF_ATF_MODE_DISABLE",
                                                        "APF_ATF_MODE_MONITOR",
                                                        "APF_ATF_MODE_SSID"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileAtfOptimization": {
                                                    "default": "APF_ATF_STEALING_POLICY_DISABLE",
                                                    "enum": [
                                                        "APF_ATF_STEALING_POLICY_DISABLE",
                                                        "APF_ATF_STEALING_POLICY_ENABLE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileBand": {
                                                    "enum": [
                                                        "DOT11_2_DOT_4_GHZ_BAND",
                                                        "DOT11_5_GHZ_BAND",
                                                        "DOT11_6_GHZ_BAND",
                                                        "DOT11_INVALID_BAND"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileBridgeClientAccess": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileChannelWidthMax": {
                                                    "default": "DCA_EWLC_CHAN_WIDTH_CAP_MAX",
                                                    "enum": [
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_20_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_40_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_80_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_MAX"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileChannelWidthMin": {
                                                    "default": "DCA_EWLC_CHAN_WIDTH_CAP_20_MHZ",
                                                    "enum": [
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_20_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_40_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_80_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_MAX"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileClientAwareFra": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileClientCountReset6Ghz": {
                                                    "default": 1,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "rfProfileDataRate11M": {
                                                    "default": "APF_TX_RATE_BASIC",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate12M": {
                                                    "default": "APF_TX_RATE_NOT_APPLICABLE",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate18M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate1M": {
                                                    "default": "APF_TX_RATE_BASIC",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate24M": {
                                                    "default": "APF_TX_RATE_NOT_APPLICABLE",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate2M": {
                                                    "default": "APF_TX_RATE_BASIC",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate36M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate48M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate54M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate55M": {
                                                    "default": "APF_TX_RATE_BASIC",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate6M": {
                                                    "default": "APF_TX_RATE_NOT_APPLICABLE",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate9M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDescription": {
                                                    "type": "string"
                                                },
                                                "rfProfileDot11Ax6GhzFeature": {
                                                    "default": "HE_6GHZ_NONE",
                                                    "enum": [
                                                        "HE_6GHZ_FILS_DISCOVERY",
                                                        "HE_6GHZ_NONE",
                                                        "HE_6GHZ_UBPR"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDot11axNonSrgObssPdMax": {
                                                    "default": -62,
                                                    "maximum": -62,
                                                    "minimum": -82,
                                                    "type": "integer"
                                                },
                                                "rfProfileDot11axObssPdEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileDot11axSrgObssPdEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileDot11axSrgObssPdMax": {
                                                    "default": -62,
                                                    "maximum": -62,
                                                    "minimum": -82,
                                                    "type": "integer"
                                                },
                                                "rfProfileDot11axSrgObssPdMin": {
                                                    "default": -82,
                                                    "maximum": -62,
                                                    "minimum": -82,
                                                    "type": "integer"
                                                },
                                                "rfProfileExceptionLevel": {
                                                    "default": 25,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "rfProfileFraAction": {
                                                    "default": "FRA_ACTION_DEFAULT",
                                                    "enum": [
                                                        "FRA_ACTION_DEFAULT",
                                                        "FRA_ACTION_MONITOR"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileGuardIntervalExt": {
                                                    "default": "GUARD_INTERVAL_NONE",
                                                    "enum": [
                                                        "GUARD_INTERVAL_1600NS",
                                                        "GUARD_INTERVAL_3200NS",
                                                        "GUARD_INTERVAL_400NS",
                                                        "GUARD_INTERVAL_800NS",
                                                        "GUARD_INTERVAL_NONE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileHsrMode": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileHsrNeighborTimeout": {
                                                    "default": 5,
                                                    "maximum": 60,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "rfProfileLoadBalancingWindow": {
                                                    "default": 5,
                                                    "maximum": 20,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "rfProfileMaxRadioClients": {
                                                    "default": 200,
                                                    "maximum": 500,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "rfProfileMbssidProfName": {
                                                    "default": "default-multi-bssid-profile",
                                                    "type": "string"
                                                },
                                                "rfProfileMinNumClients": {
                                                    "default": 3,
                                                    "maximum": 200,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "rfProfileMulticastDataRate": {
                                                    "default": "MCAST_DATA_RATE_DEFAULT",
                                                    "enum": [
                                                        "MCAST_DATA_RATE_12M",
                                                        "MCAST_DATA_RATE_18M",
                                                        "MCAST_DATA_RATE_24M",
                                                        "MCAST_DATA_RATE_36M",
                                                        "MCAST_DATA_RATE_48M",
                                                        "MCAST_DATA_RATE_54M",
                                                        "MCAST_DATA_RATE_6M",
                                                        "MCAST_DATA_RATE_9M",
                                                        "MCAST_DATA_RATE_DEFAULT"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileName": {
                                                    "type": "string"
                                                },
                                                "rfProfileNdpMode": {
                                                    "default": "NDP_MODE_AUTO",
                                                    "enum": [
                                                        "NDP_MODE_AUTO",
                                                        "NDP_MODE_OFF_CHANNEL"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileOptRoamRssiThreshold": {
                                                    "default": -127,
                                                    "maximum": 0,
                                                    "minimum": -127,
                                                    "type": "integer"
                                                },
                                                "rfProfilePscBias": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileRfDcaChannelWidth": {
                                                    "default": "RF_DCA_CHAN_WIDTH_BEST",
                                                    "enum": [
                                                        "RF_DCA_CHAN_WIDTH_160_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_20_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_40_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_80_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_8080_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_BEST"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileStatus": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileTrapThresholdClients": {
                                                    "default": 12,
                                                    "maximum": 200,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "rfProfileTxPowerMax": {
                                                    "default": 30,
                                                    "maximum": 30,
                                                    "minimum": -10,
                                                    "type": "integer"
                                                },
                                                "rfProfileTxPowerMin": {
                                                    "default": -10,
                                                    "maximum": 30,
                                                    "minimum": -10,
                                                    "type": "integer"
                                                },
                                                "rfProfileTxPowerV1Threshold": {
                                                    "default": -70,
                                                    "maximum": -50,
                                                    "minimum": -80,
                                                    "type": "integer"
                                                },
                                                "rfProfileTxPowerV2Threshold": {
                                                    "default": -67,
                                                    "maximum": -50,
                                                    "minimum": -80,
                                                    "type": "integer"
                                                },
                                                "rfProfileZerowtDfs": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rxSopSensitivityCustom": {
                                                    "default": -85,
                                                    "maximum": -60,
                                                    "minimum": -85,
                                                    "type": "integer"
                                                },
                                                "rxSopSensitivityThreshold": {
                                                    "default": "RRM_EWLC_RXSENSOP_THRESHOLD_AUTO",
                                                    "enum": [
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_AUTO",
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_CUSTOM",
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_HIGH",
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_LOW",
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_MEDIUM"
                                                    ],
                                                    "type": "string"
                                                },
                                                "trapThresholdInterference": {
                                                    "default": 10,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "trapThresholdNoise": {
                                                    "default": -70,
                                                    "maximum": 0,
                                                    "minimum": -127,
                                                    "type": "integer"
                                                },
                                                "trapThresholdUtilization": {
                                                    "default": 80,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                }
                                            },
                                            "required": [
                                                "deviceVersion",
                                                "rfProfileName"
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
                                                "bandSelectAgeOutDualBand": {
                                                    "default": 60,
                                                    "maximum": 300,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "bandSelectAgeOutSuppression": {
                                                    "default": 20,
                                                    "maximum": 200,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "bandSelectClientMidRssi": {
                                                    "default": -80,
                                                    "maximum": -20,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                },
                                                "bandSelectClientRssi": {
                                                    "default": -80,
                                                    "maximum": -20,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                },
                                                "bandSelectCycleCount": {
                                                    "default": 2,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "bandSelectCycleThreshold": {
                                                    "default": 200,
                                                    "maximum": 1000,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "bandSelectProbeResponse": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "clientNetworkPreference": {
                                                    "default": "DEFAULT",
                                                    "enum": [
                                                        "CONNECTIVITY",
                                                        "DEFAULT",
                                                        "THROUGHPUT"
                                                    ],
                                                    "type": "string"
                                                },
                                                "clientResetThresh6Ghz": {
                                                    "default": 5,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "clientResetThreshold": {
                                                    "default": 5,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "clientSelectThreshold": {
                                                    "default": 50,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "configType": {
                                                    "default": "RF_PROFILE",
                                                    "enum": [
                                                        "RF_PROFILE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "coverageDataPacketRssiThreshold": {
                                                    "default": -80,
                                                    "maximum": -60,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                },
                                                "coverageVoicePacketRssiThreshold": {
                                                    "default": -80,
                                                    "maximum": -60,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                },
                                                "dcaContributionInterference": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.13",
                                                    "type": "string"
                                                },
                                                "dot11axBcastProbeRespIntvl": {
                                                    "default": 20,
                                                    "maximum": 25,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "loadBalancingDenialCount": {
                                                    "default": 3,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "optRoamRssiCheckEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileAirtimeAllocation": {
                                                    "default": 5,
                                                    "maximum": 90,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "rfProfileAmpduWindowSize": {
                                                    "default": 255,
                                                    "maximum": 255,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "rfProfileAtfOperMode": {
                                                    "default": "APF_ATF_MODE_DISABLE",
                                                    "enum": [
                                                        "APF_ATF_MODE_DISABLE",
                                                        "APF_ATF_MODE_MONITOR",
                                                        "APF_ATF_MODE_SSID"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileAtfOptimization": {
                                                    "default": "APF_ATF_STEALING_POLICY_DISABLE",
                                                    "enum": [
                                                        "APF_ATF_STEALING_POLICY_DISABLE",
                                                        "APF_ATF_STEALING_POLICY_ENABLE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileBand": {
                                                    "enum": [
                                                        "DOT11_2_DOT_4_GHZ_BAND",
                                                        "DOT11_5_GHZ_BAND",
                                                        "DOT11_6_GHZ_BAND",
                                                        "DOT11_INVALID_BAND"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileBridgeClientAccess": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileChannelWidthMax": {
                                                    "default": "DCA_EWLC_CHAN_WIDTH_CAP_MAX",
                                                    "enum": [
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_20_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_40_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_80_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_MAX"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileChannelWidthMin": {
                                                    "default": "DCA_EWLC_CHAN_WIDTH_CAP_20_MHZ",
                                                    "enum": [
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_20_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_40_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_80_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_MAX"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileClientAwareFra": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileClientCountReset6Ghz": {
                                                    "default": 1,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "rfProfileDataRate11M": {
                                                    "default": "APF_TX_RATE_BASIC",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate12M": {
                                                    "default": "APF_TX_RATE_NOT_APPLICABLE",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate18M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate1M": {
                                                    "default": "APF_TX_RATE_BASIC",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate24M": {
                                                    "default": "APF_TX_RATE_NOT_APPLICABLE",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate2M": {
                                                    "default": "APF_TX_RATE_BASIC",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate36M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate48M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate54M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate55M": {
                                                    "default": "APF_TX_RATE_BASIC",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate6M": {
                                                    "default": "APF_TX_RATE_NOT_APPLICABLE",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate9M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDescription": {
                                                    "type": "string"
                                                },
                                                "rfProfileDot11Ax6GhzFeature": {
                                                    "default": "HE_6GHZ_NONE",
                                                    "enum": [
                                                        "HE_6GHZ_FILS_DISCOVERY",
                                                        "HE_6GHZ_NONE",
                                                        "HE_6GHZ_UBPR"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDot11axNonSrgObssPdMax": {
                                                    "default": -62,
                                                    "maximum": -62,
                                                    "minimum": -82,
                                                    "type": "integer"
                                                },
                                                "rfProfileDot11axObssPdEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileDot11axSrgObssPdEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileDot11axSrgObssPdMax": {
                                                    "default": -62,
                                                    "maximum": -62,
                                                    "minimum": -82,
                                                    "type": "integer"
                                                },
                                                "rfProfileDot11axSrgObssPdMin": {
                                                    "default": -82,
                                                    "maximum": -62,
                                                    "minimum": -82,
                                                    "type": "integer"
                                                },
                                                "rfProfileExceptionLevel": {
                                                    "default": 25,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "rfProfileFraAction": {
                                                    "default": "FRA_ACTION_DEFAULT",
                                                    "enum": [
                                                        "FRA_ACTION_DEFAULT",
                                                        "FRA_ACTION_MONITOR"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileGuardIntervalExt": {
                                                    "default": "GUARD_INTERVAL_NONE",
                                                    "enum": [
                                                        "GUARD_INTERVAL_1600NS",
                                                        "GUARD_INTERVAL_3200NS",
                                                        "GUARD_INTERVAL_400NS",
                                                        "GUARD_INTERVAL_800NS",
                                                        "GUARD_INTERVAL_NONE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileHsrMode": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileHsrNeighborTimeout": {
                                                    "default": 5,
                                                    "maximum": 60,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "rfProfileLoadBalancingWindow": {
                                                    "default": 5,
                                                    "maximum": 20,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "rfProfileMaxRadioClients": {
                                                    "default": 200,
                                                    "maximum": 500,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "rfProfileMbssidProfName": {
                                                    "default": "default-multi-bssid-profile",
                                                    "type": "string"
                                                },
                                                "rfProfileMinNumClients": {
                                                    "default": 3,
                                                    "maximum": 200,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "rfProfileMulticastDataRate": {
                                                    "default": "MCAST_DATA_RATE_DEFAULT",
                                                    "enum": [
                                                        "MCAST_DATA_RATE_12M",
                                                        "MCAST_DATA_RATE_18M",
                                                        "MCAST_DATA_RATE_24M",
                                                        "MCAST_DATA_RATE_36M",
                                                        "MCAST_DATA_RATE_48M",
                                                        "MCAST_DATA_RATE_54M",
                                                        "MCAST_DATA_RATE_6M",
                                                        "MCAST_DATA_RATE_9M",
                                                        "MCAST_DATA_RATE_DEFAULT"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileName": {
                                                    "type": "string"
                                                },
                                                "rfProfileNdpMode": {
                                                    "default": "NDP_MODE_AUTO",
                                                    "enum": [
                                                        "NDP_MODE_AUTO",
                                                        "NDP_MODE_OFF_CHANNEL"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileOptRoamRssiThreshold": {
                                                    "default": -127,
                                                    "maximum": 0,
                                                    "minimum": -127,
                                                    "type": "integer"
                                                },
                                                "rfProfilePscBias": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileRfDcaChannelWidth": {
                                                    "default": "RF_DCA_CHAN_WIDTH_BEST",
                                                    "enum": [
                                                        "RF_DCA_CHAN_WIDTH_160_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_20_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_40_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_80_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_8080_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_BEST"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileStatus": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileStdPwrModeAllowed": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileTrapThresholdClients": {
                                                    "default": 12,
                                                    "maximum": 200,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "rfProfileTxPowerMax": {
                                                    "default": 30,
                                                    "maximum": 30,
                                                    "minimum": -10,
                                                    "type": "integer"
                                                },
                                                "rfProfileTxPowerMin": {
                                                    "default": -10,
                                                    "maximum": 30,
                                                    "minimum": -10,
                                                    "type": "integer"
                                                },
                                                "rfProfileTxPowerV1Threshold": {
                                                    "default": -70,
                                                    "maximum": -50,
                                                    "minimum": -80,
                                                    "type": "integer"
                                                },
                                                "rfProfileTxPowerV2Threshold": {
                                                    "default": -67,
                                                    "maximum": -50,
                                                    "minimum": -80,
                                                    "type": "integer"
                                                },
                                                "rfProfileZerowtDfs": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rxSopSensitivityCustom": {
                                                    "default": -85,
                                                    "maximum": -60,
                                                    "minimum": -85,
                                                    "type": "integer"
                                                },
                                                "rxSopSensitivityThreshold": {
                                                    "default": "RRM_EWLC_RXSENSOP_THRESHOLD_AUTO",
                                                    "enum": [
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_AUTO",
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_CUSTOM",
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_HIGH",
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_LOW",
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_MEDIUM"
                                                    ],
                                                    "type": "string"
                                                },
                                                "trapThresholdInterference": {
                                                    "default": 10,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "trapThresholdNoise": {
                                                    "default": -70,
                                                    "maximum": 0,
                                                    "minimum": -127,
                                                    "type": "integer"
                                                },
                                                "trapThresholdUtilization": {
                                                    "default": 80,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                }
                                            },
                                            "required": [
                                                "deviceVersion",
                                                "rfProfileName"
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
                                                "bandSelectAgeOutDualBand": {
                                                    "default": 60,
                                                    "maximum": 300,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "bandSelectAgeOutSuppression": {
                                                    "default": 20,
                                                    "maximum": 200,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "bandSelectClientMidRssi": {
                                                    "default": -80,
                                                    "maximum": -20,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                },
                                                "bandSelectClientRssi": {
                                                    "default": -80,
                                                    "maximum": -20,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                },
                                                "bandSelectCycleCount": {
                                                    "default": 2,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "bandSelectCycleThreshold": {
                                                    "default": 200,
                                                    "maximum": 1000,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "bandSelectProbeResponse": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "clientNetworkPreference": {
                                                    "default": "DEFAULT",
                                                    "enum": [
                                                        "CONNECTIVITY",
                                                        "DEFAULT",
                                                        "THROUGHPUT"
                                                    ],
                                                    "type": "string"
                                                },
                                                "clientResetThresh6Ghz": {
                                                    "default": 5,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "clientResetThreshold": {
                                                    "default": 5,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "clientSelectThreshold": {
                                                    "default": 50,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "configType": {
                                                    "default": "RF_PROFILE",
                                                    "enum": [
                                                        "RF_PROFILE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "coverageDataPacketRssiThreshold": {
                                                    "default": -80,
                                                    "maximum": -60,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                },
                                                "coverageVoicePacketRssiThreshold": {
                                                    "default": -80,
                                                    "maximum": -60,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                },
                                                "dcaContributionInterference": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.14",
                                                    "type": "string"
                                                },
                                                "dot11axBcastProbeRespIntvl": {
                                                    "default": 20,
                                                    "maximum": 25,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "loadBalancingDenialCount": {
                                                    "default": 3,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "optRoamRssiCheckEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileAirtimeAllocation": {
                                                    "default": 5,
                                                    "maximum": 90,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "rfProfileAmpduWindowSize": {
                                                    "default": 255,
                                                    "maximum": 255,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "rfProfileAtfOperMode": {
                                                    "default": "APF_ATF_MODE_DISABLE",
                                                    "enum": [
                                                        "APF_ATF_MODE_DISABLE",
                                                        "APF_ATF_MODE_MONITOR",
                                                        "APF_ATF_MODE_SSID"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileAtfOptimization": {
                                                    "default": "APF_ATF_STEALING_POLICY_DISABLE",
                                                    "enum": [
                                                        "APF_ATF_STEALING_POLICY_DISABLE",
                                                        "APF_ATF_STEALING_POLICY_ENABLE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileBand": {
                                                    "enum": [
                                                        "DOT11_2_DOT_4_GHZ_BAND",
                                                        "DOT11_5_GHZ_BAND",
                                                        "DOT11_6_GHZ_BAND",
                                                        "DOT11_INVALID_BAND"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileBridgeClientAccess": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileChannelWidthMax": {
                                                    "default": "DCA_EWLC_CHAN_WIDTH_CAP_MAX",
                                                    "enum": [
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_20_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_40_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_80_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_MAX"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileChannelWidthMin": {
                                                    "default": "DCA_EWLC_CHAN_WIDTH_CAP_20_MHZ",
                                                    "enum": [
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_20_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_40_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_80_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_MAX"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileClientAwareFra": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileClientCountReset6Ghz": {
                                                    "default": 1,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "rfProfileDataRate11M": {
                                                    "default": "APF_TX_RATE_BASIC",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate12M": {
                                                    "default": "APF_TX_RATE_NOT_APPLICABLE",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate18M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate1M": {
                                                    "default": "APF_TX_RATE_BASIC",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate24M": {
                                                    "default": "APF_TX_RATE_NOT_APPLICABLE",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate2M": {
                                                    "default": "APF_TX_RATE_BASIC",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate36M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate48M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate54M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate55M": {
                                                    "default": "APF_TX_RATE_BASIC",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate6M": {
                                                    "default": "APF_TX_RATE_NOT_APPLICABLE",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate9M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDescription": {
                                                    "type": "string"
                                                },
                                                "rfProfileDot11Ax6GhzFeature": {
                                                    "default": "HE_6GHZ_NONE",
                                                    "enum": [
                                                        "HE_6GHZ_FILS_DISCOVERY",
                                                        "HE_6GHZ_NONE",
                                                        "HE_6GHZ_UBPR"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDot11axNonSrgObssPdMax": {
                                                    "default": -62,
                                                    "maximum": -62,
                                                    "minimum": -82,
                                                    "type": "integer"
                                                },
                                                "rfProfileDot11axObssPdEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileDot11axSrgObssPdEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileDot11axSrgObssPdMax": {
                                                    "default": -62,
                                                    "maximum": -62,
                                                    "minimum": -82,
                                                    "type": "integer"
                                                },
                                                "rfProfileDot11axSrgObssPdMin": {
                                                    "default": -82,
                                                    "maximum": -62,
                                                    "minimum": -82,
                                                    "type": "integer"
                                                },
                                                "rfProfileExceptionLevel": {
                                                    "default": 25,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "rfProfileFraAction": {
                                                    "default": "FRA_ACTION_DEFAULT",
                                                    "enum": [
                                                        "FRA_ACTION_DEFAULT",
                                                        "FRA_ACTION_MONITOR"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileGuardIntervalExt": {
                                                    "default": "GUARD_INTERVAL_NONE",
                                                    "enum": [
                                                        "GUARD_INTERVAL_1600NS",
                                                        "GUARD_INTERVAL_3200NS",
                                                        "GUARD_INTERVAL_400NS",
                                                        "GUARD_INTERVAL_800NS",
                                                        "GUARD_INTERVAL_NONE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileHsrMode": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileHsrNeighborTimeout": {
                                                    "default": 5,
                                                    "maximum": 60,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "rfProfileLoadBalancingWindow": {
                                                    "default": 5,
                                                    "maximum": 20,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "rfProfileMaxRadioClients": {
                                                    "default": 200,
                                                    "maximum": 500,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "rfProfileMbssidProfName": {
                                                    "default": "default-multi-bssid-profile",
                                                    "type": "string"
                                                },
                                                "rfProfileMinNumClients": {
                                                    "default": 3,
                                                    "maximum": 200,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "rfProfileMulticastDataRate": {
                                                    "default": "MCAST_DATA_RATE_DEFAULT",
                                                    "enum": [
                                                        "MCAST_DATA_RATE_12M",
                                                        "MCAST_DATA_RATE_18M",
                                                        "MCAST_DATA_RATE_24M",
                                                        "MCAST_DATA_RATE_36M",
                                                        "MCAST_DATA_RATE_48M",
                                                        "MCAST_DATA_RATE_54M",
                                                        "MCAST_DATA_RATE_6M",
                                                        "MCAST_DATA_RATE_9M",
                                                        "MCAST_DATA_RATE_DEFAULT"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileName": {
                                                    "type": "string"
                                                },
                                                "rfProfileNdpMode": {
                                                    "default": "NDP_MODE_AUTO",
                                                    "enum": [
                                                        "NDP_MODE_AUTO",
                                                        "NDP_MODE_OFF_CHANNEL"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileOptRoamRssiThreshold": {
                                                    "default": -127,
                                                    "maximum": 0,
                                                    "minimum": -127,
                                                    "type": "integer"
                                                },
                                                "rfProfilePscBias": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileRfDcaChannelWidth": {
                                                    "default": "RF_DCA_CHAN_WIDTH_BEST",
                                                    "enum": [
                                                        "RF_DCA_CHAN_WIDTH_160_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_20_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_40_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_80_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_8080_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_BEST"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileStatus": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileStdPwrModeAllowed": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileTrapThresholdClients": {
                                                    "default": 12,
                                                    "maximum": 200,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "rfProfileTxPowerMax": {
                                                    "default": 30,
                                                    "maximum": 30,
                                                    "minimum": -10,
                                                    "type": "integer"
                                                },
                                                "rfProfileTxPowerMin": {
                                                    "default": -10,
                                                    "maximum": 30,
                                                    "minimum": -10,
                                                    "type": "integer"
                                                },
                                                "rfProfileTxPowerV1Threshold": {
                                                    "default": -70,
                                                    "maximum": -50,
                                                    "minimum": -80,
                                                    "type": "integer"
                                                },
                                                "rfProfileTxPowerV2Threshold": {
                                                    "default": -67,
                                                    "maximum": -50,
                                                    "minimum": -80,
                                                    "type": "integer"
                                                },
                                                "rfProfileZerowtDfs": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rxSopSensitivityCustom": {
                                                    "default": -85,
                                                    "maximum": -60,
                                                    "minimum": -85,
                                                    "type": "integer"
                                                },
                                                "rxSopSensitivityThreshold": {
                                                    "default": "RRM_EWLC_RXSENSOP_THRESHOLD_AUTO",
                                                    "enum": [
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_AUTO",
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_CUSTOM",
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_HIGH",
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_LOW",
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_MEDIUM"
                                                    ],
                                                    "type": "string"
                                                },
                                                "trapThresholdInterference": {
                                                    "default": 10,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "trapThresholdNoise": {
                                                    "default": -70,
                                                    "maximum": 0,
                                                    "minimum": -127,
                                                    "type": "integer"
                                                },
                                                "trapThresholdUtilization": {
                                                    "default": 80,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                }
                                            },
                                            "required": [
                                                "deviceVersion",
                                                "rfProfileName"
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
                                                "bandSelectAgeOutDualBand": {
                                                    "default": 60,
                                                    "maximum": 300,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "bandSelectAgeOutSuppression": {
                                                    "default": 20,
                                                    "maximum": 200,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "bandSelectClientMidRssi": {
                                                    "default": -80,
                                                    "maximum": -20,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                },
                                                "bandSelectClientRssi": {
                                                    "default": -80,
                                                    "maximum": -20,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                },
                                                "bandSelectCycleCount": {
                                                    "default": 2,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "bandSelectCycleThreshold": {
                                                    "default": 200,
                                                    "maximum": 1000,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "bandSelectProbeResponse": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "clientNetworkPreference": {
                                                    "default": "DEFAULT",
                                                    "enum": [
                                                        "CONNECTIVITY",
                                                        "DEFAULT",
                                                        "THROUGHPUT"
                                                    ],
                                                    "type": "string"
                                                },
                                                "clientResetThresh6Ghz": {
                                                    "default": 5,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "clientResetThreshold": {
                                                    "default": 5,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "clientSelectThreshold": {
                                                    "default": 50,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "configType": {
                                                    "default": "RF_PROFILE",
                                                    "enum": [
                                                        "RF_PROFILE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "coverageDataPacketRssiThreshold": {
                                                    "default": -80,
                                                    "maximum": -60,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                },
                                                "coverageVoicePacketRssiThreshold": {
                                                    "default": -80,
                                                    "maximum": -60,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                },
                                                "dcaContributionInterference": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.15",
                                                    "type": "string"
                                                },
                                                "dot11axBcastProbeRespIntvl": {
                                                    "default": 20,
                                                    "maximum": 25,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "loadBalancingDenialCount": {
                                                    "default": 3,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "optRoamRssiCheckEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileAggregateRetries": {
                                                    "default": -1,
                                                    "maximum": 255,
                                                    "minimum": -1,
                                                    "type": "integer"
                                                },
                                                "rfProfileAirtimeAllocation": {
                                                    "default": 5,
                                                    "maximum": 90,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "rfProfileAmpduWindowSize": {
                                                    "default": 255,
                                                    "maximum": 255,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "rfProfileAtfOperMode": {
                                                    "default": "APF_ATF_MODE_DISABLE",
                                                    "enum": [
                                                        "APF_ATF_MODE_DISABLE",
                                                        "APF_ATF_MODE_MONITOR",
                                                        "APF_ATF_MODE_SSID"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileAtfOptimization": {
                                                    "default": "APF_ATF_STEALING_POLICY_DISABLE",
                                                    "enum": [
                                                        "APF_ATF_STEALING_POLICY_DISABLE",
                                                        "APF_ATF_STEALING_POLICY_ENABLE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileBand": {
                                                    "enum": [
                                                        "DOT11_2_DOT_4_GHZ_BAND",
                                                        "DOT11_5_GHZ_BAND",
                                                        "DOT11_6_GHZ_BAND",
                                                        "DOT11_INVALID_BAND"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileBridgeClientAccess": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileChannelWidthMax": {
                                                    "default": "DCA_EWLC_CHAN_WIDTH_CAP_MAX",
                                                    "enum": [
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_160_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_20_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_320_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_40_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_80_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_MAX"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileChannelWidthMin": {
                                                    "default": "DCA_EWLC_CHAN_WIDTH_CAP_20_MHZ",
                                                    "enum": [
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_160_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_20_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_320_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_40_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_80_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_MAX"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileClientAwareFra": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileClientCountReset6Ghz": {
                                                    "default": 1,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "rfProfileDataRate11M": {
                                                    "default": "APF_TX_RATE_BASIC",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate12M": {
                                                    "default": "APF_TX_RATE_NOT_APPLICABLE",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate18M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate1M": {
                                                    "default": "APF_TX_RATE_BASIC",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate24M": {
                                                    "default": "APF_TX_RATE_NOT_APPLICABLE",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate2M": {
                                                    "default": "APF_TX_RATE_BASIC",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate36M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate48M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate54M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate55M": {
                                                    "default": "APF_TX_RATE_BASIC",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate6M": {
                                                    "default": "APF_TX_RATE_NOT_APPLICABLE",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate9M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDescription": {
                                                    "type": "string"
                                                },
                                                "rfProfileDot11Ax6GhzFeature": {
                                                    "default": "HE_6GHZ_NONE",
                                                    "enum": [
                                                        "HE_6GHZ_FILS_DISCOVERY",
                                                        "HE_6GHZ_NONE",
                                                        "HE_6GHZ_UBPR"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDot11axNonSrgObssPdMax": {
                                                    "default": -62,
                                                    "maximum": -62,
                                                    "minimum": -82,
                                                    "type": "integer"
                                                },
                                                "rfProfileDot11axObssPdEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileDot11axSrgObssPdEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileDot11axSrgObssPdMax": {
                                                    "default": -62,
                                                    "maximum": -62,
                                                    "minimum": -82,
                                                    "type": "integer"
                                                },
                                                "rfProfileDot11axSrgObssPdMin": {
                                                    "default": -82,
                                                    "maximum": -62,
                                                    "minimum": -82,
                                                    "type": "integer"
                                                },
                                                "rfProfileExceptionLevel": {
                                                    "default": 25,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "rfProfileFraAction": {
                                                    "default": "FRA_ACTION_DEFAULT",
                                                    "enum": [
                                                        "FRA_ACTION_DEFAULT",
                                                        "FRA_ACTION_MONITOR"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileGuardIntervalExt": {
                                                    "default": "GUARD_INTERVAL_NONE",
                                                    "enum": [
                                                        "GUARD_INTERVAL_1600NS",
                                                        "GUARD_INTERVAL_3200NS",
                                                        "GUARD_INTERVAL_400NS",
                                                        "GUARD_INTERVAL_800NS",
                                                        "GUARD_INTERVAL_NONE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileHsrMode": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileHsrNeighborTimeout": {
                                                    "default": 5,
                                                    "maximum": 60,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "rfProfileLoadBalancingWindow": {
                                                    "default": 5,
                                                    "maximum": 20,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "rfProfileManagementRetries": {
                                                    "default": -1,
                                                    "maximum": 255,
                                                    "minimum": -1,
                                                    "type": "integer"
                                                },
                                                "rfProfileMaxRadioClients": {
                                                    "default": 200,
                                                    "maximum": 500,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "rfProfileMbssidProfName": {
                                                    "default": "default-multi-bssid-profile",
                                                    "type": "string"
                                                },
                                                "rfProfileMinNumClients": {
                                                    "default": 3,
                                                    "maximum": 200,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "rfProfileMulticastDataRate": {
                                                    "default": "MCAST_DATA_RATE_DEFAULT",
                                                    "enum": [
                                                        "MCAST_DATA_RATE_12M",
                                                        "MCAST_DATA_RATE_18M",
                                                        "MCAST_DATA_RATE_24M",
                                                        "MCAST_DATA_RATE_36M",
                                                        "MCAST_DATA_RATE_48M",
                                                        "MCAST_DATA_RATE_54M",
                                                        "MCAST_DATA_RATE_6M",
                                                        "MCAST_DATA_RATE_9M",
                                                        "MCAST_DATA_RATE_DEFAULT"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileName": {
                                                    "type": "string"
                                                },
                                                "rfProfileNdpMode": {
                                                    "default": "NDP_MODE_AUTO",
                                                    "enum": [
                                                        "NDP_MODE_AUTO",
                                                        "NDP_MODE_OFF_CHANNEL"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileNonAggregateRetries": {
                                                    "default": -1,
                                                    "maximum": 255,
                                                    "minimum": -1,
                                                    "type": "integer"
                                                },
                                                "rfProfileOptRoamRssiThreshold": {
                                                    "default": -127,
                                                    "maximum": 0,
                                                    "minimum": -127,
                                                    "type": "integer"
                                                },
                                                "rfProfilePreamblePuncture": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfilePscBias": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileRfDcaChannelWidth": {
                                                    "default": "RF_DCA_CHAN_WIDTH_BEST",
                                                    "enum": [
                                                        "RF_DCA_CHAN_WIDTH_160_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_20_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_40_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_80_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_8080_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_BEST"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileStatus": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileStdPwrModeAllowed": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileTrapThresholdClients": {
                                                    "default": 12,
                                                    "maximum": 200,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "rfProfileTxPowerMax": {
                                                    "default": 30,
                                                    "maximum": 30,
                                                    "minimum": -10,
                                                    "type": "integer"
                                                },
                                                "rfProfileTxPowerMin": {
                                                    "default": -10,
                                                    "maximum": 30,
                                                    "minimum": -10,
                                                    "type": "integer"
                                                },
                                                "rfProfileTxPowerV1Threshold": {
                                                    "default": -70,
                                                    "maximum": -50,
                                                    "minimum": -80,
                                                    "type": "integer"
                                                },
                                                "rfProfileTxPowerV2Threshold": {
                                                    "default": -67,
                                                    "maximum": -50,
                                                    "minimum": -80,
                                                    "type": "integer"
                                                },
                                                "rfProfileZerowtDfs": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rxSopSensitivityCustom": {
                                                    "default": -85,
                                                    "maximum": -60,
                                                    "minimum": -85,
                                                    "type": "integer"
                                                },
                                                "rxSopSensitivityThreshold": {
                                                    "default": "RRM_EWLC_RXSENSOP_THRESHOLD_AUTO",
                                                    "enum": [
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_AUTO",
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_CUSTOM",
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_HIGH",
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_LOW",
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_MEDIUM"
                                                    ],
                                                    "type": "string"
                                                },
                                                "trapThresholdInterference": {
                                                    "default": 10,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "trapThresholdNoise": {
                                                    "default": -70,
                                                    "maximum": 0,
                                                    "minimum": -127,
                                                    "type": "integer"
                                                },
                                                "trapThresholdUtilization": {
                                                    "default": 80,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                }
                                            },
                                            "required": [
                                                "deviceVersion",
                                                "rfProfileName"
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
                                                "bandSelectAgeOutDualBand": {
                                                    "default": 60,
                                                    "maximum": 300,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "bandSelectAgeOutSuppression": {
                                                    "default": 20,
                                                    "maximum": 200,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "bandSelectClientMidRssi": {
                                                    "default": -80,
                                                    "maximum": -20,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                },
                                                "bandSelectClientRssi": {
                                                    "default": -80,
                                                    "maximum": -20,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                },
                                                "bandSelectCycleCount": {
                                                    "default": 2,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "bandSelectCycleThreshold": {
                                                    "default": 200,
                                                    "maximum": 1000,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "bandSelectProbeResponse": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "clientNetworkPreference": {
                                                    "default": "DEFAULT",
                                                    "enum": [
                                                        "CONNECTIVITY",
                                                        "DEFAULT",
                                                        "THROUGHPUT"
                                                    ],
                                                    "type": "string"
                                                },
                                                "clientResetThresh6Ghz": {
                                                    "default": 5,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "clientResetThreshold": {
                                                    "default": 5,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "clientSelectThreshold": {
                                                    "default": 50,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "configType": {
                                                    "default": "RF_PROFILE",
                                                    "enum": [
                                                        "RF_PROFILE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "coverageDataPacketRssiThreshold": {
                                                    "default": -80,
                                                    "maximum": -60,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                },
                                                "coverageVoicePacketRssiThreshold": {
                                                    "default": -80,
                                                    "maximum": -60,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                },
                                                "dcaContributionInterference": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.16",
                                                    "type": "string"
                                                },
                                                "dot11axBcastProbeRespIntvl": {
                                                    "default": 20,
                                                    "maximum": 25,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "loadBalancingDenialCount": {
                                                    "default": 3,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "optRoamRssiCheckEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileAggregateRetries": {
                                                    "default": -1,
                                                    "maximum": 255,
                                                    "minimum": -1,
                                                    "type": "integer"
                                                },
                                                "rfProfileAirtimeAllocation": {
                                                    "default": 5,
                                                    "maximum": 90,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "rfProfileAmpduWindowSize": {
                                                    "default": 255,
                                                    "maximum": 255,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "rfProfileAtfOperMode": {
                                                    "default": "APF_ATF_MODE_DISABLE",
                                                    "enum": [
                                                        "APF_ATF_MODE_DISABLE",
                                                        "APF_ATF_MODE_MONITOR",
                                                        "APF_ATF_MODE_SSID"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileAtfOptimization": {
                                                    "default": "APF_ATF_STEALING_POLICY_DISABLE",
                                                    "enum": [
                                                        "APF_ATF_STEALING_POLICY_DISABLE",
                                                        "APF_ATF_STEALING_POLICY_ENABLE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileBand": {
                                                    "enum": [
                                                        "DOT11_2_DOT_4_GHZ_BAND",
                                                        "DOT11_5_GHZ_BAND",
                                                        "DOT11_6_GHZ_BAND",
                                                        "DOT11_INVALID_BAND"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileBridgeClientAccess": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileChannelWidthMax": {
                                                    "default": "DCA_EWLC_CHAN_WIDTH_CAP_MAX",
                                                    "enum": [
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_160_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_20_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_320_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_40_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_80_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_MAX"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileChannelWidthMin": {
                                                    "default": "DCA_EWLC_CHAN_WIDTH_CAP_20_MHZ",
                                                    "enum": [
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_160_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_20_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_320_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_40_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_80_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_MAX"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileClientAwareFra": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileClientCountReset6Ghz": {
                                                    "default": 1,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "rfProfileDataRate11M": {
                                                    "default": "APF_TX_RATE_BASIC",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate12M": {
                                                    "default": "APF_TX_RATE_NOT_APPLICABLE",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate18M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate1M": {
                                                    "default": "APF_TX_RATE_BASIC",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate24M": {
                                                    "default": "APF_TX_RATE_NOT_APPLICABLE",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate2M": {
                                                    "default": "APF_TX_RATE_BASIC",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate36M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate48M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate54M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate55M": {
                                                    "default": "APF_TX_RATE_BASIC",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate6M": {
                                                    "default": "APF_TX_RATE_NOT_APPLICABLE",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate9M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDescription": {
                                                    "maxLength": 64,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "rfProfileDot11Ax6GhzFeature": {
                                                    "default": "HE_6GHZ_NONE",
                                                    "enum": [
                                                        "HE_6GHZ_FILS_DISCOVERY",
                                                        "HE_6GHZ_NONE",
                                                        "HE_6GHZ_UBPR"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDot11axNonSrgObssPdMax": {
                                                    "default": -62,
                                                    "maximum": -62,
                                                    "minimum": -82,
                                                    "type": "integer"
                                                },
                                                "rfProfileDot11axObssPdEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileDot11axSrgObssPdEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileDot11axSrgObssPdMax": {
                                                    "default": -62,
                                                    "maximum": -62,
                                                    "minimum": -82,
                                                    "type": "integer"
                                                },
                                                "rfProfileDot11axSrgObssPdMin": {
                                                    "default": -82,
                                                    "maximum": -62,
                                                    "minimum": -82,
                                                    "type": "integer"
                                                },
                                                "rfProfileExceptionLevel": {
                                                    "default": 25,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "rfProfileFraAction": {
                                                    "default": "FRA_ACTION_DEFAULT",
                                                    "enum": [
                                                        "FRA_ACTION_DEFAULT",
                                                        "FRA_ACTION_MONITOR"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileGuardIntervalExt": {
                                                    "default": "GUARD_INTERVAL_NONE",
                                                    "enum": [
                                                        "GUARD_INTERVAL_1600NS",
                                                        "GUARD_INTERVAL_3200NS",
                                                        "GUARD_INTERVAL_400NS",
                                                        "GUARD_INTERVAL_800NS",
                                                        "GUARD_INTERVAL_NONE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileHsrMode": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileHsrNeighborTimeout": {
                                                    "default": 5,
                                                    "maximum": 60,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "rfProfileLoadBalancingWindow": {
                                                    "default": 5,
                                                    "maximum": 20,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "rfProfileManagementRetries": {
                                                    "default": -1,
                                                    "maximum": 255,
                                                    "minimum": -1,
                                                    "type": "integer"
                                                },
                                                "rfProfileMaxRadioClients": {
                                                    "default": 200,
                                                    "maximum": 500,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "rfProfileMbssidProfName": {
                                                    "default": "default-multi-bssid-profile",
                                                    "type": "string"
                                                },
                                                "rfProfileMinNumClients": {
                                                    "default": 3,
                                                    "maximum": 200,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "rfProfileMulticastDataRate": {
                                                    "default": "MCAST_DATA_RATE_DEFAULT",
                                                    "enum": [
                                                        "MCAST_DATA_RATE_12M",
                                                        "MCAST_DATA_RATE_18M",
                                                        "MCAST_DATA_RATE_24M",
                                                        "MCAST_DATA_RATE_36M",
                                                        "MCAST_DATA_RATE_48M",
                                                        "MCAST_DATA_RATE_54M",
                                                        "MCAST_DATA_RATE_6M",
                                                        "MCAST_DATA_RATE_9M",
                                                        "MCAST_DATA_RATE_DEFAULT"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileName": {
                                                    "maxLength": 32,
                                                    "minLength": 1,
                                                    "type": "string"
                                                },
                                                "rfProfileNdpMode": {
                                                    "default": "NDP_MODE_AUTO",
                                                    "enum": [
                                                        "NDP_MODE_AUTO",
                                                        "NDP_MODE_OFF_CHANNEL"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileNonAggregateRetries": {
                                                    "default": -1,
                                                    "maximum": 255,
                                                    "minimum": -1,
                                                    "type": "integer"
                                                },
                                                "rfProfileOptRoamRssiThreshold": {
                                                    "default": -127,
                                                    "maximum": 0,
                                                    "minimum": -127,
                                                    "type": "integer"
                                                },
                                                "rfProfilePreamblePuncture": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfilePscBias": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileRfDcaChannelWidth": {
                                                    "default": "RF_DCA_CHAN_WIDTH_BEST",
                                                    "enum": [
                                                        "RF_DCA_CHAN_WIDTH_160_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_20_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_40_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_80_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_8080_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_BEST"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileStatus": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileStdPwrModeAllowed": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileTrapThresholdClients": {
                                                    "default": 12,
                                                    "maximum": 200,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "rfProfileTxPowerMax": {
                                                    "default": 30,
                                                    "maximum": 30,
                                                    "minimum": -10,
                                                    "type": "integer"
                                                },
                                                "rfProfileTxPowerMin": {
                                                    "default": -10,
                                                    "maximum": 30,
                                                    "minimum": -10,
                                                    "type": "integer"
                                                },
                                                "rfProfileTxPowerV1Threshold": {
                                                    "default": -70,
                                                    "maximum": -50,
                                                    "minimum": -80,
                                                    "type": "integer"
                                                },
                                                "rfProfileTxPowerV2Threshold": {
                                                    "default": -67,
                                                    "maximum": -50,
                                                    "minimum": -80,
                                                    "type": "integer"
                                                },
                                                "rfProfileZerowtDfs": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rxSopSensitivityCustom": {
                                                    "default": -85,
                                                    "maximum": -60,
                                                    "minimum": -85,
                                                    "type": "integer"
                                                },
                                                "rxSopSensitivityThreshold": {
                                                    "default": "RRM_EWLC_RXSENSOP_THRESHOLD_AUTO",
                                                    "enum": [
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_AUTO",
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_CUSTOM",
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_HIGH",
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_LOW",
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_MEDIUM"
                                                    ],
                                                    "type": "string"
                                                },
                                                "trapThresholdInterference": {
                                                    "default": 10,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "trapThresholdNoise": {
                                                    "default": -70,
                                                    "maximum": 0,
                                                    "minimum": -127,
                                                    "type": "integer"
                                                },
                                                "trapThresholdUtilization": {
                                                    "default": 80,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                }
                                            },
                                            "required": [
                                                "deviceVersion",
                                                "rfProfileName"
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
                                                "bandSelectAgeOutDualBand": {
                                                    "default": 60,
                                                    "maximum": 300,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "bandSelectAgeOutSuppression": {
                                                    "default": 20,
                                                    "maximum": 200,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "bandSelectClientMidRssi": {
                                                    "default": -80,
                                                    "maximum": -20,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                },
                                                "bandSelectClientRssi": {
                                                    "default": -80,
                                                    "maximum": -20,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                },
                                                "bandSelectCycleCount": {
                                                    "default": 2,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "bandSelectCycleThreshold": {
                                                    "default": 200,
                                                    "maximum": 1000,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "bandSelectProbeResponse": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "clientNetworkPreference": {
                                                    "default": "DEFAULT",
                                                    "enum": [
                                                        "CONNECTIVITY",
                                                        "DEFAULT",
                                                        "THROUGHPUT"
                                                    ],
                                                    "type": "string"
                                                },
                                                "clientResetThresh6Ghz": {
                                                    "default": 5,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "clientResetThreshold": {
                                                    "default": 5,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "clientSelectThreshold": {
                                                    "default": 50,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "configType": {
                                                    "default": "RF_PROFILE",
                                                    "enum": [
                                                        "RF_PROFILE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "coverageDataPacketRssiThreshold": {
                                                    "default": -80,
                                                    "maximum": -60,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                },
                                                "coverageVoicePacketRssiThreshold": {
                                                    "default": -80,
                                                    "maximum": -60,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                },
                                                "dcaContributionInterference": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.17",
                                                    "type": "string"
                                                },
                                                "dot11axBcastProbeRespIntvl": {
                                                    "default": 20,
                                                    "maximum": 25,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "loadBalancingDenialCount": {
                                                    "default": 3,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "optRoamRssiCheckEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileAggregateRetries": {
                                                    "default": -1,
                                                    "maximum": 255,
                                                    "minimum": -1,
                                                    "type": "integer"
                                                },
                                                "rfProfileAirtimeAllocation": {
                                                    "default": 5,
                                                    "maximum": 90,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "rfProfileAmpduWindowSize": {
                                                    "default": 255,
                                                    "maximum": 255,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "rfProfileAtfOperMode": {
                                                    "default": "APF_ATF_MODE_DISABLE",
                                                    "enum": [
                                                        "APF_ATF_MODE_DISABLE",
                                                        "APF_ATF_MODE_MONITOR",
                                                        "APF_ATF_MODE_SSID"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileAtfOptimization": {
                                                    "default": "APF_ATF_STEALING_POLICY_DISABLE",
                                                    "enum": [
                                                        "APF_ATF_STEALING_POLICY_DISABLE",
                                                        "APF_ATF_STEALING_POLICY_ENABLE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileBand": {
                                                    "enum": [
                                                        "DOT11_2_DOT_4_GHZ_BAND",
                                                        "DOT11_5_GHZ_BAND",
                                                        "DOT11_6_GHZ_BAND",
                                                        "DOT11_INVALID_BAND"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileBridgeClientAccess": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileChannelWidthMax": {
                                                    "default": "DCA_EWLC_CHAN_WIDTH_CAP_MAX",
                                                    "enum": [
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_160_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_20_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_320_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_40_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_80_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_MAX"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileChannelWidthMin": {
                                                    "default": "DCA_EWLC_CHAN_WIDTH_CAP_20_MHZ",
                                                    "enum": [
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_160_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_20_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_320_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_40_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_80_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_MAX"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileClientAwareFra": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileClientCountReset6Ghz": {
                                                    "default": 1,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "rfProfileDataRate11M": {
                                                    "default": "APF_TX_RATE_BASIC",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate12M": {
                                                    "default": "APF_TX_RATE_NOT_APPLICABLE",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate18M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate1M": {
                                                    "default": "APF_TX_RATE_BASIC",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate24M": {
                                                    "default": "APF_TX_RATE_NOT_APPLICABLE",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate2M": {
                                                    "default": "APF_TX_RATE_BASIC",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate36M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate48M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate54M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate55M": {
                                                    "default": "APF_TX_RATE_BASIC",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate6M": {
                                                    "default": "APF_TX_RATE_NOT_APPLICABLE",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate9M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDescription": {
                                                    "maxLength": 64,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "rfProfileDot11Ax6GhzFeature": {
                                                    "default": "HE_6GHZ_NONE",
                                                    "enum": [
                                                        "HE_6GHZ_FILS_DISCOVERY",
                                                        "HE_6GHZ_NONE",
                                                        "HE_6GHZ_UBPR"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDot11axNonSrgObssPdMax": {
                                                    "default": -62,
                                                    "maximum": -62,
                                                    "minimum": -82,
                                                    "type": "integer"
                                                },
                                                "rfProfileDot11axObssPdEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileDot11axSrgObssPdEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileDot11axSrgObssPdMax": {
                                                    "default": -62,
                                                    "maximum": -62,
                                                    "minimum": -82,
                                                    "type": "integer"
                                                },
                                                "rfProfileDot11axSrgObssPdMin": {
                                                    "default": -82,
                                                    "maximum": -62,
                                                    "minimum": -82,
                                                    "type": "integer"
                                                },
                                                "rfProfileExceptionLevel": {
                                                    "default": 25,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "rfProfileFraAction": {
                                                    "default": "FRA_ACTION_DEFAULT",
                                                    "enum": [
                                                        "FRA_ACTION_DEFAULT",
                                                        "FRA_ACTION_MONITOR"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileGuardIntervalExt": {
                                                    "default": "GUARD_INTERVAL_NONE",
                                                    "enum": [
                                                        "GUARD_INTERVAL_1600NS",
                                                        "GUARD_INTERVAL_3200NS",
                                                        "GUARD_INTERVAL_400NS",
                                                        "GUARD_INTERVAL_800NS",
                                                        "GUARD_INTERVAL_NONE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileHsrMode": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileHsrNeighborTimeout": {
                                                    "default": 5,
                                                    "maximum": 60,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "rfProfileLoadBalancingWindow": {
                                                    "default": 5,
                                                    "maximum": 20,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "rfProfileManagementRetries": {
                                                    "default": -1,
                                                    "maximum": 255,
                                                    "minimum": -1,
                                                    "type": "integer"
                                                },
                                                "rfProfileMaxRadioClients": {
                                                    "default": 200,
                                                    "maximum": 500,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "rfProfileMbssidProfName": {
                                                    "default": "default-multi-bssid-profile",
                                                    "type": "string"
                                                },
                                                "rfProfileMinNumClients": {
                                                    "default": 3,
                                                    "maximum": 200,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "rfProfileMulticastDataRate": {
                                                    "default": "MCAST_DATA_RATE_DEFAULT",
                                                    "enum": [
                                                        "MCAST_DATA_RATE_12M",
                                                        "MCAST_DATA_RATE_18M",
                                                        "MCAST_DATA_RATE_24M",
                                                        "MCAST_DATA_RATE_36M",
                                                        "MCAST_DATA_RATE_48M",
                                                        "MCAST_DATA_RATE_54M",
                                                        "MCAST_DATA_RATE_6M",
                                                        "MCAST_DATA_RATE_9M",
                                                        "MCAST_DATA_RATE_DEFAULT"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileName": {
                                                    "maxLength": 32,
                                                    "minLength": 1,
                                                    "type": "string"
                                                },
                                                "rfProfileNdpMode": {
                                                    "default": "NDP_MODE_AUTO",
                                                    "enum": [
                                                        "NDP_MODE_AUTO",
                                                        "NDP_MODE_OFF_CHANNEL"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileNonAggregateRetries": {
                                                    "default": -1,
                                                    "maximum": 255,
                                                    "minimum": -1,
                                                    "type": "integer"
                                                },
                                                "rfProfileOptRoamRssiThreshold": {
                                                    "default": -127,
                                                    "maximum": 0,
                                                    "minimum": -127,
                                                    "type": "integer"
                                                },
                                                "rfProfilePreamblePuncture": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfilePscBias": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileRfDcaChannelWidth": {
                                                    "default": "RF_DCA_CHAN_WIDTH_BEST",
                                                    "enum": [
                                                        "RF_DCA_CHAN_WIDTH_160_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_20_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_40_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_80_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_8080_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_BEST"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileStatus": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileStdPwrModeAllowed": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileTrapThresholdClients": {
                                                    "default": 12,
                                                    "maximum": 200,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "rfProfileTxPowerMax": {
                                                    "default": 30,
                                                    "maximum": 30,
                                                    "minimum": -10,
                                                    "type": "integer"
                                                },
                                                "rfProfileTxPowerMin": {
                                                    "default": -10,
                                                    "maximum": 30,
                                                    "minimum": -10,
                                                    "type": "integer"
                                                },
                                                "rfProfileTxPowerV1Threshold": {
                                                    "default": -70,
                                                    "maximum": -50,
                                                    "minimum": -80,
                                                    "type": "integer"
                                                },
                                                "rfProfileTxPowerV2Threshold": {
                                                    "default": -67,
                                                    "maximum": -50,
                                                    "minimum": -80,
                                                    "type": "integer"
                                                },
                                                "rfProfileZerowtDfs": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfUnii3LpChannelsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rxSopSensitivityCustom": {
                                                    "default": -85,
                                                    "maximum": -60,
                                                    "minimum": -85,
                                                    "type": "integer"
                                                },
                                                "rxSopSensitivityThreshold": {
                                                    "default": "RRM_EWLC_RXSENSOP_THRESHOLD_AUTO",
                                                    "enum": [
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_AUTO",
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_CUSTOM",
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_HIGH",
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_LOW",
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_MEDIUM"
                                                    ],
                                                    "type": "string"
                                                },
                                                "trapThresholdInterference": {
                                                    "default": 10,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "trapThresholdNoise": {
                                                    "default": -70,
                                                    "maximum": 0,
                                                    "minimum": -127,
                                                    "type": "integer"
                                                },
                                                "trapThresholdUtilization": {
                                                    "default": 80,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                }
                                            },
                                            "required": [
                                                "deviceVersion",
                                                "rfProfileName"
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
                                                "bandSelectAgeOutDualBand": {
                                                    "default": 60,
                                                    "maximum": 300,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "bandSelectAgeOutSuppression": {
                                                    "default": 20,
                                                    "maximum": 200,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "bandSelectClientMidRssi": {
                                                    "default": -80,
                                                    "maximum": -20,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                },
                                                "bandSelectClientRssi": {
                                                    "default": -80,
                                                    "maximum": -20,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                },
                                                "bandSelectCycleCount": {
                                                    "default": 2,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "bandSelectCycleThreshold": {
                                                    "default": 200,
                                                    "maximum": 1000,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "bandSelectProbeResponse": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "clientNetworkPreference": {
                                                    "default": "DEFAULT",
                                                    "enum": [
                                                        "CONNECTIVITY",
                                                        "DEFAULT",
                                                        "THROUGHPUT"
                                                    ],
                                                    "type": "string"
                                                },
                                                "clientResetThresh6Ghz": {
                                                    "default": 5,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "clientResetThreshold": {
                                                    "default": 5,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "clientSelectThreshold": {
                                                    "default": 50,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "configType": {
                                                    "default": "RF_PROFILE",
                                                    "enum": [
                                                        "RF_PROFILE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "coverageDataPacketRssiThreshold": {
                                                    "default": -80,
                                                    "maximum": -60,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                },
                                                "coverageVoicePacketRssiThreshold": {
                                                    "default": -80,
                                                    "maximum": -60,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                },
                                                "dcaContributionInterference": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.18",
                                                    "type": "string"
                                                },
                                                "dot11axBcastProbeRespIntvl": {
                                                    "default": 20,
                                                    "maximum": 25,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "loadBalancingDenialCount": {
                                                    "default": 3,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "optRoamRssiCheckEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileAggregateRetries": {
                                                    "default": -1,
                                                    "maximum": 255,
                                                    "minimum": -1,
                                                    "type": "integer"
                                                },
                                                "rfProfileAirtimeAllocation": {
                                                    "default": 5,
                                                    "maximum": 90,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "rfProfileAmpduWindowSize": {
                                                    "default": 255,
                                                    "maximum": 255,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "rfProfileAtfOperMode": {
                                                    "default": "APF_ATF_MODE_DISABLE",
                                                    "enum": [
                                                        "APF_ATF_MODE_DISABLE",
                                                        "APF_ATF_MODE_MONITOR",
                                                        "APF_ATF_MODE_SSID"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileAtfOptimization": {
                                                    "default": "APF_ATF_STEALING_POLICY_DISABLE",
                                                    "enum": [
                                                        "APF_ATF_STEALING_POLICY_DISABLE",
                                                        "APF_ATF_STEALING_POLICY_ENABLE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileBand": {
                                                    "enum": [
                                                        "DOT11_2_DOT_4_GHZ_BAND",
                                                        "DOT11_5_GHZ_BAND",
                                                        "DOT11_6_GHZ_BAND",
                                                        "DOT11_INVALID_BAND"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileBridgeClientAccess": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileChannelWidthMax": {
                                                    "default": "DCA_EWLC_CHAN_WIDTH_CAP_MAX",
                                                    "enum": [
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_160_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_20_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_320_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_40_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_80_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_MAX"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileChannelWidthMin": {
                                                    "default": "DCA_EWLC_CHAN_WIDTH_CAP_20_MHZ",
                                                    "enum": [
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_160_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_20_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_320_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_40_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_80_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_MAX"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileClientAwareFra": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileClientCountReset6Ghz": {
                                                    "default": 1,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "rfProfileDataRate11M": {
                                                    "default": "APF_TX_RATE_BASIC",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate12M": {
                                                    "default": "APF_TX_RATE_NOT_APPLICABLE",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate18M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate1M": {
                                                    "default": "APF_TX_RATE_BASIC",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate24M": {
                                                    "default": "APF_TX_RATE_NOT_APPLICABLE",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate2M": {
                                                    "default": "APF_TX_RATE_BASIC",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate36M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate48M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate54M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate55M": {
                                                    "default": "APF_TX_RATE_BASIC",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate6M": {
                                                    "default": "APF_TX_RATE_NOT_APPLICABLE",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate9M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDescription": {
                                                    "maxLength": 64,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "rfProfileDot11Ax6GhzFeature": {
                                                    "default": "HE_6GHZ_NONE",
                                                    "enum": [
                                                        "HE_6GHZ_FILS_DISCOVERY",
                                                        "HE_6GHZ_NONE",
                                                        "HE_6GHZ_UBPR"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDot11axNonSrgObssPdMax": {
                                                    "default": -62,
                                                    "maximum": -62,
                                                    "minimum": -82,
                                                    "type": "integer"
                                                },
                                                "rfProfileDot11axObssPdEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileDot11axSrgObssPdEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileDot11axSrgObssPdMax": {
                                                    "default": -62,
                                                    "maximum": -62,
                                                    "minimum": -82,
                                                    "type": "integer"
                                                },
                                                "rfProfileDot11axSrgObssPdMin": {
                                                    "default": -82,
                                                    "maximum": -62,
                                                    "minimum": -82,
                                                    "type": "integer"
                                                },
                                                "rfProfileExceptionLevel": {
                                                    "default": 25,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "rfProfileFraAction": {
                                                    "default": "FRA_ACTION_DEFAULT",
                                                    "enum": [
                                                        "FRA_ACTION_DEFAULT",
                                                        "FRA_ACTION_MONITOR"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileGuardIntervalExt": {
                                                    "default": "GUARD_INTERVAL_NONE",
                                                    "enum": [
                                                        "GUARD_INTERVAL_1600NS",
                                                        "GUARD_INTERVAL_3200NS",
                                                        "GUARD_INTERVAL_400NS",
                                                        "GUARD_INTERVAL_800NS",
                                                        "GUARD_INTERVAL_NONE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileHsrMode": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileHsrNeighborTimeout": {
                                                    "default": 5,
                                                    "maximum": 60,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "rfProfileLoadBalancingWindow": {
                                                    "default": 5,
                                                    "maximum": 20,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "rfProfileManagementRetries": {
                                                    "default": -1,
                                                    "maximum": 255,
                                                    "minimum": -1,
                                                    "type": "integer"
                                                },
                                                "rfProfileMaxRadioClients": {
                                                    "default": 200,
                                                    "maximum": 500,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "rfProfileMbssidProfName": {
                                                    "default": "default-multi-bssid-profile",
                                                    "type": "string"
                                                },
                                                "rfProfileMinNumClients": {
                                                    "default": 3,
                                                    "maximum": 200,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "rfProfileMulticastDataRate": {
                                                    "default": "MCAST_DATA_RATE_DEFAULT",
                                                    "enum": [
                                                        "MCAST_DATA_RATE_12M",
                                                        "MCAST_DATA_RATE_18M",
                                                        "MCAST_DATA_RATE_24M",
                                                        "MCAST_DATA_RATE_36M",
                                                        "MCAST_DATA_RATE_48M",
                                                        "MCAST_DATA_RATE_54M",
                                                        "MCAST_DATA_RATE_6M",
                                                        "MCAST_DATA_RATE_9M",
                                                        "MCAST_DATA_RATE_DEFAULT"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileName": {
                                                    "maxLength": 32,
                                                    "minLength": 1,
                                                    "type": "string"
                                                },
                                                "rfProfileNdpMode": {
                                                    "default": "NDP_MODE_AUTO",
                                                    "enum": [
                                                        "NDP_MODE_AUTO",
                                                        "NDP_MODE_OFF_CHANNEL"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileNonAggregateRetries": {
                                                    "default": -1,
                                                    "maximum": 255,
                                                    "minimum": -1,
                                                    "type": "integer"
                                                },
                                                "rfProfileOptRoamRssiThreshold": {
                                                    "default": -127,
                                                    "maximum": 0,
                                                    "minimum": -127,
                                                    "type": "integer"
                                                },
                                                "rfProfilePreamblePuncture": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfilePscBias": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileRfDcaChannelWidth": {
                                                    "default": "RF_DCA_CHAN_WIDTH_BEST",
                                                    "enum": [
                                                        "RF_DCA_CHAN_WIDTH_160_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_20_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_40_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_80_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_8080_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_BEST"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileStatus": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileStdPwrModeAllowed": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileTrapThresholdClients": {
                                                    "default": 12,
                                                    "maximum": 200,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "rfProfileTxPowerMax": {
                                                    "default": 30,
                                                    "maximum": 30,
                                                    "minimum": -10,
                                                    "type": "integer"
                                                },
                                                "rfProfileTxPowerMin": {
                                                    "default": -10,
                                                    "maximum": 30,
                                                    "minimum": -10,
                                                    "type": "integer"
                                                },
                                                "rfProfileTxPowerV1Threshold": {
                                                    "default": -70,
                                                    "maximum": -50,
                                                    "minimum": -80,
                                                    "type": "integer"
                                                },
                                                "rfProfileTxPowerV2Threshold": {
                                                    "default": -67,
                                                    "maximum": -50,
                                                    "minimum": -80,
                                                    "type": "integer"
                                                },
                                                "rfProfileZerowtDfs": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfUnii3LpChannelsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rxSopSensitivityCustom": {
                                                    "default": -85,
                                                    "maximum": -60,
                                                    "minimum": -85,
                                                    "type": "integer"
                                                },
                                                "rxSopSensitivityThreshold": {
                                                    "default": "RRM_EWLC_RXSENSOP_THRESHOLD_AUTO",
                                                    "enum": [
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_AUTO",
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_CUSTOM",
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_HIGH",
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_LOW",
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_MEDIUM"
                                                    ],
                                                    "type": "string"
                                                },
                                                "trapThresholdInterference": {
                                                    "default": 10,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "trapThresholdNoise": {
                                                    "default": -70,
                                                    "maximum": 0,
                                                    "minimum": -127,
                                                    "type": "integer"
                                                },
                                                "trapThresholdUtilization": {
                                                    "default": 80,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                }
                                            },
                                            "required": [
                                                "deviceVersion",
                                                "rfProfileName"
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
                                                "bandSelectAgeOutDualBand": {
                                                    "default": 60,
                                                    "maximum": 300,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "bandSelectAgeOutSuppression": {
                                                    "default": 20,
                                                    "maximum": 200,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "bandSelectClientMidRssi": {
                                                    "default": -80,
                                                    "maximum": -20,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                },
                                                "bandSelectClientRssi": {
                                                    "default": -80,
                                                    "maximum": -20,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                },
                                                "bandSelectCycleCount": {
                                                    "default": 2,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "bandSelectCycleThreshold": {
                                                    "default": 200,
                                                    "maximum": 1000,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "bandSelectProbeResponse": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "clientNetworkPreference": {
                                                    "default": "DEFAULT",
                                                    "enum": [
                                                        "CONNECTIVITY",
                                                        "DEFAULT",
                                                        "THROUGHPUT"
                                                    ],
                                                    "type": "string"
                                                },
                                                "clientResetThresh6Ghz": {
                                                    "default": 5,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "clientResetThreshold": {
                                                    "default": 5,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "clientSelectThreshold": {
                                                    "default": 50,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "configType": {
                                                    "default": "RF_PROFILE",
                                                    "enum": [
                                                        "RF_PROFILE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "coverageDataPacketRssiThreshold": {
                                                    "default": -80,
                                                    "maximum": -60,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                },
                                                "coverageVoicePacketRssiThreshold": {
                                                    "default": -80,
                                                    "maximum": -60,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                },
                                                "dcaContributionInterference": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "deviceVersion": {
                                                    "default": "26.01",
                                                    "type": "string"
                                                },
                                                "dot11axBcastProbeRespIntvl": {
                                                    "default": 20,
                                                    "maximum": 25,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "loadBalancingDenialCount": {
                                                    "default": 3,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "optRoamRssiCheckEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileAggregateRetries": {
                                                    "default": -1,
                                                    "maximum": 255,
                                                    "minimum": -1,
                                                    "type": "integer"
                                                },
                                                "rfProfileAirtimeAllocation": {
                                                    "default": 5,
                                                    "maximum": 90,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "rfProfileAmpduWindowSize": {
                                                    "default": 255,
                                                    "maximum": 255,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "rfProfileAtfOperMode": {
                                                    "default": "APF_ATF_MODE_DISABLE",
                                                    "enum": [
                                                        "APF_ATF_MODE_DISABLE",
                                                        "APF_ATF_MODE_MONITOR",
                                                        "APF_ATF_MODE_SSID"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileAtfOptimization": {
                                                    "default": "APF_ATF_STEALING_POLICY_DISABLE",
                                                    "enum": [
                                                        "APF_ATF_STEALING_POLICY_DISABLE",
                                                        "APF_ATF_STEALING_POLICY_ENABLE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileBand": {
                                                    "enum": [
                                                        "DOT11_2_DOT_4_GHZ_BAND",
                                                        "DOT11_5_GHZ_BAND",
                                                        "DOT11_6_GHZ_BAND",
                                                        "DOT11_INVALID_BAND"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileBridgeClientAccess": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileChannelWidthMax": {
                                                    "default": "DCA_EWLC_CHAN_WIDTH_CAP_MAX",
                                                    "enum": [
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_160_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_20_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_320_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_40_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_80_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_MAX"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileChannelWidthMin": {
                                                    "default": "DCA_EWLC_CHAN_WIDTH_CAP_20_MHZ",
                                                    "enum": [
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_160_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_20_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_320_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_40_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_80_MHZ",
                                                        "DCA_EWLC_CHAN_WIDTH_CAP_MAX"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileClientAwareFra": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileClientCountReset6Ghz": {
                                                    "default": 1,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "rfProfileDataRate11M": {
                                                    "default": "APF_TX_RATE_BASIC",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate12M": {
                                                    "default": "APF_TX_RATE_NOT_APPLICABLE",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate18M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate1M": {
                                                    "default": "APF_TX_RATE_BASIC",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate24M": {
                                                    "default": "APF_TX_RATE_NOT_APPLICABLE",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate2M": {
                                                    "default": "APF_TX_RATE_BASIC",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate36M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate48M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate54M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate55M": {
                                                    "default": "APF_TX_RATE_BASIC",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate6M": {
                                                    "default": "APF_TX_RATE_NOT_APPLICABLE",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDataRate9M": {
                                                    "default": "APF_TX_RATE_SUPPORTED",
                                                    "enum": [
                                                        "APF_TX_RATE_BASIC",
                                                        "APF_TX_RATE_NOT_APPLICABLE",
                                                        "APF_TX_RATE_SUPPORTED",
                                                        "APF_TX_RATE_UNSUPPORTED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDescription": {
                                                    "maxLength": 64,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "rfProfileDot11Ax6GhzFeature": {
                                                    "default": "HE_6GHZ_NONE",
                                                    "enum": [
                                                        "HE_6GHZ_FILS_DISCOVERY",
                                                        "HE_6GHZ_NONE",
                                                        "HE_6GHZ_UBPR"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileDot11axNonSrgObssPdMax": {
                                                    "default": -62,
                                                    "maximum": -62,
                                                    "minimum": -82,
                                                    "type": "integer"
                                                },
                                                "rfProfileDot11axObssPdEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileDot11axSrgObssPdEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileDot11axSrgObssPdMax": {
                                                    "default": -62,
                                                    "maximum": -62,
                                                    "minimum": -82,
                                                    "type": "integer"
                                                },
                                                "rfProfileDot11axSrgObssPdMin": {
                                                    "default": -82,
                                                    "maximum": -62,
                                                    "minimum": -82,
                                                    "type": "integer"
                                                },
                                                "rfProfileExceptionLevel": {
                                                    "default": 25,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "rfProfileFraAction": {
                                                    "default": "FRA_ACTION_DEFAULT",
                                                    "enum": [
                                                        "FRA_ACTION_DEFAULT",
                                                        "FRA_ACTION_MONITOR"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileGuardIntervalExt": {
                                                    "default": "GUARD_INTERVAL_NONE",
                                                    "enum": [
                                                        "GUARD_INTERVAL_1600NS",
                                                        "GUARD_INTERVAL_3200NS",
                                                        "GUARD_INTERVAL_400NS",
                                                        "GUARD_INTERVAL_800NS",
                                                        "GUARD_INTERVAL_NONE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileHsrMode": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileHsrNeighborTimeout": {
                                                    "default": 5,
                                                    "maximum": 60,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "rfProfileIotCoexMode": {
                                                    "default": "AP_COEX_MODE_DISABLE",
                                                    "enum": [
                                                        "AP_COEX_MODE_DISABLE",
                                                        "AP_COEX_MODE_ENABLE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileLoadBalancingWindow": {
                                                    "default": 5,
                                                    "maximum": 20,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "rfProfileManagementRetries": {
                                                    "default": -1,
                                                    "maximum": 255,
                                                    "minimum": -1,
                                                    "type": "integer"
                                                },
                                                "rfProfileMaxRadioClients": {
                                                    "default": 200,
                                                    "maximum": 500,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "rfProfileMbssidProfName": {
                                                    "default": "default-multi-bssid-profile",
                                                    "type": "string"
                                                },
                                                "rfProfileMinNumClients": {
                                                    "default": 3,
                                                    "maximum": 200,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "rfProfileMulticastDataRate": {
                                                    "default": "MCAST_DATA_RATE_DEFAULT",
                                                    "enum": [
                                                        "MCAST_DATA_RATE_12M",
                                                        "MCAST_DATA_RATE_18M",
                                                        "MCAST_DATA_RATE_24M",
                                                        "MCAST_DATA_RATE_36M",
                                                        "MCAST_DATA_RATE_48M",
                                                        "MCAST_DATA_RATE_54M",
                                                        "MCAST_DATA_RATE_6M",
                                                        "MCAST_DATA_RATE_9M",
                                                        "MCAST_DATA_RATE_DEFAULT"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileName": {
                                                    "maxLength": 32,
                                                    "minLength": 1,
                                                    "type": "string"
                                                },
                                                "rfProfileNdpMode": {
                                                    "default": "NDP_MODE_AUTO",
                                                    "enum": [
                                                        "NDP_MODE_AUTO",
                                                        "NDP_MODE_OFF_CHANNEL"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileNonAggregateRetries": {
                                                    "default": -1,
                                                    "maximum": 255,
                                                    "minimum": -1,
                                                    "type": "integer"
                                                },
                                                "rfProfileOptRoamRssiThreshold": {
                                                    "default": -127,
                                                    "maximum": 0,
                                                    "minimum": -127,
                                                    "type": "integer"
                                                },
                                                "rfProfilePreamblePuncture": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfilePscBias": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileRfDcaChannelWidth": {
                                                    "default": "RF_DCA_CHAN_WIDTH_BEST",
                                                    "enum": [
                                                        "RF_DCA_CHAN_WIDTH_160_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_20_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_40_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_80_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_8080_MHZ",
                                                        "RF_DCA_CHAN_WIDTH_BEST"
                                                    ],
                                                    "type": "string"
                                                },
                                                "rfProfileStatus": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileStdPwrModeAllowed": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfProfileTrapThresholdClients": {
                                                    "default": 12,
                                                    "maximum": 200,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "rfProfileTxPowerMax": {
                                                    "default": 30,
                                                    "maximum": 30,
                                                    "minimum": -10,
                                                    "type": "integer"
                                                },
                                                "rfProfileTxPowerMin": {
                                                    "default": -10,
                                                    "maximum": 30,
                                                    "minimum": -10,
                                                    "type": "integer"
                                                },
                                                "rfProfileTxPowerV1Threshold": {
                                                    "default": -70,
                                                    "maximum": -50,
                                                    "minimum": -80,
                                                    "type": "integer"
                                                },
                                                "rfProfileTxPowerV2Threshold": {
                                                    "default": -67,
                                                    "maximum": -50,
                                                    "minimum": -80,
                                                    "type": "integer"
                                                },
                                                "rfProfileZerowtDfs": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfUnii3LpChannelsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rxSopSensitivityCustom": {
                                                    "default": -85,
                                                    "maximum": -60,
                                                    "minimum": -85,
                                                    "type": "integer"
                                                },
                                                "rxSopSensitivityThreshold": {
                                                    "default": "RRM_EWLC_RXSENSOP_THRESHOLD_AUTO",
                                                    "enum": [
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_AUTO",
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_CUSTOM",
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_HIGH",
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_LOW",
                                                        "RRM_EWLC_RXSENSOP_THRESHOLD_MEDIUM"
                                                    ],
                                                    "type": "string"
                                                },
                                                "trapThresholdInterference": {
                                                    "default": 10,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "trapThresholdNoise": {
                                                    "default": -70,
                                                    "maximum": 0,
                                                    "minimum": -127,
                                                    "type": "integer"
                                                },
                                                "trapThresholdUtilization": {
                                                    "default": 80,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                }
                                            },
                                            "required": [
                                                "deviceVersion",
                                                "rfProfileName"
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
