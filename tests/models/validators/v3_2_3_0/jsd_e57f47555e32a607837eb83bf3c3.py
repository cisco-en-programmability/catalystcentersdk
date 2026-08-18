"""Cisco Catalyst Center FetchesAllDiscoveryDetails data model.

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


class JSONSchemaValidatorE57F47555E32A607837Eb83Bf3C3:
    """FetchesAllDiscoveryDetails request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "items": {
                                "properties": {
                                    "credentials": {
                                        "properties": {
                                            "cli": {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "properties": {
                                                                    "description":
                 {
                                                                        "type": "string"
                                                                    },
                                                                    "enablePassword": {
                                                                        "type": "string"
                                                                    },
                                                                    "password": {
                                                                        "type": "string"
                                                                    },
                                                                    "username": {
                                                                        "type": "string"
                                                                    }
                                                                },
                                                                "required": [
                                                                    "description",
                                                                    "password",
                                                                    "username"
                                                                ],
                                                                "type": "object"
                                                            },
                                                            {
                                                                "properties": {
                                                                    "globalCredentialIdList": {
                                                                        "items": {
                                                                            "type": "string"
                                                                        },
                                                                        "maxItems": 5,
                                                                        "type": "array"
                                                                    }
                                                                },
                                                                "type": "object"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "properties": {
                                                            "protocolOrder": {
                                                                "items": {
                                                                    "enum": [
                                                                        "SSH",
                                                                        "TELNET"
                                                                    ],
                                                                    "type": "string"
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    }
                                                ]
                                            },
                                            "httpRead": {
                                                "anyOf": [
                                                    {
                                                        "properties": {
                                                            "description":
                 {
                                                                "type": "string"
                                                            },
                                                            "password": {
                                                                "type": "string"
                                                            },
                                                            "port": {
                                                                "type": "integer"
                                                            },
                                                            "protocol": {
                                                                "type": "string"
                                                            },
                                                            "username": {
                                                                "type": "string"
                                                            }
                                                        },
                                                        "required": [
                                                            "description",
                                                            "password",
                                                            "port",
                                                            "username"
                                                        ],
                                                        "type": "object"
                                                    },
                                                    {
                                                        "properties": {
                                                            "globalCredentialIdList": {
                                                                "items": {
                                                                    "type": "string"
                                                                },
                                                                "maxItems": 5,
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    }
                                                ]
                                            },
                                            "httpWrite": {
                                                "anyOf": [
                                                    {
                                                        "properties": {
                                                            "description":
                 {
                                                                "type": "string"
                                                            },
                                                            "password": {
                                                                "type": "string"
                                                            },
                                                            "port": {
                                                                "type": "integer"
                                                            },
                                                            "protocol": {
                                                                "type": "string"
                                                            },
                                                            "username": {
                                                                "type": "string"
                                                            }
                                                        },
                                                        "required": [
                                                            "description",
                                                            "password",
                                                            "port",
                                                            "username"
                                                        ],
                                                        "type": "object"
                                                    },
                                                    {
                                                        "properties": {
                                                            "globalCredentialIdList": {
                                                                "items": {
                                                                    "type": "string"
                                                                },
                                                                "maxItems": 5,
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    }
                                                ]
                                            },
                                            "netconf": {
                                                "anyOf": [
                                                    {
                                                        "properties": {
                                                            "description":
                 {
                                                                "type": "string"
                                                            },
                                                            "port": {
                                                                "type": "integer"
                                                            }
                                                        },
                                                        "required": [
                                                            "port"
                                                        ],
                                                        "type": "object"
                                                    },
                                                    {
                                                        "properties": {
                                                            "globalCredentialIdList": {
                                                                "items": {
                                                                    "type": "string"
                                                                },
                                                                "maxItems": 5,
                                                                "type": "array"
                                                            }
                                                        },
                                                        "type": "object"
                                                    }
                                                ]
                                            },
                                            "snmp": {
                                                "allOf": [
                                                    {
                                                        "anyOf": [
                                                            {
                                                                "properties": {
                                                                    "snmpV2Read": {
                                                                        "anyOf": [
                                                                            {
                                                                                "properties": {
                                                                                    "description":
                 {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "readCommunity": {
                                                                                        "type": "string"
                                                                                    }
                                                                                },
                                                                                "required": [
                                                                                    "description",
                                                                                    "readCommunity"
                                                                                ],
                                                                                "type": "object"
                                                                            },
                                                                            {
                                                                                "properties": {
                                                                                    "globalCredentialIdList": {
                                                                                        "items": {
                                                                                            "type": "string"
                                                                                        },
                                                                                        "maxItems": 5,
                                                                                        "type": "array"
                                                                                    }
                                                                                },
                                                                                "type": "object"
                                                                            }
                                                                        ]
                                                                    }
                                                                },
                                                                "required": [
                                                                    "snmpV2Read"
                                                                ],
                                                                "type": "object"
                                                            },
                                                            {
                                                                "properties": {
                                                                    "snmpV2Write": {
                                                                        "anyOf": [
                                                                            {
                                                                                "properties": {
                                                                                    "description":
                 {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "writeCommunity": {
                                                                                        "type": "string"
                                                                                    }
                                                                                },
                                                                                "required": [
                                                                                    "description",
                                                                                    "writeCommunity"
                                                                                ],
                                                                                "type": "object"
                                                                            },
                                                                            {
                                                                                "properties": {
                                                                                    "globalCredentialIdList": {
                                                                                        "items": {
                                                                                            "type": "string"
                                                                                        },
                                                                                        "maxItems": 5,
                                                                                        "type": "array"
                                                                                    }
                                                                                },
                                                                                "type": "object"
                                                                            }
                                                                        ]
                                                                    }
                                                                },
                                                                "required": [
                                                                    "snmpV2Write"
                                                                ],
                                                                "type": "object"
                                                            },
                                                            {
                                                                "properties": {
                                                                    "snmpV3": {
                                                                        "anyOf": [
                                                                            {
                                                                                "properties": {
                                                                                    "authPassword": {
                                                                                        "minLength": 8,
                                                                                        "type": "string"
                                                                                    },
                                                                                    "authType": {
                                                                                        "enum": [
                                                                                            "SHA",
                                                                                            "MD5",
                                                                                            "SHA256"
                                                                                        ],
                                                                                        "type": "string"
                                                                                    },
                                                                                    "description":
                 {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "mode": {
                                                                                        "enum": [
                                                                                            "AUTHPRIV",
                                                                                            "AUTHNOPRIV",
                                                                                            "NOAUTHNOPRIV"
                                                                                        ],
                                                                                        "type": "string"
                                                                                    },
                                                                                    "privacyPassword": {
                                                                                        "minLength": 8,
                                                                                        "type": "string"
                                                                                    },
                                                                                    "privacyType": {
                                                                                        "enum": [
                                                                                            "AES128",
                                                                                            "AES192",
                                                                                            "AES256",
                                                                                            "CISCOAES192",
                                                                                            "CISCOAES256"
                                                                                        ],
                                                                                        "type": "string"
                                                                                    },
                                                                                    "username": {
                                                                                        "type": "string"
                                                                                    }
                                                                                },
                                                                                "required": [
                                                                                    "description",
                                                                                    "mode",
                                                                                    "username"
                                                                                ],
                                                                                "type": "object"
                                                                            },
                                                                            {
                                                                                "properties": {
                                                                                    "globalCredentialIdList": {
                                                                                        "items": {
                                                                                            "type": "string"
                                                                                        },
                                                                                        "maxItems": 5,
                                                                                        "type": "array"
                                                                                    }
                                                                                },
                                                                                "type": "object"
                                                                            }
                                                                        ]
                                                                    }
                                                                },
                                                                "required": [
                                                                    "snmpV3"
                                                                ],
                                                                "type": "object"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "properties": {
                                                            "retries": {
                                                                "default": 3,
                                                                "maximum": 3,
                                                                "type": "integer"
                                                            },
                                                            "timeout": {
                                                                "default": 5,
                                                                "maximum": 300,
                                                                "type": "integer"
                                                            }
                                                        },
                                                        "type": "object"
                                                    }
                                                ]
                                            }
                                        },
                                        "required": [
                                            "cli",
                                            "snmp"
                                        ],
                                        "type": "object"
                                    },
                                    "discoveryTypeDetails": {
                                        "oneOf": [
                                            {
                                                "allOf": [
                                                    {
                                                        "properties": {
                                                            "type": {
                                                                "enum": [
                                                                    "SINGLE",
                                                                    "RANGE",
                                                                    "LLDP",
                                                                    "CDP",
                                                                    "CIDR"
                                                                ],
                                                                "type": "string"
                                                            }
                                                        },
                                                        "required": [
                                                            "type"
                                                        ],
                                                        "type": "object"
                                                    },
                                                    {
                                                        "properties": {
                                                            "ipAddress": {
                                                                "allOf": [
                                                                    {
                                                                        "oneOf": [
                                                                            {
                                                                                "type": "string"
                                                                            },
                                                                            {
                                                                                "type": "string"
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        },
                                                        "required": [
                                                            "ipAddress"
                                                        ],
                                                        "type": "object"
                                                    }
                                                ]
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "properties": {
                                                            "type": {
                                                                "enum": [
                                                                    "SINGLE",
                                                                    "RANGE",
                                                                    "LLDP",
                                                                    "CDP",
                                                                    "CIDR"
                                                                ],
                                                                "type": "string"
                                                            }
                                                        },
                                                        "required": [
                                                            "type"
                                                        ],
                                                        "type": "object"
                                                    },
                                                    {
                                                        "properties": {
                                                            "range": {
                                                                "items": {
                                                                    "properties": {
                                                                        "ipAddressEnd": {
                                                                            "allOf": [
                                                                                {
                                                                                    "oneOf": [
                                                                                        {
                                                                                            "type": "string"
                                                                                        },
                                                                                        {
                                                                                            "type": "string"
                                                                                        }
                                                                                    ]
                                                                                }
                                                                            ]
                                                                        },
                                                                        "ipAddressStart": {
                                                                            "allOf": [
                                                                                {
                                                                                    "oneOf": [
                                                                                        {
                                                                                            "type": "string"
                                                                                        },
                                                                                        {
                                                                                            "type": "string"
                                                                                        }
                                                                                    ]
                                                                                }
                                                                            ]
                                                                        }
                                                                    },
                                                                    "required": [
                                                                        "ipAddressEnd",
                                                                        "ipAddressStart"
                                                                    ],
                                                                    "type": "object"
                                                                },
                                                                "minItems": 1,
                                                                "type": "array"
                                                            }
                                                        },
                                                        "required": [
                                                            "range"
                                                        ],
                                                        "type": "object"
                                                    }
                                                ]
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "properties": {
                                                            "type": {
                                                                "enum": [
                                                                    "SINGLE",
                                                                    "RANGE",
                                                                    "LLDP",
                                                                    "CDP",
                                                                    "CIDR"
                                                                ],
                                                                "type": "string"
                                                            }
                                                        },
                                                        "required": [
                                                            "type"
                                                        ],
                                                        "type": "object"
                                                    },
                                                    {
                                                        "properties": {
                                                            "cidrAddress": {
                                                                "allOf": [
                                                                    {
                                                                        "properties": {
                                                                            "cidrPrefix": {
                                                                                "allOf": [
                                                                                    {
                                                                                        "oneOf": [
                                                                                            {
                                                                                                "type": "string"
                                                                                            },
                                                                                            {
                                                                                                "type": "string"
                                                                                            }
                                                                                        ]
                                                                                    }
                                                                                ]
                                                                            },
                                                                            "cidrSuffix": {
                                                                                "type": "integer"
                                                                            }
                                                                        },
                                                                        "type": "object"
                                                                    }
                                                                ]
                                                            },
                                                            "subnetFilter": {
                                                                "items": {
                                                                    "anyOf": [
                                                                        {
                                                                            "properties": {
                                                                                "ipAddress": {
                                                                                    "allOf": [
                                                                                        {
                                                                                            "oneOf": [
                                                                                                {
                                                                                                    "type": "string"
                                                                                                },
                                                                                                {
                                                                                                    "type": "string"
                                                                                                }
                                                                                            ]
                                                                                        },
                                                                                        {}
                                                                                    ]
                                                                                }
                                                                            },
                                                                            "type": "object"
                                                                        },
                                                                        {
                                                                            "properties": {
                                                                                "cidrAddress": {
                                                                                    "allOf": [
                                                                                        {
                                                                                            "properties": {
                                                                                                "cidrPrefix": {
                                                                                                    "allOf": [
                                                                                                        {
                                                                                                            "oneOf": [
                                                                                                                {
                                                                                                                    "type": "string"
                                                                                                                },
                                                                                                                {
                                                                                                                    "type": "string"
                                                                                                                }
                                                                                                            ]
                                                                                                        }
                                                                                                    ]
                                                                                                },
                                                                                                "cidrSuffix": {
                                                                                                    "type": "integer"
                                                                                                }
                                                                                            },
                                                                                            "type": "object"
                                                                                        }
                                                                                    ]
                                                                                }
                                                                            },
                                                                            "type": "object"
                                                                        }
                                                                    ]
                                                                },
                                                                "type": "array"
                                                            }
                                                        },
                                                        "required": [
                                                            "cidrAddress"
                                                        ],
                                                        "type": "object"
                                                    }
                                                ]
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "properties": {
                                                            "type": {
                                                                "enum": [
                                                                    "SINGLE",
                                                                    "RANGE",
                                                                    "LLDP",
                                                                    "CDP",
                                                                    "CIDR"
                                                                ],
                                                                "type": "string"
                                                            }
                                                        },
                                                        "required": [
                                                            "type"
                                                        ],
                                                        "type": "object"
                                                    },
                                                    {
                                                        "properties": {
                                                            "hopCount": {
                                                                "default": 16,
                                                                "maximum": 16,
                                                                "minimum": 1,
                                                                "type": "integer"
                                                            },
                                                            "ipAddress": {
                                                                "allOf": [
                                                                    {
                                                                        "oneOf": [
                                                                            {
                                                                                "type": "string"
                                                                            },
                                                                            {
                                                                                "type": "string"
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            },
                                                            "subnetFilter": {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "properties": {
                                                                                    "ipAddress": {
                                                                                        "allOf": [
                                                                                            {
                                                                                                "oneOf": [
                                                                                                    {
                                                                                                        "type": "string"
                                                                                                    },
                                                                                                    {
                                                                                                        "type": "string"
                                                                                                    }
                                                                                                ]
                                                                                            },
                                                                                            {}
                                                                                        ]
                                                                                    }
                                                                                },
                                                                                "type": "object"
                                                                            },
                                                                            {
                                                                                "properties": {
                                                                                    "cidrAddress": {
                                                                                        "allOf": [
                                                                                            {
                                                                                                "properties": {
                                                                                                    "cidrPrefix": {
                                                                                                        "allOf": [
                                                                                                            {
                                                                                                                "oneOf": [
                                                                                                                    {
                                                                                                                        "type": "string"
                                                                                                                    },
                                                                                                                    {
                                                                                                                        "type": "string"
                                                                                                                    }
                                                                                                                ]
                                                                                                            }
                                                                                                        ]
                                                                                                    },
                                                                                                    "cidrSuffix": {
                                                                                                        "type": "integer"
                                                                                                    }
                                                                                                },
                                                                                                "type": "object"
                                                                                            }
                                                                                        ]
                                                                                    }
                                                                                },
                                                                                "type": "object"
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        },
                                                        "required": [
                                                            "hopCount",
                                                            "ipAddress"
                                                        ],
                                                        "type": "object"
                                                    }
                                                ]
                                            },
                                            {
                                                "allOf": [
                                                    {
                                                        "properties": {
                                                            "type": {
                                                                "enum": [
                                                                    "SINGLE",
                                                                    "RANGE",
                                                                    "LLDP",
                                                                    "CDP",
                                                                    "CIDR"
                                                                ],
                                                                "type": "string"
                                                            }
                                                        },
                                                        "required": [
                                                            "type"
                                                        ],
                                                        "type": "object"
                                                    },
                                                    {
                                                        "properties": {
                                                            "hopCount": {
                                                                "default": 16,
                                                                "maximum": 16,
                                                                "minimum": 1,
                                                                "type": "integer"
                                                            },
                                                            "ipAddress": {
                                                                "allOf": [
                                                                    {
                                                                        "oneOf": [
                                                                            {
                                                                                "type": "string"
                                                                            },
                                                                            {
                                                                                "type": "string"
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            },
                                                            "subnetFilter": {
                                                                "allOf": [
                                                                    {
                                                                        "anyOf": [
                                                                            {
                                                                                "properties": {
                                                                                    "ipAddress": {
                                                                                        "allOf": [
                                                                                            {
                                                                                                "oneOf": [
                                                                                                    {
                                                                                                        "type": "string"
                                                                                                    },
                                                                                                    {
                                                                                                        "type": "string"
                                                                                                    }
                                                                                                ]
                                                                                            },
                                                                                            {}
                                                                                        ]
                                                                                    }
                                                                                },
                                                                                "type": "object"
                                                                            },
                                                                            {
                                                                                "properties": {
                                                                                    "cidrAddress": {
                                                                                        "allOf": [
                                                                                            {
                                                                                                "properties": {
                                                                                                    "cidrPrefix": {
                                                                                                        "allOf": [
                                                                                                            {
                                                                                                                "oneOf": [
                                                                                                                    {
                                                                                                                        "type": "string"
                                                                                                                    },
                                                                                                                    {
                                                                                                                        "type": "string"
                                                                                                                    }
                                                                                                                ]
                                                                                                            }
                                                                                                        ]
                                                                                                    },
                                                                                                    "cidrSuffix": {
                                                                                                        "type": "integer"
                                                                                                    }
                                                                                                },
                                                                                                "type": "object"
                                                                                            }
                                                                                        ]
                                                                                    }
                                                                                },
                                                                                "type": "object"
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        },
                                                        "required": [
                                                            "hopCount",
                                                            "ipAddress"
                                                        ],
                                                        "type": "object"
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    "id": {
                                        "type": "string"
                                    },
                                    "managementIpSelectionMethod": {
                                        "enum": [
                                            "DEFAULT",
                                            "LOOPBACK"
                                        ],
                                        "type": "string"
                                    },
                                    "name": {
                                        "type": "string"
                                    },
                                    "onlyNewDevice": {
                                        "default": false,
                                        "type": "boolean"
                                    },
                                    "siteId": {
                                        "type": "string"
                                    },
                                    "updateManagementIp": {
                                        "default": false,
                                        "type": "boolean"
                                    }
                                },
                                "required": [
                                    "credentials",
                                    "discoveryTypeDetails",
                                    "id",
                                    "name"
                                ],
                                "type": "object"
                            },
                            "type": "array"
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
