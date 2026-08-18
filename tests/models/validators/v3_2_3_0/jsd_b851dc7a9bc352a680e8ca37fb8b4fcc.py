"""Cisco Catalyst Center GetIntendedNetworkSettingsConfigurations data model.

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


class JSONSchemaValidatorB851Dc7A9Bc352A680E8Ca37Fb8B4Fcc:
    """GetIntendedNetworkSettingsConfigurations request schema
    definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "properties": {
                                "dhcpExcludedAddressConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "DHCP_EXCLUDED_ADDRESS_LIST_CONFIG",
                                                        "enum": [
                                                            "DHCP_EXCLUDED_ADDRESS_LIST_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "ipDhcpExcludedLowAddressConfig": {
                                                        "properties": {
                                                            "items": {
                                                                "items": {
                                                                    "properties": {
                                                                        "configType": {
                                                                            "default": "DHCP_EXCLUDED_LOW_ADDRESS_LIST_CONFIG",
                                                                            "enum": [
                                                                                "DHCP_EXCLUDED_LOW_ADDRESS_LIST_CONFIG"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "excludedAddressLow": {
                                                                            "type": "string"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "excludedAddressLow"
                                                                    ],
                                                                    "type": "object"
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "ipDhcpExcludedLowHighAddressConfig": {
                                                        "properties": {
                                                            "items": {
                                                                "items": {
                                                                    "properties": {
                                                                        "configType": {
                                                                            "default": "DHCP_EXCLUDED_LOW_HIGH_ADDRESS_LIST_CONFIG",
                                                                            "enum": [
                                                                                "DHCP_EXCLUDED_LOW_HIGH_ADDRESS_LIST_CONFIG"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "excludedAddressHigh": {
                                                                            "type": "string"
                                                                        },
                                                                        "excludedAddressLow": {
                                                                            "type": "string"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "excludedAddressHigh",
                                                                        "excludedAddressLow"
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
                                            "minItems": 1,
                                            "type": "array"
                                        }
                                    },
                                    "required": [
                                        "items"
                                    ],
                                    "type": "object"
                                },
                                "dhcpGeneralConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "DHCP_GENERAL_CONFIG",
                                                        "enum": [
                                                            "DHCP_GENERAL_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "isBootpIgnoreEnabled": {
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
                                "domainConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "IP_DOMAIN_CONFIG",
                                                        "enum": [
                                                            "IP_DOMAIN_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "domainName": {
                                                        "maxLength": 236,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "ipDomainList": {
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
                                                                            "default": "IP_DOMAIN_LIST_CONFIG",
                                                                            "enum": [
                                                                                "IP_DOMAIN_LIST_CONFIG"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "domainNameList": {
                                                                            "maxLength": 236,
                                                                            "minLength": 0,
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
                                                    "ipDomainName": {
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
                                                                            "default": "IP_DOMAIN_NAME_CONFIG",
                                                                            "enum": [
                                                                                "IP_DOMAIN_NAME_CONFIG"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "domainWithVrf": {
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
                                                                                                "default": "IP_DOMAIN_WITH_VRF_CONFIG",
                                                                                                "enum": [
                                                                                                    "IP_DOMAIN_WITH_VRF_CONFIG"
                                                                                                ],
                                                                                                "type": "string"
                                                                                            },
                                                                                            "domainName": {
                                                                                                "maxLength": 236,
                                                                                                "minLength": 0,
                                                                                                "type": "string"
                                                                                            },
                                                                                            "vrfName": {
                                                                                                "maxLength": 255,
                                                                                                "minLength": 0,
                                                                                                "type": "string"
                                                                                            }
                                                                                        },
                                                                                        "required": [
                                                                                            "vrfName"
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
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "isLookupEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "sourceLoopbackInterface": {
                                                        "maximum": 2147483647,
                                                        "minimum": -1,
                                                        "type": "integer"
                                                    },
                                                    "timeout": {
                                                        "maximum": 3600,
                                                        "minimum": 1,
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
                                "ipV4DhcpPoolConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "IPV4_DHCP_POOL_CONFIG",
                                                        "enum": [
                                                            "IPV4_DHCP_POOL_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "defaultRouterList": {
                                                        "maxLength": 255,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "dnsServerList": {
                                                        "maxLength": 255,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "domainName": {
                                                        "maxLength": 255,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "leaseDays": {
                                                        "maximum": 365,
                                                        "minimum": 0,
                                                        "type": "integer"
                                                    },
                                                    "leaseHours": {
                                                        "maximum": 23,
                                                        "minimum": 0,
                                                        "type": "integer"
                                                    },
                                                    "leaseMinutes": {
                                                        "maximum": 59,
                                                        "minimum": 0,
                                                        "type": "integer"
                                                    },
                                                    "optionCode": {
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
                                                                        "asciiString": {
                                                                            "maxLength": 225,
                                                                            "minLength": 0,
                                                                            "type": "string"
                                                                        },
                                                                        "configType": {
                                                                            "default": "OPTION_RANGE_CONFIG",
                                                                            "enum": [
                                                                                "OPTION_RANGE_CONFIG"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "hexadecimalString": {
                                                                            "maxLength": 180,
                                                                            "minLength": 0,
                                                                            "type": "string"
                                                                        },
                                                                        "ipAddressString": {
                                                                            "maxLength": 255,
                                                                            "minLength": 0,
                                                                            "type": "string"
                                                                        },
                                                                        "ipAddresses": {
                                                                            "maxLength": 255,
                                                                            "minLength": 0,
                                                                            "type": "string"
                                                                        },
                                                                        "optionCode": {
                                                                            "maximum": 254,
                                                                            "minimum": 0,
                                                                            "type": "integer"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "optionCode"
                                                                    ],
                                                                    "type": "object"
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "poolName": {
                                                        "maxLength": 236,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "primaryNetworkMask": {
                                                        "maxLength": 255,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "primaryNetworkNumber": {
                                                        "maxLength": 255,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "vrfName": {
                                                        "maxLength": 32,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "poolName"
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
                                "ipV6DhcpPoolConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "IPV6_DHCP_POOL_CONFIG",
                                                        "enum": [
                                                            "IPV6_DHCP_POOL_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "dnsServer": {
                                                        "maxLength": 255,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "domainNames": {
                                                        "maxLength": 255,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "poolName": {
                                                        "maxLength": 232,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "prefix": {
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
                                                                            "default": "PREFIX_CONFIG",
                                                                            "enum": [
                                                                                "PREFIX_CONFIG"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "ipV6Prefix": {
                                                                            "maxLength": 255,
                                                                            "minLength": 0,
                                                                            "type": "string"
                                                                        },
                                                                        "poolName": {
                                                                            "maxLength": 232,
                                                                            "minLength": 0,
                                                                            "type": "string"
                                                                        },
                                                                        "preferredLifetime": {
                                                                            "maximum": 4294967295,
                                                                            "minimum": 5,
                                                                            "type": "integer"
                                                                        },
                                                                        "validLifetime": {
                                                                            "maximum": 4294967295,
                                                                            "minimum": 5,
                                                                            "type": "integer"
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
                                                    "poolName"
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
                                "nameServerConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "NAME_SERVER_CONFIG",
                                                        "enum": [
                                                            "NAME_SERVER_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "nameServerWithVrf": {
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
                                                                            "default": "NAME_SERVER_VRF_CONFIG",
                                                                            "enum": [
                                                                                "NAME_SERVER_VRF_CONFIG"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "nameServers": {
                                                                            "maxLength": 255,
                                                                            "minLength": 0,
                                                                            "type": "string"
                                                                        },
                                                                        "vrfName": {
                                                                            "maxLength": 32,
                                                                            "minLength": 0,
                                                                            "type": "string"
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "vrfName"
                                                                    ],
                                                                    "type": "object"
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "nameServers": {
                                                        "maxLength": 255,
                                                        "minLength": 0,
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
                                    "required": [
                                        "items"
                                    ],
                                    "type": "object"
                                },
                                "ntpAuthenticationKeyConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "NTP_AUTH_KEY_CONFIG",
                                                        "enum": [
                                                            "NTP_AUTH_KEY_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "encryptionType": {
                                                        "maximum": 7,
                                                        "minimum": 0,
                                                        "type": "integer"
                                                    },
                                                    "keyNumber": {
                                                        "maximum": 4294967295,
                                                        "minimum": 1,
                                                        "type": "integer"
                                                    },
                                                    "md5": {
                                                        "maxLength": 255,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "md5Config": {
                                                        "maxLength": 32,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "keyNumber",
                                                    "md5Config"
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
                                "ntpGeneralConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "NTP_GENERAL_CONFIG",
                                                        "enum": [
                                                            "NTP_GENERAL_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "isAuthenticateEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "isLoggingEnabled": {
                                                        "type": "boolean"
                                                    },
                                                    "sourceLoopbackInterface": {
                                                        "maximum": 2147483647,
                                                        "minimum": -1,
                                                        "type": "integer"
                                                    },
                                                    "stratum": {
                                                        "maximum": 15,
                                                        "minimum": 1,
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
                                "ntpPerVrfServerConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "NTP_PER_VRF_SERVER_CONFIG",
                                                        "enum": [
                                                            "NTP_PER_VRF_SERVER_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "ntpVrfServerList": {
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
                                                                            "default": "NTP_VRF_SERVER_LIST_CONFIG",
                                                                            "enum": [
                                                                                "NTP_VRF_SERVER_LIST_CONFIG"
                                                                            ],
                                                                            "type": "string"
                                                                        },
                                                                        "ipAddress": {
                                                                            "maxLength": 64,
                                                                            "minLength": 0,
                                                                            "type": "string"
                                                                        },
                                                                        "isPreferred": {
                                                                            "type": "boolean"
                                                                        },
                                                                        "peerAuthenticationKey": {
                                                                            "maximum": 4294967295,
                                                                            "minimum": 0,
                                                                            "type": "integer"
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
                                                    "vrfName": {
                                                        "maxLength": 32,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "vrfName"
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
                                "ntpServerConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "NTP_SERVER_CONFIG",
                                                        "enum": [
                                                            "NTP_SERVER_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "ipAddress": {
                                                        "maxLength": 64,
                                                        "minLength": 0,
                                                        "type": "string"
                                                    },
                                                    "isPreferred": {
                                                        "type": "boolean"
                                                    },
                                                    "peerAuthenticationKey": {
                                                        "maximum": 4294967295,
                                                        "minimum": 0,
                                                        "type": "integer"
                                                    },
                                                    "sourceInterface": {
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
                                            "minItems": 1,
                                            "type": "array"
                                        }
                                    },
                                    "required": [
                                        "items"
                                    ],
                                    "type": "object"
                                },
                                "ntpTrustedKeyConfig": {
                                    "properties": {
                                        "items": {
                                            "items": {
                                                "properties": {
                                                    "configType": {
                                                        "default": "NTP_TRUSTED_KEY_CONFIG",
                                                        "enum": [
                                                            "NTP_TRUSTED_KEY_CONFIG"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "trustedKey": {
                                                        "maximum": 65535,
                                                        "minimum": 1,
                                                        "type": "integer"
                                                    }
                                                },
                                                "required": [
                                                    "trustedKey"
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
