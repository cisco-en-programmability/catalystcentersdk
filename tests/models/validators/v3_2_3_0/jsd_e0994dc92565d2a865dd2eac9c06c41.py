"""Cisco Catalyst Center DeviceEnrichmentDetails data model.

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


class JSONSchemaValidatorE0994Dc92565D2A865DD2Eac9C06C41:
    """DeviceEnrichmentDetails request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "items": {
                        "properties": {
                            "response": {
                                "items": {
                                    "properties": {
                                        "deviceDetails": {
                                            "properties": {
                                                "apManagerInterfaceIp": {
                                                    "type": "string"
                                                },
                                                "associatedWlcIp": {
                                                    "type": "string"
                                                },
                                                "bootDateTime": {
                                                    "type": "string"
                                                },
                                                "collectionInterval": {
                                                    "type": "string"
                                                },
                                                "collectionStatus": {
                                                    "enum": [
                                                        "Could Not Synchronize",
                                                        "Deleting Device",
                                                        "In Progress",
                                                        "Incomplete",
                                                        "Maintenance",
                                                        "Managed",
                                                        "Not Manageable",
                                                        "Partial Collection Failure",
                                                        "Quarantined",
                                                        "Sync Disabled",
                                                        "Unassociated",
                                                        "Unknown",
                                                        "Unreachable",
                                                        "Yet to Sync"
                                                    ],
                                                    "type": "string"
                                                },
                                                "createdTime": {
                                                    "type": "string"
                                                },
                                                "errorCode": {
                                                    "type": "string"
                                                },
                                                "errorDescription": {
                                                    "type": "string"
                                                },
                                                "family": {
                                                    "enum": [
                                                        "Switches and Hubs",
                                                        "Routers",
                                                        "Wireless Controller",
                                                        "Unified AP"
                                                    ],
                                                    "type": "string"
                                                },
                                                "hostname": {
                                                    "type": "string"
                                                },
                                                "id": {
                                                    "type": "string"
                                                },
                                                "interfaceCount": {
                                                    "type": "string"
                                                },
                                                "inventoryStatusDetail": {
                                                    "type": "string"
                                                },
                                                "lastUpdatedTime": {
                                                    "type": "integer"
                                                },
                                                "lineCardCount": {
                                                    "type": "string"
                                                },
                                                "lineCardId": {
                                                    "type": "string"
                                                },
                                                "location": {
                                                    "type": "object"
                                                },
                                                "locationName": {
                                                    "type": "object"
                                                },
                                                "macAddress": {
                                                    "type": "string"
                                                },
                                                "managementIpAddress": {
                                                    "type": "string"
                                                },
                                                "memorySize": {
                                                    "type": "string"
                                                },
                                                "neighborTopology": {
                                                    "properties": {
                                                        "links": {
                                                            "items": {
                                                                "properties": {
                                                                    "apRadioAdminStatus": {
                                                                        "type": "string"
                                                                    },
                                                                    "apRadioOperStatus": {
                                                                        "type": "string"
                                                                    },
                                                                    "id": {
                                                                        "type": "object"
                                                                    },
                                                                    "label": {
                                                                        "items": {
                                                                            "type": "object"
                                                                        },
                                                                        "type": "array"
                                                                    },
                                                                    "linkStatus": {
                                                                        "type": "string"
                                                                    },
                                                                    "portUtilization": {
                                                                        "type": "object"
                                                                    },
                                                                    "source": {
                                                                        "type": "string"
                                                                    },
                                                                    "sourceAdminStatus": {
                                                                        "type": "string"
                                                                    },
                                                                    "sourceDuplexInfo": {
                                                                        "type": "string"
                                                                    },
                                                                    "sourceInterfaceName": {
                                                                        "type": "string"
                                                                    },
                                                                    "sourcePortMode": {
                                                                        "type": "string"
                                                                    },
                                                                    "sourcePortVLANInfo": {
                                                                        "type": "string"
                                                                    },
                                                                    "sourcelinkStatus": {
                                                                        "type": "string"
                                                                    },
                                                                    "target": {
                                                                        "type": "string"
                                                                    },
                                                                    "targetAdminStatus": {
                                                                        "type": "string"
                                                                    },
                                                                    "targetDuplexInfo": {
                                                                        "type": "string"
                                                                    },
                                                                    "targetInterfaceName": {
                                                                        "type": "string"
                                                                    },
                                                                    "targetPortMode": {
                                                                        "type": "string"
                                                                    },
                                                                    "targetPortVLANInfo": {
                                                                        "type": "string"
                                                                    },
                                                                    "targetlinkStatus": {
                                                                        "type": "string"
                                                                    }
                                                                },
                                                                "type": "object"
                                                            },
                                                            "type": "array"
                                                        },
                                                        "nodes": {
                                                            "items": {
                                                                "properties": {
                                                                    "additionalInfo": {
                                                                        "type": "object"
                                                                    },
                                                                    "clients": {
                                                                        "type": "object"
                                                                    },
                                                                    "connectedDevice": {
                                                                        "type": "object"
                                                                    },
                                                                    "count": {
                                                                        "type": "object"
                                                                    },
                                                                    "description":
                 {
                                                                        "type": "string"
                                                                    },
                                                                    "deviceType": {
                                                                        "type": "string"
                                                                    },
                                                                    "fabricGroup": {
                                                                        "type": "object"
                                                                    },
                                                                    "fabricRole": {
                                                                        "items": {
                                                                            "type": "string"
                                                                        },
                                                                        "type": "array"
                                                                    },
                                                                    "family": {
                                                                        "type": "string"
                                                                    },
                                                                    "healthScore": {
                                                                        "type": "integer"
                                                                    },
                                                                    "id": {
                                                                        "type": "string"
                                                                    },
                                                                    "ip": {
                                                                        "type": "string"
                                                                    },
                                                                    "level": {
                                                                        "type": "number"
                                                                    },
                                                                    "name": {
                                                                        "type": "string"
                                                                    },
                                                                    "nodeType": {
                                                                        "type": "string"
                                                                    },
                                                                    "platformId": {
                                                                        "type": "string"
                                                                    },
                                                                    "radioFrequency": {
                                                                        "type": "object"
                                                                    },
                                                                    "role": {
                                                                        "type": "string"
                                                                    },
                                                                    "softwareVersion": {
                                                                        "type": "string"
                                                                    },
                                                                    "stackType": {
                                                                        "type": "string"
                                                                    },
                                                                    "userId": {
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
                                                "platformId": {
                                                    "type": "string"
                                                },
                                                "reachabilityFailureReason": {
                                                    "type": "string"
                                                },
                                                "reachabilityStatus": {
                                                    "enum": [
                                                        "Reachable",
                                                        "Unreachable"
                                                    ],
                                                    "type": "string"
                                                },
                                                "role": {
                                                    "enum": [
                                                        "DISTRIBUTION",
                                                        "ACCESS",
                                                        "CORE",
                                                        "BORDER ROUTER"
                                                    ],
                                                    "type": "string"
                                                },
                                                "roleSource": {
                                                    "type": "string"
                                                },
                                                "serialNumber": {
                                                    "type": "string"
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
                                                "softwareVersion": {
                                                    "type": "string"
                                                },
                                                "tagCount": {
                                                    "type": "string"
                                                },
                                                "tunnelUdpPort": {
                                                    "type": "object"
                                                },
                                                "type": {
                                                    "type": "string"
                                                },
                                                "upTime": {
                                                    "type": "string"
                                                },
                                                "waasDeviceMode": {
                                                    "type": "object"
                                                }
                                            },
                                            "type": "object"
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
                        "type": "object"
                    },
                    "type": "array"
                }""".replace("\n" + " " * 16, "")))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                "{} is invalid. Reason: {}".format(request, e.message)
            )
