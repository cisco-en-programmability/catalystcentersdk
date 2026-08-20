"""Cisco Catalyst Center GetConfigurationsForAnIntendedLayer2FeatureOnAWiredDevice data model.

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


class JSONSchemaValidatorD1B2D399192A5Da39B4AE3Fe0F5288D4:
    """GetConfigurationsForAnIntendedLayer2FeatureOnAWiredDevice request
    schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "cdpGlobalConfig": {
                            "properties": {
                                "items": {
                                    "items": {
                                        "properties": {
                                            "configType": {
                                                "enum": [
                                                    "CDP_GLOBAL"
                                                ],
                                                "type": "string"
                                            },
                                            "holdTime": {
                                                "exclusiveMaximum": true,
                                                "exclusiveMinimum": true,
                                                "maximum": 255,
                                                "minimum": 10,
                                                "type": "integer"
                                            },
                                            "isAdvertiseV2Enabled": {
                                                "type": "boolean"
                                            },
                                            "isCdpEnabled": {
                                                "type": "boolean"
                                            },
                                            "isLogDuplexMismatchEnabled": {
                                                "type": "boolean"
                                            },
                                            "timer": {
                                                "exclusiveMaximum": true,
                                                "exclusiveMinimum": true,
                                                "maximum": 254,
                                                "minimum": 5,
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
                            "type": "object"
                        },
                        "cdpInterfaceConfig": {
                            "properties": {
                                "items": {
                                    "items": {
                                        "properties": {
                                            "configType": {
                                                "enum": [
                                                    "CDP_INTERFACE"
                                                ],
                                                "type": "string"
                                            },
                                            "interfaceName": {
                                                "type": "string"
                                            },
                                            "isCdpEnabled": {
                                                "type": "boolean"
                                            },
                                            "isLogDuplexMismatchEnabled": {
                                                "type": "boolean"
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
                        "dhcpSnoopingGlobalConfig": {
                            "properties": {
                                "items": {
                                    "items": {
                                        "properties": {
                                            "configType": {
                                                "enum": [
                                                    ""
                                                ],
                                                "type": "string"
                                            },
                                            "databaseAgent": {
                                                "properties": {
                                                    "agentUrl": {
                                                        "maxLength": 227,
                                                        "minLength": 5,
                                                        "type": "string"
                                                    },
                                                    "configType": {
                                                        "enum": [
                                                            "DHCP_SNOOPING_DATABASE_AGENT"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "timeout": {
                                                        "exclusiveMaximum": true,
                                                        "exclusiveMinimum": true,
                                                        "maximum": 86400,
                                                        "minimum": 0,
                                                        "type": "integer"
                                                    },
                                                    "writeDelay": {
                                                        "exclusiveMaximum": true,
                                                        "exclusiveMinimum": true,
                                                        "maximum": 86400,
                                                        "minimum": 15,
                                                        "type": "integer"
                                                    }
                                                },
                                                "type": "object"
                                            },
                                            "dhcpSnoopingVlans": {
                                                "type": "string"
                                            },
                                            "isDhcpSnoopingEnabled": {
                                                "type": "boolean"
                                            },
                                            "isGleaningEnabled": {
                                                "type": "boolean"
                                            },
                                            "proxyBridgeVlans": {
                                                "type": "string"
                                            }
                                        },
                                        "type": "object"
                                    },
                                    "type": "array"
                                }
                            },
                            "type": "object"
                        },
                        "dhcpSnoopingInterfaceConfig": {
                            "properties": {
                                "items": {
                                    "items": {
                                        "properties": {
                                            "configType": {
                                                "enum": [
                                                    "DHCP_SNOOPING_INTERFACE"
                                                ],
                                                "type": "string"
                                            },
                                            "interfaceName": {
                                                "minLength": 1,
                                                "type": "string"
                                            },
                                            "isTrustedInterface": {
                                                "type": "boolean"
                                            },
                                            "messageRateLimit": {
                                                "exclusiveMaximum": true,
                                                "exclusiveMinimum": true,
                                                "maximum": 2048,
                                                "minimum": 1,
                                                "type": "integer"
                                            }
                                        },
                                        "type": "object"
                                    },
                                    "type": "array"
                                }
                            },
                            "type": "object"
                        },
                        "dot1xGlobalConfig": {
                            "properties": {
                                "items": {
                                    "items": {
                                        "properties": {
                                            "authenticationConfigMode": {
                                                "enum": [
                                                    "LEGACY",
                                                    "NEW_STYLE"
                                                ],
                                                "type": "string"
                                            },
                                            "configType": {
                                                "enum": [
                                                    "DOT1X_GLOBAL"
                                                ],
                                                "type": "string"
                                            },
                                            "isDot1xEnabled": {
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
                            "type": "object"
                        },
                        "dot1xInterfaceConfig": {
                            "properties": {
                                "items": {
                                    "items": {
                                        "properties": {
                                            "authenticationOrder": {
                                                "properties": {
                                                    "configType": {
                                                        "enum": [
                                                            "ORDERED_SET"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "items": {
                                                        "items": {
                                                            "type": "string"
                                                        },
                                                        "maxItems": 3,
                                                        "type": "array"
                                                    }
                                                },
                                                "type": "object"
                                            },
                                            "configType": {
                                                "enum": [
                                                    "DOT1X_INTERFACE"
                                                ],
                                                "type": "string"
                                            },
                                            "interfaceName": {
                                                "minLength": 1,
                                                "type": "string"
                                            }
                                        },
                                        "type": "object"
                                    },
                                    "type": "array"
                                }
                            },
                            "type": "object"
                        },
                        "igmpSnoopingGlobalConfig": {
                            "properties": {
                                "items": {
                                    "items": {
                                        "properties": {
                                            "configType": {
                                                "enum": [
                                                    "IGMP_SNOOPING_GLOBAL"
                                                ],
                                                "type": "string"
                                            },
                                            "igmpSnoopingVlanSettings": {
                                                "properties": {
                                                    "configType": {
                                                        "enum": [
                                                            "SET"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "items": {
                                                        "items": {
                                                            "properties": {
                                                                "configType": {
                                                                    "enum": [
                                                                        "IGMP_SNOOPING_VLAN"
                                                                    ],
                                                                    "type": "string"
                                                                },
                                                                "igmpSnoopingVlanMrouters": {
                                                                    "properties": {
                                                                        "configType": {
                                                                            "enum": [
                                                                                "SET"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "items": {
                                                                            "items": {
                                                                                "properties": {
                                                                                    "configType": {
                                                                                        "enum": [
                                                                                            "IGMP_SNOOPING_VLAN_MROUTER"
                                                                                        ],
                                                                                        "type": "string"
                                                                                    },
                                                                                    "interfaceName": {
                                                                                        "minLength": 1,
                                                                                        "type": "string"
                                                                                    }
                                                                                },
                                                                                "required": [
                                                                                    "interfaceName"
                                                                                ],
                                                                                "type": "object"
                                                                            },
                                                                            "maxItems": 2,
                                                                            "type": "array"
                                                                        }
                                                                    },
                                                                    "type": "object"
                                                                },
                                                                "isIgmpSnoopingEnabled": {
                                                                    "type": "boolean"
                                                                },
                                                                "isImmediateLeaveEnabled": {
                                                                    "type": "boolean"
                                                                },
                                                                "isQuerierEnabled": {
                                                                    "type": "boolean"
                                                                },
                                                                "querierAddress": {
                                                                    "type": "string"
                                                                },
                                                                "querierQueryInterval": {
                                                                    "exclusiveMaximum": true,
                                                                    "exclusiveMinimum": true,
                                                                    "maximum": 18000,
                                                                    "minimum": 1,
                                                                    "type": "integer"
                                                                },
                                                                "querierVersion": {
                                                                    "enum": [
                                                                        "VERSION_1",
                                                                        "VERSION_2",
                                                                        "VERSION_3"
                                                                    ],
                                                                    "type": "string"
                                                                },
                                                                "vlanId": {
                                                                    "exclusiveMaximum": true,
                                                                    "exclusiveMinimum": true,
                                                                    "maximum": 4094,
                                                                    "minimum": 1,
                                                                    "type": "integer"
                                                                }
                                                            },
                                                            "type": "object"
                                                        },
                                                        "type": "array"
                                                    }
                                                },
                                                "type": "object"
                                            },
                                            "isIgmpSnoopingEnabled": {
                                                "type": "boolean"
                                            },
                                            "isQuerierEnabled": {
                                                "type": "boolean"
                                            },
                                            "querierAddress": {
                                                "type": "string"
                                            },
                                            "querierQueryInterval": {
                                                "exclusiveMaximum": true,
                                                "exclusiveMinimum": true,
                                                "maximum": 18000,
                                                "minimum": 1,
                                                "type": "integer"
                                            },
                                            "querierVersion": {
                                                "enum": [
                                                    "VERSION_1",
                                                    "VERSION_2",
                                                    "VERSION_3"
                                                ],
                                                "type": "string"
                                            }
                                        },
                                        "type": "object"
                                    },
                                    "maxItems": 1,
                                    "minItems": 1,
                                    "type": "array"
                                }
                            },
                            "type": "object"
                        },
                        "lldpGlobalConfig": {
                            "properties": {
                                "items": {
                                    "items": {
                                        "properties": {
                                            "configType": {
                                                "enum": [
                                                    "LLDP_GLOBAL"
                                                ],
                                                "type": "string"
                                            },
                                            "holdTime": {
                                                "exclusiveMaximum": true,
                                                "exclusiveMinimum": true,
                                                "maximum": 32767,
                                                "minimum": 0,
                                                "type": "integer"
                                            },
                                            "isLldpEnabled": {
                                                "type": "boolean"
                                            },
                                            "reinitializationDelay": {
                                                "exclusiveMaximum": true,
                                                "exclusiveMinimum": true,
                                                "maximum": 5,
                                                "minimum": 2,
                                                "type": "integer"
                                            },
                                            "timer": {
                                                "exclusiveMaximum": true,
                                                "exclusiveMinimum": true,
                                                "maximum": 32767,
                                                "minimum": 5,
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
                            "type": "object"
                        },
                        "lldpInterfaceConfig": {
                            "properties": {
                                "items": {
                                    "items": {
                                        "properties": {
                                            "adminStatus": {
                                                "enum": [
                                                    "TRANSMIT_ONLY",
                                                    "RECEIVE_ONLY",
                                                    "TRANSMIT_AND_RECEIVE",
                                                    "DISABLED"
                                                ],
                                                "type": "string"
                                            },
                                            "configType": {
                                                "enum": [
                                                    "LLDP_INTERFACE"
                                                ],
                                                "type": "string"
                                            },
                                            "interfaceName": {
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
                            "type": "object"
                        },
                        "mabInterfaceConfig": {
                            "properties": {
                                "items": {
                                    "items": {
                                        "properties": {
                                            "configType": {
                                                "enum": [
                                                    "MAB_INTERFACE"
                                                ],
                                                "type": "string"
                                            },
                                            "interfaceName": {
                                                "minLength": 1,
                                                "type": "string"
                                            },
                                            "isMabEnabled": {
                                                "type": "boolean"
                                            }
                                        },
                                        "type": "object"
                                    },
                                    "type": "array"
                                }
                            },
                            "type": "object"
                        },
                        "mldSnoopingGlobalConfig": {
                            "properties": {
                                "items": {
                                    "items": {
                                        "properties": {
                                            "configType": {
                                                "enum": [
                                                    "MLD_SNOOPING_GLOBAL"
                                                ],
                                                "type": "string"
                                            },
                                            "isMldSnoopingEnabled": {
                                                "type": "boolean"
                                            },
                                            "isQuerierEnabled": {
                                                "type": "boolean"
                                            },
                                            "isSuppressListenerMessagesEnabled": {
                                                "type": "boolean"
                                            },
                                            "mldSnoopingVlanSettings": {
                                                "properties": {
                                                    "configType": {
                                                        "enum": [
                                                            "SET"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "items": {
                                                        "items": {
                                                            "properties": {
                                                                "configType": {
                                                                    "enum": [
                                                                        "MLD_SNOOPING_VLAN"
                                                                    ],
                                                                    "type": "string"
                                                                },
                                                                "isImmediateLeaveEnabled": {
                                                                    "type": "boolean"
                                                                },
                                                                "isMldSnoopingEnabled": {
                                                                    "type": "boolean"
                                                                },
                                                                "isQuerierEnabled": {
                                                                    "type": "boolean"
                                                                },
                                                                "mldSnoopingVlanMrouters": {
                                                                    "properties": {
                                                                        "configType": {
                                                                            "enum": [
                                                                                "SET"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "items": {
                                                                            "items": {
                                                                                "properties": {
                                                                                    "configType": {
                                                                                        "enum": [
                                                                                            "MLD_SNOOPING_VLAN_MROUTER"
                                                                                        ],
                                                                                        "type": "string"
                                                                                    },
                                                                                    "interfaceName": {
                                                                                        "minLength": 1,
                                                                                        "type": "string"
                                                                                    }
                                                                                },
                                                                                "type": "object"
                                                                            },
                                                                            "maxItems": 2,
                                                                            "type": "array"
                                                                        }
                                                                    },
                                                                    "type": "object"
                                                                },
                                                                "querierAddress": {
                                                                    "type": "string"
                                                                },
                                                                "querierQueryInterval": {
                                                                    "exclusiveMaximum": true,
                                                                    "exclusiveMinimum": true,
                                                                    "maximum": 18000,
                                                                    "minimum": 1,
                                                                    "type": "integer"
                                                                },
                                                                "querierVersion": {
                                                                    "enum": [
                                                                        "VERSION_1",
                                                                        "VERSION_2"
                                                                    ],
                                                                    "type": "string"
                                                                },
                                                                "vlanId": {
                                                                    "exclusiveMaximum": true,
                                                                    "exclusiveMinimum": true,
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
                                                        "type": "array"
                                                    }
                                                },
                                                "type": "object"
                                            },
                                            "querierAddress": {
                                                "type": "string"
                                            },
                                            "querierQueryInterval": {
                                                "exclusiveMaximum": true,
                                                "exclusiveMinimum": true,
                                                "maximum": 18000,
                                                "minimum": 1,
                                                "type": "integer"
                                            },
                                            "querierVersion": {
                                                "enum": [
                                                    "VERSION_1",
                                                    "VERSION_2"
                                                ],
                                                "type": "string"
                                            }
                                        },
                                        "type": "object"
                                    },
                                    "maxItems": 1,
                                    "minItems": 1,
                                    "type": "array"
                                }
                            },
                            "type": "object"
                        },
                        "portChannelConfig": {
                            "properties": {
                                "items": {
                                    "items": {
                                        "properties": {
                                            "configType": {
                                                "enum": [
                                                    "PORTCHANNEL"
                                                ],
                                                "type": "string"
                                            },
                                            "isAutoEnabled": {
                                                "type": "boolean"
                                            },
                                            "lacpSystemPriority": {
                                                "exclusiveMaximum": true,
                                                "exclusiveMinimum": true,
                                                "maximum": 65535,
                                                "minimum": 0,
                                                "type": "integer"
                                            },
                                            "loadBalancingMethod": {
                                                "enum": [
                                                    "SRC_MAC",
                                                    "DST_MAC",
                                                    "SRC_DST_MAC",
                                                    "SRC_IP",
                                                    "DST_IP",
                                                    "SRC_DST_IP",
                                                    "SRC_PORT",
                                                    "DST_PORT",
                                                    "SRC_DST_PORT",
                                                    "SRC_DST_MIXED_IP_PORT",
                                                    "SRC_MIXED_IP_PORT",
                                                    "DST_MIXED_IP_PORT",
                                                    "VLAN_SRC_IP",
                                                    "VLAN_DST_IP",
                                                    "VLAN_SRC_DST_IP",
                                                    "VLAN_SRC_MIXED_IP_PORT",
                                                    "VLAN_DST_MIXED_IP_PORT",
                                                    "VLAN_SRC_DST_MIXED_IP_PORT"
                                                ],
                                                "type": "string"
                                            },
                                            "portchannels": {
                                                "properties": {
                                                    "configType": {
                                                        "enum": [
                                                            "SET"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "items": {
                                                        "items": {
                                                            "properties": {
                                                                "AnyOf": {
                                                                    "properties": {
                                                                        "EtherchannelConfig": {
                                                                            "properties": {
                                                                                "configType": {
                                                                                    "enum": [
                                                                                        "ETHERCHANNEL_CONFIG"
                                                                                    ],
                                                                                    "type": "string"
                                                                                },
                                                                                "memberPorts": {
                                                                                    "properties": {
                                                                                        "configType": {
                                                                                            "enum": [
                                                                                                "SET"
                                                                                            ],
                                                                                            "type": "string"
                                                                                        },
                                                                                        "items": {
                                                                                            "items": {
                                                                                                "properties": {
                                                                                                    "configType": {
                                                                                                        "enum": [
                                                                                                            "ETHERCHANNEL_MEMBER_PORT_CONFIG"
                                                                                                        ],
                                                                                                        "type": "string"
                                                                                                    },
                                                                                                    "interfaceName": {
                                                                                                        "type": "string"
                                                                                                    },
                                                                                                    "mode": {
                                                                                                        "enum": [
                                                                                                            true
                                                                                                        ],
                                                                                                        "type": "string"
                                                                                                    }
                                                                                                },
                                                                                                "type": "object"
                                                                                            },
                                                                                            "type": "array"
                                                                                        }
                                                                                    },
                                                                                    "type": "object"
                                                                                },
                                                                                "minLinks": {
                                                                                    "exclusiveMaximum": true,
                                                                                    "exclusiveMinimum": true,
                                                                                    "maximum": 8,
                                                                                    "minimum": 2,
                                                                                    "type": "integer"
                                                                                },
                                                                                "name": {
                                                                                    "maxLength": 15,
                                                                                    "minLength": 13,
                                                                                    "type": "string"
                                                                                }
                                                                            },
                                                                            "type": "object"
                                                                        },
                                                                        "LacpPortchannelConfig": {
                                                                            "properties": {
                                                                                "configType": {
                                                                                    "enum": [
                                                                                        "LACP_PORTCHANNEL_CONFIG"
                                                                                    ],
                                                                                    "type": "string"
                                                                                },
                                                                                "memberPorts": {
                                                                                    "properties": {
                                                                                        "configType": {
                                                                                            "enum": [
                                                                                                "SET"
                                                                                            ],
                                                                                            "type": "string"
                                                                                        },
                                                                                        "items": {
                                                                                            "items": {
                                                                                                "properties": {
                                                                                                    "configType": {
                                                                                                        "enum": [
                                                                                                            "LACP_PORTCHANNEL_MEMBER_PORT_CONFIG"
                                                                                                        ],
                                                                                                        "type": "string"
                                                                                                    },
                                                                                                    "interfaceName": {
                                                                                                        "type": "string"
                                                                                                    },
                                                                                                    "mode": {
                                                                                                        "enum": [
                                                                                                            "ACTIVE",
                                                                                                            "PASSIVE"
                                                                                                        ],
                                                                                                        "type": "string"
                                                                                                    },
                                                                                                    "portPriority": {
                                                                                                        "exclusiveMaximum": true,
                                                                                                        "exclusiveMinimum": true,
                                                                                                        "maximum": 65535,
                                                                                                        "minimum": 0,
                                                                                                        "type": "integer"
                                                                                                    },
                                                                                                    "rate": {
                                                                                                        "exclusiveMaximum": true,
                                                                                                        "exclusiveMinimum": true,
                                                                                                        "maximum": 30,
                                                                                                        "minimum": 1,
                                                                                                        "type": "integer"
                                                                                                    }
                                                                                                },
                                                                                                "type": "object"
                                                                                            },
                                                                                            "maxItems": 16,
                                                                                            "type": "array"
                                                                                        }
                                                                                    },
                                                                                    "type": "object"
                                                                                },
                                                                                "minLinks": {
                                                                                    "exclusiveMaximum": true,
                                                                                    "exclusiveMinimum": true,
                                                                                    "maximum": 8,
                                                                                    "minimum": 2,
                                                                                    "type": "integer"
                                                                                },
                                                                                "name": {
                                                                                    "maxLength": 15,
                                                                                    "minLength": 13,
                                                                                    "type": "string"
                                                                                }
                                                                            },
                                                                            "type": "object"
                                                                        },
                                                                        "PagpPortchannelConfig": {
                                                                            "properties": {
                                                                                "configType": {
                                                                                    "enum": [
                                                                                        "PAGP_PORTCHANNEL_CONFIG"
                                                                                    ],
                                                                                    "type": "string"
                                                                                },
                                                                                "memberPorts": {
                                                                                    "properties": {
                                                                                        "configType": {
                                                                                            "enum": [
                                                                                                "SET"
                                                                                            ],
                                                                                            "type": "string"
                                                                                        },
                                                                                        "items": {
                                                                                            "items": {
                                                                                                "properties": {
                                                                                                    "configType": {
                                                                                                        "enum": [
                                                                                                            "PAGP_PORTCHANNEL_MEMBER_PORT_CONFIG"
                                                                                                        ],
                                                                                                        "type": "string"
                                                                                                    },
                                                                                                    "interfaceName": {
                                                                                                        "type": "string"
                                                                                                    },
                                                                                                    "learnMethod": {
                                                                                                        "enum": [
                                                                                                            "AGGREGATION_PORT",
                                                                                                            "PHYSICAL_PORT"
                                                                                                        ],
                                                                                                        "type": "string"
                                                                                                    },
                                                                                                    "mode": {
                                                                                                        "enum": [
                                                                                                            "AUTO",
                                                                                                            "AUTO_NON_SILENT",
                                                                                                            "DESIRABLE",
                                                                                                            "DESIRABLE_NON_SILENT"
                                                                                                        ],
                                                                                                        "type": "string"
                                                                                                    },
                                                                                                    "portPriority": {
                                                                                                        "exclusiveMaximum": true,
                                                                                                        "exclusiveMinimum": true,
                                                                                                        "maximum": 255,
                                                                                                        "minimum": 0,
                                                                                                        "type": "integer"
                                                                                                    }
                                                                                                },
                                                                                                "type": "object"
                                                                                            },
                                                                                            "type": "array"
                                                                                        }
                                                                                    },
                                                                                    "type": "object"
                                                                                },
                                                                                "minLinks": {
                                                                                    "exclusiveMaximum": true,
                                                                                    "exclusiveMinimum": true,
                                                                                    "maximum": 8,
                                                                                    "minimum": 2,
                                                                                    "type": "integer"
                                                                                },
                                                                                "name": {
                                                                                    "maxLength": 15,
                                                                                    "minLength": 13,
                                                                                    "type": "string"
                                                                                }
                                                                            },
                                                                            "type": "object"
                                                                        }
                                                                    },
                                                                    "type": "object"
                                                                }
                                                            },
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
                                    "type": "array"
                                }
                            },
                            "type": "object"
                        },
                        "stpGlobalConfig": {
                            "properties": {
                                "items": {
                                    "items": {
                                        "properties": {
                                            "configType": {
                                                "enum": [
                                                    "STP_GLOBAL"
                                                ],
                                                "type": "string"
                                            },
                                            "isBackboneFastEnabled": {
                                                "type": "boolean"
                                            },
                                            "isBpduFilterEnabled": {
                                                "type": "boolean"
                                            },
                                            "isBpduGuardEnabled": {
                                                "type": "boolean"
                                            },
                                            "isEtherChannelGuardEnabled": {
                                                "type": "boolean"
                                            },
                                            "isExtendedSystemIdEnabled": {
                                                "type": "boolean"
                                            },
                                            "isLoggingEnabled": {
                                                "type": "boolean"
                                            },
                                            "isLoopGuardEnabled": {
                                                "type": "boolean"
                                            },
                                            "isUplinkFastEnabled": {
                                                "type": "boolean"
                                            },
                                            "portFastMode": {
                                                "enum": [
                                                    "ENABLE",
                                                    "DISABLE",
                                                    "EDGE",
                                                    "NETWORK"
                                                ],
                                                "type": "string"
                                            },
                                            "stpInstances": {
                                                "properties": {
                                                    "configType": {
                                                        "enum": [
                                                            "LIST"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "items": {
                                                        "items": {
                                                            "properties": {
                                                                "configType": {
                                                                    "enum": [
                                                                        "STP_VLAN"
                                                                    ],
                                                                    "type": "string"
                                                                },
                                                                "priority": {
                                                                    "exclusiveMaximum": true,
                                                                    "exclusiveMinimum": true,
                                                                    "maximum": 61440,
                                                                    "minimum": 0,
                                                                    "type": "integer"
                                                                },
                                                                "timers": {
                                                                    "properties": {
                                                                        "configType": {
                                                                            "enum": [
                                                                                "STP_TIMERS"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "forwardDelay": {
                                                                            "exclusiveMaximum": true,
                                                                            "exclusiveMinimum": true,
                                                                            "maximum": 30,
                                                                            "minimum": 4,
                                                                            "type": "integer"
                                                                        },
                                                                        "helloInterval": {
                                                                            "exclusiveMaximum": true,
                                                                            "exclusiveMinimum": true,
                                                                            "maximum": 10,
                                                                            "minimum": 1,
                                                                            "type": "integer"
                                                                        },
                                                                        "isStpEnabled": {
                                                                            "type": "boolean"
                                                                        },
                                                                        "maxAge": {
                                                                            "exclusiveMaximum": true,
                                                                            "exclusiveMinimum": true,
                                                                            "maximum": 40,
                                                                            "minimum": 6,
                                                                            "type": "integer"
                                                                        }
                                                                    },
                                                                    "type": "object"
                                                                },
                                                                "vlanId": {
                                                                    "exclusiveMaximum": true,
                                                                    "exclusiveMinimum": true,
                                                                    "maximum": 4094,
                                                                    "minimum": 1,
                                                                    "type": "integer"
                                                                }
                                                            },
                                                            "type": "object"
                                                        },
                                                        "type": "array"
                                                    }
                                                },
                                                "type": "object"
                                            },
                                            "stpMode": {
                                                "enum": [
                                                    "PVST",
                                                    "RSTP",
                                                    "MST"
                                                ],
                                                "type": "string"
                                            },
                                            "transmitHoldCount": {
                                                "exclusiveMaximum": true,
                                                "exclusiveMinimum": true,
                                                "maximum": 20,
                                                "minimum": 1,
                                                "type": "integer"
                                            },
                                            "uplinkFastMaxUpdateRate": {
                                                "exclusiveMaximum": true,
                                                "exclusiveMinimum": true,
                                                "maximum": 32000,
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
                            "type": "object"
                        },
                        "stpInterfaceConfig": {
                            "properties": {
                                "items": {
                                    "properties": {
                                        "bpduFilter": {
                                            "enum": [
                                                "ENABLE",
                                                "DISABLE",
                                                "NONE"
                                            ],
                                            "type": "string"
                                        },
                                        "bpduGuard": {
                                            "enum": [
                                                "ENABLE",
                                                "DISABLE",
                                                "NONE"
                                            ],
                                            "type": "string"
                                        },
                                        "configType": {
                                            "enum": [
                                                "STP_INTERFACE"
                                            ],
                                            "type": "string"
                                        },
                                        "guardMode": {
                                            "enum": [
                                                "LOOP",
                                                "ROOT",
                                                "NONE"
                                            ],
                                            "type": "string"
                                        },
                                        "interfaceName": {
                                            "minLength": 1,
                                            "type": "string"
                                        },
                                        "pathCost": {
                                            "exclusiveMaximum": true,
                                            "exclusiveMinimum": true,
                                            "maximum": 20000000,
                                            "minimum": 1,
                                            "type": "integer"
                                        },
                                        "portFastMode": {
                                            "enum": [
                                                "NONE",
                                                "DISABLE",
                                                "EDGE",
                                                "EDGE_TRUNK",
                                                "NETWORK",
                                                "TRUNK"
                                            ],
                                            "type": "string"
                                        },
                                        "portVlanCostSettings": {
                                            "properties": {
                                                "configType": {
                                                    "enum": [
                                                        "LIST"
                                                    ],
                                                    "type": "string"
                                                },
                                                "items": {
                                                    "items": {
                                                        "properties": {
                                                            "configType": {
                                                                "enum": [
                                                                    "STP_INTERFACE_VLAN_COST"
                                                                ],
                                                                "type": "string"
                                                            },
                                                            "cost": {
                                                                "exclusiveMaximum": true,
                                                                "exclusiveMinimum": true,
                                                                "maximum": 20000000,
                                                                "minimum": 1,
                                                                "type": "integer"
                                                            },
                                                            "vlans": {
                                                                "minLength": 1,
                                                                "type": "string"
                                                            }
                                                        },
                                                        "required": [
                                                            "cost",
                                                            "vlans"
                                                        ],
                                                        "type": "object"
                                                    },
                                                    "type": "array"
                                                }
                                            },
                                            "type": "object"
                                        },
                                        "portVlanPrioritySettings": {
                                            "properties": {
                                                "configType": {
                                                    "enum": [
                                                        "LIST"
                                                    ],
                                                    "type": "string"
                                                },
                                                "items": {
                                                    "items": {
                                                        "properties": {
                                                            "configType": {
                                                                "enum": [
                                                                    "STP_INTERFACE_VLAN_PRIORITY"
                                                                ],
                                                                "type": "string"
                                                            },
                                                            "priority": {
                                                                "exclusiveMaximum": true,
                                                                "exclusiveMinimum": true,
                                                                "maximum": 240,
                                                                "minimum": 0,
                                                                "type": "integer"
                                                            },
                                                            "vlans": {
                                                                "minLength": 1,
                                                                "type": "string"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "type": "array"
                                                }
                                            },
                                            "type": "object"
                                        },
                                        "priority": {
                                            "exclusiveMaximum": true,
                                            "exclusiveMinimum": true,
                                            "maximum": 240,
                                            "minimum": 0,
                                            "type": "integer"
                                        }
                                    },
                                    "required": [
                                        "interfaceName"
                                    ],
                                    "type": "object"
                                }
                            },
                            "type": "object"
                        },
                        "switchportInterfaceConfig": {
                            "properties": {
                                "items": {
                                    "items": {
                                        "properties": {
                                            "accessVlan": {
                                                "exclusiveMaximum": true,
                                                "exclusiveMinimum": true,
                                                "maximum": 4094,
                                                "minimum": 1,
                                                "type": "integer"
                                            },
                                            "adminStatus": {
                                                "enum": [
                                                    "UP",
                                                    "DOWN"
                                                ],
                                                "type": "string"
                                            },
                                            "configType": {
                                                "enum": [
                                                    "SWITCHPORT_INTERFACE"
                                                ],
                                                "type": "string"
                                            },
                                            "description":
                 {
                                                "maxLength": 230,
                                                "minLength": 1,
                                                "type": "string"
                                            },
                                            "interfaceName": {
                                                "minLength": 1,
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
                                            "nativeVlan": {
                                                "exclusiveMaximum": true,
                                                "exclusiveMinimum": true,
                                                "maximum": 4094,
                                                "minimum": 1,
                                                "type": "integer"
                                            },
                                            "trunkAllowedVlans": {
                                                "maxLength": 218,
                                                "minLength": 1,
                                                "type": "string"
                                            },
                                            "voiceVlan": {
                                                "exclusiveMaximum": true,
                                                "exclusiveMinimum": true,
                                                "maximum": 4094,
                                                "minimum": 1,
                                                "type": "integer"
                                            }
                                        },
                                        "type": "object"
                                    },
                                    "type": "array"
                                }
                            },
                            "type": "object"
                        },
                        "trunkInterfaceConfig": {
                            "properties": {
                                "items": {
                                    "items": {
                                        "properties": {
                                            "configType": {
                                                "enum": [
                                                    "TRUNK_INTERFACE"
                                                ],
                                                "type": "string"
                                            },
                                            "interfaceName": {
                                                "minLength": 1,
                                                "type": "string"
                                            },
                                            "isDtpNegotiationEnabled": {
                                                "type": "boolean"
                                            },
                                            "isProtected": {
                                                "type": "boolean"
                                            },
                                            "pruneEligibleVlans": {
                                                "maxLength": 218,
                                                "minLength": 1,
                                                "type": "string"
                                            }
                                        },
                                        "type": "object"
                                    },
                                    "type": "array"
                                }
                            },
                            "type": "object"
                        },
                        "vlanConfig": {
                            "properties": {
                                "items": {
                                    "items": {
                                        "properties": {
                                            "configType": {
                                                "enum": [
                                                    "VLAN"
                                                ],
                                                "type": "string"
                                            },
                                            "isVlanEnabled": {
                                                "type": "boolean"
                                            },
                                            "name": {
                                                "maxLength": 128,
                                                "type": "string"
                                            },
                                            "vlanId": {
                                                "exclusiveMaximum": true,
                                                "exclusiveMinimum": true,
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
                                    "type": "array"
                                }
                            },
                            "type": "object"
                        },
                        "vtpGlobalConfig": {
                            "properties": {
                                "items": {
                                    "items": {
                                        "properties": {
                                            "configType": {
                                                "enum": [
                                                    "VTP_GLOBAL"
                                                ],
                                                "type": "string"
                                            },
                                            "configurationFileName": {
                                                "maxLength": 244,
                                                "minLength": 1,
                                                "type": "string"
                                            },
                                            "domainName": {
                                                "maxLength": 32,
                                                "minLength": 1,
                                                "type": "string"
                                            },
                                            "isPruningEnabled": {
                                                "type": "boolean"
                                            },
                                            "mode": {
                                                "enum": [
                                                    "SERVER",
                                                    "CLIENT",
                                                    "TRANSPARENT",
                                                    false
                                                ],
                                                "type": "string"
                                            },
                                            "sourceInterface": {
                                                "type": "string"
                                            },
                                            "version": {
                                                "enum": [
                                                    "VERSION_1",
                                                    "VERSION_2",
                                                    "VERSION_3"
                                                ],
                                                "type": "string"
                                            }
                                        },
                                        "type": "object"
                                    },
                                    "maxItems": 1,
                                    "minItems": 1,
                                    "type": "array"
                                }
                            },
                            "type": "object"
                        },
                        "vtpInterfaceConfig": {
                            "properties": {
                                "items": {
                                    "items": {
                                        "properties": {
                                            "configType": {
                                                "enum": [
                                                    "VTP_INTERFACE"
                                                ],
                                                "type": "string"
                                            },
                                            "interfaceName": {
                                                "minLength": 1,
                                                "type": "string"
                                            },
                                            "isVtpEnabled": {
                                                "type": "boolean"
                                            }
                                        },
                                        "type": "object"
                                    },
                                    "type": "array"
                                }
                            },
                            "type": "object"
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
