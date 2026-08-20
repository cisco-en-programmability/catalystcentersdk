"""Cisco Catalyst Center GetIntendedPortConfigurations data model.

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


class JSONSchemaValidatorD1F7Bd92B654Ee8A8549F868B7225F:
    """GetIntendedPortConfigurations request schema definition."""

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
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "accessSessionControlDirection": {
                                                        "enum": [
                                                            "BOTH",
                                                            "IN"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "accessSessionHostModeCfg": {
                                                        "enum": [
                                                            "SINGLE_HOST",
                                                            "MULTI_AUTH",
                                                            "MULTI_HOST",
                                                            "MULTI_DOMAIN"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "accessSessionHostModeEnum": {
                                                        "enum": [
                                                            "MULTI_AUTH",
                                                            "SINGLE_HOST",
                                                            "MULTI_HOST",
                                                            "MULTI_DOMAIN"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "accessSessionPortControl": {
                                                        "enum": [
                                                            "FORCE_AUTHORIZED",
                                                            "FORCE_UNAUTHORIZED",
                                                            "AUTO"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "accessVlanId": {
                                                        "maximum": 4094,
                                                        "minimum": 1,
                                                        "type": "integer"
                                                    },
                                                    "authControlDirection": {
                                                        "enum": [
                                                            "BOTH",
                                                            "IN"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "authHostMode": {
                                                        "enum": [
                                                            "SINGLE_HOST",
                                                            "MULTI_AUTH",
                                                            "MULTI_HOST",
                                                            "MULTI_DOMAIN"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "authInactivityTimer": {
                                                        "maximum": 65535,
                                                        "minimum": 0,
                                                        "type": "integer"
                                                    },
                                                    "authPortControl": {
                                                        "enum": [
                                                            "FORCE_AUTHORIZED",
                                                            "FORCE_UNAUTHORIZED",
                                                            "AUTO"
                                                        ],
                                                        "type": "string"
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
                                                        "minimum": 0,
                                                        "type": "integer"
                                                    },
                                                    "bfdTemplate": {
                                                        "maxLength": 255,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "channelGroupMode": {
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
                                                        "minimum": 0,
                                                        "type": "integer"
                                                    },
                                                    "channelProtocol": {
                                                        "enum": [
                                                            "LACP",
                                                            "PAGP",
                                                            "NONE"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "clientPdPreName": {
                                                        "maxLength": 200,
                                                        "minLength": 0,
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
                                                                            "minLength": 0,
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
                                                        "minimum": 0,
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
                                                                        "ipAddress"
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
                                                                        "ipV6Address"
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
                                                                        "ipV6Address"
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
                                                                            "type": "string"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "ipV6Address"
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
                                                                            "minLength": 0,
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
                                                                "maxItems": 2,
                                                                "minItems": 0,
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
                                                        "type": "boolean"
                                                    },
                                                    "isAuthOpenEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isBfdEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isBfdIntervalEnabled": {},
                                                    "isCdpEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isCdpTlvAppEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isDeviceTrackingEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isDhcpEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isDhcpSnoopingTrustEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isDot1xMabOrderEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isDot1xMabPriorityEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isIpV6AutoconfigEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isIpV6DhcpEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isIpV6Enabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isMabEapEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isMabEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isMabWebauthPriority": {
                                                        "type": "boolean"
                                                    },
                                                    "isPeriodicAuthEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isPortSecurityEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isReauthTimerFromServerEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isShutdown": {
                                                        "type": "boolean"
                                                    },
                                                    "isStaticTrustedEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isStormControlShutdownEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isStormControlTrapEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isSwitchportEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isSwitchportNonegotiate": {
                                                        "type": "boolean"
                                                    },
                                                    "lacpPortPriority": {
                                                        "maximum": 65535,
                                                        "minimum": -1,
                                                        "type": "integer"
                                                    },
                                                    "lacpRate": {
                                                        "enum": [
                                                            "FAST",
                                                            "NORMAL"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "lldpAdminStatus": {
                                                        "enum": [
                                                            "TRANSMIT_ONLY",
                                                            "RECEIVE_ONLY",
                                                            "TRANSMIT_AND_RECEIVE",
                                                            "DISABLED"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "mode": {
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
                                                        "maximum": 4094,
                                                        "minimum": 1,
                                                        "type": "integer"
                                                    },
                                                    "portSecurityAgingTime": {
                                                        "maximum": 1440,
                                                        "minimum": 0,
                                                        "type": "integer"
                                                    },
                                                    "portSecurityAgingType": {
                                                        "enum": [
                                                            "INACTIVITY",
                                                            "ABSOLUTE"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "portSecurityViolation": {
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
                                                                        "ipAddress",
                                                                        "mask"
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
                                                        "minimum": 0,
                                                        "type": "integer"
                                                    },
                                                    "stpBpduGuard": {
                                                        "enum": [
                                                            "ENABLE",
                                                            "DISABLE",
                                                            "NONE"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "stpBpdufilterStatus": {
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
                                                        "multipleOf": 16,
                                                        "type": "integer"
                                                    },
                                                    "stpPortfastMode": {
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
                                                        "minimum": 0,
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
                                                        "minimum": 0,
                                                        "type": "integer"
                                                    },
                                                    "bfdTemplate": {
                                                        "maxLength": 32,
                                                        "minLength": 0,
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
                                                                        "ipAddress"
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
                                                        "minLength": 0,
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
                                                                        "ipV6Address"
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
                                                                            "maxLength": 255,
                                                                            "minLength": 0,
                                                                            "type": "string"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "ipV6Address"
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
                                                                        "ipV6Prefix"
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
                                                                            "minLength": 0,
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
                                                                "maxItems": 2,
                                                                "minItems": 0,
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "isBfdEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isBfdIntervalEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isIpV4DhcpEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isIpV4RedirectsEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isIpV4UnreachablesEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isIpV6AutoconfigEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isIpV6DhcpEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isIpV6Enabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isIpV6RedirectsEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isIpv6RedirectsEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isLacpFastSwitchoverEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isProxyArpEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isRapidCommitEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isShutdown": {
                                                        "type": "boolean"
                                                    },
                                                    "isSwitchportEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isSwitchportNonegotiate": {
                                                        "type": "boolean"
                                                    },
                                                    "lacpMaxBundle": {
                                                        "maximum": 8,
                                                        "minimum": 0,
                                                        "type": "integer"
                                                    },
                                                    "macAddress": {
                                                        "type": "string"
                                                    },
                                                    "minLinks": {
                                                        "maximum": 8,
                                                        "minimum": 0,
                                                        "type": "integer"
                                                    },
                                                    "mode": {
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
                                                                        "ipAddress",
                                                                        "mask"
                                                                    ],
                                                                    "type": "object"
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "stpBpduGuard": {
                                                        "enum": [
                                                            "ENABLE",
                                                            "DISABLE",
                                                            "NONE"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "stpBpdufilterStatus": {
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
                                                        "enum": [
                                                            "LOOP",
                                                            "NONE",
                                                            "ROOT"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "stpPortPriority": {
                                                        "maximum": 240,
                                                        "minimum": -1,
                                                        "type": "integer"
                                                    },
                                                    "stpPortfastMode": {
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
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "trunkAllowedVlansMode": {
                                                        "enum": [
                                                            "NONE",
                                                            "ALL",
                                                            "VLANIDS"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "voiceVlanId": {
                                                        "maximum": 4094,
                                                        "minimum": 0,
                                                        "type": "integer"
                                                    },
                                                    "vrfName": {
                                                        "maxLength": 32,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "portchannelNumber"
                                                ],
                                                "type": "object"
                                            },
                                            "maxItems": 512,
                                            "minItems": 0,
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
