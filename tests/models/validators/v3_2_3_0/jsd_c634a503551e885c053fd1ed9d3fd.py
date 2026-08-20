"""Cisco Catalyst Center GetAnycastGateways data model.

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


class JSONSchemaValidatorC634A503551E885C053Fd1Ed9D3Fd:
    """GetAnycastGateways request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "properties": {
                        "response": {
                            "items": {
                                "properties": {
                                    "additionalIpPools": {
                                        "items": {
                                            "properties": {
                                                "name": {
                                                    "type": "string"
                                                },
                                                "order": {
                                                    "maximum": 5,
                                                    "minimum": 2,
                                                    "type": "integer"
                                                }
                                            },
                                            "required": [
                                                "name",
                                                "order"
                                            ],
                                            "type": "object"
                                        },
                                        "maxItems": 4,
                                        "minItems": 0,
                                        "type": "array"
                                    },
                                    "fabricId": {},
                                    "id": {},
                                    "ipPoolName": {},
                                    "isCriticalPool": {},
                                    "isGroupBasedPolicyEnforcementEnabled": {},
                                    "isIntraSubnetRoutingEnabled": {},
                                    "isIpDirectedBroadcast": {},
                                    "isLayer2FloodingEnabled": {},
                                    "isMacsecEncrypted": {},
                                    "isMultipleIpToMacAddresses": {},
                                    "isResourceGuardEnabled": {},
                                    "isSupplicantBasedExtendedNodeOnboarding": {},
                                    "isWirelessFloodingEnabled": {},
                                    "isWirelessPool": {},
                                    "layer2FloodingAddress": {},
                                    "layer2FloodingAddressAssignment": {},
                                    "poolType": {},
                                    "securityGroupName": {},
                                    "tcpMssAdjustment": {},
                                    "trafficType": {},
                                    "virtualNetworkName": {},
                                    "vlanId": {},
                                    "vlanName": {}
                                },
                                "type": "object"
                            },
                            "maxItems": 500,
                            "minItems": 0,
                            "type": "array"
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
