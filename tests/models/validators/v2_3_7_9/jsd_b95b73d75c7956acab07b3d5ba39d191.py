# -*- coding: utf-8 -*-
"""Cisco Catalyst Center ReadTransitNetworkWithItsHealthSummaryFromIdV1 data model.

Copyright (c) 2024 Cisco Systems.

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
from builtins import *

import fastjsonschema

from catalystcentersdk.exceptions import MalformedRequest


class JSONSchemaValidatorB95B73D75C7956AcAb07B3D5Ba39D191(object):
    """ReadTransitNetworkWithItsHealthSummaryFromIdV1 request schema
    definition."""
    def __init__(self):
        super(JSONSchemaValidatorB95B73D75C7956AcAb07B3D5Ba39D191, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "properties": {
                "bgpTcpFairHealthDeviceCount": {
                "type": "integer"
                },
                "bgpTcpGoodHealthDeviceCount": {
                "type": "integer"
                },
                "bgpTcpHealthPercentage": {
                "type": "integer"
                },
                "bgpTcpPoorHealthDeviceCount": {
                "type": "integer"
                },
                "bgpTcpTotalDeviceCount": {
                "type": "integer"
                },
                "controlPlaneCount": {
                "type": "integer"
                },
                "fabricSitesCount": {
                "type": "integer"
                },
                "fairHealthDeviceCount": {
                "type": "integer"
                },
                "goodHealthDeviceCount": {
                "type": "integer"
                },
                "goodHealthPercentage": {
                "type": "integer"
                },
                "id": {
                "type": "string"
                },
                "internetAvailTransitFairHealthDeviceCount": {
                "type": "integer"
                },
                "internetAvailTransitGoodHealthDeviceCount": {
                "type": "integer"
                },
                "internetAvailTransitHealthPercentage": {
                "type": "integer"
                },
                "internetAvailTransitPoorHealthDeviceCount": {
                "type": "integer"
                },
                "internetAvailTransitTotalDeviceCount": {
                "type": "integer"
                },
                "lispTransitFairHealthDeviceCount": {
                "type": "integer"
                },
                "lispTransitGoodHealthDeviceCount": {
                "type": "integer"
                },
                "lispTransitHealthPercentage": {
                "type": "integer"
                },
                "lispTransitPoorHealthDeviceCount": {
                "type": "number"
                },
                "lispTransitTotalDeviceCount": {
                "type": "integer"
                },
                "name": {
                "type": "string"
                },
                "poorHealthDeviceCount": {
                "type": "integer"
                },
                "pubsubTransitFairHealthDeviceCount": {
                "type": "integer"
                },
                "pubsubTransitGoodHealthDeviceCount": {
                "type": "integer"
                },
                "pubsubTransitHealthPercentage": {
                "type": "integer"
                },
                "pubsubTransitPoorHealthDeviceCount": {
                "type": "integer"
                },
                "pubsubTransitTotalDeviceCount": {
                "type": "integer"
                },
                "totalDeviceCount": {
                "type": "integer"
                },
                "transitControlPlaneFairHealthDeviceCount": {
                "type": "integer"
                },
                "transitControlPlaneGoodHealthDeviceCount": {
                "type": "integer"
                },
                "transitControlPlaneHealthPercentage": {
                "type": "integer"
                },
                "transitControlPlanePoorHealthDeviceCount": {
                "type": "integer"
                },
                "transitControlPlaneTotalDeviceCount": {
                "type": "integer"
                },
                "transitServicesFairHealthDeviceCount": {
                "type": "integer"
                },
                "transitServicesGoodHealthDeviceCount": {
                "type": "integer"
                },
                "transitServicesHealthPercentage": {
                "type": "integer"
                },
                "transitServicesPoorHealthDeviceCount": {
                "type": "number"
                },
                "transitServicesTotalDeviceCount": {
                "type": "integer"
                },
                "transitType": {
                "type": "string"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                }'''.replace("\n" + ' ' * 16, '')
        ))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                '{} is invalid. Reason: {}'.format(request, e.message)
            )
