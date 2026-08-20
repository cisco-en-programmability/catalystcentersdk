"""Cisco Catalyst Center GetIntendedSecurityConfigurations data model.

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


class JSONSchemaValidatorCa61C56055259Bd48E61F6Bbeac29:
    """GetIntendedSecurityConfigurations request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "properties": {
                                "arpInspectionConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "ARP_INSPECTION_VLAN_CONFIG",
                                                        "enum": [
                                                            "ARP_INSPECTION_VLAN_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "vlanId": {
                                                        "maximum": 4094,
                                                        "minimum": 1,
                                                        "type": "integer"
                                                    }
                                                },
                                                "required": [
                                                    "vlanId"
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
                                },
                                "ctsConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "authorizationList": {
                                                        "maxLength": 64,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "configType": {
                                                        "default": "CTS_CONFIG",
                                                        "enum": [
                                                            "CTS_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "ctsSgt": {
                                                        "maximum": 65519,
                                                        "minimum": 0,
                                                        "type": "integer"
                                                    },
                                                    "defaultSxpPassword": {
                                                        "maxLength": 162,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "enforcementVlans": {
                                                        "maxLength": 4094,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "ipSgtMappings": {
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
                                                                            "default": "IP_SGT_MAPPING_CONFIG",
                                                                            "enum": [
                                                                                "IP_SGT_MAPPING_CONFIG"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "hostOrSubnetIpAddress": {
                                                                            "maxLength": 255,
                                                                            "minLength": 0,
                                                                            "type": "string"
                                                                        },
                                                                        "sgt": {
                                                                            "maximum": 65521,
                                                                            "minimum": 0,
                                                                            "type": "integer"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "hostOrSubnetIpAddress"
                                                                    ],
                                                                    "type": "object"
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "ipVrfSgtMappings": {
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
                                                                            "default": "PER_VRF_IP_SGT_MAPPING_CONFIG",
                                                                            "enum": [
                                                                                "PER_VRF_IP_SGT_MAPPING_CONFIG"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "ipAddress": {
                                                                            "maxLength": 255,
                                                                            "minLength": 0,
                                                                            "type": "string"
                                                                        },
                                                                        "sgt": {
                                                                            "maximum": 65521,
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
                                                                        "ipAddress",
                                                                        "vrfName"
                                                                    ],
                                                                    "type": "object"
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "isRoleBasedEnforcementEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isSxpEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "roleBasedPermissions": {
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
                                                                            "default": "CTS_PERMISSIONS_CONFIG",
                                                                            "enum": [
                                                                                "CTS_PERMISSIONS_CONFIG"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "destinationSgtRanges": {
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
                                                                                                "default": "CTS_ROLE_BASED_PERMISSIONS_RANGE_CONFIG",
                                                                                                "enum": [
                                                                                                    "CTS_ROLE_BASED_PERMISSIONS_RANGE_CONFIG"
                                                                                                ],
                                                                                                "type": "string"
                                                                                            },
                                                                                            "destinationSgt": {
                                                                                                "maximum": 65521,
                                                                                                "minimum": 0,
                                                                                                "type": "integer"
                                                                                            },
                                                                                            "ipv4RoleBasedAclName": {
                                                                                                "maxLength": 255,
                                                                                                "minLength": 0,
                                                                                                "type": "string"
                                                                                            },
                                                                                            "ipv6RoleBasedAclName": {
                                                                                                "maxLength": 255,
                                                                                                "minLength": 0,
                                                                                                "type": "string"
                                                                                            }
                                                                                        },
                                                                                        "required": [
                                                                                            "destinationSgt"
                                                                                        ],
                                                                                        "type": "object"
                                                                                    },
                                                                                    "type": "array"
                                                                                }
                                                                            },
                                                                            "type": "object"
                                                                        },
                                                                        "sourceSgtRange": {
                                                                            "maximum": 65521,
                                                                            "minimum": 0,
                                                                            "type": "integer"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "sourceSgtRange"
                                                                    ],
                                                                    "type": "object"
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "sxpIpV4Peers": {
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
                                                                            "default": "CTS_SXP_IPV4_PEER_CONFIG",
                                                                            "enum": [
                                                                                "CTS_SXP_IPV4_PEER_CONFIG"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "ipV4Address": {
                                                                            "maxLength": 255,
                                                                            "minLength": 0,
                                                                            "type": "string"
                                                                        },
                                                                        "localDeviceMode": {
                                                                            "enum": [
                                                                                "SPEAKER",
                                                                                "LISTENER",
                                                                                "BOTH"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "maximumHoldTime": {
                                                                            "maximum": 65535,
                                                                            "minimum": 0,
                                                                            "type": "integer"
                                                                        },
                                                                        "minimumHoldTime": {
                                                                            "maximum": 65535,
                                                                            "minimum": 0,
                                                                            "type": "integer"
                                                                        },
                                                                        "mode": {
                                                                            "enum": [
                                                                                "LOCAL",
                                                                                "PEER"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "passwordType": {
                                                                            "type": "string"
                                                                        },
                                                                        "sourceIpv4Address": {
                                                                            "type": "string"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "ipV4Address"
                                                                    ],
                                                                    "type": "object"
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    }
                                                },
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
                                },
                                "deviceTrackingConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "DEVICE_TRACKING_CONFIG",
                                                        "enum": [
                                                            "DEVICE_TRACKING_CONFIG"
                                                        ],
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
                                                                        "addressCountLimit": {
                                                                            "maximum": 32000,
                                                                            "minimum": 0,
                                                                            "type": "integer"
                                                                        },
                                                                        "configType": {
                                                                            "default": "DEVICE_TRACKING_POLICY_CONFIG",
                                                                            "enum": [
                                                                                "DEVICE_TRACKING_POLICY_CONFIG"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "deviceRole": {
                                                                            "enum": [
                                                                                "NODE",
                                                                                "SWITCH",
                                                                                "ROUTER"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "isDestinationGleanLogOnly": {
                                                                            "type": "boolean"
                                                                        },
                                                                        "isPrefixGleanEnabled": {
                                                                            "type": "boolean"
                                                                        },
                                                                        "isProtocolArpEnabled": {
                                                                            "type": "boolean"
                                                                        },
                                                                        "isProtocolDhcp4Enabled": {
                                                                            "type": "boolean"
                                                                        },
                                                                        "isProtocolDhcp6Enabled": {
                                                                            "type": "boolean"
                                                                        },
                                                                        "isProtocolNdpEnabled": {
                                                                            "type": "boolean"
                                                                        },
                                                                        "isSecurityLevelGleanEnabled": {
                                                                            "type": "boolean"
                                                                        },
                                                                        "isTrackingEnabled": {
                                                                            "type": "boolean"
                                                                        },
                                                                        "isTrustedPortEnabled": {
                                                                            "type": "boolean"
                                                                        },
                                                                        "policyName": {
                                                                            "maxLength": 255,
                                                                            "minLength": 0,
                                                                            "type": "string"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "policyName"
                                                                    ],
                                                                    "type": "object"
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "fallbackSourceIpv4Address": {
                                                        "type": "string"
                                                    },
                                                    "fallbackSourceIpv4Mask": {
                                                        "type": "string"
                                                    },
                                                    "isAutoSourceEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isFallbackSourceOverrideEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isLoggingTheftEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isTrackingEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "maxBindingEntries": {
                                                        "maximum": 1000000,
                                                        "minimum": 0,
                                                        "type": "integer"
                                                    }
                                                },
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
                                },
                                "deviceTrackingVlanConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "DEVICE_TRACKING_VLAN_CONFIG",
                                                        "enum": [
                                                            "DEVICE_TRACKING_VLAN_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "deviceTrackingPolicy": {
                                                        "maxLength": 255,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "isDeviceTrackingEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "vlanId": {
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "vlanId"
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
                                },
                                "dhcpSnoopingConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "DHCP_SNOOPING_CONFIG",
                                                        "enum": [
                                                            "DHCP_SNOOPING_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "databaseTimeout": {
                                                        "maximum": 86400,
                                                        "minimum": 0,
                                                        "type": "integer"
                                                    },
                                                    "databaseUrl": {
                                                        "type": "string"
                                                    },
                                                    "dhcpSnoopingVlans": {
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
                                                                            "default": "DHCP_SNOOPING_VLAN_CONFIG",
                                                                            "enum": [
                                                                                "DHCP_SNOOPING_VLAN_CONFIG"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "vlanId": {
                                                                            "maximum": 4094,
                                                                            "minimum": 1,
                                                                            "type": "integer"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "vlanId"
                                                                    ]
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "isDhcpSnoopingEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isGleanEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isSnoopingInfoOptionEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isSnoopingOptionAllowUntrustedEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "writeDelay": {
                                                        "maximum": 86400,
                                                        "minimum": 15,
                                                        "type": "integer"
                                                    }
                                                },
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
                                },
                                "dot1xConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "DOT1X_CONFIG",
                                                        "enum": [
                                                            "DOT1X_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "dot1xCredentials": {
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
                                                                            "default": "DOT1X_CREDENTIALS_CONFIG",
                                                                            "enum": [
                                                                                "DOT1X_CREDENTIALS_CONFIG"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "password": {
                                                                            "maxLength": 241,
                                                                            "minLength": 0,
                                                                            "type": "string"
                                                                        },
                                                                        "passwordType": {
                                                                            "type": "string"
                                                                        },
                                                                        "profileName": {
                                                                            "maxLength": 255,
                                                                            "minLength": 0,
                                                                            "type": "string"
                                                                        },
                                                                        "username": {
                                                                            "maxLength": 255,
                                                                            "minLength": 0,
                                                                            "type": "string"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "profileName"
                                                                    ],
                                                                    "type": "object"
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "isDot1xEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isLoggingVerboseEnabled": {
                                                        "type": "boolean"
                                                    }
                                                },
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
                                },
                                "ipV4ExtendedAccessListConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "accessListSequenceRules": {
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
                                                                        "action": {
                                                                            "enum": [
                                                                                "DENY",
                                                                                "PERMIT"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "configType": {
                                                                            "default": "IPV4_EXTENDED_ACCESS_LIST_RULE",
                                                                            "enum": [
                                                                                "IPV4_EXTENDED_ACCESS_LIST_RULE"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "destinationEndRange": {
                                                                            "type": "string"
                                                                        },
                                                                        "destinationIpV4Address": {
                                                                            "type": "string"
                                                                        },
                                                                        "destinationIpV4Subnet": {
                                                                            "type": "string"
                                                                        },
                                                                        "destinationStartRange": {
                                                                            "type": "string"
                                                                        },
                                                                        "destinationType": {
                                                                            "enum": [
                                                                                "EQUAL_TO",
                                                                                "GREATER_THAN",
                                                                                "LESS_THAN",
                                                                                "RANGE",
                                                                                "NOT_EQUAL"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "destinationValue": {
                                                                            "type": "string"
                                                                        },
                                                                        "destinationWildcard": {
                                                                            "type": "string"
                                                                        },
                                                                        "isDestinationAnyEnabled": {
                                                                            "type": "boolean"
                                                                        },
                                                                        "isLoggingEnabled": {
                                                                            "type": "boolean"
                                                                        },
                                                                        "isSourceAnyEnabled": {
                                                                            "type": "boolean"
                                                                        },
                                                                        "matchDscp": {
                                                                            "enum": [
                                                                                "af11",
                                                                                "af12",
                                                                                "af13",
                                                                                "af21",
                                                                                "af22",
                                                                                "af23",
                                                                                "af31",
                                                                                "af32",
                                                                                "af33",
                                                                                "af41",
                                                                                "af42",
                                                                                "af43",
                                                                                "cs1",
                                                                                "cs2",
                                                                                "cs3",
                                                                                "cs4",
                                                                                "cs5",
                                                                                "cs6",
                                                                                "cs7",
                                                                                "ef",
                                                                                "default"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "protocol": {
                                                                            "type": "string"
                                                                        },
                                                                        "sequence": {
                                                                            "maximum": 2147483647,
                                                                            "minimum": 1,
                                                                            "type": "integer"
                                                                        },
                                                                        "sourceEndRange": {
                                                                            "type": "string"
                                                                        },
                                                                        "sourceIpV4Address": {
                                                                            "type": "string"
                                                                        },
                                                                        "sourceIpV4Subnet": {
                                                                            "type": "string"
                                                                        },
                                                                        "sourceStartRange": {
                                                                            "type": "string"
                                                                        },
                                                                        "sourceType": {
                                                                            "enum": [
                                                                                "EQUAL_TO",
                                                                                "GREATER_THAN",
                                                                                "LESS_THAN",
                                                                                "RANGE",
                                                                                "NOT_EQUAL"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "sourceValue": {
                                                                            "type": "string"
                                                                        },
                                                                        "sourceWildcard": {
                                                                            "type": "string"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "sequence"
                                                                    ],
                                                                    "type": "object"
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "aclName": {
                                                        "maxLength": 231,
                                                        "minLength": 1,
                                                        "type": "string"
                                                    },
                                                    "configType": {
                                                        "default": "IPV4_EXTENDED_ACCESS_LIST_CONFIG",
                                                        "enum": [
                                                            "IPV4_EXTENDED_ACCESS_LIST_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "aclName"
                                                ],
                                                "type": "object"
                                            },
                                            "maxItems": 2147483647,
                                            "minItems": 0,
                                            "type": "array"
                                        }
                                    },
                                    "required": [
                                        "items"
                                    ],
                                    "type": "object"
                                },
                                "ipV4RoleBasedAccessListConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "accessListSequenceRules": {
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
                                                                        "action": {
                                                                            "enum": [
                                                                                "DENY",
                                                                                "PERMIT"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "configType": {
                                                                            "default": "IPV4_ROLE_BASED_ACCESS_LIST_RULE",
                                                                            "enum": [
                                                                                "IPV4_ROLE_BASED_ACCESS_LIST_RULE"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "isLoggingEnabled": {
                                                                            "type": "boolean"
                                                                        },
                                                                        "protocol": {
                                                                            "type": "string"
                                                                        },
                                                                        "sequence": {
                                                                            "maximum": 2147483647,
                                                                            "minimum": 1,
                                                                            "type": "integer"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "sequence"
                                                                    ],
                                                                    "type": "object"
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "aclName": {
                                                        "maxLength": 229,
                                                        "minLength": 1,
                                                        "type": "string"
                                                    },
                                                    "configType": {
                                                        "default": "IPV4_ROLE_BASED_ACCESS_LIST_CONFIG",
                                                        "enum": [
                                                            "IPV4_ROLE_BASED_ACCESS_LIST_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "aclName"
                                                ],
                                                "type": "object"
                                            },
                                            "maxItems": 2147483647,
                                            "minItems": 0,
                                            "type": "array"
                                        }
                                    },
                                    "required": [
                                        "items"
                                    ],
                                    "type": "object"
                                },
                                "ipV4StandardAccessListConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "accessListSequenceRules": {
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
                                                                            "default": "IPV4_STANDARD_ACCESS_LIST_RULE",
                                                                            "enum": [
                                                                                "IPV4_STANDARD_ACCESS_LIST_RULE"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "isDenyAnyEnabled": {
                                                                            "type": "boolean"
                                                                        },
                                                                        "isDenyLogEnabled": {
                                                                            "type": "boolean"
                                                                        },
                                                                        "isPermitAnyEnabled": {
                                                                            "type": "boolean"
                                                                        },
                                                                        "isPermitLogEnabled": {
                                                                            "type": "boolean"
                                                                        },
                                                                        "sequence": {
                                                                            "maximum": 2147483647,
                                                                            "minimum": 1,
                                                                            "type": "integer"
                                                                        },
                                                                        "sourceHostIpV4Address": {
                                                                            "type": "string"
                                                                        },
                                                                        "sourceIpV4Address": {
                                                                            "type": "string"
                                                                        },
                                                                        "sourceWildcard": {
                                                                            "type": "string"
                                                                        },
                                                                        "subnetHostIpV4Address": {
                                                                            "type": "string"
                                                                        },
                                                                        "subnetIpV4Address": {
                                                                            "type": "string"
                                                                        },
                                                                        "subnetWildcard": {
                                                                            "type": "string"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "sequence"
                                                                    ],
                                                                    "type": "object"
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "aclName": {
                                                        "maxLength": 231,
                                                        "minLength": 1,
                                                        "type": "string"
                                                    },
                                                    "configType": {
                                                        "default": "IPV4_STANDARD_ACCESS_LIST_CONFIG",
                                                        "enum": [
                                                            "IPV4_STANDARD_ACCESS_LIST_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "aclName"
                                                ],
                                                "type": "object"
                                            },
                                            "maxItems": 2147483647,
                                            "minItems": 0,
                                            "type": "array"
                                        }
                                    },
                                    "required": [
                                        "items"
                                    ],
                                    "type": "object"
                                },
                                "ipV6AccessListConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "accessListSequenceRules": {
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
                                                                        "action": {
                                                                            "enum": [
                                                                                "DENY",
                                                                                "PERMIT"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "configType": {
                                                                            "default": "IPV6_ACCESS_LIST_RULE",
                                                                            "enum": [
                                                                                "IPV6_ACCESS_LIST_RULE"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "destinationEndRange": {
                                                                            "type": "string"
                                                                        },
                                                                        "destinationIpV6Address": {
                                                                            "type": "string"
                                                                        },
                                                                        "destinationNetworkAddress": {
                                                                            "type": "string"
                                                                        },
                                                                        "destinationNetworkWildcard": {
                                                                            "type": "string"
                                                                        },
                                                                        "destinationPrefix": {
                                                                            "type": "string"
                                                                        },
                                                                        "destinationStartRange": {
                                                                            "type": "string"
                                                                        },
                                                                        "destinationType": {
                                                                            "enum": [
                                                                                "EQUAL_TO",
                                                                                "GREATER_THAN",
                                                                                "LESS_THAN",
                                                                                "RANGE",
                                                                                "NOT_EQUAL"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "destinationValue": {
                                                                            "type": "string"
                                                                        },
                                                                        "isDestinationAnyEnabled": {
                                                                            "type": "boolean"
                                                                        },
                                                                        "isEstablishedEnabled": {
                                                                            "type": "boolean"
                                                                        },
                                                                        "isLoggingEnabled": {
                                                                            "type": "boolean"
                                                                        },
                                                                        "isSourceAnyEnabled": {
                                                                            "type": "boolean"
                                                                        },
                                                                        "matchDscp": {
                                                                            "enum": [
                                                                                "af11",
                                                                                "af12",
                                                                                "af13",
                                                                                "af21",
                                                                                "af22",
                                                                                "af23",
                                                                                "af31",
                                                                                "af32",
                                                                                "af33",
                                                                                "af41",
                                                                                "af42",
                                                                                "af43",
                                                                                "cs1",
                                                                                "cs2",
                                                                                "cs3",
                                                                                "cs4",
                                                                                "cs5",
                                                                                "cs6",
                                                                                "cs7",
                                                                                "ef",
                                                                                "default"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "protocol": {
                                                                            "type": "string"
                                                                        },
                                                                        "sequence": {
                                                                            "maximum": 4294967294,
                                                                            "minimum": 1,
                                                                            "type": "integer"
                                                                        },
                                                                        "sourceEndRange": {
                                                                            "type": "string"
                                                                        },
                                                                        "sourceIpV6Address": {
                                                                            "type": "string"
                                                                        },
                                                                        "sourceNetworkAddress": {
                                                                            "type": "string"
                                                                        },
                                                                        "sourceNetworkWildcard": {
                                                                            "type": "string"
                                                                        },
                                                                        "sourcePrefix": {
                                                                            "type": "string"
                                                                        },
                                                                        "sourceStartRange": {
                                                                            "type": "string"
                                                                        },
                                                                        "sourceType": {
                                                                            "enum": [
                                                                                "EQUAL_TO",
                                                                                "GREATER_THAN",
                                                                                "LESS_THAN",
                                                                                "RANGE",
                                                                                "NOT_EQUAL"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "sourceValue": {
                                                                            "type": "string"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "sequence"
                                                                    ]
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "aclName": {
                                                        "maxLength": 233,
                                                        "minLength": 1,
                                                        "type": "string"
                                                    },
                                                    "configType": {
                                                        "default": "IPV6_ACCESS_LIST_CONFIG",
                                                        "enum": [
                                                            "IPV6_ACCESS_LIST_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "aclName"
                                                ],
                                                "type": "object"
                                            },
                                            "minItems": 1,
                                            "type": "array"
                                        }
                                    },
                                    "required": [
                                        "items"
                                    ],
                                    "type": "object"
                                },
                                "ipV6RoleBasedAccessListConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "accessListSequenceRules": {
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
                                                                        "action": {
                                                                            "enum": [
                                                                                "DENY",
                                                                                "PERMIT"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "configType": {
                                                                            "default": "IPV6_ROLE_BASED_ACCESS_LIST_RULE",
                                                                            "enum": [
                                                                                "IPV6_ROLE_BASED_ACCESS_LIST_RULE"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "isLogEnabled": {
                                                                            "type": "boolean"
                                                                        },
                                                                        "protocolType": {
                                                                            "enum": [
                                                                                "TCP",
                                                                                "UDP",
                                                                                "ICMP",
                                                                                "SCTP",
                                                                                "OTHER"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "protocolValue": {
                                                                            "type": "string"
                                                                        },
                                                                        "sequence": {
                                                                            "maximum": 4294967294,
                                                                            "minimum": 1,
                                                                            "type": "integer"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "sequence"
                                                                    ],
                                                                    "type": "object"
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "aclName": {
                                                        "maxLength": 222,
                                                        "minLength": 1,
                                                        "type": "string"
                                                    },
                                                    "configType": {
                                                        "default": "IPV6_ROLE_BASED_ACCESS_LIST_CONFIG",
                                                        "enum": [
                                                            "IPV6_ROLE_BASED_ACCESS_LIST_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "aclName"
                                                ],
                                                "type": "object"
                                            },
                                            "minItems": 0,
                                            "type": "array"
                                        }
                                    },
                                    "required": [
                                        "items"
                                    ],
                                    "type": "object"
                                },
                                "macExtendedAccessListConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "accessListExtendedEntries": {
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
                                                                        "action": {
                                                                            "enum": [
                                                                                "DENY",
                                                                                "PERMIT"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "configType": {
                                                                            "default": "MAC_ACCESS_LIST_EXTENDED_ENTRY",
                                                                            "enum": [
                                                                                "MAC_ACCESS_LIST_EXTENDED_ENTRY"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "values": {
                                                                            "type": "string"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "action",
                                                                        "values"
                                                                    ],
                                                                    "type": "object"
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "aclName": {
                                                        "maxLength": 230,
                                                        "minLength": 1,
                                                        "type": "string"
                                                    },
                                                    "configType": {
                                                        "default": "MAC_ACCESS_LIST_EXTENDED_CONFIG",
                                                        "enum": [
                                                            "MAC_ACCESS_LIST_EXTENDED_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "aclName"
                                                ],
                                                "type": "object"
                                            },
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
