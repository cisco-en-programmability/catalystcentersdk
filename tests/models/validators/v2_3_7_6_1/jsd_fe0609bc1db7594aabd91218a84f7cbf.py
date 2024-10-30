# -*- coding: utf-8 -*-
"""Cisco Catalyst Center GetTheDetailsOfIssuesForGivenSetOfFiltersKnowYourNetworkV1 data model.

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


class JSONSchemaValidatorFe0609Bc1Db7594AAbd91218A84F7Cbf(object):
    """GetTheDetailsOfIssuesForGivenSetOfFiltersKnowYourNetworkV1 request
    schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorFe0609Bc1Db7594AAbd91218A84F7Cbf, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "page": {
                "properties": {
                "count": {
                "type": "integer"
                },
                "limit": {
                "type": "integer"
                },
                "offset": {
                "type": "integer"
                },
                "sortBy": {
                "items": {
                "properties": {
                "name": {
                "type": "string"
                },
                "order": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "response": {
                "items": {
                "properties": {
                "additionalAttributes": {
                "items": {
                "properties": {
                "key": {
                "type": "string"
                },
                "value": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "category": {
                "type": "string"
                },
                "description":
                 {
                "type": "string"
                },
                "deviceType": {
                "type": "string"
                },
                "entityId": {
                "type": "string"
                },
                "entityType": {
                "type": "string"
                },
                "firstOccurredTime": {
                "type": "integer"
                },
                "isGlobal": {
                "type": "boolean"
                },
                "issueId": {
                "type": "string"
                },
                "mostRecentOccurredTime": {
                "type": "integer"
                },
                "name": {
                "type": "string"
                },
                "notes": {
                "type": "object"
                },
                "priority": {
                "type": "string"
                },
                "severity": {
                "type": "string"
                },
                "siteHierarchy": {
                "type": "object"
                },
                "siteHierarchyId": {
                "type": "object"
                },
                "siteId": {
                "type": "object"
                },
                "siteName": {
                "type": "object"
                },
                "status": {
                "type": "string"
                },
                "suggestedActions": {
                "items": {
                "properties": {
                "message": {
                "type": "string"
                },
                "steps": {
                "items": {
                "type": "object"
                },
                "type": "array"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "summary": {
                "type": "string"
                },
                "updatedBy": {
                "type": "object"
                },
                "updatedTime": {
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
                }'''.replace("\n" + ' ' * 16, '')
        ))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                '{} is invalid. Reason: {}'.format(request, e.message)
            )