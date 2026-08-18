"""Cisco Catalyst Center FetchesTheDiscoveryJobDetailsForTheGivenJobId data model.

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


class JSONSchemaValidatorDbf7Bf70E5556A590074784C2E0C7B1:
    """FetchesTheDiscoveryJobDetailsForTheGivenJobId request schema
    definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "allOf": [
                                {
                                    "properties": {
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
                                        "endTime": {
                                            "type": "integer"
                                        },
                                        "id": {
                                            "type": "string"
                                        },
                                        "jobId": {
                                            "type": "string"
                                        },
                                        "name": {
                                            "type": "string"
                                        },
                                        "startTime": {
                                            "type": "integer"
                                        },
                                        "status": {
                                            "enum": [
                                                "RUNNING",
                                                "COMPLETED",
                                                "QUEUED",
                                                "SCHEDULED",
                                                "TERMINATED"
                                            ],
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "discoveryTypeDetails",
                                        "id",
                                        "jobId",
                                        "name",
                                        "startTime",
                                        "status"
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
