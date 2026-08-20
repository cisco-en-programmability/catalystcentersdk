"""Cisco Catalyst Center GetPnPDeviceDetailsByID data model.

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


class JSONSchemaValidatorEDfdb5E49851A6758Ff9Ada83:
    """GetPnPDeviceDetailsByID request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "allOf": [
                                {
                                    "properties": {
                                        "apProvisionType": {
                                            "enum": [
                                                "DAY0",
                                                "LSC"
                                            ],
                                            "type": "string"
                                        },
                                        "authenticatedMicNumber": {
                                            "allOf": [
                                                {
                                                    "type": "string"
                                                }
                                            ],
                                            "type": "string"
                                        },
                                        "authenticatedSudiSerialNumber": {
                                            "type": "string"
                                        },
                                        "authorizationStatus": {
                                            "enum": [
                                                "NO_OP",
                                                "AUTHORIZATION_REQUESTED",
                                                "AUTHORIZATION_ACCEPTED",
                                                "AUTHORIZATION_NOT_REQUIRED"
                                            ],
                                            "type": "string"
                                        },
                                        "bootMode": {
                                            "enum": [
                                                "BUNDLE",
                                                "INSTALL"
                                            ],
                                            "type": "string"
                                        },
                                        "contactedStatus": {
                                            "enum": [
                                                "CONTACTED",
                                                "NOT_CONTACTED"
                                            ],
                                            "type": "string"
                                        },
                                        "deviceType": {
                                            "enum": [
                                                "ROUTER",
                                                "SWITCH",
                                                "AP",
                                                "ME",
                                                "WLC",
                                                "EWC",
                                                "SENSOR",
                                                "UNSUPPORTED"
                                            ],
                                            "type": "string"
                                        },
                                        "firstContactTime": {
                                            "allOf": [
                                                {
                                                    "minimum": 0,
                                                    "type": "integer"
                                                }
                                            ]
                                        },
                                        "hostname": {
                                            "type": "string"
                                        },
                                        "id": {
                                            "type": "string"
                                        },
                                        "imageFile": {
                                            "type": "string"
                                        },
                                        "imageVersion": {
                                            "type": "string"
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
                                        "ipInterfaces": {
                                            "items": {
                                                "properties": {
                                                    "ipv4Address": {
                                                        "allOf": [
                                                            {
                                                                "type": "string"
                                                            }
                                                        ]
                                                    },
                                                    "ipv6AddressList": {
                                                        "items": {
                                                            "allOf": [
                                                                {
                                                                    "type": "string"
                                                                }
                                                            ]
                                                        },
                                                        "type": "array"
                                                    },
                                                    "macAddress": {
                                                        "allOf": [
                                                            {
                                                                "type": "string"
                                                            }
                                                        ]
                                                    },
                                                    "name": {
                                                        "type": "string"
                                                    },
                                                    "status": {
                                                        "enum": [
                                                            "UP",
                                                            "DOWN"
                                                        ],
                                                        "type": "string"
                                                    }
                                                },
                                                "type": "object"
                                            },
                                            "type": "array"
                                        },
                                        "lastContactTime": {
                                            "allOf": [
                                                {
                                                    "minimum": 0,
                                                    "type": "integer"
                                                }
                                            ]
                                        },
                                        "licenseLevel": {
                                            "enum": [
                                                "DNA_ADVANTAGE",
                                                "DNA_ESSENTIALS",
                                                "ADVANTAGE",
                                                "ESSENTIALS",
                                                "LANBASE",
                                                "IPSERVICES"
                                            ],
                                            "type": "string"
                                        },
                                        "macAddress": {
                                            "allOf": [
                                                {
                                                    "type": "string"
                                                }
                                            ],
                                            "type": "string"
                                        },
                                        "neighborLinks": {
                                            "items": {
                                                "properties": {
                                                    "localInterfaceName": {
                                                        "type": "string"
                                                    },
                                                    "localMacAddress": {
                                                        "allOf": [
                                                            {
                                                                "type": "string"
                                                            }
                                                        ]
                                                    },
                                                    "localShortInterfaceName": {
                                                        "type": "string"
                                                    },
                                                    "remoteDeviceName": {
                                                        "type": "string"
                                                    },
                                                    "remoteInterfaceName": {
                                                        "type": "string"
                                                    },
                                                    "remoteMacAddress": {
                                                        "allOf": [
                                                            {
                                                                "type": "string"
                                                            }
                                                        ]
                                                    },
                                                    "remotePlatform": {
                                                        "type": "string"
                                                    },
                                                    "remoteShortInterfaceName": {
                                                        "type": "string"
                                                    },
                                                    "remoteVersion": {
                                                        "type": "string"
                                                    }
                                                },
                                                "type": "object"
                                            },
                                            "type": "array"
                                        },
                                        "networkDeviceId": {
                                            "type": "string"
                                        },
                                        "onboardingState": {
                                            "enum": [
                                                "NOT_CONTACTED",
                                                "CONNECTING",
                                                "ERROR_SECURING_CONNECTION",
                                                "ERROR_AUTHENTICATING",
                                                "INITIALIZING",
                                                "INITIALIZED",
                                                "ERROR_INITIALIZING",
                                                "ERROR_INITIALIZED_TIMEOUT",
                                                "SUDI_AUTHORIZING",
                                                "ERROR_SUDI_AUTHORIZING",
                                                "SUDI_AUTHORIZED",
                                                "EXECUTING_WORKFLOW",
                                                "EXECUTED_WORKFLOW",
                                                "ERROR_EXECUTING_WORKFLOW",
                                                "EXECUTING_RESET",
                                                "ERROR_EXECUTING_RESET",
                                                "PROVISIONED"
                                            ],
                                            "type": "string"
                                        },
                                        "physicalInterfaces": {
                                            "items": {
                                                "properties": {
                                                    "duplex": {
                                                        "type": "string"
                                                    },
                                                    "port": {
                                                        "type": "string"
                                                    },
                                                    "speed": {
                                                        "type": "string"
                                                    },
                                                    "status": {
                                                        "enum": [
                                                            "CONNECTED",
                                                            "NOT_CONNECTED"
                                                        ],
                                                        "type": "string"
                                                    },
                                                    "type": {
                                                        "type": "string"
                                                    },
                                                    "vlan": {
                                                        "type": "string"
                                                    }
                                                },
                                                "type": "object"
                                            },
                                            "type": "array"
                                        },
                                        "pid": {
                                            "type": "string"
                                        },
                                        "pnpProfileList": {
                                            "items": {
                                                "properties": {
                                                    "createdBy": {
                                                        "type": "string"
                                                    },
                                                    "discoveryCreated": {
                                                        "type": "boolean"
                                                    },
                                                    "primaryEndpoint": {
                                                        "properties": {
                                                            "certificateURL": {
                                                                "type": "string"
                                                            },
                                                            "fqdn": {
                                                                "allOf": [
                                                                    {
                                                                        "type": "string"
                                                                    }
                                                                ]
                                                            },
                                                            "ipv4Address": {
                                                                "allOf": [
                                                                    {
                                                                        "type": "string"
                                                                    }
                                                                ]
                                                            },
                                                            "ipv6Address": {
                                                                "allOf": [
                                                                    {
                                                                        "type": "string"
                                                                    }
                                                                ]
                                                            },
                                                            "port": {
                                                                "type": "integer"
                                                            },
                                                            "protocol": {
                                                                "type": "string"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "profileName": {
                                                        "type": "string"
                                                    },
                                                    "secondaryEndpoint": {
                                                        "properties": {
                                                            "certificateURL": {
                                                                "type": "string"
                                                            },
                                                            "fqdn": {
                                                                "allOf": [
                                                                    {
                                                                        "type": "string"
                                                                    }
                                                                ]
                                                            },
                                                            "ipv4Address": {
                                                                "allOf": [
                                                                    {
                                                                        "type": "string"
                                                                    }
                                                                ]
                                                            },
                                                            "ipv6Address": {
                                                                "allOf": [
                                                                    {
                                                                        "type": "string"
                                                                    }
                                                                ]
                                                            },
                                                            "port": {
                                                                "type": "integer"
                                                            },
                                                            "protocol": {
                                                                "type": "string"
                                                            }
                                                        },
                                                        "type": "object"
                                                    }
                                                },
                                                "type": "object"
                                            },
                                            "type": "array"
                                        },
                                        "provisionedSuccessTime": {
                                            "allOf": [
                                                {
                                                    "minimum": 0,
                                                    "type": "integer"
                                                }
                                            ]
                                        },
                                        "serialNumber": {
                                            "type": "string"
                                        },
                                        "siteId": {
                                            "type": "string"
                                        },
                                        "siteNameHierarchy": {
                                            "type": "string"
                                        },
                                        "smartAccount": {
                                            "type": "string"
                                        },
                                        "source": {
                                            "enum": [
                                                "NETWORK",
                                                "USER",
                                                "SMART_ACCOUNT"
                                            ],
                                            "type": "string"
                                        },
                                        "stackDevice": {
                                            "type": "boolean"
                                        },
                                        "stackInfo": {
                                            "properties": {
                                                "fullRing": {
                                                    "type": "boolean"
                                                },
                                                "stackMemberList": {
                                                    "items": {
                                                        "properties": {
                                                            "licenseLevel": {
                                                                "enum": [
                                                                    "DNA_ADVANTAGE",
                                                                    "DNA_ESSENTIALS",
                                                                    "ADVANTAGE",
                                                                    "ESSENTIALS"
                                                                ],
                                                                "type": "string"
                                                            },
                                                            "macAddress": {
                                                                "allOf": [
                                                                    {
                                                                        "type": "string"
                                                                    }
                                                                ]
                                                            },
                                                            "pid": {
                                                                "type": "string"
                                                            },
                                                            "role": {
                                                                "enum": [
                                                                    "ACTIVE",
                                                                    "STANDBY",
                                                                    "MEMBER"
                                                                ],
                                                                "type": "string"
                                                            },
                                                            "serialNumber": {
                                                                "type": "string"
                                                            },
                                                            "state": {
                                                                "type": "string"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "type": "array"
                                                },
                                                "supportsStackWorkflows": {
                                                    "type": "boolean"
                                                }
                                            },
                                            "type": "object"
                                        },
                                        "state": {
                                            "enum": [
                                                "UNCLAIMED",
                                                "PENDING_AUTHORIZATION",
                                                "PLANNED",
                                                "ONBOARDING",
                                                "PROVISIONED",
                                                "ERROR",
                                                "RESETTING",
                                                "DELETED"
                                            ],
                                            "type": "string"
                                        },
                                        "sudiMicAuthenticationStatus": {
                                            "enum": [
                                                "NONE",
                                                "UNSUPPORTED",
                                                "ERROR",
                                                "PENDING",
                                                "AUTHENTICATED"
                                            ],
                                            "type": "string"
                                        },
                                        "sudiSerialNumbers": {
                                            "items": {
                                                "type": "string"
                                            },
                                            "type": "array"
                                        },
                                        "svlClaimable": {
                                            "type": "boolean"
                                        },
                                        "svlDevice": {
                                            "type": "boolean"
                                        },
                                        "svlInfo": {
                                            "allOf": [
                                                {
                                                    "properties": {
                                                        "activeSerialNumber": {
                                                            "type": "string"
                                                        },
                                                        "dadLink": {
                                                            "allOf": [
                                                                {
                                                                    "properties": {
                                                                        "localInterface": {
                                                                            "type": "string"
                                                                        },
                                                                        "remoteInterface": {
                                                                            "type": "string"
                                                                        }
                                                                    },
                                                                    "type": "object"
                                                                }
                                                            ]
                                                        },
                                                        "domain": {
                                                            "maximum": 255,
                                                            "minimum": 1,
                                                            "type": "integer"
                                                        },
                                                        "standbySerialNumber": {
                                                            "type": "string"
                                                        },
                                                        "state": {
                                                            "enum": [
                                                                "NONE",
                                                                "INITIATED",
                                                                "WAITING",
                                                                "READY",
                                                                "PRE_CHECK",
                                                                "PUSHING_CONFIG",
                                                                "POST_CHECK",
                                                                "SUCCESS",
                                                                "ERROR"
                                                            ],
                                                            "type": "string"
                                                        },
                                                        "svlLinks": {
                                                            "items": {
                                                                "properties": {
                                                                    "localInterface": {
                                                                        "type": "string"
                                                                    },
                                                                    "remoteInterface": {
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
                                            ]
                                        },
                                        "svlNeighbors": {
                                            "items": {
                                                "properties": {
                                                    "localToRemoteLinks": {
                                                        "items": {
                                                            "properties": {
                                                                "localInterface": {
                                                                    "type": "string"
                                                                },
                                                                "remoteInterface": {
                                                                    "type": "string"
                                                                }
                                                            },
                                                            "type": "object"
                                                        },
                                                        "type": "array"
                                                    },
                                                    "remoteSerialNumber": {
                                                        "type": "string"
                                                    }
                                                },
                                                "type": "object"
                                            },
                                            "type": "array"
                                        },
                                        "virtualAccount": {
                                            "type": "string"
                                        },
                                        "workflowId": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "contactedStatus",
                                        "id",
                                        "onboardingState",
                                        "pid",
                                        "serialNumber",
                                        "source",
                                        "state"
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
