"""Cisco Catalyst Center GetDeployedLayer2Configurations data model.

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


class JSONSchemaValidatorB5E8D2FbD8Dc5094A82F37C49Ebc4A9D:
    """GetDeployedLayer2Configurations request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "properties": {
                                "cdpConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "CDP_CONFIG",
                                                        "enum": [
                                                            "CDP_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "holdtime": {
                                                        "default": 180,
                                                        "maximum": 255,
                                                        "minimum": 10,
                                                        "type": "integer"
                                                    },
                                                    "isAdvertiseV2Enabled": {
                                                        "default": true,
                                                        "type": "boolean"
                                                    },
                                                    "isCdpEnabled": {
                                                        "default": true,
                                                        "type": "boolean"
                                                    },
                                                    "timer": {
                                                        "default": 60,
                                                        "maximum": 254,
                                                        "minimum": 5,
                                                        "type": "integer"
                                                    }
                                                },
                                                "required": [
                                                    "configType"
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
                                "etherchannelConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "ETHERCHANNEL_CONFIG",
                                                        "enum": [
                                                            "ETHERCHANNEL_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "isAutoEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "lacpSystemPriority": {
                                                        "default": 32768,
                                                        "maximum": 65535,
                                                        "minimum": 0,
                                                        "type": "integer"
                                                    },
                                                    "loadBalancingMethod": {
                                                        "default": "SRC_MAC",
                                                        "enum": [
                                                            "DST_IP",
                                                            "DST_MAC",
                                                            "DST_MIXED_IP_PORT",
                                                            "DST_PORT",
                                                            "SRC_DST_IP",
                                                            "SRC_DST_MAC",
                                                            "SRC_DST_MIXED_IP_PORT",
                                                            "SRC_DST_PORT",
                                                            "SRC_IP",
                                                            "SRC_MAC",
                                                            "SRC_MIXED_IP_PORT",
                                                            "SRC_PORT",
                                                            "VLAN_DST_IP",
                                                            "VLAN_DST_MIXED_IP_PORT",
                                                            "VLAN_SRC_DST_IP",
                                                            "VLAN_SRC_DST_MIXED_IP_PORT",
                                                            "VLAN_SRC_IP",
                                                            "VLAN_SRC_MIXED_IP_PORT"
                                                        ],
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "configType"
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
                                "igmpSnoopingConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "IGMP_SNOOPING_CONFIG",
                                                        "enum": [
                                                            "IGMP_SNOOPING_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "igmpSnoopingQuerierEntry": {
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
                                                                            "default": "IGMP_SNOOPING_QUERIER_ENTRY_CONFIG",
                                                                            "enum": [
                                                                                "IGMP_SNOOPING_QUERIER_ENTRY_CONFIG"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "querierAddress": {
                                                                            "type": "string"
                                                                        },
                                                                        "querierVersion": {
                                                                            "default": 2,
                                                                            "maximum": 3,
                                                                            "minimum": 1,
                                                                            "type": "integer"
                                                                        },
                                                                        "queryInterval": {
                                                                            "default": 60,
                                                                            "maximum": 18000,
                                                                            "minimum": 1,
                                                                            "type": "integer"
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
                                                    "igmpSnoopingVlans": {
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
                                                                            "default": "IGMP_SNOOPING_VLANS_CONFIG",
                                                                            "enum": [
                                                                                "IGMP_SNOOPING_VLANS_CONFIG"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "isImmediateLeaveEnabled": {
                                                                            "default": false,
                                                                            "type": "boolean"
                                                                        },
                                                                        "isQuerierEnabled": {
                                                                            "default": false,
                                                                            "type": "boolean"
                                                                        },
                                                                        "mrouterInterface": {
                                                                            "minLength": 1,
                                                                            "type": "string"
                                                                        },
                                                                        "querierAddress": {
                                                                            "type": "string"
                                                                        },
                                                                        "querierVersion": {
                                                                            "maximum": 2,
                                                                            "minimum": 1,
                                                                            "type": "integer"
                                                                        },
                                                                        "queryInterval": {
                                                                            "maximum": 18000,
                                                                            "minimum": 1,
                                                                            "type": "integer"
                                                                        },
                                                                        "vlanId": {
                                                                            "maximum": 4094,
                                                                            "minimum": 1,
                                                                            "type": "integer"
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
                                                    "isIgmpSnoopingEnabled": {
                                                        "default": true,
                                                        "type": "boolean"
                                                    },
                                                    "isQuerierEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "lastMemberQueryInterval": {
                                                        "default": 1000,
                                                        "maximum": 32767,
                                                        "minimum": 100,
                                                        "type": "integer"
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
                                    "required": [
                                        "items"
                                    ],
                                    "type": "object"
                                },
                                "lldpConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "LLDP_CONFIG",
                                                        "enum": [
                                                            "LLDP_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "holdtime": {
                                                        "default": 120,
                                                        "maximum": 65535,
                                                        "minimum": 0,
                                                        "type": "integer"
                                                    },
                                                    "isLldpEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "reinitializationDelay": {
                                                        "default": 2,
                                                        "maximum": 5,
                                                        "minimum": 2,
                                                        "type": "integer"
                                                    },
                                                    "timer": {
                                                        "default": 30,
                                                        "maximum": 65534,
                                                        "minimum": 5,
                                                        "type": "integer"
                                                    }
                                                },
                                                "required": [
                                                    "configType"
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
                                "macAddressTableConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "agingTime": {
                                                        "default": 300,
                                                        "maximum": 1000000,
                                                        "minimum": 0,
                                                        "type": "integer"
                                                    },
                                                    "configType": {
                                                        "default": "MAC_ADDRESS_TABLE_CONFIG",
                                                        "enum": [
                                                            "MAC_ADDRESS_TABLE_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "isChangeNotificationEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isMacMoveEnabled": {
                                                        "default": true,
                                                        "type": "boolean"
                                                    },
                                                    "isNotificationThresholdEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "macAddressTableStatic": {
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
                                                                            "default": "MAC_ADDRESS_TABLE_STATIC_CONFIG",
                                                                            "enum": [
                                                                                "MAC_ADDRESS_TABLE_STATIC_CONFIG"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "destinationInterface": {
                                                                            "maxLength": 191,
                                                                            "minLength": 0,
                                                                            "type": "string"
                                                                        },
                                                                        "isDropEnabled": {
                                                                            "default": false,
                                                                            "type": "boolean"
                                                                        },
                                                                        "macAddress": {
                                                                            "maxLength": 255,
                                                                            "minLength": 0,
                                                                            "type": "string"
                                                                        },
                                                                        "vlanId": {
                                                                            "maximum": 4094,
                                                                            "minimum": 1,
                                                                            "type": "integer"
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
                                                    "macAddressTableVlanAgingTime": {
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
                                                                        "agingTime": {
                                                                            "default": 300,
                                                                            "maximum": 1000000,
                                                                            "minimum": 0,
                                                                            "type": "integer"
                                                                        },
                                                                        "configType": {
                                                                            "default": "MAC_ADDRESS_TABLE_VLAN_AGING_TIME_CONFIG",
                                                                            "enum": [
                                                                                "MAC_ADDRESS_TABLE_VLAN_AGING_TIME_CONFIG"
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
                                                                        "configType"
                                                                    ],
                                                                    "type": "object"
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "notificationChangeHistorySize": {
                                                        "default": 1,
                                                        "maximum": 500,
                                                        "minimum": 0,
                                                        "type": "integer"
                                                    },
                                                    "notificationChangeInterval": {
                                                        "default": 1,
                                                        "maximum": 2147483647,
                                                        "minimum": 0,
                                                        "type": "integer"
                                                    },
                                                    "notificationThresholdInterval": {
                                                        "default": 120,
                                                        "maximum": 1000000,
                                                        "minimum": 120,
                                                        "type": "integer"
                                                    },
                                                    "notificationThresholdLimit": {
                                                        "default": 50,
                                                        "maximum": 100,
                                                        "minimum": 0,
                                                        "type": "integer"
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
                                    "required": [
                                        "items"
                                    ],
                                    "type": "object"
                                },
                                "mldSnoopingConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "MLD_SNOOPING_CONFIG",
                                                        "enum": [
                                                            "MLD_SNOOPING_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "isListenerMessageSuppressionEnabled": {
                                                        "default": true,
                                                        "type": "boolean"
                                                    },
                                                    "isMldSnoopingEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isQuerierEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "lastListenerQueryInterval": {
                                                        "default": 1000,
                                                        "maximum": 32768,
                                                        "minimum": 100,
                                                        "type": "integer"
                                                    },
                                                    "mldSnoopingQuerierEntry": {
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
                                                                            "default": "MLD_SNOOPING_QUERIER_CONFIG",
                                                                            "enum": [
                                                                                "MLD_SNOOPING_QUERIER_CONFIG"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "querierAddress": {
                                                                            "type": "string"
                                                                        },
                                                                        "querierVersion": {
                                                                            "default": 1,
                                                                            "maximum": 2,
                                                                            "minimum": 1,
                                                                            "type": "integer"
                                                                        },
                                                                        "queryInterval": {
                                                                            "default": 125,
                                                                            "maximum": 18000,
                                                                            "minimum": 1,
                                                                            "type": "integer"
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
                                                    "mldSnoopingVlans": {
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
                                                                            "default": "MLD_SNOOPING_VLAN_CONFIG",
                                                                            "enum": [
                                                                                "MLD_SNOOPING_VLAN_CONFIG"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "isImmediateLeaveEnabled": {
                                                                            "default": false,
                                                                            "type": "boolean"
                                                                        },
                                                                        "isQuerierEnabled": {
                                                                            "default": false,
                                                                            "type": "boolean"
                                                                        },
                                                                        "mrouterInterface": {
                                                                            "minLength": 1,
                                                                            "type": "string"
                                                                        },
                                                                        "querierAddress": {
                                                                            "type": "string"
                                                                        },
                                                                        "querierVersion": {
                                                                            "default": 1,
                                                                            "maximum": 2,
                                                                            "minimum": 1,
                                                                            "type": "integer"
                                                                        },
                                                                        "queryInterval": {
                                                                            "default": 125,
                                                                            "maximum": 18000,
                                                                            "minimum": 1,
                                                                            "type": "integer"
                                                                        },
                                                                        "vlanId": {
                                                                            "maximum": 4094,
                                                                            "minimum": 1,
                                                                            "type": "integer"
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
                                    "required": [
                                        "items"
                                    ],
                                    "type": "object"
                                },
                                "stpConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "STP_CONFIG",
                                                        "enum": [
                                                            "STP_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "isBackboneFastEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isBpduFilterEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isBpduGuardEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isEtherChannelGuardEnabled": {
                                                        "default": true,
                                                        "type": "boolean"
                                                    },
                                                    "isExtendedSystemIdEnabled": {
                                                        "default": true,
                                                        "type": "boolean"
                                                    },
                                                    "isLoggingEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isLoopGuardEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isUplinkFastEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "portFastMode": {
                                                        "default": "NONE",
                                                        "enum": [
                                                            "ENABLE",
                                                            "EDGE",
                                                            "NETWORK",
                                                            "NONE"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "stpMode": {
                                                        "default": "RAPID_PVST",
                                                        "enum": [
                                                            "RAPID_PVST",
                                                            "MST",
                                                            "PVST"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "transmitHoldCount": {
                                                        "default": 6,
                                                        "maximum": 20,
                                                        "minimum": 1,
                                                        "type": "integer"
                                                    },
                                                    "uplinkFastMaxUpdateRate": {
                                                        "default": 150,
                                                        "maximum": 32000,
                                                        "minimum": 0,
                                                        "type": "integer"
                                                    },
                                                    "vlanConfig": {
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
                                                                            "default": "STP_VLAN_CONFIG",
                                                                            "enum": [
                                                                                "STP_VLAN_CONFIG"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "forwardDelay": {
                                                                            "default": 15,
                                                                            "maximum": 30,
                                                                            "minimum": 4,
                                                                            "type": "integer"
                                                                        },
                                                                        "helloInterval": {
                                                                            "default": 2,
                                                                            "maximum": 10,
                                                                            "minimum": 1,
                                                                            "type": "integer"
                                                                        },
                                                                        "maxAge": {
                                                                            "default": 20,
                                                                            "maximum": 40,
                                                                            "minimum": 6,
                                                                            "type": "integer"
                                                                        },
                                                                        "priority": {
                                                                            "default": 32768,
                                                                            "maximum": 61440,
                                                                            "minimum": 0,
                                                                            "multipleOf": 4096,
                                                                            "type": "integer"
                                                                        },
                                                                        "vlan": {
                                                                            "maximum": 4094,
                                                                            "minimum": 1,
                                                                            "type": "integer"
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
                                                    }
                                                },
                                                "required": [
                                                    "configType"
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
                                "udldConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "UDLD_CONFIG",
                                                        "enum": [
                                                            "UDLD_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "isAggressiveEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isRecoveryEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isUdldEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "messageTime": {
                                                        "default": 15,
                                                        "maximum": 90,
                                                        "minimum": 1,
                                                        "type": "integer"
                                                    },
                                                    "recoveryInterval": {
                                                        "maximum": 86400,
                                                        "minimum": 30,
                                                        "type": "integer"
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
                                    "required": [
                                        "items"
                                    ],
                                    "type": "object"
                                },
                                "vlanConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "VLAN_CONFIG",
                                                        "enum": [
                                                            "VLAN_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "isRemoteSpanEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "name": {
                                                        "maxLength": 128,
                                                        "minLength": 1,
                                                        "type": "string"
                                                    },
                                                    "state": {
                                                        "default": "ACTIVE",
                                                        "enum": [
                                                            "ACTIVE",
                                                            "SUSPEND"
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
                                                    "configType"
                                                ],
                                                "type": "object"
                                            },
                                            "maxItems": 4094,
                                            "minItems": 1,
                                            "type": "array"
                                        }
                                    },
                                    "required": [
                                        "items"
                                    ],
                                    "type": "object"
                                },
                                "vtpConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "VTP_CONFIG",
                                                        "enum": [
                                                            "VTP_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "configurationFileName": {
                                                        "maxLength": 244,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "domainName": {
                                                        "maxLength": 32,
                                                        "minLength": 1,
                                                        "type": "string"
                                                    },
                                                    "interfaceName": {
                                                        "type": "string"
                                                    },
                                                    "isPruningEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isServerPrimary": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "mode": {
                                                        "default": "SERVER",
                                                        "enum": [
                                                            "SERVER",
                                                            "CLIENT",
                                                            "TRANSPARENT",
                                                            false
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "version": {
                                                        "default": 1,
                                                        "maximum": 3,
                                                        "minimum": 1,
                                                        "type": "integer"
                                                    }
                                                },
                                                "required": [
                                                    "configType"
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
