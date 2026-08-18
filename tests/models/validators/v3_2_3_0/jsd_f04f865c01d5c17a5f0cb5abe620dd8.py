"""Cisco Catalyst Center DeviceLicenseDetails data model.

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


class JSONSchemaValidatorF04F865C01D5C17A5F0Cb5Abe620Dd8:
    """DeviceLicenseDetails request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "access_points": {
                            "items": {
                                "properties": {
                                    "ap_type": {
                                        "type": "string"
                                    },
                                    "count": {
                                        "type": "string"
                                    }
                                },
                                "required": [
                                    "ap_type",
                                    "count"
                                ],
                                "type": "object"
                            },
                            "type": "array"
                        },
                        "chassis_details": {
                            "properties": {
                                "board_serial_number": {
                                    "type": "string"
                                },
                                "modules": {
                                    "items": {
                                        "properties": {
                                            "id": {
                                                "type": "integer"
                                            },
                                            "module_name": {
                                                "type": "string"
                                            },
                                            "module_type": {
                                                "type": "string"
                                            },
                                            "serial_number": {
                                                "type": "string"
                                            }
                                        },
                                        "required": [
                                            "module_type",
                                            "module_name",
                                            "serial_number",
                                            "id"
                                        ],
                                        "type": "object"
                                    },
                                    "type": "array"
                                },
                                "port": {
                                    "type": "integer"
                                },
                                "supervisor_cards": {
                                    "items": {
                                        "properties": {
                                            "serial_number": {
                                                "type": "string"
                                            },
                                            "status": {
                                                "type": "string"
                                            },
                                            "supervisor_card_type": {
                                                "type": "string"
                                            }
                                        },
                                        "required": [
                                            "serial_number",
                                            "supervisor_card_type",
                                            "status"
                                        ],
                                        "type": "object"
                                    },
                                    "type": "array"
                                }
                            },
                            "required": [
                                "board_serial_number",
                                "modules",
                                "supervisor_cards",
                                "port"
                            ],
                            "type": "object"
                        },
                        "device_name": {
                            "type": "string"
                        },
                        "device_type": {
                            "type": "string"
                        },
                        "device_uuid": {
                            "type": "string"
                        },
                        "dna_level": {
                            "type": "string"
                        },
                        "evaluation_license_expiry": {
                            "type": "string"
                        },
                        "feature_license": {
                            "items": {
                                "type": "string"
                            },
                            "type": "array"
                        },
                        "has_sup_cards": {
                            "type": "boolean"
                        },
                        "ip_address": {
                            "type": "string"
                        },
                        "is_license_expired": {
                            "type": "boolean"
                        },
                        "is_stacked_device": {
                            "type": "boolean"
                        },
                        "license_mode": {
                            "type": "string"
                        },
                        "mac_address": {
                            "type": "string"
                        },
                        "model": {
                            "type": "string"
                        },
                        "network_license": {
                            "type": "string"
                        },
                        "site": {
                            "type": "string"
                        },
                        "sntc_status": {
                            "type": "string"
                        },
                        "software_version": {
                            "type": "string"
                        },
                        "stacked_devices": {
                            "items": {
                                "properties": {
                                    "id": {
                                        "type": "integer"
                                    },
                                    "mac_address": {
                                        "type": "string"
                                    },
                                    "role": {
                                        "type": "string"
                                    },
                                    "serial_number": {
                                        "type": "string"
                                    }
                                },
                                "required": [
                                    "mac_address",
                                    "id",
                                    "role",
                                    "serial_number"
                                ],
                                "type": "object"
                            },
                            "type": "array"
                        },
                        "udi": {
                            "type": "string"
                        },
                        "virtual_account_name": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "device_uuid",
                        "site",
                        "model",
                        "license_mode",
                        "is_license_expired",
                        "software_version",
                        "network_license",
                        "evaluation_license_expiry",
                        "device_name",
                        "device_type",
                        "dna_level",
                        "virtual_account_name",
                        "ip_address",
                        "mac_address",
                        "sntc_status",
                        "feature_license",
                        "udi",
                        "stacked_devices",
                        "is_stacked_device",
                        "access_points",
                        "chassis_details"
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
