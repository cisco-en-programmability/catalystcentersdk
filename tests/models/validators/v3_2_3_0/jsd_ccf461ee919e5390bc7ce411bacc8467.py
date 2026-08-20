"""Cisco Catalyst Center GetDetailsOfASingleGlobalCredential data model.

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


class JSONSchemaValidatorCcf461Ee919E5390Bc7CE411Bacc8467:
    """GetDetailsOfASingleGlobalCredential request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "oneOf": [
                                {
                                    "oneOf": [
                                        {
                                            "allOf": [
                                                {
                                                    "properties": {
                                                        "id": {
                                                            "type": "string"
                                                        },
                                                        "type": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "id",
                                                        "type"
                                                    ],
                                                    "type": "object"
                                                },
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
                                                }
                                            ]
                                        },
                                        {
                                            "allOf": [
                                                {
                                                    "properties": {
                                                        "id": {
                                                            "type": "string"
                                                        },
                                                        "type": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "id",
                                                        "type"
                                                    ],
                                                    "type": "object"
                                                },
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
                                                }
                                            ]
                                        },
                                        {
                                            "allOf": [
                                                {
                                                    "properties": {
                                                        "id": {
                                                            "type": "string"
                                                        },
                                                        "type": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "id",
                                                        "type"
                                                    ],
                                                    "type": "object"
                                                },
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
                                                }
                                            ]
                                        },
                                        {
                                            "allOf": [
                                                {
                                                    "properties": {
                                                        "id": {
                                                            "type": "string"
                                                        },
                                                        "type": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "id",
                                                        "type"
                                                    ],
                                                    "type": "object"
                                                },
                                                {
                                                    "properties": {
                                                        "authPassword": {
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
                                                }
                                            ]
                                        },
                                        {
                                            "allOf": [
                                                {
                                                    "properties": {
                                                        "id": {
                                                            "type": "string"
                                                        },
                                                        "type": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "id",
                                                        "type"
                                                    ],
                                                    "type": "object"
                                                },
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
                                                            "default": "HTTPS",
                                                            "enum": [
                                                                "HTTPS",
                                                                "HTTP"
                                                            ],
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
                                                }
                                            ]
                                        },
                                        {
                                            "allOf": [
                                                {
                                                    "properties": {
                                                        "id": {
                                                            "type": "string"
                                                        },
                                                        "type": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "id",
                                                        "type"
                                                    ],
                                                    "type": "object"
                                                },
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
                                                            "default": "HTTPS",
                                                            "enum": [
                                                                "HTTPS",
                                                                "HTTP"
                                                            ],
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
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "properties": {
                                        "description":
                 {
                                            "type": "string"
                                        },
                                        "id": {
                                            "type": "string"
                                        },
                                        "port": {
                                            "default": "830",
                                            "type": "string"
                                        },
                                        "type": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "id",
                                        "port",
                                        "type"
                                    ],
                                    "type": "object"
                                }
                            ]
                        },
                        "version": {
                            "type": "string"
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
