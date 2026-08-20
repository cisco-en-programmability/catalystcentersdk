"""Cisco Catalyst Center GetDeployedLayer3Configurations data model.

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


class JSONSchemaValidatorF2343F549DB494389Fc73A8D48:
    """GetDeployedLayer3Configurations request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "properties": {
                                "bfdConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "BFD_CONFIG",
                                                        "enum": [
                                                            "BFD_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "ipV6L3Cos": {
                                                        "maximum": 7,
                                                        "minimum": 0,
                                                        "type": "integer"
                                                    },
                                                    "isMoreSnmpTrapsEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    }
                                                },
                                                "required": [
                                                    "configType"
                                                ],
                                                "type": "object"
                                            },
                                            "maxItems": 1,
                                            "type": "array"
                                        }
                                    },
                                    "required": [
                                        "items"
                                    ],
                                    "type": "object"
                                },
                                "bfdTemplateSingleHopConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "BFD_TEMPLATE_SINGLE_HOP_CONFIG",
                                                        "enum": [
                                                            "BFD_TEMPLATE_SINGLE_HOP_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "intervalMultiplier": {
                                                        "default": 3,
                                                        "maximum": 50,
                                                        "minimum": 3,
                                                        "type": "integer"
                                                    },
                                                    "isEchoEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "minRxInterval": {
                                                        "maximum": 9999,
                                                        "minimum": 50,
                                                        "type": "integer"
                                                    },
                                                    "minTxInterval": {
                                                        "maximum": 9999,
                                                        "minimum": 50,
                                                        "type": "integer"
                                                    },
                                                    "name": {
                                                        "maxLength": 255,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "sha1AuthenticationKeychain": {
                                                        "maxLength": 31,
                                                        "minLength": 1,
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
                                    "required": [
                                        "items"
                                    ],
                                    "type": "object"
                                },
                                "dhcpRelayConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "DHCP_RELAY_CONFIG",
                                                        "enum": [
                                                            "DHCP_RELAY_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "isDefaultOptionEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isTrustAllEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isVpnOptionEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
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
                                "ipv4RoutesConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "IPV4_ROUTES_CONFIG",
                                                        "enum": [
                                                            "IPV4_ROUTES_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "forwardingList": {
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
                                                                            "default": "IPV4_FWD_LIST",
                                                                            "enum": [
                                                                                "IPV4_FWD_LIST"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "metric": {
                                                                            "default": 1,
                                                                            "maximum": 255,
                                                                            "minimum": 1,
                                                                            "type": "integer"
                                                                        },
                                                                        "nextHopFwd": {
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
                                                    "mask": {
                                                        "type": "string"
                                                    },
                                                    "prefix": {
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "configType"
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
                                "ipv4RoutingConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "IPV4_ROUTING_CONFIG",
                                                        "enum": [
                                                            "IPV4_ROUTING_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "isRoutingEnabled": {
                                                        "default": true,
                                                        "type": "boolean"
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
                                "ipv4VrfConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "IPV4_VRF_CONFIG",
                                                        "enum": [
                                                            "IPV4_VRF_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "name": {
                                                        "maxLength": 255,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "routeDistinguisher": {
                                                        "maxLength": 255,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "routeTarget": {
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
                                                                            "default": "IPV4_VRF_ROUTE_TARGET",
                                                                            "enum": [
                                                                                "IPV4_VRF_ROUTE_TARGET"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "direction": {
                                                                            "enum": [
                                                                                "IMPORT",
                                                                                "EXPORT"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "target": {
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
                                                        }
                                                    }
                                                },
                                                "required": [
                                                    "configType"
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
                                "ipv4VrfRoutesConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "IPV4_VRF_ROUTES_CONFIG",
                                                        "enum": [
                                                            "IPV4_VRF_ROUTES_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "forwardingList": {
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
                                                                            "default": "IPV4_VRF_INTF_FWD_LIST",
                                                                            "enum": [
                                                                                "IPV4_VRF_INTF_FWD_LIST"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "forwardingList": {
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
                                                                                                "default": "IPV4_VRF_FWD_LIST",
                                                                                                "enum": [
                                                                                                    "IPV4_VRF_FWD_LIST"
                                                                                                ],
                                                                                                "type": "string"
                                                                                            },
                                                                                            "interfaceNextHop": {
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
                                                                                                                    "default": "IPV4_VRF_INTERFACE_NEXT_HOP",
                                                                                                                    "enum": [
                                                                                                                        "IPV4_VRF_INTERFACE_NEXT_HOP"
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
                                                                                            "nextHopFwd": {
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
                                                                        "mask": {
                                                                            "type": "string"
                                                                        },
                                                                        "prefix": {
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
                                                    "vrfName": {
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
                                            "minItems": 0,
                                            "type": "array"
                                        }
                                    },
                                    "required": [
                                        "items"
                                    ],
                                    "type": "object"
                                },
                                "ipv6RoutesConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "IPV6_ROUTES_CONFIG",
                                                        "enum": [
                                                            "IPV6_ROUTES_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "forwardingList": {
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
                                                                            "default": "IPV6_FWD_LIST",
                                                                            "enum": [
                                                                                "IPV6_FWD_LIST"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "interfaceNextHop": {
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
                                                                                                "default": "IPV6_INTERFACE_NEXT_HOP",
                                                                                                "enum": [
                                                                                                    "IPV6_INTERFACE_NEXT_HOP"
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
                                                                        "nextHopFwd": {
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
                                                    "prefix": {
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
                                            "minItems": 0,
                                            "type": "array"
                                        }
                                    },
                                    "required": [
                                        "items"
                                    ],
                                    "type": "object"
                                },
                                "ipv6RoutingConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "IPV6_ROUTING_CONFIG",
                                                        "enum": [
                                                            "IPV6_ROUTING_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "isUnicastRoutingEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    }
                                                },
                                                "required": [
                                                    "configType"
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
                                "ipv6VrfRoutesConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "IPV6_VRF_ROUTES_CONFIG",
                                                        "enum": [
                                                            "IPV6_VRF_ROUTES_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "forwardingList": {
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
                                                                            "default": "IPV6_VRF_INTF_FWD_LIST",
                                                                            "enum": [
                                                                                "IPV6_VRF_INTF_FWD_LIST"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "forwardingList": {
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
                                                                                                "default": "IPV6_VRF_FWD_LIST",
                                                                                                "enum": [
                                                                                                    "IPV6_VRF_FWD_LIST"
                                                                                                ],
                                                                                                "type": "string"
                                                                                            },
                                                                                            "interfaceNextHop": {
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
                                                                                                                    "default": "IPV6_VRF_INTERFACE_NEXT_HOP",
                                                                                                                    "enum": [
                                                                                                                        "IPV6_VRF_INTERFACE_NEXT_HOP"
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
                                                                                            "nextHopFwd": {
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
                                                                        "prefix": {
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
                                                    "vrfName": {
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
                                            "minItems": 0,
                                            "type": "array"
                                        }
                                    },
                                    "required": [
                                        "items"
                                    ],
                                    "type": "object"
                                },
                                "loopbackConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
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
                                                        "maxLength": 32,
                                                        "minLength": 1,
                                                        "type": "string"
                                                    },
                                                    "configType": {
                                                        "default": "LOOPBACK_CONFIG",
                                                        "enum": [
                                                            "LOOPBACK_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "description":
                 {
                                                        "maxLength": 200,
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
                                                                            "default": "LOOPBACK_IPV6_DHCP_RELAY_DEST_ADDRESS",
                                                                            "enum": [
                                                                                "LOOPBACK_IPV6_DHCP_RELAY_DEST_ADDRESS"
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
                                                    "ipV6DhcpServerAddress": {
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
                                                                            "default": "LOOPBACK_IPV6_DHCP_SERVER_ADDRESS",
                                                                            "enum": [
                                                                                "LOOPBACK_IPV6_DHCP_SERVER_ADDRESS"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "dhcpServerPool": {
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
                                                                            "default": "LOOPBACK_IPV6_PREFIX_LIST",
                                                                            "enum": [
                                                                                "LOOPBACK_IPV6_PREFIX_LIST"
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
                                                    "ipVrfName": {
                                                        "maxLength": 32,
                                                        "minLength": 1,
                                                        "type": "string"
                                                    },
                                                    "isBfdEnabled": {
                                                        "default": true,
                                                        "type": "boolean"
                                                    },
                                                    "isBfdIntervalEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isDhcpEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isDhcpRelayInfoTrusted": {
                                                        "default": false,
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
                                                    "isIpV6Enabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isProxyArpEnabled": {
                                                        "default": true,
                                                        "type": "boolean"
                                                    },
                                                    "isRedirectsEnabled": {
                                                        "default": true,
                                                        "type": "boolean"
                                                    },
                                                    "isShutdownEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "loopbackNumber": {
                                                        "maximum": 2147483647,
                                                        "minimum": 0,
                                                        "type": "integer"
                                                    },
                                                    "primaryIpAddress": {
                                                        "type": "string"
                                                    },
                                                    "primaryMask": {
                                                        "type": "string"
                                                    },
                                                    "secondaryAddresses": {
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
                                                                            "default": "LOOPBACK_SECONDARY_ADDRESS",
                                                                            "enum": [
                                                                                "LOOPBACK_SECONDARY_ADDRESS"
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
                                                    "vrfName": {
                                                        "maxLength": 32,
                                                        "minLength": 1,
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "configType"
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
                                "sviConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
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
                                                        "maxLength": 64,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "configType": {
                                                        "default": "SVI_CONFIG",
                                                        "enum": [
                                                            "SVI_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "description":
                 {
                                                        "maxLength": 200,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "dhcpClientId": {
                                                        "maxLength": 200,
                                                        "minLength": 1,
                                                        "type": "string"
                                                    },
                                                    "dhcpRelaySourceInterface": {
                                                        "maxLength": 255,
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
                                                                            "default": "SVI_HELPER_ADDRESS",
                                                                            "enum": [
                                                                                "SVI_HELPER_ADDRESS"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "ipAddress": {
                                                                            "type": "string"
                                                                        },
                                                                        "vrfName": {
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
                                                    "igmpVersion": {
                                                        "default": 2,
                                                        "maximum": 3,
                                                        "minimum": 1,
                                                        "type": "integer"
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
                                                    "ipV4Unnumbered": {
                                                        "maxLength": 64,
                                                        "minLength": 1,
                                                        "type": "string"
                                                    },
                                                    "ipV6AddressPrefixList": {
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
                                                                            "default": "SVI_IPV6_ADDRESS_PREFIX_LIST",
                                                                            "enum": [
                                                                                "SVI_IPV6_ADDRESS_PREFIX_LIST"
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
                                                    "ipV6DhcpRelayDestinationAddress": {
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
                                                                            "default": "SVI_IPV6_DHCP_RELAY_DEST_ADDRESS",
                                                                            "enum": [
                                                                                "SVI_IPV6_DHCP_RELAY_DEST_ADDRESS"
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
                                                                            "default": "SVI_IPV6_DHCP_RELAY_DEST_GLOBAL",
                                                                            "enum": [
                                                                                "SVI_IPV6_DHCP_RELAY_DEST_GLOBAL"
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
                                                    "ipV6DhcpRelayLoopbackSrcInterface": {
                                                        "maximum": 2147483647,
                                                        "minimum": 0,
                                                        "type": "integer"
                                                    },
                                                    "ipV6DhcpServer": {
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
                                                                            "default": "SVI_IPV6_DHCP_SERVER",
                                                                            "enum": [
                                                                                "SVI_IPV6_DHCP_SERVER"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "dhcpServerPool": {
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
                                                    "ipV6UnnumberedInterface": {
                                                        "maxLength": 255,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "ipVrfName": {
                                                        "maxLength": 255,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "isAutostateEnabled": {
                                                        "default": true,
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
                                                    "isDhcpEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isDhcpRelayInfoOptionVpnIdEnabled": {
                                                        "default": false,
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
                                                    "isIpV6DhcpClientReqVendorEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isIpV6DhcpEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isIpV6DhcpRelayOptionVpnEnabled": {
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
                                                    "isIpv6DhcpRelayTrustEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isProxyArpEnabled": {
                                                        "default": true,
                                                        "type": "boolean"
                                                    },
                                                    "isRedirectsEnabled": {
                                                        "default": true,
                                                        "type": "boolean"
                                                    },
                                                    "isShutdownEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "macAddress": {
                                                        "maxLength": 255,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "primaryAddress": {
                                                        "type": "string"
                                                    },
                                                    "primaryMask": {
                                                        "type": "string"
                                                    },
                                                    "secondaryAddresses": {
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
                                                                            "default": "SVI_SECONDARY_ADDRESS",
                                                                            "enum": [
                                                                                "SVI_SECONDARY_ADDRESS"
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
                                                    "trafficFilter": {
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
                                                                        "accessListName": {
                                                                            "type": "string"
                                                                        },
                                                                        "configType": {
                                                                            "default": "SVI_IPV6_TRAFFIC_FILTER",
                                                                            "enum": [
                                                                                "SVI_IPV6_TRAFFIC_FILTER"
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
                                                                        "configType"
                                                                    ],
                                                                    "type": "object"
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "vlanId": {
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
                                                    "configType"
                                                ],
                                                "type": "object"
                                            },
                                            "maxItems": 2048,
                                            "minItems": 1,
                                            "type": "array"
                                        }
                                    },
                                    "required": [
                                        "items"
                                    ],
                                    "type": "object"
                                },
                                "vrfConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "VRF_CONFIG",
                                                        "enum": [
                                                            "VRF_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "description":
                 {
                                                        "maxLength": 244,
                                                        "minLength": 1,
                                                        "type": "string"
                                                    },
                                                    "ipV4ExportRouteTargetWithoutStitching": {
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
                                                                        "asnIp": {
                                                                            "type": "string"
                                                                        },
                                                                        "configType": {
                                                                            "default": "VRF_DEF_AF_IPV4_ERT_WITHOUT_STITCH",
                                                                            "enum": [
                                                                                "VRF_DEF_AF_IPV4_ERT_WITHOUT_STITCH"
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
                                                    "ipV4ImportRouteTargetWithoutStitching": {
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
                                                                        "asnIp": {
                                                                            "type": "string"
                                                                        },
                                                                        "configType": {
                                                                            "default": "VRF_DEF_AF_IPV4_IRT_WITHOUT_STITCH",
                                                                            "enum": [
                                                                                "VRF_DEF_AF_IPV4_IRT_WITHOUT_STITCH"
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
                                                    "ipV6ExportRouteTargetWithoutStitching": {
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
                                                                        "asnIp": {
                                                                            "type": "string"
                                                                        },
                                                                        "configType": {
                                                                            "default": "VRF_DEF_AF_IPV6_ERT_WITHOUT_STITCH",
                                                                            "enum": [
                                                                                "VRF_DEF_AF_IPV6_ERT_WITHOUT_STITCH"
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
                                                    "ipV6ImportRouteTargetWithoutStitching": {
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
                                                                        "asnIp": {
                                                                            "type": "string"
                                                                        },
                                                                        "configType": {
                                                                            "default": "VRF_DEF_AF_IPV6_IRT_WITHOUT_STITCH",
                                                                            "enum": [
                                                                                "VRF_DEF_AF_IPV6_IRT_WITHOUT_STITCH"
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
                                                    "isIpV4AddressFamilyEnabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "isIpV6Enabled": {
                                                        "default": false,
                                                        "type": "boolean"
                                                    },
                                                    "name": {
                                                        "type": "string"
                                                    },
                                                    "routeDistinguisher": {
                                                        "type": "string"
                                                    },
                                                    "routeTargetExport": {
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
                                                                        "asnIp": {
                                                                            "type": "string"
                                                                        },
                                                                        "configType": {
                                                                            "default": "ROUTE_TARGET_EXPORT",
                                                                            "enum": [
                                                                                "ROUTE_TARGET_EXPORT"
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
                                                    "routeTargetImport": {
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
                                                                        "asnIp": {
                                                                            "type": "string"
                                                                        },
                                                                        "configType": {
                                                                            "default": "ROUTE_TARGET_IMPORT",
                                                                            "enum": [
                                                                                "ROUTE_TARGET_IMPORT"
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
                                                    }
                                                },
                                                "required": [
                                                    "configType"
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
