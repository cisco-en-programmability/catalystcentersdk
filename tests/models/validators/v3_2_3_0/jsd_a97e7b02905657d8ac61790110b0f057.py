"""Cisco Catalyst Center GetDeployedPortFeatureConfigurations data model.

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


class JSONSchemaValidatorA97E7B02905657D8Ac61790110B0F057:
    """GetDeployedPortFeatureConfigurations request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "properties": {
                                "ethernetInterfaceConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "accessList": {
                                                        "maxLength": 230,
                                                        "minLength": 1,
                                                        "type": "string"
                                                    },
                                                    "accessSessionControlDirection": {
                                                        "default": "BOTH",
                                                        "enum": [
                                                            "BOTH",
                                                            "IN"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "accessSessionHostModeCfg": {
                                                        "default": "MULTI_AUTH",
                                                        "enum": [
                                                            "SINGLE_HOST",
                                                            "MULTI_AUTH",
                                                            "MULTI_HOST",
                                                            "MULTI_DOMAIN"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "accessSessionHostModeEnum": {
                                                        "default": "MULTI_AUTH",
                                                        "enum": [
                                                            "MULTI_AUTH",
                                                            "SINGLE_HOST",
                                                            "MULTI_HOST",
                                                            "MULTI_DOMAIN"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "accessSessionPortControl": {
                                                        "default": "FORCE_AUTHORIZED",
                                                        "enum": [
                                                            "FORCE_AUTHORIZED",
                                                            "FORCE_UNAUTHORIZED",
                                                            "AUTO"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "accessVlanId": {
                                                        "default": 1,
                                                        "maximum": 4094,
                                                        "minimum": 1,
                                                        "type": "integer"
                                                    },
                                                    "authControlDirection": {
                                                        "default": "BOTH",
                                                        "enum": [
                                                            "BOTH",
                                                            "IN"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "authHostMode": {
                                                        "default": "SINGLE_HOST",
                                                        "enum": [
                                                            "SINGLE_HOST",
                                                            "MULTI_AUTH",
                                                            "MULTI_HOST",
                                                            "MULTI_DOMAIN"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "authInactivityTimer": {
                                                        "default": 0,
                                                        "maximum": 65535,
                                                        "minimum": 0,
                                                        "type": "integer"
                                                    },
                                                    "authPortControl": {
                                                        "default": "FORCE_AUTHORIZED",
                                                        "type": "string"
                                                    },
                                                    "bfdIntervalMultiplier": {
                                                        "maximum": 50,
                                                        "minimum": 3,
                                                        "type": "integer"
                                                    },
                                                    "bfdMinRxInterval": {
                                                        "maximum": 9999,
                                                        "minimum": 50,
                                                        "type": "integer"
                                                    },
                                                    "bfdMinTxInterval": {
                                                        "maximum": 9999,
                                                        "minimum": 50,
                                                        "type": "integer"
                                                    },
                                                    "bfdTemplate": {
                                                        "maxLength": 255,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "channelGroupMode": {
                                                        "default": "NONE",
                                                        "enum": [
                                                            "ACTIVE",
                                                            "AUTO",
                                                            "DESIRABLE",
                                                            true,
                                                            "PASSIVE",
                                                            "NONE"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "channelGroupNumber": {
                                                        "maximum": 512,
                                                        "minimum": 1,
                                                        "type": "integer"
                                                    },
                                                    "channelProtocol": {
                                                        "default": "NONE",
                                                        "enum": [
                                                            "LACP",
                                                            "PAGP",
                                                            "NONE"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "clientPdPreName": {
                                                        "maxLength": 200,
                                                        "minLength": 1,
                                                        "type": "string"
                                                    },
                                                    "configType": {
                                                        "default": "ETHERNET_INTERFACE_CONFIG",
                                                        "enum": [
                                                            "ETHERNET_INTERFACE_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "description":
                 {
                                                        "maxLength": 200,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "deviceTrackingPolicy": {
                                                        "properties": {
                                                            "configType": {
                                                                "default": "SET",
                                                                "enum": [
                                                                    "SET"
                                                                ],
                                                                "type": "string"
                                                            },
                                                            "items": {
                                                                "items": {
                                                                    "properties": {
                                                                        "configType": {
                                                                            "default": "ETHERNET_INTERFACE_DEVICE_TRACKING_POLICY_CONFIG",
                                                                            "enum": [
                                                                                "ETHERNET_INTERFACE_DEVICE_TRACKING_POLICY_CONFIG"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "deviceTrackingPolicy": {
                                                                            "maxLength": 64,
                                                                            "minLength": 1,
                                                                            "type": "string"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "deviceTrackingPolicy"
                                                                    ],
                                                                    "type": "object"
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "dhcpSnoopingLimitRate": {
                                                        "maximum": 2048,
                                                        "minimum": 1,
                                                        "type": "integer"
                                                    },
                                                    "direction": {
                                                        "enum": [
                                                            "IN",
                                                            "OUT"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "helperAddresses": {
                                                        "properties": {
                                                            "configType": {
                                                                "default": "SET",
                                                                "enum": [
                                                                    "SET"
                                                                ],
                                                                "type": "string"
                                                            },
                                                            "items": {
                                                                "items": {
                                                                    "properties": {
                                                                        "configType": {
                                                                            "default": "ETHERNET_INTERFACE_HELPER_ADDRESS",
                                                                            "enum": [
                                                                                "ETHERNET_INTERFACE_HELPER_ADDRESS"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "ipAddress": {
                                                                            "type": "string"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "configType"
                                                                    ],
                                                                    "type": "object"
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "interfaceName": {
                                                        "minLength": 1,
                                                        "type": "string"
                                                    },
                                                    "ipDhcpHostname": {
                                                        "maxLength": 255,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "ipV4InboundAclName": {
                                                        "maxLength": 255,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "ipV4OutboundAclName": {
                                                        "maxLength": 255,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "ipV4VrfName": {
                                                        "maxLength": 255,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "ipV6DhcpRelayDestination": {
                                                        "properties": {
                                                            "configType": {
                                                                "default": "SET",
                                                                "enum": [
                                                                    "SET"
                                                                ],
                                                                "type": "string"
                                                            },
                                                            "items": {
                                                                "items": {
                                                                    "properties": {
                                                                        "configType": {
                                                                            "default": "ETHERNET_INTERFACE_IPV6_DHCP_RELAY_DEST_ADDRESS",
                                                                            "enum": [
                                                                                "ETHERNET_INTERFACE_IPV6_DHCP_RELAY_DEST_ADDRESS"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "ipV6Address": {
                                                                            "type": "string"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "configType"
                                                                    ],
                                                                    "type": "object"
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "ipV6DhcpRelayDestinationGlobal": {
                                                        "properties": {
                                                            "configType": {
                                                                "default": "SET",
                                                                "enum": [
                                                                    "SET"
                                                                ],
                                                                "type": "string"
                                                            },
                                                            "items": {
                                                                "items": {
                                                                    "properties": {
                                                                        "configType": {
                                                                            "default": "ETHERNET_INTERFACE_IPV6_DHCP_RELAY_DEST_GLOBAL",
                                                                            "enum": [
                                                                                "ETHERNET_INTERFACE_IPV6_DHCP_RELAY_DEST_GLOBAL"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "ipV6Address": {
                                                                            "type": "string"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "configType"
                                                                    ],
                                                                    "type": "object"
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "ipV6LinkLocalAddress": {
                                                        "type": "string"
                                                    },
                                                    "ipV6PrefixList": {
                                                        "properties": {
                                                            "configType": {
                                                                "default": "SET",
                                                                "enum": [
                                                                    "SET"
                                                                ],
                                                                "type": "string"
                                                            },
                                                            "items": {
                                                                "items": {
                                                                    "properties": {
                                                                        "configType": {
                                                                            "default": "ETHERNET_INTERFACE_IPV6_PREFIX_LIST",
                                                                            "enum": [
                                                                                "ETHERNET_INTERFACE_IPV6_PREFIX_LIST"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "ipV6Address": {
                                                                            "maxLength": 255,
                                                                            "minLength": 0,
                                                                            "type": "string"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "configType"
                                                                    ],
                                                                    "type": "object"
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "ipV6TrafficFilter": {
                                                        "properties": {
                                                            "configType": {
                                                                "default": "SET",
                                                                "enum": [
                                                                    "SET"
                                                                ],
                                                                "type": "string"
                                                            },
                                                            "items": {
                                                                "items": {
                                                                    "properties": {
                                                                        "accessList": {
                                                                            "maxLength": 230,
                                                                            "minLength": 1,
                                                                            "type": "string"
                                                                        },
                                                                        "configType": {
                                                                            "default": "ETHERNET_INTERFACE_IPV6_TRAFFIC_FILTER",
                                                                            "enum": [
                                                                                "ETHERNET_INTERFACE_IPV6_TRAFFIC_FILTER"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "direction": {
                                                                            "enum": [
                                                                                "IN",
                                                                                "OUT"
                                                                            ],
                                                                            "type": "string"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "direction"
                                                                    ],
                                                                    "type": "object"
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "isAccessSessionClosed": {
                                                        "type": "boolean"
                                                    },
                                                    "isArpInspectionTrustEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isAuthInactivityTimerFromServerEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isAuthOpenEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isBfdEnabled": {
                                                        "default": true,
                                                        "type": "boolean"
                                                    },
                                                    "isBfdIntervalEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isCdpEnabled": {
                                                        "default": true,
                                                        "type": "boolean"
                                                    },
                                                    "isCdpTlvAppEnabled": {
                                                        "default": true,
                                                        "type": "boolean"
                                                    },
                                                    "isDeviceTrackingEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isDhcpEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isDhcpSnoopingTrustEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isDot1xMabOrderEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isDot1xMabPriorityEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isIpV6AutoconfigEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isIpV6DhcpEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isIpV6Enabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isMabEapEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isMabEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isMabWebauthPriority": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isPeriodicAuthEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isPortSecurityEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isReauthTimerFromServerEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isShutdown": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isStaticTrustedEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isStormControlShutdownEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isStormControlTrapEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isSwitchportEnabled": {
                                                        "default": true,
                                                        "type": "boolean"
                                                    },
                                                    "isSwitchportNonegotiate": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "lacpPortPriority": {
                                                        "maximum": 65535,
                                                        "minimum": 0,
                                                        "type": "integer"
                                                    },
                                                    "lacpRate": {
                                                        "default": "NORMAL",
                                                        "enum": [
                                                            "FAST",
                                                            "NORMAL"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "lldpAdminStatus": {
                                                        "default": "TRANSMIT_AND_RECEIVE",
                                                        "enum": [
                                                            "TRANSMIT_ONLY",
                                                            "RECEIVE_ONLY",
                                                            "TRANSMIT_AND_RECEIVE",
                                                            "DISABLED"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "mode": {
                                                        "default": "DYNAMIC_AUTO",
                                                        "enum": [
                                                            "ACCESS",
                                                            "TRUNK",
                                                            "DYNAMIC_AUTO",
                                                            "DYNAMIC_DESIRABLE",
                                                            "DOT1Q_TUNNEL"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "nativeVlanId": {
                                                        "default": 1,
                                                        "maximum": 4094,
                                                        "minimum": 1,
                                                        "type": "integer"
                                                    },
                                                    "portSecurityAgingTime": {
                                                        "maximum": 1440,
                                                        "minimum": 1,
                                                        "type": "integer"
                                                    },
                                                    "portSecurityAgingType": {
                                                        "default": "ABSOLUTE",
                                                        "enum": [
                                                            "INACTIVITY",
                                                            "ABSOLUTE"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "portSecurityViolation": {
                                                        "default": "SHUTDOWN_VLAN",
                                                        "enum": [
                                                            "SHUTDOWN_VLAN",
                                                            "PROTECT",
                                                            "RESTRICT",
                                                            "REPORT"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "primaryIpAddress": {
                                                        "type": "string"
                                                    },
                                                    "primaryIpMask": {
                                                        "type": "string"
                                                    },
                                                    "reauthTimer": {
                                                        "default": 3600,
                                                        "maximum": 1073741823,
                                                        "minimum": 1,
                                                        "type": "integer"
                                                    },
                                                    "secondaryAddress": {
                                                        "properties": {
                                                            "configType": {
                                                                "default": "SET",
                                                                "enum": [
                                                                    "SET"
                                                                ],
                                                                "type": "string"
                                                            },
                                                            "items": {
                                                                "items": {
                                                                    "properties": {
                                                                        "configType": {
                                                                            "default": "ETHERNET_INTERFACE_SECONDARY_ADDRESS",
                                                                            "enum": [
                                                                                "ETHERNET_INTERFACE_SECONDARY_ADDRESS"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "ipAddress": {
                                                                            "type": "string"
                                                                        },
                                                                        "mask": {
                                                                            "type": "string"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "configType"
                                                                    ],
                                                                    "type": "object"
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "staticSgt": {
                                                        "maximum": 65521,
                                                        "minimum": 2,
                                                        "type": "integer"
                                                    },
                                                    "stpBpduGuard": {
                                                        "default": "NONE",
                                                        "enum": [
                                                            "ENABLE",
                                                            "DISABLE",
                                                            "NONE"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "stpBpdufilterStatus": {
                                                        "default": "NONE",
                                                        "enum": [
                                                            "DISABLE",
                                                            "ENABLE",
                                                            "NONE"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "stpCost": {
                                                        "maximum": 200000000,
                                                        "minimum": 0,
                                                        "type": "integer"
                                                    },
                                                    "stpGuardMode": {
                                                        "default": "NONE",
                                                        "enum": [
                                                            "LOOP",
                                                            "NONE",
                                                            "ROOT"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "stpPortPriority": {
                                                        "default": 128,
                                                        "maximum": 240,
                                                        "minimum": 0,
                                                        "multipleOf": 16,
                                                        "type": "integer"
                                                    },
                                                    "stpPortfastMode": {
                                                        "default": "NONE",
                                                        "enum": [
                                                            "ENABLE",
                                                            "DISABLE",
                                                            "EDGE",
                                                            "EDGE_TRUNK",
                                                            "NETWORK",
                                                            "TRUNK",
                                                            "NONE"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "trunkAllowedVlanIds": {
                                                        "maxLength": 224,
                                                        "type": "string"
                                                    },
                                                    "trunkAllowedVlansMode": {
                                                        "default": "ALL",
                                                        "enum": [
                                                            "NONE",
                                                            "ALL",
                                                            "VLANIDS"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "trunkVlans": {
                                                        "maxLength": 255,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "txPeriod": {
                                                        "default": 30,
                                                        "maximum": 65535,
                                                        "minimum": 1,
                                                        "type": "integer"
                                                    },
                                                    "udldMode": {
                                                        "enum": [
                                                            "AGGRESS_ALERT",
                                                            "AGGRESSIVE",
                                                            "ALERT",
                                                            "DISABLE",
                                                            "ENABLE"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "voiceVlanId": {
                                                        "maximum": 4094,
                                                        "minimum": 1,
                                                        "type": "integer"
                                                    },
                                                    "vrfName": {
                                                        "maxLength": 255,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "interfaceName"
                                                ],
                                                "type": "object"
                                            },
                                            "type": "array"
                                        }
                                    },
                                    "required": [
                                        "items"
                                    ],
                                    "type": "object"
                                },
                                "portChannelInterfaceConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "accessVlanId": {
                                                        "default": 1,
                                                        "maximum": 4094,
                                                        "minimum": 1,
                                                        "type": "integer"
                                                    },
                                                    "bfdIntervalMultiplier": {
                                                        "maximum": 50,
                                                        "minimum": 3,
                                                        "type": "integer"
                                                    },
                                                    "bfdMinRxInterval": {
                                                        "maximum": 9999,
                                                        "minimum": 250,
                                                        "type": "integer"
                                                    },
                                                    "bfdMinTxInterval": {
                                                        "maximum": 9999,
                                                        "minimum": 250,
                                                        "type": "integer"
                                                    },
                                                    "bfdTemplate": {
                                                        "maxLength": 32,
                                                        "minLength": 1,
                                                        "type": "string"
                                                    },
                                                    "configType": {
                                                        "default": "PORT_CHANNEL_INTERFACE_CONFIG",
                                                        "enum": [
                                                            "PORT_CHANNEL_INTERFACE_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "description":
                 {
                                                        "maxLength": 200,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "helperAddress": {
                                                        "properties": {
                                                            "configType": {
                                                                "default": "SET",
                                                                "enum": [
                                                                    "SET"
                                                                ],
                                                                "type": "string"
                                                            },
                                                            "items": {
                                                                "items": {
                                                                    "properties": {
                                                                        "configType": {
                                                                            "default": "PORT_CHANNEL_HELPER_ADDRESS",
                                                                            "enum": [
                                                                                "PORT_CHANNEL_HELPER_ADDRESS"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "ipAddress": {
                                                                            "maxLength": 255,
                                                                            "minLength": 0,
                                                                            "type": "string"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "configType"
                                                                    ],
                                                                    "type": "object"
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "ipV4InboundAclName": {
                                                        "maxLength": 64,
                                                        "minLength": 1,
                                                        "type": "string"
                                                    },
                                                    "ipV4Mask": {
                                                        "type": "string"
                                                    },
                                                    "ipV4OutboundAclName": {
                                                        "maxLength": 255,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "ipV4VrfName": {
                                                        "maxLength": 32,
                                                        "minLength": 1,
                                                        "type": "string"
                                                    },
                                                    "ipV6DhcpRelayDestination": {
                                                        "properties": {
                                                            "configType": {
                                                                "default": "SET",
                                                                "enum": [
                                                                    "SET"
                                                                ],
                                                                "type": "string"
                                                            },
                                                            "items": {
                                                                "items": {
                                                                    "properties": {
                                                                        "configType": {
                                                                            "default": "PORT_CHANNEL_IPV6_DHCP_RELAY_DEST_ADDRESS",
                                                                            "enum": [
                                                                                "PORT_CHANNEL_IPV6_DHCP_RELAY_DEST_ADDRESS"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "ipV6Address": {
                                                                            "type": "string"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "configType"
                                                                    ],
                                                                    "type": "object"
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "ipV6DhcpRelayDestinationGlobal": {
                                                        "properties": {
                                                            "configType": {
                                                                "default": "SET",
                                                                "enum": [
                                                                    "SET"
                                                                ],
                                                                "type": "string"
                                                            },
                                                            "items": {
                                                                "items": {
                                                                    "properties": {
                                                                        "configType": {
                                                                            "default": "PORT_CHANNEL_IPV6_DHCP_RELAY_DEST_GLOBAL",
                                                                            "enum": [
                                                                                "PORT_CHANNEL_IPV6_DHCP_RELAY_DEST_GLOBAL"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "ipV6Address": {
                                                                            "type": "string"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "configType"
                                                                    ],
                                                                    "type": "object"
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "ipV6LinkLocalAddress": {
                                                        "type": "string"
                                                    },
                                                    "ipV6PrefixList": {
                                                        "properties": {
                                                            "configType": {
                                                                "default": "SET",
                                                                "enum": [
                                                                    "SET"
                                                                ],
                                                                "type": "string"
                                                            },
                                                            "items": {
                                                                "items": {
                                                                    "properties": {
                                                                        "configType": {
                                                                            "default": "PORT_CHANNEL_IPV6_PREFIX_LIST",
                                                                            "enum": [
                                                                                "PORT_CHANNEL_IPV6_PREFIX_LIST"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "ipV6Prefix": {
                                                                            "maxLength": 255,
                                                                            "minLength": 0,
                                                                            "type": "string"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "configType"
                                                                    ],
                                                                    "type": "object"
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "ipV6TrafficFilter": {
                                                        "properties": {
                                                            "configType": {
                                                                "default": "SET",
                                                                "enum": [
                                                                    "SET"
                                                                ],
                                                                "type": "string"
                                                            },
                                                            "items": {
                                                                "items": {
                                                                    "properties": {
                                                                        "actionList": {
                                                                            "maxLength": 64,
                                                                            "minLength": 1,
                                                                            "type": "string"
                                                                        },
                                                                        "configType": {
                                                                            "default": "PORT_CHANNEL_IPV6_TRAFFIC_FILTER_CONFIG",
                                                                            "enum": [
                                                                                "PORT_CHANNEL_IPV6_TRAFFIC_FILTER_CONFIG"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "direction": {
                                                                            "enum": [
                                                                                "IN",
                                                                                "OUT"
                                                                            ],
                                                                            "type": "string"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "direction"
                                                                    ],
                                                                    "type": "object"
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "isBfdEnabled": {
                                                        "default": true,
                                                        "type": "boolean"
                                                    },
                                                    "isBfdIntervalEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isIpV4DhcpEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isIpV4RedirectsEnabled": {
                                                        "default": true,
                                                        "type": "boolean"
                                                    },
                                                    "isIpV4UnreachablesEnabled": {
                                                        "default": true,
                                                        "type": "boolean"
                                                    },
                                                    "isIpV6AutoconfigEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isIpV6DhcpEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isIpV6Enabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isIpV6RedirectsEnabled": {
                                                        "default": true,
                                                        "type": "boolean"
                                                    },
                                                    "isLacpFastSwitchoverEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isProxyArpEnabled": {
                                                        "default": true,
                                                        "type": "boolean"
                                                    },
                                                    "isRapidCommitEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isShutdown": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isSwitchportEnabled": {
                                                        "default": true,
                                                        "type": "boolean"
                                                    },
                                                    "isSwitchportNonegotiate": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "lacpMaxBundle": {
                                                        "maximum": 8,
                                                        "minimum": 1,
                                                        "type": "integer"
                                                    },
                                                    "macAddress": {
                                                        "type": "string"
                                                    },
                                                    "minLinks": {
                                                        "maximum": 8,
                                                        "minimum": 2,
                                                        "type": "integer"
                                                    },
                                                    "mode": {
                                                        "default": "DYNAMIC_AUTO",
                                                        "enum": [
                                                            "ACCESS",
                                                            "TRUNK",
                                                            "DYNAMIC_AUTO",
                                                            "DYNAMIC_DESIRABLE",
                                                            "DOT1Q_TUNNEL"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "nativeVlanId": {
                                                        "default": 1,
                                                        "maximum": 4094,
                                                        "minimum": 1,
                                                        "type": "integer"
                                                    },
                                                    "portchannelNumber": {
                                                        "maximum": 512,
                                                        "minimum": 1,
                                                        "type": "integer"
                                                    },
                                                    "primaryAddress": {
                                                        "type": "string"
                                                    },
                                                    "secondaryAddress": {
                                                        "properties": {
                                                            "configType": {
                                                                "default": "SET",
                                                                "enum": [
                                                                    "SET"
                                                                ],
                                                                "type": "string"
                                                            },
                                                            "items": {
                                                                "items": {
                                                                    "properties": {
                                                                        "configType": {
                                                                            "default": "PORT_CHANNEL_SECONDARY_ADDRESS",
                                                                            "enum": [
                                                                                "PORT_CHANNEL_SECONDARY_ADDRESS"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "ipAddress": {
                                                                            "type": "string"
                                                                        },
                                                                        "mask": {
                                                                            "type": "string"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "configType"
                                                                    ],
                                                                    "type": "object"
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "stpBpduGuard": {
                                                        "default": "NONE",
                                                        "enum": [
                                                            "ENABLE",
                                                            "DISABLE",
                                                            "NONE"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "stpBpdufilterStatus": {
                                                        "default": "NONE",
                                                        "enum": [
                                                            "DISABLE",
                                                            "ENABLE",
                                                            "NONE"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "stpCost": {
                                                        "maximum": 200000000,
                                                        "minimum": 1,
                                                        "type": "integer"
                                                    },
                                                    "stpGuardMode": {
                                                        "default": "NONE",
                                                        "enum": [
                                                            "LOOP",
                                                            "NONE",
                                                            "ROOT"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "stpPortPriority": {
                                                        "maximum": 240,
                                                        "minimum": 0,
                                                        "type": "integer"
                                                    },
                                                    "stpPortfastMode": {
                                                        "default": "NONE",
                                                        "enum": [
                                                            "ENABLE",
                                                            "DISABLE",
                                                            "EDGE",
                                                            "NETWORK",
                                                            "TRUNK",
                                                            "EDGE_TRUNK",
                                                            "NONE"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "trunkAllowedVlanIds": {
                                                        "maxLength": 224,
                                                        "minLength": 1,
                                                        "type": "string"
                                                    },
                                                    "trunkAllowedVlansMode": {
                                                        "default": "ALL",
                                                        "enum": [
                                                            "NONE",
                                                            "ALL",
                                                            "VLANIDS"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "voiceVlanId": {
                                                        "maximum": 4094,
                                                        "minimum": 1,
                                                        "type": "integer"
                                                    },
                                                    "vrfName": {
                                                        "maxLength": 32,
                                                        "minLength": 1,
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "portchannelNumber"
                                                ],
                                                "type": "object"
                                            },
                                            "maxItems": 1,
                                            "minItems": 1,
                                            "type": "array"
                                        }
                                    },
                                    "required": [
                                        "items"
                                    ],
                                    "type": "object"
                                }
                            },
                            "type": "object"
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
