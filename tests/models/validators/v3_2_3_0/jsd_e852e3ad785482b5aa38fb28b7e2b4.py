"""Cisco Catalyst Center UserEnrichmentDetails data model.

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


class JSONSchemaValidatorE852E3Ad785482B5Aa38Fb28B7E2B4:
    """UserEnrichmentDetails request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "items": {
                        "properties": {
                            "response": {
                                "items": {
                                    "properties": {
                                        "connectedDevice": {
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
                                                            "createdDateTime": {
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
                                        "userDetails": {
                                            "properties": {
                                                "aaaServerEAPLatency": {
                                                    "type": "string"
                                                },
                                                "aaaServerFailedTransaction": {
                                                    "type": "string"
                                                },
                                                "aaaServerIp": {
                                                    "type": "string"
                                                },
                                                "aaaServerLatency": {
                                                    "type": "string"
                                                },
                                                "aaaServerMABLatency": {
                                                    "type": "string"
                                                },
                                                "aaaServerSuccessTransaction": {
                                                    "type": "string"
                                                },
                                                "aaaServerTransaction": {
                                                    "type": "string"
                                                },
                                                "apGroup": {
                                                    "type": "string"
                                                },
                                                "authType": {
                                                    "type": "string"
                                                },
                                                "avgRssi": {
                                                    "type": "string"
                                                },
                                                "avgSnr": {
                                                    "type": "string"
                                                },
                                                "bridgeVMMode": {
                                                    "type": "string"
                                                },
                                                "channel": {
                                                    "type": "string"
                                                },
                                                "clientConnection": {
                                                    "type": "string"
                                                },
                                                "clientType": {
                                                    "type": "string"
                                                },
                                                "connectedDevice": {
                                                    "items": {
                                                        "properties": {
                                                            "band": {
                                                                "type": "string"
                                                            },
                                                            "id": {
                                                                "type": "string"
                                                            },
                                                            "ipAddress": {
                                                                "type": "string"
                                                            },
                                                            "mac": {
                                                                "type": "string"
                                                            },
                                                            "mgmtIp": {
                                                                "type": "string"
                                                            },
                                                            "mode": {
                                                                "type": "string"
                                                            },
                                                            "name": {
                                                                "type": "string"
                                                            },
                                                            "type": {
                                                                "type": "string"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "type": "array"
                                                },
                                                "connectedUpn": {
                                                    "type": "string"
                                                },
                                                "connectedUpnId": {
                                                    "type": "string"
                                                },
                                                "connectedUpnOwner": {
                                                    "type": "string"
                                                },
                                                "connectionStatus": {
                                                    "enum": [
                                                        "CONNECTED",
                                                        "DISCONNECTED",
                                                        "CONNECTING",
                                                        "UNKNOWN"
                                                    ],
                                                    "type": "string"
                                                },
                                                "countryCode": {
                                                    "type": "string"
                                                },
                                                "dataRate": {
                                                    "type": "string"
                                                },
                                                "deviceForm": {
                                                    "type": "string"
                                                },
                                                "deviceVendor": {
                                                    "type": "string"
                                                },
                                                "dhcpDeclineIp": {
                                                    "type": "string"
                                                },
                                                "dhcpNakIp": {
                                                    "type": "string"
                                                },
                                                "dhcpServerDOLatency": {
                                                    "type": "string"
                                                },
                                                "dhcpServerFailedTransaction": {
                                                    "type": "string"
                                                },
                                                "dhcpServerIp": {
                                                    "type": "string"
                                                },
                                                "dhcpServerLatency": {
                                                    "type": "string"
                                                },
                                                "dhcpServerRALatency": {
                                                    "type": "string"
                                                },
                                                "dhcpServerSuccessTransaction": {
                                                    "type": "string"
                                                },
                                                "dhcpServerTransaction": {
                                                    "type": "string"
                                                },
                                                "dnsRequest": {
                                                    "type": "string"
                                                },
                                                "dnsResponse": {
                                                    "type": "string"
                                                },
                                                "dot11Protocol": {
                                                    "type": "string"
                                                },
                                                "dot11ProtocolCapability": {
                                                    "type": "string"
                                                },
                                                "duId": {
                                                    "type": "string"
                                                },
                                                "firmwareVersion": {
                                                    "type": "string"
                                                },
                                                "frequency": {
                                                    "type": "string"
                                                },
                                                "healthScore": {
                                                    "items": {
                                                        "properties": {
                                                            "healthType": {
                                                                "type": "string"
                                                            },
                                                            "reason": {
                                                                "type": "string"
                                                            },
                                                            "score": {
                                                                "type": "integer"
                                                            }
                                                        },
                                                        "type": "object"
                                                    },
                                                    "type": "array"
                                                },
                                                "hostIpV4": {
                                                    "type": "string"
                                                },
                                                "hostIpV6": {
                                                    "items": {
                                                        "type": "string"
                                                    },
                                                    "type": "array"
                                                },
                                                "hostMac": {
                                                    "type": "string"
                                                },
                                                "hostName": {
                                                    "type": "string"
                                                },
                                                "hostOs": {
                                                    "type": "string"
                                                },
                                                "hostType": {
                                                    "type": "string"
                                                },
                                                "hostVersion": {
                                                    "type": "string"
                                                },
                                                "hwModel": {
                                                    "type": "string"
                                                },
                                                "id": {
                                                    "type": "string"
                                                },
                                                "identifier": {
                                                    "type": "string"
                                                },
                                                "intelCapable": {
                                                    "type": "boolean"
                                                },
                                                "iosCapable": {
                                                    "type": "boolean"
                                                },
                                                "isGuestUPNEndpoint": {
                                                    "type": "boolean"
                                                },
                                                "issueCount": {
                                                    "type": "integer"
                                                },
                                                "l2VirtualNetwork": {
                                                    "type": "string"
                                                },
                                                "l3VirtualNetwork": {
                                                    "type": "string"
                                                },
                                                "lastUpdatedTime": {
                                                    "type": "integer"
                                                },
                                                "latencyBe": {
                                                    "type": "integer"
                                                },
                                                "latencyBg": {
                                                    "type": "integer"
                                                },
                                                "latencyVideo": {
                                                    "type": "integer"
                                                },
                                                "latencyVoice": {
                                                    "type": "integer"
                                                },
                                                "linkSpeed": {
                                                    "type": "integer"
                                                },
                                                "linkThreshold": {
                                                    "type": "string"
                                                },
                                                "location": {
                                                    "type": "string"
                                                },
                                                "maxRoamingDuration": {
                                                    "type": "string"
                                                },
                                                "modelName": {
                                                    "type": "string"
                                                },
                                                "onboarding": {
                                                    "properties": {
                                                        "aaaServerIp": {
                                                            "type": "string"
                                                        },
                                                        "assocDoneTime": {
                                                            "type": "integer"
                                                        },
                                                        "authDoneTime": {
                                                            "type": "integer"
                                                        },
                                                        "averageAssocDuration": {
                                                            "type": "string"
                                                        },
                                                        "averageAuthDuration": {
                                                            "type": "string"
                                                        },
                                                        "averageDhcpDuration": {
                                                            "type": "string"
                                                        },
                                                        "averageRunDuration": {
                                                            "type": "string"
                                                        },
                                                        "dhcpDoneTime": {
                                                            "type": "integer"
                                                        },
                                                        "dhcpRootCauseList": {
                                                            "items": {
                                                                "type": "string"
                                                            },
                                                            "type": "array"
                                                        },
                                                        "dhcpServerIp": {
                                                            "type": "string"
                                                        },
                                                        "latestRootCauseList": {
                                                            "items": {
                                                                "type": "string"
                                                            },
                                                            "type": "array"
                                                        },
                                                        "maxAssocDuration": {
                                                            "type": "string"
                                                        },
                                                        "maxAuthDuration": {
                                                            "type": "string"
                                                        },
                                                        "maxDhcpDuration": {
                                                            "type": "string"
                                                        },
                                                        "maxRunDuration": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "type": "object"
                                                },
                                                "onboardingTime": {
                                                    "type": "integer"
                                                },
                                                "port": {
                                                    "type": "string"
                                                },
                                                "portDescription": {
                                                    "type": "string"
                                                },
                                                "powerType": {
                                                    "type": "string"
                                                },
                                                "privateMac": {
                                                    "type": "boolean"
                                                },
                                                "remoteEndDuplexMode": {
                                                    "type": "string"
                                                },
                                                "rssi": {
                                                    "type": "string"
                                                },
                                                "rssiIsInclude": {
                                                    "type": "string"
                                                },
                                                "rssiThreshold": {
                                                    "type": "string"
                                                },
                                                "rxBytes": {
                                                    "type": "string"
                                                },
                                                "rxLinkError": {
                                                    "type": "integer"
                                                },
                                                "rxRate": {
                                                    "type": "number"
                                                },
                                                "rxRetryPct": {
                                                    "type": "string"
                                                },
                                                "salesCode": {
                                                    "type": "string"
                                                },
                                                "sessionDuration": {
                                                    "type": "string"
                                                },
                                                "slotId": {
                                                    "type": "integer"
                                                },
                                                "snr": {
                                                    "type": "string"
                                                },
                                                "snrIsInclude": {
                                                    "type": "string"
                                                },
                                                "snrThreshold": {
                                                    "type": "string"
                                                },
                                                "ssId": {
                                                    "type": "string"
                                                },
                                                "subType": {
                                                    "type": "string"
                                                },
                                                "tracked": {
                                                    "type": "string"
                                                },
                                                "trustDetails": {
                                                    "type": "string"
                                                },
                                                "trustScore": {
                                                    "type": "string"
                                                },
                                                "txBytes": {
                                                    "type": "string"
                                                },
                                                "txLinkError": {
                                                    "type": "integer"
                                                },
                                                "txRate": {
                                                    "type": "number"
                                                },
                                                "upnId": {
                                                    "type": "string"
                                                },
                                                "upnName": {
                                                    "type": "string"
                                                },
                                                "upnOwner": {
                                                    "type": "string"
                                                },
                                                "usage": {
                                                    "type": "integer"
                                                },
                                                "userId": {
                                                    "type": "string"
                                                },
                                                "versionTime": {
                                                    "type": "string"
                                                },
                                                "vlanId": {
                                                    "type": "integer"
                                                },
                                                "vnId": {
                                                    "type": "string"
                                                },
                                                "wlcName": {
                                                    "type": "string"
                                                },
                                                "wlcUuid": {
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
