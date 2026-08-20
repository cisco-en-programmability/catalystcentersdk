"""Cisco Catalyst Center RetrieveTheComplianceDetailsOfNetworkDevices data model.

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


class JSONSchemaValidatorE539A3B94Ca52AfBf6C7Fd185C50B81:
    """RetrieveTheComplianceDetailsOfNetworkDevices request schema
    definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "items": {
                                "properties": {
                                    "acknowledgementStatus": {
                                        "enum": [
                                            "ACKNOWLEDGED",
                                            "UNACKNOWLEDGED"
                                        ],
                                        "type": "string"
                                    },
                                    "details": {
                                        "items": {
                                            "properties": {
                                                "acknowledgementStatus": {
                                                    "enum": [
                                                        "ACKNOWLEDGED",
                                                        "UNACKNOWLEDGED"
                                                    ],
                                                    "type": "string"
                                                },
                                                "complianceType": {
                                                    "enum": [
                                                        "RUNNING_CONFIG",
                                                        "PSIRT",
                                                        "EOX",
                                                        "NETWORK_SETTINGS",
                                                        "NETWORK_PROFILE",
                                                        "NETWORK_RULES",
                                                        "IMAGE",
                                                        "FABRIC",
                                                        "APPLICATION_VISIBILITY",
                                                        "WORKFLOW"
                                                    ],
                                                    "type": "string"
                                                },
                                                "errorCode": {
                                                    "type": "string"
                                                },
                                                "lastComplianceExecutionTime": {
                                                    "type": "integer"
                                                },
                                                "lastStatusChangeTime": {
                                                    "type": "integer"
                                                },
                                                "remediationSupported": {
                                                    "type": "boolean"
                                                },
                                                "severity": {
                                                    "enum": [
                                                        "CRITICAL",
                                                        "MAJOR",
                                                        "MINOR",
                                                        "INFO"
                                                    ],
                                                    "type": "string"
                                                },
                                                "status": {
                                                    "enum": [
                                                        "COMPLIANT",
                                                        "NON_COMPLIANT",
                                                        "NOT_APPLICABLE",
                                                        "NOT_AVAILABLE",
                                                        "ERROR",
                                                        "ABORTED",
                                                        "IN_PROGRESS",
                                                        "REMEDIATION_IN_PROGRESS"
                                                    ],
                                                    "type": "string"
                                                },
                                                "statusDescription": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "complianceType",
                                                "lastComplianceExecutionTime",
                                                "lastStatusChangeTime",
                                                "severity",
                                                "status"
                                            ],
                                            "type": "object"
                                        },
                                        "type": "array"
                                    },
                                    "id": {
                                        "type": "string"
                                    },
                                    "lastComplianceExecutionTime": {
                                        "type": "integer"
                                    },
                                    "lastStatusChangeTime": {
                                        "type": "integer"
                                    },
                                    "networkDeviceId": {
                                        "type": "string"
                                    },
                                    "nextScheduledComplianceExecutionTime": {
                                        "type": "integer"
                                    },
                                    "severity": {
                                        "enum": [
                                            "CRITICAL",
                                            "MAJOR",
                                            "MINOR",
                                            "INFO"
                                        ],
                                        "type": "string"
                                    },
                                    "status": {
                                        "enum": [
                                            "COMPLIANT",
                                            "NON_COMPLIANT",
                                            "NOT_APPLICABLE",
                                            "NOT_AVAILABLE",
                                            "ERROR",
                                            "ABORTED",
                                            "IN_PROGRESS",
                                            "REMEDIATION_IN_PROGRESS"
                                        ],
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
