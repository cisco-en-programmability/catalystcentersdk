"""Cisco Catalyst Center QueryNetworkDevicesWithFilters data model.

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


class JSONSchemaValidatorFff3662537E538F82BfB5809E30B3Df:
    """QueryNetworkDevicesWithFilters request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "items": {
                                "properties": {
                                    "apEthernetMacAddress": {
                                        "type": "string"
                                    },
                                    "apManagerInterfaceIpAddress": {
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
                                    "apWlcIpAddress": {
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
                                    "bootTime": {
                                        "allOf": [
                                            {
                                                "minimum": 0,
                                                "type": "integer"
                                            }
                                        ]
                                    },
                                    "deviceSupportLevel": {
                                        "enum": [
                                            "SUPPORTED",
                                            "LIMITED",
                                            "THIRD_PARTY",
                                            "UNSUPPORTED"
                                        ],
                                        "type": "string"
                                    },
                                    "dnsResolvedManagementIpAddress": {
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
                                    "errorCode": {
                                        "enum": [
                                            "UNREACHABLE",
                                            "ONLY_PING_REACHABLE",
                                            "CREDENTIAL_MISSING",
                                            "SNMP_TIMEOUT",
                                            "SNMP_AUTH_ERROR",
                                            "SNMP_UNSUPPORTED_AUTH",
                                            "SNMP_UNSUPPORTED_PRIV",
                                            "SNMP_DES_DEPRECATED",
                                            "SNMP_UNSUPPORTED_SECURITY_LEVEL",
                                            "SNMP_SPARSE_ERROR",
                                            "SNMP_FAILED",
                                            "CLI_TIMEOUT",
                                            "CLI_CONNECTION_CLOSED",
                                            "CLI_CONNECTION_ERROR",
                                            "CLI_AUTH_ERROR",
                                            "CLI_MISSING_ENABLE_PASSWORD",
                                            "CLI_INCORRECT_ENABLE_PASSWORD",
                                            "NETCONF_CONNECTION_ERROR",
                                            "NETCONF_AUTH_ERROR",
                                            "NETCONF_PORT_MISSING",
                                            "NETCONF_ACCESS_DENIED",
                                            "NETCONF_RPC_ERROR",
                                            "HTTP_FAILED",
                                            "QUARANTINED",
                                            "SYNC_DELAYED",
                                            "SYNC_CANCELLED",
                                            "SYNC_DISABLED",
                                            "WLAN_CONTROLLER_MISSING",
                                            "SERIAL_NUMBER_CONFLICT",
                                            "UNSUPPORTED_MANAGEMENT_IP",
                                            "INCORRECT_THIRD_PARTY_CATEGORY",
                                            "INCORRECT_NETWORK_DEVICE_CATEGORY",
                                            "SSH_KEY_VERIFICATION_ERROR",
                                            "SSL_HANDSHAKE_FAILURE",
                                            "SSH_KEY_EXCHANGE_FAILED",
                                            "UNKNOWN"
                                        ],
                                        "type": "string"
                                    },
                                    "errorDescription": {
                                        "type": "string"
                                    },
                                    "family": {
                                        "type": "string"
                                    },
                                    "hostname": {
                                        "type": "string"
                                    },
                                    "id": {
                                        "type": "string"
                                    },
                                    "lastSuccessfulResyncReasons": {
                                        "items": {
                                            "enum": [
                                                "ADD_DEVICE_SYNC",
                                                "LINK_UP_DOWN",
                                                "CONFIG_CHANGE",
                                                "DEVICE_UPDATED_SYNC",
                                                "AP_EVENT_BASED_SYNC",
                                                "APP_REQUESTED_SYNC",
                                                "PERIODIC_SYNC",
                                                "UI_SYNC",
                                                "UNKNOWN",
                                                "REFRESH_OBJECTS_FEATURE_BASED_SYNC"
                                            ],
                                            "type": "string"
                                        },
                                        "maxItems": 50,
                                        "type": "array"
                                    },
                                    "macAddress": {
                                        "type": "string"
                                    },
                                    "managementAddress": {
                                        "allOf": [
                                            {
                                                "oneOf": [
                                                    {
                                                        "type": "string"
                                                    },
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
                                        ]
                                    },
                                    "managementState": {
                                        "enum": [
                                            "MANAGED",
                                            "UNDER_MAINTENANCE",
                                            "NEVER_MANAGED"
                                        ],
                                        "type": "string"
                                    },
                                    "pendingResyncRequestCount": {
                                        "type": "integer"
                                    },
                                    "pendingResyncRequestReasons": {
                                        "items": {
                                            "enum": [
                                                "ADD_DEVICE_SYNC",
                                                "LINK_UP_DOWN",
                                                "CONFIG_CHANGE",
                                                "DEVICE_UPDATED_SYNC",
                                                "AP_EVENT_BASED_SYNC",
                                                "APP_REQUESTED_SYNC",
                                                "PERIODIC_SYNC",
                                                "UI_SYNC",
                                                "CUSTOM",
                                                "UNKNOWN",
                                                "REFRESH_OBJECTS_FEATURE_BASED_SYNC"
                                            ],
                                            "type": "string"
                                        },
                                        "maxItems": 50,
                                        "type": "array"
                                    },
                                    "platformIds": {
                                        "type": "string"
                                    },
                                    "reachabilityFailureReason": {
                                        "type": "string"
                                    },
                                    "reachabilityStatus": {
                                        "enum": [
                                            "REACHABLE",
                                            "ONLY_PING_REACHABLE",
                                            "UNREACHABLE",
                                            "UNKNOWN"
                                        ],
                                        "type": "string"
                                    },
                                    "resyncEndTime": {
                                        "allOf": [
                                            {
                                                "minimum": 0,
                                                "type": "integer"
                                            }
                                        ]
                                    },
                                    "resyncIntervalMinutes": {
                                        "type": "integer"
                                    },
                                    "resyncIntervalSource": {
                                        "enum": [
                                            "GLOBAL",
                                            "CUSTOM",
                                            "NA"
                                        ],
                                        "type": "string"
                                    },
                                    "resyncReasons": {
                                        "items": {
                                            "enum": [
                                                "ADD_DEVICE_SYNC",
                                                "LINK_UP_DOWN",
                                                "CONFIG_CHANGE",
                                                "DEVICE_UPDATED_SYNC",
                                                "AP_EVENT_BASED_SYNC",
                                                "APP_REQUESTED_SYNC",
                                                "PERIODIC_SYNC",
                                                "UI_SYNC",
                                                "CUSTOM",
                                                "UNKNOWN",
                                                "REFRESH_OBJECTS_FEATURE_BASED_SYNC"
                                            ],
                                            "type": "string"
                                        },
                                        "maxItems": 50,
                                        "type": "array"
                                    },
                                    "resyncRequestedByApps": {
                                        "items": {
                                            "type": "string"
                                        },
                                        "maxItems": 50,
                                        "type": "array"
                                    },
                                    "resyncStartTime": {
                                        "allOf": [
                                            {
                                                "minimum": 0,
                                                "type": "integer"
                                            }
                                        ]
                                    },
                                    "role": {
                                        "enum": [
                                            "BORDER_ROUTER",
                                            "CORE",
                                            "DISTRIBUTION",
                                            "ACCESS",
                                            "UNKNOWN"
                                        ],
                                        "type": "string"
                                    },
                                    "roleSource": {
                                        "enum": [
                                            "AUTO",
                                            "MANUAL"
                                        ],
                                        "type": "string"
                                    },
                                    "secureMode": {
                                        "enum": [
                                            "ENABLED",
                                            "DISABLED",
                                            "NOT_APPLICABLE",
                                            "UNKNOWN"
                                        ],
                                        "type": "string"
                                    },
                                    "serialNumbers": {
                                        "items": {
                                            "type": "string"
                                        },
                                        "maxItems": 50,
                                        "type": "array"
                                    },
                                    "series": {
                                        "type": "string"
                                    },
                                    "snmpContact": {
                                        "type": "string"
                                    },
                                    "snmpLocation": {
                                        "type": "string"
                                    },
                                    "softwareType": {
                                        "type": "string"
                                    },
                                    "softwareVersion": {
                                        "type": "string"
                                    },
                                    "stackDevice": {
                                        "type": "boolean"
                                    },
                                    "status": {
                                        "enum": [
                                            "MANAGED",
                                            "SYNC_NOT_STARTED",
                                            "SYNC_INIT_FAILED",
                                            "SYNC_PRECHECK_FAILED",
                                            "SYNC_IN_PROGRESS",
                                            "SYNC_INTERNAL_ERROR",
                                            "SYNC_DISABLED",
                                            "DELETING_DEVICE",
                                            "UNDER_MAINTENANCE",
                                            "QUARANTINED",
                                            "UNASSOCIATED",
                                            "UNREACHABLE",
                                            "UNKNOWN"
                                        ],
                                        "type": "string"
                                    },
                                    "type": {
                                        "type": "string"
                                    },
                                    "userDefinedFields": {
                                        "additionalProperties": {
                                            "type": "string"
                                        },
                                        "type": "object"
                                    },
                                    "vendor": {
                                        "type": "string"
                                    }
                                },
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
