"""Cisco Catalyst Center Know Your Network API wrapper.

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

from ...restsession import RestSession
from ...utils import (
    apply_path_params,
    check_type,
    dict_from_items_with_values,
    dict_of_str,
)


class KnowYourNetwork:
    """Cisco Catalyst Center Know Your Network API (version: 3.2.3.0).

    Wraps the Catalyst Center Know Your Network
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new KnowYourNetwork
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Catalyst Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super().__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_energy_trend_analytics(
        self,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        page=None,
        startTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Retrieve the energy trend analytics data related to device energy consumption for all devices, including network
        devices and clients assigned to specific sites. For detailed information about the usage of the API,
        please refer to the Open API specification document - https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        deviceEnergy_1.0-1.0.1-resolved.yaml.   Retrieve the energy trend analytics data related to device
        energy consumption for all devices, including network devices and clients assigned to specific sites.
        Utilize advanced filters to query a specific subset of energy information. The input payload contains
        the following fields: Field Name Description startTime Start time from which API queries the data set
        related to the resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. If
        startTime  is not provided, API will default to one day before  endTime . endTime End time to which API
        queries the data set related to the resource. It must be specified in UNIX epochtime in milliseconds.
        Value is inclusive. If  endTime  is not provided, API will default to one day after  startTime . If
        startTime  is not provided either, API will default to current time. trendInterval Specifies the
        granularity on which data should be queried. Ex. If 1HR is specified than the data returned will in 1
        hour interval. By default, if no value is specified for 24 hours or less, it would be 1HR interval and
        anything more than 24 hours, the interval would be 1 day. filters Used to define one or more filter
        conditions. Only devices that satisfy these conditions will be taken into consideration during the
        aggregation calculation. This field can be empty. The supported list of filter keys and operators are:
        'id', 'deviceName', 'deviceCategory', 'deviceSubCategory', 'siteId', 'siteHierarchy', 'siteHierarchyId'
        . groupBy Specifies the attributes for grouping the data. The supported attributes are specified in
        DeviceEnergyGroupBy  model. As of now, Group by supports the following combinations of attributes:
        ['deviceCategory'], ['deviceSubCategory'], and ['deviceCategory', 'deviceSubCategory'] . attributes The
        attribute is useful for obtaining one or more field data in addition to the aggregated data within the
        specified start and end time range. The supported attributes are listed in  DeviceEnergyAttribute
        model. aggregateAttributes Specifies the name of the attribute on which the aggregate function should be
        applied when querying the data. The supported attribute names are listed in
        DevicesEnergyAggregateAttribute  model. page Contains  limit, offset and sortBy  fields.  limit  Number
        of records to fetch in a page,  offset  starting offset of data and  sortBy  attribute name, order and
        function if you want to sort by the aggregated field.  sortBy  field is a list, but only single field
        sorting is supported on this API. Notes: If 'groupby.attributes' is left empty or set to default, the
        result will be an aggregation of all filtered data. If no 'aggregateattributes' are specified, the
        default attributes and functions applied are 'avg' for carbonIntensity and 'sum' for 'energyConsumed',
        'estimatedCost', and 'estimatedEmission'. How the filtering behavior works The filters field in each
        post body can be used in numerous ways: Each filter in the list of filters will applied ''together'' In
        the example below, this would request filtering data from devices belonging to the ''Switch'' family
        and  have series equal to ''cat9300'' or ''cat9400''. 'filters': [   {     'key': 'deviceCategory',
        'operator': 'eq',     'value': 'Switch'   },   {     'key': 'deviceSubCategory',     'operator': 'in',
        'value': [       'cat9300',       'cat9400'     ]   } ] Each filter object can contrastingly utilize its
        logical operator  to provide nested filtering functionality. In the example below you can see a logical
        'OR' filter being applied using the nested filtering functionality: The primary filter object does not
        have its 'key', 'value', or 'operator' fields populated. Only the 'logicalOperator' field is populated,
        to indicate the filters within the nested filters list are to be logically conjoined. 'filters': [   {
        'logicalOperator': 'or',     'filters': [       {         'key': 'deviceCategory',         'operator':
        'eq',         'value': 'Switch'       },       {         'key': 'deviceSubCategory',         'operator':
        'in',         'value': ['cat9300', 'cat9400']       }     ]   } ] Please refer to the 'API Support
        Documentation' section to understand which fields and filters are supported. How Pagination Works
        'limit' field, is the total number of records you want to retrieve. 'offset' field, is the record you
        want to start on. 'timestampOrder' is supported for trend analytics with 'asc' (ascending), or 'desc'
        (descending) ordering Example1 Request Body: {   'startTime': 1710964767403,   'endTime': 1711051167403,
        'filters': [     {       'key': 'siteHierarchyId',       'value':
        '/8df02c92-755e-4583-8c19-fb62ea75daf9*',       'operator': 'like'     }   ],   'groupBy': [],
        'aggregateAttributes': [     {       'name': 'energyConsumed',       'function': 'sum'     }   ],
        'page': {     'limit': 2,     'offset': 1,     'timestampOrder': 'desc'   } } Response: {   'response':
        [     {       'time': 1.7109648E+12,       'aggregateAttributes': [         {           'name':
        'energyConsumed',           'function': 'sum',           'value': 1343.875         }       ]     },
        {       'time': 1.7109684E+12,       'aggregateAttributes': [         {           'name':
        'energyConsumed',           'function': 'sum',           'value': 1033.25         }       ]     }   ],
        'page': {     'limit': 2,     'offset': 1,     'count': 24,     'timestampOrder': 'desc'   },
        'version': '1.0' }.

        Args:
            aggregateAttributes(list): Know Your Network's aggregateAttributes (list of objects).
            attributes(list): Know Your Network's attributes (list of strings).
            endTime(integer): Know Your Network's endTime.
            filters(list): Know Your Network's filters (list of objects).
            groupBy(list): Know Your Network's groupBy (list of strings).
            page(object): Know Your Network's page.
            startTime(integer): Know Your Network's startTime.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-energy-trend-analytics
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "startTime": startTime,
            "endTime": endTime,
            "filters": filters,
            "groupBy": groupBy,
            "attributes": attributes,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator("jsd_de4a255bc6849a7c9cec69f13c_v3_2_3_0").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/energy/trendAnalytics"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_de4a255bc6849a7c9cec69f13c_v3_2_3_0", json_data
        )

    def get_energy_summary_analytics(
        self,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        page=None,
        startTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Retrieve the summary analytics data related to device energy consumption for all devices, including network
        devices and clients assigned to specific sites. For detailed information about the usage of the API,
        please refer to the Open API specification document - https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        deviceEnergy_1.0-1.0.1-resolved.yaml.   Retrieve the summary analytics data related to device energy
        consumption for all devices, including network devices and clients assigned to specific sites. Utilize
        advanced filters to query a specific subset of energy information. The input payload contains the
        following fields Field Name Description startTime Start time from which API queries the data set related
        to the resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. If
        startTime is not provided, API will default to one day before endTime . endTime End time to which API
        queries the data set related to the resource. It must be specified in UNIX epochtime in milliseconds.
        Value is inclusive. If endTime is not provided, API will default to one day after startTime . If
        startTime is not provided either, API will default to current time. filters Used to define one or more
        filter conditions. Only devices that satisfy these conditions will be taken into consideration during
        the aggregation calculation. This field can be empty. The supported list of filter keys and operators
        are: "id", "deviceName", "deviceCategory", "deviceSubCategory", "siteId", "siteHierarchy",
        "siteHierarchyId" . groupBy Specifies the attributes for grouping the data. The supported attributes are
        speficied in DeviceEnergyGroupBy model. As of now, Group by supports the following combinations of
        attributes: ["deviceCategory"], ["deviceSubCategory"], and ["deviceCategory", "deviceSubCategory"] .
        attributes The attribute is useful for obtaining one or more field data in addition to the aggregated
        data within the specified start and end time range. The supported attributes are listed in
        DeviceEnergyAttribute model aggregateAttributes Specifies the name of the attribute on which the
        aggregate function should be applied when querying the data. The supported attribute names are listed in
        DevicesEnergyAggregateAttribute model. page Contains limit, offset and sortBy fields. limit Number of
        records to fetch in a page, offset starting offset of data and sortBy attribute name, order and function
        if you want to sort by the aggregated field. sortBy field is a list, but only single field sorting is
        supported on this API. Notes: If "groupby.attributes" is left empty or set to default, the result will
        be an aggregation of all filtered data. If no "aggregateattributes" are specified, the default
        attributes and functions appliedare "avg" for carbonIntensity and "sum" for "energyConsumed",
        "estimatedCost", and "estimatedEmission". How the filtering behavior works The filters field in each
        post body can be used in numerous ways: Each filter in the list of filters will applied ''together''. In
        the example below, this would request filtering data from devices belonging to the ''Switch'' family and
        have series equal to ''cat9300'' or ''cat9400'. 'filters': [   {     'key': 'deviceCategory',
        'operator': 'eq',     'value': 'Switch'   },   {     'key': 'deviceSubCategory',     'operator': 'in',
        'value': [       'cat9300',       'cat9400'     ]   } ] Each filter object can contrastingly utilize its
        logical operator to provide nested filtering functionality. In the example below you can see a logical
        "OR" filter being applied using the nested filtering functionality: The primary filter object does not
        have its 'key', 'value', or 'operator' fields populated. Only the 'logicalOperator' field is populated,
        to indicate the filters within the nested filters list are to be logically conjoined. 'filters': [   {
        'logicalOperator': 'or',     'filters': [       {         'key': 'deviceCategory',         'operator':
        'eq',         'value': 'Switch'       },       {         'key': 'deviceSubCategory',         'operator':
        'in',         'value': [           'cat9300',           'cat9400'         ]       }     ]   } ] Please
        refer to the 'API Support Documentation' section to understand which fields and filters are supported.
        How Pagination Works 'limit' field, is the total number of records you want to retrieve. 'offset' field,
        is the record you want to start on. If you have a limit of 100, each page would be viewed as 100
        elements. So starting with an offset of 1, means look at the first page (starting from first record). To
        get the second page, you need to specify offset 101 (starting with the 101st element). 'sortBy' field is
        a list, but only single field sorting is supported on this API, with 'asc' (ascending), or 'desc'
        (descending) ordering. 'page': {   'limit': 5,   'offset': 1,   'sortBy': [     {       'name':
        'siteId',       'order': 'desc',       'function': 'max'     }   ] } Example 1 :The JSON input below
        represents a request body used to retrieve sum data of deviceCount, energyConsumed on one specific site.
        {   'startTime': 1706590800000,   'endTime': 1707496410913,   'filters': [     {       'key':
        'siteHierarchyId',       'operator': 'like',       'value': '/8df02c92-755e-4583-8c19-
        fb62ea75daf9/416e8ba7-87d6-43c4-943a-d33dd3a93236/006be1b2-ffea-4a0c-9783-1a845ccddfec*'     }   ],
        'aggregateAttributes': [     {       'name': 'deviceCount',       'function': 'distinctCount'     },
        {       'name': 'energyConsumed',       'function': 'sum'     }   ],   'page': {     'limit': 100,
        'offset': 1   } } Response {   'response': {     'aggregateAttributes': [       {         'name':
        'deviceCount',         'function': 'distinctCount',         'value': 1       },       {         'name':
        'energyConsumed',         'function': 'sum',         'value': 108457.0       }     ]   },   'page': {
        'limit': 100,     'offset': 1,     'count': 1,     'sortBy': null   },   'version': '1.0' }.

        Args:
            aggregateAttributes(list): Know Your Network's aggregateAttributes (list of objects).
            attributes(list): Know Your Network's attributes (list of strings).
            endTime(integer): Know Your Network's endTime.
            filters(list): Know Your Network's filters (list of objects).
            groupBy(list): Know Your Network's groupBy (list of strings).
            page(object): Know Your Network's page.
            startTime(integer): Know Your Network's startTime.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-energy-summary-analytics
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "startTime": startTime,
            "endTime": endTime,
            "filters": filters,
            "groupBy": groupBy,
            "attributes": attributes,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d0b2cc705afb536fab6fd0848baa73c0_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/energy/summaryAnalytics"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_d0b2cc705afb536fab6fd0848baa73c0_v3_2_3_0", json_data
        )
