"""Cisco Catalyst Center GetConfigurationsForASpecificInstanceOfAApJoinProfileFeatureOnAWirelessContr
oller data model.

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


class JSONSchemaValidatorA1D0B19F735Feb8AbcA0B120Ac7A50:
    """GetConfigurationsForASpecificInstanceOfAApJoinProfileFeatureOnAWir
    elessController request schema definition."""

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
                                                "acctMethodList": {
                                                    "type": "string"
                                                },
                                                "actionApReloadEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "adrIndividualAggrEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "adrIndividualEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "adrIndividualPcThrottle": {
                                                    "default": 5,
                                                    "maximum": 50,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "adrIndividualPtThrottle": {
                                                    "default": 5,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "adrSummaryEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "alarmHoldTime": {
                                                    "default": 6,
                                                    "maximum": 3600,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "alarmsEnabled": {
                                                    "type": "boolean"
                                                },
                                                "anomalyDetTriggerTraceAp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "anomalyDetectionEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "antennaMonitorDetectionTime": {
                                                    "default": 12,
                                                    "maximum": 180,
                                                    "minimum": 9,
                                                    "type": "integer"
                                                },
                                                "antennaMonitorEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "antennaMonitorRssiFailThreshold": {
                                                    "default": 40,
                                                    "maximum": 90,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "apCfgProfileDescription": {
                                                    "type": "string"
                                                },
                                                "apCfgProfileLedFlashSec": {
                                                    "default": 0,
                                                    "maximum": 3600,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "apCfgProfileName": {
                                                    "type": "string"
                                                },
                                                "apCfgProfileStatsTimer": {
                                                    "default": 180,
                                                    "maximum": 65535,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "apCountryCountryCode": {
                                                    "default": "UNCONFIGURED",
                                                    "enum": [
                                                        "AD",
                                                        "AE",
                                                        "AF",
                                                        "AG",
                                                        "AI",
                                                        "AL",
                                                        "AM",
                                                        "AO",
                                                        "AQ",
                                                        "AR",
                                                        "AS",
                                                        "AT",
                                                        "AU",
                                                        "AW",
                                                        "AX",
                                                        "AZ",
                                                        "BA",
                                                        "BB",
                                                        "BD",
                                                        "BE",
                                                        "BF",
                                                        "BG",
                                                        "BH",
                                                        "BI",
                                                        "BJ",
                                                        "BL",
                                                        "BM",
                                                        "BN",
                                                        "BO",
                                                        "BQ",
                                                        "BR",
                                                        "BS",
                                                        "BT",
                                                        "BV",
                                                        "BW",
                                                        "BY",
                                                        "BZ",
                                                        "CA",
                                                        "CC",
                                                        "CD",
                                                        "CF",
                                                        "CG",
                                                        "CH",
                                                        "CI",
                                                        "CK",
                                                        "CL",
                                                        "CM",
                                                        "CN",
                                                        "CO",
                                                        "CR",
                                                        "CU",
                                                        "CV",
                                                        "CW",
                                                        "CX",
                                                        "CY",
                                                        "CZ",
                                                        "DE",
                                                        "DJ",
                                                        "DK",
                                                        "DM",
                                                        "DO",
                                                        "DZ",
                                                        "EC",
                                                        "EE",
                                                        "EG",
                                                        "EH",
                                                        "EL",
                                                        "ER",
                                                        "ES",
                                                        "ET",
                                                        "FI",
                                                        "FJ",
                                                        "FK",
                                                        "FM",
                                                        "FO",
                                                        "FR",
                                                        "GA",
                                                        "GB",
                                                        "GD",
                                                        "GE",
                                                        "GF",
                                                        "GG",
                                                        "GH",
                                                        "GI",
                                                        "GL",
                                                        "GM",
                                                        "GN",
                                                        "GP",
                                                        "GQ",
                                                        "GR",
                                                        "GS",
                                                        "GT",
                                                        "GU",
                                                        "GW",
                                                        "GY",
                                                        "HK",
                                                        "HM",
                                                        "HN",
                                                        "HR",
                                                        "HT",
                                                        "HU",
                                                        "ID",
                                                        "IE",
                                                        "IL",
                                                        "IM",
                                                        "IN",
                                                        "IO",
                                                        "IQ",
                                                        "IR",
                                                        "IS",
                                                        "IT",
                                                        "J2",
                                                        "J3",
                                                        "J4",
                                                        "JE",
                                                        "JM",
                                                        "JO",
                                                        "JP",
                                                        "KE",
                                                        "KG",
                                                        "KH",
                                                        "KI",
                                                        "KM",
                                                        "KN",
                                                        "KP",
                                                        "KR",
                                                        "KW",
                                                        "KY",
                                                        "KZ",
                                                        "LA",
                                                        "LB",
                                                        "LC",
                                                        "LI",
                                                        "LK",
                                                        "LR",
                                                        "LS",
                                                        "LT",
                                                        "LU",
                                                        "LV",
                                                        "LY",
                                                        "MA",
                                                        "MC",
                                                        "MD",
                                                        "ME",
                                                        "MF",
                                                        "MG",
                                                        "MH",
                                                        "MK",
                                                        "ML",
                                                        "MM",
                                                        "MN",
                                                        "MO",
                                                        "MP",
                                                        "MQ",
                                                        "MR",
                                                        "MS",
                                                        "MT",
                                                        "MU",
                                                        "MV",
                                                        "MW",
                                                        "MX",
                                                        "MY",
                                                        "MZ",
                                                        "NA",
                                                        "NC",
                                                        "NE",
                                                        "NF",
                                                        "NG",
                                                        "NI",
                                                        "NL",
                                                        false,
                                                        "NP",
                                                        "NR",
                                                        "NU",
                                                        "NZ",
                                                        "OM",
                                                        "PA",
                                                        "PE",
                                                        "PF",
                                                        "PG",
                                                        "PH",
                                                        "PK",
                                                        "PL",
                                                        "PM",
                                                        "PN",
                                                        "PR",
                                                        "PS",
                                                        "PT",
                                                        "PW",
                                                        "PY",
                                                        "QA",
                                                        "RE",
                                                        "RO",
                                                        "RS",
                                                        "RU",
                                                        "RW",
                                                        "SA",
                                                        "SB",
                                                        "SC",
                                                        "SD",
                                                        "SE",
                                                        "SG",
                                                        "SH",
                                                        "SI",
                                                        "SJ",
                                                        "SK",
                                                        "SL",
                                                        "SM",
                                                        "SN",
                                                        "SO",
                                                        "SR",
                                                        "SS",
                                                        "ST",
                                                        "SV",
                                                        "SX",
                                                        "SY",
                                                        "SZ",
                                                        "TC",
                                                        "TD",
                                                        "TF",
                                                        "TG",
                                                        "TH",
                                                        "TI",
                                                        "TJ",
                                                        "TK",
                                                        "TL",
                                                        "TM",
                                                        "TN",
                                                        "TO",
                                                        "TR",
                                                        "TT",
                                                        "TV",
                                                        "TW",
                                                        "TZ",
                                                        "UA",
                                                        "UG",
                                                        "UM",
                                                        "UNCONFIGURED",
                                                        "US",
                                                        "UY",
                                                        "UZ",
                                                        "VA",
                                                        "VC",
                                                        "VE",
                                                        "VG",
                                                        "VI",
                                                        "VN",
                                                        "VU",
                                                        "WF",
                                                        "WS",
                                                        "XK",
                                                        "YE",
                                                        "YT",
                                                        "ZA",
                                                        "ZM",
                                                        "ZW"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apDtlsCtrlPrefEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "apLagEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apNtpServerInfoKeyType": {
                                                    "default": "AP_NTP_KEY_TYPE_MD5",
                                                    "enum": [
                                                        "AP_NTP_KEY_TYPE_MD5",
                                                        "AP_NTP_KEY_TYPE_SHA1"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apPacketCaptureProfile": {
                                                    "type": "string"
                                                },
                                                "apProfPpCfgPowerProfileName": {
                                                    "maxLength": 128,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "apRogueDetectionEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "apRogueDetectionMinRssi": {
                                                    "default": -90,
                                                    "maximum": -70,
                                                    "minimum": -128,
                                                    "type": "integer"
                                                },
                                                "apRogueDetectionTransientInterval": {
                                                    "default": 0,
                                                    "type": "integer"
                                                },
                                                "apStatsDnsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsDnsFreq": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsInterfaceEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsInterfaceFreq": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsMemoryEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsMemoryFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsRadioEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsRadioFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsRoutingEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsRoutingFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsSysEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsSystemFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsWlanEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsWlanFreq": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apSubModeType": {
                                                    "enum": [
                                                        "AP_SUB_MODE_NONE",
                                                        "FORENSIC_AWIPS_MODE",
                                                        "LOCAL_NETWORK",
                                                        "NON_LOCAL_NETWORK",
                                                        "WIPS_MODE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apTraceProfile": {
                                                    "type": "string"
                                                },
                                                "apTrustsUpstreamDscpEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "apTzConfigMode": {
                                                    "default": "AP_TZ_NOT_CONFIGURED",
                                                    "enum": [
                                                        "AP_TZ_CONTROLLER_TZ",
                                                        "AP_TZ_NOT_CONFIGURED",
                                                        "AP_TZ_UTC_OFFSET"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apTzConfigOffsetHour": {
                                                    "default": 0,
                                                    "maximum": 14,
                                                    "minimum": -12,
                                                    "type": "integer"
                                                },
                                                "apTzConfigOffsetMin": {
                                                    "default": 0,
                                                    "maximum": 59,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "apphostEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "auxClientInterfaceVlanId": {
                                                    "default": 0,
                                                    "maximum": 4094,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "awipsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "awipsForensicEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "bleBeaconAdvpwr": {
                                                    "default": 59,
                                                    "maximum": 100,
                                                    "minimum": 40,
                                                    "type": "integer"
                                                },
                                                "bleBeaconInterval": {
                                                    "default": 1,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "bleScanStateEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "bssidEnableStats": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "bssidNeighborStatsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "bssidNeighborStatsFrequency": {
                                                    "default": 30,
                                                    "maximum": 600,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "bssidStatsFrequency": {
                                                    "default": 30,
                                                    "maximum": 180,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "capwapWindowWindowSize": {
                                                    "default": 1,
                                                    "maximum": 50,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "cdpEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "clientFilterStatsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "clientFilterStatsFrequency": {
                                                    "default": 5,
                                                    "maximum": 3600,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "clientRssiStatsEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "clientRssiStatsInterval": {
                                                    "default": 30,
                                                    "maximum": 300,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "clientStatsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "clientStatsFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "configType": {
                                                    "default": "AP_JOIN_PROFILE",
                                                    "enum": [
                                                        "AP_JOIN_PROFILE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "coredumpFlagEnabled": {
                                                    "default": "TFTP_COREDUMP_DISABLE",
                                                    "enum": [
                                                        "TFTP_COREDUMP_COMPRESS",
                                                        "TFTP_COREDUMP_DISABLE",
                                                        "TFTP_COREDUMP_UNCOMPRESS"
                                                    ],
                                                    "type": "string"
                                                },
                                                "corefileName": {
                                                    "default": "default",
                                                    "type": "string"
                                                },
                                                "cpuThreshold": {
                                                    "default": 0,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "dataEncryptionEnabled": {
                                                    "type": "boolean"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.12",
                                                    "type": "string"
                                                },
                                                "dhcpFallbackEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "dhcpServerEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "discoveryTimeout": {
                                                    "default": 10,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "dot1xEapTypeInfoDot1xEapType": {
                                                    "default": "DOT1X_EAP_FAST",
                                                    "enum": [
                                                        "DOT1X_EAP_FAST",
                                                        "DOT1X_EAP_NONE",
                                                        "DOT1X_EAP_PEAP",
                                                        "DOT1X_EAP_TLS"
                                                    ],
                                                    "type": "string"
                                                },
                                                "dot1xPassword": {
                                                    "type": "string"
                                                },
                                                "dot1xUsername": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "extModuleEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "fallbackEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "fastChannel": {
                                                    "maximum": 4294967295,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "fastHeartBeatTimeout": {
                                                    "default": 0,
                                                    "maximum": 10,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "ftmEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "ftmInitBurstDuration": {
                                                    "default": "ENUM_32MS",
                                                    "enum": [
                                                        "ENUM_128MS",
                                                        "ENUM_16MS",
                                                        "ENUM_1MS",
                                                        "ENUM_250US",
                                                        "ENUM_2MS",
                                                        "ENUM_32MS",
                                                        "ENUM_4MS",
                                                        "ENUM_500US",
                                                        "ENUM_64MS",
                                                        "ENUM_8MS",
                                                        "ANY"
                                                    ],
                                                    "type": "string"
                                                },
                                                "ftmInitBurstSize": {
                                                    "default": 8,
                                                    "maximum": 64,
                                                    "minimum": 4,
                                                    "type": "integer"
                                                },
                                                "gasRateLimitEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "gasRateLimitIntervalMsec": {
                                                    "maximum": 10000,
                                                    "minimum": 100,
                                                    "type": "integer"
                                                },
                                                "gasRateLimitNumReqPerInterval": {
                                                    "maximum": 100,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "grpcEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "heartBeatTimeout": {
                                                    "default": 30,
                                                    "maximum": 30,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "hyperlocationEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "icapAdrIndividualThrottle": {
                                                    "default": 5,
                                                    "maximum": 500,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "icapAdrSummaryFrequency": {
                                                    "default": 5,
                                                    "maximum": 60,
                                                    "minimum": 3,
                                                    "type": "integer"
                                                },
                                                "icapAggrTraceEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "icapAnomalyDetDhcpTimeout": {
                                                    "default": 5,
                                                    "maximum": 120,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "icapFullTraceEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "injectorSwitchMacAddr": {
                                                    "default": "00:00:00:00:00:00",
                                                    "type": "string"
                                                },
                                                "isRfSpectrumSlot2Enabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "jumboMtuEnabled": {
                                                    "type": "boolean"
                                                },
                                                "kernelCoredumpLimit": {
                                                    "default": 0,
                                                    "maximum": 5,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "lawfulInterceptionEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "lawfulInterceptionTimerInterval": {
                                                    "default": 60,
                                                    "maximum": 600,
                                                    "minimum": 60,
                                                    "type": "integer"
                                                },
                                                "ledFlashMode": {
                                                    "default": "LED_FLASH_MODE_INDEFINITE",
                                                    "enum": [
                                                        "LED_FLASH_MODE_DISABLE",
                                                        "LED_FLASH_MODE_DURATION",
                                                        "LED_FLASH_MODE_INDEFINITE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "ledStateEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "linkLatencyFlagEnabled": {
                                                    "default": "LINK_AUDITING_DISABLE",
                                                    "enum": [
                                                        "LINK_AUDITING_DATA",
                                                        "LINK_AUDITING_DISABLE",
                                                        "LINK_AUDITING_ENABLE",
                                                        "LINK_AUDITING_RESET"
                                                    ],
                                                    "type": "string"
                                                },
                                                "loginCredentialsDot1xPasswordType": {
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
                                                "lscApAuthTypeInfoAuthType": {
                                                    "default": "LSC_AP_AUTH_CAPWAP_DTLS",
                                                    "enum": [
                                                        "LSC_AP_AUTH_BOTH",
                                                        "LSC_AP_AUTH_CAPWAP_DTLS",
                                                        "LSC_AP_AUTH_DOT1X_PORT_AUTH",
                                                        "LSC_AP_AUTH_NONE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "max1xSessionLimitPerAp": {
                                                    "default": 0,
                                                    "type": "integer"
                                                },
                                                "maxCfgClients": {
                                                    "default": 0,
                                                    "maximum": 1200,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "memThresholdStatsMonitor": {
                                                    "default": 0,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "meshProfileName": {
                                                    "default": "default-mesh-profile",
                                                    "type": "string"
                                                },
                                                "noProxyList": {
                                                    "type": "string"
                                                },
                                                "ntpServerInfoKeyFormat": {
                                                    "default": "AP_NTP_KEY_FORMAT_ASCII",
                                                    "enum": [
                                                        "AP_NTP_KEY_FORMAT_ASCII",
                                                        "AP_NTP_KEY_FORMAT_HEX"
                                                    ],
                                                    "type": "string"
                                                },
                                                "ntpServerInfoKeyId": {
                                                    "default": 1,
                                                    "maximum": 65535,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "ntpServerInfoNtpAddr": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "ntpServerTrustKey": {
                                                    "type": "string"
                                                },
                                                "oeapDataEncryptionEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "oeapLocalNet": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "oeapRogueDetectEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "pakRssiThresholdDetection": {
                                                    "default": -100,
                                                    "maximum": -50,
                                                    "minimum": -100,
                                                    "type": "integer"
                                                },
                                                "pakRssiThresholdReset": {
                                                    "default": 8,
                                                    "maximum": 99,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "pakRssiThresholdTrigger": {
                                                    "default": 10,
                                                    "maximum": 100,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "partialTraceEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoAll": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoCiscoAll": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoCiscoNdp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataAll": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataArp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataDhcp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataDhcpv6": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataDns": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataEap": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataIcmp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataIcmpv6": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoMgmtAll": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoMgmtAssoc": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoMgmtAuth": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoMgmtProbe": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "persistentSsidBroadcastEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "pmfDeauthEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "powerInjectorSelection": {
                                                    "default": "PWRINJ_UNKNOWN",
                                                    "enum": [
                                                        "PWRINJ_INSTALLED",
                                                        "PWRINJ_OVERRIDE",
                                                        "PWRINJ_UNKNOWN"
                                                    ],
                                                    "type": "string"
                                                },
                                                "powerInjectorStateEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "preStandard8023afSwitchFlag": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "pressSensConfigState": {
                                                    "default": "PRESS_SENSOR_AUTO",
                                                    "enum": [
                                                        "PRESS_SENSOR_AUTO",
                                                        "PRESS_SENSOR_DISABLED",
                                                        "PRESS_SENSOR_ENABLED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "primaryControllerIpAddr": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "primaryControllerName": {
                                                    "type": "string"
                                                },
                                                "primaryDiscoveryTimeout": {
                                                    "default": 120,
                                                    "maximum": 3000,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "primedJoinTimeout": {
                                                    "default": 0,
                                                    "maximum": 43200,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "privateIpDiscoveryEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "provisionalSsidEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "proxyHostname": {
                                                    "type": "string"
                                                },
                                                "proxyPort": {
                                                    "maximum": 65535,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "publicIpDiscoveryEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "qosmapActionFrameEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "radio24GhzReportingInterval": {
                                                    "default": 90,
                                                    "maximum": 90,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "radio5GhzReportingInterval": {
                                                    "default": 90,
                                                    "maximum": 90,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "radioResetEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "radioStatsMonitorAlarmsEnabled": {
                                                    "type": "boolean"
                                                },
                                                "radioStatsMonitorEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "retransmitTimerCount": {
                                                    "default": 5,
                                                    "maximum": 8,
                                                    "minimum": 3,
                                                    "type": "integer"
                                                },
                                                "retransmitTimerInterval": {
                                                    "default": 3,
                                                    "maximum": 5,
                                                    "minimum": 2,
                                                    "type": "integer"
                                                },
                                                "rfSpectrumEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfSpectrumSlot0Enabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfSpectrumSlot1Enabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfSpectrumSlot3Enabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rogueContainmentAutorate": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rogueContainmentFlexconnect": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rogueDetectionPmfDenial": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rogueDetectionProfileName": {
                                                    "type": "string"
                                                },
                                                "rogueReportInterval": {
                                                    "default": 10,
                                                    "maximum": 300,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "sampleInterval": {
                                                    "default": 720,
                                                    "maximum": 3600,
                                                    "minimum": 720,
                                                    "type": "integer"
                                                },
                                                "sampleIntvl": {
                                                    "default": 30,
                                                    "maximum": 900,
                                                    "minimum": 2,
                                                    "type": "integer"
                                                },
                                                "secondaryControllerIpAddr": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "secondaryControllerName": {
                                                    "type": "string"
                                                },
                                                "serialConsoleEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "sshEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "statsMonitorEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "statsMonitorStatsInterval": {
                                                    "default": 300,
                                                    "maximum": 900,
                                                    "minimum": 120,
                                                    "type": "integer"
                                                },
                                                "syslogFacilityValue": {
                                                    "default": "FACILITY_KERN",
                                                    "enum": [
                                                        "FACILITY_AUTH",
                                                        "FACILITY_CRON",
                                                        "FACILITY_DAEMON",
                                                        "FACILITY_KERN",
                                                        "FACILITY_LOCAL0",
                                                        "FACILITY_LOCAL1",
                                                        "FACILITY_LOCAL2",
                                                        "FACILITY_LOCAL3",
                                                        "FACILITY_LOCAL4",
                                                        "FACILITY_LOCAL5",
                                                        "FACILITY_LOCAL6",
                                                        "FACILITY_LOCAL7",
                                                        "FACILITY_LPR",
                                                        "FACILITY_MAIL",
                                                        "FACILITY_NEWS",
                                                        "FACILITY_SYS10",
                                                        "FACILITY_SYS11",
                                                        "FACILITY_SYS12",
                                                        "FACILITY_SYS13",
                                                        "FACILITY_SYS14",
                                                        "FACILITY_SYS9",
                                                        "FACILITY_SYSLOG",
                                                        "FACILITY_USER",
                                                        "FACILITY_UUCP"
                                                    ],
                                                    "type": "string"
                                                },
                                                "syslogHostIpAddress": {
                                                    "default": "255.255.255.255",
                                                    "type": "string"
                                                },
                                                "syslogLogLevel": {
                                                    "default": "SYSLOG_LEVEL_INFORMATION",
                                                    "enum": [
                                                        "SYSLOG_LEVEL_ALERT",
                                                        "SYSLOG_LEVEL_CRITICAL",
                                                        "SYSLOG_LEVEL_DEBUG",
                                                        "SYSLOG_LEVEL_EMERGENCY",
                                                        "SYSLOG_LEVEL_ERRORS",
                                                        "SYSLOG_LEVEL_INFORMATION",
                                                        "SYSLOG_LEVEL_NOTIFICATION",
                                                        "SYSLOG_LEVEL_WARNING"
                                                    ],
                                                    "type": "string"
                                                },
                                                "syslogTlsModeEnabled": {
                                                    "type": "boolean"
                                                },
                                                "tcpAdjustMss": {
                                                    "default": 1250,
                                                    "maximum": 1363,
                                                    "minimum": 536,
                                                    "type": "integer"
                                                },
                                                "tcpMssAdjustEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "telnetEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "tftpDowngradeFilename": {
                                                    "type": "string"
                                                },
                                                "tftpDowngradeIpAddress": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "tftpServerIpAddress": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "trafficDistributionInterval": {
                                                    "default": 300,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "trafficDistributionStatus": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "trapRetxTime": {
                                                    "default": 0,
                                                    "maximum": 65535,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "trustKeyType": {
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
                                                "tunnelPreferredMode": {
                                                    "default": "PREFERRED_MODE_UNCONFIG",
                                                    "enum": [
                                                        "PREFERRED_MODE_IPV4",
                                                        "PREFERRED_MODE_IPV6",
                                                        "PREFERRED_MODE_UNCONFIG"
                                                    ],
                                                    "type": "string"
                                                },
                                                "tzConfigEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "udpLiteIpv6CapwapChecksumType": {
                                                    "default": "UDPLITE_CHECKSUM_DISABLED",
                                                    "enum": [
                                                        "UDPLITE_CHECKSUM_DISABLED",
                                                        "UDPLITE_CHECKSUM_ENABLED",
                                                        "UDPLITE_CHECKSUM_UNCONFIGURED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "usbModuleEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "userMgmtPassword": {
                                                    "type": "string"
                                                },
                                                "userMgmtPasswordCryptType": {
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
                                                "userMgmtSecret": {
                                                    "type": "string"
                                                },
                                                "userMgmtSecretType": {
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
                                                "userMgmtUsername": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "weakRssi": {
                                                    "default": -60,
                                                    "maximum": -10,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                }
                                            },
                                            "required": [
                                                "apCfgProfileName",
                                                "deviceVersion"
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
                                                "acctMethodList": {
                                                    "type": "string"
                                                },
                                                "actionApReloadEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "adrIndividualAggrEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "adrIndividualEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "adrIndividualPcThrottle": {
                                                    "default": 5,
                                                    "maximum": 50,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "adrIndividualPtThrottle": {
                                                    "default": 5,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "adrSummaryEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "alarmHoldTime": {
                                                    "default": 6,
                                                    "maximum": 3600,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "alarmsEnabled": {
                                                    "type": "boolean"
                                                },
                                                "anomalyDetTriggerTraceAp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "anomalyDetectionEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "antennaMonitorDetectionTime": {
                                                    "default": 12,
                                                    "maximum": 180,
                                                    "minimum": 9,
                                                    "type": "integer"
                                                },
                                                "antennaMonitorEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "antennaMonitorRssiFailThreshold": {
                                                    "default": 40,
                                                    "maximum": 90,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "apCfgProfileDescription": {
                                                    "type": "string"
                                                },
                                                "apCfgProfileLedFlashSec": {
                                                    "default": 0,
                                                    "maximum": 3600,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "apCfgProfileName": {
                                                    "type": "string"
                                                },
                                                "apCfgProfileStatsTimer": {
                                                    "default": 180,
                                                    "maximum": 65535,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "apCountryCountryCode": {
                                                    "default": "UNCONFIGURED",
                                                    "enum": [
                                                        "AD",
                                                        "AE",
                                                        "AF",
                                                        "AG",
                                                        "AI",
                                                        "AL",
                                                        "AM",
                                                        "AO",
                                                        "AQ",
                                                        "AR",
                                                        "AS",
                                                        "AT",
                                                        "AU",
                                                        "AW",
                                                        "AX",
                                                        "AZ",
                                                        "BA",
                                                        "BB",
                                                        "BD",
                                                        "BE",
                                                        "BF",
                                                        "BG",
                                                        "BH",
                                                        "BI",
                                                        "BJ",
                                                        "BL",
                                                        "BM",
                                                        "BN",
                                                        "BO",
                                                        "BQ",
                                                        "BR",
                                                        "BS",
                                                        "BT",
                                                        "BV",
                                                        "BW",
                                                        "BY",
                                                        "BZ",
                                                        "CA",
                                                        "CC",
                                                        "CD",
                                                        "CF",
                                                        "CG",
                                                        "CH",
                                                        "CI",
                                                        "CK",
                                                        "CL",
                                                        "CM",
                                                        "CN",
                                                        "CO",
                                                        "CR",
                                                        "CU",
                                                        "CV",
                                                        "CW",
                                                        "CX",
                                                        "CY",
                                                        "CZ",
                                                        "DE",
                                                        "DJ",
                                                        "DK",
                                                        "DM",
                                                        "DO",
                                                        "DZ",
                                                        "EC",
                                                        "EE",
                                                        "EG",
                                                        "EH",
                                                        "EL",
                                                        "ER",
                                                        "ES",
                                                        "ET",
                                                        "FI",
                                                        "FJ",
                                                        "FK",
                                                        "FM",
                                                        "FO",
                                                        "FR",
                                                        "GA",
                                                        "GB",
                                                        "GD",
                                                        "GE",
                                                        "GF",
                                                        "GG",
                                                        "GH",
                                                        "GI",
                                                        "GL",
                                                        "GM",
                                                        "GN",
                                                        "GP",
                                                        "GQ",
                                                        "GR",
                                                        "GS",
                                                        "GT",
                                                        "GU",
                                                        "GW",
                                                        "GY",
                                                        "HK",
                                                        "HM",
                                                        "HN",
                                                        "HR",
                                                        "HT",
                                                        "HU",
                                                        "ID",
                                                        "IE",
                                                        "IL",
                                                        "IM",
                                                        "IN",
                                                        "IO",
                                                        "IQ",
                                                        "IR",
                                                        "IS",
                                                        "IT",
                                                        "J2",
                                                        "J3",
                                                        "J4",
                                                        "JE",
                                                        "JM",
                                                        "JO",
                                                        "JP",
                                                        "KE",
                                                        "KG",
                                                        "KH",
                                                        "KI",
                                                        "KM",
                                                        "KN",
                                                        "KP",
                                                        "KR",
                                                        "KW",
                                                        "KY",
                                                        "KZ",
                                                        "LA",
                                                        "LB",
                                                        "LC",
                                                        "LI",
                                                        "LK",
                                                        "LR",
                                                        "LS",
                                                        "LT",
                                                        "LU",
                                                        "LV",
                                                        "LY",
                                                        "MA",
                                                        "MC",
                                                        "MD",
                                                        "ME",
                                                        "MF",
                                                        "MG",
                                                        "MH",
                                                        "MK",
                                                        "ML",
                                                        "MM",
                                                        "MN",
                                                        "MO",
                                                        "MP",
                                                        "MQ",
                                                        "MR",
                                                        "MS",
                                                        "MT",
                                                        "MU",
                                                        "MV",
                                                        "MW",
                                                        "MX",
                                                        "MY",
                                                        "MZ",
                                                        "NA",
                                                        "NC",
                                                        "NE",
                                                        "NF",
                                                        "NG",
                                                        "NI",
                                                        "NL",
                                                        false,
                                                        "NP",
                                                        "NR",
                                                        "NU",
                                                        "NZ",
                                                        "OM",
                                                        "PA",
                                                        "PE",
                                                        "PF",
                                                        "PG",
                                                        "PH",
                                                        "PK",
                                                        "PL",
                                                        "PM",
                                                        "PN",
                                                        "PR",
                                                        "PS",
                                                        "PT",
                                                        "PW",
                                                        "PY",
                                                        "QA",
                                                        "RE",
                                                        "RO",
                                                        "RS",
                                                        "RU",
                                                        "RW",
                                                        "SA",
                                                        "SB",
                                                        "SC",
                                                        "SD",
                                                        "SE",
                                                        "SG",
                                                        "SH",
                                                        "SI",
                                                        "SJ",
                                                        "SK",
                                                        "SL",
                                                        "SM",
                                                        "SN",
                                                        "SO",
                                                        "SR",
                                                        "SS",
                                                        "ST",
                                                        "SV",
                                                        "SX",
                                                        "SY",
                                                        "SZ",
                                                        "TC",
                                                        "TD",
                                                        "TF",
                                                        "TG",
                                                        "TH",
                                                        "TI",
                                                        "TJ",
                                                        "TK",
                                                        "TL",
                                                        "TM",
                                                        "TN",
                                                        "TO",
                                                        "TR",
                                                        "TT",
                                                        "TV",
                                                        "TW",
                                                        "TZ",
                                                        "UA",
                                                        "UG",
                                                        "UM",
                                                        "UNCONFIGURED",
                                                        "US",
                                                        "UY",
                                                        "UZ",
                                                        "VA",
                                                        "VC",
                                                        "VE",
                                                        "VG",
                                                        "VI",
                                                        "VN",
                                                        "VU",
                                                        "WF",
                                                        "WS",
                                                        "XK",
                                                        "YE",
                                                        "YT",
                                                        "ZA",
                                                        "ZM",
                                                        "ZW"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apDeploymentModeType": {
                                                    "default": "AP_MODE_DEFAULT",
                                                    "enum": [
                                                        "AP_MODE_DEFAULT",
                                                        "AP_MODE_INDOOR",
                                                        "AP_MODE_OUTDOOR"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apDtlsCtrlPrefEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "apLagEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apNtpServerInfoKeyType": {
                                                    "default": "AP_NTP_KEY_TYPE_MD5",
                                                    "enum": [
                                                        "AP_NTP_KEY_TYPE_MD5",
                                                        "AP_NTP_KEY_TYPE_SHA1"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apPacketCaptureProfile": {
                                                    "type": "string"
                                                },
                                                "apProfPpCfgPowerProfileName": {
                                                    "maxLength": 128,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "apRogueDetectionEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "apRogueDetectionMinRssi": {
                                                    "default": -90,
                                                    "maximum": -70,
                                                    "minimum": -128,
                                                    "type": "integer"
                                                },
                                                "apRogueDetectionTransientInterval": {
                                                    "default": 0,
                                                    "type": "integer"
                                                },
                                                "apStatsDnsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsDnsFreq": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsInterfaceEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsInterfaceFreq": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsMemoryEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsMemoryFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsRadioEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsRadioFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsRoutingEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsRoutingFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsSysEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsSystemFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsWlanEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsWlanFreq": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apSubModeType": {
                                                    "enum": [
                                                        "AP_SUB_MODE_NONE",
                                                        "FORENSIC_AWIPS_MODE",
                                                        "LOCAL_NETWORK",
                                                        "NON_LOCAL_NETWORK",
                                                        "WIPS_MODE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apTraceProfile": {
                                                    "type": "string"
                                                },
                                                "apTrustsUpstreamDscpEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "apTzConfigMode": {
                                                    "default": "AP_TZ_NOT_CONFIGURED",
                                                    "enum": [
                                                        "AP_TZ_CONTROLLER_TZ",
                                                        "AP_TZ_NOT_CONFIGURED",
                                                        "AP_TZ_UTC_OFFSET"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apTzConfigOffsetHour": {
                                                    "default": 0,
                                                    "maximum": 14,
                                                    "minimum": -12,
                                                    "type": "integer"
                                                },
                                                "apTzConfigOffsetMin": {
                                                    "default": 0,
                                                    "maximum": 59,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "apphostEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "auxClientInterfaceVlanId": {
                                                    "default": 0,
                                                    "maximum": 4094,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "awipsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "awipsForensicEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "bleBeaconAdvpwr": {
                                                    "default": 59,
                                                    "maximum": 100,
                                                    "minimum": 40,
                                                    "type": "integer"
                                                },
                                                "bleBeaconInterval": {
                                                    "default": 1,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "bleScanStateEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "bssidEnableStats": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "bssidNeighborStatsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "bssidNeighborStatsFrequency": {
                                                    "default": 180,
                                                    "maximum": 600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "bssidStatsFrequency": {
                                                    "default": 30,
                                                    "maximum": 180,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "capwapWindowWindowSize": {
                                                    "default": 1,
                                                    "maximum": 50,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "cdpEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "clientFilterStatsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "clientFilterStatsFrequency": {
                                                    "default": 5,
                                                    "maximum": 3600,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "clientRssiStatsEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "clientRssiStatsInterval": {
                                                    "default": 30,
                                                    "maximum": 300,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "clientStatsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "clientStatsFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "configType": {
                                                    "default": "AP_JOIN_PROFILE",
                                                    "enum": [
                                                        "AP_JOIN_PROFILE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "coredumpFlagEnabled": {
                                                    "default": "TFTP_COREDUMP_DISABLE",
                                                    "enum": [
                                                        "TFTP_COREDUMP_COMPRESS",
                                                        "TFTP_COREDUMP_DISABLE",
                                                        "TFTP_COREDUMP_UNCOMPRESS"
                                                    ],
                                                    "type": "string"
                                                },
                                                "corefileName": {
                                                    "default": "default",
                                                    "type": "string"
                                                },
                                                "cpuThreshold": {
                                                    "default": 0,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "dataEncryptionEnabled": {
                                                    "type": "boolean"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.13",
                                                    "type": "string"
                                                },
                                                "dhcpFallbackEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "dhcpServerEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "discoveryTimeout": {
                                                    "default": 10,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "dot1xEapTypeInfoDot1xEapType": {
                                                    "default": "DOT1X_EAP_FAST",
                                                    "enum": [
                                                        "DOT1X_EAP_FAST",
                                                        "DOT1X_EAP_NONE",
                                                        "DOT1X_EAP_PEAP",
                                                        "DOT1X_EAP_TLS"
                                                    ],
                                                    "type": "string"
                                                },
                                                "dot1xPassword": {
                                                    "type": "string"
                                                },
                                                "dot1xUsername": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "extModuleEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "fallbackEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "fastChannel": {
                                                    "maximum": 4294967295,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "fastHeartBeatTimeout": {
                                                    "default": 0,
                                                    "maximum": 10,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "ftmEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "ftmInitBurstDuration": {
                                                    "default": "ENUM_32MS",
                                                    "enum": [
                                                        "ENUM_128MS",
                                                        "ENUM_16MS",
                                                        "ENUM_1MS",
                                                        "ENUM_250US",
                                                        "ENUM_2MS",
                                                        "ENUM_32MS",
                                                        "ENUM_4MS",
                                                        "ENUM_500US",
                                                        "ENUM_64MS",
                                                        "ENUM_8MS",
                                                        "ANY"
                                                    ],
                                                    "type": "string"
                                                },
                                                "ftmInitBurstSize": {
                                                    "default": 8,
                                                    "maximum": 64,
                                                    "minimum": 4,
                                                    "type": "integer"
                                                },
                                                "gasRateLimitEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "gasRateLimitIntervalMsec": {
                                                    "maximum": 10000,
                                                    "minimum": 100,
                                                    "type": "integer"
                                                },
                                                "gasRateLimitNumReqPerInterval": {
                                                    "maximum": 100,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "grpcEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "heartBeatTimeout": {
                                                    "default": 30,
                                                    "maximum": 30,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "hyperlocationEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "icapAdrIndividualThrottle": {
                                                    "default": 5,
                                                    "maximum": 500,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "icapAdrSummaryFrequency": {
                                                    "default": 5,
                                                    "maximum": 60,
                                                    "minimum": 3,
                                                    "type": "integer"
                                                },
                                                "icapAggrTraceEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "icapAnomalyDetDhcpTimeout": {
                                                    "default": 5,
                                                    "maximum": 120,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "icapFullTraceEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "injectorSwitchMacAddr": {
                                                    "default": "00:00:00:00:00:00",
                                                    "type": "string"
                                                },
                                                "isRfSpectrumSlot2Enabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "jumboMtuEnabled": {
                                                    "type": "boolean"
                                                },
                                                "kernelCoredumpLimit": {
                                                    "default": 0,
                                                    "maximum": 5,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "lawfulInterceptionEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "lawfulInterceptionTimerInterval": {
                                                    "default": 60,
                                                    "maximum": 600,
                                                    "minimum": 60,
                                                    "type": "integer"
                                                },
                                                "ledFlashMode": {
                                                    "default": "LED_FLASH_MODE_INDEFINITE",
                                                    "enum": [
                                                        "LED_FLASH_MODE_DISABLE",
                                                        "LED_FLASH_MODE_DURATION",
                                                        "LED_FLASH_MODE_INDEFINITE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "ledStateEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "linkLatencyFlagEnabled": {
                                                    "default": "LINK_AUDITING_DISABLE",
                                                    "enum": [
                                                        "LINK_AUDITING_DATA",
                                                        "LINK_AUDITING_DISABLE",
                                                        "LINK_AUDITING_ENABLE",
                                                        "LINK_AUDITING_RESET"
                                                    ],
                                                    "type": "string"
                                                },
                                                "loginCredentialsDot1xPasswordType": {
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
                                                "lscApAuthTypeInfoAuthType": {
                                                    "default": "LSC_AP_AUTH_CAPWAP_DTLS",
                                                    "enum": [
                                                        "LSC_AP_AUTH_BOTH",
                                                        "LSC_AP_AUTH_CAPWAP_DTLS",
                                                        "LSC_AP_AUTH_DOT1X_PORT_AUTH",
                                                        "LSC_AP_AUTH_NONE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "max1xSessionLimitPerAp": {
                                                    "default": 0,
                                                    "type": "integer"
                                                },
                                                "maxCfgClients": {
                                                    "default": 0,
                                                    "maximum": 1200,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "memThresholdStatsMonitor": {
                                                    "default": 0,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "meshProfileName": {
                                                    "default": "default-mesh-profile",
                                                    "type": "string"
                                                },
                                                "noProxyList": {
                                                    "type": "string"
                                                },
                                                "nsiPortsStateEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "ntpServerInfoKeyFormat": {
                                                    "default": "AP_NTP_KEY_FORMAT_ASCII",
                                                    "enum": [
                                                        "AP_NTP_KEY_FORMAT_ASCII",
                                                        "AP_NTP_KEY_FORMAT_HEX"
                                                    ],
                                                    "type": "string"
                                                },
                                                "ntpServerInfoKeyId": {
                                                    "default": 1,
                                                    "maximum": 65535,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "ntpServerInfoNtpAddr": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "ntpServerTrustKey": {
                                                    "type": "string"
                                                },
                                                "oeapDataEncryptionEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "oeapLocalNet": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "oeapRogueDetectEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "pakRssiThresholdDetection": {
                                                    "default": -100,
                                                    "maximum": -50,
                                                    "minimum": -100,
                                                    "type": "integer"
                                                },
                                                "pakRssiThresholdReset": {
                                                    "default": 8,
                                                    "maximum": 99,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "pakRssiThresholdTrigger": {
                                                    "default": 10,
                                                    "maximum": 100,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "partialTraceEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoAll": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoCiscoAll": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoCiscoNdp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataAll": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataArp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataDhcp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataDhcpv6": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataDns": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataEap": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataIcmp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataIcmpv6": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoMgmtAll": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoMgmtAssoc": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoMgmtAuth": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoMgmtProbe": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "persistentSsidBroadcastEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "pmfDeauthEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "powerInjectorSelection": {
                                                    "default": "PWRINJ_UNKNOWN",
                                                    "enum": [
                                                        "PWRINJ_INSTALLED",
                                                        "PWRINJ_OVERRIDE",
                                                        "PWRINJ_UNKNOWN"
                                                    ],
                                                    "type": "string"
                                                },
                                                "powerInjectorStateEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "preStandard8023afSwitchFlag": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "pressSensConfigState": {
                                                    "default": "PRESS_SENSOR_AUTO",
                                                    "enum": [
                                                        "PRESS_SENSOR_AUTO",
                                                        "PRESS_SENSOR_DISABLED",
                                                        "PRESS_SENSOR_ENABLED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "primaryControllerIpAddr": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "primaryControllerName": {
                                                    "type": "string"
                                                },
                                                "primaryDiscoveryTimeout": {
                                                    "default": 120,
                                                    "maximum": 3000,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "primedJoinTimeout": {
                                                    "default": 0,
                                                    "maximum": 43200,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "privateIpDiscoveryEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "provisionalSsidEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "proxyHostname": {
                                                    "type": "string"
                                                },
                                                "proxyPort": {
                                                    "maximum": 65535,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "publicIpDiscoveryEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "qosmapActionFrameEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "radio24GhzReportingInterval": {
                                                    "default": 90,
                                                    "maximum": 90,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "radio5GhzReportingInterval": {
                                                    "default": 90,
                                                    "maximum": 90,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "radioResetEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "radioStatsMonitorAlarmsEnabled": {
                                                    "type": "boolean"
                                                },
                                                "radioStatsMonitorEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "retransmitTimerCount": {
                                                    "default": 5,
                                                    "maximum": 8,
                                                    "minimum": 3,
                                                    "type": "integer"
                                                },
                                                "retransmitTimerInterval": {
                                                    "default": 3,
                                                    "maximum": 5,
                                                    "minimum": 2,
                                                    "type": "integer"
                                                },
                                                "rfSpectrumEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfSpectrumSlot0Enabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfSpectrumSlot1Enabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfSpectrumSlot3Enabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rogueContainmentAutorate": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rogueContainmentFlexconnect": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rogueDetectionPmfDenial": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rogueDetectionProfileName": {
                                                    "type": "string"
                                                },
                                                "rogueReportInterval": {
                                                    "default": 10,
                                                    "maximum": 300,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "sampleInterval": {
                                                    "default": 720,
                                                    "maximum": 3600,
                                                    "minimum": 720,
                                                    "type": "integer"
                                                },
                                                "sampleIntvl": {
                                                    "default": 30,
                                                    "maximum": 900,
                                                    "minimum": 2,
                                                    "type": "integer"
                                                },
                                                "secondaryControllerIpAddr": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "secondaryControllerName": {
                                                    "type": "string"
                                                },
                                                "serialConsoleEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "sshEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "statsMonitorEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "statsMonitorStatsInterval": {
                                                    "default": 300,
                                                    "maximum": 900,
                                                    "minimum": 120,
                                                    "type": "integer"
                                                },
                                                "syslogFacilityValue": {
                                                    "default": "FACILITY_KERN",
                                                    "enum": [
                                                        "FACILITY_AUTH",
                                                        "FACILITY_CRON",
                                                        "FACILITY_DAEMON",
                                                        "FACILITY_KERN",
                                                        "FACILITY_LOCAL0",
                                                        "FACILITY_LOCAL1",
                                                        "FACILITY_LOCAL2",
                                                        "FACILITY_LOCAL3",
                                                        "FACILITY_LOCAL4",
                                                        "FACILITY_LOCAL5",
                                                        "FACILITY_LOCAL6",
                                                        "FACILITY_LOCAL7",
                                                        "FACILITY_LPR",
                                                        "FACILITY_MAIL",
                                                        "FACILITY_NEWS",
                                                        "FACILITY_SYS10",
                                                        "FACILITY_SYS11",
                                                        "FACILITY_SYS12",
                                                        "FACILITY_SYS13",
                                                        "FACILITY_SYS14",
                                                        "FACILITY_SYS9",
                                                        "FACILITY_SYSLOG",
                                                        "FACILITY_USER",
                                                        "FACILITY_UUCP"
                                                    ],
                                                    "type": "string"
                                                },
                                                "syslogHostIpAddress": {
                                                    "default": "255.255.255.255",
                                                    "type": "string"
                                                },
                                                "syslogLogLevel": {
                                                    "default": "SYSLOG_LEVEL_INFORMATION",
                                                    "enum": [
                                                        "SYSLOG_LEVEL_ALERT",
                                                        "SYSLOG_LEVEL_CRITICAL",
                                                        "SYSLOG_LEVEL_DEBUG",
                                                        "SYSLOG_LEVEL_EMERGENCY",
                                                        "SYSLOG_LEVEL_ERRORS",
                                                        "SYSLOG_LEVEL_INFORMATION",
                                                        "SYSLOG_LEVEL_NOTIFICATION",
                                                        "SYSLOG_LEVEL_WARNING"
                                                    ],
                                                    "type": "string"
                                                },
                                                "syslogTlsModeEnabled": {
                                                    "type": "boolean"
                                                },
                                                "tcpAdjustMss": {
                                                    "default": 1250,
                                                    "maximum": 1363,
                                                    "minimum": 536,
                                                    "type": "integer"
                                                },
                                                "tcpMssAdjustEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "telnetEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "tftpDowngradeFilename": {
                                                    "type": "string"
                                                },
                                                "tftpDowngradeIpAddress": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "tftpServerIpAddress": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "trafficDistributionInterval": {
                                                    "default": 300,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "trafficDistributionStatus": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "trapRetxTime": {
                                                    "default": 0,
                                                    "maximum": 65535,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "trustKeyType": {
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
                                                "tunnelPreferredMode": {
                                                    "default": "PREFERRED_MODE_UNCONFIG",
                                                    "enum": [
                                                        "PREFERRED_MODE_IPV4",
                                                        "PREFERRED_MODE_IPV6",
                                                        "PREFERRED_MODE_UNCONFIG"
                                                    ],
                                                    "type": "string"
                                                },
                                                "tzConfigEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "udpLiteIpv6CapwapChecksumType": {
                                                    "default": "UDPLITE_CHECKSUM_DISABLED",
                                                    "enum": [
                                                        "UDPLITE_CHECKSUM_DISABLED",
                                                        "UDPLITE_CHECKSUM_ENABLED",
                                                        "UDPLITE_CHECKSUM_UNCONFIGURED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "usbModuleEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "userMgmtPassword": {
                                                    "type": "string"
                                                },
                                                "userMgmtPasswordCryptType": {
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
                                                "userMgmtSecret": {
                                                    "type": "string"
                                                },
                                                "userMgmtSecretType": {
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
                                                "userMgmtUsername": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "weakRssi": {
                                                    "default": -60,
                                                    "maximum": -10,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                }
                                            },
                                            "required": [
                                                "apCfgProfileName",
                                                "deviceVersion"
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
                                                "acctMethodList": {
                                                    "type": "string"
                                                },
                                                "actionApReloadEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "adrIndividualAggrEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "adrIndividualEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "adrIndividualPcThrottle": {
                                                    "default": 5,
                                                    "maximum": 50,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "adrIndividualPtThrottle": {
                                                    "default": 5,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "adrSummaryEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "alarmHoldTime": {
                                                    "default": 6,
                                                    "maximum": 3600,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "alarmsEnabled": {
                                                    "type": "boolean"
                                                },
                                                "anomalyDetTriggerTraceAp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "anomalyDetectionEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "antennaMonitorDetectionTime": {
                                                    "default": 12,
                                                    "maximum": 180,
                                                    "minimum": 9,
                                                    "type": "integer"
                                                },
                                                "antennaMonitorEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "antennaMonitorRssiFailThreshold": {
                                                    "default": 40,
                                                    "maximum": 90,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "apCfgProfileDescription": {
                                                    "type": "string"
                                                },
                                                "apCfgProfileLedFlashSec": {
                                                    "default": 0,
                                                    "maximum": 3600,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "apCfgProfileName": {
                                                    "type": "string"
                                                },
                                                "apCfgProfileStatsTimer": {
                                                    "default": 180,
                                                    "maximum": 65535,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "apCountryCountryCode": {
                                                    "default": "UNCONFIGURED",
                                                    "enum": [
                                                        "AD",
                                                        "AE",
                                                        "AF",
                                                        "AG",
                                                        "AI",
                                                        "AL",
                                                        "AM",
                                                        "AO",
                                                        "AQ",
                                                        "AR",
                                                        "AS",
                                                        "AT",
                                                        "AU",
                                                        "AW",
                                                        "AX",
                                                        "AZ",
                                                        "BA",
                                                        "BB",
                                                        "BD",
                                                        "BE",
                                                        "BF",
                                                        "BG",
                                                        "BH",
                                                        "BI",
                                                        "BJ",
                                                        "BL",
                                                        "BM",
                                                        "BN",
                                                        "BO",
                                                        "BQ",
                                                        "BR",
                                                        "BS",
                                                        "BT",
                                                        "BV",
                                                        "BW",
                                                        "BY",
                                                        "BZ",
                                                        "CA",
                                                        "CC",
                                                        "CD",
                                                        "CF",
                                                        "CG",
                                                        "CH",
                                                        "CI",
                                                        "CK",
                                                        "CL",
                                                        "CM",
                                                        "CN",
                                                        "CO",
                                                        "CR",
                                                        "CU",
                                                        "CV",
                                                        "CW",
                                                        "CX",
                                                        "CY",
                                                        "CZ",
                                                        "DE",
                                                        "DJ",
                                                        "DK",
                                                        "DM",
                                                        "DO",
                                                        "DZ",
                                                        "EC",
                                                        "EE",
                                                        "EG",
                                                        "EH",
                                                        "EL",
                                                        "ER",
                                                        "ES",
                                                        "ET",
                                                        "FI",
                                                        "FJ",
                                                        "FK",
                                                        "FM",
                                                        "FO",
                                                        "FR",
                                                        "GA",
                                                        "GB",
                                                        "GD",
                                                        "GE",
                                                        "GF",
                                                        "GG",
                                                        "GH",
                                                        "GI",
                                                        "GL",
                                                        "GM",
                                                        "GN",
                                                        "GP",
                                                        "GQ",
                                                        "GR",
                                                        "GS",
                                                        "GT",
                                                        "GU",
                                                        "GW",
                                                        "GY",
                                                        "HK",
                                                        "HM",
                                                        "HN",
                                                        "HR",
                                                        "HT",
                                                        "HU",
                                                        "ID",
                                                        "IE",
                                                        "IL",
                                                        "IM",
                                                        "IN",
                                                        "IO",
                                                        "IQ",
                                                        "IR",
                                                        "IS",
                                                        "IT",
                                                        "J2",
                                                        "J3",
                                                        "J4",
                                                        "JE",
                                                        "JM",
                                                        "JO",
                                                        "JP",
                                                        "KE",
                                                        "KG",
                                                        "KH",
                                                        "KI",
                                                        "KM",
                                                        "KN",
                                                        "KP",
                                                        "KR",
                                                        "KW",
                                                        "KY",
                                                        "KZ",
                                                        "LA",
                                                        "LB",
                                                        "LC",
                                                        "LI",
                                                        "LK",
                                                        "LR",
                                                        "LS",
                                                        "LT",
                                                        "LU",
                                                        "LV",
                                                        "LY",
                                                        "MA",
                                                        "MC",
                                                        "MD",
                                                        "ME",
                                                        "MF",
                                                        "MG",
                                                        "MH",
                                                        "MK",
                                                        "ML",
                                                        "MM",
                                                        "MN",
                                                        "MO",
                                                        "MP",
                                                        "MQ",
                                                        "MR",
                                                        "MS",
                                                        "MT",
                                                        "MU",
                                                        "MV",
                                                        "MW",
                                                        "MX",
                                                        "MY",
                                                        "MZ",
                                                        "NA",
                                                        "NC",
                                                        "NE",
                                                        "NF",
                                                        "NG",
                                                        "NI",
                                                        "NL",
                                                        false,
                                                        "NP",
                                                        "NR",
                                                        "NU",
                                                        "NZ",
                                                        "OM",
                                                        "PA",
                                                        "PE",
                                                        "PF",
                                                        "PG",
                                                        "PH",
                                                        "PK",
                                                        "PL",
                                                        "PM",
                                                        "PN",
                                                        "PR",
                                                        "PS",
                                                        "PT",
                                                        "PW",
                                                        "PY",
                                                        "QA",
                                                        "RE",
                                                        "RO",
                                                        "RS",
                                                        "RU",
                                                        "RW",
                                                        "SA",
                                                        "SB",
                                                        "SC",
                                                        "SD",
                                                        "SE",
                                                        "SG",
                                                        "SH",
                                                        "SI",
                                                        "SJ",
                                                        "SK",
                                                        "SL",
                                                        "SM",
                                                        "SN",
                                                        "SO",
                                                        "SR",
                                                        "SS",
                                                        "ST",
                                                        "SV",
                                                        "SX",
                                                        "SY",
                                                        "SZ",
                                                        "TC",
                                                        "TD",
                                                        "TF",
                                                        "TG",
                                                        "TH",
                                                        "TI",
                                                        "TJ",
                                                        "TK",
                                                        "TL",
                                                        "TM",
                                                        "TN",
                                                        "TO",
                                                        "TR",
                                                        "TT",
                                                        "TV",
                                                        "TW",
                                                        "TZ",
                                                        "UA",
                                                        "UG",
                                                        "UM",
                                                        "UNCONFIGURED",
                                                        "US",
                                                        "UY",
                                                        "UZ",
                                                        "VA",
                                                        "VC",
                                                        "VE",
                                                        "VG",
                                                        "VI",
                                                        "VN",
                                                        "VU",
                                                        "WF",
                                                        "WS",
                                                        "XK",
                                                        "YE",
                                                        "YT",
                                                        "ZA",
                                                        "ZM",
                                                        "ZW"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apDeploymentModeType": {
                                                    "default": "AP_MODE_DEFAULT",
                                                    "enum": [
                                                        "AP_MODE_DEFAULT",
                                                        "AP_MODE_INDOOR",
                                                        "AP_MODE_OUTDOOR"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apDtlsCtrlPrefEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "apLagEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apNtpServerInfoKeyType": {
                                                    "default": "AP_NTP_KEY_TYPE_MD5",
                                                    "enum": [
                                                        "AP_NTP_KEY_TYPE_MD5",
                                                        "AP_NTP_KEY_TYPE_SHA1"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apPacketCaptureProfile": {
                                                    "type": "string"
                                                },
                                                "apProfPpCfgPowerProfileName": {
                                                    "maxLength": 128,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "apRogueDetectionEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "apRogueDetectionMinRssi": {
                                                    "default": -90,
                                                    "maximum": -70,
                                                    "minimum": -128,
                                                    "type": "integer"
                                                },
                                                "apRogueDetectionTransientInterval": {
                                                    "default": 0,
                                                    "type": "integer"
                                                },
                                                "apStatsDnsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsDnsFreq": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsInterfaceEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsInterfaceFreq": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsMemoryEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsMemoryFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsRadioEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsRadioFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsRoutingEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsRoutingFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsSysEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsSystemFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsWlanEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsWlanFreq": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apSubModeType": {
                                                    "enum": [
                                                        "AP_SUB_MODE_NONE",
                                                        "FORENSIC_AWIPS_MODE",
                                                        "LOCAL_NETWORK",
                                                        "NON_LOCAL_NETWORK",
                                                        "WIPS_MODE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apTraceProfile": {
                                                    "type": "string"
                                                },
                                                "apTrustsUpstreamDscpEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "apTzConfigMode": {
                                                    "default": "AP_TZ_NOT_CONFIGURED",
                                                    "enum": [
                                                        "AP_TZ_CONTROLLER_TZ",
                                                        "AP_TZ_NOT_CONFIGURED",
                                                        "AP_TZ_UTC_OFFSET"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apTzConfigOffsetHour": {
                                                    "default": 0,
                                                    "maximum": 14,
                                                    "minimum": -12,
                                                    "type": "integer"
                                                },
                                                "apTzConfigOffsetMin": {
                                                    "default": 0,
                                                    "maximum": 59,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "apphostEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "auxClientInterfaceVlanId": {
                                                    "default": 0,
                                                    "maximum": 4094,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "awipsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "awipsForensicEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "bleBeaconAdvpwr": {
                                                    "default": 59,
                                                    "maximum": 100,
                                                    "minimum": 40,
                                                    "type": "integer"
                                                },
                                                "bleBeaconInterval": {
                                                    "default": 1,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "bleScanStateEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "bssidEnableStats": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "bssidNeighborStatsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "bssidNeighborStatsFrequency": {
                                                    "default": 180,
                                                    "maximum": 600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "bssidStatsFrequency": {
                                                    "default": 30,
                                                    "maximum": 180,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "capwapWindowWindowSize": {
                                                    "default": 1,
                                                    "maximum": 50,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "cdpEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "clientFilterStatsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "clientFilterStatsFrequency": {
                                                    "default": 5,
                                                    "maximum": 3600,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "clientRssiStatsEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "clientRssiStatsInterval": {
                                                    "default": 30,
                                                    "maximum": 300,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "clientStatsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "clientStatsFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "configType": {
                                                    "default": "AP_JOIN_PROFILE",
                                                    "enum": [
                                                        "AP_JOIN_PROFILE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "coredumpFlagEnabled": {
                                                    "default": "TFTP_COREDUMP_DISABLE",
                                                    "enum": [
                                                        "TFTP_COREDUMP_COMPRESS",
                                                        "TFTP_COREDUMP_DISABLE",
                                                        "TFTP_COREDUMP_UNCOMPRESS"
                                                    ],
                                                    "type": "string"
                                                },
                                                "corefileName": {
                                                    "default": "default",
                                                    "type": "string"
                                                },
                                                "cpuThreshold": {
                                                    "default": 0,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "dataEncryptionEnabled": {
                                                    "type": "boolean"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.14",
                                                    "type": "string"
                                                },
                                                "dhcpFallbackEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "dhcpServerEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "discoveryTimeout": {
                                                    "default": 10,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "dot1xEapTypeInfoDot1xEapType": {
                                                    "default": "DOT1X_EAP_FAST",
                                                    "enum": [
                                                        "DOT1X_EAP_FAST",
                                                        "DOT1X_EAP_NONE",
                                                        "DOT1X_EAP_PEAP",
                                                        "DOT1X_EAP_TLS"
                                                    ],
                                                    "type": "string"
                                                },
                                                "dot1xPassword": {
                                                    "type": "string"
                                                },
                                                "dot1xUsername": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "extModuleEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "fallbackEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "fastChannel": {
                                                    "maximum": 4294967295,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "fastHeartBeatTimeout": {
                                                    "default": 0,
                                                    "maximum": 10,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "ftmEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "ftmInitBurstDuration": {
                                                    "default": "ENUM_32MS",
                                                    "enum": [
                                                        "ENUM_128MS",
                                                        "ENUM_16MS",
                                                        "ENUM_1MS",
                                                        "ENUM_250US",
                                                        "ENUM_2MS",
                                                        "ENUM_32MS",
                                                        "ENUM_4MS",
                                                        "ENUM_500US",
                                                        "ENUM_64MS",
                                                        "ENUM_8MS",
                                                        "ANY"
                                                    ],
                                                    "type": "string"
                                                },
                                                "ftmInitBurstSize": {
                                                    "default": 8,
                                                    "maximum": 64,
                                                    "minimum": 4,
                                                    "type": "integer"
                                                },
                                                "gasRateLimitEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "gasRateLimitIntervalMsec": {
                                                    "maximum": 10000,
                                                    "minimum": 100,
                                                    "type": "integer"
                                                },
                                                "gasRateLimitNumReqPerInterval": {
                                                    "maximum": 100,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "grpcEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "heartBeatTimeout": {
                                                    "default": 30,
                                                    "maximum": 30,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "hyperlocationEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "icapAdrIndividualThrottle": {
                                                    "default": 5,
                                                    "maximum": 500,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "icapAdrSummaryFrequency": {
                                                    "default": 5,
                                                    "maximum": 60,
                                                    "minimum": 3,
                                                    "type": "integer"
                                                },
                                                "icapAggrTraceEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "icapAnomalyDetDhcpTimeout": {
                                                    "default": 5,
                                                    "maximum": 120,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "icapFullTraceEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "injectorSwitchMacAddr": {
                                                    "default": "00:00:00:00:00:00",
                                                    "type": "string"
                                                },
                                                "isRfSpectrumSlot2Enabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "jumboMtuEnabled": {
                                                    "type": "boolean"
                                                },
                                                "kernelCoredumpLimit": {
                                                    "default": 0,
                                                    "maximum": 5,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "lawfulInterceptionEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "lawfulInterceptionTimerInterval": {
                                                    "default": 60,
                                                    "maximum": 600,
                                                    "minimum": 60,
                                                    "type": "integer"
                                                },
                                                "ledFlashMode": {
                                                    "default": "LED_FLASH_MODE_INDEFINITE",
                                                    "enum": [
                                                        "LED_FLASH_MODE_DISABLE",
                                                        "LED_FLASH_MODE_DURATION",
                                                        "LED_FLASH_MODE_INDEFINITE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "ledStateEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "linkLatencyFlagEnabled": {
                                                    "default": "LINK_AUDITING_DISABLE",
                                                    "enum": [
                                                        "LINK_AUDITING_DATA",
                                                        "LINK_AUDITING_DISABLE",
                                                        "LINK_AUDITING_ENABLE",
                                                        "LINK_AUDITING_RESET"
                                                    ],
                                                    "type": "string"
                                                },
                                                "loginCredentialsDot1xPasswordType": {
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
                                                "lscApAuthTypeInfoAuthType": {
                                                    "default": "LSC_AP_AUTH_CAPWAP_DTLS",
                                                    "enum": [
                                                        "LSC_AP_AUTH_BOTH",
                                                        "LSC_AP_AUTH_CAPWAP_DTLS",
                                                        "LSC_AP_AUTH_DOT1X_PORT_AUTH",
                                                        "LSC_AP_AUTH_NONE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "max1xSessionLimitPerAp": {
                                                    "default": 0,
                                                    "type": "integer"
                                                },
                                                "maxCfgClients": {
                                                    "default": 0,
                                                    "maximum": 1200,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "memThresholdStatsMonitor": {
                                                    "default": 0,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "meshProfileName": {
                                                    "default": "default-mesh-profile",
                                                    "type": "string"
                                                },
                                                "noProxyList": {
                                                    "type": "string"
                                                },
                                                "nsiPortsStateEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "ntpServerInfoKeyFormat": {
                                                    "default": "AP_NTP_KEY_FORMAT_ASCII",
                                                    "enum": [
                                                        "AP_NTP_KEY_FORMAT_ASCII",
                                                        "AP_NTP_KEY_FORMAT_HEX"
                                                    ],
                                                    "type": "string"
                                                },
                                                "ntpServerInfoKeyId": {
                                                    "default": 1,
                                                    "maximum": 65535,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "ntpServerInfoNtpAddr": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "ntpServerTrustKey": {
                                                    "type": "string"
                                                },
                                                "oeapDataEncryptionEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "oeapLocalNet": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "oeapRogueDetectEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "pakRssiThresholdDetection": {
                                                    "default": -100,
                                                    "maximum": -50,
                                                    "minimum": -100,
                                                    "type": "integer"
                                                },
                                                "pakRssiThresholdReset": {
                                                    "default": 8,
                                                    "maximum": 99,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "pakRssiThresholdTrigger": {
                                                    "default": 10,
                                                    "maximum": 100,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "partialTraceEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoAll": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoCiscoAll": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoCiscoNdp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataAll": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataArp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataDhcp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataDhcpv6": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataDns": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataEap": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataIcmp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataIcmpv6": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoMgmtAll": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoMgmtAssoc": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoMgmtAuth": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoMgmtProbe": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "persistentSsidBroadcastEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "pmfDeauthEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "powerInjectorSelection": {
                                                    "default": "PWRINJ_UNKNOWN",
                                                    "enum": [
                                                        "PWRINJ_INSTALLED",
                                                        "PWRINJ_OVERRIDE",
                                                        "PWRINJ_UNKNOWN"
                                                    ],
                                                    "type": "string"
                                                },
                                                "powerInjectorStateEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "preStandard8023afSwitchFlag": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "pressSensConfigState": {
                                                    "default": "PRESS_SENSOR_AUTO",
                                                    "enum": [
                                                        "PRESS_SENSOR_AUTO",
                                                        "PRESS_SENSOR_DISABLED",
                                                        "PRESS_SENSOR_ENABLED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "primaryControllerIpAddr": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "primaryControllerName": {
                                                    "type": "string"
                                                },
                                                "primaryDiscoveryTimeout": {
                                                    "default": 120,
                                                    "maximum": 3000,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "primedJoinTimeout": {
                                                    "default": 0,
                                                    "maximum": 43200,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "privateIpDiscoveryEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "provisionalSsidEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "proxyHostname": {
                                                    "type": "string"
                                                },
                                                "proxyPort": {
                                                    "maximum": 65535,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "publicIpDiscoveryEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "qosmapActionFrameEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "radio24GhzReportingInterval": {
                                                    "default": 90,
                                                    "maximum": 90,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "radio5GhzReportingInterval": {
                                                    "default": 90,
                                                    "maximum": 90,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "radioResetEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "radioStatsMonitorAlarmsEnabled": {
                                                    "type": "boolean"
                                                },
                                                "radioStatsMonitorEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "retransmitTimerCount": {
                                                    "default": 5,
                                                    "maximum": 8,
                                                    "minimum": 3,
                                                    "type": "integer"
                                                },
                                                "retransmitTimerInterval": {
                                                    "default": 3,
                                                    "maximum": 5,
                                                    "minimum": 2,
                                                    "type": "integer"
                                                },
                                                "rfSpectrumEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfSpectrumSlot0Enabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfSpectrumSlot1Enabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfSpectrumSlot3Enabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rogueContainmentAutorate": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rogueContainmentFlexconnect": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rogueDetectionPmfDenial": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rogueDetectionProfileName": {
                                                    "type": "string"
                                                },
                                                "rogueReportInterval": {
                                                    "default": 10,
                                                    "maximum": 300,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "sampleInterval": {
                                                    "default": 720,
                                                    "maximum": 3600,
                                                    "minimum": 720,
                                                    "type": "integer"
                                                },
                                                "sampleIntvl": {
                                                    "default": 30,
                                                    "maximum": 900,
                                                    "minimum": 2,
                                                    "type": "integer"
                                                },
                                                "secondaryControllerIpAddr": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "secondaryControllerName": {
                                                    "type": "string"
                                                },
                                                "serialConsoleEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "sshEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "statsMonitorEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "statsMonitorStatsInterval": {
                                                    "default": 300,
                                                    "maximum": 900,
                                                    "minimum": 120,
                                                    "type": "integer"
                                                },
                                                "syslogFacilityValue": {
                                                    "default": "FACILITY_KERN",
                                                    "enum": [
                                                        "FACILITY_AUTH",
                                                        "FACILITY_CRON",
                                                        "FACILITY_DAEMON",
                                                        "FACILITY_KERN",
                                                        "FACILITY_LOCAL0",
                                                        "FACILITY_LOCAL1",
                                                        "FACILITY_LOCAL2",
                                                        "FACILITY_LOCAL3",
                                                        "FACILITY_LOCAL4",
                                                        "FACILITY_LOCAL5",
                                                        "FACILITY_LOCAL6",
                                                        "FACILITY_LOCAL7",
                                                        "FACILITY_LPR",
                                                        "FACILITY_MAIL",
                                                        "FACILITY_NEWS",
                                                        "FACILITY_SYS10",
                                                        "FACILITY_SYS11",
                                                        "FACILITY_SYS12",
                                                        "FACILITY_SYS13",
                                                        "FACILITY_SYS14",
                                                        "FACILITY_SYS9",
                                                        "FACILITY_SYSLOG",
                                                        "FACILITY_USER",
                                                        "FACILITY_UUCP"
                                                    ],
                                                    "type": "string"
                                                },
                                                "syslogHostIpAddress": {
                                                    "default": "255.255.255.255",
                                                    "type": "string"
                                                },
                                                "syslogLogLevel": {
                                                    "default": "SYSLOG_LEVEL_INFORMATION",
                                                    "enum": [
                                                        "SYSLOG_LEVEL_ALERT",
                                                        "SYSLOG_LEVEL_CRITICAL",
                                                        "SYSLOG_LEVEL_DEBUG",
                                                        "SYSLOG_LEVEL_EMERGENCY",
                                                        "SYSLOG_LEVEL_ERRORS",
                                                        "SYSLOG_LEVEL_INFORMATION",
                                                        "SYSLOG_LEVEL_NOTIFICATION",
                                                        "SYSLOG_LEVEL_WARNING"
                                                    ],
                                                    "type": "string"
                                                },
                                                "syslogTlsModeEnabled": {
                                                    "type": "boolean"
                                                },
                                                "tcpAdjustMss": {
                                                    "default": 1250,
                                                    "maximum": 1363,
                                                    "minimum": 536,
                                                    "type": "integer"
                                                },
                                                "tcpMssAdjustEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "telnetEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "tftpDowngradeFilename": {
                                                    "type": "string"
                                                },
                                                "tftpDowngradeIpAddress": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "tftpServerIpAddress": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "trafficDistributionInterval": {
                                                    "default": 300,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "trafficDistributionStatus": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "trapRetxTime": {
                                                    "default": 0,
                                                    "maximum": 65535,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "trustKeyType": {
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
                                                "tunnelPreferredMode": {
                                                    "default": "PREFERRED_MODE_UNCONFIG",
                                                    "enum": [
                                                        "PREFERRED_MODE_IPV4",
                                                        "PREFERRED_MODE_IPV6",
                                                        "PREFERRED_MODE_UNCONFIG"
                                                    ],
                                                    "type": "string"
                                                },
                                                "tzConfigEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "udpLiteIpv6CapwapChecksumType": {
                                                    "default": "UDPLITE_CHECKSUM_DISABLED",
                                                    "enum": [
                                                        "UDPLITE_CHECKSUM_DISABLED",
                                                        "UDPLITE_CHECKSUM_ENABLED",
                                                        "UDPLITE_CHECKSUM_UNCONFIGURED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "usbModuleEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "userMgmtPassword": {
                                                    "type": "string"
                                                },
                                                "userMgmtPasswordCryptType": {
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
                                                "userMgmtSecret": {
                                                    "type": "string"
                                                },
                                                "userMgmtSecretType": {
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
                                                "userMgmtUsername": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "weakRssi": {
                                                    "default": -60,
                                                    "maximum": -10,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                }
                                            },
                                            "required": [
                                                "apCfgProfileName",
                                                "deviceVersion"
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
                                                "accelerometerSensorEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "acctMethodList": {
                                                    "type": "string"
                                                },
                                                "actionApReloadEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "adrIndividualAggrEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "adrIndividualEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "adrIndividualPcThrottle": {
                                                    "default": 5,
                                                    "maximum": 50,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "adrIndividualPtThrottle": {
                                                    "default": 5,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "adrSummaryEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "alarmHoldTime": {
                                                    "default": 6,
                                                    "maximum": 3600,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "alarmsEnabled": {
                                                    "type": "boolean"
                                                },
                                                "anomalyDetTriggerTraceAp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "anomalyDetectionEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "antennaMonitorDetectionTime": {
                                                    "default": 12,
                                                    "maximum": 180,
                                                    "minimum": 9,
                                                    "type": "integer"
                                                },
                                                "antennaMonitorEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "antennaMonitorRssiFailThreshold": {
                                                    "default": 40,
                                                    "maximum": 90,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "apCfgProfileDescription": {
                                                    "type": "string"
                                                },
                                                "apCfgProfileLedFlashSec": {
                                                    "default": 0,
                                                    "maximum": 3600,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "apCfgProfileName": {
                                                    "type": "string"
                                                },
                                                "apCfgProfileStatsTimer": {
                                                    "default": 180,
                                                    "maximum": 65535,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "apCountryCountryCode": {
                                                    "default": "UNCONFIGURED",
                                                    "enum": [
                                                        "AD",
                                                        "AE",
                                                        "AF",
                                                        "AG",
                                                        "AI",
                                                        "AL",
                                                        "AM",
                                                        "AO",
                                                        "AQ",
                                                        "AR",
                                                        "AS",
                                                        "AT",
                                                        "AU",
                                                        "AW",
                                                        "AX",
                                                        "AZ",
                                                        "BA",
                                                        "BB",
                                                        "BD",
                                                        "BE",
                                                        "BF",
                                                        "BG",
                                                        "BH",
                                                        "BI",
                                                        "BJ",
                                                        "BL",
                                                        "BM",
                                                        "BN",
                                                        "BO",
                                                        "BQ",
                                                        "BR",
                                                        "BS",
                                                        "BT",
                                                        "BV",
                                                        "BW",
                                                        "BY",
                                                        "BZ",
                                                        "CA",
                                                        "CC",
                                                        "CD",
                                                        "CF",
                                                        "CG",
                                                        "CH",
                                                        "CI",
                                                        "CK",
                                                        "CL",
                                                        "CM",
                                                        "CN",
                                                        "CO",
                                                        "CR",
                                                        "CU",
                                                        "CV",
                                                        "CW",
                                                        "CX",
                                                        "CY",
                                                        "CZ",
                                                        "DE",
                                                        "DJ",
                                                        "DK",
                                                        "DM",
                                                        "DO",
                                                        "DZ",
                                                        "EC",
                                                        "EE",
                                                        "EG",
                                                        "EH",
                                                        "EL",
                                                        "ER",
                                                        "ES",
                                                        "ET",
                                                        "FI",
                                                        "FJ",
                                                        "FK",
                                                        "FM",
                                                        "FO",
                                                        "FR",
                                                        "GA",
                                                        "GB",
                                                        "GD",
                                                        "GE",
                                                        "GF",
                                                        "GG",
                                                        "GH",
                                                        "GI",
                                                        "GL",
                                                        "GM",
                                                        "GN",
                                                        "GP",
                                                        "GQ",
                                                        "GR",
                                                        "GS",
                                                        "GT",
                                                        "GU",
                                                        "GW",
                                                        "GY",
                                                        "HK",
                                                        "HM",
                                                        "HN",
                                                        "HR",
                                                        "HT",
                                                        "HU",
                                                        "ID",
                                                        "IE",
                                                        "IL",
                                                        "IM",
                                                        "IN",
                                                        "IO",
                                                        "IQ",
                                                        "IR",
                                                        "IS",
                                                        "IT",
                                                        "J2",
                                                        "J3",
                                                        "J4",
                                                        "JE",
                                                        "JM",
                                                        "JO",
                                                        "JP",
                                                        "KE",
                                                        "KG",
                                                        "KH",
                                                        "KI",
                                                        "KM",
                                                        "KN",
                                                        "KP",
                                                        "KR",
                                                        "KW",
                                                        "KY",
                                                        "KZ",
                                                        "LA",
                                                        "LB",
                                                        "LC",
                                                        "LI",
                                                        "LK",
                                                        "LR",
                                                        "LS",
                                                        "LT",
                                                        "LU",
                                                        "LV",
                                                        "LY",
                                                        "MA",
                                                        "MC",
                                                        "MD",
                                                        "ME",
                                                        "MF",
                                                        "MG",
                                                        "MH",
                                                        "MK",
                                                        "ML",
                                                        "MM",
                                                        "MN",
                                                        "MO",
                                                        "MP",
                                                        "MQ",
                                                        "MR",
                                                        "MS",
                                                        "MT",
                                                        "MU",
                                                        "MV",
                                                        "MW",
                                                        "MX",
                                                        "MY",
                                                        "MZ",
                                                        "NA",
                                                        "NC",
                                                        "NE",
                                                        "NF",
                                                        "NG",
                                                        "NI",
                                                        "NL",
                                                        false,
                                                        "NP",
                                                        "NR",
                                                        "NU",
                                                        "NZ",
                                                        "OM",
                                                        "PA",
                                                        "PE",
                                                        "PF",
                                                        "PG",
                                                        "PH",
                                                        "PK",
                                                        "PL",
                                                        "PM",
                                                        "PN",
                                                        "PR",
                                                        "PS",
                                                        "PT",
                                                        "PW",
                                                        "PY",
                                                        "QA",
                                                        "RE",
                                                        "RO",
                                                        "RS",
                                                        "RU",
                                                        "RW",
                                                        "SA",
                                                        "SB",
                                                        "SC",
                                                        "SD",
                                                        "SE",
                                                        "SG",
                                                        "SH",
                                                        "SI",
                                                        "SJ",
                                                        "SK",
                                                        "SL",
                                                        "SM",
                                                        "SN",
                                                        "SO",
                                                        "SR",
                                                        "SS",
                                                        "ST",
                                                        "SV",
                                                        "SX",
                                                        "SY",
                                                        "SZ",
                                                        "TC",
                                                        "TD",
                                                        "TF",
                                                        "TG",
                                                        "TH",
                                                        "TI",
                                                        "TJ",
                                                        "TK",
                                                        "TL",
                                                        "TM",
                                                        "TN",
                                                        "TO",
                                                        "TR",
                                                        "TT",
                                                        "TV",
                                                        "TW",
                                                        "TZ",
                                                        "UA",
                                                        "UG",
                                                        "UM",
                                                        "UNCONFIGURED",
                                                        "US",
                                                        "UY",
                                                        "UZ",
                                                        "VA",
                                                        "VC",
                                                        "VE",
                                                        "VG",
                                                        "VI",
                                                        "VN",
                                                        "VU",
                                                        "WF",
                                                        "WS",
                                                        "XK",
                                                        "YE",
                                                        "YT",
                                                        "ZA",
                                                        "ZM",
                                                        "ZW"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apDeploymentModeType": {
                                                    "default": "AP_MODE_DEFAULT",
                                                    "enum": [
                                                        "AP_MODE_DEFAULT",
                                                        "AP_MODE_INDOOR",
                                                        "AP_MODE_OUTDOOR"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apDtlsCtrlPrefEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "apLagEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apNtpServerInfoKeyType": {
                                                    "default": "AP_NTP_KEY_TYPE_MD5",
                                                    "enum": [
                                                        "AP_NTP_KEY_TYPE_MD5",
                                                        "AP_NTP_KEY_TYPE_SHA1"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apPacketCaptureProfile": {
                                                    "type": "string"
                                                },
                                                "apProfPpCfgPowerProfileName": {
                                                    "maxLength": 128,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "apRogueDetectionEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "apRogueDetectionMinRssi": {
                                                    "default": -90,
                                                    "maximum": -70,
                                                    "minimum": -128,
                                                    "type": "integer"
                                                },
                                                "apRogueDetectionTransientInterval": {
                                                    "default": 0,
                                                    "type": "integer"
                                                },
                                                "apStatsDnsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsDnsFreq": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsInterfaceEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsInterfaceFreq": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsMemoryEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsMemoryFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsRadioEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsRadioFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsRoutingEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsRoutingFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsSysEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsSystemFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsWlanEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsWlanFreq": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apSubModeType": {
                                                    "enum": [
                                                        "AP_SUB_MODE_NONE",
                                                        "FORENSIC_AWIPS_MODE",
                                                        "LOCAL_NETWORK",
                                                        "NON_LOCAL_NETWORK",
                                                        "WIPS_MODE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apTraceProfile": {
                                                    "type": "string"
                                                },
                                                "apTrustsUpstreamDscpEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "apTzConfigMode": {
                                                    "default": "AP_TZ_NOT_CONFIGURED",
                                                    "enum": [
                                                        "AP_TZ_CONTROLLER_TZ",
                                                        "AP_TZ_NOT_CONFIGURED",
                                                        "AP_TZ_UTC_OFFSET"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apTzConfigOffsetHour": {
                                                    "default": 0,
                                                    "maximum": 14,
                                                    "minimum": -12,
                                                    "type": "integer"
                                                },
                                                "apTzConfigOffsetMin": {
                                                    "default": 0,
                                                    "maximum": 59,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "apphostEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "auxClientInterfaceVlanId": {
                                                    "default": 0,
                                                    "maximum": 4094,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "awipsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "awipsForensicEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "bleBeaconAdvpwr": {
                                                    "default": 59,
                                                    "maximum": 100,
                                                    "minimum": 40,
                                                    "type": "integer"
                                                },
                                                "bleBeaconInterval": {
                                                    "default": 1,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "bleScanStateEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "bssidEnableStats": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "bssidNeighborStatsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "bssidNeighborStatsFrequency": {
                                                    "default": 180,
                                                    "maximum": 600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "bssidStatsFrequency": {
                                                    "default": 30,
                                                    "maximum": 180,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "capwapAggregationEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "capwapWindowWindowSize": {
                                                    "default": 1,
                                                    "maximum": 50,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "cdpEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "clientFilterStatsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "clientFilterStatsFrequency": {
                                                    "default": 5,
                                                    "maximum": 3600,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "clientRssiStatsEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "clientRssiStatsInterval": {
                                                    "default": 30,
                                                    "maximum": 300,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "clientStatsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "clientStatsFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "configType": {
                                                    "default": "AP_JOIN_PROFILE",
                                                    "enum": [
                                                        "AP_JOIN_PROFILE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "coredumpFlagEnabled": {
                                                    "default": "TFTP_COREDUMP_DISABLE",
                                                    "enum": [
                                                        "TFTP_COREDUMP_COMPRESS",
                                                        "TFTP_COREDUMP_DISABLE",
                                                        "TFTP_COREDUMP_UNCOMPRESS"
                                                    ],
                                                    "type": "string"
                                                },
                                                "corefileName": {
                                                    "default": "default",
                                                    "type": "string"
                                                },
                                                "cpuThreshold": {
                                                    "default": 0,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "dataEncryptionEnabled": {
                                                    "type": "boolean"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.15",
                                                    "type": "string"
                                                },
                                                "dhcpFallbackEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "dhcpServerEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "discoveryTimeout": {
                                                    "default": 10,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "dot1xEapTypeInfoDot1xEapType": {
                                                    "default": "DOT1X_EAP_FAST",
                                                    "enum": [
                                                        "DOT1X_EAP_FAST",
                                                        "DOT1X_EAP_NONE",
                                                        "DOT1X_EAP_PEAP",
                                                        "DOT1X_EAP_TLS"
                                                    ],
                                                    "type": "string"
                                                },
                                                "dot1xPassword": {
                                                    "type": "string"
                                                },
                                                "dot1xUsername": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "extModuleEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "fallbackEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "fastChannel": {
                                                    "maximum": 4294967295,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "fastHeartBeatTimeout": {
                                                    "default": 0,
                                                    "maximum": 10,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "ftmEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "ftmInitBurstDuration": {
                                                    "default": "ENUM_32MS",
                                                    "enum": [
                                                        "ENUM_128MS",
                                                        "ENUM_16MS",
                                                        "ENUM_1MS",
                                                        "ENUM_250US",
                                                        "ENUM_2MS",
                                                        "ENUM_32MS",
                                                        "ENUM_4MS",
                                                        "ENUM_500US",
                                                        "ENUM_64MS",
                                                        "ENUM_8MS",
                                                        "ANY"
                                                    ],
                                                    "type": "string"
                                                },
                                                "ftmInitBurstSize": {
                                                    "default": 16,
                                                    "maximum": 31,
                                                    "minimum": 2,
                                                    "type": "integer"
                                                },
                                                "gasRateLimitEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "gasRateLimitIntervalMsec": {
                                                    "maximum": 10000,
                                                    "minimum": 100,
                                                    "type": "integer"
                                                },
                                                "gasRateLimitNumReqPerInterval": {
                                                    "maximum": 100,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "grpcEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "heartBeatTimeout": {
                                                    "default": 30,
                                                    "maximum": 30,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "hyperlocationEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "icapAdrIndividualThrottle": {
                                                    "default": 5,
                                                    "maximum": 500,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "icapAdrSummaryFrequency": {
                                                    "default": 5,
                                                    "maximum": 60,
                                                    "minimum": 3,
                                                    "type": "integer"
                                                },
                                                "icapAggrTraceEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "icapAnomalyDetDhcpTimeout": {
                                                    "default": 5,
                                                    "maximum": 120,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "icapFullTraceEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "injectorSwitchMacAddr": {
                                                    "default": "00:00:00:00:00:00",
                                                    "type": "string"
                                                },
                                                "isRfSpectrumSlot2Enabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "jumboMtuEnabled": {
                                                    "type": "boolean"
                                                },
                                                "kernelCoredumpLimit": {
                                                    "default": 5,
                                                    "maximum": 5,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "kernelCoredumpType": {
                                                    "default": "KERNEL_COREDUMP_TYPE_DISABLED",
                                                    "enum": [
                                                        "KERNEL_COREDUMP_TYPE_DISABLED",
                                                        "KERNEL_COREDUMP_TYPE_FULL",
                                                        "KERNEL_COREDUMP_TYPE_MINI"
                                                    ],
                                                    "type": "string"
                                                },
                                                "lawfulInterceptionEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "lawfulInterceptionTimerInterval": {
                                                    "default": 60,
                                                    "maximum": 600,
                                                    "minimum": 60,
                                                    "type": "integer"
                                                },
                                                "ledFlashMode": {
                                                    "default": "LED_FLASH_MODE_INDEFINITE",
                                                    "enum": [
                                                        "LED_FLASH_MODE_DISABLE",
                                                        "LED_FLASH_MODE_DURATION",
                                                        "LED_FLASH_MODE_INDEFINITE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "ledStateEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "linkLatencyFlagEnabled": {
                                                    "default": "LINK_AUDITING_DISABLE",
                                                    "enum": [
                                                        "LINK_AUDITING_DATA",
                                                        "LINK_AUDITING_DISABLE",
                                                        "LINK_AUDITING_ENABLE",
                                                        "LINK_AUDITING_RESET"
                                                    ],
                                                    "type": "string"
                                                },
                                                "loginCredentialsDot1xPasswordType": {
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
                                                "lscApAuthTypeInfoAuthType": {
                                                    "default": "LSC_AP_AUTH_CAPWAP_DTLS",
                                                    "enum": [
                                                        "LSC_AP_AUTH_BOTH",
                                                        "LSC_AP_AUTH_CAPWAP_DTLS",
                                                        "LSC_AP_AUTH_DOT1X_PORT_AUTH",
                                                        "LSC_AP_AUTH_NONE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "max1xSessionLimitPerAp": {
                                                    "default": 0,
                                                    "type": "integer"
                                                },
                                                "maxCfgClients": {
                                                    "default": 0,
                                                    "maximum": 1200,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "memThresholdStatsMonitor": {
                                                    "default": 0,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "meshProfileName": {
                                                    "default": "default-mesh-profile",
                                                    "type": "string"
                                                },
                                                "noProxyList": {
                                                    "type": "string"
                                                },
                                                "nsiPortsStateEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "ntpServerInfoKeyFormat": {
                                                    "default": "AP_NTP_KEY_FORMAT_ASCII",
                                                    "enum": [
                                                        "AP_NTP_KEY_FORMAT_ASCII",
                                                        "AP_NTP_KEY_FORMAT_HEX"
                                                    ],
                                                    "type": "string"
                                                },
                                                "ntpServerInfoKeyId": {
                                                    "default": 1,
                                                    "maximum": 65535,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "ntpServerInfoNtpAddr": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "ntpServerTrustKey": {
                                                    "type": "string"
                                                },
                                                "oeapDataEncryptionEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "oeapLocalNet": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "oeapRogueDetectEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "pakRssiThresholdDetection": {
                                                    "default": -100,
                                                    "maximum": -50,
                                                    "minimum": -100,
                                                    "type": "integer"
                                                },
                                                "pakRssiThresholdReset": {
                                                    "default": 8,
                                                    "maximum": 99,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "pakRssiThresholdTrigger": {
                                                    "default": 10,
                                                    "maximum": 100,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "partialTraceEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoAll": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoCiscoAll": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoCiscoNdp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataAll": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataArp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataDhcp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataDhcpv6": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataDns": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataEap": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataIcmp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataIcmpv6": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoMgmtAll": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoMgmtAssoc": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoMgmtAuth": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoMgmtProbe": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "persistentSsidBroadcastEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "pmfDeauthEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "powerInjectorSelection": {
                                                    "default": "PWRINJ_UNKNOWN",
                                                    "enum": [
                                                        "PWRINJ_INSTALLED",
                                                        "PWRINJ_OVERRIDE",
                                                        "PWRINJ_UNKNOWN"
                                                    ],
                                                    "type": "string"
                                                },
                                                "powerInjectorStateEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "preStandard8023afSwitchFlag": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "pressSensConfigState": {
                                                    "default": "PRESS_SENSOR_AUTO",
                                                    "enum": [
                                                        "PRESS_SENSOR_AUTO",
                                                        "PRESS_SENSOR_DISABLED",
                                                        "PRESS_SENSOR_ENABLED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "primaryControllerIpAddr": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "primaryControllerName": {
                                                    "type": "string"
                                                },
                                                "primaryDiscoveryTimeout": {
                                                    "default": 120,
                                                    "maximum": 3000,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "primedJoinTimeout": {
                                                    "default": 0,
                                                    "maximum": 43200,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "privateIpDiscoveryEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "provisionalSsidEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "proxyHostname": {
                                                    "type": "string"
                                                },
                                                "proxyPort": {
                                                    "maximum": 65535,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "publicIpDiscoveryEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "qosmapActionFrameEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "radio24GhzReportingInterval": {
                                                    "default": 90,
                                                    "maximum": 90,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "radio5GhzReportingInterval": {
                                                    "default": 90,
                                                    "maximum": 90,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "radioResetEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "radioStatsMonitorAlarmsEnabled": {
                                                    "type": "boolean"
                                                },
                                                "radioStatsMonitorEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "retransmitTimerCount": {
                                                    "default": 5,
                                                    "maximum": 8,
                                                    "minimum": 3,
                                                    "type": "integer"
                                                },
                                                "retransmitTimerInterval": {
                                                    "default": 3,
                                                    "maximum": 5,
                                                    "minimum": 2,
                                                    "type": "integer"
                                                },
                                                "rfSpectrumEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfSpectrumSlot0Enabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfSpectrumSlot1Enabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfSpectrumSlot3Enabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rogueContainmentAutorate": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rogueContainmentFlexconnect": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rogueDetectionPmfDenial": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rogueDetectionProfileName": {
                                                    "type": "string"
                                                },
                                                "rogueReportInterval": {
                                                    "default": 10,
                                                    "maximum": 300,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "sampleInterval": {
                                                    "default": 720,
                                                    "maximum": 3600,
                                                    "minimum": 720,
                                                    "type": "integer"
                                                },
                                                "sampleIntvl": {
                                                    "default": 30,
                                                    "maximum": 900,
                                                    "minimum": 2,
                                                    "type": "integer"
                                                },
                                                "secondaryControllerIpAddr": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "secondaryControllerName": {
                                                    "type": "string"
                                                },
                                                "serialConsoleEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "sshEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "statsMonitorEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "statsMonitorStatsInterval": {
                                                    "default": 300,
                                                    "maximum": 900,
                                                    "minimum": 120,
                                                    "type": "integer"
                                                },
                                                "syslogFacilityValue": {
                                                    "default": "FACILITY_KERN",
                                                    "enum": [
                                                        "FACILITY_AUTH",
                                                        "FACILITY_CRON",
                                                        "FACILITY_DAEMON",
                                                        "FACILITY_KERN",
                                                        "FACILITY_LOCAL0",
                                                        "FACILITY_LOCAL1",
                                                        "FACILITY_LOCAL2",
                                                        "FACILITY_LOCAL3",
                                                        "FACILITY_LOCAL4",
                                                        "FACILITY_LOCAL5",
                                                        "FACILITY_LOCAL6",
                                                        "FACILITY_LOCAL7",
                                                        "FACILITY_LPR",
                                                        "FACILITY_MAIL",
                                                        "FACILITY_NEWS",
                                                        "FACILITY_SYS10",
                                                        "FACILITY_SYS11",
                                                        "FACILITY_SYS12",
                                                        "FACILITY_SYS13",
                                                        "FACILITY_SYS14",
                                                        "FACILITY_SYS9",
                                                        "FACILITY_SYSLOG",
                                                        "FACILITY_USER",
                                                        "FACILITY_UUCP"
                                                    ],
                                                    "type": "string"
                                                },
                                                "syslogHostIpAddress": {
                                                    "default": "255.255.255.255",
                                                    "type": "string"
                                                },
                                                "syslogLogLevel": {
                                                    "default": "SYSLOG_LEVEL_INFORMATION",
                                                    "enum": [
                                                        "SYSLOG_LEVEL_ALERT",
                                                        "SYSLOG_LEVEL_CRITICAL",
                                                        "SYSLOG_LEVEL_DEBUG",
                                                        "SYSLOG_LEVEL_EMERGENCY",
                                                        "SYSLOG_LEVEL_ERRORS",
                                                        "SYSLOG_LEVEL_INFORMATION",
                                                        "SYSLOG_LEVEL_NOTIFICATION",
                                                        "SYSLOG_LEVEL_WARNING"
                                                    ],
                                                    "type": "string"
                                                },
                                                "syslogTlsModeEnabled": {
                                                    "type": "boolean"
                                                },
                                                "tcpAdjustMss": {
                                                    "default": 1250,
                                                    "maximum": 1363,
                                                    "minimum": 536,
                                                    "type": "integer"
                                                },
                                                "tcpMssAdjustEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "telnetEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "tftpDowngradeFilename": {
                                                    "type": "string"
                                                },
                                                "tftpDowngradeIpAddress": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "tftpServerIpAddress": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "trafficDistributionInterval": {
                                                    "default": 300,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "trafficDistributionStatus": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "trapRetxTime": {
                                                    "default": 0,
                                                    "maximum": 65535,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "trustKeyType": {
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
                                                "tunnelPreferredMode": {
                                                    "default": "PREFERRED_MODE_UNCONFIG",
                                                    "enum": [
                                                        "PREFERRED_MODE_IPV4",
                                                        "PREFERRED_MODE_IPV6",
                                                        "PREFERRED_MODE_UNCONFIG"
                                                    ],
                                                    "type": "string"
                                                },
                                                "tzConfigEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "udpLiteIpv6CapwapChecksumType": {
                                                    "default": "UDPLITE_CHECKSUM_DISABLED",
                                                    "enum": [
                                                        "UDPLITE_CHECKSUM_DISABLED",
                                                        "UDPLITE_CHECKSUM_ENABLED",
                                                        "UDPLITE_CHECKSUM_UNCONFIGURED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "usbModuleEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "userMgmtPassword": {
                                                    "type": "string"
                                                },
                                                "userMgmtPasswordCryptType": {
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
                                                "userMgmtSecret": {
                                                    "type": "string"
                                                },
                                                "userMgmtSecretType": {
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
                                                "userMgmtUsername": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "uwbEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "uwbInitBurstDuration": {
                                                    "default": 10,
                                                    "maximum": 30,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "uwbInitBurstSize": {
                                                    "default": 32,
                                                    "maximum": 100,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "weakRssi": {
                                                    "default": -60,
                                                    "maximum": -10,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                }
                                            },
                                            "required": [
                                                "apCfgProfileName",
                                                "deviceVersion"
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
                                                "accelerometerSensorEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "acctMethodList": {
                                                    "type": "string"
                                                },
                                                "actionApReloadEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "adrIndividualAggrEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "adrIndividualEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "adrIndividualPcThrottle": {
                                                    "default": 5,
                                                    "maximum": 50,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "adrIndividualPtThrottle": {
                                                    "default": 5,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "adrSummaryEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "alarmHoldTime": {
                                                    "default": 6,
                                                    "maximum": 3600,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "alarmsEnabled": {
                                                    "type": "boolean"
                                                },
                                                "anomalyDetTriggerTraceAp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "anomalyDetectionEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "antennaMonitorDetectionTime": {
                                                    "default": 12,
                                                    "maximum": 180,
                                                    "minimum": 9,
                                                    "type": "integer"
                                                },
                                                "antennaMonitorEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "antennaMonitorRssiFailThreshold": {
                                                    "default": 40,
                                                    "maximum": 90,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "apCfgProfileDescription": {
                                                    "type": "string"
                                                },
                                                "apCfgProfileLedFlashSec": {
                                                    "default": 0,
                                                    "maximum": 3600,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "apCfgProfileName": {
                                                    "type": "string"
                                                },
                                                "apCfgProfileStatsTimer": {
                                                    "default": 180,
                                                    "maximum": 65535,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "apCountryCountryCode": {
                                                    "default": "UNCONFIGURED",
                                                    "enum": [
                                                        "AD",
                                                        "AE",
                                                        "AF",
                                                        "AG",
                                                        "AI",
                                                        "AL",
                                                        "AM",
                                                        "AO",
                                                        "AQ",
                                                        "AR",
                                                        "AS",
                                                        "AT",
                                                        "AU",
                                                        "AW",
                                                        "AX",
                                                        "AZ",
                                                        "BA",
                                                        "BB",
                                                        "BD",
                                                        "BE",
                                                        "BF",
                                                        "BG",
                                                        "BH",
                                                        "BI",
                                                        "BJ",
                                                        "BL",
                                                        "BM",
                                                        "BN",
                                                        "BO",
                                                        "BQ",
                                                        "BR",
                                                        "BS",
                                                        "BT",
                                                        "BV",
                                                        "BW",
                                                        "BY",
                                                        "BZ",
                                                        "CA",
                                                        "CC",
                                                        "CD",
                                                        "CF",
                                                        "CG",
                                                        "CH",
                                                        "CI",
                                                        "CK",
                                                        "CL",
                                                        "CM",
                                                        "CN",
                                                        "CO",
                                                        "CR",
                                                        "CU",
                                                        "CV",
                                                        "CW",
                                                        "CX",
                                                        "CY",
                                                        "CZ",
                                                        "DE",
                                                        "DJ",
                                                        "DK",
                                                        "DM",
                                                        "DO",
                                                        "DZ",
                                                        "EC",
                                                        "EE",
                                                        "EG",
                                                        "EH",
                                                        "EL",
                                                        "ER",
                                                        "ES",
                                                        "ET",
                                                        "FI",
                                                        "FJ",
                                                        "FK",
                                                        "FM",
                                                        "FO",
                                                        "FR",
                                                        "GA",
                                                        "GB",
                                                        "GD",
                                                        "GE",
                                                        "GF",
                                                        "GG",
                                                        "GH",
                                                        "GI",
                                                        "GL",
                                                        "GM",
                                                        "GN",
                                                        "GP",
                                                        "GQ",
                                                        "GR",
                                                        "GS",
                                                        "GT",
                                                        "GU",
                                                        "GW",
                                                        "GY",
                                                        "HK",
                                                        "HM",
                                                        "HN",
                                                        "HR",
                                                        "HT",
                                                        "HU",
                                                        "ID",
                                                        "IE",
                                                        "IL",
                                                        "IM",
                                                        "IN",
                                                        "IO",
                                                        "IQ",
                                                        "IR",
                                                        "IS",
                                                        "IT",
                                                        "J2",
                                                        "J3",
                                                        "J4",
                                                        "JE",
                                                        "JM",
                                                        "JO",
                                                        "JP",
                                                        "KE",
                                                        "KG",
                                                        "KH",
                                                        "KI",
                                                        "KM",
                                                        "KN",
                                                        "KP",
                                                        "KR",
                                                        "KW",
                                                        "KY",
                                                        "KZ",
                                                        "LA",
                                                        "LB",
                                                        "LC",
                                                        "LI",
                                                        "LK",
                                                        "LR",
                                                        "LS",
                                                        "LT",
                                                        "LU",
                                                        "LV",
                                                        "LY",
                                                        "MA",
                                                        "MC",
                                                        "MD",
                                                        "ME",
                                                        "MF",
                                                        "MG",
                                                        "MH",
                                                        "MK",
                                                        "ML",
                                                        "MM",
                                                        "MN",
                                                        "MO",
                                                        "MP",
                                                        "MQ",
                                                        "MR",
                                                        "MS",
                                                        "MT",
                                                        "MU",
                                                        "MV",
                                                        "MW",
                                                        "MX",
                                                        "MY",
                                                        "MZ",
                                                        "NA",
                                                        "NC",
                                                        "NE",
                                                        "NF",
                                                        "NG",
                                                        "NI",
                                                        "NL",
                                                        false,
                                                        "NP",
                                                        "NR",
                                                        "NU",
                                                        "NZ",
                                                        "OM",
                                                        "PA",
                                                        "PE",
                                                        "PF",
                                                        "PG",
                                                        "PH",
                                                        "PK",
                                                        "PL",
                                                        "PM",
                                                        "PN",
                                                        "PR",
                                                        "PS",
                                                        "PT",
                                                        "PW",
                                                        "PY",
                                                        "QA",
                                                        "RE",
                                                        "RO",
                                                        "RS",
                                                        "RU",
                                                        "RW",
                                                        "SA",
                                                        "SB",
                                                        "SC",
                                                        "SD",
                                                        "SE",
                                                        "SG",
                                                        "SH",
                                                        "SI",
                                                        "SJ",
                                                        "SK",
                                                        "SL",
                                                        "SM",
                                                        "SN",
                                                        "SO",
                                                        "SR",
                                                        "SS",
                                                        "ST",
                                                        "SV",
                                                        "SX",
                                                        "SY",
                                                        "SZ",
                                                        "TC",
                                                        "TD",
                                                        "TF",
                                                        "TG",
                                                        "TH",
                                                        "TI",
                                                        "TJ",
                                                        "TK",
                                                        "TL",
                                                        "TM",
                                                        "TN",
                                                        "TO",
                                                        "TR",
                                                        "TT",
                                                        "TV",
                                                        "TW",
                                                        "TZ",
                                                        "UA",
                                                        "UG",
                                                        "UM",
                                                        "UNCONFIGURED",
                                                        "US",
                                                        "UY",
                                                        "UZ",
                                                        "VA",
                                                        "VC",
                                                        "VE",
                                                        "VG",
                                                        "VI",
                                                        "VN",
                                                        "VU",
                                                        "WF",
                                                        "WS",
                                                        "XK",
                                                        "YE",
                                                        "YT",
                                                        "ZA",
                                                        "ZM",
                                                        "ZW"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apDeploymentModeType": {
                                                    "default": "AP_MODE_DEFAULT",
                                                    "enum": [
                                                        "AP_MODE_DEFAULT",
                                                        "AP_MODE_INDOOR",
                                                        "AP_MODE_OUTDOOR"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apDtlsCtrlPrefEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "apLagEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apNtpServerInfoKeyType": {
                                                    "default": "AP_NTP_KEY_TYPE_MD5",
                                                    "enum": [
                                                        "AP_NTP_KEY_TYPE_MD5",
                                                        "AP_NTP_KEY_TYPE_SHA1"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apPacketCaptureProfile": {
                                                    "type": "string"
                                                },
                                                "apProfPpCfgPowerProfileName": {
                                                    "maxLength": 128,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "apRogueDetectionEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "apRogueDetectionMinRssi": {
                                                    "default": -90,
                                                    "maximum": -70,
                                                    "minimum": -128,
                                                    "type": "integer"
                                                },
                                                "apRogueDetectionTransientInterval": {
                                                    "default": 0,
                                                    "type": "integer"
                                                },
                                                "apStatsDnsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsDnsFreq": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsInterfaceEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsInterfaceFreq": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsMemoryEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsMemoryFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsRadioEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsRadioFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsRoutingEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsRoutingFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsSysEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsSystemFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsWlanEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsWlanFreq": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apSubModeType": {
                                                    "enum": [
                                                        "AP_SUB_MODE_NONE",
                                                        "FORENSIC_AWIPS_MODE",
                                                        "LOCAL_NETWORK",
                                                        "NON_LOCAL_NETWORK",
                                                        "WIPS_MODE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apTraceProfile": {
                                                    "type": "string"
                                                },
                                                "apTrustsUpstreamDscpEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "apTzConfigMode": {
                                                    "default": "AP_TZ_NOT_CONFIGURED",
                                                    "enum": [
                                                        "AP_TZ_CONTROLLER_TZ",
                                                        "AP_TZ_NOT_CONFIGURED",
                                                        "AP_TZ_UTC_OFFSET"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apTzConfigOffsetHour": {
                                                    "default": 0,
                                                    "maximum": 14,
                                                    "minimum": -12,
                                                    "type": "integer"
                                                },
                                                "apTzConfigOffsetMin": {
                                                    "default": 0,
                                                    "maximum": 59,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "apphostEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "auxClientInterfaceVlanId": {
                                                    "default": 0,
                                                    "maximum": 4094,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "awipsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "awipsForensicEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "bleBeaconAdvpwr": {
                                                    "default": 59,
                                                    "maximum": 100,
                                                    "minimum": 40,
                                                    "type": "integer"
                                                },
                                                "bleBeaconInterval": {
                                                    "default": 1,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "bleScanStateEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "bssidEnableStats": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "bssidNeighborStatsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "bssidNeighborStatsFrequency": {
                                                    "default": 180,
                                                    "maximum": 600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "bssidStatsFrequency": {
                                                    "default": 30,
                                                    "maximum": 180,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "capwapAggregationEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "capwapWindowWindowSize": {
                                                    "default": 1,
                                                    "maximum": 50,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "cdpEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "clientFilterStatsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "clientFilterStatsFrequency": {
                                                    "default": 5,
                                                    "maximum": 3600,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "clientRssiStatsEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "clientRssiStatsInterval": {
                                                    "default": 30,
                                                    "maximum": 300,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "clientStatsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "clientStatsFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "configType": {
                                                    "default": "AP_JOIN_PROFILE",
                                                    "enum": [
                                                        "AP_JOIN_PROFILE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "coredumpFlagEnabled": {
                                                    "default": "TFTP_COREDUMP_DISABLE",
                                                    "enum": [
                                                        "TFTP_COREDUMP_COMPRESS",
                                                        "TFTP_COREDUMP_DISABLE",
                                                        "TFTP_COREDUMP_UNCOMPRESS"
                                                    ],
                                                    "type": "string"
                                                },
                                                "corefileName": {
                                                    "default": "default",
                                                    "type": "string"
                                                },
                                                "cpuThreshold": {
                                                    "default": 0,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "dataEncryptionEnabled": {
                                                    "type": "boolean"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.16",
                                                    "type": "string"
                                                },
                                                "dhcpFallbackEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "dhcpServerEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "discoveryTimeout": {
                                                    "default": 10,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "dot1xEapTypeInfoDot1xEapType": {
                                                    "default": "DOT1X_EAP_FAST",
                                                    "enum": [
                                                        "DOT1X_EAP_FAST",
                                                        "DOT1X_EAP_NONE",
                                                        "DOT1X_EAP_PEAP",
                                                        "DOT1X_EAP_TLS"
                                                    ],
                                                    "type": "string"
                                                },
                                                "dot1xPassword": {
                                                    "type": "string"
                                                },
                                                "dot1xUsername": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "extModuleEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "fallbackEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "fastChannel": {
                                                    "maximum": 4294967295,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "fastHeartBeatTimeout": {
                                                    "default": 0,
                                                    "maximum": 10,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "ftmEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "ftmInitBurstDuration": {
                                                    "default": "ENUM_32MS",
                                                    "enum": [
                                                        "ENUM_128MS",
                                                        "ENUM_16MS",
                                                        "ENUM_1MS",
                                                        "ENUM_250US",
                                                        "ENUM_2MS",
                                                        "ENUM_32MS",
                                                        "ENUM_4MS",
                                                        "ENUM_500US",
                                                        "ENUM_64MS",
                                                        "ENUM_8MS",
                                                        "ANY"
                                                    ],
                                                    "type": "string"
                                                },
                                                "ftmInitBurstSize": {
                                                    "default": 16,
                                                    "maximum": 31,
                                                    "minimum": 2,
                                                    "type": "integer"
                                                },
                                                "gasRateLimitEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "gasRateLimitIntervalMsec": {
                                                    "maximum": 10000,
                                                    "minimum": 100,
                                                    "type": "integer"
                                                },
                                                "gasRateLimitNumReqPerInterval": {
                                                    "maximum": 100,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "grpcEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "heartBeatTimeout": {
                                                    "default": 30,
                                                    "maximum": 30,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "hyperlocationEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "icapAdrIndividualThrottle": {
                                                    "default": 5,
                                                    "maximum": 500,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "icapAdrSummaryFrequency": {
                                                    "default": 5,
                                                    "maximum": 60,
                                                    "minimum": 3,
                                                    "type": "integer"
                                                },
                                                "icapAggrTraceEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "icapAnomalyDetDhcpTimeout": {
                                                    "default": 5,
                                                    "maximum": 120,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "icapFullTraceEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "injectorSwitchMacAddr": {
                                                    "default": "00:00:00:00:00:00",
                                                    "type": "string"
                                                },
                                                "isRfSpectrumSlot2Enabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "jumboMtuEnabled": {
                                                    "type": "boolean"
                                                },
                                                "kernelCoredumpLimit": {
                                                    "default": 5,
                                                    "maximum": 5,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "kernelCoredumpType": {
                                                    "default": "KERNEL_COREDUMP_TYPE_DISABLED",
                                                    "enum": [
                                                        "KERNEL_COREDUMP_TYPE_DISABLED",
                                                        "KERNEL_COREDUMP_TYPE_FULL",
                                                        "KERNEL_COREDUMP_TYPE_MINI"
                                                    ],
                                                    "type": "string"
                                                },
                                                "lawfulInterceptionEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "lawfulInterceptionTimerInterval": {
                                                    "default": 60,
                                                    "maximum": 600,
                                                    "minimum": 60,
                                                    "type": "integer"
                                                },
                                                "ledFlashMode": {
                                                    "default": "LED_FLASH_MODE_INDEFINITE",
                                                    "enum": [
                                                        "LED_FLASH_MODE_DISABLE",
                                                        "LED_FLASH_MODE_DURATION",
                                                        "LED_FLASH_MODE_INDEFINITE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "ledStateEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "linkLatencyFlagEnabled": {
                                                    "default": "LINK_AUDITING_DISABLE",
                                                    "enum": [
                                                        "LINK_AUDITING_DATA",
                                                        "LINK_AUDITING_DISABLE",
                                                        "LINK_AUDITING_ENABLE",
                                                        "LINK_AUDITING_RESET"
                                                    ],
                                                    "type": "string"
                                                },
                                                "loginCredentialsDot1xPasswordType": {
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
                                                "lscApAuthTypeInfoAuthType": {
                                                    "default": "LSC_AP_AUTH_CAPWAP_DTLS",
                                                    "enum": [
                                                        "LSC_AP_AUTH_BOTH",
                                                        "LSC_AP_AUTH_CAPWAP_DTLS",
                                                        "LSC_AP_AUTH_DOT1X_PORT_AUTH",
                                                        "LSC_AP_AUTH_NONE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "max1xSessionLimitPerAp": {
                                                    "default": 0,
                                                    "type": "integer"
                                                },
                                                "maxCfgClients": {
                                                    "default": 0,
                                                    "maximum": 1200,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "memThresholdStatsMonitor": {
                                                    "default": 0,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "meshProfileName": {
                                                    "default": "default-mesh-profile",
                                                    "type": "string"
                                                },
                                                "noProxyList": {
                                                    "type": "string"
                                                },
                                                "nsiPortsStateEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "ntpServerInfoKeyFormat": {
                                                    "default": "AP_NTP_KEY_FORMAT_ASCII",
                                                    "enum": [
                                                        "AP_NTP_KEY_FORMAT_ASCII",
                                                        "AP_NTP_KEY_FORMAT_HEX"
                                                    ],
                                                    "type": "string"
                                                },
                                                "ntpServerInfoKeyId": {
                                                    "default": 1,
                                                    "maximum": 65535,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "ntpServerInfoNtpAddr": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "ntpServerTrustKey": {
                                                    "type": "string"
                                                },
                                                "oeapDataEncryptionEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "oeapLocalNet": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "oeapRogueDetectEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "onboardConfig": {
                                                    "default": "AP_OB_UNICAST",
                                                    "enum": [
                                                        "AP_OB_ALL",
                                                        "AP_OB_DISABLED",
                                                        "AP_OB_UNICAST"
                                                    ],
                                                    "type": "string"
                                                },
                                                "pakRssiThresholdDetection": {
                                                    "default": -100,
                                                    "maximum": -50,
                                                    "minimum": -100,
                                                    "type": "integer"
                                                },
                                                "pakRssiThresholdReset": {
                                                    "default": 8,
                                                    "maximum": 99,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "pakRssiThresholdTrigger": {
                                                    "default": 10,
                                                    "maximum": 100,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "partialTraceEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoAll": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoCiscoAll": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoCiscoNdp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataAll": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataArp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataDhcp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataDhcpv6": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataDns": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataEap": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataIcmp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataIcmpv6": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoMgmtAll": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoMgmtAssoc": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoMgmtAuth": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoMgmtProbe": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "persistentSsidBroadcastEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "pmfDeauthEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "powerInjectorSelection": {
                                                    "default": "PWRINJ_UNKNOWN",
                                                    "enum": [
                                                        "PWRINJ_INSTALLED",
                                                        "PWRINJ_OVERRIDE",
                                                        "PWRINJ_UNKNOWN"
                                                    ],
                                                    "type": "string"
                                                },
                                                "powerInjectorStateEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "preStandard8023afSwitchFlag": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "pressSensConfigState": {
                                                    "default": "PRESS_SENSOR_AUTO",
                                                    "enum": [
                                                        "PRESS_SENSOR_AUTO",
                                                        "PRESS_SENSOR_DISABLED",
                                                        "PRESS_SENSOR_ENABLED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "primaryControllerIpAddr": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "primaryControllerName": {
                                                    "type": "string"
                                                },
                                                "primaryDiscoveryTimeout": {
                                                    "default": 120,
                                                    "maximum": 3000,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "primedJoinTimeout": {
                                                    "default": 0,
                                                    "maximum": 43200,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "privateIpDiscoveryEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "provisionalSsidEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "proxyHostname": {
                                                    "type": "string"
                                                },
                                                "proxyPort": {
                                                    "maximum": 65535,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "publicIpDiscoveryEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "qosmapActionFrameEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "radio24GhzReportingInterval": {
                                                    "default": 90,
                                                    "maximum": 90,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "radio5GhzReportingInterval": {
                                                    "default": 90,
                                                    "maximum": 90,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "radioResetEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "radioStatsMonitorAlarmsEnabled": {
                                                    "type": "boolean"
                                                },
                                                "radioStatsMonitorEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "retransmitTimerCount": {
                                                    "default": 5,
                                                    "maximum": 8,
                                                    "minimum": 3,
                                                    "type": "integer"
                                                },
                                                "retransmitTimerInterval": {
                                                    "default": 3,
                                                    "maximum": 5,
                                                    "minimum": 2,
                                                    "type": "integer"
                                                },
                                                "rfSpectrumEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfSpectrumSlot0Enabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfSpectrumSlot1Enabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfSpectrumSlot3Enabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rlanFastSwitchingEnabled": {
                                                    "type": "boolean"
                                                },
                                                "rogueContainmentAutorate": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rogueContainmentFlexconnect": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rogueDetectionPmfDenial": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rogueDetectionProfileName": {
                                                    "type": "string"
                                                },
                                                "rogueReportInterval": {
                                                    "default": 10,
                                                    "maximum": 300,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "sampleInterval": {
                                                    "default": 720,
                                                    "maximum": 3600,
                                                    "minimum": 720,
                                                    "type": "integer"
                                                },
                                                "sampleIntvl": {
                                                    "default": 30,
                                                    "maximum": 900,
                                                    "minimum": 2,
                                                    "type": "integer"
                                                },
                                                "secondaryControllerIpAddr": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "secondaryControllerName": {
                                                    "type": "string"
                                                },
                                                "serialConsoleEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "spacesConnCfgToken": {
                                                    "maxLength": 2047,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "spacesConnTokenType": {
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
                                                "sshEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "statsMonitorEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "statsMonitorStatsInterval": {
                                                    "default": 300,
                                                    "maximum": 900,
                                                    "minimum": 120,
                                                    "type": "integer"
                                                },
                                                "syslogFacilityValue": {
                                                    "default": "FACILITY_KERN",
                                                    "enum": [
                                                        "FACILITY_AUTH",
                                                        "FACILITY_CRON",
                                                        "FACILITY_DAEMON",
                                                        "FACILITY_KERN",
                                                        "FACILITY_LOCAL0",
                                                        "FACILITY_LOCAL1",
                                                        "FACILITY_LOCAL2",
                                                        "FACILITY_LOCAL3",
                                                        "FACILITY_LOCAL4",
                                                        "FACILITY_LOCAL5",
                                                        "FACILITY_LOCAL6",
                                                        "FACILITY_LOCAL7",
                                                        "FACILITY_LPR",
                                                        "FACILITY_MAIL",
                                                        "FACILITY_NEWS",
                                                        "FACILITY_SYS10",
                                                        "FACILITY_SYS11",
                                                        "FACILITY_SYS12",
                                                        "FACILITY_SYS13",
                                                        "FACILITY_SYS14",
                                                        "FACILITY_SYS9",
                                                        "FACILITY_SYSLOG",
                                                        "FACILITY_USER",
                                                        "FACILITY_UUCP"
                                                    ],
                                                    "type": "string"
                                                },
                                                "syslogHostIpAddress": {
                                                    "default": "255.255.255.255",
                                                    "type": "string"
                                                },
                                                "syslogLogLevel": {
                                                    "default": "SYSLOG_LEVEL_INFORMATION",
                                                    "enum": [
                                                        "SYSLOG_LEVEL_ALERT",
                                                        "SYSLOG_LEVEL_CRITICAL",
                                                        "SYSLOG_LEVEL_DEBUG",
                                                        "SYSLOG_LEVEL_EMERGENCY",
                                                        "SYSLOG_LEVEL_ERRORS",
                                                        "SYSLOG_LEVEL_INFORMATION",
                                                        "SYSLOG_LEVEL_NOTIFICATION",
                                                        "SYSLOG_LEVEL_WARNING"
                                                    ],
                                                    "type": "string"
                                                },
                                                "syslogTlsModeEnabled": {
                                                    "type": "boolean"
                                                },
                                                "tcpAdjustMss": {
                                                    "default": 1250,
                                                    "maximum": 1363,
                                                    "minimum": 536,
                                                    "type": "integer"
                                                },
                                                "tcpMssAdjustEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "telnetEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "tftpDowngradeFilename": {
                                                    "type": "string"
                                                },
                                                "tftpDowngradeIpAddress": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "tftpServerIpAddress": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "trafficDistributionInterval": {
                                                    "default": 300,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "trafficDistributionStatus": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "trapRetxTime": {
                                                    "default": 0,
                                                    "maximum": 65535,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "trustKeyType": {
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
                                                "tunnelPreferredMode": {
                                                    "default": "PREFERRED_MODE_UNCONFIG",
                                                    "enum": [
                                                        "PREFERRED_MODE_IPV4",
                                                        "PREFERRED_MODE_IPV6",
                                                        "PREFERRED_MODE_UNCONFIG"
                                                    ],
                                                    "type": "string"
                                                },
                                                "tzConfigEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "udpLiteIpv6CapwapChecksumType": {
                                                    "default": "UDPLITE_CHECKSUM_DISABLED",
                                                    "enum": [
                                                        "UDPLITE_CHECKSUM_DISABLED",
                                                        "UDPLITE_CHECKSUM_ENABLED",
                                                        "UDPLITE_CHECKSUM_UNCONFIGURED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "usbModuleEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "userMgmtPassword": {
                                                    "type": "string"
                                                },
                                                "userMgmtPasswordCryptType": {
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
                                                "userMgmtSecret": {
                                                    "type": "string"
                                                },
                                                "userMgmtSecretType": {
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
                                                "userMgmtUsername": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "uwbEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "uwbInitBurstDuration": {
                                                    "default": 10,
                                                    "maximum": 30,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "uwbInitBurstSize": {
                                                    "default": 32,
                                                    "maximum": 100,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "weakRssi": {
                                                    "default": -60,
                                                    "maximum": -10,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                }
                                            },
                                            "required": [
                                                "apCfgProfileName",
                                                "deviceVersion"
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
                                                "accelerometerSensorEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "acctMethodList": {
                                                    "type": "string"
                                                },
                                                "actionApReloadEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "adrIndividualAggrEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "adrIndividualEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "adrIndividualPcThrottle": {
                                                    "default": 5,
                                                    "maximum": 50,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "adrIndividualPtThrottle": {
                                                    "default": 5,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "adrSummaryEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "alarmHoldTime": {
                                                    "default": 6,
                                                    "maximum": 3600,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "alarmsEnabled": {
                                                    "type": "boolean"
                                                },
                                                "anomalyDetTriggerTraceAp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "anomalyDetectionEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "antennaMonitorDetectionTime": {
                                                    "default": 12,
                                                    "maximum": 180,
                                                    "minimum": 9,
                                                    "type": "integer"
                                                },
                                                "antennaMonitorEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "antennaMonitorRssiFailThreshold": {
                                                    "default": 40,
                                                    "maximum": 90,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "apCfgProfileDescription": {
                                                    "type": "string"
                                                },
                                                "apCfgProfileLedFlashSec": {
                                                    "default": 0,
                                                    "maximum": 3600,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "apCfgProfileName": {
                                                    "type": "string"
                                                },
                                                "apCfgProfileStatsTimer": {
                                                    "default": 180,
                                                    "maximum": 65535,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "apCountryCountryCode": {
                                                    "default": "UNCONFIGURED",
                                                    "enum": [
                                                        "AD",
                                                        "AE",
                                                        "AF",
                                                        "AG",
                                                        "AI",
                                                        "AL",
                                                        "AM",
                                                        "AO",
                                                        "AQ",
                                                        "AR",
                                                        "AS",
                                                        "AT",
                                                        "AU",
                                                        "AW",
                                                        "AX",
                                                        "AZ",
                                                        "BA",
                                                        "BB",
                                                        "BD",
                                                        "BE",
                                                        "BF",
                                                        "BG",
                                                        "BH",
                                                        "BI",
                                                        "BJ",
                                                        "BL",
                                                        "BM",
                                                        "BN",
                                                        "BO",
                                                        "BQ",
                                                        "BR",
                                                        "BS",
                                                        "BT",
                                                        "BV",
                                                        "BW",
                                                        "BY",
                                                        "BZ",
                                                        "CA",
                                                        "CC",
                                                        "CD",
                                                        "CF",
                                                        "CG",
                                                        "CH",
                                                        "CI",
                                                        "CK",
                                                        "CL",
                                                        "CM",
                                                        "CN",
                                                        "CO",
                                                        "CR",
                                                        "CU",
                                                        "CV",
                                                        "CW",
                                                        "CX",
                                                        "CY",
                                                        "CZ",
                                                        "DE",
                                                        "DJ",
                                                        "DK",
                                                        "DM",
                                                        "DO",
                                                        "DZ",
                                                        "EC",
                                                        "EE",
                                                        "EG",
                                                        "EH",
                                                        "EL",
                                                        "ER",
                                                        "ES",
                                                        "ET",
                                                        "FI",
                                                        "FJ",
                                                        "FK",
                                                        "FM",
                                                        "FO",
                                                        "FR",
                                                        "GA",
                                                        "GB",
                                                        "GD",
                                                        "GE",
                                                        "GF",
                                                        "GG",
                                                        "GH",
                                                        "GI",
                                                        "GL",
                                                        "GM",
                                                        "GN",
                                                        "GP",
                                                        "GQ",
                                                        "GR",
                                                        "GS",
                                                        "GT",
                                                        "GU",
                                                        "GW",
                                                        "GY",
                                                        "HK",
                                                        "HM",
                                                        "HN",
                                                        "HR",
                                                        "HT",
                                                        "HU",
                                                        "ID",
                                                        "IE",
                                                        "IL",
                                                        "IM",
                                                        "IN",
                                                        "IO",
                                                        "IQ",
                                                        "IR",
                                                        "IS",
                                                        "IT",
                                                        "J2",
                                                        "J3",
                                                        "J4",
                                                        "JE",
                                                        "JM",
                                                        "JO",
                                                        "JP",
                                                        "KE",
                                                        "KG",
                                                        "KH",
                                                        "KI",
                                                        "KM",
                                                        "KN",
                                                        "KP",
                                                        "KR",
                                                        "KW",
                                                        "KY",
                                                        "KZ",
                                                        "LA",
                                                        "LB",
                                                        "LC",
                                                        "LI",
                                                        "LK",
                                                        "LR",
                                                        "LS",
                                                        "LT",
                                                        "LU",
                                                        "LV",
                                                        "LY",
                                                        "MA",
                                                        "MC",
                                                        "MD",
                                                        "ME",
                                                        "MF",
                                                        "MG",
                                                        "MH",
                                                        "MK",
                                                        "ML",
                                                        "MM",
                                                        "MN",
                                                        "MO",
                                                        "MP",
                                                        "MQ",
                                                        "MR",
                                                        "MS",
                                                        "MT",
                                                        "MU",
                                                        "MV",
                                                        "MW",
                                                        "MX",
                                                        "MY",
                                                        "MZ",
                                                        "NA",
                                                        "NC",
                                                        "NE",
                                                        "NF",
                                                        "NG",
                                                        "NI",
                                                        "NL",
                                                        false,
                                                        "NP",
                                                        "NR",
                                                        "NU",
                                                        "NZ",
                                                        "OM",
                                                        "PA",
                                                        "PE",
                                                        "PF",
                                                        "PG",
                                                        "PH",
                                                        "PK",
                                                        "PL",
                                                        "PM",
                                                        "PN",
                                                        "PR",
                                                        "PS",
                                                        "PT",
                                                        "PW",
                                                        "PY",
                                                        "QA",
                                                        "RE",
                                                        "RO",
                                                        "RS",
                                                        "RU",
                                                        "RW",
                                                        "SA",
                                                        "SB",
                                                        "SC",
                                                        "SD",
                                                        "SE",
                                                        "SG",
                                                        "SH",
                                                        "SI",
                                                        "SJ",
                                                        "SK",
                                                        "SL",
                                                        "SM",
                                                        "SN",
                                                        "SO",
                                                        "SR",
                                                        "SS",
                                                        "ST",
                                                        "SV",
                                                        "SX",
                                                        "SY",
                                                        "SZ",
                                                        "TC",
                                                        "TD",
                                                        "TF",
                                                        "TG",
                                                        "TH",
                                                        "TI",
                                                        "TJ",
                                                        "TK",
                                                        "TL",
                                                        "TM",
                                                        "TN",
                                                        "TO",
                                                        "TR",
                                                        "TT",
                                                        "TV",
                                                        "TW",
                                                        "TZ",
                                                        "UA",
                                                        "UG",
                                                        "UM",
                                                        "UNCONFIGURED",
                                                        "US",
                                                        "UY",
                                                        "UZ",
                                                        "VA",
                                                        "VC",
                                                        "VE",
                                                        "VG",
                                                        "VI",
                                                        "VN",
                                                        "VU",
                                                        "WF",
                                                        "WS",
                                                        "XK",
                                                        "YE",
                                                        "YT",
                                                        "ZA",
                                                        "ZM",
                                                        "ZW"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apDeploymentModeType": {
                                                    "default": "AP_MODE_DEFAULT",
                                                    "enum": [
                                                        "AP_MODE_DEFAULT",
                                                        "AP_MODE_INDOOR",
                                                        "AP_MODE_OUTDOOR"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apDtlsCtrlPrefEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "apLagEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apNtpServerInfoKeyType": {
                                                    "default": "AP_NTP_KEY_TYPE_MD5",
                                                    "enum": [
                                                        "AP_NTP_KEY_TYPE_MD5",
                                                        "AP_NTP_KEY_TYPE_SHA1"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apPacketCaptureProfile": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "apProfPpCfgPowerProfileName": {
                                                    "maxLength": 128,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "apRogueDetectionEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "apRogueDetectionMinRssi": {
                                                    "default": -90,
                                                    "maximum": -70,
                                                    "minimum": -128,
                                                    "type": "integer"
                                                },
                                                "apRogueDetectionTransientInterval": {
                                                    "default": 0,
                                                    "type": "integer"
                                                },
                                                "apStatsDnsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsDnsFreq": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsInterfaceEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsInterfaceFreq": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsMemoryEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsMemoryFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsRadioEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsRadioFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsRoutingEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsRoutingFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsSysEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsSystemFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsWlanEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsWlanFreq": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apSubModeType": {
                                                    "enum": [
                                                        "AP_SUB_MODE_NONE",
                                                        "FORENSIC_AWIPS_MODE",
                                                        "LOCAL_NETWORK",
                                                        "NON_LOCAL_NETWORK",
                                                        "WIPS_MODE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apTraceProfile": {
                                                    "type": "string"
                                                },
                                                "apTrustsUpstreamDscpEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "apTzConfigMode": {
                                                    "default": "AP_TZ_NOT_CONFIGURED",
                                                    "enum": [
                                                        "AP_TZ_CONTROLLER_TZ",
                                                        "AP_TZ_NOT_CONFIGURED",
                                                        "AP_TZ_UTC_OFFSET"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apTzConfigOffsetHour": {
                                                    "default": 0,
                                                    "maximum": 14,
                                                    "minimum": -12,
                                                    "type": "integer"
                                                },
                                                "apTzConfigOffsetMin": {
                                                    "default": 0,
                                                    "maximum": 59,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "apphostEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "auxClientInterfaceVlanId": {
                                                    "default": 0,
                                                    "maximum": 4094,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "awipsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "awipsForensicEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "bleBeaconAdvpwr": {
                                                    "default": 59,
                                                    "maximum": 100,
                                                    "minimum": 40,
                                                    "type": "integer"
                                                },
                                                "bleBeaconInterval": {
                                                    "default": 1,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "bleScanStateEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "bssidEnableStats": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "bssidNeighborStatsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "bssidNeighborStatsFrequency": {
                                                    "default": 180,
                                                    "maximum": 600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "bssidStatsFrequency": {
                                                    "default": 30,
                                                    "maximum": 180,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "capwapAggregationEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "capwapWindowWindowSize": {
                                                    "default": 1,
                                                    "maximum": 50,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "cdpEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "clientFilterStatsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "clientFilterStatsFrequency": {
                                                    "default": 5,
                                                    "maximum": 3600,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "clientRssiStatsEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "clientRssiStatsInterval": {
                                                    "default": 30,
                                                    "maximum": 300,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "clientStatsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "clientStatsFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "configType": {
                                                    "default": "AP_JOIN_PROFILE",
                                                    "enum": [
                                                        "AP_JOIN_PROFILE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "coredumpFlagEnabled": {
                                                    "default": "TFTP_COREDUMP_DISABLE",
                                                    "enum": [
                                                        "TFTP_COREDUMP_COMPRESS",
                                                        "TFTP_COREDUMP_DISABLE",
                                                        "TFTP_COREDUMP_UNCOMPRESS"
                                                    ],
                                                    "type": "string"
                                                },
                                                "corefileName": {
                                                    "default": "default",
                                                    "type": "string"
                                                },
                                                "cpuThreshold": {
                                                    "default": 0,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "dataEncryptionEnabled": {
                                                    "type": "boolean"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.17",
                                                    "type": "string"
                                                },
                                                "dhcpFallbackEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "dhcpServerEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "discoveryTimeout": {
                                                    "default": 10,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "dot1xEapTypeInfoDot1xEapType": {
                                                    "default": "DOT1X_EAP_FAST",
                                                    "enum": [
                                                        "DOT1X_EAP_FAST",
                                                        "DOT1X_EAP_NONE",
                                                        "DOT1X_EAP_PEAP",
                                                        "DOT1X_EAP_TLS"
                                                    ],
                                                    "type": "string"
                                                },
                                                "dot1xPassword": {
                                                    "type": "string"
                                                },
                                                "dot1xUsername": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "extModuleEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "fallbackEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "fastChannel": {
                                                    "maximum": 4294967295,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "fastHeartBeatTimeout": {
                                                    "default": 0,
                                                    "maximum": 10,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "ftmEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "ftmInitBurstDuration": {
                                                    "default": "ENUM_32MS",
                                                    "enum": [
                                                        "ENUM_128MS",
                                                        "ENUM_16MS",
                                                        "ENUM_1MS",
                                                        "ENUM_250US",
                                                        "ENUM_2MS",
                                                        "ENUM_32MS",
                                                        "ENUM_4MS",
                                                        "ENUM_500US",
                                                        "ENUM_64MS",
                                                        "ENUM_8MS",
                                                        "ANY"
                                                    ],
                                                    "type": "string"
                                                },
                                                "ftmInitBurstSize": {
                                                    "default": 16,
                                                    "maximum": 31,
                                                    "minimum": 2,
                                                    "type": "integer"
                                                },
                                                "gasRateLimitEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "gasRateLimitIntervalMsec": {
                                                    "maximum": 10000,
                                                    "minimum": 100,
                                                    "type": "integer"
                                                },
                                                "gasRateLimitNumReqPerInterval": {
                                                    "maximum": 100,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "grpcEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "heartBeatTimeout": {
                                                    "default": 30,
                                                    "maximum": 30,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "hyperlocationEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "icapAdrIndividualThrottle": {
                                                    "default": 5,
                                                    "maximum": 500,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "icapAdrSummaryFrequency": {
                                                    "default": 5,
                                                    "maximum": 60,
                                                    "minimum": 3,
                                                    "type": "integer"
                                                },
                                                "icapAggrTraceEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "icapAnomalyDetDhcpTimeout": {
                                                    "default": 5,
                                                    "maximum": 120,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "icapFullTraceEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "injectorSwitchMacAddr": {
                                                    "default": "00:00:00:00:00:00",
                                                    "type": "string"
                                                },
                                                "isRfSpectrumSlot2Enabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "jumboMtuEnabled": {
                                                    "type": "boolean"
                                                },
                                                "kernelCoredumpLimit": {
                                                    "default": 5,
                                                    "maximum": 5,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "kernelCoredumpType": {
                                                    "default": "KERNEL_COREDUMP_TYPE_DISABLED",
                                                    "enum": [
                                                        "KERNEL_COREDUMP_TYPE_DISABLED",
                                                        "KERNEL_COREDUMP_TYPE_FULL",
                                                        "KERNEL_COREDUMP_TYPE_MINI"
                                                    ],
                                                    "type": "string"
                                                },
                                                "lawfulInterceptionEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "lawfulInterceptionTimerInterval": {
                                                    "default": 60,
                                                    "maximum": 600,
                                                    "minimum": 60,
                                                    "type": "integer"
                                                },
                                                "ledFlashMode": {
                                                    "default": "LED_FLASH_MODE_INDEFINITE",
                                                    "enum": [
                                                        "LED_FLASH_MODE_DISABLE",
                                                        "LED_FLASH_MODE_DURATION",
                                                        "LED_FLASH_MODE_INDEFINITE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "ledStateEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "linkLatencyFlagEnabled": {
                                                    "default": "LINK_AUDITING_DISABLE",
                                                    "enum": [
                                                        "LINK_AUDITING_DATA",
                                                        "LINK_AUDITING_DISABLE",
                                                        "LINK_AUDITING_ENABLE",
                                                        "LINK_AUDITING_RESET"
                                                    ],
                                                    "type": "string"
                                                },
                                                "loginCredentialsDot1xPasswordType": {
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
                                                "lscApAuthTypeInfoAuthType": {
                                                    "default": "LSC_AP_AUTH_CAPWAP_DTLS",
                                                    "enum": [
                                                        "LSC_AP_AUTH_BOTH",
                                                        "LSC_AP_AUTH_CAPWAP_DTLS",
                                                        "LSC_AP_AUTH_DOT1X_PORT_AUTH",
                                                        "LSC_AP_AUTH_NONE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "max1xSessionLimitPerAp": {
                                                    "default": 0,
                                                    "maximum": 255,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "maxCfgClients": {
                                                    "default": 0,
                                                    "maximum": 1200,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "memThresholdStatsMonitor": {
                                                    "default": 0,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "meshProfileName": {
                                                    "default": "default-mesh-profile",
                                                    "type": "string"
                                                },
                                                "noProxyList": {
                                                    "type": "string"
                                                },
                                                "nsiPortsStateEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "ntpServerInfoKeyFormat": {
                                                    "default": "AP_NTP_KEY_FORMAT_ASCII",
                                                    "enum": [
                                                        "AP_NTP_KEY_FORMAT_ASCII",
                                                        "AP_NTP_KEY_FORMAT_HEX"
                                                    ],
                                                    "type": "string"
                                                },
                                                "ntpServerInfoKeyId": {
                                                    "default": 1,
                                                    "maximum": 65535,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "ntpServerInfoNtpAddr": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "ntpServerTrustKey": {
                                                    "type": "string"
                                                },
                                                "oeapDataEncryptionEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "oeapLocalNet": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "oeapRogueDetectEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "onboardConfig": {
                                                    "default": "AP_OB_UNICAST",
                                                    "enum": [
                                                        "AP_OB_ALL",
                                                        "AP_OB_DISABLED",
                                                        "AP_OB_UNICAST"
                                                    ],
                                                    "type": "string"
                                                },
                                                "pakRssiThresholdDetection": {
                                                    "default": -100,
                                                    "maximum": -50,
                                                    "minimum": -100,
                                                    "type": "integer"
                                                },
                                                "pakRssiThresholdReset": {
                                                    "default": 8,
                                                    "maximum": 99,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "pakRssiThresholdTrigger": {
                                                    "default": 10,
                                                    "maximum": 100,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "partialTraceEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoAll": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoCiscoAll": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoCiscoNdp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataAll": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataArp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataDhcp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataDhcpv6": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataDns": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataEap": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataIcmp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataIcmpv6": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoMgmtAll": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoMgmtAssoc": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoMgmtAuth": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoMgmtProbe": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "persistentSsidBroadcastEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "pmfDeauthEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "powerInjectorSelection": {
                                                    "default": "PWRINJ_UNKNOWN",
                                                    "enum": [
                                                        "PWRINJ_INSTALLED",
                                                        "PWRINJ_OVERRIDE",
                                                        "PWRINJ_UNKNOWN"
                                                    ],
                                                    "type": "string"
                                                },
                                                "powerInjectorStateEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "preStandard8023afSwitchFlag": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "pressSensConfigState": {
                                                    "default": "PRESS_SENSOR_AUTO",
                                                    "enum": [
                                                        "PRESS_SENSOR_AUTO",
                                                        "PRESS_SENSOR_DISABLED",
                                                        "PRESS_SENSOR_ENABLED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "primaryControllerIpAddr": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "primaryControllerName": {
                                                    "type": "string"
                                                },
                                                "primaryDiscoveryTimeout": {
                                                    "default": 120,
                                                    "maximum": 3000,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "primedJoinTimeout": {
                                                    "default": 0,
                                                    "maximum": 43200,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "privateIpDiscoveryEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "provisionalSsidEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "proxyHostname": {
                                                    "type": "string"
                                                },
                                                "proxyPort": {
                                                    "maximum": 65535,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "publicIpDiscoveryEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "qosmapActionFrameEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "radio24GhzReportingInterval": {
                                                    "default": 90,
                                                    "maximum": 90,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "radio5GhzReportingInterval": {
                                                    "default": 90,
                                                    "maximum": 90,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "radioResetEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "radioStatsMonitorAlarmsEnabled": {
                                                    "type": "boolean"
                                                },
                                                "radioStatsMonitorEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "retransmitTimerCount": {
                                                    "default": 5,
                                                    "maximum": 8,
                                                    "minimum": 3,
                                                    "type": "integer"
                                                },
                                                "retransmitTimerInterval": {
                                                    "default": 3,
                                                    "maximum": 5,
                                                    "minimum": 2,
                                                    "type": "integer"
                                                },
                                                "rfSpectrumEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfSpectrumSlot0Enabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfSpectrumSlot1Enabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfSpectrumSlot3Enabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rlanFastSwitchingEnabled": {
                                                    "type": "boolean"
                                                },
                                                "rogueContainmentAutorate": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rogueContainmentFlexconnect": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rogueDetectionPmfDenial": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rogueDetectionPmfOffchannel": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rogueDetectionProfileName": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "rogueReportInterval": {
                                                    "default": 10,
                                                    "maximum": 300,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "sampleInterval": {
                                                    "default": 720,
                                                    "maximum": 3600,
                                                    "minimum": 720,
                                                    "type": "integer"
                                                },
                                                "sampleIntvl": {
                                                    "default": 30,
                                                    "maximum": 900,
                                                    "minimum": 2,
                                                    "type": "integer"
                                                },
                                                "secondaryControllerIpAddr": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "secondaryControllerName": {
                                                    "type": "string"
                                                },
                                                "serialConsoleEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "spacesConnCfgToken": {
                                                    "maxLength": 2047,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "spacesConnTokenType": {
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
                                                "sshEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "staticMtuSize": {
                                                    "maximum": 1485,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "statsMonitorEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "statsMonitorStatsInterval": {
                                                    "default": 300,
                                                    "maximum": 900,
                                                    "minimum": 120,
                                                    "type": "integer"
                                                },
                                                "syslogFacilityValue": {
                                                    "default": "FACILITY_KERN",
                                                    "enum": [
                                                        "FACILITY_AUTH",
                                                        "FACILITY_CRON",
                                                        "FACILITY_DAEMON",
                                                        "FACILITY_KERN",
                                                        "FACILITY_LOCAL0",
                                                        "FACILITY_LOCAL1",
                                                        "FACILITY_LOCAL2",
                                                        "FACILITY_LOCAL3",
                                                        "FACILITY_LOCAL4",
                                                        "FACILITY_LOCAL5",
                                                        "FACILITY_LOCAL6",
                                                        "FACILITY_LOCAL7",
                                                        "FACILITY_LPR",
                                                        "FACILITY_MAIL",
                                                        "FACILITY_NEWS",
                                                        "FACILITY_SYS10",
                                                        "FACILITY_SYS11",
                                                        "FACILITY_SYS12",
                                                        "FACILITY_SYS13",
                                                        "FACILITY_SYS14",
                                                        "FACILITY_SYS9",
                                                        "FACILITY_SYSLOG",
                                                        "FACILITY_USER",
                                                        "FACILITY_UUCP"
                                                    ],
                                                    "type": "string"
                                                },
                                                "syslogHostIpAddress": {
                                                    "default": "255.255.255.255",
                                                    "type": "string"
                                                },
                                                "syslogLogLevel": {
                                                    "default": "SYSLOG_LEVEL_INFORMATION",
                                                    "enum": [
                                                        "SYSLOG_LEVEL_ALERT",
                                                        "SYSLOG_LEVEL_CRITICAL",
                                                        "SYSLOG_LEVEL_DEBUG",
                                                        "SYSLOG_LEVEL_EMERGENCY",
                                                        "SYSLOG_LEVEL_ERRORS",
                                                        "SYSLOG_LEVEL_INFORMATION",
                                                        "SYSLOG_LEVEL_NOTIFICATION",
                                                        "SYSLOG_LEVEL_WARNING"
                                                    ],
                                                    "type": "string"
                                                },
                                                "syslogTlsModeEnabled": {
                                                    "type": "boolean"
                                                },
                                                "tcpAdjustMss": {
                                                    "default": 1250,
                                                    "maximum": 1363,
                                                    "minimum": 536,
                                                    "type": "integer"
                                                },
                                                "tcpMssAdjustEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "telnetEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "tftpDowngradeFilename": {
                                                    "type": "string"
                                                },
                                                "tftpDowngradeIpAddress": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "tftpServerIpAddress": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "trafficDistributionInterval": {
                                                    "default": 300,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "trafficDistributionStatus": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "trapRetxTime": {
                                                    "default": 0,
                                                    "maximum": 65535,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "trustKeyType": {
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
                                                "tunnelPreferredMode": {
                                                    "default": "PREFERRED_MODE_UNCONFIG",
                                                    "enum": [
                                                        "PREFERRED_MODE_IPV4",
                                                        "PREFERRED_MODE_IPV6",
                                                        "PREFERRED_MODE_UNCONFIG"
                                                    ],
                                                    "type": "string"
                                                },
                                                "tzConfigEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "udpLiteIpv6CapwapChecksumType": {
                                                    "default": "UDPLITE_CHECKSUM_DISABLED",
                                                    "enum": [
                                                        "UDPLITE_CHECKSUM_DISABLED",
                                                        "UDPLITE_CHECKSUM_ENABLED",
                                                        "UDPLITE_CHECKSUM_UNCONFIGURED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "usbModuleEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "userMgmtPassword": {
                                                    "type": "string"
                                                },
                                                "userMgmtPasswordCryptType": {
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
                                                "userMgmtSecret": {
                                                    "type": "string"
                                                },
                                                "userMgmtSecretType": {
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
                                                "userMgmtUsername": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "uwbEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "uwbInitBurstDuration": {
                                                    "default": 10,
                                                    "maximum": 30,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "uwbInitBurstSize": {
                                                    "default": 32,
                                                    "maximum": 100,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "weakRssi": {
                                                    "default": -60,
                                                    "maximum": -10,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                }
                                            },
                                            "required": [
                                                "apCfgProfileName",
                                                "deviceVersion"
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
                                                "accelerometerSensorEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "acctMethodList": {
                                                    "type": "string"
                                                },
                                                "actionApReloadEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "adrIndividualAggrEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "adrIndividualEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "adrIndividualPcThrottle": {
                                                    "default": 5,
                                                    "maximum": 50,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "adrIndividualPtThrottle": {
                                                    "default": 5,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "adrSummaryEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "alarmHoldTime": {
                                                    "default": 6,
                                                    "maximum": 3600,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "alarmsEnabled": {
                                                    "type": "boolean"
                                                },
                                                "anomalyDetTriggerTraceAp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "anomalyDetectionEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "antennaMonitorDetectionTime": {
                                                    "default": 12,
                                                    "maximum": 180,
                                                    "minimum": 9,
                                                    "type": "integer"
                                                },
                                                "antennaMonitorEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "antennaMonitorRssiFailThreshold": {
                                                    "default": 40,
                                                    "maximum": 90,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "apCfgProfileDescription": {
                                                    "type": "string"
                                                },
                                                "apCfgProfileLedFlashSec": {
                                                    "default": 0,
                                                    "maximum": 3600,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "apCfgProfileName": {
                                                    "type": "string"
                                                },
                                                "apCfgProfileStatsTimer": {
                                                    "default": 180,
                                                    "maximum": 65535,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "apCountryCountryCode": {
                                                    "default": "UNCONFIGURED",
                                                    "enum": [
                                                        "AD",
                                                        "AE",
                                                        "AF",
                                                        "AG",
                                                        "AI",
                                                        "AL",
                                                        "AM",
                                                        "AN",
                                                        "AO",
                                                        "AQ",
                                                        "AR",
                                                        "AS",
                                                        "AT",
                                                        "AU",
                                                        "AW",
                                                        "AX",
                                                        "AZ",
                                                        "BA",
                                                        "BB",
                                                        "BD",
                                                        "BE",
                                                        "BF",
                                                        "BG",
                                                        "BH",
                                                        "BI",
                                                        "BJ",
                                                        "BL",
                                                        "BM",
                                                        "BN",
                                                        "BO",
                                                        "BQ",
                                                        "BR",
                                                        "BS",
                                                        "BT",
                                                        "BU",
                                                        "BV",
                                                        "BW",
                                                        "BY",
                                                        "BZ",
                                                        "CA",
                                                        "CC",
                                                        "CD",
                                                        "CF",
                                                        "CG",
                                                        "CH",
                                                        "CI",
                                                        "CK",
                                                        "CL",
                                                        "CM",
                                                        "CN",
                                                        "CO",
                                                        "CR",
                                                        "CU",
                                                        "CV",
                                                        "CW",
                                                        "CX",
                                                        "CY",
                                                        "CZ",
                                                        "DE",
                                                        "DJ",
                                                        "DK",
                                                        "DM",
                                                        "DO",
                                                        "DZ",
                                                        "EC",
                                                        "EE",
                                                        "EG",
                                                        "EH",
                                                        "EL",
                                                        "ER",
                                                        "ES",
                                                        "ET",
                                                        "FI",
                                                        "FJ",
                                                        "FK",
                                                        "FM",
                                                        "FO",
                                                        "FR",
                                                        "GA",
                                                        "GB",
                                                        "GD",
                                                        "GE",
                                                        "GF",
                                                        "GG",
                                                        "GH",
                                                        "GI",
                                                        "GL",
                                                        "GM",
                                                        "GN",
                                                        "GP",
                                                        "GQ",
                                                        "GR",
                                                        "GS",
                                                        "GT",
                                                        "GU",
                                                        "GW",
                                                        "GY",
                                                        "HK",
                                                        "HM",
                                                        "HN",
                                                        "HR",
                                                        "HT",
                                                        "HU",
                                                        "IB",
                                                        "ID",
                                                        "IE",
                                                        "IL",
                                                        "IM",
                                                        "IN",
                                                        "IO",
                                                        "IQ",
                                                        "IR",
                                                        "IS",
                                                        "IT",
                                                        "J2",
                                                        "J3",
                                                        "J4",
                                                        "JE",
                                                        "JM",
                                                        "JO",
                                                        "JP",
                                                        "KE",
                                                        "KG",
                                                        "KH",
                                                        "KI",
                                                        "KM",
                                                        "KN",
                                                        "KP",
                                                        "KR",
                                                        "KW",
                                                        "KY",
                                                        "KZ",
                                                        "LA",
                                                        "LB",
                                                        "LC",
                                                        "LI",
                                                        "LK",
                                                        "LR",
                                                        "LS",
                                                        "LT",
                                                        "LU",
                                                        "LV",
                                                        "LY",
                                                        "MA",
                                                        "MC",
                                                        "MD",
                                                        "ME",
                                                        "MF",
                                                        "MG",
                                                        "MH",
                                                        "MK",
                                                        "ML",
                                                        "MM",
                                                        "MN",
                                                        "MO",
                                                        "MP",
                                                        "MQ",
                                                        "MR",
                                                        "MS",
                                                        "MT",
                                                        "MU",
                                                        "MV",
                                                        "MW",
                                                        "MX",
                                                        "MY",
                                                        "MZ",
                                                        "NA",
                                                        "NC",
                                                        "NE",
                                                        "NF",
                                                        "NG",
                                                        "NI",
                                                        "NK",
                                                        "NL",
                                                        false,
                                                        "NP",
                                                        "NR",
                                                        "NU",
                                                        "NZ",
                                                        "OM",
                                                        "PA",
                                                        "PE",
                                                        "PF",
                                                        "PG",
                                                        "PH",
                                                        "PK",
                                                        "PL",
                                                        "PM",
                                                        "PN",
                                                        "PR",
                                                        "PS",
                                                        "PT",
                                                        "PW",
                                                        "PY",
                                                        "QA",
                                                        "RE",
                                                        "RO",
                                                        "RS",
                                                        "RU",
                                                        "RW",
                                                        "SA",
                                                        "SB",
                                                        "SC",
                                                        "SD",
                                                        "SE",
                                                        "SG",
                                                        "SH",
                                                        "SI",
                                                        "SJ",
                                                        "SK",
                                                        "SL",
                                                        "SM",
                                                        "SN",
                                                        "SO",
                                                        "SR",
                                                        "SS",
                                                        "ST",
                                                        "SV",
                                                        "SX",
                                                        "SY",
                                                        "SZ",
                                                        "TC",
                                                        "TD",
                                                        "TF",
                                                        "TG",
                                                        "TH",
                                                        "TI",
                                                        "TJ",
                                                        "TK",
                                                        "TL",
                                                        "TM",
                                                        "TN",
                                                        "TO",
                                                        "TR",
                                                        "TT",
                                                        "TV",
                                                        "TW",
                                                        "TZ",
                                                        "UA",
                                                        "UG",
                                                        "UM",
                                                        "UNCONFIGURED",
                                                        "US",
                                                        "UY",
                                                        "UZ",
                                                        "VA",
                                                        "VC",
                                                        "VE",
                                                        "VG",
                                                        "VI",
                                                        "VN",
                                                        "VU",
                                                        "WF",
                                                        "WS",
                                                        "XK",
                                                        "XX",
                                                        "YE",
                                                        "YT",
                                                        "ZA",
                                                        "ZM",
                                                        "ZW"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apDeploymentModeType": {
                                                    "default": "AP_MODE_DEFAULT",
                                                    "enum": [
                                                        "AP_MODE_DEFAULT",
                                                        "AP_MODE_INDOOR",
                                                        "AP_MODE_OUTDOOR"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apDtlsCtrlPrefEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "apLagEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apMgmtAclNameV4": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "apMgmtAclNameV6": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "apNtpServerInfoKeyType": {
                                                    "default": "AP_NTP_KEY_TYPE_MD5",
                                                    "enum": [
                                                        "AP_NTP_KEY_TYPE_MD5",
                                                        "AP_NTP_KEY_TYPE_SHA1"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apPacketCaptureProfile": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "apProfPpCfgPowerProfileName": {
                                                    "maxLength": 128,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "apRogueDetectionEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "apRogueDetectionMinRssi": {
                                                    "default": -90,
                                                    "maximum": -70,
                                                    "minimum": -128,
                                                    "type": "integer"
                                                },
                                                "apRogueDetectionTransientInterval": {
                                                    "default": 0,
                                                    "type": "integer"
                                                },
                                                "apStatsDnsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsDnsFreq": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsInterfaceEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsInterfaceFreq": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsMemoryEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsMemoryFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsRadioEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsRadioFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsRoutingEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsRoutingFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsSysEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsSystemFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsWlanEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsWlanFreq": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apSubModeType": {
                                                    "enum": [
                                                        "AP_SUB_MODE_NONE",
                                                        "FORENSIC_AWIPS_MODE",
                                                        "LOCAL_NETWORK",
                                                        "NON_LOCAL_NETWORK",
                                                        "WIPS_MODE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apTraceProfile": {
                                                    "type": "string"
                                                },
                                                "apTrustsUpstreamDscpEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "apTzConfigMode": {
                                                    "default": "AP_TZ_NOT_CONFIGURED",
                                                    "enum": [
                                                        "AP_TZ_CONTROLLER_TZ",
                                                        "AP_TZ_NOT_CONFIGURED",
                                                        "AP_TZ_UTC_OFFSET"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apTzConfigOffsetHour": {
                                                    "default": 0,
                                                    "maximum": 14,
                                                    "minimum": -12,
                                                    "type": "integer"
                                                },
                                                "apTzConfigOffsetMin": {
                                                    "default": 0,
                                                    "maximum": 59,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "apphostEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "auxClientInterfaceVlanId": {
                                                    "default": 0,
                                                    "maximum": 4094,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "awipsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "awipsForensicEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "bleBeaconAdvpwr": {
                                                    "default": 59,
                                                    "maximum": 100,
                                                    "minimum": 40,
                                                    "type": "integer"
                                                },
                                                "bleBeaconInterval": {
                                                    "default": 1,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "bleScanStateEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "bssidEnableStats": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "bssidNeighborStatsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "bssidNeighborStatsFrequency": {
                                                    "default": 180,
                                                    "maximum": 600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "bssidStatsFrequency": {
                                                    "default": 30,
                                                    "maximum": 180,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "capwapAggregationEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "capwapWindowWindowSize": {
                                                    "default": 1,
                                                    "maximum": 50,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "cdpEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "clientFilterStatsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "clientFilterStatsFrequency": {
                                                    "default": 5,
                                                    "maximum": 3600,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "clientRssiStatsEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "clientRssiStatsInterval": {
                                                    "default": 30,
                                                    "maximum": 300,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "clientStatsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "clientStatsFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "configType": {
                                                    "default": "AP_JOIN_PROFILE",
                                                    "enum": [
                                                        "AP_JOIN_PROFILE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "coredumpFlagEnabled": {
                                                    "default": "TFTP_COREDUMP_DISABLE",
                                                    "enum": [
                                                        "TFTP_COREDUMP_COMPRESS",
                                                        "TFTP_COREDUMP_DISABLE",
                                                        "TFTP_COREDUMP_UNCOMPRESS"
                                                    ],
                                                    "type": "string"
                                                },
                                                "corefileName": {
                                                    "default": "default",
                                                    "type": "string"
                                                },
                                                "cpuThreshold": {
                                                    "default": 0,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "dataEncryptionEnabled": {
                                                    "type": "boolean"
                                                },
                                                "deviceVersion": {
                                                    "default": "17.18",
                                                    "type": "string"
                                                },
                                                "dhcpFallbackEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "dhcpServerEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "discoveryTimeout": {
                                                    "default": 10,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "dot1xEapTypeInfoDot1xEapType": {
                                                    "default": "DOT1X_EAP_FAST",
                                                    "enum": [
                                                        "DOT1X_EAP_FAST",
                                                        "DOT1X_EAP_NONE",
                                                        "DOT1X_EAP_PEAP",
                                                        "DOT1X_EAP_TLS"
                                                    ],
                                                    "type": "string"
                                                },
                                                "dot1xPassword": {
                                                    "type": "string"
                                                },
                                                "dot1xUsername": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "extModuleEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "fallbackEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "fastChannel": {
                                                    "maximum": 4294967295,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "fastHeartBeatTimeout": {
                                                    "default": 0,
                                                    "maximum": 10,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "ftmEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "ftmInitBurstDuration": {
                                                    "default": "ENUM_32MS",
                                                    "enum": [
                                                        "ENUM_128MS",
                                                        "ENUM_16MS",
                                                        "ENUM_1MS",
                                                        "ENUM_250US",
                                                        "ENUM_2MS",
                                                        "ENUM_32MS",
                                                        "ENUM_4MS",
                                                        "ENUM_500US",
                                                        "ENUM_64MS",
                                                        "ENUM_8MS",
                                                        "ANY"
                                                    ],
                                                    "type": "string"
                                                },
                                                "ftmInitBurstSize": {
                                                    "default": 16,
                                                    "maximum": 31,
                                                    "minimum": 2,
                                                    "type": "integer"
                                                },
                                                "gasRateLimitEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "gasRateLimitIntervalMsec": {
                                                    "maximum": 10000,
                                                    "minimum": 100,
                                                    "type": "integer"
                                                },
                                                "gasRateLimitNumReqPerInterval": {
                                                    "maximum": 100,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "grpcEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "heartBeatTimeout": {
                                                    "default": 30,
                                                    "maximum": 30,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "hyperlocationEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "icapAdrIndividualThrottle": {
                                                    "default": 5,
                                                    "maximum": 500,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "icapAdrSummaryFrequency": {
                                                    "default": 5,
                                                    "maximum": 60,
                                                    "minimum": 3,
                                                    "type": "integer"
                                                },
                                                "icapAggrTraceEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "icapAnomalyDetDhcpTimeout": {
                                                    "default": 5,
                                                    "maximum": 120,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "icapFullTraceEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "injectorSwitchMacAddr": {
                                                    "default": "00:00:00:00:00:00",
                                                    "type": "string"
                                                },
                                                "isRfSpectrumSlot2Enabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "jumboMtuEnabled": {
                                                    "type": "boolean"
                                                },
                                                "kernelCoredumpDlimit": {
                                                    "default": 15,
                                                    "maximum": 25,
                                                    "minimum": 15,
                                                    "type": "integer"
                                                },
                                                "kernelCoredumpLimit": {
                                                    "default": 5,
                                                    "maximum": 5,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "kernelCoredumpType": {
                                                    "default": "KERNEL_COREDUMP_TYPE_DISABLED",
                                                    "enum": [
                                                        "KERNEL_COREDUMP_TYPE_DISABLED",
                                                        "KERNEL_COREDUMP_TYPE_FULL",
                                                        "KERNEL_COREDUMP_TYPE_MINI"
                                                    ],
                                                    "type": "string"
                                                },
                                                "lawfulInterceptionEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "lawfulInterceptionTimerInterval": {
                                                    "default": 60,
                                                    "maximum": 600,
                                                    "minimum": 60,
                                                    "type": "integer"
                                                },
                                                "ledFlashMode": {
                                                    "default": "LED_FLASH_MODE_INDEFINITE",
                                                    "enum": [
                                                        "LED_FLASH_MODE_DISABLE",
                                                        "LED_FLASH_MODE_DURATION",
                                                        "LED_FLASH_MODE_INDEFINITE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "ledStateEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "linkLatencyFlagEnabled": {
                                                    "default": "LINK_AUDITING_DISABLE",
                                                    "enum": [
                                                        "LINK_AUDITING_DATA",
                                                        "LINK_AUDITING_DISABLE",
                                                        "LINK_AUDITING_ENABLE",
                                                        "LINK_AUDITING_RESET"
                                                    ],
                                                    "type": "string"
                                                },
                                                "loginCredentialsDot1xPasswordType": {
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
                                                "lscApAuthTypeInfoAuthType": {
                                                    "default": "LSC_AP_AUTH_CAPWAP_DTLS",
                                                    "enum": [
                                                        "LSC_AP_AUTH_BOTH",
                                                        "LSC_AP_AUTH_CAPWAP_DTLS",
                                                        "LSC_AP_AUTH_DOT1X_PORT_AUTH",
                                                        "LSC_AP_AUTH_NONE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "max1xSessionLimitPerAp": {
                                                    "default": 0,
                                                    "maximum": 255,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "maxCfgClients": {
                                                    "default": 0,
                                                    "maximum": 1200,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "memThresholdStatsMonitor": {
                                                    "default": 0,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "meshProfileName": {
                                                    "default": "default-mesh-profile",
                                                    "type": "string"
                                                },
                                                "noProxyList": {
                                                    "type": "string"
                                                },
                                                "nsiPortsStateEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "ntpServerInfoKeyFormat": {
                                                    "default": "AP_NTP_KEY_FORMAT_ASCII",
                                                    "enum": [
                                                        "AP_NTP_KEY_FORMAT_ASCII",
                                                        "AP_NTP_KEY_FORMAT_HEX"
                                                    ],
                                                    "type": "string"
                                                },
                                                "ntpServerInfoKeyId": {
                                                    "default": 1,
                                                    "maximum": 65535,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "ntpServerInfoNtpAddr": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "ntpServerTrustKey": {
                                                    "type": "string"
                                                },
                                                "oeapDataEncryptionEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "oeapLocalNet": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "oeapRogueDetectEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "onboardConfig": {
                                                    "default": "AP_OB_UNICAST",
                                                    "enum": [
                                                        "AP_OB_ALL",
                                                        "AP_OB_DISABLED",
                                                        "AP_OB_UNICAST"
                                                    ],
                                                    "type": "string"
                                                },
                                                "pakRssiThresholdDetection": {
                                                    "default": -100,
                                                    "maximum": -50,
                                                    "minimum": -100,
                                                    "type": "integer"
                                                },
                                                "pakRssiThresholdReset": {
                                                    "default": 8,
                                                    "maximum": 99,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "pakRssiThresholdTrigger": {
                                                    "default": 10,
                                                    "maximum": 100,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "partialTraceEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoAll": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoCiscoAll": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoCiscoNdp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataAll": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataArp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataDhcp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataDhcpv6": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataDns": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataEap": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataIcmp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataIcmpv6": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoMgmtAll": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoMgmtAssoc": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoMgmtAuth": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoMgmtProbe": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "persistentSsidBroadcastEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "pmfDeauthEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "powerInjectorSelection": {
                                                    "default": "PWRINJ_UNKNOWN",
                                                    "enum": [
                                                        "PWRINJ_INSTALLED",
                                                        "PWRINJ_OVERRIDE",
                                                        "PWRINJ_UNKNOWN"
                                                    ],
                                                    "type": "string"
                                                },
                                                "powerInjectorStateEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "preStandard8023afSwitchFlag": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "pressSensConfigState": {
                                                    "default": "PRESS_SENSOR_AUTO",
                                                    "enum": [
                                                        "PRESS_SENSOR_AUTO",
                                                        "PRESS_SENSOR_DISABLED",
                                                        "PRESS_SENSOR_ENABLED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "primaryControllerIpAddr": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "primaryControllerName": {
                                                    "type": "string"
                                                },
                                                "primaryDiscoveryTimeout": {
                                                    "default": 120,
                                                    "maximum": 3000,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "primedJoinTimeout": {
                                                    "default": 0,
                                                    "maximum": 43200,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "privateIpDiscoveryEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "provisionalSsidEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "proxyHostname": {
                                                    "type": "string"
                                                },
                                                "proxyPort": {
                                                    "maximum": 65535,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "publicIpDiscoveryEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "qosmapActionFrameEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "radio24GhzReportingInterval": {
                                                    "default": 90,
                                                    "maximum": 90,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "radio5GhzReportingInterval": {
                                                    "default": 90,
                                                    "maximum": 90,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "radioResetEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "radioStatsMonitorAlarmsEnabled": {
                                                    "type": "boolean"
                                                },
                                                "radioStatsMonitorEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "retransmitTimerCount": {
                                                    "default": 5,
                                                    "maximum": 8,
                                                    "minimum": 3,
                                                    "type": "integer"
                                                },
                                                "retransmitTimerInterval": {
                                                    "default": 3,
                                                    "maximum": 5,
                                                    "minimum": 2,
                                                    "type": "integer"
                                                },
                                                "rfSpectrumEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfSpectrumSlot0Enabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfSpectrumSlot1Enabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfSpectrumSlot3Enabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rlanFastSwitchingEnabled": {
                                                    "type": "boolean"
                                                },
                                                "rogueContainmentAutorate": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rogueContainmentFlexconnect": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rogueDetectionPmfDenial": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rogueDetectionPmfOffchannel": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rogueDetectionProfileName": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "rogueReportInterval": {
                                                    "default": 10,
                                                    "maximum": 300,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "sampleInterval": {
                                                    "default": 720,
                                                    "maximum": 3600,
                                                    "minimum": 720,
                                                    "type": "integer"
                                                },
                                                "sampleIntvl": {
                                                    "default": 30,
                                                    "maximum": 900,
                                                    "minimum": 2,
                                                    "type": "integer"
                                                },
                                                "secondaryControllerIpAddr": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "secondaryControllerName": {
                                                    "type": "string"
                                                },
                                                "serialConsoleEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "spacesConnCfgToken": {
                                                    "maxLength": 2047,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "spacesConnTokenType": {
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
                                                "sshEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "staticMtuSize": {
                                                    "maximum": 1485,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "statsMonitorEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "statsMonitorStatsInterval": {
                                                    "default": 300,
                                                    "maximum": 900,
                                                    "minimum": 120,
                                                    "type": "integer"
                                                },
                                                "syslogFacilityValue": {
                                                    "default": "FACILITY_KERN",
                                                    "enum": [
                                                        "FACILITY_AUTH",
                                                        "FACILITY_CRON",
                                                        "FACILITY_DAEMON",
                                                        "FACILITY_KERN",
                                                        "FACILITY_LOCAL0",
                                                        "FACILITY_LOCAL1",
                                                        "FACILITY_LOCAL2",
                                                        "FACILITY_LOCAL3",
                                                        "FACILITY_LOCAL4",
                                                        "FACILITY_LOCAL5",
                                                        "FACILITY_LOCAL6",
                                                        "FACILITY_LOCAL7",
                                                        "FACILITY_LPR",
                                                        "FACILITY_MAIL",
                                                        "FACILITY_NEWS",
                                                        "FACILITY_SYS10",
                                                        "FACILITY_SYS11",
                                                        "FACILITY_SYS12",
                                                        "FACILITY_SYS13",
                                                        "FACILITY_SYS14",
                                                        "FACILITY_SYS9",
                                                        "FACILITY_SYSLOG",
                                                        "FACILITY_USER",
                                                        "FACILITY_UUCP"
                                                    ],
                                                    "type": "string"
                                                },
                                                "syslogHostIpAddress": {
                                                    "default": "255.255.255.255",
                                                    "type": "string"
                                                },
                                                "syslogLogLevel": {
                                                    "default": "SYSLOG_LEVEL_INFORMATION",
                                                    "enum": [
                                                        "SYSLOG_LEVEL_ALERT",
                                                        "SYSLOG_LEVEL_CRITICAL",
                                                        "SYSLOG_LEVEL_DEBUG",
                                                        "SYSLOG_LEVEL_EMERGENCY",
                                                        "SYSLOG_LEVEL_ERRORS",
                                                        "SYSLOG_LEVEL_INFORMATION",
                                                        "SYSLOG_LEVEL_NOTIFICATION",
                                                        "SYSLOG_LEVEL_WARNING"
                                                    ],
                                                    "type": "string"
                                                },
                                                "syslogTlsModeEnabled": {
                                                    "type": "boolean"
                                                },
                                                "tcpAdjustMss": {
                                                    "default": 1250,
                                                    "maximum": 1363,
                                                    "minimum": 536,
                                                    "type": "integer"
                                                },
                                                "tcpMssAdjustEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "telnetEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "tftpDowngradeFilename": {
                                                    "type": "string"
                                                },
                                                "tftpDowngradeIpAddress": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "tftpServerIpAddress": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "trafficDistributionInterval": {
                                                    "default": 300,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "trafficDistributionStatus": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "trapRetxTime": {
                                                    "default": 0,
                                                    "maximum": 65535,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "trustKeyType": {
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
                                                "tunnelPreferredMode": {
                                                    "default": "PREFERRED_MODE_UNCONFIG",
                                                    "enum": [
                                                        "PREFERRED_MODE_IPV4",
                                                        "PREFERRED_MODE_IPV6",
                                                        "PREFERRED_MODE_UNCONFIG"
                                                    ],
                                                    "type": "string"
                                                },
                                                "tzConfigEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "udpLiteIpv6CapwapChecksumType": {
                                                    "default": "UDPLITE_CHECKSUM_DISABLED",
                                                    "enum": [
                                                        "UDPLITE_CHECKSUM_DISABLED",
                                                        "UDPLITE_CHECKSUM_ENABLED",
                                                        "UDPLITE_CHECKSUM_UNCONFIGURED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "usbModuleEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "userMgmtPassword": {
                                                    "type": "string"
                                                },
                                                "userMgmtPasswordCryptType": {
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
                                                "userMgmtSecret": {
                                                    "type": "string"
                                                },
                                                "userMgmtSecretType": {
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
                                                "userMgmtUsername": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "uwbEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "uwbInitBurstDuration": {
                                                    "default": 10,
                                                    "maximum": 30,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "uwbInitBurstSize": {
                                                    "default": 32,
                                                    "maximum": 100,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "uwbWayFindingBlockDuration": {
                                                    "default": "WF_BLK_DUR_1SEC",
                                                    "enum": [
                                                        "WF_BLK_DUR_1SEC",
                                                        "WF_BLK_DUR_500MS"
                                                    ],
                                                    "type": "string"
                                                },
                                                "uwbWayFindingEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "weakRssi": {
                                                    "default": -60,
                                                    "maximum": -10,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                }
                                            },
                                            "required": [
                                                "apCfgProfileName",
                                                "deviceVersion"
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
                                                "accelerometerSensorEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "acctMethodList": {
                                                    "type": "string"
                                                },
                                                "actionApReloadEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "adrIndividualAggrEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "adrIndividualEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "adrIndividualPcThrottle": {
                                                    "default": 5,
                                                    "maximum": 50,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "adrIndividualPtThrottle": {
                                                    "default": 5,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "adrSummaryEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "alarmHoldTime": {
                                                    "default": 6,
                                                    "maximum": 3600,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "alarmsEnabled": {
                                                    "type": "boolean"
                                                },
                                                "anomalyDetTriggerTraceAp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "anomalyDetectionEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "antennaMonitorDetectionTime": {
                                                    "default": 12,
                                                    "maximum": 180,
                                                    "minimum": 9,
                                                    "type": "integer"
                                                },
                                                "antennaMonitorEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "antennaMonitorRssiFailThreshold": {
                                                    "default": 40,
                                                    "maximum": 90,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "apCfgProfileDescription": {
                                                    "type": "string"
                                                },
                                                "apCfgProfileLedFlashSec": {
                                                    "default": 0,
                                                    "maximum": 3600,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "apCfgProfileName": {
                                                    "type": "string"
                                                },
                                                "apCfgProfileStatsTimer": {
                                                    "default": 180,
                                                    "maximum": 65535,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "apCountryCountryCode": {
                                                    "default": "UNCONFIGURED",
                                                    "enum": [
                                                        "AD",
                                                        "AE",
                                                        "AF",
                                                        "AG",
                                                        "AI",
                                                        "AL",
                                                        "AM",
                                                        "AN",
                                                        "AO",
                                                        "AQ",
                                                        "AR",
                                                        "AS",
                                                        "AT",
                                                        "AU",
                                                        "AW",
                                                        "AX",
                                                        "AZ",
                                                        "BA",
                                                        "BB",
                                                        "BD",
                                                        "BE",
                                                        "BF",
                                                        "BG",
                                                        "BH",
                                                        "BI",
                                                        "BJ",
                                                        "BL",
                                                        "BM",
                                                        "BN",
                                                        "BO",
                                                        "BQ",
                                                        "BR",
                                                        "BS",
                                                        "BT",
                                                        "BU",
                                                        "BV",
                                                        "BW",
                                                        "BY",
                                                        "BZ",
                                                        "CA",
                                                        "CC",
                                                        "CD",
                                                        "CF",
                                                        "CG",
                                                        "CH",
                                                        "CI",
                                                        "CK",
                                                        "CL",
                                                        "CM",
                                                        "CN",
                                                        "CO",
                                                        "CR",
                                                        "CU",
                                                        "CV",
                                                        "CW",
                                                        "CX",
                                                        "CY",
                                                        "CZ",
                                                        "DE",
                                                        "DJ",
                                                        "DK",
                                                        "DM",
                                                        "DO",
                                                        "DZ",
                                                        "EC",
                                                        "EE",
                                                        "EG",
                                                        "EH",
                                                        "EL",
                                                        "ER",
                                                        "ES",
                                                        "ET",
                                                        "FI",
                                                        "FJ",
                                                        "FK",
                                                        "FM",
                                                        "FO",
                                                        "FR",
                                                        "GA",
                                                        "GB",
                                                        "GD",
                                                        "GE",
                                                        "GF",
                                                        "GG",
                                                        "GH",
                                                        "GI",
                                                        "GL",
                                                        "GM",
                                                        "GN",
                                                        "GP",
                                                        "GQ",
                                                        "GR",
                                                        "GS",
                                                        "GT",
                                                        "GU",
                                                        "GW",
                                                        "GY",
                                                        "HK",
                                                        "HM",
                                                        "HN",
                                                        "HR",
                                                        "HT",
                                                        "HU",
                                                        "IB",
                                                        "ID",
                                                        "IE",
                                                        "IL",
                                                        "IM",
                                                        "IN",
                                                        "IO",
                                                        "IQ",
                                                        "IR",
                                                        "IS",
                                                        "IT",
                                                        "J2",
                                                        "J3",
                                                        "J4",
                                                        "JE",
                                                        "JM",
                                                        "JO",
                                                        "JP",
                                                        "KE",
                                                        "KG",
                                                        "KH",
                                                        "KI",
                                                        "KM",
                                                        "KN",
                                                        "KP",
                                                        "KR",
                                                        "KW",
                                                        "KY",
                                                        "KZ",
                                                        "LA",
                                                        "LB",
                                                        "LC",
                                                        "LI",
                                                        "LK",
                                                        "LR",
                                                        "LS",
                                                        "LT",
                                                        "LU",
                                                        "LV",
                                                        "LY",
                                                        "MA",
                                                        "MC",
                                                        "MD",
                                                        "ME",
                                                        "MF",
                                                        "MG",
                                                        "MH",
                                                        "MK",
                                                        "ML",
                                                        "MM",
                                                        "MN",
                                                        "MO",
                                                        "MP",
                                                        "MQ",
                                                        "MR",
                                                        "MS",
                                                        "MT",
                                                        "MU",
                                                        "MV",
                                                        "MW",
                                                        "MX",
                                                        "MY",
                                                        "MZ",
                                                        "NA",
                                                        "NC",
                                                        "NE",
                                                        "NF",
                                                        "NG",
                                                        "NI",
                                                        "NK",
                                                        "NL",
                                                        false,
                                                        "NP",
                                                        "NR",
                                                        "NU",
                                                        "NZ",
                                                        "OM",
                                                        "PA",
                                                        "PE",
                                                        "PF",
                                                        "PG",
                                                        "PH",
                                                        "PK",
                                                        "PL",
                                                        "PM",
                                                        "PN",
                                                        "PR",
                                                        "PS",
                                                        "PT",
                                                        "PW",
                                                        "PY",
                                                        "QA",
                                                        "RE",
                                                        "RO",
                                                        "RS",
                                                        "RU",
                                                        "RW",
                                                        "SA",
                                                        "SB",
                                                        "SC",
                                                        "SD",
                                                        "SE",
                                                        "SG",
                                                        "SH",
                                                        "SI",
                                                        "SJ",
                                                        "SK",
                                                        "SL",
                                                        "SM",
                                                        "SN",
                                                        "SO",
                                                        "SR",
                                                        "SS",
                                                        "ST",
                                                        "SV",
                                                        "SX",
                                                        "SY",
                                                        "SZ",
                                                        "TC",
                                                        "TD",
                                                        "TF",
                                                        "TG",
                                                        "TH",
                                                        "TI",
                                                        "TJ",
                                                        "TK",
                                                        "TL",
                                                        "TM",
                                                        "TN",
                                                        "TO",
                                                        "TR",
                                                        "TT",
                                                        "TV",
                                                        "TW",
                                                        "TZ",
                                                        "UA",
                                                        "UG",
                                                        "UM",
                                                        "UNCONFIGURED",
                                                        "US",
                                                        "UY",
                                                        "UZ",
                                                        "VA",
                                                        "VC",
                                                        "VE",
                                                        "VG",
                                                        "VI",
                                                        "VN",
                                                        "VU",
                                                        "WF",
                                                        "WS",
                                                        "XK",
                                                        "XX",
                                                        "YE",
                                                        "YT",
                                                        "ZA",
                                                        "ZM",
                                                        "ZW"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apDeploymentModeType": {
                                                    "default": "AP_MODE_DEFAULT",
                                                    "enum": [
                                                        "AP_MODE_DEFAULT",
                                                        "AP_MODE_INDOOR",
                                                        "AP_MODE_OUTDOOR"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apDtlsCtrlPrefEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "apLagEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apMgmtAclNameV4": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "apMgmtAclNameV6": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "apNtpServerInfoKeyType": {
                                                    "default": "AP_NTP_KEY_TYPE_MD5",
                                                    "enum": [
                                                        "AP_NTP_KEY_TYPE_MD5",
                                                        "AP_NTP_KEY_TYPE_SHA1"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apPacketCaptureProfile": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "apProfPpCfgPowerProfileName": {
                                                    "maxLength": 128,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "apRogueDetectionEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "apRogueDetectionMinRssi": {
                                                    "default": -90,
                                                    "maximum": -70,
                                                    "minimum": -128,
                                                    "type": "integer"
                                                },
                                                "apRogueDetectionTransientInterval": {
                                                    "default": 0,
                                                    "type": "integer"
                                                },
                                                "apStatsDnsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsDnsFreq": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsInterfaceEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsInterfaceFreq": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsMemoryEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsMemoryFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsRadioEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsRadioFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsRoutingEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsRoutingFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsSysEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsSystemFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apStatsWlanEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "apStatsWlanFreq": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "apSubModeType": {
                                                    "enum": [
                                                        "AP_SUB_MODE_NONE",
                                                        "FORENSIC_AWIPS_MODE",
                                                        "LOCAL_NETWORK",
                                                        "NON_LOCAL_NETWORK",
                                                        "WIPS_MODE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apTraceProfile": {
                                                    "type": "string"
                                                },
                                                "apTrustsUpstreamDscpEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "apTzConfigMode": {
                                                    "default": "AP_TZ_NOT_CONFIGURED",
                                                    "enum": [
                                                        "AP_TZ_CONTROLLER_TZ",
                                                        "AP_TZ_NOT_CONFIGURED",
                                                        "AP_TZ_UTC_OFFSET"
                                                    ],
                                                    "type": "string"
                                                },
                                                "apTzConfigOffsetHour": {
                                                    "default": 0,
                                                    "maximum": 14,
                                                    "minimum": -12,
                                                    "type": "integer"
                                                },
                                                "apTzConfigOffsetMin": {
                                                    "default": 0,
                                                    "maximum": 59,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "apphostEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "auxClientInterfaceVlanId": {
                                                    "default": 0,
                                                    "maximum": 4094,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "awipsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "awipsForensicEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "bleBeaconAdvpwr": {
                                                    "default": 59,
                                                    "maximum": 100,
                                                    "minimum": 40,
                                                    "type": "integer"
                                                },
                                                "bleBeaconInterval": {
                                                    "default": 1,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "bleScanStateEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "bssidEnableStats": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "bssidNeighborStatsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "bssidNeighborStatsFrequency": {
                                                    "default": 180,
                                                    "maximum": 600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "bssidStatsFrequency": {
                                                    "default": 30,
                                                    "maximum": 180,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "capwapAggregationEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "capwapWindowWindowSize": {
                                                    "default": 1,
                                                    "maximum": 50,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "cdpEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "clientFilterStatsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "clientFilterStatsFrequency": {
                                                    "default": 5,
                                                    "maximum": 3600,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "clientRssiStatsEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "clientRssiStatsInterval": {
                                                    "default": 30,
                                                    "maximum": 300,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "clientStatsEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "clientStatsFrequency": {
                                                    "default": 30,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "configType": {
                                                    "default": "AP_JOIN_PROFILE",
                                                    "enum": [
                                                        "AP_JOIN_PROFILE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "consoleSpeed": {
                                                    "default": "CON_SPEED_NONE",
                                                    "enum": [
                                                        "CON_SPEED_115200",
                                                        "CON_SPEED_9600",
                                                        "CON_SPEED_NONE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "coredumpFlagEnabled": {
                                                    "default": "TFTP_COREDUMP_DISABLE",
                                                    "enum": [
                                                        "TFTP_COREDUMP_COMPRESS",
                                                        "TFTP_COREDUMP_DISABLE",
                                                        "TFTP_COREDUMP_UNCOMPRESS"
                                                    ],
                                                    "type": "string"
                                                },
                                                "corefileName": {
                                                    "default": "default",
                                                    "type": "string"
                                                },
                                                "cpuThreshold": {
                                                    "default": 0,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "dataEncryptionEnabled": {
                                                    "type": "boolean"
                                                },
                                                "deviceVersion": {
                                                    "default": "26.01",
                                                    "type": "string"
                                                },
                                                "dhcpFallbackEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "dhcpServerEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "discoveryTimeout": {
                                                    "default": 10,
                                                    "maximum": 10,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "dot1xEapTypeInfoDot1xEapType": {
                                                    "default": "DOT1X_EAP_FAST",
                                                    "enum": [
                                                        "DOT1X_EAP_FAST",
                                                        "DOT1X_EAP_NONE",
                                                        "DOT1X_EAP_PEAP",
                                                        "DOT1X_EAP_TLS"
                                                    ],
                                                    "type": "string"
                                                },
                                                "dot1xPassword": {
                                                    "type": "string"
                                                },
                                                "dot1xUsername": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "extModuleEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "fallbackEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "fastChannel": {
                                                    "maximum": 4294967295,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "fastHeartBeatTimeout": {
                                                    "default": 0,
                                                    "maximum": 10,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "ftmEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "ftmInitBurstDuration": {
                                                    "default": "ENUM_32MS",
                                                    "enum": [
                                                        "ENUM_128MS",
                                                        "ENUM_16MS",
                                                        "ENUM_1MS",
                                                        "ENUM_250US",
                                                        "ENUM_2MS",
                                                        "ENUM_32MS",
                                                        "ENUM_4MS",
                                                        "ENUM_500US",
                                                        "ENUM_64MS",
                                                        "ENUM_8MS",
                                                        "ANY"
                                                    ],
                                                    "type": "string"
                                                },
                                                "ftmInitBurstSize": {
                                                    "default": 16,
                                                    "maximum": 31,
                                                    "minimum": 2,
                                                    "type": "integer"
                                                },
                                                "gasRateLimitEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "gasRateLimitIntervalMsec": {
                                                    "maximum": 10000,
                                                    "minimum": 100,
                                                    "type": "integer"
                                                },
                                                "gasRateLimitNumReqPerInterval": {
                                                    "maximum": 100,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "grpcEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "heartBeatTimeout": {
                                                    "default": 30,
                                                    "maximum": 30,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "hyperlocationEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "icapAdrIndividualThrottle": {
                                                    "default": 5,
                                                    "maximum": 500,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "icapAdrSummaryFrequency": {
                                                    "default": 5,
                                                    "maximum": 60,
                                                    "minimum": 3,
                                                    "type": "integer"
                                                },
                                                "icapAggrTraceEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "icapAnomalyDetDhcpTimeout": {
                                                    "default": 5,
                                                    "maximum": 120,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "icapFullTraceEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "injectorSwitchMacAddr": {
                                                    "default": "00:00:00:00:00:00",
                                                    "type": "string"
                                                },
                                                "isRfSpectrumSlot2Enabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "jumboMtuEnabled": {
                                                    "type": "boolean"
                                                },
                                                "kernelCoredumpDlimit": {
                                                    "default": 15,
                                                    "maximum": 25,
                                                    "minimum": 15,
                                                    "type": "integer"
                                                },
                                                "kernelCoredumpLimit": {
                                                    "default": 5,
                                                    "maximum": 5,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "kernelCoredumpType": {
                                                    "default": "KERNEL_COREDUMP_TYPE_DISABLED",
                                                    "enum": [
                                                        "KERNEL_COREDUMP_TYPE_DISABLED",
                                                        "KERNEL_COREDUMP_TYPE_FULL",
                                                        "KERNEL_COREDUMP_TYPE_MINI"
                                                    ],
                                                    "type": "string"
                                                },
                                                "lawfulInterceptionEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "lawfulInterceptionTimerInterval": {
                                                    "default": 60,
                                                    "maximum": 600,
                                                    "minimum": 60,
                                                    "type": "integer"
                                                },
                                                "ledFlashMode": {
                                                    "default": "LED_FLASH_MODE_INDEFINITE",
                                                    "enum": [
                                                        "LED_FLASH_MODE_DISABLE",
                                                        "LED_FLASH_MODE_DURATION",
                                                        "LED_FLASH_MODE_INDEFINITE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "ledStateEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "linkLatencyFlagEnabled": {
                                                    "default": "LINK_AUDITING_DISABLE",
                                                    "enum": [
                                                        "LINK_AUDITING_DATA",
                                                        "LINK_AUDITING_DISABLE",
                                                        "LINK_AUDITING_ENABLE",
                                                        "LINK_AUDITING_RESET"
                                                    ],
                                                    "type": "string"
                                                },
                                                "loginCredentialsDot1xPasswordType": {
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
                                                "lscApAuthTypeInfoAuthType": {
                                                    "default": "LSC_AP_AUTH_CAPWAP_DTLS",
                                                    "enum": [
                                                        "LSC_AP_AUTH_BOTH",
                                                        "LSC_AP_AUTH_CAPWAP_DTLS",
                                                        "LSC_AP_AUTH_DOT1X_PORT_AUTH",
                                                        "LSC_AP_AUTH_NONE"
                                                    ],
                                                    "type": "string"
                                                },
                                                "macsecEnabled": {
                                                    "type": "boolean"
                                                },
                                                "macsecPskChain": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "macsecWindowSize": {
                                                    "type": "integer"
                                                },
                                                "max1xSessionLimitPerAp": {
                                                    "default": 0,
                                                    "maximum": 255,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "maxCfgClients": {
                                                    "default": 0,
                                                    "maximum": 1200,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "memThresholdStatsMonitor": {
                                                    "default": 0,
                                                    "maximum": 100,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "meshProfileName": {
                                                    "default": "default-mesh-profile",
                                                    "type": "string"
                                                },
                                                "noProxyList": {
                                                    "type": "string"
                                                },
                                                "nsiPortsStateEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "ntpServerInfoKeyFormat": {
                                                    "default": "AP_NTP_KEY_FORMAT_ASCII",
                                                    "enum": [
                                                        "AP_NTP_KEY_FORMAT_ASCII",
                                                        "AP_NTP_KEY_FORMAT_HEX"
                                                    ],
                                                    "type": "string"
                                                },
                                                "ntpServerInfoKeyId": {
                                                    "default": 1,
                                                    "maximum": 65535,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "ntpServerInfoNtpAddr": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "ntpServerTrustKey": {
                                                    "type": "string"
                                                },
                                                "oeapDataEncryptionEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "oeapLocalNet": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "oeapRogueDetectEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "onboardConfig": {
                                                    "default": "AP_OB_UNICAST",
                                                    "enum": [
                                                        "AP_OB_ALL",
                                                        "AP_OB_DISABLED",
                                                        "AP_OB_UNICAST"
                                                    ],
                                                    "type": "string"
                                                },
                                                "pakRssiThresholdDetection": {
                                                    "default": -100,
                                                    "maximum": -50,
                                                    "minimum": -100,
                                                    "type": "integer"
                                                },
                                                "pakRssiThresholdReset": {
                                                    "default": 8,
                                                    "maximum": 99,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "pakRssiThresholdTrigger": {
                                                    "default": 10,
                                                    "maximum": 100,
                                                    "minimum": 1,
                                                    "type": "integer"
                                                },
                                                "partialTraceEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoAll": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoCiscoAll": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoCiscoNdp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataAll": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataArp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataDhcp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataDhcpv6": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataDns": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataEap": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataIcmp": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoDataIcmpv6": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoMgmtAll": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoMgmtAssoc": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoMgmtAuth": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "partialTraceProtoMgmtProbe": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "persistentSsidBroadcastEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "pmfDeauthEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "powerInjectorSelection": {
                                                    "default": "PWRINJ_UNKNOWN",
                                                    "enum": [
                                                        "PWRINJ_INSTALLED",
                                                        "PWRINJ_OVERRIDE",
                                                        "PWRINJ_UNKNOWN"
                                                    ],
                                                    "type": "string"
                                                },
                                                "powerInjectorStateEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "preStandard8023afSwitchFlag": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "pressSensConfigState": {
                                                    "default": "PRESS_SENSOR_AUTO",
                                                    "enum": [
                                                        "PRESS_SENSOR_AUTO",
                                                        "PRESS_SENSOR_DISABLED",
                                                        "PRESS_SENSOR_ENABLED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "primaryControllerIpAddr": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "primaryControllerName": {
                                                    "type": "string"
                                                },
                                                "primaryDiscoveryTimeout": {
                                                    "default": 120,
                                                    "maximum": 3000,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "primedJoinTimeout": {
                                                    "default": 0,
                                                    "maximum": 43200,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "privateIpDiscoveryEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "provisionalSsidEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "proxyHostname": {
                                                    "type": "string"
                                                },
                                                "proxyPort": {
                                                    "maximum": 65535,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "publicIpDiscoveryEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "qosmapActionFrameEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "radio24GhzReportingInterval": {
                                                    "default": 90,
                                                    "maximum": 90,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "radio5GhzReportingInterval": {
                                                    "default": 90,
                                                    "maximum": 90,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "radioResetEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "radioStatsMonitorAlarmsEnabled": {
                                                    "type": "boolean"
                                                },
                                                "radioStatsMonitorEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "retransmitTimerCount": {
                                                    "default": 5,
                                                    "maximum": 8,
                                                    "minimum": 3,
                                                    "type": "integer"
                                                },
                                                "retransmitTimerInterval": {
                                                    "default": 3,
                                                    "maximum": 5,
                                                    "minimum": 2,
                                                    "type": "integer"
                                                },
                                                "rfSpectrumEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfSpectrumSlot0Enabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfSpectrumSlot1Enabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rfSpectrumSlot3Enabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rlanFastSwitchingEnabled": {
                                                    "type": "boolean"
                                                },
                                                "rogueContainmentAutorate": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rogueContainmentFlexconnect": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rogueDetectionPmfDenial": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rogueDetectionPmfOffchannel": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "rogueDetectionProfileName": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "rogueReportInterval": {
                                                    "default": 10,
                                                    "maximum": 300,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "sampleInterval": {
                                                    "default": 720,
                                                    "maximum": 3600,
                                                    "minimum": 720,
                                                    "type": "integer"
                                                },
                                                "sampleIntvl": {
                                                    "default": 30,
                                                    "maximum": 900,
                                                    "minimum": 2,
                                                    "type": "integer"
                                                },
                                                "secondaryControllerIpAddr": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "secondaryControllerName": {
                                                    "type": "string"
                                                },
                                                "serialConsoleEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "spacesConnCfgToken": {
                                                    "maxLength": 2047,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "spacesConnTokenType": {
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
                                                "sshEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "staticMtuSize": {
                                                    "maximum": 1485,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "statsMonitorEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "statsMonitorStatsInterval": {
                                                    "default": 300,
                                                    "maximum": 900,
                                                    "minimum": 120,
                                                    "type": "integer"
                                                },
                                                "syslogFacilityValue": {
                                                    "default": "FACILITY_KERN",
                                                    "enum": [
                                                        "FACILITY_AUTH",
                                                        "FACILITY_CRON",
                                                        "FACILITY_DAEMON",
                                                        "FACILITY_KERN",
                                                        "FACILITY_LOCAL0",
                                                        "FACILITY_LOCAL1",
                                                        "FACILITY_LOCAL2",
                                                        "FACILITY_LOCAL3",
                                                        "FACILITY_LOCAL4",
                                                        "FACILITY_LOCAL5",
                                                        "FACILITY_LOCAL6",
                                                        "FACILITY_LOCAL7",
                                                        "FACILITY_LPR",
                                                        "FACILITY_MAIL",
                                                        "FACILITY_NEWS",
                                                        "FACILITY_SYS10",
                                                        "FACILITY_SYS11",
                                                        "FACILITY_SYS12",
                                                        "FACILITY_SYS13",
                                                        "FACILITY_SYS14",
                                                        "FACILITY_SYS9",
                                                        "FACILITY_SYSLOG",
                                                        "FACILITY_USER",
                                                        "FACILITY_UUCP"
                                                    ],
                                                    "type": "string"
                                                },
                                                "syslogHostIpAddress": {
                                                    "default": "255.255.255.255",
                                                    "type": "string"
                                                },
                                                "syslogLogLevel": {
                                                    "default": "SYSLOG_LEVEL_INFORMATION",
                                                    "enum": [
                                                        "SYSLOG_LEVEL_ALERT",
                                                        "SYSLOG_LEVEL_CRITICAL",
                                                        "SYSLOG_LEVEL_DEBUG",
                                                        "SYSLOG_LEVEL_EMERGENCY",
                                                        "SYSLOG_LEVEL_ERRORS",
                                                        "SYSLOG_LEVEL_INFORMATION",
                                                        "SYSLOG_LEVEL_NOTIFICATION",
                                                        "SYSLOG_LEVEL_WARNING"
                                                    ],
                                                    "type": "string"
                                                },
                                                "syslogTlsModeEnabled": {
                                                    "type": "boolean"
                                                },
                                                "tcpAdjustMss": {
                                                    "default": 1250,
                                                    "maximum": 1363,
                                                    "minimum": 536,
                                                    "type": "integer"
                                                },
                                                "tcpMssAdjustEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "telnetEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "tftpDowngradeFilename": {
                                                    "type": "string"
                                                },
                                                "tftpDowngradeIpAddress": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "tftpServerIpAddress": {
                                                    "default": "0.0.0.0",
                                                    "type": "string"
                                                },
                                                "trafficDistributionInterval": {
                                                    "default": 300,
                                                    "maximum": 3600,
                                                    "minimum": 30,
                                                    "type": "integer"
                                                },
                                                "trafficDistributionStatus": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "trapRetxTime": {
                                                    "default": 0,
                                                    "maximum": 65535,
                                                    "minimum": 0,
                                                    "type": "integer"
                                                },
                                                "trustKeyType": {
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
                                                "tunnelPreferredMode": {
                                                    "default": "PREFERRED_MODE_UNCONFIG",
                                                    "enum": [
                                                        "PREFERRED_MODE_IPV4",
                                                        "PREFERRED_MODE_IPV6",
                                                        "PREFERRED_MODE_UNCONFIG"
                                                    ],
                                                    "type": "string"
                                                },
                                                "tzConfigEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "udpLiteIpv6CapwapChecksumType": {
                                                    "default": "UDPLITE_CHECKSUM_DISABLED",
                                                    "enum": [
                                                        "UDPLITE_CHECKSUM_DISABLED",
                                                        "UDPLITE_CHECKSUM_ENABLED",
                                                        "UDPLITE_CHECKSUM_UNCONFIGURED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "usbModuleEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "userMgmtPassword": {
                                                    "type": "string"
                                                },
                                                "userMgmtPasswordCryptType": {
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
                                                "userMgmtSecret": {
                                                    "type": "string"
                                                },
                                                "userMgmtSecretType": {
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
                                                "userMgmtUsername": {
                                                    "maxLength": 32,
                                                    "minLength": 0,
                                                    "type": "string"
                                                },
                                                "uwbEnabled": {
                                                    "default": true,
                                                    "type": "boolean"
                                                },
                                                "uwbInitBurstDuration": {
                                                    "default": 10,
                                                    "maximum": 30,
                                                    "minimum": 5,
                                                    "type": "integer"
                                                },
                                                "uwbInitBurstSize": {
                                                    "default": 32,
                                                    "maximum": 100,
                                                    "minimum": 10,
                                                    "type": "integer"
                                                },
                                                "uwbWayFindingBlockDuration": {
                                                    "default": "WF_BLK_DUR_1SEC",
                                                    "enum": [
                                                        "WF_BLK_DUR_1SEC",
                                                        "WF_BLK_DUR_500MS"
                                                    ],
                                                    "type": "string"
                                                },
                                                "uwbWayFindingEnabled": {
                                                    "default": false,
                                                    "type": "boolean"
                                                },
                                                "weakRssi": {
                                                    "default": -60,
                                                    "maximum": -10,
                                                    "minimum": -90,
                                                    "type": "integer"
                                                }
                                            },
                                            "required": [
                                                "apCfgProfileName",
                                                "deviceVersion"
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
