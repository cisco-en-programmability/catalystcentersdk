"""Cisco Catalyst Center Devices API wrapper.

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


class Devices:
    """Cisco Catalyst Center Devices API (version: 3.2.3.0).

    Wraps the Catalyst Center Devices
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Devices
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

    def get_trend_analytics_data_of_aaa_services_for_given_set_of_complex_filters(
        self,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        page=None,
        startTime=None,
        trendInterval=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Gets the trend analytics data related to AAA Services based on given filters and group by field. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-AAAServices-1.0.0-resolved.yaml.   Gets the trend analytics
        data related to AAA Services based on given filters and group by field. If startTime and endTime are not
        provided, the API defaults to the last 24 hours. Field Name Description startTime start time from which
        API queries the data set related to the resource. It must be specified in UNIX epochtime in
        milliseconds. Value is inclusive & the default is 24 hours ago from end time endTime end time to which
        API queries the data set related to the resource. It must be specified in UNIX epochtime in
        milliseconds. Value is inclusive & the default is current time trendInterval the trend time interval in
        minutues. This is a mantadory field. The possible values in minutes are  5 minutes, 15 minutes, 1 hour,
        1 day . groupBy specifies the attributes for grouping the data. filters used to define one or more
        conditions. Only the data that satisfy these conditions will be taken into consideration during the
        aggregation calculation. attributes attributes are used for obtaining one or more field's data in
        addition to the aggregated data. The supported attributes are listed in
        AAAServicesAnalyticsAttributeKey  model aggregateAttributes specifies the names of the attributes on
        which the aggregate function should be applied when querying the data. The supported attribute names are
        listed in  AAAServicesAggregateAttributeKey  model page contains  limit, offset, and timestampOrder
        fields.  limit  number of records to be returned in response.  offset  starting offset of data.
        timestampOrder  to sort the response based on the timestamp either in ascending or descending order.

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's attributes (list of strings).
            endTime(integer): Devices's endTime.
            filters(list): Devices's filters (list of objects).
            groupBy(list): Devices's groupBy (list of strings).
            page(object): Devices's page.
            startTime(integer): Devices's startTime.
            trendInterval(string): Devices's trendInterval.
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
            https://developer.cisco.com/docs/dna-center/#!get-trend-analytics-data-of-a-a-a-services-for-given-set-of-complex-filters
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
            "trendInterval": trendInterval,
            "groupBy": groupBy,
            "filters": filters,
            "attributes": attributes,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_c60312a923ee5a6fb3f2c725c32dc96f_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/aaaServices/trendAnalytics"
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
            "bpm_c60312a923ee5a6fb3f2c725c32dc96f_v3_2_3_0", json_data
        )

    def the_trend_analytics_data_for_the_network_device_in_the_specified_time_range(
        self,
        id,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        page=None,
        startTime=None,
        trendIntervalInMinutes=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """The Trend analytics data for the network Device in the specified time range. The data is grouped based on the
        trend time Interval, other input parameters like attribute and aggregate attributes. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-AssuranceNetworkDevices-2.0.1-resolved.yaml.   How the
        filtering behavior works   The filters field in each post body can be used in numerous ways:   Each
        filter in the list of filters will applied ''together'' ].

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's attributes (list of strings).
            endTime(integer): Devices's endTime.
            filters(list): Devices's filters (list of objects).
            groupBy(list): Devices's groupBy (list of strings).
            page(object): Devices's page.
            startTime(integer): Devices's startTime.
            trendIntervalInMinutes(integer): Devices's trendIntervalInMinutes.
            id(str): id path parameter. The device Uuid.
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
            https://developer.cisco.com/docs/dna-center/#!the-trend-analytics-data-for-the-network-device-in-the-specified-time-range
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "startTime": startTime,
            "endTime": endTime,
            "trendIntervalInMinutes": trendIntervalInMinutes,
            "groupBy": groupBy,
            "filters": filters,
            "attributes": attributes,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ca2f659b595c0ba7c649fd8c8bdad6_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/networkDevices/{id}/trendAnalytics"
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
            "bpm_ca2f659b595c0ba7c649fd8c8bdad6_v3_2_3_0", json_data
        )

    def get_global_settings_value_for_new_ssh_key_handling(
        self, headers=None, **request_parameters
    ):
        """This API retrieves the current settings for handling SSH key changes from network devices during SSH
        connections. If the `autoAcceptSshKeys` flag is `true`, SSH keys are accepted automatically. If it is
        `false`, manual approval is needed for any SSH key changes.

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-global-settings-value-for-new-s-s-h-key-handling
        """
        check_type(headers, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDeviceSettings/sshKeySettings"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bf69272a0b575fb4819bef563b0504_v3_2_3_0", json_data
        )

    def configure_global_settings_for_ssh_key_handling(
        self,
        autoAcceptSshKeys=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API lets users control how the system handles new SSH key from network devices during SSH connections. With
        the `autoAcceptSshKeys` flag set to `false`, the system will block the SSH connection if a network
        device presents a new SSH key. If the flag is set to `true`, the system will automatically accept the
        SSH key. Users can also use the device-specific `/dna/intent/api/v1/networkDevices/acceptSshKeyChange`
        API to approve SSH key changes individually when the global auto-accept is turned off.

        Args:
            autoAcceptSshKeys(boolean): Devices's Indicates whether SSH keys are automatically accepted.
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
            https://developer.cisco.com/docs/dna-center/#!configure-global-settings-for-s-s-h-key-handling
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "autoAcceptSshKeys": autoAcceptSshKeys,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_c297e60246665ade932f94cd3fe2c3cf_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDeviceSettings/sshKeySettings"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_c297e60246665ade932f94cd3fe2c3cf_v3_2_3_0", json_data
        )

    def query_network_devices_with_filters(
        self,
        filter=None,
        page=None,
        views=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Returns the list of network devices, determined by the filters. It is possible to filter the network devices
        based on various parameters, such as device type, device role, software version, etc.  **How the
        filtering behavior works**  All items in the `filters` array are combined using the `AND` operator by
        default. This can be changed by setting the `logicalOperator` field in the `filter` object to `OR`.
        Each item in the array is filtered on the `key`, `operator`, and `value` fields. For string fields, such
        as `hostname`, the operators `eq`, `contains`, and `in` are allowed. For numerical fields, such as
        timestamps, the operators `eq`, `in` `gt`, `lt`, `gte`, and `lte` are allowed. Array of values can be
        provided for the `value` field when using the `in` operator.  Network devices can be queried by
        `userDefinedFields` by providing the `key` as `userDefinedFields. ` and the `value`. Only `eq` operator
        is allowed.  For   ### Examples of request body for the filter.  *Example 1: Multiple values for a
        filter item*  ```json {     "filter": {         "filters": [             {                 "key":
        "deviceSupportLevel",                 "operator": "in",                 "value": ["SUPPORTED",
        "THIRD_PARTY"]             }         ]     },     "views": ["BASIC"],     "page": {         "limit": 10,
        "offset": 1     } } ```  The above example will return the first 10 network devices that have the
        deviceSupportLevel as `SUPPORTED` or `THIRD_PARTY`.  *Example 2: Multiple filter items* ```json {
        "filter": {         "filters": [             {                 "key": "deviceSupportLevel",
        "operator": "in",                 "value": ["SUPPORTED", "THIRD_PARTY"]             },             {
        "key": "softwareVersion",                 "operator": "eq",                 "value": "16.12.1"
        }         ]     },     "views": ["BASIC"],     "page": {         "limit": 10,         "offset": 1     }
        } ```  The above example will return the first 10 network devices with the deviceSupportLevel
        `SUPPORTED` or `THIRD_PARTY` AND the softwareVersion `16.12.1`.  *Example 3: Filtering based on multiple
        user-defined fields and values* ```json {     "filter": {         "filters":[             {
        "key": "deviceSupportLevel",                 "operator": "in",                 "value": ["SUPPORTED",
        "THIRD_PARTY"]             },             {                 "key": "userDefinedFields.Location",
        "operator": "eq",                 "value": Building 1"             },             {
        "key": "userDefinedFields.Department",                 "operator": "eq",                 "value":
        "Engineering"             }         ]     },     "views": ["BASIC", "USER_DEFINED_FIELDS"],     "page":
        {         "limit": 10,         "offset": 1     } } ``` The above example will return the first 10
        network devices that have the user-defined field `Location` with values `Building 1` or `Building 2` and
        the user-defined field `Department` with value `Engineering` and the deviceSupportLevel as `SUPPORTED`
        or `THIRD_PARTY`.   **Supported filter keys and types** | Key                        | Value Type |
        Allowed Operators                |
        |----------------------------|------------|----------------------------------| | id
        | string     | eq, contains, in                 | | managementAddress          | string     | eq,
        contains, in                 | | hostname                   | string     | eq, contains, in
        | | macAddress                 | string     | eq, contains, in                 | | serialNumbers
        | string     | eq, contains, in                 | | type                       | string     | eq,
        contains, in                 | | family                     | string     | eq, contains, in
        | | series                     | string     | eq, contains, in                 | | status
        | string     | eq, contains, in                 | | platformIds                | string     | eq,
        contains, in                 | | softwareType               | string     | eq, contains, in
        | | softwareVersion            | string     | eq, contains, in                 | | stackDevice
        | boolean    | eq                               | | bootTime                   | string     | eq,
        contains, in                 | | role                       | string     | eq, contains, in
        | | roleSource                 | string     | eq, contains, in                 | | apWlcIpAddress
        | string     | eq, contains, in                 | | deviceSupportLevel         | string     | eq,
        contains, in                 | | reachabilityStatus         | string     | eq, contains, in
        | | managementState            | string     | eq, contains, in                 | | resyncEndTime
        | integer    | eq, lt, gt, lte, gte, in         | | resyncIntervalSource       | string     | eq,
        contains, in                 | | resyncIntervalMinutes      | integer    | eq, lt, gt, lte, gte, in
        | | errorCode                  | string     | eq, contains, in                 | |
        userDefinedFields.fieldName| string     | eq, contains                     | | secureMode
        | string     | eq, in                 |  **How views work** The `views` parameter is an optional field
        to specify which attributes to retrieve. If this is not provided, then it will default to `BASIC` views.
        If multiple views are provided, the response will  contain the union of the views.  Attributes covered
        by the views are: * `BASIC`: id, managementAddress, dnsResolvedManagementIpAddress, hostname,
        macAddress, serialNumbers, type, family, series, status, platformIds, softwareType, softwareVersion,
        vendor, stackDevice, bootTime, role, roleSource, apEthernetMacAddress, apManagerInterfaceIpAddress,
        apWlcIpAddress, deviceSupportLevel, snmpContact, snmpLocation, secureMode * `RESYNC`: id,
        managementAddress, dnsResolvedManagementIpAddress, hostname, macAddress, serialNumbers, type, family,
        series, status, reachabilityStatus, reachabilityFailureReason, managementState,
        lastSuccessfulResyncReasons, resyncStartTime, resyncEndTime, resyncReasons, resyncRequestedByApps,
        pendingResyncRequestCount, pendingResyncRequestReasons, resyncIntervalSource, resyncIntervalMinutes,
        errorCode, errorDescription, secureMode * `USER_DEFINED_FIELDS`: id, managementAddress,
        dnsResolvedManagementIpAddress, hostname, macAddress, serialNumbers, type, family, series, status,
        userDefinedFields  **Note**: `CREDENTIALS` view is not supported in this API. Use the
        `/dna/intent/api/v1/networkDevices/{id}` API to get the credentials of a network device.

        Args:
            filter(object): Devices's Filter to query network devices. The result will contain the network devices
                that match ALL the filter criteria  (AND condition) unless specified in
                'logicalOperator'. Total number of filter criteria should not exceed 20. .
            page(object): Devices's Pagination related parameters. This is an optional parameter which can be passed
                to get the paginated response.
            views(list): Devices's The specific views being requested. This is an optional parameter which can be
                passed to get one or more of the network  device data. If this is not provided, then it
                will default to `BASIC` views. If multiple views are provided, the response  will
                contain the union of the views.  Attributes covered by the views are: Attributes covered
                by the views are: * `BASIC`: id, managementAddress, dnsResolvedManagementIpAddress,
                hostname, macAddress, serialNumbers, type, family, series, status, platformIds,
                softwareType, softwareVersion, vendor, stackDevice, bootTime, role, roleSource,
                apEthernetMacAddress, apManagerInterfaceIpAddress, apWlcIpAddress, deviceSupportLevel,
                snmpContact, snmpLocation, secureMode * `RESYNC`: id, managementAddress,
                dnsResolvedManagementIpAddress, hostname, macAddress, serialNumbers, type, family,
                series, status, reachabilityStatus, reachabilityFailureReason, managementState,
                lastSuccessfulResyncReasons, resyncStartTime, resyncEndTime, resyncReasons,
                resyncRequestedByApps, pendingResyncRequestCount, pendingResyncRequestReasons,
                resyncIntervalSource, resyncIntervalMinutes, errorCode, errorDescription, secureMode *
                `USER_DEFINED_FIELDS`: id, managementAddress, dnsResolvedManagementIpAddress, hostname,
                macAddress, serialNumbers, type, family, series, status, userDefinedFields  (list of
                strings. Available values are 'BASIC', 'RESYNC' and 'USER_DEFINED_FIELDS').
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
            https://developer.cisco.com/docs/dna-center/#!query-network-devices-with-filters
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "filter": filter,
            "views": views,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_fff3662537e538f82bfb5809e30b3df_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDevices/query"
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
            "bpm_fff3662537e538f82bfb5809e30b3df_v3_2_3_0", json_data
        )

    def get_module_info_by_id(self, id, headers=None, **request_parameters):
        """Returns Module info by 'module id'.

        Args:
            id(str): id path parameter. Module id.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-module-info-by-id
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/module/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a4588640da5b018b499c5760f4092a_v3_2_3_0", json_data
        )

    def retrieves_the_list_of_wireless_controllers_statistics(
        self,
        attribute=None,
        end_time=None,
        limit=None,
        offset=None,
        order=None,
        sort_by=None,
        start_time=None,
        view=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the list of Wireless Controllers' statistics. If startTime and endTime are not provided, the API
        defaults to the last 24 hours.

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            view(list, set, str, tuple): view query parameter. WLC Stats related Views Refer to WlcStatsView schema
                for list of views supported Examples: `view=ClientBandCounts` (single view requested)
                `view=clientAssociationCounts&view=clientStateCounts` (multiple view requested) .
            attribute(list, set, str, tuple): attribute query parameter. List of attributes related to resource that
                can be requested to only be part of the response along with the required attributes.
                Refer to WlcStatsAttribute schema for list of attributes supported Examples:
                `attribute=totalClientCount` (single attribute requested)
                `attribute=totalClientCount&attribute=clientRoamCounts` (multiple attribute requested).
            limit(int): limit query parameter. Maximum number of records to return.
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1.
            sort_by(str): sortBy query parameter. A field within the response to sort by.
            order(str): order query parameter. The sort order of the field ascending or descending.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-wireless-controllers-statistics
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(view, (list, set, str, tuple))
        check_type(attribute, (list, set, str, tuple))
        check_type(limit, int)
        check_type(offset, int)
        check_type(sort_by, str)
        check_type(order, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "view": view,
            "attribute": attribute,
            "limit": limit,
            "offset": offset,
            "sortBy": sort_by,
            "order": order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/wirelessControllersStats"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ccba8f6b875869a62c451f96ef1b08_v3_2_3_0", json_data
        )

    def retrieve_port_channels_count_for_a_network_device(
        self, network_device_id, id=None, name=None, headers=None, **request_parameters
    ):
        """This API endpoint retrieves the count of port channels for the given network device.

        Args:
            network_device_id(str): networkDeviceId path parameter. Unique identifier for the network device.
            id(str): id query parameter. Optional list of the port channel ids to filter by.
            name(str): name query parameter. Optional name of the port channel to filter by. This supports partial
                search. For example, searching for "Port" will match "Port-channel1", "Port-channel2",
                etc. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-port-channels-count-for-a-network-device
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(name, str)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "name": name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/networkDevices/{networkDeviceId}/port"
            + "Channels/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_eef6fe8cbdb35819ad2c9e83c6fa9876_v3_2_3_0", json_data
        )

    def get_chassis_details_for_device(
        self, device_id, headers=None, **request_parameters
    ):
        """Returns chassis details for given device ID.

        Args:
            device_id(str): deviceId path parameter. Device ID.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-chassis-details-for-device
        """
        check_type(headers, dict)
        check_type(device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceId": device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/{deviceId}/chassis"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a03cee8dfd7514487a134a422f5e0d7_v3_2_3_0", json_data
        )

    def get_all_user_defined_fields(
        self, id=None, name=None, headers=None, **request_parameters
    ):
        """Gets existing global User Defined Fields. If no input is given, it fetches ALL the Global UDFs. Filter/search is
        supported by UDF Id(s) or UDF name(s) or both.

        Args:
            id(str): id query parameter. Comma-seperated id(s) used for search/filtering.
            name(str): name query parameter. Comma-seperated name(s) used for search/filtering.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-all-user-defined-fields
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "name": name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/user-defined-field"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d31b0bb4bde55bb8a3078b66c81f3a22_v3_2_3_0", json_data
        )

    def create_user_defined_field(
        self,
        description=None,
        name=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Creates a new global User Defined Field, which can be assigned to devices.

        Args:
            description(string): Devices's Description of UDF.
            name(string): Devices's Name of UDF.
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
            https://developer.cisco.com/docs/dna-center/#!create-user-defined-field
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "name": name,
            "description": description,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ed266e6eda225aedbf581508635da822_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/user-defined-field"
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
            "bpm_ed266e6eda225aedbf581508635da822_v3_2_3_0", json_data
        )

    def query_assurance_events(
        self,
        device_family,
        ap_mac=None,
        attribute=None,
        client_mac=None,
        end_time=None,
        limit=None,
        message_type=None,
        network_device_id=None,
        network_device_name=None,
        offset=None,
        order=None,
        severity=None,
        site_hierarchy_id=None,
        site_id=None,
        sort_by=None,
        start_time=None,
        view=None,
        headers=None,
        **request_parameters
    ):
        """Returns the list of events discovered by Catalyst Center, determined by the complex filters. Please refer to the
        'API Support Documentation' section to understand which fields are supported. For detailed information
        about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-AssuranceEvents-1.0.0-resolved.yaml.   OpenAPI specification
        defined to fetch the list of assurance events using basic filters present in Catalyst Center   API
        Support Documentation   Note that querying of data spanning more than 7 days is not allowed, so
        difference between startTime and endTime must not be more than that.   Query Parameters:   deviceFamily
        Supported values: Switches and Hubs, Routers, Wireless Controller, Third Party Device, Unified AP, Wired
        Client, and  Wireless Client   Please note that multiple families across network device type and client
        type is not allowed.       For example, choosing 'Routers' along with 'Wireless Client' or 'Unified AP'
        is not supported.      Examples :      ?deviceFamily=Switches and Hubs (single deviceFamily requested)
        ?deviceFamily=Switches and Hubs&deviceFamily=Routers (multiple deviceFamily requested)   startTime
        Start time from which API queries the data set related to the resource. It must be specified in UNIX
        epochtime in milliseconds. Value is inclusive.    If 'startTime' is not provided, API will default to
        current time minus 24 hours.   endTime   End time to which API queries the data set related to the
        resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive.    If 'endTime' is
        not provided, API will default to current time.   messageType   Message type for the event.    Supported
        values: Syslog, Trap, Device, Device Controller, ISE and TDL      Examples :      ?messageType=Syslog
        (single messageType requested)     ?messageType=Trap&messageType=Syslog (multiple messageType requested)
        severity   Severity of the event between 0 and 6. This is applicable only for events related to network
        devices (other than AP) and 'Wired Client' events.     Examples :      ?severity=0 (single severity
        requested)     ?severity=0&severity=1 (multiple severity requested)   siteId     The UUID of the site.
        Ex:flooruuid      Examples :      ?siteId=uuiid1 (single siteId requested)
        ?siteId=uuid2&siteId=uuid3 (multiple siteId requested)   siteHierarchyId     The full hierarchy
        breakdown of the site tree in id form starting from Global site UUID and ending with the specific site
        UUID. Ex: globalUuid/areaUuid/buildingUuid/floorUuid    This field supports wildcard ('*') character-
        based search. Ex: *uuid* or uuid* or *uuid     Examples :
        ?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid (single siteHierarchyId requested)     ?site
        HierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=globalUuid/areaUuid2/buildingUuid
        2/floorUuid2 (multiple siteHierarchyId requested)   networkDeviceName   Network device name. This
        parameter is applicable for network device related families.    This field supports wildcard ('*')
        character-based search. Ex: *Branch* or Branch* or *Branch      Examples :
        ?networkDeviceName=Branch-3-Gateway (single networkDeviceName requested)
        ?networkDeviceName=Branch-3-Gateway&networkDeviceName=Branch-3-Switch (multiple networkDeviceName
        requested)   networkDeviceId     The Network Device Uuids. Ex: 6bef213c-19ca-4170-8375-b694e251101c
        Examples :      ?networkDeviceId=6bef213c-19ca-4170-8375-b694e251101c (single networkDeviceId requested)
        ?networkDeviceId=6bef213c-19ca-4170-8375-b694e251101c&networkDeviceId=2541e9a7-b80d-4955-8aa2-
        79b233318ba0 (multiple networkDeviceId requested)   apMac   MAC address of the access point. This
        parameter is applicable for 'Unified AP' and 'Wireless Client' events.    This field supports wildcard
        ('*') character-based search. Ex: *50:0F* or 50:0F* or *50:0F     Examples :
        ?apMac=50:0F:80:0F:F7:E0 (single apMac requested)     ?apMac=50:0F:80:0F:F7:E0&apMac=18:80:90:AB:7E:A0
        (multiple apMac requested)   clientMac   MAC address of the client. This parameter is applicable for
        'Wired Client' and 'Wireless Client' events.    This field supports wildcard ('*') character-based
        search. Ex: *66:2B* or 66:2B* or *66:2B     Examples :      ?clientMac=66:2B:B8:D2:01:56 (single
        clientMac requested)     ?clientMac=66:2B:B8:D2:01:56&clientMac=DC:A6:32:F5:5A:89 (multiple clientMac
        requested)   view   Specified 'view' can be requested. Each view correspondsto different sets of data.
        By default basic view attributes will be shown   'view' an optional parameter which can be passed to get
        one or more of the views.         View   Response Data           basic   id, name, timestamp, details,
        messageType, siteHierarchyId, siteHierarchy, deviceFamily, networkDeviceId, networkDeviceName,
        managementIpAddress       network   id, name, severity, facility, mnemonic, eventStatus, timestamp,
        details, messageType, siteHierarchyId, siteHierarchy, deviceFamily, networkDeviceId, networkDeviceName,
        managementIpAddress, replacedDeviceSerialNumber, replacingDeviceSerialNumber, switchNumber       ap
        id, name, eventStatus, timestamp, details, messageType, siteHierarchyId, siteHierarchy, deviceFamily,
        networkDeviceId, networkDeviceName, managementIpAddress, apMac, wlcName, frequency, apSwitchName,
        apSwitchId, wlcId, reasonDescription, lastApDisconnectReason, lastApResetType, apRadioOperationState,
        currentRadioPowerLevel, previousRadioPowerLevel, newRadioChannelList, newRadioChannelWidth,
        oldRadioChannelList, oldRadioChannelWidth, radioNoise, radioInterference, radioChannelUtilization,
        affectedClients       wiredClient   id, name, severity, facility, mnemonic, eventStatus, timestamp,
        details, messageType, siteHierarchyId, siteHierarchy, deviceFamily, networkDeviceId, networkDeviceName,
        managementIpAddress, identifier, clientMac, connectedInterfaceName, ipv4, ipv6, vlanId, auditSessionId,
        reasonDescription       wirelessClient   id, name, timestamp, details, messageType, siteHierarchyId,
        siteHierarchy, deviceFamily, networkDeviceId, networkDeviceName, identifier, clientMac,
        wirelessClientEventStartTime, wirelessClientEventEndTime, radioChannelSlot, isPrivateMac, vlanId,
        authServerIp, apRole, assocRssi, assocSnr, udnName, udnId, duid, failureIpAddress, roamType,
        subReasonDescription, invalidIeAPs, candidateAPs, missingResponseAPs, apMac, wlcName, wlcId, ssid,
        username, frequency, resultStatus, failureCategory, dhcpServerIp, ipv4, ipv6, reasonDescription,
        childEvents           Examples :   ?view=network (single view requested)
        ?view=wiredClient&view=network (multiple view requested)   attribute   The list of attributes that needs
        to be included in the response. If this parameter is not provided, then basic attributes ('id', 'name',
        'timestamp', 'details', 'messageType', 'siteHierarchyId', 'siteHierarchy', 'deviceFamily',
        'networkDeviceId', 'networkDeviceName', 'managementIpAddress') would be part of the response.
        Supported Attributes:   affectedClients ,  apMac ,  apRadioOperationState ,  apRole ,  apSwitchName ,
        apSwitchId ,  assocRssi ,  assocSnr ,  auditSessionId , authServerIp , bssid , candidateAPs ,
        childEvents , clientMac ,  connectedInterfaceName , currentRadioPowerLevel ,  details , deviceFamily ,
        dhcpServerIp , duid ,  eventStatus ,  facility , failureCategory ,  failureIpAddress ,  frequency , id ,
        identifier , invalidIeAPs ,  ipv4 , ipv6 , isPrivateMac ,  lastApDisconnectReason , lastApResetType ,
        managementIpAddress , messageType ,  missingResponseAPs ,  mnemonic , name ,  networkDeviceId ,
        networkDeviceName , newRadioChannelList ,  newRadioChannelWidth , oldRadioChannelList ,
        oldRadioChannelWidth , previousRadioPowerLevel ,  radioChannelSlot ,  radioChannelUtilization ,
        radioInterference , radioNoise , reasonDescription , replacedDeviceSerialNumber ,
        replacingDeviceSerialNumber , resultStatus , roamType , severity , siteHierarchy , siteHierarchyId ,
        ssid , subReasonDescription , switchNumber , timestamp , udnId , udnName , username , vlanId ,
        wirelessClientEventEndTime , wirelessClientEventStartTime , wlcId wlcName     If length of attribute
        list is too long, when using the query parameter, please use  view  param instead.     Examples :
        ?attribute=id (single attribute requested)   ?attribute=id&attribute=name (multiple attribute requested)
        offset   Specifies the starting point within all records returned by the API. It's one based offset. The
        starting value is 1.   limit   Maximum number of records to return.   sortBy   A field within the
        response to sortBy. Default value : timestamp    Supported sortBy values based on device family
        Network Device: name, messageType, severity, networkDeviceId, networkDeviceName, managementIpAddress,
        timestamp            Unified AP: name, messageType, severity, networkDeviceId, networkDeviceName,
        managementIpAddress, apMac, wlcId, wlcName, frequency, timestamp            Wired Client: name,
        messageType, severity, ipv4, ipv6, identifier, connectedDeviceId, connectedDeviceName,
        connectedDeviceIp, connectedInterfaceName, vlanId, clientMac, timestamp           Wireless Client: name,
        messageType, ipv4, ipv6, identifier, clientMac, apId, apName, apMac, wlcId, wlcName, frequency, ssid,
        username, dhcpServerIp, timestamp      order   The sort order of the field ascending or descending.
        Default value : desc.

        Args:
            device_family(str): deviceFamily query parameter. Device family. Please note that multiple families
                across network device type and client type is not allowed. For example, choosing
                `Routers` along with `Wireless Client` or `Unified AP` is not supported. Examples:
                `deviceFamily=Switches and Hubs` (single deviceFamily requested) `deviceFamily=Switches
                and Hubs&deviceFamily=Routers` (multiple deviceFamily requested) .
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to current time minus 24
                hours. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. If
                `endTime` is not provided, API will default to current time. .
            message_type(str): messageType query parameter. Message type for the event. Examples:
                `messageType=Syslog` (single messageType requested)
                `messageType=Trap&messageType=Syslog` (multiple messageType requested) .
            severity(int): severity query parameter. Severity of the event between 0 and 6. This is applicable only
                for events related to network devices (other than AP) and `Wired Client` events. (Value:
                Severity),  (0: Emergency),  (1: Alert),  (2: Critical),  (3: Error),  (4: Warning),
                (5: Notice),  (6: Info),  Examples: `severity=0` (single severity requested)
                `severity=0&severity=1` (multiple severity requested) .
            site_id(str): siteId query parameter. The UUID of the site. (Ex. `flooruuid`) Examples: `?siteId=id1`
                (single siteId requested) `?siteId=id1&siteId=id2&siteId=id3` (multiple siteId
                requested) .
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site tree
                in id form starting from Global site UUID and ending with the specific site UUID. (Ex.
                `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk
                (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyId requested) .
            network_device_name(str): networkDeviceName query parameter. Network device name. This parameter is
                applicable for network device related families. This field supports wildcard (`*`)
                character-based search. Ex: `*Branch*` or `Branch*` or `*Branch` Examples:
                `networkDeviceName=Branch-3-Gateway` (single networkDeviceName requested)
                `networkDeviceName=Branch-3-Gateway&networkDeviceName=Branch-3-Switch` (multiple
                networkDeviceName requested) .
            network_device_id(str): networkDeviceId query parameter. The list of Network Device Uuids. (Ex.
                `6bef213c-19ca-4170-8375-b694e251101c`) Examples:
                `networkDeviceId=6bef213c-19ca-4170-8375-b694e251101c` (single networkDeviceId
                requested) `networkDeviceId=6bef213c-19ca-4170-8375-
                b694e251101c&networkDeviceId=32219612-819e-4b5e-a96b-
                cf22aca13dd9&networkDeviceId=2541e9a7-b80d-4955-8aa2-79b233318ba0` (multiple
                networkDeviceId with & separator) .
            ap_mac(str): apMac query parameter. MAC address of the access point. This parameter is applicable for
                `Unified AP` and `Wireless Client` events. This field supports wildcard (`*`) character-
                based search. Ex: `*50:0F*` or `50:0F*` or `*50:0F` Examples: `apMac=50:0F:80:0F:F7:E0`
                (single apMac requested) `apMac=50:0F:80:0F:F7:E0&apMac=18:80:90:AB:7E:A0` (multiple
                apMac requested) .
            client_mac(str): clientMac query parameter. MAC address of the client. This parameter is applicable for
                `Wired Client` and `Wireless Client` events. This field supports wildcard (`*`)
                character-based search. Ex: `*66:2B*` or `66:2B*` or `*66:2B` Examples:
                `clientMac=66:2B:B8:D2:01:56` (single clientMac requested)
                `clientMac=66:2B:B8:D2:01:56&clientMac=DC:A6:32:F5:5A:89` (multiple clientMac requested)
                .
            attribute(str): attribute query parameter. The list of attributes that needs to be included in the
                response. If this parameter is not provided, then basic attributes (`id`, `name`,
                `timestamp`, `details`, `messageType`, `siteHierarchyId`, `siteHierarchy`,
                `deviceFamily`, `networkDeviceId`, `networkDeviceName`, `managementIpAddress`) would be
                part of the response.  Examples: `attribute=name` (single attribute requested)
                `attribute=name&attribute=networkDeviceName` (multiple attribute requested) .
            view(str): view query parameter. The list of events views. Please refer to `EventViews` for the
                supported list  Examples: `view=network` (single view requested) `view=network&view=ap`
                (multiple view requested) .
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1.
            limit(int): limit query parameter. Maximum number of records to return.
            sort_by(str): sortBy query parameter. A field within the response to sort by.
            order(str): order query parameter. The sort order of the field ascending or descending.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!query-assurance-events
        """
        check_type(headers, dict)
        check_type(device_family, str, may_be_none=False)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(message_type, str)
        check_type(severity, int)
        check_type(site_id, str)
        check_type(site_hierarchy_id, str)
        check_type(network_device_name, str)
        check_type(network_device_id, str)
        check_type(ap_mac, str)
        check_type(client_mac, str)
        check_type(attribute, str)
        check_type(view, str)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, str)
        check_type(order, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deviceFamily": device_family,
            "startTime": start_time,
            "endTime": end_time,
            "messageType": message_type,
            "severity": severity,
            "siteId": site_id,
            "siteHierarchyId": site_hierarchy_id,
            "networkDeviceName": network_device_name,
            "networkDeviceId": network_device_id,
            "apMac": ap_mac,
            "clientMac": client_mac,
            "attribute": attribute,
            "view": view,
            "offset": offset,
            "limit": limit,
            "sortBy": sort_by,
            "order": order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/assuranceEvents"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bc891de5102872b3415d23b7a0b_v3_2_3_0", json_data
        )

    def gets_the_summary_analytics_data_related_to_network_devices(
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
        """Gets the summary analytics data related to network devices based on the provided input data. This endpoint helps
        to obtain the consolidated insights into the performance and status of the monitored network devices.
        For detailed information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-AssuranceNetworkDevices-2.0.1-resolved.yaml.   The input
        payload contains the following fields,         Field Name   Description           startTime   The start
        time indicates the point from which the API retrieves the dataset associated with the resource. It must
        be specified in UNIX epochtime in milliseconds. Value is inclusive & the default is latest       endTime
        The end time signifies the limit until which the API retrieves the dataset associated with the resource.
        It must be specified in UNIX epochtime in milliseconds. Value is inclusive & the default is latest
        groupBy   The groupby defines the criteria for grouping the data based on specific attributes. The
        available group by fields correspond to the attributes listed. For a comprehensive list of supported
        attributes, please refer to the  NetworkDevicesAnalyticsGroupBy  model       attributes   The attribute
        is useful for obtaining one or more field data in addition to the aggregated data within the specified
        start and end time range. The supported attributes are listed in  NetworkDevicesAnalyticsAttributes
        model       aggregateAttributes   The aggregateAttributes denotes the attribute name(s) on which the
        aggregate functions is to be applied during data querying. The supported attribute names are listed in
        NetworkDevicesAnalyticsAggregateAttributes  model       filters   The filters used to  define one or
        more conditions and the data that meets these conditions will be considered during the aggregation
        calculation. The supported list of fiters defined in  NetworkDevicesAnalyticsFilters       page   The
        page includes  limit, offset , and  sortBy  fields. Limit indicates.

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's attributes (list of strings).
            endTime(integer): Devices's endTime.
            filters(list): Devices's filters (list of objects).
            groupBy(list): Devices's groupBy (list of strings).
            page(object): Devices's page.
            startTime(integer): Devices's startTime.
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
            https://developer.cisco.com/docs/dna-center/#!gets-the-summary-analytics-data-related-to-network-devices
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "startTime": startTime,
            "endTime": endTime,
            "groupBy": groupBy,
            "attributes": attributes,
            "filters": filters,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_bb7c52e5225e9398a006fecf4da06f_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/networkDevices/summaryAnalytics"
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
            "bpm_bb7c52e5225e9398a006fecf4da06f_v3_2_3_0", json_data
        )

    def get_device_list(
        self,
        associated_wlc_ip=None,
        collection_interval=None,
        collection_status=None,
        device_support_level=None,
        error_code=None,
        error_description=None,
        family=None,
        hostname=None,
        id=None,
        license_name=None,
        license_status=None,
        license_type=None,
        limit=None,
        location=None,
        location_name=None,
        mac_address=None,
        management_ip_address=None,
        module_equpimenttype=None,
        module_name=None,
        module_operationstatecode=None,
        module_partnumber=None,
        module_servicestate=None,
        module_vendorequipmenttype=None,
        not_synced_for_minutes=None,
        offset=None,
        platform_id=None,
        reachability_status=None,
        role=None,
        serial_number=None,
        series=None,
        software_type=None,
        software_version=None,
        type=None,
        up_time=None,
        headers=None,
        **request_parameters
    ):
        """Returns list of network devices based on filter criteria such as management IP address, mac address, hostname,
        etc. You can use the .* in any value to conduct a wildcard search. For example, to find all hostnames
        beginning with myhost in the IP address range 192.25.18.n, issue the following request: GET
        /dna/intent/api/v1/network-device?hostname=myhost.*&managementIpAddress=192.25.18..*  If id parameter is
        provided with comma separated ids, it will return the list of network-devices for the given ids and
        ignores the other request parameters. The API returns a paginated response based on 'limit' and 'offset'
        parameters, allowing up to 500 records per page. 'limit' specifies the number of records, and 'offset'
        sets the starting point using 1-based indexing. Use '/dna/intent/api/v1/network-device/count' to get the
        total record count. For data sets over 500 records, make multiple calls, adjusting 'limit' and 'offset'
        to retrieve all records incrementally.

        Args:
            hostname(list, set, str, tuple): hostname query parameter.
            management_ip_address(list, set, str, tuple): managementIpAddress query parameter.
            mac_address(list, set, str, tuple): macAddress query parameter.
            location_name(list, set, str, tuple): locationName query parameter.
            serial_number(list, set, str, tuple): serialNumber query parameter.
            location(list, set, str, tuple): location query parameter.
            family(list, set, str, tuple): family query parameter.
            type(list, set, str, tuple): type query parameter.
            series(list, set, str, tuple): series query parameter.
            collection_status(list, set, str, tuple): collectionStatus query parameter.
            collection_interval(list, set, str, tuple): collectionInterval query parameter.
            not_synced_for_minutes(list, set, str, tuple): notSyncedForMinutes query parameter.
            error_code(list, set, str, tuple): errorCode query parameter.
            error_description(list, set, str, tuple): errorDescription query parameter.
            software_version(list, set, str, tuple): softwareVersion query parameter.
            software_type(list, set, str, tuple): softwareType query parameter.
            platform_id(list, set, str, tuple): platformId query parameter.
            role(list, set, str, tuple): role query parameter.
            reachability_status(list, set, str, tuple): reachabilityStatus query parameter.
            up_time(list, set, str, tuple): upTime query parameter.
            associated_wlc_ip(list, set, str, tuple): associatedWlcIp query parameter.
            license_name(list, set, str, tuple): license.name query parameter.
            license_type(list, set, str, tuple): license.type query parameter.
            license_status(list, set, str, tuple): license.status query parameter.
            module_name(list, set, str, tuple): module+name query parameter.
            module_equpimenttype(list, set, str, tuple): module+equpimenttype query parameter.
            module_servicestate(list, set, str, tuple): module+servicestate query parameter.
            module_vendorequipmenttype(list, set, str, tuple): module+vendorequipmenttype query parameter.
            module_partnumber(list, set, str, tuple): module+partnumber query parameter.
            module_operationstatecode(list, set, str, tuple): module+operationstatecode query parameter.
            id(str): id query parameter. Accepts comma separated ids and return list of network-devices for the
                given ids. If invalid or not-found ids are provided, null entry will be returned in the
                list.
            device_support_level(str): deviceSupportLevel query parameter.
            offset(int): offset query parameter. offset >= 1 [X gives results from Xth device onwards].
            limit(int): limit query parameter. The number of records to show for this page. Min: 1, Max: 500.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-device-list
        """
        check_type(headers, dict)
        check_type(hostname, (list, set, str, tuple))
        check_type(management_ip_address, (list, set, str, tuple))
        check_type(mac_address, (list, set, str, tuple))
        check_type(location_name, (list, set, str, tuple))
        check_type(serial_number, (list, set, str, tuple))
        check_type(location, (list, set, str, tuple))
        check_type(family, (list, set, str, tuple))
        check_type(type, (list, set, str, tuple))
        check_type(series, (list, set, str, tuple))
        check_type(collection_status, (list, set, str, tuple))
        check_type(collection_interval, (list, set, str, tuple))
        check_type(not_synced_for_minutes, (list, set, str, tuple))
        check_type(error_code, (list, set, str, tuple))
        check_type(error_description, (list, set, str, tuple))
        check_type(software_version, (list, set, str, tuple))
        check_type(software_type, (list, set, str, tuple))
        check_type(platform_id, (list, set, str, tuple))
        check_type(role, (list, set, str, tuple))
        check_type(reachability_status, (list, set, str, tuple))
        check_type(up_time, (list, set, str, tuple))
        check_type(associated_wlc_ip, (list, set, str, tuple))
        check_type(license_name, (list, set, str, tuple))
        check_type(license_type, (list, set, str, tuple))
        check_type(license_status, (list, set, str, tuple))
        check_type(module_name, (list, set, str, tuple))
        check_type(module_equpimenttype, (list, set, str, tuple))
        check_type(module_servicestate, (list, set, str, tuple))
        check_type(module_vendorequipmenttype, (list, set, str, tuple))
        check_type(module_partnumber, (list, set, str, tuple))
        check_type(module_operationstatecode, (list, set, str, tuple))
        check_type(id, str)
        check_type(device_support_level, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "hostname": hostname,
            "managementIpAddress": management_ip_address,
            "macAddress": mac_address,
            "locationName": location_name,
            "serialNumber": serial_number,
            "location": location,
            "family": family,
            "type": type,
            "series": series,
            "collectionStatus": collection_status,
            "collectionInterval": collection_interval,
            "notSyncedForMinutes": not_synced_for_minutes,
            "errorCode": error_code,
            "errorDescription": error_description,
            "softwareVersion": software_version,
            "softwareType": software_type,
            "platformId": platform_id,
            "role": role,
            "reachabilityStatus": reachability_status,
            "upTime": up_time,
            "associatedWlcIp": associated_wlc_ip,
            "license.name": license_name,
            "license.type": license_type,
            "license.status": license_status,
            "module+name": module_name,
            "module+equpimenttype": module_equpimenttype,
            "module+servicestate": module_servicestate,
            "module+vendorequipmenttype": module_vendorequipmenttype,
            "module+partnumber": module_partnumber,
            "module+operationstatecode": module_operationstatecode,
            "id": id,
            "deviceSupportLevel": device_support_level,
            "offset": offset,
            "limit": limit,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fe602e8165035b5cbc304fada4ee2f26_v3_2_3_0", json_data
        )

    def add_device(
        self,
        cliTransport=None,
        computeDevice=None,
        enablePassword=None,
        extendedDiscoveryInfo=None,
        httpPassword=None,
        httpPort=None,
        httpSecure=None,
        httpUserName=None,
        ipAddress=None,
        merakiOrgId=None,
        netconfPort=None,
        password=None,
        serialNumber=None,
        snmpAuthPassphrase=None,
        snmpAuthProtocol=None,
        snmpMode=None,
        snmpPrivPassphrase=None,
        snmpPrivProtocol=None,
        snmpROCommunity=None,
        snmpRWCommunity=None,
        snmpRetry=None,
        snmpTimeout=None,
        snmpUserName=None,
        snmpVersion=None,
        type=None,
        userName=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Adds the device with given credential.

        Args:
            cliTransport(string): Devices's CLI transport. Supported values: telnet, ssh. Required if type is
                NETWORK_DEVICE.
            computeDevice(boolean): Devices's Compute Device or not. Options are true / false.
            enablePassword(string): Devices's CLI enable password of the device. Required if device is configured to
                use enable password.
            extendedDiscoveryInfo(string): Devices's This field holds that info as whether to add device with canned
                data or not. Supported values: DISCOVER_WITH_CANNED_DATA.
            httpPassword(string): Devices's HTTP password of the device / API key for Meraki Dashboard. Required if
                type is MERAKI_DASHBOARD or COMPUTE_DEVICE.
            httpPort(string): Devices's HTTP port of the device. Required if type is COMPUTE_DEVICE.
            httpSecure(boolean): Devices's Flag to select HTTP / HTTPS protocol. Options are true / false. true for
                HTTPS and false for HTTP. Default is true.
            httpUserName(string): Devices's HTTP Username of the device. Required if type is COMPUTE_DEVICE.
            ipAddress(list): Devices's IP Address of the device. Required if type is NETWORK_DEVICE, COMPUTE_DEVICE
                or THIRD_PARTY_DEVICE. (list of strings).
            merakiOrgId(list): Devices's Selected Meraki organization for which the devices needs to be imported.
                Required if type is MERAKI_DASHBOARD. (list of strings).
            netconfPort(string): Devices's Netconf Port of the device. cliTransport must be 'ssh' if netconf is
                provided. Netconf port is required for eWLC.
            password(string): Devices's CLI Password of the device. Required if type is NETWORK_DEVICE.
            serialNumber(string): Devices's Serial Number of the Device. Required if extendedDiscoveryInfo is
                'DISCOVER_WITH_CANNED_DATA'.
            snmpAuthPassphrase(string): Devices's SNMPv3 auth passphrase of the device. Required if snmpMode is
                authNoPriv or authPriv.
            snmpAuthProtocol(string): Devices's SNMPv3 auth protocol. Supported values: sha, md5. Required if
                snmpMode is authNoPriv or authPriv.
            snmpMode(string): Devices's SNMPv3 mode. Supported values: noAuthnoPriv, authNoPriv, authPriv. Required
                if snmpVersion is v3.
            snmpPrivPassphrase(string): Devices's SNMPv3 priv passphrase. Required if snmpMode is authPriv.
            snmpPrivProtocol(string): Devices's SNMPv3 priv protocol. Supported values: AES128. Required if snmpMode
                is authPriv.
            snmpROCommunity(string): Devices's SNMP Read Community of the device. If snmpVersion is v2, at least one
                of snmpROCommunity and snmpRWCommunity is required.
            snmpRWCommunity(string): Devices's SNMP Write Community of the device. If snmpVersion is v2, at least
                one of snmpROCommunity and snmpRWCommunity is required.
            snmpRetry(integer): Devices's SNMP retry count. Max value supported is 3. Default is Global SNMP retry
                (if exists) or 3.
            snmpTimeout(integer): Devices's SNMP timeout in seconds. Max value supported is 300. Default is Global
                SNMP timeout (if exists) or 5.
            snmpUserName(string): Devices's SNMPV3 user name of the device. Required if snmpVersion is v3.
            snmpVersion(string): Devices's SNMP version. Values supported: v2, v3. Required if type is
                NETWORK_DEVICE, COMPUTE_DEVICE or THIRD_PARTY_DEVICE.
            type(string): Devices's Type of device being added. Default is NETWORK_DEVICE.. Available values are
                'COMPUTE_DEVICE', 'MERAKI_DASHBOARD', 'THIRD_PARTY_DEVICE' and 'NETWORK_DEVICE'.
            userName(string): Devices's CLI user name of the device. Required if type is NETWORK_DEVICE.
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
            https://developer.cisco.com/docs/dna-center/#!add-device
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "cliTransport": cliTransport,
            "computeDevice": computeDevice,
            "enablePassword": enablePassword,
            "extendedDiscoveryInfo": extendedDiscoveryInfo,
            "httpPassword": httpPassword,
            "httpPort": httpPort,
            "httpSecure": httpSecure,
            "httpUserName": httpUserName,
            "ipAddress": ipAddress,
            "merakiOrgId": merakiOrgId,
            "netconfPort": netconfPort,
            "password": password,
            "serialNumber": serialNumber,
            "snmpAuthPassphrase": snmpAuthPassphrase,
            "snmpAuthProtocol": snmpAuthProtocol,
            "snmpMode": snmpMode,
            "snmpPrivPassphrase": snmpPrivPassphrase,
            "snmpPrivProtocol": snmpPrivProtocol,
            "snmpROCommunity": snmpROCommunity,
            "snmpRWCommunity": snmpRWCommunity,
            "snmpRetry": snmpRetry,
            "snmpTimeout": snmpTimeout,
            "snmpUserName": snmpUserName,
            "snmpVersion": snmpVersion,
            "type": type,
            "userName": userName,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_fe3ec7651e79d891fce37a0d860_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device"
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
            "bpm_fe3ec7651e79d891fce37a0d860_v3_2_3_0", json_data
        )

    def sync_devices(
        self,
        cliTransport=None,
        computeDevice=None,
        enablePassword=None,
        extendedDiscoveryInfo=None,
        httpPassword=None,
        httpPort=None,
        httpSecure=None,
        httpUserName=None,
        ipAddress=None,
        merakiOrgId=None,
        netconfPort=None,
        password=None,
        serialNumber=None,
        snmpAuthPassphrase=None,
        snmpAuthProtocol=None,
        snmpMode=None,
        snmpPrivPassphrase=None,
        snmpPrivProtocol=None,
        snmpROCommunity=None,
        snmpRWCommunity=None,
        snmpRetry=None,
        snmpTimeout=None,
        snmpUserName=None,
        snmpVersion=None,
        type=None,
        updateMgmtIPaddressList=None,
        userName=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Update the credentials, management IP address of a given device (or a set of devices) in Catalyst Center and
        trigger an inventory sync.

        Args:
            cliTransport(string): Devices's CLI transport. Supported values: telnet, ssh. Use NO!$DATA!$ if no
                change is required. Required if type is NETWORK_DEVICE.
            computeDevice(boolean): Devices's Compute Device or not. Options are true / false.
            enablePassword(string): Devices's CLI enable password of the device. Required if device is configured to
                use enable password. Use NO!$DATA!$ if no change is required.
            extendedDiscoveryInfo(string): Devices's This field holds that info as whether to add device with canned
                data or not. Supported values: DISCOVER_WITH_CANNED_DATA.
            httpPassword(string): Devices's HTTP password of the device / API key for Meraki Dashboard. Required if
                type is MERAKI_DASHBOARD or COMPUTE_DEVICE. Use NO!$DATA!$ if no change is required.
            httpPort(string): Devices's HTTP port of the device. Required if type is COMPUTE_DEVICE.
            httpSecure(boolean): Devices's Flag to select HTTP / HTTPS protocol. Options are true / false. true for
                HTTPS and false for HTTP.
            httpUserName(string): Devices's HTTP Username of the device. Required if type is COMPUTE_DEVICE. Use
                NO!$DATA!$ if no change is required.
            ipAddress(list): Devices's IP Address of the device. Required. Use 'api.meraki.com' for Meraki
                Dashboard. (list of strings).
            merakiOrgId(list): Devices's Selected Meraki organization for which the devices needs to be imported.
                Required if type is MERAKI_DASHBOARD. (list of strings).
            netconfPort(string): Devices's Netconf Port of the device. cliTransport must be 'ssh' if netconf is
                provided. Netconf port is required for eWLC.
            password(string): Devices's CLI Password of the device. Required if type is NETWORK_DEVICE. Use
                NO!$DATA!$ if no change is required.
            serialNumber(string): Devices's Serial Number of the Device. Required if extendedDiscoveryInfo is
                'DISCOVER_WITH_CANNED_DATA'.
            snmpAuthPassphrase(string): Devices's SNMPv3 auth passphrase of the device. Required if snmpMode is
                authNoPriv or authPriv. Use NO!$DATA!$ if no change is required.
            snmpAuthProtocol(string): Devices's SNMPv3 auth protocol. Supported values: sha, md5.  Required if
                snmpMode is authNoPriv or authPriv. Use NODATACHANGE if no change is required.
            snmpMode(string): Devices's SNMPv3 mode. Supported values: noAuthnoPriv, authNoPriv, authPriv. Required
                if snmpVersion is v3. Use NODATACHANGE if no change is required.
            snmpPrivPassphrase(string): Devices's SNMPv3 priv passphrase. Required if snmpMode is authPriv. Use
                NO!$DATA!$ if no change is required.
            snmpPrivProtocol(string): Devices's SNMPv3 priv protocol. Supported values: AES128. Required if snmpMode
                is authPriv. Use NODATACHANGE if no change is required.
            snmpROCommunity(string): Devices's SNMP Read Community of the device. If snmpVersion is v2, at least one
                of snmpROCommunity and snmpRWCommunity is required. Use NO!$DATA!$ if no change is
                required.
            snmpRWCommunity(string): Devices's SNMP Write Community of the device. If snmpVersion is v2, at least
                one of snmpROCommunity and snmpRWCommunity is required. Use NO!$DATA!$ if no change is
                required.
            snmpRetry(integer): Devices's SNMP retry count. Max value supported is 3. Default is Global SNMP retry
                (if exists) or 3.
            snmpTimeout(integer): Devices's SNMP timeout in seconds. Max value supported is 300. Default is Global
                SNMP timeout (if exists) or 5.
            snmpUserName(string): Devices's SNMPV3 user name of the device. Required if snmpVersion is v3. Use
                NO!$DATA!$ if no change is required.
            snmpVersion(string): Devices's SNMP version. Values supported: v2, v3. Required if type is
                NETWORK_DEVICE, COMPUTE_DEVICE or THIRD_PARTY_DEVICE. Use NODATACHANGE if no change is
                required.
            type(string): Devices's Type of device being edited. Default is NETWORK_DEVICE.. Available values are
                'COMPUTE_DEVICE', 'MERAKI_DASHBOARD', 'NETWORK_DEVICE', 'THIRD_PARTY_DEVICE' and
                'NODATACHANGE'.
            updateMgmtIPaddressList(list): Devices's IPAddress of the device to be mapped to New IPAddress. (list of
                objects).
            userName(string): Devices's CLI user name of the device. Required if type is NETWORK_DEVICE. Use
                NO!$DATA!$ if no change is required.
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
            https://developer.cisco.com/docs/dna-center/#!update-device-details
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "cliTransport": cliTransport,
            "computeDevice": computeDevice,
            "enablePassword": enablePassword,
            "extendedDiscoveryInfo": extendedDiscoveryInfo,
            "httpPassword": httpPassword,
            "httpPort": httpPort,
            "httpSecure": httpSecure,
            "httpUserName": httpUserName,
            "ipAddress": ipAddress,
            "merakiOrgId": merakiOrgId,
            "netconfPort": netconfPort,
            "password": password,
            "serialNumber": serialNumber,
            "snmpAuthPassphrase": snmpAuthPassphrase,
            "snmpAuthProtocol": snmpAuthProtocol,
            "snmpMode": snmpMode,
            "snmpPrivPassphrase": snmpPrivPassphrase,
            "snmpPrivProtocol": snmpPrivProtocol,
            "snmpROCommunity": snmpROCommunity,
            "snmpRWCommunity": snmpRWCommunity,
            "snmpRetry": snmpRetry,
            "snmpTimeout": snmpTimeout,
            "snmpUserName": snmpUserName,
            "snmpVersion": snmpVersion,
            "type": type,
            "updateMgmtIPaddressList": updateMgmtIPaddressList,
            "userName": userName,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_fe06867e548bba1919024b40d992_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_fe06867e548bba1919024b40d992_v3_2_3_0", json_data
        )

    def create_maintenance_schedule_for_network_devices(
        self,
        description=None,
        id=None,
        maintenanceSchedule=None,
        networkDeviceIds=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """API to create maintenance schedule for network devices. The state of network device can be queried using API
        `GET /dna/intent/api/v1/networkDevices`. The `managementState` attribute of the network device will be
        updated to `UNDER_MAINTENANCE` when the maintenance window starts.

        Args:
            description(string): Devices's A brief narrative describing the maintenance schedule.
            id(string): Devices's Id of the schedule maintenance window.
            maintenanceSchedule(object): Devices's Contains all the details necessary to define the maintenance
                window and its recurrence.
            networkDeviceIds(list): Devices's networkDeviceIds (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!create-maintenance-schedule-for-network-devices
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "id": id,
            "description": description,
            "maintenanceSchedule": maintenanceSchedule,
            "networkDeviceIds": networkDeviceIds,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_c1dae5c13e6959348fe1fe0652958647_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDeviceMaintenanceSchedules"
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
            "bpm_c1dae5c13e6959348fe1fe0652958647_v3_2_3_0", json_data
        )

    def retrieve_scheduled_maintenance_windows_for_network_devices(
        self,
        limit=None,
        network_device_ids=None,
        offset=None,
        order=None,
        sort_by=None,
        status=None,
        headers=None,
        **request_parameters
    ):
        """This API retrieves a list of scheduled maintenance windows for network devices based on filter parameters. Each
        maintenance window is composed of a start schedule and end schedule, both of which have unique
        identifiers(`startId` and `endId`). These identifiers can be used to fetch the status of the start
        schedule and end schedule using the `GET /dna/intent/api/v1/activities/{id}` API. Completed maintenance
        schedules are automatically removed from the system after two weeks.

        Args:
            network_device_ids(list, set, str, tuple): networkDeviceIds query parameter. List of network device ids.
            status(str): status query parameter. The status of the maintenance schedule. Possible values are:
                `UPCOMING`: The maintenance is scheduled and pending execution.  `IN_PROGRESS`: The
                maintenance is currently in progress.   `COMPLETED`: The maintenance window has been
                fully completed (For recurring maintenance, this indicates completion of the most recent
                occurrence).  `FAILED`: Updating the device's management state was not successful. For
                more information on failure use `GET /dna/intent/api/v1/activities/{id}` API with
                `startId` and `endId` value. .
            limit(int): limit query parameter. The number of records to show for this page.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1.
            sort_by(str): sortBy query parameter. A property within the response to sort by.
            order(str): order query parameter. Whether ascending or descending order should be used to sort the
                response.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-scheduled-maintenance-windows-for-network-devices
        """
        check_type(headers, dict)
        check_type(network_device_ids, (list, set, str, tuple))
        check_type(status, str)
        check_type(limit, int)
        check_type(offset, int)
        check_type(sort_by, str)
        check_type(order, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "networkDeviceIds": network_device_ids,
            "status": status,
            "limit": limit,
            "offset": offset,
            "sortBy": sort_by,
            "order": order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDeviceMaintenanceSchedules"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a90a937a8af85fbfa73d607be7ebafc2_v3_2_3_0", json_data
        )

    def get_summary_analytics_data_of_aaa_services_for_given_set_of_complex_filters(
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
        """Gets the summary analytics data related to AAA Services based on given filters and group by field. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-AAAServices-1.0.0-resolved.yaml.   Gets the summary
        analytics data related to AAA Services based on given filters and group by field. If startTime and
        endTime are not provided, the API defaults to the last 24 hours. Field Name Description startTime start
        time from which API queries the data set related to the resource. It must be specified in UNIX epochtime
        in milliseconds. Value is inclusive & the default is 24 hours ago from end time endTime end time to
        which API queries the data set related to the resource. It must be specified in UNIX epochtime in
        milliseconds. Value is inclusive & the default is current time groupBy specifies the attributes for
        grouping the data. filters used to define one or more conditions. Only the data that satisfy these
        conditions will be taken into consideration during the aggregation calculation. attributes attributes
        are used for obtaining one or more field's data in addition to the aggregated data. The supported
        attributes are listed in  AAAServicesAnalyticsAttributeKey  model aggregateAttributes specifies the
        names of the attributes on which the aggregate function should be applied when querying the data. The
        supported attribute names are listed in  AAAServicesAggregateAttributeKey  model page contains  limit,
        offset and sortBy  fields.  limit  Number of records to be returned in response,  offset  starting
        offset of data and  sortBy  attribute name, order to sort.

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's attributes (list of strings).
            endTime(integer): Devices's endTime.
            filters(list): Devices's filters (list of objects).
            groupBy(list): Devices's groupBy (list of strings).
            page(object): Devices's page.
            startTime(integer): Devices's startTime.
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
            https://developer.cisco.com/docs/dna-center/#!get-summary-analytics-data-of-a-a-a-services-for-given-set-of-complex-filters
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
            "groupBy": groupBy,
            "filters": filters,
            "attributes": attributes,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d54c40ecb5f531cb5a78d0cd5dd585e_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/aaaServices/summaryAnalytics"
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
            "bpm_d54c40ecb5f531cb5a78d0cd5dd585e_v3_2_3_0", json_data
        )

    def get_device_interface_vlans(
        self, id, interface_type=None, headers=None, **request_parameters
    ):
        """Returns Device Interface VLANs. If parameter value is null or empty, it won't return any value in response.

        Args:
            id(str): id path parameter.
            interface_type(str): interfaceType query parameter. Vlan associated with sub-interface. If no
                interfaceType mentioned it will return all types of Vlan interfaces. If interfaceType is
                selected but not specified then it will take default value.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-device-interface-v-l-a-ns
        """
        check_type(headers, dict)
        check_type(interface_type, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "interfaceType": interface_type,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/{id}/vlan"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fd5fb603cba6523abb25c8ec131fbb8b_v3_2_3_0", json_data
        )

    def get_details_of_a_single_network_device(
        self, id, views=None, headers=None, **request_parameters
    ):
        """API to fetch the details of network device using the `id`. Use the `/dna/intent/api/v1/networkDevices/query` API
        for advanced filtering. The API supports views  to fetch only the required fields.  This API supports
        `CREDENTIALS` view to return the non-sensitive credentials of the network device.  **How views work**
        The `views` parameter is an optional field to specify which attributes to retrieve. If this is not
        provided, then it will default to `BASIC` views. If multiple views are provided, the response will
        contain the union of the views.  Attributes covered by the views are:  * `BASIC`: id, managementAddress,
        dnsResolvedManagementIpAddress, hostname, macAddress, serialNumbers, type, family, series, status,
        platformIds, softwareType, softwareVersion, vendor, stackDevice, bootTime, role, roleSource,
        apEthernetMacAddress, apManagerInterfaceIpAddress, apWlcIpAddress, deviceSupportLevel, snmpContact,
        snmpLocation, secureMode * `RESYNC`: id, managementAddress, dnsResolvedManagementIpAddress, hostname,
        macAddress, serialNumbers, type, family, series, status, reachabilityStatus, reachabilityFailureReason,
        managementState, lastSuccessfulResyncReasons, resyncStartTime, resyncEndTime, resyncReasons,
        resyncRequestedByApps, pendingResyncRequestCount, pendingResyncRequestReasons, resyncIntervalSource,
        resyncIntervalMinutes, errorCode, errorDescription, secureMode * `USER_DEFINED_FIELDS`: id,
        managementAddress, dnsResolvedManagementIpAddress, hostname, macAddress, serialNumbers, type, family,
        series, status, userDefinedFields * `CREDENTIALS` (without sensitive fields): id, managementAddress,
        dnsResolvedManagementIpAddress, hostname, macAddress, serialNumbers, type, family, series, status,
        credentials, category  Note: `CREDENTIALS` view only returns the non-sensitive credentials of the
        network device. The sensitive credentials are not returned in the response.

        Args:
            id(str): id path parameter. Unique identifier for the network device.
            views(list, set, str, tuple): views query parameter. The specific views being requested. This is an
                optional parameter which can be passed to get one or more of the network  device data.
                If this is not provided, then it will default to `BASIC` views. If multiple views are
                provided, the response  will contain the union of the views. Attributes covered by the
                views are: * `BASIC`: id, managementAddress, dnsResolvedManagementIpAddress, hostname,
                macAddress, serialNumbers, type, family, series, status, platformIds, softwareType,
                softwareVersion, vendor, stackDevice, bootTime, role, roleSource, apEthernetMacAddress,
                apManagerInterfaceIpAddress, apWlcIpAddress, deviceSupportLevel, snmpContact,
                snmpLocation, secureMode * `RESYNC`: id, managementAddress,
                dnsResolvedManagementIpAddress, hostname, macAddress, serialNumbers, type, family,
                series, status, reachabilityStatus, reachabilityFailureReason, managementState,
                lastSuccessfulResyncReasons, resyncStartTime, resyncEndTime, resyncReasons,
                resyncRequestedByApps, pendingResyncRequestCount, pendingResyncRequestReasons,
                resyncIntervalSource, resyncIntervalMinutes, errorCode, errorDescription, secureMode *
                `USER_DEFINED_FIELDS`: id, managementAddress, dnsResolvedManagementIpAddress, hostname,
                macAddress, serialNumbers, type, family, series, status, userDefinedFields *
                `CREDENTIALS` (without sensitive credentials): id, managementAddress,
                dnsResolvedManagementIpAddress, hostname, macAddress, serialNumbers, type, family,
                series, status, credentials, category Note: `CREDENTIALS` view only returns the non-
                sensitive credentials of the network device. The sensitive credentials are not returned
                in the response. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-details-of-a-single-network-device
        """
        check_type(headers, dict)
        check_type(views, (list, set, str, tuple))
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "views": views,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDevices/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fc15032bbf55ec0bbdd3964c9f00089_v3_2_3_0", json_data
        )

    def updates_the_network_device(
        self,
        id,
        category=None,
        credentials=None,
        managementAddress=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Updates the network device with the given identifier. The API supports Network Device, Meraki Dashboard, Compute
        Device, Firewall Management Center (FMC) and Third-Party Device. Access  points associated with added
        WLC will be automatically added to inventory. For Meraki Dashboard, use the dashboard URL as the
        management address.  If a different `managementIpAddress` is provided, the device will be updated with
        the new `managementIpAddress`.  This API does not support partial updates. If you want to perform a
        partial update, use the POST `/dna/intent/api/v1/networkDevices/{id}/update` API.

        Args:
            category(string): Devices's Category of the device. Used to determine the type of the device being
                added. | Category                                    | Description
                | Required Credentials | Optional Credentials | |
                ------------------------------------------|
                --------------------------------------------------------------------------------------|
                -------------------| -------------------| | `NETWORK_DEVICE`
                | Standard Cisco network devices like switches, routers, controllers
                | CLI, SNMP            | HTTP, NETCONF        | | `COMPUTE_DEVICE`
                | Server or computing system manufactured by Cisco such as Unified Computing System
                (UCS) | HTTP                 | CLI, SNMP            | | `THIRD_PARTY_DEVICE`
                | Non-Cisco network devices that support SNMP monitoring
                | SNMP                 |                    | | `MERAKI_DASHBOARD`
                | Cisco Meraki cloud-managed devices accessed via Meraki Dashboard
                | Meraki               |                    | | `FIREWALL_MANAGEMENT_CENTER`
                | Cisco Secure Firewall Management Center (FMC)
                | HTTP                 |                    | . Available values are
                'FIREWALL_MANAGEMENT_CENTER'.
            credentials(object): Devices's Credentials used to access the network device. .
            managementAddress(): Devices's Management address of the network device. For meraki dashboard, this is
                the dashboard URL.
            id(str): id path parameter. Unique identifier of the device.
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
            https://developer.cisco.com/docs/dna-center/#!updates-the-network-device
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "category": category,
            "managementAddress": managementAddress,
            "credentials": credentials,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_b0780003f8f05720a7b04cfa0d0a9a85_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDevices/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_b0780003f8f05720a7b04cfa0d0a9a85_v3_2_3_0", json_data
        )

    def retrieves_specific_stats_for_a_wlc_over_a_specified_period_of_time(
        self,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        page=None,
        startTime=None,
        trendInterval=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Retrieves the time series stats of a specific WLC by applying complex filters, aggregate functions, and
        grouping. The data will be grouped based on the specified trend time interval. If startTime and endTime
        are not provided, the API defaults to the last 24 hours.  **The input payload contains the following
        fields,** |Field Name | Description | | --| --| | `startTime` | The start time indicates when the API
        begins retrieving data related to the resource. It must be specified in the UNIX epoch time format,
        measured in milliseconds. This value is inclusive, and if left unspecified, the default is 1 day before
        the endTime. | | `endTime` | The end time indicates the upper limit until which the API retrieves data
        related to the resource. It must be defined in the UNIX epoch time format, measured in milliseconds.
        This value is inclusive, and if left unspecified, the default is the latest available data. | |
        `trendInterval` |  The time window for aggregating metrics. This is a mandatory request field. Possible
        values include *5 minutes, 10 minutes, 1 hour, 1 day, or 7 days*. If the start and end time range
        exceeds 1 day, the trendInterval defaults to 1 hour.| | `groupBy` | Specifies the attributes for
        grouping the data. Refer to `WlcStatsGroupByField` model for the supported grouping attributes| |
        `attributes` | A list of attributes associated with the resource, which can be requested to be included
        in the response alongside the required attributes. Refer to `WlcStatsAttribute` model for the supported
        attributes | | `aggregateAttributes` | This specifies the attribute name and the function to be applied
        during data querying. The aggregate function is then applied to data within the specified start and end
        times. Refer to `WlcStatsAggregateField` model for the supported aggregate attributes | |`filters`| This
        is used to specify one or more conditions for filtering the queried data. Refer to `WlcStatsFilterField`
        model for the supported filters | |`page`| It includes the **limit, cursor, and timeSortOrder** fields.
        *limit* denotes the number of records to retrieve per page, *cursor* signifies the initial data
        position, and *timeSortOrder* is used sort the response based on the timestamp either in ascending or
        descending order. |.

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's attributes (list of strings. Available values are 'id', 'name',
                'siteHierarchy', 'siteHierarchyId', 'lastUpdatedTime', '24ghzClients', '5ghzClients',
                '6ghzClients', 'totalClientCount', 'assocAttempts', 'assocFailures', 'assocRespAccepts',
                'assocRespRejects', 'assocRespErrors', 'startAttempts', 'associationAttempts',
                'localAuthAttempts', 'l2AuthAttempts', 'l2AuthFailures', 'mabAttempts', 'mabFailures',
                'ipLearnAttempts', 'ipLearnFailures', 'l3AuthAttempts', 'l3AuthFailures',
                'sessionPushAttempts', 'sessionPushFailures', 'runAttempts', 'deletedAttempts', 'roams',
                'cckmRoams', 'dot11rRoams', 'dot11iFastRoams', 'dot11iSlowRoams', 'failedRoams',
                'mdnsTxPackets', 'mdnsRxPackets', 'mdnsDropPackets', 'l2Roams', 'l3Roams',
                'interWncdRoams', 'hwDropsCapwapControl', 'hwDropsCapwapData', 'hwDropsmobilityControl',
                'hwDropsmobilityData', 'hwDropsIpGlean', 'hwDropsIpSg', 'hwDropsIpLearn',
                'hwDropsL2Bridging', 'hwDropsClientUidb', 'hwDropsClientNotFound', 'hwDropsP2PBlock',
                'swDropsCapwapControl', 'swDropsCapwapData', 'swDropsmobilityControl',
                'swDropsmobilityData', 'swDropsIpGlean', 'swDropsIpSg', 'swDropsIpLearn',
                'swDropsL2Bridging', 'swDropsClientUidb', 'swDropsClientNotFound', 'swDropsP2PBlock',
                'puntCapwapControl', 'puntCapwapData', 'puntmobilityControl', 'puntmobilityData',
                'puntDot11IAPP', 'puntDot11RRM', 'puntDot11Dot1x', 'puntWebAuth',
                'puntDot11ProbeRequest', 'puntDot11Rfid', 'puntDot11Mgmt', 'puntCapwapKeepAlive',
                'puntMobilityKeepAlive', 'puntArp', 'puntDhcp', 'puntDhcp6', 'puntIpv6Nd',
                'puntDataGlean', 'puntDataGlean6', 'puntDhcpRelay', 'txBytes', 'rxBytes', 'txPackets',
                'rxPackets', 'txErrorPackets', 'rxErrorPackets', 'txErrorPercentage' and
                'rxErrorPercentage').
            endTime(integer): Devices's End time to which the API queries the dataset related to the resource. It
                must be specified in terms of milliseconds since UNIX epoch. Value is inclusive.
            filters(list): Devices's filters (list of objects).
            groupBy(list): Devices's groupBy (list of strings. Available values are 'id').
            page(object): Devices's page.
            startTime(integer): Devices's Start time from which the API queries the dataset related to the resource.
                It must be specified in terms of milliseconds since UNIX epoch. Value is inclusive.
            trendInterval(string): Devices's The time window to aggregate the metrics.  Interval can be 5 minutes or
                10 minutes or 1 hour or 1 day or 7 days . Available values are '5MIN', '10MIN', '1HR',
                '1DAY' and '7DAY'.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-specific-stats-for-a-w-l-c-over-a-specified-period-of-time
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
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
            "trendInterval": trendInterval,
            "groupBy": groupBy,
            "attributes": attributes,
            "filters": filters,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a1ad35e390057d2bb116bf2d4ebc85e_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/wirelessControllersStats/trendAnalytics"
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
            "bpm_a1ad35e390057d2bb116bf2d4ebc85e_v3_2_3_0", json_data
        )

    def get_wired_capture_configuration_status(
        self, preview_activity_id, headers=None, **request_parameters
    ):
        """Get wired capture configuration intent status per network device by the previewActivityId.

        Args:
            preview_activity_id(str): previewActivityId path parameter. activity from the POST
                /deviceConfigugrationModels task response.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-wired-capture-configuration-status
        """
        check_type(headers, dict)
        check_type(preview_activity_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "previewActivityId": preview_activity_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/capture/wired/configurationModels/{pr"
            + "eviewActivityId}/networkDeviceStatusDetails"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bf30c3daee865421bfcce834e0f87872_v3_2_3_0", json_data
        )

    def get_device_interfaces_by_specified_range(
        self,
        device_id,
        records_to_return,
        start_index,
        headers=None,
        **request_parameters
    ):
        """Returns the list of interfaces for the device for the specified range.

        Args:
            device_id(str): deviceId path parameter. Device ID.
            start_index(int): startIndex path parameter. Start index.
            records_to_return(int): recordsToReturn path parameter. Number of records to return.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-device-interfaces-by-specified-range
        """
        check_type(headers, dict)
        check_type(device_id, str, may_be_none=False)
        check_type(start_index, int, may_be_none=False)
        check_type(records_to_return, int, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceId": device_id,
            "startIndex": start_index,
            "recordsToReturn": records_to_return,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/interface/network-"
            + "device/{deviceId}/{startIndex}/{recordsToReturn}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a3d52c630ba5deaada16fe3b07af744_v3_2_3_0", json_data
        )

    def update_planned_access_point_for_floor(
        self,
        floor_id,
        attributes=None,
        isSensor=None,
        location=None,
        position=None,
        radioCount=None,
        radios=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Allows updating a planned access point on an existing floor map including its planned radio and antenna details.
        Use the Get variant of this API to fetch the existing planned access points for the floor.  The payload
        to update a planned access point is in the same format, albeit a single object instead of a list, of
        that API.  API to update an existing planned access point within a floor map.

        Args:
            attributes(object): Devices's Attributes of the planned access point.
            isSensor(boolean): Devices's Indicates that PAP is a sensor.
            location(object): Devices's Location of the planned access point.
            position(object): Devices's Position of the planned access point.
            radioCount(integer): Devices's Number of radios of the planned access point.
            radios(list): Devices's Radios of the planned access point (list of objects).
            floor_id(str): floorId path parameter. The instance UUID of the floor hierarchy element.
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
            https://developer.cisco.com/docs/dna-center/#!update-planned-access-point-for-floor
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(floor_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "floorId": floor_id,
        }
        _payload = {
            "attributes": attributes,
            "isSensor": isSensor,
            "location": location,
            "position": position,
            "radioCount": radioCount,
            "radios": radios,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f6f9dde38ce458fcaf27ffd4f84bfe68_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/floors/{floorId}/planned-access-" + "points"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_f6f9dde38ce458fcaf27ffd4f84bfe68_v3_2_3_0", json_data
        )

    def create_planned_access_point_for_floor(
        self,
        floor_id,
        attributes=None,
        isSensor=None,
        location=None,
        position=None,
        radioCount=None,
        radios=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Allows creation of a new planned access point on an existing floor map including its planned radio and antenna
        details.  Use the Get variant of this API to fetch any existing planned access points for the floor.
        The payload to create a planned access point is in the same format, albeit a single object instead of a
        list, of that API.  API to create a new planned access point within a floor map.

        Args:
            attributes(object): Devices's Attributes of the planned access point.
            isSensor(boolean): Devices's Indicates that PAP is a sensor.
            location(object): Devices's Location of the planned access point.
            position(object): Devices's Position of the planned access point.
            radioCount(integer): Devices's Number of radios of the planned access point.
            radios(list): Devices's Radios of the planned access point (list of objects).
            floor_id(str): floorId path parameter. The instance UUID of the floor hierarchy element.
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
            https://developer.cisco.com/docs/dna-center/#!create-planned-access-point-for-floor
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(floor_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "floorId": floor_id,
        }
        _payload = {
            "attributes": attributes,
            "isSensor": isSensor,
            "location": location,
            "position": position,
            "radioCount": radioCount,
            "radios": radios,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ca2fe989a227585086452d24d32867a6_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/floors/{floorId}/planned-access-" + "points"
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
            "bpm_ca2fe989a227585086452d24d32867a6_v3_2_3_0", json_data
        )

    def get_planned_access_points_for_floor(
        self,
        floor_id,
        limit=None,
        offset=None,
        radios=None,
        headers=None,
        **request_parameters
    ):
        """Provides a list of Planned Access Points for the Floor it is requested for.

        Args:
            floor_id(str): floorId path parameter. The instance UUID of the floor hierarchy element.
            limit(int): limit query parameter. The number of records to show for this page;The minimum is 1, and the
                maximum is 500.
            offset(int): offset query parameter. The page offset for the response. E.g. if limit=100, offset=0 will
                return first 100 records, offset=1 will return next 100 records, etc.
            radios(bool): radios query parameter. Whether to include the planned radio details of the planned access
                points.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-planned-access-points-for-floor
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        check_type(radios, bool)
        check_type(floor_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "limit": limit,
            "offset": offset,
            "radios": radios,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "floorId": floor_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/floors/{floorId}/planned-access-" + "points"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a570c5ee77b59d8b9cd203e566288e1_v3_2_3_0", json_data
        )

    def fetches_the_details_of_all_the_devices_discovered_by_the_given_job_id_and_discovery_id(
        self,
        discovery_id,
        job_id,
        cli=None,
        http=None,
        limit=None,
        management_ip_address=None,
        netconf=None,
        offset=None,
        ping=None,
        reachability_status=None,
        snmp=None,
        headers=None,
        **request_parameters
    ):
        """API to get the details of all the devices discovered by the given jobId and discoveryId.

        Args:
            discovery_id(str): discoveryId path parameter. The id of the discovery. .
            job_id(str): jobId path parameter. The id of the discovery job. .
            management_ip_address(str): managementIpAddress query parameter. Management IP address of the network
                device    .
            reachability_status(str): reachabilityStatus query parameter. Reachability status of the network device.
            ping(str): ping query parameter. Ping status for the IP during the job run.
            cli(str): cli query parameter. CLI status for the IP during the job run.
            snmp(str): snmp query parameter. SNMP status for the IP during the job run.
            http(str): http query parameter. HTTP status for the IP during the job run.
            netconf(str): netconf query parameter. Netconf status for the IP during the job run.
            limit(int): limit query parameter. The number of records to show for this page.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!fetches-the-details-of-all-the-devices-discovered-by-the-given-job-id-and-discovery-id
        """
        check_type(headers, dict)
        check_type(management_ip_address, str)
        check_type(reachability_status, str)
        check_type(ping, str)
        check_type(cli, str)
        check_type(snmp, str)
        check_type(http, str)
        check_type(netconf, str)
        check_type(limit, int)
        check_type(offset, int)
        check_type(discovery_id, str, may_be_none=False)
        check_type(job_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "managementIpAddress": management_ip_address,
            "reachabilityStatus": reachability_status,
            "ping": ping,
            "cli": cli,
            "snmp": snmp,
            "http": http,
            "netconf": netconf,
            "limit": limit,
            "offset": offset,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "discoveryId": discovery_id,
            "jobId": job_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/discoverys/{discoveryId}/jobs/{jobId}"
            + "/discoveredNetworkDevices"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c16b0a13d2a55b479931ae0fab475cb5_v3_2_3_0", json_data
        )

    def retrieves_the_devices_clis_in_preview(
        self, network_device_id, preview_activity_id, headers=None, **request_parameters
    ):
        """Returns the device's CLIs of the wired capture intent.

        Args:
            preview_activity_id(str): previewActivityId path parameter. activity from the POST
                /deviceConfigugrationModels task response.
            network_device_id(str): networkDeviceId path parameter. device id from intent/api/v1/network-device.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-devices-c-l-is-in-preview
        """
        check_type(headers, dict)
        check_type(preview_activity_id, str, may_be_none=False)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "previewActivityId": preview_activity_id,
            "networkDeviceId": network_device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/capture/wired/configurationModels/{pr"
            + "eviewActivityId}/networkDevices/{networkDeviceId}/config"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bb142a4652d5f77b615f5662757979e_v3_2_3_0", json_data
        )

    def generates_the_devices_clis_in_preview(
        self, network_device_id, preview_activity_id, headers=None, **request_parameters
    ):
        """Generates the CLIs that will be applied on the switch device for preview.

        Args:
            preview_activity_id(str): previewActivityId path parameter. activity from the POST
                /deviceConfigugrationModels task response.
            network_device_id(str): networkDeviceId path parameter. device id from intent/api/v1/network-device.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!generates-the-devices-c-l-is-in-preview
        """
        check_type(headers, dict)
        check_type(preview_activity_id, str, may_be_none=False)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "previewActivityId": preview_activity_id,
            "networkDeviceId": network_device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/capture/wired/configurationModels/{pr"
            + "eviewActivityId}/networkDevices/{networkDeviceId}/config"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e5e7fd80e77e5f3ca4391cb360428412_v3_2_3_0", json_data
        )

    def get_device_interface_count_by_id(
        self, device_id, headers=None, **request_parameters
    ):
        """Returns the interface count for the given device.

        Args:
            device_id(str): deviceId path parameter. Device ID.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-device-interface-count
        """
        check_type(headers, dict)
        check_type(device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceId": device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/interface/network-" + "device/{deviceId}/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b7d6c62ea6522081fcf55de7eb9fd7_v3_2_3_0", json_data
        )

    def gets_the_top_n_analytics_data_related_to_network_devices(
        self,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        page=None,
        startTime=None,
        topN=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Gets the Top N analytics data related to network devices based on the provided input data. This endpoint is
        valuable to obtain the top-performing or most impacted network devices. For detailed information about
        the usage of the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        AssuranceNetworkDevices-2.0.1-resolved.yaml  The required properties for this API are topN and groupBy.

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's attributes (list of any objects).
            endTime(integer): Devices's endTime.
            filters(list): Devices's filters (list of objects).
            groupBy(list): Devices's groupBy (list of strings).
            page(object): Devices's page.
            startTime(integer): Devices's startTime.
            topN(integer): Devices's topN.
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
            https://developer.cisco.com/docs/dna-center/#!gets-the-top-n-analytics-data-related-to-network-devices
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "startTime": startTime,
            "endTime": endTime,
            "topN": topN,
            "groupBy": groupBy,
            "attributes": attributes,
            "filters": filters,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_c5c273290fae513da209ec2c9270e46d_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/networkDevices/topNAnalytics"
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
            "bpm_c5c273290fae513da209ec2c9270e46d_v3_2_3_0", json_data
        )

    def get_device_count(
        self,
        hostname=None,
        location_name=None,
        mac_address=None,
        management_ip_address=None,
        headers=None,
        **request_parameters
    ):
        """Returns the count of network devices based on the filter criteria by management IP address, mac address,
        hostname and location name.

        Args:
            hostname(list, set, str, tuple): hostname query parameter.
            management_ip_address(list, set, str, tuple): managementIpAddress query parameter.
            mac_address(list, set, str, tuple): macAddress query parameter.
            location_name(list, set, str, tuple): locationName query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-device-count
        """
        check_type(headers, dict)
        check_type(hostname, (list, set, str, tuple))
        check_type(management_ip_address, (list, set, str, tuple))
        check_type(mac_address, (list, set, str, tuple))
        check_type(location_name, (list, set, str, tuple))
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "hostname": hostname,
            "managementIpAddress": management_ip_address,
            "macAddress": mac_address,
            "locationName": location_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bbfe7340fe6752e5bc273a303d165654_v3_2_3_0", json_data
        )

    def retrieves_wired_capture_sessions(
        self,
        capture_status,
        limit=None,
        offset=None,
        switch_id=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves wired capture sessions that have been deployed (in-progress), completed, or scheduled.  Parameter
        captureStatus must be one of the following:    INPROGRESS : Wired capture sessions are on-going.
        COMPLETE :  Wired capture sessions have completed.    SCHEDULED :  Wired capture sessions that will be
        deployed to the switch device.

        Args:
            capture_status(str): captureStatus query parameter. Catalyst Center wired capture configuration status,
                Complete Status Indicates that a wired capture is completed and packet capture is
                available. In Progress Indicates that a wired packet capture is in progress and
                scheduled indicates that the packet capture is scheduled in future.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1.
            limit(int): limit query parameter. The number of records to show for this page.
            switch_id(str): switchId query parameter. The wired controller device's UUID.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-wired-capture-sessions
        """
        check_type(headers, dict)
        check_type(capture_status, str, may_be_none=False)
        check_type(offset, int)
        check_type(limit, int)
        check_type(switch_id, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "captureStatus": capture_status,
            "offset": offset,
            "limit": limit,
            "switchId": switch_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/capture/wired"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d3ba2e724e0a5bb5884670a996f28d5f_v3_2_3_0", json_data
        )

    def get_ospf_interfaces(self, headers=None, **request_parameters):
        """Returns the interfaces that has OSPF enabled.

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-o-s-p-f-interfaces
        """
        check_type(headers, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/interface/ospf"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a2868ff45f5621965f6ece01a742ce_v3_2_3_0", json_data
        )

    def retrieves_the_wireless_controller_redundancy_slots_details(
        self, id, end_time=None, start_time=None, headers=None, **request_parameters
    ):
        """Retrieves the wireless controller redundancy slots details. If startTime and endTime are not provided, the API
        defaults to the last 24 hours.

        Args:
            id(str): id path parameter. Wireless Controller UUID.
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-wireless-controller-redundancy-slots-details
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/networkDevices/{id}/wlcRedundancySlots"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f12ecf40f95453b940f0a98bc49963_v3_2_3_0", json_data
        )

    def retrieves_group_of_processes_kpis_in_wlc_over_a_specified_period_of_time(
        self,
        network_device_id,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        page=None,
        startTime=None,
        trendInterval=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Retrieves the time series process kpis for group of processes in WLC by applying complex filters, aggregate
        functions, and grouping. The data will be grouped based on the specified trend time interval. If
        startTime and endTime are not provided, the API defaults to the last 24 hours.  **The input payload
        contains the following fields,** |Field Name | Description | | --| --| | `startTime` | The start time
        indicates when the API begins retrieving data related to the resource. It must be specified in the UNIX
        epoch time format, measured in milliseconds. This value is inclusive, and if left unspecified, the
        default is 1 day before the endTime. | | `endTime` | The end time indicates the upper limit until which
        the API retrieves data related to the resource. It must be defined in the UNIX epoch time format,
        measured in milliseconds. This value is inclusive, and if left unspecified, the default is the latest
        available data. | | `trendInterval` |  The time window for aggregating metrics. This is a mandatory
        request field. Possible values include *5 minutes, 10 minutes, 1 hour, 1 day, or 7 days*. If the start
        and end time range exceeds 1 day, the trendInterval defaults to 1 hour.| | `groupBy` | Specifies the
        attributes for grouping the data. Refer to `ProcessKpisGroupByField` model for the supported grouping
        attributes| | `attributes` | A list of attributes associated with the resource, which can be requested
        to be included in the response alongside the required attributes. Refer to `ProcessKpisAttribute` model
        for the supported attributes | | `aggregateAttributes` | This specifies the attribute name and the
        function to be applied during data querying. The aggregate function is then applied to data within the
        specified start and end times. Refer to `ProcessKpisAggregateField` model for the supported aggregate
        attributes | |`filters`| This is used to specify one or more conditions for filtering the queried data.
        Refer to `ProcessKpisFilterField` model for the supported filters | |`page`| It includes the **limit,
        cursor, and timeSortOrder** fields. *limit* denotes the number of records to retrieve per page, *cursor*
        signifies the initial data position, and *timeSortOrder* is used sort the response based on the
        timestamp either in ascending or descending order. |.

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's attributes (list of strings. Available values are 'siteHierarchy',
                'siteHierarchyId', 'lastUpdatedTime', 'pid', 'name', 'totalRunTime', 'cpuPercentage',
                'memoryPercentage', 'memoryUsage' and 'apCount').
            endTime(integer): Devices's End time to which the API queries the dataset related to the resource. It
                must be specified in terms of milliseconds since UNIX epoch. Value is inclusive.
            filters(list): Devices's filters (list of objects).
            groupBy(list): Devices's groupBy (list of strings. Available values are 'name').
            page(object): Devices's page.
            startTime(integer): Devices's Start time from which the API queries the dataset related to the resource.
                It must be specified in terms of milliseconds since UNIX epoch. Value is inclusive.
            trendInterval(string): Devices's The time window to aggregate the metrics.  Interval can be 5 minutes or
                10 minutes or 1 hour or 1 day or 7 days . Available values are '5MIN', '10MIN', '1HR',
                '1DAY' and '7DAY'.
            network_device_id(str): networkDeviceId path parameter. Network Device UUID.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-group-of-processes-kpis-in-w-l-c-over-a-specified-period-of-time
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
        }
        _payload = {
            "startTime": startTime,
            "endTime": endTime,
            "trendInterval": trendInterval,
            "groupBy": groupBy,
            "attributes": attributes,
            "filters": filters,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ee2a1077335ac489ac3d4a5f7cd354_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/data/api/v1/networkDevices/{networkDeviceId}/proces"
            + "sKpis/trendAnalytics"
        )
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
            "bpm_ee2a1077335ac489ac3d4a5f7cd354_v3_2_3_0", json_data
        )

    def retrieves_the_list_of_process_cpu_and_memory_kpis_for_a_given_network_device_while_also_supporting_aggregate_attributes(
        self,
        network_device_id,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        page=None,
        startTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Retrieves the list of Process CPU and Memory KPIs for a given network device while also supporting aggregate
        attributes. If startTime and endTime are not provided, the API defaults to the last 24 hours.  **The
        input payload contains the following fields,** |Field Name | Description | | --| --| | `startTime` | The
        start time indicates when the API begins retrieving data related to the resource. It must be specified
        in the UNIX epoch time format, measured in milliseconds. This value is inclusive, and if left
        unspecified, the default is 1 day before the endTime. | | `endTime` | The end time indicates the upper
        limit until which the API retrieves data related to the resource. It must be defined in the UNIX epoch
        time format, measured in milliseconds. This value is inclusive, and if left unspecified, the default is
        the latest available data. | | `attributes` | A list of attributes associated with the resource, which
        can be requested to be included in the response alongside the required attributes. Refer to
        `ProcessKpisAttribute` model for the supported attributes | | `aggregateAttributes` | This specifies the
        attribute name and the function to be applied during data querying. The aggregate function is then
        applied to data within the specified start and end times. Refer to `ProcessKpisAggregateField` model for
        the supported aggregate attributes | |`filters`| This is used to specify one or more conditions for
        filtering the queried data. Refer to `ProcessKpisFilterField` model for the supported filters | |`page`|
        It includes the **limit, offset, and sortBy** fields. *limit* denotes the number of records to retrieve
        per page, *offset* signifies the initial data position, and *sortBy* is used to sort the response based
        on the sortBy fields. It contains the attribute name, order, and optional function for sorting by the
        aggregated field. Refer to `ProcessKpisSortByField` model for the supported sortBy names.|.

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's attributes (list of strings. Available values are 'siteHierarchy',
                'siteHierarchyId', 'lastUpdatedTime', 'pid', 'name', 'totalRunTime', 'cpuPercentage',
                'memoryPercentage', 'memoryUsage' and 'apCount').
            endTime(integer): Devices's End time to which the API queries the dataset related to the resource. It
                must be specified in terms of milliseconds since UNIX epoch. Value is inclusive.
            filters(list): Devices's filters (list of objects).
            page(object): Devices's page.
            startTime(integer): Devices's Start time from which the API queries the dataset related to the resource.
                It must be specified in terms of milliseconds since UNIX epoch. Value is inclusive.
            network_device_id(str): networkDeviceId path parameter. Network Device UUID.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-process-c-p-u-and-memory-k-p-is-for-a-given-network-device-while-also-supporting-aggregate-attributes
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
        }
        _payload = {
            "startTime": startTime,
            "endTime": endTime,
            "attributes": attributes,
            "filters": filters,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_c61dcc83f4fa53e99be03f0bbb3bf75c_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/data/api/v1/networkDevices/{networkDeviceId}/proces" + "sKpis/query"
        )
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
            "bpm_c61dcc83f4fa53e99be03f0bbb3bf75c_v3_2_3_0", json_data
        )

    def delete_user_defined_field(self, id, headers=None, **request_parameters):
        """Deletes an existing Global User-Defined-Field using it's id.

        Args:
            id(str): id path parameter. UDF id.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!delete-user-defined-field
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/user-defined-" + "field/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f0f19119501094fb5fafe05dfbca_v3_2_3_0", json_data
        )

    def update_user_defined_field(
        self,
        id,
        description=None,
        name=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Updates an existing global User Defined Field, using it's id.

        Args:
            description(string): Devices's Description of UDF.
            name(string): Devices's Name of UDF.
            id(str): id path parameter. UDF id.
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
            https://developer.cisco.com/docs/dna-center/#!update-user-defined-field
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "name": name,
            "description": description,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d76a951f85a7a927afc2f1ea935c8_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/user-defined-" + "field/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_d76a951f85a7a927afc2f1ea935c8_v3_2_3_0", json_data
        )

    def get_stack_details_for_device(
        self, device_id, headers=None, **request_parameters
    ):
        """Retrieves complete stack details for given device ID.

        Args:
            device_id(str): deviceId path parameter. Device ID.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-stack-details-for-device
        """
        check_type(headers, dict)
        check_type(device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceId": device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/{deviceId}/stack"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c07eaefa1fa45faa801764d9094336ae_v3_2_3_0", json_data
        )

    def fetches_the_summary_of_all_discoveries_with_latest_jobs(
        self,
        id=None,
        limit=None,
        name=None,
        offset=None,
        order=None,
        order_by=None,
        headers=None,
        **request_parameters
    ):
        """API to fetch the summary of all discoveries. The response includes the basic details of all discoveries, latest
        job status and the number of reachable devices.

        Args:
            id(list, set, str, tuple): id query parameter. Optional list of the discovery ids to filter by.
            name(str): name query parameter. Optional name of the discovery to filter by. This supports partial
                search. For example, searching for "Disc" will match "Discovery1", "Discovery2", etc.
            limit(int): limit query parameter. The number of records to show for this page.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1.
            order_by(str): orderBy query parameter. To fetch the latest discovery job.  use the orderBy query
                parameter with values such as lastUpdatedDate, startTime and endTime. By default, jobs
                are ordered by lastUpdatedDate display the most recent entries first.
            order(str): order query parameter. To fetch the latest discovery job.  use the order query parameter
                with values such as asc or des. By default, jobs are ordered by descending order to
                display the most recent entries first.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!fetches-the-summary-of-all-discoveries-with-latest-jobs
        """
        check_type(headers, dict)
        check_type(id, (list, set, str, tuple))
        check_type(name, str)
        check_type(limit, int)
        check_type(offset, int)
        check_type(order_by, str)
        check_type(order, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "name": name,
            "limit": limit,
            "offset": offset,
            "orderBy": order_by,
            "order": order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/discoverys/jobs/summarys"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d5b6cf4fe5628b00d79a402465216_v3_2_3_0", json_data
        )

    def get_device_summary(self, id, headers=None, **request_parameters):
        """Returns brief summary of device info for the given device Id.

        Args:
            id(str): id path parameter. Device ID.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-device-summary
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/{id}/brief"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fe0153ca24205608b8741d51f5a6d54a_v3_2_3_0", json_data
        )

    def get_functional_capability_by_id(self, id, headers=None, **request_parameters):
        """Returns functional capability with given Id.

        Args:
            id(str): id path parameter. Functional Capability UUID.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-functional-capability-by-id
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/functional-" + "capability/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f494532c45654fdaeda8d46a0d9753d_v3_2_3_0", json_data
        )

    def get_polling_interval_by_id(self, id, headers=None, **request_parameters):
        """Returns polling interval by device id.

        Args:
            id(str): id path parameter. Device ID.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-polling-interval-by-id
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/{id}/collection-" + "schedule"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f90daf1c279351f884ba3198d3b2d641_v3_2_3_0", json_data
        )

    def get_device_config_by_id(
        self, network_device_id, headers=None, **request_parameters
    ):
        """Returns the device config by specified device ID.

        Args:
            network_device_id(str): networkDeviceId path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-device-config-by-id
        """
        check_type(headers, dict)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-" + "device/{networkDeviceId}/config"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_af0bbf34adb5146b931ec874fc2cc40_v3_2_3_0", json_data
        )

    def update_interface_details(
        self,
        interface_uuid,
        adminStatus=None,
        deployment_mode=None,
        description=None,
        vlanId=None,
        voiceVlanId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Add/Update Interface description, VLAN membership, Voice VLAN and change Interface admin status ('UP'/'DOWN')
        from Request body.

        Args:
            adminStatus(string): Devices's Admin status as ('UP'/'DOWN').
            description(string): Devices's Description for the Interface.
            vlanId(integer): Devices's VLAN Id to be Updated.
            voiceVlanId(integer): Devices's Voice Vlan Id to be Updated.
            interface_uuid(str): interfaceUuid path parameter. Interface ID.
            deployment_mode(str): deploymentMode query parameter. Preview/Deploy ['Preview' means the configuration
                is not pushed to the device. 'Deploy' makes the configuration pushed to the device].
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
            https://developer.cisco.com/docs/dna-center/#!update-interface-details
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(deployment_mode, str)
        check_type(interface_uuid, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deploymentMode": deployment_mode,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "interfaceUuid": interface_uuid,
        }
        _payload = {
            "description": description,
            "adminStatus": adminStatus,
            "vlanId": vlanId,
            "voiceVlanId": voiceVlanId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator("jsd_b887c55faaca726bbe4ac2564_v3_2_3_0").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/interface/{interfaceUuid}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory("bpm_b887c55faaca726bbe4ac2564_v3_2_3_0", json_data)

    def get_supervisor_card_detail(
        self, device_uuid, headers=None, **request_parameters
    ):
        """Get supervisor card detail for a given deviceuuid. Response will contain serial no, part no, switch no and slot
        no.

        Args:
            device_uuid(str): deviceUuid path parameter. instanceuuid of device.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-supervisor-card-detail
        """
        check_type(headers, dict)
        check_type(device_uuid, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceUuid": device_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-" + "device/{deviceUuid}/supervisor-card"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_eb13516155a28570e542dcf10a91_v3_2_3_0", json_data
        )

    def remove_user_defined_field_from_device(
        self, device_id, name, headers=None, **request_parameters
    ):
        """Remove a User-Defined-Field from device. Name of UDF has to be passed as the query parameter. Please note that
        Global UDF will not be deleted by this operation.

        Args:
            device_id(str): deviceId path parameter. UUID of device from which UDF has to be removed.
            name(str): name query parameter. Name of UDF to be removed.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!remove-user-defined-field-from-device
        """
        check_type(headers, dict)
        check_type(name, str, may_be_none=False)
        check_type(device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "name": name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceId": device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/{deviceId}/user-" + "defined-field"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c1144f7a496455f99f95d36d6474c4b4_v3_2_3_0", json_data
        )

    def add_user_defined_field_to_device(
        self,
        device_id,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Assigns an existing Global User-Defined-Field to a device. If the UDF is already assigned to the specific
        device, then it updates the device UDF value accordingly. Please note that the assigning UDF 'name' must
        be an existing global UDF. Otherwise error shall be shown.

        Args:
            device_id(str): deviceId path parameter. UUID of device to which UDF has to be added.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(list): A JSON serializable Python object to send in the
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
            https://developer.cisco.com/docs/dna-center/#!add-user-defined-field-to-device
        """
        check_type(headers, dict)
        check_type(payload, list)
        check_type(device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceId": device_id,
        }
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_a73fbc67627e5bbbafe748de84d42df6_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/{deviceId}/user-" + "defined-field"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_a73fbc67627e5bbbafe748de84d42df6_v3_2_3_0", json_data
        )

    def retrieves_the_list_of_process_cpu_and_memory_kpis_for_a_given_network_device(
        self,
        network_device_id,
        end_time=None,
        limit=None,
        offset=None,
        order=None,
        sort_by=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the list of Process CPU and Memory KPIs for a given network device. Only the latest top 13 Processes
        (including all WNCD processes) are returned. If startTime and endTime are not provided, the API defaults
        to the last 24 hours.

        Args:
            network_device_id(str): networkDeviceId path parameter. Network Device UUID.
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            limit(int): limit query parameter. Maximum number of records to return.
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1.
            sort_by(str): sortBy query parameter. A field within the response to sort by.
            order(str): order query parameter. The sort order of the field ascending or descending.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-process-c-p-u-and-memory-k-p-is-for-a-given-network-device
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(limit, int)
        check_type(offset, int)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "limit": limit,
            "offset": offset,
            "sortBy": sort_by,
            "order": order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/networkDevices/{networkDeviceId}/proces" + "sKpis"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c2afd2431b0b55078d9bba2f682e1166_v3_2_3_0", json_data
        )

    def retrieves_the_total_number_of_dhcp_services_for_given_parameters(
        self,
        device_id=None,
        device_name=None,
        device_site_hierarchy=None,
        device_site_hierarchy_id=None,
        device_site_id=None,
        end_time=None,
        server_ip=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the total number of DHCP Services for given parameters. For detailed information about the usage of
        the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        DHCPServices-1.0.0-resolved.yaml.   Retrieves the total number of DHCP Services for given parameters. If
        startTime and endTime are not provided, the API defaults to the last 24 hours.

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            server_ip(str): serverIp query parameter. IP Address of the DHCP Server. This parameter supports
                wildcard (`*`) character -based search. Example: `10.76.81.*` or `*56.78*` or `*50.28`
                Examples: serverIp=10.42.3.31 (single IP Address is requested)
                serverIp=10.42.3.31&serverIp=name2&fabricVnName=name3 (multiple IP Addresses are
                requested) .
            device_id(str): deviceId query parameter. The device UUID.  Examples:
                `deviceId=6bef213c-19ca-4170-8375-b694e251101c` (single deviceId is requested)  `deviceI
                d=6bef213c-19ca-4170-8375-b694e251101c&deviceId=32219612-819e-4b5e-a96b-cf22aca13dd9
                (multiple networkDeviceIds with & separator) .
            device_name(str): deviceName query parameter. Name of the device. This parameter supports wildcard (`*`)
                character -based search. Example: `wnbu-sjc*` or `*wnbu-sjc*` or `*wnbu-sjc` Examples:
                deviceName=wnbu-sjc24.cisco.com (single device name is requested) deviceName=wnbu-
                sjc24.cisco.com&deviceName=wnbu-sjc22.cisco.com (multiple device names are requested)
                .
            device_site_hierarchy(str): deviceSiteHierarchy query parameter. The full hierarchical breakdown of the
                site tree starting from Global site name and ending with the specific site name. The
                Root site is named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`) This field
                supports wildcard asterisk (`*`) character search support. E.g. `*/San*, */San, /San*`
                Examples: `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy
                requested) `?deviceSiteHierarchy=Global/AreaName/BuildingName/FloorName&deviceSiteHierar
                chy=Global/AreaName2/BuildingName2/FloorName2` (multiple siteHierarchies requested) .
            device_site_hierarchy_id(str): deviceSiteHierarchyId query parameter. The full hierarchy breakdown of
                the site tree in id form starting from Global site UUID and ending with the specific
                site UUID. (Ex. `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports
                wildcard asterisk (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?deviceSiteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single
                siteHierarchyId requested) `?deviceSiteHierarchyId=globalUuid/areaUuid/buildingUuid/floo
                rUuid&deviceSiteHierarchyId=globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple
                siteHierarchyIds requested) .
            device_site_id(str): deviceSiteId query parameter. The UUID of the site. (Ex. `flooruuid`) Examples:
                `?deviceSiteIds=id1` (single id requested)
                `?deviceSiteIds=id1&deviceSiteIds=id2&siteId=id3` (multiple ids requested) .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-total-number-of-d-h-c-p-services-for-given-parameters
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(server_ip, str)
        check_type(device_id, str)
        check_type(device_name, str)
        check_type(device_site_hierarchy, str)
        check_type(device_site_hierarchy_id, str)
        check_type(device_site_id, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "serverIp": server_ip,
            "deviceId": device_id,
            "deviceName": device_name,
            "deviceSiteHierarchy": device_site_hierarchy,
            "deviceSiteHierarchyId": device_site_hierarchy_id,
            "deviceSiteId": device_site_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/dhcpServices/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cf3eff4f30ab56ef8e4cad0be8bac653_v3_2_3_0", json_data
        )

    def get_device_by_id(self, id, headers=None, **request_parameters):
        """Returns the network device details for the given device ID.

        Args:
            id(str): id path parameter. Device ID.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-device-by-i-d
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d86f657f8592f97014d2ebf8d37ac_v3_2_3_0", json_data
        )

    def delete_device_by_id(
        self, id, clean_config=None, headers=None, **request_parameters
    ):
        """This API allows any network device that is not currently provisioned to be removed from the inventory.
        Important: Devices currently provisioned cannot be deleted. To delete a provisioned device, the device
        must be first deprovisioned.   API to delete a network device that is not provisioned.    To delete a
        provisioned network device, use the "Delete provisioned device by Id" API
        ("/dna/intent/api/v1/sda/provisionDevices/${id}").   If the device is part of an SDA fabric, delete the
        device from the fabric before attempting to delete the network device.     To remove wireless
        controllers from the fabric domain, use the "Remove WLC from Fabric Domain" API
        ("/dna/intent/api/v1/business/sda/wireless-controller").     To remove a wired device from the fabric,
        use the "Delete a fabric device by id" API ("/dna/intent/api/v1/sda/fabricDevices/${id}").    .

        Args:
            id(str): id path parameter. Device ID.
            clean_config(bool): cleanConfig query parameter. Selecting the clean up configuration option will
                attempt to remove device settings that were configured during the addition of the device
                to the inventory and site assignment. Please note that this operation is different from
                deprovisioning. It does not remove configurations that were pushed during device
                provisioning.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!delete-device-by-id
        """
        check_type(headers, dict)
        check_type(clean_config, bool)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "cleanConfig": clean_config,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e01233fa258e393239c4b41882806_v3_2_3_0", json_data
        )

    def update_resync_interval_for_the_network_device(
        self,
        id,
        interval=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Update the resync interval (in minutes) for the given network device id.  To disable periodic resync, set
        interval as `0`.  To use global settings, set interval as `null`.

        Args:
            interval(integer): Devices's Resync interval should be between 360 to 1440 minutes. To disable periodic
                resync, set interval as `0`. To use global settings, set interval as `null`.
            id(str): id path parameter. The id of the network device.
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
            https://developer.cisco.com/docs/dna-center/#!update-resync-interval-for-the-network-device
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "interval": interval,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_fdfc828270d950ecb75480fe03f7d573_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDevices/{id}/resyncIntervalSet" + "tings"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_fdfc828270d950ecb75480fe03f7d573_v3_2_3_0", json_data
        )

    def get_resync_interval_for_the_network_device(
        self, id, headers=None, **request_parameters
    ):
        """Fetch the reysnc interval for the given network device id.

        Args:
            id(str): id path parameter. The id of the network device.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-resync-interval-for-the-network-device
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDevices/{id}/resyncIntervalSet" + "tings"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e56a4c0d91dd53ecb737da824115a050_v3_2_3_0", json_data
        )

    def get_health_score_definition_for_the_given_id(
        self, id, headers=None, **request_parameters
    ):
        """Get health score defintion for the given id. Definition includes all properties from HealthScoreDefinition
        schema by default. For detailed information about the usage of the API, please refer to the Open API
        specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-issueAndHealthDefinitions-1.0.0-resolved.yaml.   OpenAPI
        specification defined to get health score defintion for the given id. Definition includes all properties
        from HealthScoreDefinition schema by default.   API Support Documentation   id   Health score definition
        id.

        Args:
            id(str): id path parameter. Health score definition id.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-health-score-definition-for-the-given-id
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/healthScoreDefinitions/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d2a0bbce2c5b6ba0b4aee3248ace42_v3_2_3_0", json_data
        )

    def update_health_score_definition_for_the_given_id(
        self,
        id,
        includeForOverallHealth=None,
        synchronizeToIssueThreshold=None,
        thresholdValue=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Update health threshold, include status of overall health status.  And also to synchronize with global profile
        issue thresholds of the definition for given id. For detailed information about the usage of the API,
        please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        issueAndHealthDefinitions-1.0.0-resolved.yaml.   OpenAPI specification defined to update health
        threshold, include status of overall health status. And also to synchronize with global profile issue
        thresholds of the definition for given id.   API Support Documentation   id   Health score definition
        id.   The supported attributes of payload defined in  'HealthScoreDefinition'.

        Args:
            includeForOverallHealth(boolean): Devices's includeForOverallHealth.
            synchronizeToIssueThreshold(boolean): Devices's synchronizeToIssueThreshold.
            thresholdValue(number): Devices's thresholdValue.
            id(str): id path parameter. Health score definition id.
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
            https://developer.cisco.com/docs/dna-center/#!update-health-score-definition-for-the-given-id
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
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

        path_params = {
            "id": id,
        }
        _payload = {
            "includeForOverallHealth": includeForOverallHealth,
            "thresholdValue": thresholdValue,
            "synchronizeToIssueThreshold": synchronizeToIssueThreshold,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_b4f52e69ddca5b2583b28fb4c96447aa_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/healthScoreDefinitions/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_b4f52e69ddca5b2583b28fb4c96447aa_v3_2_3_0", json_data
        )

    def retrieves_the_list_of_dhcp_services_for_given_set_of_complex_filters(
        self,
        endTime=None,
        filters=None,
        page=None,
        startTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Retrieves the list of DHCP Services and offers complex filtering and sorting capabilities. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-DHCPServices-1.0.0-resolved.yaml.   Retrieves the list of
        DHCP Services and offers complex filtering and sorting capabilities. If startTime and endTime are not
        provided, the API defaults to the last 24 hours. The data in the response is calculated for the given
        time range. Field Name Description startTime start time from which API queries the data set related to
        the resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive & the default
        is latest endTime end time to which API queries the data set related to the resource. It must be
        specified in UNIX epochtime in milliseconds. Value is inclusive & the default is latest filters used to
        define one or more conditions. Only the data that satisfy these conditions will be taken into
        consideration during the calculation. page contains  limit, offset and sortBy  fields.  limit  Number of
        records to be returned in response,  offset  starting offset of data and  sortBy  attribute name, order
        to sort.

        Args:
            endTime(integer): Devices's endTime.
            filters(list): Devices's filters (list of objects).
            page(object): Devices's page.
            startTime(integer): Devices's startTime.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-d-h-c-p-services-for-given-set-of-complex-filters
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
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e6c22549e5145c4892d0bd3b97614e07_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/dhcpServices/query"
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
            "bpm_e6c22549e5145c4892d0bd3b97614e07_v3_2_3_0", json_data
        )

    def retrieve_network_devices(
        self,
        family=None,
        id=None,
        limit=None,
        management_address=None,
        management_state=None,
        offset=None,
        order=None,
        reachability_status=None,
        role=None,
        secure_mode=None,
        serial_number=None,
        sort_by=None,
        stack_device=None,
        status=None,
        views=None,
        headers=None,
        **request_parameters
    ):
        """API to fetch the list of network devices using basic filters. Use the `/dna/intent/api/v1/networkDevices/query`
        API for advanced filtering. The API supports views to fetch only the required fields.  **How the
        filtering behavior works**  Each filter item provided in the query parameters will be applied
        simultaneously such that the result is the `AND` of all the filter items.  **How views work**  The
        `views` parameter is an optional field to specify which attributes to retrieve. If this is not provided,
        then it will default to `BASIC` views. If multiple views are provided, the response will  contain the
        union of the views.  Attributes covered by the views are: * `BASIC`: id, managementAddress,
        dnsResolvedManagementIpAddress, hostname, macAddress, serialNumbers, type, family, series, status,
        platformIds, softwareType, softwareVersion, vendor, stackDevice, bootTime, role, roleSource,
        apEthernetMacAddress, apManagerInterfaceIpAddress, apWlcIpAddress, deviceSupportLevel, snmpContact,
        snmpLocation, secureMode * `RESYNC`: id, managementAddress, dnsResolvedManagementIpAddress, hostname,
        macAddress, serialNumbers, type, family, series, status, reachabilityStatus, reachabilityFailureReason,
        managementState, lastSuccessfulResyncReasons, resyncStartTime, resyncEndTime, resyncReasons,
        resyncRequestedByApps, pendingResyncRequestCount, pendingResyncRequestReasons, resyncIntervalSource,
        resyncIntervalMinutes, errorCode, errorDescription, secureMode * `USER_DEFINED_FIELDS`: id,
        managementAddress, dnsResolvedManagementIpAddress, hostname, macAddress, serialNumbers, type, family,
        series, status, userDefinedFields  **Note** `CREDENTIALS` view is not supported in this API. Use the
        `/dna/intent/api/v1/networkDevices/{id}` API to get the credentials of a network device.

        Args:
            id(str): id query parameter. Network device Id.
            management_address(str): managementAddress query parameter. Management address of the network device.
            serial_number(str): serialNumber query parameter. Serial number of the network device.
            family(str): family query parameter. Product family of the network device. For example, Switches,
                Routers, etc.
            stack_device(bool): stackDevice query parameter. Flag indicating if the device is a stack device.
            role(str): role query parameter. Role assigned to the network device. .
            status(str): status query parameter. Inventory related status of the network device. (status:
                Description),  (`MANAGED`: The device is successfully managed.),  (`SYNC_NOT_STARTED`:
                Sync request is queued and pending processing.),  (`SYNC_INIT_FAILED`: Sync
                initialization failed due to bootstrap issues.),  (`SYNC_PRECHECK_FAILED`: Device failed
                to meet necessary preconditions for sync.),  (`SYNC_IN_PROGRESS`: Sync with the device
                is in progress.),  (`SYNC_INTERNAL_ERROR`: Encountered an internal error during data
                collection, potentially leading to incomplete or outdated device information.),
                (`SYNC_DISABLED`: Sync has been disabled on the device.),  (`DELETING_DEVICE`: The
                device is being deleted from Catalyst Center.),  (`UNDER_MAINTENANCE`: The device is in
                maintenance mode. Assurance will not raise alerts when the network device is in
                maintenance mode.),  (`QUARANTINED`: The device is in quarantined state. Inventory sync
                and provisioning are disabled for the device.),  (`UNASSOCIATED`: Access point is not
                associated with any WLC.),  (`UNREACHABLE`: The device is not reachable by either
                SNMP/HTTP/NETCONF or ICMP.),  (`UNKNOWN`: All information from the device could not be
                collected, or inventory collection was not started. It may be a temporary issue. Attempt
                to resync the device, and if the error persists, contact Cisco TAC.),  .
            reachability_status(str): reachabilityStatus query parameter. Reachability status of the network device.
                Possible values are: * `REACHABLE` Device is reachable by SNMP (in case of network
                device) or HTTP (in case of compute device or Meraki device). * `ONLY_PING_REACHABLE`
                Mandatory protocol (SNMP/HTTP/NETCONF) failed for the device. The device is reachable
                only by ICMP.  * `UNREACHABLE` Device is not reachable by either SNMP/HTTP or ICMP. *
                `UNKNOWN` Device reachability status can't be determined. The product hasn't interacted
                with the device yet, or the parent device that controls the device is unreachable. .
            management_state(str): managementState query parameter. The status of the network device's
                manageability. Possible values are: * `MANAGED`: Device is managed. *
                `UNDER_MAINTENANCE`: Device is in service maintenance. * `NEVER_MANAGED`: Device has
                never been managed. .
            secure_mode(str): secureMode query parameter. Security mode of the network device.
            views(list, set, str, tuple): views query parameter. The specific views being requested. This is an
                optional parameter which can be passed to get one or more of the network  device data.
                If this is not provided, then it will default to `BASIC` views. If multiple views are
                provided, the response  will contain the union of the views. Attributes covered by the
                views are: * `BASIC`: id, managementAddress, dnsResolvedManagementIpAddress, hostname,
                macAddress, serialNumbers, type, family, series, status, platformIds, softwareType,
                softwareVersion, vendor, stackDevice, bootTime, role, roleSource, apEthernetMacAddress,
                apManagerInterfaceIpAddress, apWlcIpAddress, deviceSupportLevel, snmpContact,
                snmpLocation, secureMode * `RESYNC`: id, managementAddress,
                dnsResolvedManagementIpAddress, hostname, macAddress, serialNumbers, type, family,
                series, status, reachabilityStatus, reachabilityFailureReason, managementState,
                lastSuccessfulResyncReasons, resyncStartTime, resyncEndTime, resyncReasons,
                resyncRequestedByApps, pendingResyncRequestCount, pendingResyncRequestReasons,
                resyncIntervalSource, resyncIntervalMinutes, errorCode, errorDescription, secureMode *
                `USER_DEFINED_FIELDS`: id, managementAddress, dnsResolvedManagementIpAddress, hostname,
                macAddress, serialNumbers, type, family, series, status, userDefinedFields Note:
                `CREDENTIALS` view is not supported in this API. Use the
                `/dna/intent/api/v1/networkDevices/{id}` API to get the credentials of a network device.
                .
            limit(int): limit query parameter. The number of records to show for this page.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1.
            sort_by(str): sortBy query parameter. A property within the response to sort by.
            order(str): order query parameter. Whether ascending or descending order should be used to sort the
                response.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-network-devices
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(management_address, str)
        check_type(serial_number, str)
        check_type(family, str)
        check_type(stack_device, bool)
        check_type(role, str)
        check_type(status, str)
        check_type(reachability_status, str)
        check_type(management_state, str)
        check_type(secure_mode, str)
        check_type(views, (list, set, str, tuple))
        check_type(limit, int)
        check_type(offset, int)
        check_type(sort_by, str)
        check_type(order, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "managementAddress": management_address,
            "serialNumber": serial_number,
            "family": family,
            "stackDevice": stack_device,
            "role": role,
            "status": status,
            "reachabilityStatus": reachability_status,
            "managementState": management_state,
            "secureMode": secure_mode,
            "views": views,
            "limit": limit,
            "offset": offset,
            "sortBy": sort_by,
            "order": order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDevices"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e78bc218325565becdd907ff2e4e30_v3_2_3_0", json_data
        )

    def adds_a_new_network_device(
        self,
        category=None,
        credentials=None,
        managementAddress=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Adds the network device to inventory. The API supports Network Device, Meraki Dashboard, Compute Device,
        Firewall Management Center (FMC) and Third-Party Device. Access  points associated with added WLC will
        be automatically added to inventory. For Meraki Dashboard, use the dashboard URL as the management
        address.

        Args:
            category(string): Devices's Category of the device. Used to determine the type of the device being
                added. | Category                                    | Description
                | Required Credentials | Optional Credentials | |
                ------------------------------------------|
                --------------------------------------------------------------------------------------|
                -------------------| -------------------| | `NETWORK_DEVICE`
                | Standard Cisco network devices like switches, routers, controllers
                | CLI, SNMP            | HTTP, NETCONF        | | `COMPUTE_DEVICE`
                | Server or computing system manufactured by Cisco such as Unified Computing System
                (UCS) | HTTP                 | CLI, SNMP            | | `THIRD_PARTY_DEVICE`
                | Non-Cisco network devices that support SNMP monitoring
                | SNMP                 |                    | | `MERAKI_DASHBOARD`
                | Cisco Meraki cloud-managed devices accessed via Meraki Dashboard
                | Meraki               |                    | | `FIREWALL_MANAGEMENT_CENTER`
                | Cisco Secure Firewall Management Center (FMC)
                | HTTP                 |                    | . Available values are
                'FIREWALL_MANAGEMENT_CENTER'.
            credentials(object): Devices's Credentials used to access the network device. .
            managementAddress(): Devices's Management address of the network device. For meraki dashboard, this is
                the dashboard URL.
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
            https://developer.cisco.com/docs/dna-center/#!adds-a-new-network-device
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "category": category,
            "managementAddress": managementAddress,
            "credentials": credentials,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_c5df380093bd5a748d177a34375faab4_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDevices"
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
            "bpm_c5df380093bd5a748d177a34375faab4_v3_2_3_0", json_data
        )

    def the_total_interfaces_count_across_the_network_devices(
        self,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        page=None,
        startTime=None,
        views=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Gets the total number of interfaces across the Network devices based on the provided complex filters and
        aggregation functions. For detailed information about the usage of the API, please refer to the Open API
        specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-interfaces-2.0.0-resolved.yaml.

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's attributes (list of strings).
            endTime(integer): Devices's endTime.
            filters(list): Devices's filters (list of objects).
            page(object): Devices's page.
            startTime(integer): Devices's startTime.
            views(list): Devices's views (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!the-total-interfaces-count-across-the-network-devices
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "startTime": startTime,
            "endTime": endTime,
            "views": views,
            "attributes": attributes,
            "filters": filters,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_b0b146a144a65aa296b8b939c2926158_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/interfaces/query/count"
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
            "bpm_b0b146a144a65aa296b8b939c2926158_v3_2_3_0", json_data
        )

    def get_connected_device_detail(
        self, device_uuid, interface_uuid, headers=None, **request_parameters
    ):
        """Get connected device detail for given deviceUuid and interfaceUuid.

        Args:
            device_uuid(str): deviceUuid path parameter. instanceuuid of Device.
            interface_uuid(str): interfaceUuid path parameter. instanceuuid of interface.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-connected-device-detail
        """
        check_type(headers, dict)
        check_type(device_uuid, str, may_be_none=False)
        check_type(interface_uuid, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceUuid": device_uuid,
            "interfaceUuid": interface_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/network-"
            + "device/{deviceUuid}/interface/{interfaceUuid}/neighbor"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a1878314ffd35d29bea49f12d10b59c8_v3_2_3_0", json_data
        )

    def get_the_filter_groups_for_given_search_criteria(
        self,
        id=None,
        limit=None,
        name=None,
        offset=None,
        type=None,
        headers=None,
        **request_parameters
    ):
        """Returns the details of filter groups for given search criteria specified in query parameters.

        Args:
            id(list, set, str, tuple): id query parameter. Filter Group id. Examples:
                `?id=2ee1b9f0-8036-443b-bad0-7692760af1b5`(single id requested)
                `?id=2ee1b9f0-8036-443b-bad0-7692760af1b5&id=ae368f0b-f4e3-4e8f-a914-011cbd19bb51`
                (multiple ids requested) .
            name(list, set, str, tuple): name query parameter. Filter Group name. Examples: `?name=SJC
                Wireless`(single name requested) `?name=SJC Wireless&name=Global Wired` (multiple names
                requested) .
            type(list, set, str, tuple): type query parameter. Type of the filter group. Examples: type=Generic
                (single Filter Group type requested) type=Generic&type=Site (multiple Filter Group types
                requested) .
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1.
            limit(int): limit query parameter. Maximum number of records to return.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-the-filter-groups-for-given-search-criteria
        """
        check_type(headers, dict)
        check_type(id, (list, set, str, tuple))
        check_type(name, (list, set, str, tuple))
        check_type(type, (list, set, str, tuple))
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "name": name,
            "type": type,
            "offset": offset,
            "limit": limit,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/filterGroups"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c44f41d6d561bb2a687325b094257_v3_2_3_0", json_data
        )

    def create_filter_group(
        self,
        filters=None,
        name=None,
        type=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Creates filter group with given filters.

        Args:
            filters(list): Devices's List of filters used in this Filter Group (list of objects).
            name(string): Devices's Filter Group name. Only alphabhets, digits and space is allowed for name.
            type(string): Devices's The type of the Filter Group.. Available values are 'Generic', 'Site', 'Network'
                and 'Client'.
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
            https://developer.cisco.com/docs/dna-center/#!create-filter-group
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "name": name,
            "type": type,
            "filters": filters,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d6866f768b05f8aa12a142ec526f432_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/filterGroups"
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
            "bpm_d6866f768b05f8aa12a142ec526f432_v3_2_3_0", json_data
        )

    def update_device_management_address(
        self,
        deviceid,
        newIP=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This is a simple PUT API to edit the management IP Address of the device.

        Args:
            newIP(string): Devices's New IP Address of the device to be Updated.
            deviceid(str): deviceid path parameter. The UUID of the device whose management IP address is to be
                updated.
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
            https://developer.cisco.com/docs/dna-center/#!update-device-management-address
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(deviceid, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceid": deviceid,
        }
        _payload = {
            "newIP": newIP,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_cb98464ddb5ee9ba7ebb4428443ba9_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/{deviceid}/management-" + "address"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_cb98464ddb5ee9ba7ebb4428443ba9_v3_2_3_0", json_data
        )

    def get_device_config_for_all_devices(self, headers=None, **request_parameters):
        """Returns the config for all devices. This API has been deprecated and will not be available in a Cisco Catalyst
        Center release after Nov 1st 2024 23:59:59 GMT.

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-device-config-for-all-devices
        """
        check_type(headers, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/config"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ed2bca4be412527198720a4dfec9604a_v3_2_3_0", json_data
        )

    def get_interface_by_id(self, id, headers=None, **request_parameters):
        """Returns the interface for the given interface ID.

        Args:
            id(str): id path parameter. Interface ID.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-interface-by-id
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/interface/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b16bff74ae54ca88a02b34df169218_v3_2_3_0", json_data
        )

    def count_the_number_of_network_devices(
        self,
        family=None,
        id=None,
        management_address=None,
        management_state=None,
        reachability_status=None,
        role=None,
        secure_mode=None,
        serial_number=None,
        stack_device=None,
        status=None,
        headers=None,
        **request_parameters
    ):
        """API to fetch the count of network devices using basic filters. Use the
        `/dna/intent/api/v1/networkDevices/query/count` API if you need advanced filtering.

        Args:
            id(str): id query parameter. Network device Id.
            management_address(str): managementAddress query parameter. Management address of the network device.
            serial_number(str): serialNumber query parameter. Serial number of the network device.
            family(str): family query parameter. Product family of the network device. For example, Switches,
                Routers, etc.
            stack_device(bool): stackDevice query parameter. Flag indicating if the device is a stack device.
            role(str): role query parameter. Role assigned to the network device. .
            status(str): status query parameter. Inventory related status of the network device. (status:
                Description),  (`MANAGED`: The device is successfully managed.),  (`SYNC_NOT_STARTED`:
                Sync request is queued and pending processing.),  (`SYNC_INIT_FAILED`: Sync
                initialization failed due to bootstrap issues.),  (`SYNC_PRECHECK_FAILED`: Device failed
                to meet necessary preconditions for sync.),  (`SYNC_IN_PROGRESS`: Sync with the device
                is in progress.),  (`SYNC_INTERNAL_ERROR`: Encountered an internal error during data
                collection, potentially leading to incomplete or outdated device information.),
                (`SYNC_DISABLED`: Sync has been disabled on the device.),  (`DELETING_DEVICE`: The
                device is being deleted from Catalyst Center.),  (`UNDER_MAINTENANCE`: The device is in
                maintenance mode. Assurance will not raise alerts when the network device is in
                maintenance mode.),  (`QUARANTINED`: The device is in quarantined state. Inventory sync
                and provisioning are disabled for the device.),  (`UNASSOCIATED`: Access point is not
                associated with any WLC.),  (`UNREACHABLE`: The device is not reachable by either
                SNMP/HTTP/NETCONF or ICMP.),  (`UNKNOWN`: All information from the device could not be
                collected, or inventory collection was not started. It may be a temporary issue. Attempt
                to resync the device, and if the error persists, contact Cisco TAC.),  .
            reachability_status(str): reachabilityStatus query parameter. Reachability status of the network device.
                Possible values are: * `REACHABLE` Device is reachable by SNMP (in case of network
                device) or HTTP (in case of compute device or Meraki device). * `ONLY_PING_REACHABLE`
                Mandatory protocol (SNMP/HTTP/NETCONF) failed for the device. The device is reachable
                only by ICMP.  * `UNREACHABLE` Device is not reachable by either SNMP/HTTP or ICMP. *
                `UNKNOWN` Device reachability status can't be determined. The product hasn't interacted
                with the device yet, or the parent device that controls the device is unreachable. .
            management_state(str): managementState query parameter. The status of the network device's
                manageability. Possible values are: * `MANAGED`: Device is managed. *
                `UNDER_MAINTENANCE`: Device is in service maintenance. * `NEVER_MANAGED`: Device has
                never been managed. .
            secure_mode(str): secureMode query parameter. Security mode of the network device.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!count-the-number-of-network-devices
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(management_address, str)
        check_type(serial_number, str)
        check_type(family, str)
        check_type(stack_device, bool)
        check_type(role, str)
        check_type(status, str)
        check_type(reachability_status, str)
        check_type(management_state, str)
        check_type(secure_mode, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "managementAddress": management_address,
            "serialNumber": serial_number,
            "family": family,
            "stackDevice": stack_device,
            "role": role,
            "status": status,
            "reachabilityStatus": reachability_status,
            "managementState": management_state,
            "secureMode": secure_mode,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDevices/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fc60c9c2ca32545fab1bbe540a99c218_v3_2_3_0", json_data
        )

    def get_details_of_a_single_assurance_event(
        self, id, attribute=None, view=None, headers=None, **request_parameters
    ):
        """API to fetch the details of an assurance event using event `id`. For detailed information about the usage of the
        API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        AssuranceEvents-1.0.0-resolved.yaml.   OpenAPI specification defined to fetch the single assurance using
        event 'id'   API Support Documentation   id   Unique identifier for the event   Query Parameters:   view
        Specified 'view' can be requested. Each view correspondsto different sets of data. By default basic view
        attributes will be shown   'view' an optional parameter which can be passed to get one or more of the
        views.         View   Response Data           basic   id, name, timestamp, details, messageType,
        siteHierarchyId, siteHierarchy, deviceFamily, networkDeviceId, networkDeviceName, managementIpAddress
        network   id, name, severity, facility, mnemonic, eventStatus, timestamp, details, messageType,
        siteHierarchyId, siteHierarchy, deviceFamily, networkDeviceId, networkDeviceName, managementIpAddress,
        replacedDeviceSerialNumber, replacingDeviceSerialNumber, switchNumber       ap   id, name, eventStatus,
        timestamp, details, messageType, siteHierarchyId, siteHierarchy, deviceFamily, networkDeviceId,
        networkDeviceName, managementIpAddress, apMac, wlcName, frequency, apSwitchName, apSwitchId, wlcId,
        reasonDescription, lastApDisconnectReason, lastApResetType, apRadioOperationState,
        currentRadioPowerLevel, previousRadioPowerLevel, newRadioChannelList, newRadioChannelWidth,
        oldRadioChannelList, oldRadioChannelWidth, radioNoise, radioInterference, radioChannelUtilization,
        affectedClients       wiredClient   id, name, severity, facility, mnemonic, eventStatus, timestamp,
        details, messageType, siteHierarchyId, siteHierarchy, deviceFamily, networkDeviceId, networkDeviceName,
        managementIpAddress, identifier, clientMac, connectedInterfaceName, ipv4, ipv6, vlanId, auditSessionId,
        reasonDescription       wirelessClient   id, name, timestamp, details, messageType, siteHierarchyId,
        siteHierarchy, deviceFamily, networkDeviceId, networkDeviceName, identifier, clientMac,
        wirelessClientEventStartTime, wirelessClientEventEndTime, radioChannelSlot, isPrivateMac, vlanId,
        authServerIp, apRole, assocRssi, assocSnr, udnName, udnId, duid, failureIpAddress, roamType,
        subReasonDescription, invalidIeAPs, candidateAPs, missingResponseAPs, apMac, wlcName, wlcId, ssid,
        username, frequency, resultStatus, failureCategory, dhcpServerIp, ipv4, ipv6, reasonDescription,
        childEvents           Examples :   ?view=network (single view requested)
        ?view=wiredClient&view=network (multiple view requested)   attribute   The list of attributes that needs
        to be included in the response. If this parameter is not provided, then basic attributes ('id', 'name',
        'timestamp', 'details', 'messageType', 'siteHierarchyId', 'siteHierarchy', 'deviceFamily',
        'networkDeviceId', 'networkDeviceName', 'managementIpAddress') would be part of the response.
        Supported Attributes:   affectedClients ,  apMac ,  apRadioOperationState ,  apRole ,  apSwitchName ,
        apSwitchId ,  assocRssi ,  assocSnr ,  auditSessionId , authServerIp , bssid , candidateAPs ,
        childEvents , clientMac ,  connectedInterfaceName , currentRadioPowerLevel ,  details , deviceFamily ,
        dhcpServerIp , duid ,  eventStatus ,  facility , failureCategory ,  failureIpAddress ,  frequency , id ,
        identifier , invalidIeAPs ,  ipv4 , ipv6 , isPrivateMac ,  lastApDisconnectReason , lastApResetType ,
        managementIpAddress , messageType ,  missingResponseAPs ,  mnemonic , name ,  networkDeviceId ,
        networkDeviceName , newRadioChannelList ,  newRadioChannelWidth , oldRadioChannelList ,
        oldRadioChannelWidth , previousRadioPowerLevel ,  radioChannelSlot ,  radioChannelUtilization ,
        radioInterference , radioNoise , reasonDescription , replacedDeviceSerialNumber ,
        replacingDeviceSerialNumber , resultStatus , roamType , severity , siteHierarchy , siteHierarchyId ,
        ssid , subReasonDescription , switchNumber , timestamp , udnId , udnName , username , vlanId ,
        wirelessClientEventEndTime , wirelessClientEventStartTime , wlcId wlcName     If length of attribute
        list is too long, when using the query parameter, please use  view  param instead.     Examples :
        ?attribute=id (single attribute requested)   ?attribute=id&attribute=name (multiple attribute
        requested).

        Args:
            id(str): id path parameter. Unique identifier for the event.
            attribute(str): attribute query parameter. The list of attributes that needs to be included in the
                response. If this parameter is not provided, then basic attributes (`id`, `name`,
                `timestamp`, `details`, `messageType`, `siteHierarchyId`, `siteHierarchy`,
                `deviceFamily`, `networkDeviceId`, `networkDeviceName`, `managementIpAddress`) would be
                part of the response.  Examples: `attribute=name` (single attribute requested)
                `attribute=name&attribute=networkDeviceName` (multiple attribute requested) .
            view(str): view query parameter. The list of events views. Please refer to `EventViews` for the
                supported list  Examples: `view=network` (single view requested) `view=network&view=ap`
                (multiple view requested) .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-details-of-a-single-assurance-event
        """
        check_type(headers, dict)
        check_type(attribute, str)
        check_type(view, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "attribute": attribute,
            "view": view,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/assuranceEvents/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a36092e78528b9bd8730c93b5412d_v3_2_3_0", json_data
        )

    def get_network_device_insecure_configurations(
        self,
        id,
        limit=None,
        module=None,
        offset=None,
        order=None,
        sort_by=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the list of insecure CLI configurations currently applied on the network device identified by network
        device `id`. Insecure configurations are CLI commands that use deprecated, weak, or non-compliant
        security settings and are restricted on IOS-XE devices beginning with release `26.1.1`. These include
        configurations that rely on outdated security protocols, insecure authentication mechanisms, or any
        commands flagged as non-secure by the device.

        Args:
            id(str): id path parameter. Unique identifier of the network device.
            module(list, set, str, tuple): module query parameter. The module names associated with insecure
                configurations. Examples AAA, BOOTP, HTTP, CDP, IP, TRANSPORT, TFTP, TELNET, RCMD, LINE,
                FTP, NTP, SNMP, SANET, CTS, PARSER, LOGGING, DSPFARM_PROFILE, STCAPP, SSH, HSRP, CAPWAP,
                MSDP, KEY_CHAIN, KEY_CHAIN_MACSEC, VOICE, HTTPCLIENT, CALLMANAGER, SIPUA, PMIPv6,
                TLS_TUNNEL, DEVICE_SENSOR, EPC, DHCP, SYSTEM, IFS, MPLS_LDP, ISIS, BGP, NMSP, EIGRP,
                OSPFV2, OSPFV3, IVR, GATEWAY_ACCOUNTING, CALL_LEG, APPLICATION_MONITOR, WEB_SERVICE,
                VRRP, GLBP, WCCP, LISP. Up to 10 filter values are allowed. .
            limit(int): limit query parameter. The number of records to show for this page.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1.
            sort_by(str): sortBy query parameter. A property within the response to sort by, if not provided default
                sorts by module .
            order(str): order query parameter. Whether ascending or descending order should be used to sort the
                response.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-network-device-insecure-configurations
        """
        check_type(headers, dict)
        check_type(module, (list, set, str, tuple))
        check_type(limit, int)
        check_type(offset, int)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "module": module,
            "limit": limit,
            "offset": offset,
            "sortBy": sort_by,
            "order": order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDevices/{id}/insecureConfigura" + "tions"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a5f965d15f59c8bf115d69f06bc729_v3_2_3_0", json_data
        )

    def retrieves_information_for_the_given_port_channel_on_a_specific_network_device(
        self, id, network_device_id, headers=None, **request_parameters
    ):
        """This API endpoint retrieves detailed information for a specified port channel using its unique identifier within
        a given network device.  ### Aggregation Protocol  **The protocol used for aggregating multiple physical
        links into the port channel:**  | Protocol | Description | |----------|-------------| | LACP     | A
        dynamic, IEEE-standard protocol that aggregates multiple physical links into a single logical link. It
        provides automatic negotiation and configuration for increased bandwidth and redundancy. Commonly used
        in multi-vendor networks. | | PAGP     | A Cisco proprietary protocol that aggregates links into a
        logical link. It automatically negotiates link aggregation between Cisco devices. Typically used in
        Cisco-only environments. | | NONE     | Indicates no link aggregation protocol is used. Links are
        manually configured without protocol-based negotiation. |  ### Channel Mode  **The mode of operation for
        the channel:**  | Mode                | Description | |---------------------|-------------| | ON
        | This mode forces the interface to channel without any negotiation protocol. It assumes the other side
        is also set to `ON`. This mode does not use LACP or PAgP, making it less flexible as both ends must be
        manually configured. | | ACTIVE              | Used with LACP, this mode actively tries to form an
        EtherChannel by sending LACP packets. It requires the other side to be in either `ACTIVE` or `PASSIVE`
        mode. | | PASSIVE             | Also used with LACP, this mode waits for the other side to initiate the
        channel. It will form a channel if it receives LACP packets from a switch in `ACTIVE` mode. | | AUTO
        | Used with PAgP, this mode passively waits for the other side to initiate the EtherChannel. It requires
        the other side to be in `DESIRABLE` mode to form a channel. | | AUTO_NON_SILENT     | Similar to `AUTO`,
        but specifically for use in environments where devices do not send PAgP packets unless they detect PAgP
        packets from a neighbor. | | DESIRABLE           | Another PAgP mode, where the interface actively tries
        to negotiate the EtherChannel by sending PAgP packets. It will form a channel if the other side is in
        either `AUTO` or `DESIRABLE` mode. | | DESIRABLE_NON_SILENT| Similar to `DESIRABLE`, but requires
        explicit acknowledgment from the other side before forming a channel. It is used when the other device
        might not send PAgP packets unless it receives them. | | NONE                | Refers to a state where
        no channeling protocol is configured. This is essentially a non-operational mode regarding EtherChannel
        formation. |.

        Args:
            network_device_id(str): networkDeviceId path parameter. Unique identifier for the network device.
            id(str): id path parameter. Unique identifier for the port channel.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-information-for-the-given-port-channel-on-a-specific-network-device
        """
        check_type(headers, dict)
        check_type(network_device_id, str, may_be_none=False)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/networkDevices/{networkDeviceId}/port" + "Channels/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fa69f2cf023d5cd7add1507135193f53_v3_2_3_0", json_data
        )

    def retrieves_the_list_of_dns_services_for_given_parameters(
        self,
        device_id=None,
        device_site_hierarchy_id=None,
        device_site_id=None,
        end_time=None,
        limit=None,
        offset=None,
        order=None,
        server_ip=None,
        sort_by=None,
        ssid=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the list of DNS Services and offers basic filtering and sorting capabilities. For detailed information
        about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-DNSServices-1.0.0-resolved.yaml.   Retrieves the list of DNS
        Services and offers basic filtering and sorting capabilities. If startTime and endTime are not provided,
        the API defaults to the last 24 hours. The data in the response is calculated for the given time range.

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            limit(int): limit query parameter. Maximum number of records to return.
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1.
            sort_by(str): sortBy query parameter. Field name on which sorting needs to be done.
            order(str): order query parameter. The sort order of the field ascending or descending.
            server_ip(str): serverIp query parameter. IP Address of the DNS Server. This parameter supports wildcard
                (`*`) character -based search. Example: `10.76.81.*` or `*56.78*` or `*50.28` Examples:
                serverIp=10.42.3.31 (single IP Address is requested)
                serverIp=10.42.3.31&serverIp=name2&fabricVnName=name3 (multiple IP Addresses are
                requested) .
            device_id(str): deviceId query parameter. The device UUID.  Examples:
                `deviceId=6bef213c-19ca-4170-8375-b694e251101c` (single deviceId is requested)  `deviceI
                d=6bef213c-19ca-4170-8375-b694e251101c&deviceId=32219612-819e-4b5e-a96b-cf22aca13dd9
                (multiple networkDeviceIds with & separator) .
            device_site_hierarchy_id(str): deviceSiteHierarchyId query parameter. The full hierarchy breakdown of
                the site tree in id form starting from Global site UUID and ending with the specific
                site UUID. (Ex. `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports
                wildcard asterisk (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?deviceSiteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single
                siteHierarchyId requested) `?deviceSiteHierarchyId=globalUuid/areaUuid/buildingUuid/floo
                rUuid&deviceSiteHierarchyId=globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple
                siteHierarchyIds requested) .
            device_site_id(str): deviceSiteId query parameter. The UUID of the site. (Ex. `flooruuid`) Examples:
                `?deviceSiteIds=id1` (single id requested)
                `?deviceSiteIds=id1&deviceSiteIds=id2&siteId=id3` (multiple ids requested) .
            ssid(str): ssid query parameter. SSID is the name of wireless network to which client connects to. It is
                also referred to as WLAN ID Wireless Local Area Network Identifier. This field supports
                wildcard (`*`) character-based search. If the field contains the (`*`) character, please
                use the /query API for search.  Ex: `*Alpha*` or `Alpha*` or `*Alpha` Examples:
                `ssid=Alpha` (single ssid requested) `ssid=Alpha&ssid=Guest` (multiple ssid requested) .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-d-n-s-services-for-given-parameters
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(limit, int)
        check_type(offset, int)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(server_ip, str)
        check_type(device_id, str)
        check_type(device_site_hierarchy_id, str)
        check_type(device_site_id, str)
        check_type(ssid, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "limit": limit,
            "offset": offset,
            "sortBy": sort_by,
            "order": order,
            "serverIp": server_ip,
            "deviceId": device_id,
            "deviceSiteHierarchyId": device_site_hierarchy_id,
            "deviceSiteId": device_site_id,
            "ssid": ssid,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/dnsServices"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e71b7fc7245755ec8be93800d32738a8_v3_2_3_0", json_data
        )

    def gets_the_trend_analytics_data(
        self,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        page=None,
        startTime=None,
        trendInterval=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Gets the Trend analytics Network device data for the given time range. The data will be grouped based on the
        given trend time Interval. The required property for this API is `trendInterval`. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-AssuranceNetworkDevices-2.0.1-resolved.yaml.   The input
        payload contains the following fields,         Field Name   Description           startTime   The start
        time indicates the point from which the API retrieves the dataset associated with the resource. It must
        be specified in UNIX epochtime in milliseconds. Value is inclusive & the default is latest       endTime
        The end time signifies the limit until which the API retrieves the dataset associated with the resource.
        It must be specified in UNIX epochtime in milliseconds. Value is inclusive & the default is latest
        trendInterval   The time window for aggregating metrics can be set to intervals of 5 minutes, 10
        minutes, 30 minutes, 1 hour, 1 day, or 7 days. If the start and end time range exceeds 1 day, the
        minimum expected interval value is 1 hour or higher. The default polling or data collection interval for
        switches and router family devices is 10 minutes. Therefore, even if a 5-minute interval is specified in
        the input, the data will be available for intervals of 10 minutes. This is a required property for this
        API       groupBy   The groupby defines the criteria for grouping the data based on specific attributes.
        The available group by fields correspond to the attributes listed. For a comprehensive list of supported
        attributes, please refer to the  NetworkDevicesAnalyticsGroupBy  model.       attributes   The attribute
        is useful for obtaining one or more field data in addition to the aggregated data within the specified
        start and end time range. The supported attributes are listed in   NetworkDevicesAnalyticsAttributes
        model       aggregateAttributes   The aggregateAttributes denotes the attribute name(s) on which the
        aggregate functions is to be applied.

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of any objects).
            attributes(list): Devices's attributes (list of strings).
            endTime(integer): Devices's endTime.
            filters(list): Devices's filters (list of objects).
            groupBy(list): Devices's groupBy (list of any objects).
            page(object): Devices's page.
            startTime(integer): Devices's startTime.
            trendInterval(string): Devices's trendInterval.
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
            https://developer.cisco.com/docs/dna-center/#!gets-the-trend-analytics-data
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "startTime": startTime,
            "endTime": endTime,
            "trendInterval": trendInterval,
            "groupBy": groupBy,
            "attributes": attributes,
            "filters": filters,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ac7ce690e0f55a469b0a9bfa3d2c165e_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/networkDevices/trendAnalytics"
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
            "bpm_ac7ce690e0f55a469b0a9bfa3d2c165e_v3_2_3_0", json_data
        )

    def count_the_number_of_discovered_network_devices_by_discovery_id(
        self,
        discovery_id,
        job_id,
        cli=None,
        http=None,
        management_ip_address=None,
        netconf=None,
        ping=None,
        reachability_status=None,
        snmp=None,
        headers=None,
        **request_parameters
    ):
        """API to fetch the number of discovered network devices by using the given discoveryId and jobId.

        Args:
            discovery_id(str): discoveryId path parameter. Discovery id     .
            job_id(str): jobId path parameter. The id of the discovery job. .
            management_ip_address(str): managementIpAddress query parameter. Management IP address of the network
                device    .
            reachability_status(str): reachabilityStatus query parameter. Reachability status of the network device.
            ping(str): ping query parameter. Ping status for the IP during the job run. Available values are
                'SUCCESS', 'FAILURE', 'NOT_PROVIDED' and 'NOT_VALIDATED        .
            cli(str): cli query parameter. CLI status for the IP during the job run. Available values are 'SUCCESS',
                'FAILURE', 'NOT_PROVIDED' and 'NOT_VALIDATED   .
            snmp(str): snmp query parameter. SNMP status for the IP during the job run. Available values are
                'SUCCESS', 'FAILURE', 'NOT_PROVIDED' and 'NOT_VALIDATED        .
            http(str): http query parameter. HTTP status for the IP during the job run. Available values are
                'SUCCESS', 'FAILURE', 'NOT_PROVIDED' and 'NOT_VALIDATED        .
            netconf(str): netconf query parameter. Netconf status for the IP during the job run. Available values
                are 'SUCCESS', 'FAILURE', 'NOT_PROVIDED' and 'NOT_VALIDATED       .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!count-the-number-of-discovered-network-devices-by-discovery-id
        """
        check_type(headers, dict)
        check_type(management_ip_address, str)
        check_type(reachability_status, str)
        check_type(ping, str)
        check_type(cli, str)
        check_type(snmp, str)
        check_type(http, str)
        check_type(netconf, str)
        check_type(discovery_id, str, may_be_none=False)
        check_type(job_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "managementIpAddress": management_ip_address,
            "reachabilityStatus": reachability_status,
            "ping": ping,
            "cli": cli,
            "snmp": snmp,
            "http": http,
            "netconf": netconf,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "discoveryId": discovery_id,
            "jobId": job_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/discoverys/{discoveryId}/jobs/{jobId}"
            + "/discoveredNetworkDevices/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ccb8d17550e3a75aa606aeee6ed3_v3_2_3_0", json_data
        )

    def poe_interface_details(
        self, device_uuid, interface_name_list=None, headers=None, **request_parameters
    ):
        """Returns POE interface details for the device, where deviceuuid is mandatory & accepts comma seperated interface
        names which is optional and returns information for that particular interfaces where(operStatus =
        operationalStatus).

        Args:
            device_uuid(str): deviceUuid path parameter. uuid of the device.
            interface_name_list(str): interfaceNameList query parameter. comma seperated interface names.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!returns-p-o-e-interface-details-for-the-device
        """
        check_type(headers, dict)
        check_type(interface_name_list, str)
        check_type(device_uuid, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "interfaceNameList": interface_name_list,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceUuid": device_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/network-" + "device/{deviceUuid}/interface/poe-detail"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ab3215d9be065533b7cbbc978cb4d905_v3_2_3_0", json_data
        )

    def retrieves_the_statistics_of_a_given_wireless_controller(
        self,
        id,
        attribute=None,
        end_time=None,
        start_time=None,
        view=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the statistics of a given Wireless Controller. If startTime and endTime are not provided, the API
        defaults to the last 24 hours.

        Args:
            id(str): id path parameter. The WLC device UUID.
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            view(list, set, str, tuple): view query parameter. WLC Stats related Views Refer to WlcStatsView schema
                for list of views supported Examples: `view=ClientBandCounts` (single view requested)
                `view=clientAssociationCounts&view=clientStateCounts` (multiple view requested) .
            attribute(list, set, str, tuple): attribute query parameter. List of attributes related to resource that
                can be requested to only be part of the response along with the required attributes.
                Refer to WlcStatsAttribute schema for list of attributes supported Examples:
                `attribute=totalClientCount` (single attribute requested)
                `attribute=totalClientCount&attribute=clientRoamCounts` (multiple attribute requested).
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-statistics-of-a-given-wireless-controller
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(view, (list, set, str, tuple))
        check_type(attribute, (list, set, str, tuple))
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "view": view,
            "attribute": attribute,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/wirelessControllersStats/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d9bac3a3a638531b864aa43dd788911e_v3_2_3_0", json_data
        )

    def gets_the_total_number_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions(
        self,
        endTime=None,
        filters=None,
        startTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Gets the total number Network Devices based on the provided complex filters and aggregation functions. For
        detailed information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-AssuranceNetworkDevices-2.0.1-resolved.yaml.

        Args:
            endTime(integer): Devices's endTime.
            filters(list): Devices's filters (list of objects).
            startTime(integer): Devices's startTime.
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
            https://developer.cisco.com/docs/dna-center/#!gets-the-total-number-network-devices-based-on-the-provided-complex-filters-and-aggregation-functions
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
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
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d05c763ada545fbe94a4c0391456b89f_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/networkDevices/query/count"
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
            "bpm_d05c763ada545fbe94a4c0391456b89f_v3_2_3_0", json_data
        )

    def retrieves_the_process_kpis_for_a_given_process_of_wireless_controller(
        self,
        id,
        network_device_id,
        end_time=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the Process KPIs for a given process of wireless controller. If startTime and endTime are not
        provided, the API defaults to the last 24 hours.

        Args:
            network_device_id(str): networkDeviceId path parameter. Network Device UUID.
            id(str): id path parameter. Process Name.
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-process-k-p-is-for-a-given-process-of-wireless-controller
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(network_device_id, str, may_be_none=False)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/data/api/v1/networkDevices/{networkDeviceId}/proces" + "sKpis/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fe79e951dc8d9fac0d5672924b_v3_2_3_0", json_data
        )

    def creates_a_wired_capture_for_preview(
        self,
        metadata=None,
        previewDescription=None,
        wiredCaptureSettings=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Creates a wired capture session for preview prior to deploying the configurations on to the switch device. This
        is currently available for only 1 switch at a time.

        Args:
            metadata(object): Devices's Additional metadata for the request.
            previewDescription(string): Devices's The wired capture session's preview-deploy description string.
            wiredCaptureSettings(list): Devices's A list of wired capture session intents parameters that will be
                applied to switch (list of objects).
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
            https://developer.cisco.com/docs/dna-center/#!creates-a-wired-capture-for-preview
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "wiredCaptureSettings": wiredCaptureSettings,
            "previewDescription": previewDescription,
            "metadata": metadata,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_fc806e8386155aeb81be175778bc4773_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/capture/wired/configurationModels"
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
            "bpm_fc806e8386155aeb81be175778bc4773_v3_2_3_0", json_data
        )

    def count_devices_energy_from_query(
        self,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        page=None,
        startTime=None,
        views=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Retrieves the total count of network devices based on the specified complex filters. For detailed information
        about the usage of the API, please refer to the Open API specification document
        - https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-deviceEnergy_1.0-1.0.1-resolved.yaml.  Retrieves the total
        count of network devices based on the specified complex filters. The request payload format is similar
        to that used with the query API.

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's attributes (list of strings).
            endTime(integer): Devices's endTime.
            filters(list): Devices's filters (list of objects).
            page(object): Devices's page.
            startTime(integer): Devices's startTime.
            views(list): Devices's views (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!count-devices-energy-from-query
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
            "views": views,
            "attributes": attributes,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_fcd7200871e5e2db7f1720d95fee764_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/energy/networkDevices/query/count"
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
            "bpm_fcd7200871e5e2db7f1720d95fee764_v3_2_3_0", json_data
        )

    def retrieves_the_total_number_of_aaa_services_for_given_parameters(
        self,
        device_id=None,
        device_name=None,
        device_site_hierarchy=None,
        device_site_hierarchy_id=None,
        device_site_id=None,
        end_time=None,
        server_ip=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the total number of AAA Services for given parameters. For detailed information about the usage of the
        API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        AAAServices-1.0.0-resolved.yaml.   Retrieves the total number of AAA Services for given parameters. If
        startTime and endTime are not provided, the API defaults to the last 24 hours.

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            server_ip(str): serverIp query parameter. IP Address of the AAA Server. This parameter supports wildcard
                (`*`) character -based search. Example: `10.76.81.*` or `*56.78*` or `*50.28` Examples:
                serverIp=10.42.3.31 (single IP Address is requested)
                serverIp=10.42.3.31&serverIp=name2&fabricVnName=name3 (multiple IP Addresses are
                requested) .
            device_id(str): deviceId query parameter. The device UUID.  Examples:
                `deviceId=6bef213c-19ca-4170-8375-b694e251101c` (single deviceId is requested)  `deviceI
                d=6bef213c-19ca-4170-8375-b694e251101c&deviceId=32219612-819e-4b5e-a96b-cf22aca13dd9
                (multiple networkDeviceIds with & separator) .
            device_name(str): deviceName query parameter. Name of the device. This parameter supports wildcard (`*`)
                character -based search. Example: `wnbu-sjc*` or `*wnbu-sjc*` or `*wnbu-sjc` Examples:
                deviceName=wnbu-sjc24.cisco.com (single device name is requested) deviceName=wnbu-
                sjc24.cisco.com&deviceName=wnbu-sjc22.cisco.com (multiple device names are requested)
                .
            device_site_hierarchy(str): deviceSiteHierarchy query parameter. The full hierarchical breakdown of the
                site tree starting from Global site name and ending with the specific site name. The
                Root site is named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`) This field
                supports wildcard asterisk (`*`) character search support. E.g. `*/San*, */San, /San*`
                Examples: `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy
                requested) `?deviceSiteHierarchy=Global/AreaName/BuildingName/FloorName&deviceSiteHierar
                chy=Global/AreaName2/BuildingName2/FloorName2` (multiple siteHierarchies requested) .
            device_site_hierarchy_id(str): deviceSiteHierarchyId query parameter. The full hierarchy breakdown of
                the site tree in id form starting from Global site UUID and ending with the specific
                site UUID. (Ex. `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports
                wildcard asterisk (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?deviceSiteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single
                siteHierarchyId requested) `?deviceSiteHierarchyId=globalUuid/areaUuid/buildingUuid/floo
                rUuid&deviceSiteHierarchyId=globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple
                siteHierarchyIds requested) .
            device_site_id(str): deviceSiteId query parameter. The UUID of the site. (Ex. `flooruuid`) Examples:
                `?deviceSiteIds=id1` (single id requested)
                `?deviceSiteIds=id1&deviceSiteIds=id2&siteId=id3` (multiple ids requested) .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-total-number-of-a-a-a-services-for-given-parameters
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(server_ip, str)
        check_type(device_id, str)
        check_type(device_name, str)
        check_type(device_site_hierarchy, str)
        check_type(device_site_hierarchy_id, str)
        check_type(device_site_id, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "serverIp": server_ip,
            "deviceId": device_id,
            "deviceName": device_name,
            "deviceSiteHierarchy": device_site_hierarchy,
            "deviceSiteHierarchyId": device_site_hierarchy_id,
            "deviceSiteId": device_site_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/aaaServices/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dd9685e1250c69fcc71fa7f766750_v3_2_3_0", json_data
        )

    def get_device_energy_by_id(
        self,
        id,
        attribute=None,
        end_time=None,
        start_time=None,
        view=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves network device energy data for a specified time range based on the device ID. For detailed information
        about the usage of the API, please refer to the Open API specification document
        - https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-deviceEnergy_1.0-1.0.1-resolved.yaml.  Retrieves network
        device energy data for a specified time range based on the device ID. Returns the latest available
        snapshot of energy data between the provided start and end times. If no start and end times are
        specified, it defaults to returning the latest available energy data for the past 24 hours.

        Args:
            id(str): id path parameter. The UUID of the Network Device. (Ex.
                "6bef213c-19ca-4170-8375-b694e251101c").
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to one day before `endTime`.
                .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. If
                `endTime` is not provided, API will default to one day after `startTime`. If `startTime`
                is not provided either, API will default to current time. .
            view(str): view query parameter. List of views. View and attribute work in union. Each view will include
                its attributes. For example, view device includes all the attributes related to device.
                Please refer to `NetworkDeviceEnergyView` model for supported list of views Examples:
                `view=device&view=energy` .
            attribute(str): attribute query parameter. List of attributes. Please refer to
                `NetworkDeviceEnergyAttribute` for supported list of attributes     Examples:
                `attribute=id&attribute=energyConsumed` .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-device-energy-by-i-d
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(view, str)
        check_type(attribute, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "view": view,
            "attribute": attribute,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/energy/networkDevices/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f69049b5d6255ec68609f804c58c1bcb_v3_2_3_0", json_data
        )

    def retrieves_the_list_of_dns_services_for_given_set_of_complex_filters(
        self,
        endTime=None,
        filters=None,
        page=None,
        startTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Retrieves the list of DNS Services and offers complex filtering and sorting capabilities. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-DNSServices-1.0.0-resolved.yaml.   Retrieves the list of DNS
        Services and offers complex filtering and sorting capabilities. If startTime and endTime are not
        provided, the API defaults to the last 24 hours. The data in the response is calculated for the given
        time range. Field Name Description startTime start time from which API queries the data set related to
        the resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive & the default
        is latest endTime end time to which API queries the data set related to the resource. It must be
        specified in UNIX epochtime in milliseconds. Value is inclusive & the default is latest filters used to
        define one or more conditions. Only the data that satisfy these conditions will be taken into
        consideration during the calculation. page contains  limit, offset and sortBy  fields.  limit  Number of
        records to be returned in response,  offset  starting offset of data and  sortBy  attribute name, order
        to sort.

        Args:
            endTime(integer): Devices's endTime.
            filters(list): Devices's filters (list of objects).
            page(object): Devices's page.
            startTime(integer): Devices's startTime.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-d-n-s-services-for-given-set-of-complex-filters
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
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_af7031cc5ca5b44af0e6454d558412c_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/dnsServices/query"
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
            "bpm_af7031cc5ca5b44af0e6454d558412c_v3_2_3_0", json_data
        )

    def get_interface_by_ip(self, ip_address, headers=None, **request_parameters):
        """Returns list of interfaces for specified device management IP address.

        Args:
            ip_address(str): ipAddress path parameter. IP address of the interface.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-interface-by-i-p
        """
        check_type(headers, dict)
        check_type(ip_address, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "ipAddress": ip_address,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/interface/ip-address/{ipAddress}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cf7fa95e3ed4527aa5ba8ca871a8c142_v3_2_3_0", json_data
        )

    def update_health_score_definitions(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Update health thresholds, include status of overall health status for each metric.  And also to synchronize with
        global profile issue thresholds of the definition for given metric. For detailed information about the
        usage of the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        issueAndHealthDefinitions-1.0.0-resolved.yaml.   OpenAPI specification defined to Update health
        thresholds, include status of overall health status for each metric and also to synchronize with global
        profile issue thresholds of the definition for given metric.     API Support Documentation   The
        supported attributes of payload defined in  'HealthScoreDefinition'.

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(list): A JSON serializable Python object to send in the
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
            https://developer.cisco.com/docs/dna-center/#!update-health-score-definitions
        """
        check_type(headers, dict)
        check_type(payload, list)
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
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_b08f499f995f5f46ba52e0385b54721a_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/healthScoreDefinitions/bulkUpdate"
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
            "bpm_b08f499f995f5f46ba52e0385b54721a_v3_2_3_0", json_data
        )

    def count_the_number_of_events_with_filters(
        self,
        deviceFamily=None,
        endTime=None,
        filters=None,
        startTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """API to fetch the count of assurance events for the given complex query. Please refer to the 'API Support
        Documentation' section to understand which fields are supported. For detailed information about the
        usage of the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        AssuranceEvents-1.0.0-resolved.yaml.   OpenAPI specification defined to fetch the count of assurance
        events using complex filters present in Catalyst Center API Support Documentation Note that querying of
        data spanning more than 7 days is not allowed, so difference between startTime and endTime must not be
        more than that. The input payload contains the following fields: deviceFamily  Supported values:
        Switches and Hubs, Routers, Wireless Controller, Third Party Device, Unified AP, Wired Client, and
        Wireless Client This is a mandatory field. Please note that multiple families across network device type
        and client type is not allowed.  For example, choosing 'Routers' along with 'Wireless Client' or
        'Unified AP' is not supported.   startTime Start time from which API queries the data set related to the
        resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive.  If 'startTime' is
        not provided, API will default to current time minus 24 hours. endTime End time to which API queries the
        data set related to the resource. It must be specified in UNIX epochtime in milliseconds. Value is
        inclusive.  If 'endTime' is not provided, API will default to current time. filters  Used to define one
        or more filter conditions. Only the data that satisfy these conditions will be taken into consideration
        during the aggregation calculation. The supported list of filters in defined in 'EventsFilterObj'.

        Args:
            deviceFamily(list): Devices's deviceFamily (list of strings).
            endTime(integer): Devices's endTime.
            filters(list): Devices's filters (list of objects).
            startTime(integer): Devices's startTime.
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
            https://developer.cisco.com/docs/dna-center/#!count-the-number-of-events-with-filters
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
            "deviceFamily": deviceFamily,
            "startTime": startTime,
            "endTime": endTime,
            "filters": filters,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a91eed12dfc85dbdaacab22e6e9f04a5_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/assuranceEvents/query/count"
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
            "bpm_a91eed12dfc85dbdaacab22e6e9f04a5_v3_2_3_0", json_data
        )

    def get_device_by_serial_number(
        self, serial_number, headers=None, **request_parameters
    ):
        """Returns the network device with given serial number.

        Args:
            serial_number(str): serialNumber path parameter. Device serial number.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-device-by-serial-number
        """
        check_type(headers, dict)
        check_type(serial_number, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "serialNumber": serial_number,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/serial-" + "number/{serialNumber}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c53d56c282e5f108c659009d21f9d26_v3_2_3_0", json_data
        )

    def get_the_details_of_physical_components_of_the_given_device(
        self, device_uuid, type=None, headers=None, **request_parameters
    ):
        """Return all types of equipment details like PowerSupply, Fan, Chassis, Backplane, Module, PROCESSOR, Other and
        SFP for the Given device.

        Args:
            device_uuid(str): deviceUuid path parameter.
            type(str): type query parameter. Type value can be PowerSupply, Fan, Chassis, Backplane, Module,
                PROCESSOR, Other, SFP. If no type is mentioned, All equipments are fetched for the
                device.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-the-details-of-physical-components-of-the-given-device
        """
        check_type(headers, dict)
        check_type(type, str)
        check_type(device_uuid, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "type": type,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceUuid": device_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/{deviceUuid}/equipment"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c1cb24a2b53ce8d29d119c6ee1112_v3_2_3_0", json_data
        )

    def retrieves_the_details_of_a_specific_aaa_service_matching_the_id_of_the_service(
        self, id, end_time=None, start_time=None, headers=None, **request_parameters
    ):
        """Retrieves the details of the AAA Service matching the given id. For detailed information about the usage of the
        API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        AAAServices-1.0.0-resolved.yaml.   Retrieves the details of the AAA Service matching the given id. If
        startTime and endTime are not provided, the API defaults to the last 24 hours. The data in the response
        is from the given time range. Transaction fields are summed up and latncy fields are averaged. It
        returns transaction and latency data for the two phases of the authentication process 1) EAP Extensible
        Authentication Protocol 2) MAB MAC Authentication Bypass.

        Args:
            id(str): id path parameter. Unique id of the AAA Service. It is the combination of AAA Server IP
                (`serverIp`) and Device UUID (`deviceId`) separated by underscore (`_`). Example: If
                `serverIp` is `10.76.81.33` and `deviceId` is `6bef213c-19ca-4170-8375-b694e251101c`,
                then the `id` would be `10.76.81.33_6bef213c-19ca-4170-8375-b694e251101c` .
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-details-of-a-specific-a-a-a-service-matching-the-id-of-the-service
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/aaaServices/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory("bpm_a5f075784aa6b582aa9a24901_v3_2_3_0", json_data)

    def fetches_all_the_discovery_job_details_by_discovery_id(
        self,
        id,
        job_id=None,
        limit=None,
        offset=None,
        order_by=None,
        headers=None,
        **request_parameters
    ):
        """API to get all the discovery job details by discovery id. A discovery can have multiple discovery jobs, created
        against the same discovery id.

        Args:
            id(str): id path parameter. The id of the discovery.
            job_id(list, set, str, tuple): jobId query parameter. Optional list of the discovery job ids to filter
                by.
            limit(int): limit query parameter. The number of records to show for this page.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1.
            order_by(str): orderBy query parameter. To fetch the latest discovery job.  use the orderBy query
                parameter with values such as startTime or endTime. By default, jobs are ordered by
                startTime in descending order to display the most recent entries first.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!fetches-all-the-discovery-job-details-by-discovery-id
        """
        check_type(headers, dict)
        check_type(job_id, (list, set, str, tuple))
        check_type(limit, int)
        check_type(offset, int)
        check_type(order_by, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "jobId": job_id,
            "limit": limit,
            "offset": offset,
            "orderBy": order_by,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/discoverys/{id}/jobs"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_faf4d312916c5aa6b23caccaf2f60d2c_v3_2_3_0", json_data
        )

    def starts_the_existing_discovery(self, id, headers=None, **request_parameters):
        """This API starts a discovery job using the given discovery id. The response includes a task `url` that provides
        access to the task's details.  By accessing this URL, users will receive a response containing a
        `resultLocation` attribute, which provides  details of the discovery job that was started, including the
        `jobId`. A new discovery job is created every time this API is triggered.

        Args:
            id(str): id path parameter. The id of the discovery.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!starts-the-existing-discovery
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/discoverys/{id}/jobs"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ca023ebd45bc4a916050fc418dd7f_v3_2_3_0", json_data
        )

    def clear_mac_address_table(
        self,
        interface_uuid,
        deployment_mode=None,
        operation=None,
        payload_=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Clear mac-address on an individual port. In request body, operation needs to be specified as 'ClearMacAddress'.
        In the future more possible operations will be added to this API.

        Args:
            operation(string): Devices's Operation needs to be specified as 'ClearMacAddress'.
            payload_: Part of the JSON serializable Python object to send in the body of the Request.
            interface_uuid(str): interfaceUuid path parameter. Interface Id.
            deployment_mode(str): deploymentMode query parameter. Preview/Deploy ['Preview' means the configuration
                is not pushed to the device. 'Deploy' makes the configuration pushed to the device].
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
            https://developer.cisco.com/docs/dna-center/#!clear-mac-address-table
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(deployment_mode, str)
        check_type(interface_uuid, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deploymentMode": deployment_mode,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "interfaceUuid": interface_uuid,
        }
        _payload = {
            "operation": operation,
            "payload": payload_,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e702d5786552992aa76b930780569_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/interface/{interfaceUuid}/operation"
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
            "bpm_e702d5786552992aa76b930780569_v3_2_3_0", json_data
        )

    def get_polling_interval_for_all_devices(self, headers=None, **request_parameters):
        """Returns polling interval of all devices.

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-polling-interval-for-all-devices
        """
        check_type(headers, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/collection-" + "schedule/global"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ce94ab18ad505e8a9846f6c4c9df0d2b_v3_2_3_0", json_data
        )

    def update_global_resync_interval(
        self,
        interval=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Updates the resync interval (in minutes) globally for devices which do not have custom resync interval. To
        override this setting for all network devices refer to
        [/networkDevices/resyncIntervalSettings/override].

        Args:
            interval(integer): Devices's Resync Interval should be between 360 to 1440 minutes.
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
            https://developer.cisco.com/docs/dna-center/#!update-global-resync-interval
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "interval": interval,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a64bd4956649de3a61e10f0637e_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDevices/resyncIntervalSettings"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_a64bd4956649de3a61e10f0637e_v3_2_3_0", json_data
        )

    def get_device_interface_count(self, headers=None, **request_parameters):
        """Returns the count of interfaces for all devices.

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-device-interface-count-for-multiple-devices
        """
        check_type(headers, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/interface/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_da44fbc3e415a99aac0bdd291e9a87a_v3_2_3_0", json_data
        )

    def get_the_filter_group_associations(
        self,
        entity_id=None,
        entity_type=None,
        filter_group_id=None,
        headers=None,
        **request_parameters
    ):
        """Returns the details of associations for the given parameters.

        Args:
            filter_group_id(list, set, str, tuple): filterGroupId query parameter. Filter Group id. Examples:
                `?filterGroupId=2ee1b9f0-8036-443b-bad0-7692760af1b5`(single id requested) `?filterGroup
                Id=2ee1b9f0-8036-443b-bad0-7692760af1b5&filterGroupId=ae368f0b-f4e3-4e8f-a914-
                011cbd19bb51` (multiple ids requested) .
            entity_id(list, set, str, tuple): entityId query parameter. Entity id with which the filter group is
                associated. Examples: `?entityId=2ee1b9f0-8036-443b-bad0-7692760af1b5`(single id
                requested) `?entityId=2ee1b9f0-8036-443b-bad0-7692760af1b5&entityId=ae368f0b-f4e3-4e8f-
                a914-011cbd19bb51` (multiple ids requested) .
            entity_type(list, set, str, tuple): entityType query parameter. Type of the entity with which the filter
                group is associated. Examples: `?entityType=Issue Settings`(single type requested)
                `?entityType=Custom Dashboard&entityType=Issue Settings` (multiple types requested) .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-the-filter-group-associations
        """
        check_type(headers, dict)
        check_type(filter_group_id, (list, set, str, tuple))
        check_type(entity_id, (list, set, str, tuple))
        check_type(entity_type, (list, set, str, tuple))
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "filterGroupId": filter_group_id,
            "entityId": entity_id,
            "entityType": entity_type,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/filterGroupAssociations"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c44db9c3340579198ce6b231439d6bd_v3_2_3_0", json_data
        )

    def create_filter_group_association(
        self,
        entityId=None,
        entityName=None,
        entityType=None,
        filterGroupId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Creates association between a filter group and entity.

        Args:
            entityId(string): Devices's Entity id with which the Filter Group is associated.
            entityName(string): Devices's Entity name with which the Filter Group is associated.
            entityType(string): Devices's The type of the entity with which the Filter Group is associated.
            filterGroupId(string): Devices's Filter Group id.
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
            https://developer.cisco.com/docs/dna-center/#!create-filter-group-association
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "filterGroupId": filterGroupId,
            "entityId": entityId,
            "entityName": entityName,
            "entityType": entityType,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_bc35f54af11e5b83a81c25927d1a10b5_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/filterGroupAssociations"
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
            "bpm_bc35f54af11e5b83a81c25927d1a10b5_v3_2_3_0", json_data
        )

    def retrieves_the_details_of_a_specific_dhcp_service_matching_the_id_of_the_service(
        self, id, end_time=None, start_time=None, headers=None, **request_parameters
    ):
        """Retrieves the details of the DHCP Service matching the given id. For detailed information about the usage of the
        API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        DHCPServices-1.0.0-resolved.yaml.   Retrieves the details of the DHCP Service matching the given id. If
        startTime and endTime are not provided, the API defaults to the last 24 hours. The data in the response
        is from latest available snapshot in the given time range.

        Args:
            id(str): id path parameter. Unique id of the DHCP Service. It is the combination of DHCP Server IP
                (`serverIp`) and Device UUID (`deviceId`) separated by underscore (`_`). Example: If
                `serverIp` is `10.76.81.33` and `deviceId` is `6bef213c-19ca-4170-8375-b694e251101c`,
                then the `id` would be `10.76.81.33_6bef213c-19ca-4170-8375-b694e251101c` .
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-details-of-a-specific-d-h-c-p-service-matching-the-id-of-the-service
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/dhcpServices/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b5e7fa71240f5e669c902db27de09860_v3_2_3_0", json_data
        )

    def retrieves_the_total_number_of_dns_services_for_given_parameters(
        self,
        device_id=None,
        device_site_hierarchy_id=None,
        device_site_id=None,
        end_time=None,
        server_ip=None,
        ssid=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the total number of DNS Services for given parameters. For detailed information about the usage of the
        API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        DNSServices-1.0.0-resolved.yaml.   Retrieves the total number of DNS Services for given parameters. If
        startTime and endTime are not provided, the API defaults to the last 24 hours.

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            server_ip(str): serverIp query parameter. IP Address of the DNS Server. This parameter supports wildcard
                (`*`) character -based search. Example: `10.76.81.*` or `*56.78*` or `*50.28` Examples:
                serverIp=10.42.3.31 (single IP Address is requested)
                serverIp=10.42.3.31&serverIp=name2&fabricVnName=name3 (multiple IP Addresses are
                requested) .
            device_id(str): deviceId query parameter. The device UUID.  Examples:
                `deviceId=6bef213c-19ca-4170-8375-b694e251101c` (single deviceId is requested)  `deviceI
                d=6bef213c-19ca-4170-8375-b694e251101c&deviceId=32219612-819e-4b5e-a96b-cf22aca13dd9
                (multiple networkDeviceIds with & separator) .
            device_site_hierarchy_id(str): deviceSiteHierarchyId query parameter. The full hierarchy breakdown of
                the site tree in id form starting from Global site UUID and ending with the specific
                site UUID. (Ex. `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports
                wildcard asterisk (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?deviceSiteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single
                siteHierarchyId requested) `?deviceSiteHierarchyId=globalUuid/areaUuid/buildingUuid/floo
                rUuid&deviceSiteHierarchyId=globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple
                siteHierarchyIds requested) .
            device_site_id(str): deviceSiteId query parameter. The UUID of the site. (Ex. `flooruuid`) Examples:
                `?deviceSiteIds=id1` (single id requested)
                `?deviceSiteIds=id1&deviceSiteIds=id2&siteId=id3` (multiple ids requested) .
            ssid(str): ssid query parameter. SSID is the name of wireless network to which client connects to. It is
                also referred to as WLAN ID Wireless Local Area Network Identifier. This field supports
                wildcard (`*`) character-based search. If the field contains the (`*`) character, please
                use the /query API for search.  Ex: `*Alpha*` or `Alpha*` or `*Alpha` Examples:
                `ssid=Alpha` (single ssid requested) `ssid=Alpha&ssid=Guest` (multiple ssid requested) .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-total-number-of-d-n-s-services-for-given-parameters
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(server_ip, str)
        check_type(device_id, str)
        check_type(device_site_hierarchy_id, str)
        check_type(device_site_id, str)
        check_type(ssid, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "serverIp": server_ip,
            "deviceId": device_id,
            "deviceSiteHierarchyId": device_site_hierarchy_id,
            "deviceSiteId": device_site_id,
            "ssid": ssid,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/dnsServices/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory("bpm_b1b7509cb0f7dc3d0a04479f_v3_2_3_0", json_data)

    def count_the_number_of_events(
        self,
        device_family,
        ap_mac=None,
        client_mac=None,
        end_time=None,
        message_type=None,
        network_device_id=None,
        network_device_name=None,
        severity=None,
        site_hierarchy_id=None,
        site_id=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """API to fetch the count of assurance events that match the filter criteria. Please refer to the 'API Support
        Documentation' section to understand which fields are supported. For detailed information about the
        usage of the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        AssuranceEvents-1.0.0-resolved.yaml.   OpenAPI specification defined to fetch the count of assurance
        events using basic filters present in Catalyst Center   API Support Documentation   Note that querying
        of data spanning more than 7 days is not allowed, so difference between startTime and endTime must not
        be more than that.   Query Parameters:   deviceFamily    Supported values: Switches and Hubs, Routers,
        Wireless Controller, Third Party Device, Unified AP, Wired Client, and  Wireless Client   Please note
        that multiple families across network device type and client type is not allowed.       For example,
        choosing 'Routers' along with 'Wireless Client' or 'Unified AP' is not supported.      Examples :
        ?deviceFamily=Switches and Hubs (single deviceFamily requested)     ?deviceFamily=Switches and
        Hubs&deviceFamily=Routers (multiple deviceFamily requested)   startTime   Start time from which API
        queries the data set related to the resource. It must be specified in UNIX epochtime in milliseconds.
        Value is inclusive.    If 'startTime' is not provided, API will default to current time minus 24 hours.
        endTime   End time to which API queries the data set related to the resource. It must be specified in
        UNIX epochtime in milliseconds. Value is inclusive.    If 'endTime' is not provided, API will default to
        current time.   messageType   Message type for the event.    Supported values: Syslog, Trap, Device,
        Device Controller, ISE and TDL      Examples :      ?messageType=Syslog (single messageType requested)
        ?messageType=Trap&messageType=Syslog (multiple messageType requested)   severity   Severity of the event
        between 0 and 6. This is applicable only for events related to network devices (other than AP) and
        'Wired Client' events.     Examples :      ?severity=0 (single severity requested)
        ?severity=0&severity=1 (multiple severity requested)   siteId     The UUID of the site. Ex:flooruuid
        Examples :      ?siteId=uuiid1 (single siteId requested)     ?siteId=uuid2&siteId=uuid3 (multiple siteId
        requested)   siteHierarchyId     The full hierarchy breakdown of the site tree in id form starting from
        Global site UUID and ending with the specific site UUID. Ex: globalUuid/areaUuid/buildingUuid/floorUuid
        This field supports wildcard ('*') character-based search. Ex: *uuid* or uuid* or *uuid     Examples :
        ?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid (single siteHierarchyId requested)     ?site
        HierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=globalUuid/areaUuid2/buildingUuid
        2/floorUuid2 (multiple siteHierarchyId requested)   networkDeviceName   Network device name. This
        parameter is applicable for network device related families.    This field supports wildcard ('*')
        character-based search. Ex: *Branch* or Branch* or *Branch      Examples :
        ?networkDeviceName=Branch-3-Gateway (single networkDeviceName requested)
        ?networkDeviceName=Branch-3-Gateway&networkDeviceName=Branch-3-Switch (multiple networkDeviceName
        requested)   networkDeviceId     The Network Device Uuids. Ex: 6bef213c-19ca-4170-8375-b694e251101c
        Examples :      ?networkDeviceId=6bef213c-19ca-4170-8375-b694e251101c (single networkDeviceId requested)
        ?networkDeviceId=6bef213c-19ca-4170-8375-b694e251101c&networkDeviceId=2541e9a7-b80d-4955-8aa2-
        79b233318ba0 (multiple networkDeviceId requested)   apMac   MAC address of the access point. This
        parameter is applicable for 'Unified AP' and 'Wireless Client' events.    This field supports wildcard
        ('*') character-based search. Ex: *50:0F* or 50:0F* or *50:0F     Examples :
        ?apMac=50:0F:80:0F:F7:E0 (single apMac requested)     ?apMac=50:0F:80:0F:F7:E0&apMac=18:80:90:AB:7E:A0
        (multiple apMac requested)   clientMac   MAC address of the client. This parameter is applicable for
        'Wired Client' and 'Wireless Client' events.    This field supports wildcard ('*') character-based
        search. Ex: *66:2B* or 66:2B* or *66:2B     Examples :      ?clientMac=66:2B:B8:D2:01:56 (single
        clientMac requested)     ?clientMac=66:2B:B8:D2:01:56&clientMac=DC:A6:32:F5:5A:89 (multiple clientMac
        requested).

        Args:
            device_family(str): deviceFamily query parameter. Device family. Please note that multiple families
                across network device type and client type is not allowed. For example, choosing
                `Routers` along with `Wireless Client` or `Unified AP` is not supported. Examples:
                `deviceFamily=Switches and Hubs` (single deviceFamily requested) `deviceFamily=Switches
                and Hubs&deviceFamily=Routers` (multiple deviceFamily requested) .
            start_time(str): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to current time minus 24
                hours. .
            end_time(str): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. If
                `endTime` is not provided, API will default to current time. .
            message_type(str): messageType query parameter. Message type for the event. Examples:
                `messageType=Syslog` (single messageType requested)
                `messageType=Trap&messageType=Syslog` (multiple messageType requested) .
            severity(str): severity query parameter. Severity of the event between 0 and 6. This is applicable only
                for events related to network devices (other than AP) and `Wired Client` events. (Value:
                Severity),  (0: Emergency),  (1: Alert),  (2: Critical),  (3: Error),  (4: Warning),
                (5: Notice),  (6: Info),  Examples: `severity=0` (single severity requested)
                `severity=0&severity=1` (multiple severity requested) .
            site_id(str): siteId query parameter. The UUID of the site. (Ex. `flooruuid`) Examples: `?siteId=id1`
                (single siteId requested) `?siteId=id1&siteId=id2&siteId=id3` (multiple siteId
                requested) .
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site tree
                in id form starting from Global site UUID and ending with the specific site UUID. (Ex.
                `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk
                (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyId requested) .
            network_device_name(str): networkDeviceName query parameter. Network device name. This parameter is
                applicable for network device related families. This field supports wildcard (`*`)
                character-based search. Ex: `*Branch*` or `Branch*` or `*Branch` Examples:
                `networkDeviceName=Branch-3-Gateway` (single networkDeviceName requested)
                `networkDeviceName=Branch-3-Gateway&networkDeviceName=Branch-3-Switch` (multiple
                networkDeviceName requested) .
            network_device_id(str): networkDeviceId query parameter. The list of Network Device Uuids. (Ex.
                `6bef213c-19ca-4170-8375-b694e251101c`) Examples:
                `networkDeviceId=6bef213c-19ca-4170-8375-b694e251101c` (single networkDeviceId
                requested) `networkDeviceId=6bef213c-19ca-4170-8375-
                b694e251101c&networkDeviceId=32219612-819e-4b5e-a96b-
                cf22aca13dd9&networkDeviceId=2541e9a7-b80d-4955-8aa2-79b233318ba0` (multiple
                networkDeviceId requested) .
            ap_mac(str): apMac query parameter. MAC address of the access point. This parameter is applicable for
                `Unified AP` and `Wireless Client` events. This field supports wildcard (`*`) character-
                based search. Ex: `*50:0F*` or `50:0F*` or `*50:0F` Examples: `apMac=50:0F:80:0F:F7:E0`
                (single apMac requested) `apMac=50:0F:80:0F:F7:E0&apMac=18:80:90:AB:7E:A0` (multiple
                apMac requested) .
            client_mac(str): clientMac query parameter. MAC address of the client. This parameter is applicable for
                `Wired Client` and `Wireless Client` events. This field supports wildcard (`*`)
                character-based search. Ex: `*66:2B*` or `66:2B*` or `*66:2B` Examples:
                `clientMac=66:2B:B8:D2:01:56` (single clientMac requested)
                `clientMac=66:2B:B8:D2:01:56&clientMac=DC:A6:32:F5:5A:89` (multiple clientMac requested)
                .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!count-the-number-of-events
        """
        check_type(headers, dict)
        check_type(device_family, str, may_be_none=False)
        check_type(start_time, str)
        check_type(end_time, str)
        check_type(message_type, str)
        check_type(severity, str)
        check_type(site_id, str)
        check_type(site_hierarchy_id, str)
        check_type(network_device_name, str)
        check_type(network_device_id, str)
        check_type(ap_mac, str)
        check_type(client_mac, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deviceFamily": device_family,
            "startTime": start_time,
            "endTime": end_time,
            "messageType": message_type,
            "severity": severity,
            "siteId": site_id,
            "siteHierarchyId": site_hierarchy_id,
            "networkDeviceName": network_device_name,
            "networkDeviceId": network_device_id,
            "apMac": ap_mac,
            "clientMac": client_mac,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/assuranceEvents/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_abf597583520eb0a7a0b24e5c7f69_v3_2_3_0", json_data
        )

    def count_devices_energy(
        self,
        device_category=None,
        device_sub_category=None,
        end_time=None,
        id=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the total count of network devices that provide energy data, filtered according to the specified query
        parameters. For detailed information about the usage of the API, please refer to the Open API
        specification document - https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-deviceEnergy_1.0-1.0.1-resolved.yaml.  Retrieves the total
        count of network devices that provide energy data, filtered according to the specified query parameters.

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to one day before `endTime`.
                .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. If
                `endTime` is not provided, API will default to one day after `startTime`. If `startTime`
                is not provided either, API will default to current time. .
            id(str): id query parameter. The list of Device Uuids (e.g., `6bef213c-19ca-4170-8375-b694e251101c`).
                Examples: `id=6bef213c-19ca-4170-8375-b694e251101c` (single device requested)
                `id=6bef213c-19ca-4170-8375-b694e251101c&id=32219612-819e-4b5e-a96b-cf22aca13dd9` .
            site_id(str): siteId query parameter. The UUID of the site. (Ex. `flooruuid`) Examples: `?siteId=id1`
                (single id requested) `?siteId=id1&siteId=id2&siteId=id3` (multiple ids requested) .
            site_hierarchy(str): siteHierarchy query parameter. The full hierarchical breakdown of the site tree
                starting from Global site name and ending with the specific site name. The Root site is
                named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`) This field supports
                wildcard asterisk (`*`) character search support. E.g. `*/San*, */San, /San*` Examples:
                `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy requested)
                `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global/AreaName2/Bu
                ildingName2/FloorName2` (multiple siteHierarchies requested) .
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site tree
                in id form starting from Global site UUID and ending with the specific site UUID. (Ex.
                `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk
                (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds requested) .
            device_category(str): deviceCategory query parameter. The list of device deviceCategories.  Examples:
                `deviceCategory=Switch` (single device family requested)
                `deviceCategory=Switch&deviceCategory=Router` (multiple device categories with comma
                separator) .
            device_sub_category(str): deviceSubCategory query parameter. The list of device sub categories.
                Examples: `deviceSubCategory=Cisco Catalyst 9300 Series Switches` (single device family
                requested) `deviceSubCategory=Cisco Catalyst 9300 Series
                Switches&deviceSubCategory=Cisco Catalyst 9400 Series Switches` .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!count-devices-energy
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(id, str)
        check_type(site_id, str)
        check_type(site_hierarchy, str)
        check_type(site_hierarchy_id, str)
        check_type(device_category, str)
        check_type(device_sub_category, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "id": id,
            "siteId": site_id,
            "siteHierarchy": site_hierarchy,
            "siteHierarchyId": site_hierarchy_id,
            "deviceCategory": device_category,
            "deviceSubCategory": device_sub_category,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/energy/networkDevices/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d220b1f9a1530fad206800cf7a946f_v3_2_3_0", json_data
        )

    def get_linecard_details(self, device_uuid, headers=None, **request_parameters):
        """Get line card detail for a given deviceuuid.  Response will contain serial no, part no, switch no and slot no.

        Args:
            device_uuid(str): deviceUuid path parameter. instanceuuid of device.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-linecard-details
        """
        check_type(headers, dict)
        check_type(device_uuid, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceUuid": device_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/{deviceUuid}/line-card"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bd31690b61f45d9f880d74d4e682b070_v3_2_3_0", json_data
        )

    def devices(
        self,
        device_role=None,
        end_time=None,
        health=None,
        limit=None,
        offset=None,
        site_id=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Intent API for accessing DNA Assurance Device object for generating reports, creating dashboards or creating
        additional value added services.

        Args:
            device_role(str): deviceRole query parameter. CORE, ACCESS, DISTRIBUTION, ROUTER, WLC, or AP (case
                insensitive).
            site_id(str): siteId query parameter. DNAC site UUID.
            health(str): health query parameter. DNAC health catagory: POOR, FAIR, or GOOD (case insensitive).
            start_time(int): startTime query parameter. UTC epoch time in milliseconds.
            end_time(int): endTime query parameter. UTC epoch time in milliseconds.
            limit(int): limit query parameter. Max number of device entries in the response (default to 50. Max at
                500).
            offset(int): offset query parameter. The offset of the first device in the returned data (Mutiple of
                'limit' + 1).
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!devices
        """
        check_type(headers, dict)
        check_type(device_role, str)
        check_type(site_id, str)
        check_type(health, str)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(limit, int)
        check_type(offset, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deviceRole": device_role,
            "siteId": site_id,
            "health": health,
            "startTime": start_time,
            "endTime": end_time,
            "limit": limit,
            "offset": offset,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/device-health"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c75e364632e15384a18063458e2ba0e3_v3_2_3_0", json_data
        )

    def retrieves_the_total_number_of_dhcp_services_for_given_set_of_complex_filters(
        self,
        endTime=None,
        filters=None,
        startTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Retrieves the total number of DHCP Services and offers complex filtering and sorting capabilities. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-DHCPServices-1.0.0-resolved.yaml.   Retrieves the total
        number of DHCP Services and offers complex filtering and sorting capabilities. If startTime and endTime
        are not provided, the API defaults to the last 24 hours. Field Name Description startTime start time
        from which API queries the data set related to the resource. It must be specified in UNIX epochtime in
        milliseconds. Value is inclusive & the default is latest endTime end time to which API queries the data
        set related to the resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive
        & the default is latest filters used to define one or more conditions. Only the data that satisfy these
        conditions will be taken into consideration during the aggregation calculation.

        Args:
            endTime(integer): Devices's endTime.
            filters(list): Devices's filters (list of objects).
            startTime(integer): Devices's startTime.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-total-number-of-d-h-c-p-services-for-given-set-of-complex-filters
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
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_afcd4a0cbe985fd7aafa73d671c43a1e_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/dhcpServices/query/count"
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
            "bpm_afcd4a0cbe985fd7aafa73d671c43a1e_v3_2_3_0", json_data
        )

    def sync_devices_using_forcesync(
        self,
        force_sync=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Synchronizes the devices. If forceSync param is false (default) then the sync would run in normal priority
        thread. If forceSync param is true then the sync would run in high priority thread if available, else
        the sync will fail. Result can be seen in the child task of each device.

        Args:
            force_sync(bool): forceSync query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(list): A JSON serializable Python object to send in the
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
            https://developer.cisco.com/docs/dna-center/#!sync-devices
        """
        check_type(headers, dict)
        check_type(payload, list)
        check_type(force_sync, bool)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "forceSync": force_sync,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_f2c120b855cb8c852806ce72e54d_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/sync"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_f2c120b855cb8c852806ce72e54d_v3_2_3_0", json_data
        )

    def delete_network_device_with_configuration_cleanup(
        self,
        id=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API endpoint facilitates the deletion of a network device after performing configuration cleanup on the
        device.  This API endpoint facilitates the deletion of a network device after performing configuration
        cleanup on the device.

        Args:
            id(string): Devices's The unique identifier of the network device to be deleted.
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
            https://developer.cisco.com/docs/dna-center/#!delete-network-device-with-configuration-cleanup
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "id": id,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a18e761ac8592e9a5c4e0bb2308cf0_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDevices/deleteWithCleanup"
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
            "bpm_a18e761ac8592e9a5c4e0bb2308cf0_v3_2_3_0", json_data
        )

    def retrieves_wired_capture_session_count(
        self, capture_status, headers=None, **request_parameters
    ):
        """Retrieves the count of wired capture sessions that have been deployed (in-progress), completed, or scheduled.

        Args:
            capture_status(str): captureStatus query parameter. Catalyst Center wired capture configuration status.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-wired-capture-session-count
        """
        check_type(headers, dict)
        check_type(capture_status, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "captureStatus": capture_status,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/capture/wired/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d48d3d208ebd5f3ab48ab6a3a23d2aaa_v3_2_3_0", json_data
        )

    def gets_the_total_network_device_interface_counts_in_the_specified_time_range_when_there_is_no_start_and_end_time_specified_returns_the_latest_interfaces_total_count(
        self,
        end_time=None,
        interface_id=None,
        interface_name=None,
        network_device_id=None,
        network_device_ip_address=None,
        network_device_mac_address=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Gets the total Network device interface counts. For detailed information about the usage of the API, please
        refer to the Open API specification document https://github.com/cisco-en-programmability/catalyst-
        center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-interfaces-2.0.0-resolved.yaml.

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to current time. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            site_hierarchy(str): siteHierarchy query parameter. The full hierarchical breakdown of the site tree
                starting from Global site name and ending with the specific site name. The Root site is
                named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`) This field supports
                wildcard asterisk (`*`) character search support. E.g. `*/San*, */San, /San*` Examples:
                `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy requested)
                `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global/AreaName2/Bu
                ildingName2/FloorName2` (multiple siteHierarchies requested) .
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site tree
                in id form starting from Global site UUID and ending with the specific site UUID. (Ex.
                `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk
                (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds requested) .
            site_id(str): siteId query parameter. The UUID of the site. (Ex. `flooruuid`) Examples: `?siteId=id1`
                (single id requested) `?siteId=id1&siteId=id2&siteId=id3` (multiple ids requested) .
            network_device_id(str): networkDeviceId query parameter. The list of Network Device Uuids. (Ex.
                `6bef213c-19ca-4170-8375-b694e251101c`) Examples:
                `networkDeviceId=6bef213c-19ca-4170-8375-b694e251101c` (single networkDeviceId
                requested) `networkDeviceId=6bef213c-19ca-4170-8375-
                b694e251101c&networkDeviceId=32219612-819e-4b5e-a96b-
                cf22aca13dd9&networkDeviceId=2541e9a7-b80d-4955-8aa2-79b233318ba0` (multiple
                networkDeviceIds with & separator) .
            network_device_ip_address(str): networkDeviceIpAddress query parameter. The list of Network Device
                management IP Address. (Ex. `121.1.1.10`) This field supports wildcard (`*`) character-
                based search.  Ex: `*1.1*` or `1.1*` or `*1.1` Examples:
                `networkDeviceIpAddress=121.1.1.10` `networkDeviceIpAddress=121.1.1.10&networkDeviceIpAd
                dress=172.20.1.10&networkDeviceIpAddress=10.10.20.10` (multiple networkDevice IP Address
                with & separator) .
            network_device_mac_address(str): networkDeviceMacAddress query parameter. The list of Network Device MAC
                Address. (Ex. `64:f6:9d:07:9a:00`) This field supports wildcard (`*`) character-based
                search.  Ex: `*AB:AB:AB*` or `AB:AB:AB*` or `*AB:AB:AB` Examples:
                `networkDeviceMacAddress=64:f6:9d:07:9a:00`
                `networkDeviceMacAddress=64:f6:9d:07:9a:00&networkDeviceMacAddress=70:56:9d:07:ac:77`
                (multiple networkDevice MAC addresses with & separator) .
            interface_id(str): interfaceId query parameter. The list of Interface Uuids. (Ex.
                `6bef213c-19ca-4170-8375-b694e251101c`) Examples:
                `interfaceId=6bef213c-19ca-4170-8375-b694e251101c` (single interface uuid ) `interfaceId
                =6bef213c-19ca-4170-8375-b694e251101c&32219612-819e-4b5e-a96b-cf22aca13dd9&2541e9a7-
                b80d-4955-8aa2-79b233318ba0` (multiple Interface uuid with & separator) .
            interface_name(str): interfaceName query parameter. The list of Interface name (Ex.
                `GigabitEthernet1/0/1`) This field supports wildcard (`*`) character-based search.  Ex:
                `*1/0/1*` or `1/0/1*` or `*1/0/1` Examples: `interfaceNames=GigabitEthernet1/0/1`
                (single interface name)
                `interfaceNames=GigabitEthernet1/0/1&GigabitEthernet2/0/1&GigabitEthernet3/0/1`
                (multiple interface names with & separator) .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!gets-the-total-network-device-interface-counts-in-the-specified-time-range-when-there-is-no-start-and-end-time-specified-returns-the-latest-interfaces-total-count
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(site_hierarchy, str)
        check_type(site_hierarchy_id, str)
        check_type(site_id, str)
        check_type(network_device_id, str)
        check_type(network_device_ip_address, str)
        check_type(network_device_mac_address, str)
        check_type(interface_id, str)
        check_type(interface_name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "siteHierarchy": site_hierarchy,
            "siteHierarchyId": site_hierarchy_id,
            "siteId": site_id,
            "networkDeviceId": network_device_id,
            "networkDeviceIpAddress": network_device_ip_address,
            "networkDeviceMacAddress": network_device_mac_address,
            "interfaceId": interface_id,
            "interfaceName": interface_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/interfaces/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory("bpm_0f4b503bbce76ebb802f0ad7_v3_2_3_0", json_data)

    def override_resync_interval(self, headers=None, **request_parameters):
        """Overrides the global resync interval on all network devices. This essentially removes device specific intervals
        if set.

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!override-resync-interval
        """
        check_type(headers, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDevices/resyncIntervalSettings" + "/override"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dc239a9ab9e5562b93a45ea0b9708b84_v3_2_3_0", json_data
        )

    def gets_the_list_of_interfaces_across_the_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions(
        self,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        page=None,
        startTime=None,
        views=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Gets the list of interfaces across the Network Devices based on the provided complex filters and aggregation
        functions  The elements are grouped and sorted by deviceUuid first, and are then sorted by the given
        sort field, or by the default value: name.  The supported sorting options are: name, adminStatus,
        description, duplexConfig, duplexOper, interfaceIfIndex,interfaceType, macAddress,mediaType, operStatus,
        portChannelId, portMode, portType,speed, vlanId,pdPowerAdminMaxInWatt,pdPowerBudgetInWatt,pdPowerConsume
        dInWatt,pdPowerRemainingInWatt,pdMaxPowerDrawn. For detailed information about the usage of the API,
        please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        interfaces-2.0.0-resolved.yaml.   How the filtering behavior works   The filters field in each post body
        can be used in numerous ways:   Each filter in the list of filters will applied ''together''   In the
        example below, this would request filtering to retrieve FullDuplex interfaces  and  portMode either
        trunk or access.   "filters" : [     {        "key" :  "duplexOper" ,        "operator" :  "eq" ,
        "value" :  "FullDuplex"      },     {        "key" :  "portMode" ,        "operator" :  "in" ,
        "value" : [          "trunk" ,          "access"        ]     } ]  Each filter object can contrastingly
        utilize its  logical operator  to provide nested filtering functionality.   In the example below you can
        see a logical "OR" filter being applied using the nested filtering functionality:   The primary filter
        object does not have its 'key', 'value', or 'operator' fields populated. Only the 'logicalOperator'
        field is populated, to indicate the filters within the nested filters list are to be logically
        conjoined.   "filters" : [     {        "logicalOperator" :  "or" ,        "filters" : [         {
        "key" :  "siteName" ,            "operator" :  "like".

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's attributes (list of strings).
            endTime(integer): Devices's endTime.
            filters(list): Devices's filters (list of objects).
            page(object): Devices's page.
            startTime(integer): Devices's startTime.
            views(list): Devices's views (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!gets-the-list-of-interfaces-across-the-network-devices-based-on-the-provided-complex-filters-and-aggregation-functions
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "startTime": startTime,
            "endTime": endTime,
            "views": views,
            "attributes": attributes,
            "filters": filters,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f667322836d5527482ad2100bec7feb4_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/interfaces/query"
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
            "bpm_f667322836d5527482ad2100bec7feb4_v3_2_3_0", json_data
        )

    def inventory_insight_device_link_mismatch(
        self,
        category,
        site_id,
        limit=None,
        offset=None,
        order=None,
        sort_by=None,
        headers=None,
        **request_parameters
    ):
        """Find all devices with link mismatch (speed /  vlan).

        Args:
            site_id(str): siteId path parameter.
            offset(int): offset query parameter. Row Number.  Default value is 1.
            limit(int): limit query parameter. The number of records to show for this page. Min: 1, Max: 500.
            category(str): category query parameter. Links mismatch category.  Value can be speed-duplex or vlan.
            sort_by(str): sortBy query parameter. Sort By.
            order(str): order query parameter. Order.  Value can be asc or desc.  Default value is asc.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!inventory-insight-device-link-mismatch-a-p-i
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(category, str, may_be_none=False)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(site_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "offset": offset,
            "limit": limit,
            "category": category,
            "sortBy": sort_by,
            "order": order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "siteId": site_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-" + "device/insight/{siteId}/device-link"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_eed1595442b757bf94938c858a257ced_v3_2_3_0", json_data
        )

    def get_the_count_of_health_score_definitions_based_on_provided_filters(
        self,
        device_type=None,
        id=None,
        include_for_overall_health=None,
        headers=None,
        **request_parameters
    ):
        """Get the count of health score definitions based on provided filters. Supported filters are id, name and overall
        health include status. For detailed information about the usage of the API, please refer to the Open API
        specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-issueAndHealthDefinitions-1.0.0-resolved.yaml.   OpenAPI
        specification defined to get the count of health score definitions based on provided filters. Supported
        filters are id, name and overall health include status.   API Support Documentation   Query Parameters:
        deviceType   These are the device families/types supported for system issue definitions. If no input is
        made on device type, all device types are considered.    Supported values: ROUTER, SWITCH_AND_HUB,
        WIRELESS_CONTROLLER, UNIFIED_AP, WIRELESS_CLIENT, WIRED_CLIENT     Example :     ?deviceType=ROUTER   id
        The definition identifier.     Examples :     ?id=015d9cba-4f53-4087-8317-7e49e5ffef46 (single id
        requested)    ?id=T015d9cba-4f53-4087-8317-7e49e5ffef46&id=015d9cba-4f53-4087-8317-7e49e5ffef47
        (multiple id requested)   includeForOverallHealth   The inclusion status of the issue definition, either
        true or false. true indicates that particular health metric is included in overall health computation,
        otherwise false. By default it's set to true.     Example :     ?includeForOverallHealth=true.

        Args:
            device_type(str): deviceType query parameter. These are the device families supported for health score
                definitions. If no input is made on device family, all device families are considered.
            id(str): id query parameter. The definition identifier. Examples:
                id=015d9cba-4f53-4087-8317-7e49e5ffef46 (single entity id request)
                id=015d9cba-4f53-4087-8317-7e49e5ffef46&id=015d9cba-4f53-4087-8317-7e49e5ffef47
                (multiple ids in the query param) .
            include_for_overall_health(bool): includeForOverallHealth query parameter. The inclusion status of the
                issue definition, either true or false. true indicates that particular health metric is
                included in overall health computation, otherwise false. By default it's set to true.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-the-count-of-health-score-definitions-based-on-provided-filters
        """
        check_type(headers, dict)
        check_type(device_type, str)
        check_type(id, str)
        check_type(include_for_overall_health, bool)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deviceType": device_type,
            "id": id,
            "includeForOverallHealth": include_for_overall_health,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/healthScoreDefinitions/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d7eefccfc590dae32a123469f9fe3_v3_2_3_0", json_data
        )

    def retrieves_the_list_of_wireless_controllers_statistics_while_also_supporting_aggregate_attributes(
        self,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        page=None,
        startTime=None,
        views=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Retrieves the list of Wireless Controllers' statistics while also supporting aggregate attributes. If startTime
        and endTime are not provided, the API defaults to the last 24 hours.  **The input payload contains the
        following fields,** |Field Name | Description | | --| --| | `startTime` | The start time indicates when
        the API begins retrieving data related to the resource. It must be specified in the UNIX epoch time
        format, measured in milliseconds. This value is inclusive, and if left unspecified, the default is 1 day
        before the endTime. | | `endTime` | The end time indicates the upper limit until which the API retrieves
        data related to the resource. It must be defined in the UNIX epoch time format, measured in
        milliseconds. This value is inclusive, and if left unspecified, the default is the latest available
        data. | | `attributes` | A list of attributes associated with the resource, which can be requested to be
        included in the response alongside the required attributes. Refer to `WlcStatsAttribute` model for the
        supported attributes | | `aggregateAttributes` | This specifies the attribute name and the function to
        be applied during data querying. The aggregate function is then applied to data within the specified
        start and end times. Refer to `WlcStatsAggregateField` model for the supported aggregate attributes |
        |`filters`| This is used to specify one or more conditions for filtering the queried data. Refer to
        `WlcStatsFilterField` model for the supported filters | |`page`| It includes the **limit, offset, and
        sortBy** fields. *limit* denotes the number of records to retrieve per page, *offset* signifies the
        initial data position, and *sortBy* is used to sort the response based on the sortBy fields. It contains
        the attribute name, order, and optional function for sorting by the aggregated field. Refer to
        `WlcStatsSortByField` model for the supported sortBy names.|.

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's attributes (list of strings. Available values are 'id', 'name',
                'siteHierarchy', 'siteHierarchyId', 'lastUpdatedTime', '24ghzClients', '5ghzClients',
                '6ghzClients', 'totalClientCount', 'assocAttempts', 'assocFailures', 'assocRespAccepts',
                'assocRespRejects', 'assocRespErrors', 'startAttempts', 'associationAttempts',
                'localAuthAttempts', 'l2AuthAttempts', 'l2AuthFailures', 'mabAttempts', 'mabFailures',
                'ipLearnAttempts', 'ipLearnFailures', 'l3AuthAttempts', 'l3AuthFailures',
                'sessionPushAttempts', 'sessionPushFailures', 'runAttempts', 'deletedAttempts', 'roams',
                'cckmRoams', 'dot11rRoams', 'dot11iFastRoams', 'dot11iSlowRoams', 'failedRoams',
                'mdnsTxPackets', 'mdnsRxPackets', 'mdnsDropPackets', 'l2Roams', 'l3Roams',
                'interWncdRoams', 'hwDropsCapwapControl', 'hwDropsCapwapData', 'hwDropsmobilityControl',
                'hwDropsmobilityData', 'hwDropsIpGlean', 'hwDropsIpSg', 'hwDropsIpLearn',
                'hwDropsL2Bridging', 'hwDropsClientUidb', 'hwDropsClientNotFound', 'hwDropsP2PBlock',
                'swDropsCapwapControl', 'swDropsCapwapData', 'swDropsmobilityControl',
                'swDropsmobilityData', 'swDropsIpGlean', 'swDropsIpSg', 'swDropsIpLearn',
                'swDropsL2Bridging', 'swDropsClientUidb', 'swDropsClientNotFound', 'swDropsP2PBlock',
                'puntCapwapControl', 'puntCapwapData', 'puntmobilityControl', 'puntmobilityData',
                'puntDot11IAPP', 'puntDot11RRM', 'puntDot11Dot1x', 'puntWebAuth',
                'puntDot11ProbeRequest', 'puntDot11Rfid', 'puntDot11Mgmt', 'puntCapwapKeepAlive',
                'puntMobilityKeepAlive', 'puntArp', 'puntDhcp', 'puntDhcp6', 'puntIpv6Nd',
                'puntDataGlean', 'puntDataGlean6', 'puntDhcpRelay', 'txBytes', 'rxBytes', 'txPackets',
                'rxPackets', 'txErrorPackets', 'rxErrorPackets', 'txErrorPercentage' and
                'rxErrorPercentage').
            endTime(integer): Devices's End time to which the API queries the dataset related to the resource. It
                must be specified in terms of milliseconds since UNIX epoch. Value is inclusive.
            filters(list): Devices's filters (list of objects).
            page(object): Devices's page.
            startTime(integer): Devices's Start time from which the API queries the dataset related to the resource.
                It must be specified in terms of milliseconds since UNIX epoch. Value is inclusive.
            views(list): Devices's views (list of strings. Available values are 'ClientBandCounts',
                'ClientAssociationCounts', 'ClientStateCounts', 'ClientRoamCounts', 'MdnsStats',
                'MobilityStats', 'HardwareDrops', 'SoftwareDrops', 'PuntCounters' and 'TrafficStats').
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-wireless-controllers-statistics-while-also-supporting-aggregate-attributes
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
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
            "views": views,
            "attributes": attributes,
            "filters": filters,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_de67eccfefdd5bb7927d4f83c3133cae_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/wirelessControllersStats/query"
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
            "bpm_de67eccfefdd5bb7927d4f83c3133cae_v3_2_3_0", json_data
        )

    def get_interface_details(
        self, device_id, name, headers=None, **request_parameters
    ):
        """Returns interface by specified device Id and interface name.

        Args:
            device_id(str): deviceId path parameter. Device ID.
            name(str): name query parameter. Interface name.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-interface-details-by-device-id-and-interface-name
        """
        check_type(headers, dict)
        check_type(name, str, may_be_none=False)
        check_type(device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "name": name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceId": device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/interface/network-" + "device/{deviceId}/interface-name"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bef9e9b306085d879b877598fad71b51_v3_2_3_0", json_data
        )

    def retrieves_the_list_of_aaa_services_for_given_set_of_complex_filters(
        self,
        endTime=None,
        filters=None,
        page=None,
        startTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Retrieves the list of AAA Services and offers complex filtering and sorting capabilities. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-AAAServices-1.0.0-resolved.yaml.   Retrieves the list of AAA
        Services and offers complex filtering and sorting capabilities. If startTime and endTime are not
        provided, the API defaults to the last 24 hours. The data in the response is calculated for the given
        time range. Transaction fields are summed up and latncy fields are averaged. It returns transaction and
        latency data for the two phases of the authentication process 1) EAP Extensible Authentication Protocol
        2) MAB MAC Authentication Bypass Field Name Description startTime start time from which API queries the
        data set related to the resource. It must be specified in UNIX epochtime in milliseconds. Value is
        inclusive & the default is 24 hours ago from end time endTime end time to which API queries the data set
        related to the resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive &
        the default is current time filters used to define one or more conditions. Only the data that satisfy
        these conditions will be taken into consideration during the calculation. page contains  limit, offset
        and sortBy  fields.  limit  Number of records to be returned in response,  offset  starting offset of
        data and  sortBy  attribute name, order to sort.

        Args:
            endTime(integer): Devices's endTime.
            filters(list): Devices's filters (list of objects).
            page(object): Devices's page.
            startTime(integer): Devices's startTime.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-a-a-a-services-for-given-set-of-complex-filters
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
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator("jsd_f24a5ad5bf03fe236dd96dcb_v3_2_3_0").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/aaaServices/query"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory("bpm_f24a5ad5bf03fe236dd96dcb_v3_2_3_0", json_data)

    def creates_discovery(
        self,
        credentials=None,
        discoveryTypeDetails=None,
        id=None,
        managementIpSelectionMethod=None,
        name=None,
        onlyNewDevice=None,
        siteId=None,
        updateManagementIp=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API creates a discovery. The response includes a task `url` that provides access to the task's details.  By
        accessing this URL, users will receive a response containing a `resultLocation` attribute, which
        provides  details of the discovery settings that was created, including the discovery `id`.

        Args:
            credentials(object): Devices's Credentials to be used for discovering devices. If multiple credentials
                are provided, they will be prioritized based on specificity and protocol version.
                Device-specific credentials take precedence over global credentials. Among SNMP
                versions, SNMPv3 credentials are given higher priority over SNMPv2 credentials.
            discoveryTypeDetails(): Devices's Details of the discovery type.
            id(string): Devices's Unique identifier of the discovery settings.
            managementIpSelectionMethod(string): Devices's When Catalyst Center discovers a device, it uses one of
                the device's IP addresses as the preferred management IP address for the device. The IP
                address can be that of a built-in management interface of the device, another physical
                interface, or a logical interface like Loopback0. You can configure Catalyst Center to
                log the device's loopback IP address as the preferred management IP address, provided
                the IP address is reachable from Catalyst Center.  `DEFAULT`   * Uses the IP address
                provided in the discovery request as the management IP.  `LOOPBACK`   If you choose to
                use a device's loopback IP address as the preferred management IP address, Catalyst
                Center determines the preferred management IP address as follows:   * If the device has
                one loopback interface, that loopback interface IP address is used.   * If the device
                has multiple loopback interfaces, the loopback interface with the highest IP address is
                used.   * If there are no loopback interfaces, the Ethernet interface with the highest
                IP address is used. (Subinterface IP addresses are not considered.)   * If there are no
                Ethernet interfaces, the serial interface with the highest IP address is used.  example:
                LOOPBACK . Available values are 'DEFAULT' and 'LOOPBACK'.
            name(string): Devices's The name of the discovery job being created. This will be a unique name.
            onlyNewDevice(boolean): Devices's This flag indicates to discover only new devices that are not in
                inventory. If set to `true`, only devices that are not in the inventory will be
                discovered. If set to `false`, devices that already exist in the inventory will not be
                listed in the `discovered devices` list. .
            siteId(string): Devices's The site id to which the discovered devices will be assigned.
            updateManagementIp(boolean): Devices's This flag indicates if the management IP address of existing
                devices to be updated as part of this discovery.  If set false devices get discovered
                with the existing management IP address. If set true it overwrites the management IP
                address with the new IP address used in discovery.
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
            https://developer.cisco.com/docs/dna-center/#!creates-discovery
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "id": id,
            "name": name,
            "managementIpSelectionMethod": managementIpSelectionMethod,
            "discoveryTypeDetails": discoveryTypeDetails,
            "onlyNewDevice": onlyNewDevice,
            "updateManagementIp": updateManagementIp,
            "credentials": credentials,
            "siteId": siteId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d5ecdc670ebc5bae807f25a53d4e8b7f_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/discoverys"
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
            "bpm_d5ecdc670ebc5bae807f25a53d4e8b7f_v3_2_3_0", json_data
        )

    def fetches_all_discovery_details(
        self,
        id=None,
        limit=None,
        name=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """API to fetch the discovery details using basic filters.  **How the filtering behavior works**  Each filter item
        provided in the query parameters will be applied simultaneously such that the result is the `AND` of all
        the filter items.

        Args:
            id(list, set, str, tuple): id query parameter. Optional list of the discovery ids to filter by.
            name(str): name query parameter. Optional name of the discovery to filter by. This supports partial
                search. For example, searching for "Disc" will match "Discovery1", "Discovery2", etc.
            limit(int): limit query parameter. The number of records to show for this page.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!fetches-all-discovery-details
        """
        check_type(headers, dict)
        check_type(id, (list, set, str, tuple))
        check_type(name, str)
        check_type(limit, int)
        check_type(offset, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "name": name,
            "limit": limit,
            "offset": offset,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/discoverys"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e57f47555e32a607837eb83bf3c3_v3_2_3_0", json_data
        )

    def stops_the_existing_discovery(
        self, discovery_id, job_id, headers=None, **request_parameters
    ):
        """This API is to be used to stop an ongoing discovery job. After initiating discovery with the `POST
        /dna/intent/api/v1/discoverys/{id}/jobs` API, the response will contain a `jobId` that can be used to
        stop that particular discovery job.

        Args:
            discovery_id(str): discoveryId path parameter. The id of the discovery.
            job_id(str): jobId path parameter. The id of the discovery job.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!stops-the-existing-discovery
        """
        check_type(headers, dict)
        check_type(discovery_id, str, may_be_none=False)
        check_type(job_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "discoveryId": discovery_id,
            "jobId": job_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/discoverys/{discoveryId}/jobs/{jobId}" + "/stop"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bbd887834f58fab833d3194555514e_v3_2_3_0", json_data
        )

    def get_the_device_data_for_the_given_device_id_uuid(
        self,
        id,
        attribute=None,
        end_time=None,
        start_time=None,
        view=None,
        headers=None,
        **request_parameters
    ):
        """Returns the device data for the given device Uuid in the specified start and end time range. When there is no
        start and end time specified returns the latest available data for the given Id. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-AssuranceNetworkDevices-2.0.1-resolved.yaml.

        Args:
            id(str): id path parameter. The device Uuid.
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to current time. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            view(str): view query parameter. The List of Network Device model views. Please refer to
                ```NetworkDeviceView``` section in the Open API specification document mentioned in the
                description.
            attribute(str): attribute query parameter. The List of Network Device model attributes. Please refer to
                ```NetworkDeviceAttribute``` section in the Open API specification document mentioned in
                the description.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-the-device-data-for-the-given-device-id-uuid
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(view, str)
        check_type(attribute, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "view": view,
            "attribute": attribute,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/networkDevices/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f89c7ee84a615469b754add8feeabb5a_v3_2_3_0", json_data
        )

    def get_the_count_of_devices_that_support_wired_packet_capture_functional_capability(
        self, site_hierarchy_id, headers=None, **request_parameters
    ):
        """Returns the count of devices that support wired packet capture functional capability.

        Args:
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site tree
                in id form starting from Global site UUID and ending with the specific site UUID. (Ex.
                `globalUuid/areaUuid/buildingUuid/floorUuid`) This value can be obtained from the
                responses of APIs like `/dna/intent/api/v1/sites` or `intent/api/v1/areas/${id}` or
                `/dna/intent/api/v2/floors/${id}` or `dna/intent/api/v2/buildings/${id}` Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid` .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-the-count-of-devices-that-support-wired-packet-capture-functional-capability
        """
        check_type(headers, dict)
        check_type(site_hierarchy_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "siteHierarchyId": site_hierarchy_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/flowAnalysis/packetCapture/supportedD" + "evices/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bc076d2c3535afab79357622653c917_v3_2_3_0", json_data
        )

    def retrieves_the_maintenance_schedule_information(
        self, id, headers=None, **request_parameters
    ):
        """API to retrieve the maintenance schedule information for the given id.

        Args:
            id(str): id path parameter. Unique identifier for the maintenance schedule.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-maintenance-schedule-information
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDeviceMaintenanceSchedules/{id" + "}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ce5b6297263a50feb20e532932d39580_v3_2_3_0", json_data
        )

    def updates_the_maintenance_schedule_information(
        self,
        id,
        description=None,
        maintenanceSchedule=None,
        networkDeviceIds=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """API to update the maintenance schedule for the network devices.  The `maintenanceSchedule` can be updated only
        if the `status` value is `UPCOMING` or `IN_PROGRESS`. User can exit `IN_PROGRESS` maintenance window by
        setting the `endTime` to -1. This will update the endTime to the current time and exit the maintenance
        window immediately. When exiting the maintenance window, only the endTime will be updated while other
        parameters remain read-only. The description for the maintenance schedule cannot be updated.

        Args:
            description(string): Devices's A brief narrative describing the maintenance schedule.
            id(string): Devices's Id of the schedule maintenance window.
            maintenanceSchedule(object): Devices's Contains all the details necessary to define the maintenance
                window and its recurrence.
            networkDeviceIds(list): Devices's networkDeviceIds (list of strings).
            id(str): id path parameter. Unique identifier for the maintenance schedule.
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
            https://developer.cisco.com/docs/dna-center/#!updates-the-maintenance-schedule-information
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "id": id,
            "description": description,
            "maintenanceSchedule": maintenanceSchedule,
            "networkDeviceIds": networkDeviceIds,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e5bb87a955e33a7ee46f1085fd880_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDeviceMaintenanceSchedules/{id" + "}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_e5bb87a955e33a7ee46f1085fd880_v3_2_3_0", json_data
        )

    def delete_maintenance_schedule(self, id, headers=None, **request_parameters):
        """API to delete maintenance schedule by id. Deletion is allowed if the maintenance window is in the `UPCOMING`,
        `COMPLETED`, or `FAILED` state. Deletion of maintenance schedule is not allowed if the maintenance
        window is currently `IN_PROGRESS`. To delete the maintenance schedule while it is `IN_PROGRESS`, first
        exit the current maintenance window using `PUT
        /dna/intent/api/v1/networkDeviceMaintenanceSchedules/{id}` API, and then proceed to delete the
        maintenance schedule.

        Args:
            id(str): id path parameter. Unique identifier for the maintenance schedule.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!delete-maintenance-schedule
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDeviceMaintenanceSchedules/{id" + "}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ff24d0609c3514fbb7377f5dbd70d0a_v3_2_3_0", json_data
        )

    def get_devices_energy(
        self,
        attribute=None,
        cursor=None,
        device_category=None,
        device_sub_category=None,
        end_time=None,
        id=None,
        limit=None,
        order=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        sort_by=None,
        start_time=None,
        view=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves a list of network devices with energy data based on the specified query parameters. For detailed
        information about the usage of the API, please refer to the Open API specification document
        - https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-deviceEnergy_1.0-1.0.1-resolved.yaml.  Retrieves a list of
        network devices with energy data based on the specified query parameters. It returns the most recent
        snapshot of energy data within the provided start and end times. If no start and end times are
        specified, it defaults to returning the latest available energy data from the past 24 hours.

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to one day before `endTime`.
                .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. If
                `endTime` is not provided, API will default to one day after `startTime`. If `startTime`
                is not provided either, API will default to current time. .
            limit(int): limit query parameter. Maximum number of records to return.
            cursor(str): cursor query parameter. It's an opaque string field that indicates the next record in the
                requested collection. If no records remain, the API returns a response with a count of
                zero. The default value is an empty string, and the initial value must be an empty
                string. The cursor value is populated by the API in the response page block. If the user
                wants more records, the cursor in the subsequent request must be updated with the value
                from the previous response.
            sort_by(str): sortBy query parameter. A field within the response to sort by.
            order(str): order query parameter. The sort order of the field ascending or descending.
            id(str): id query parameter. The list of Device Uuids (e.g., `6bef213c-19ca-4170-8375-b694e251101c`).
                Examples: `id=6bef213c-19ca-4170-8375-b694e251101c` (single device requested)
                `id=6bef213c-19ca-4170-8375-b694e251101c&id=32219612-819e-4b5e-a96b-cf22aca13dd9` .
            site_id(str): siteId query parameter. The UUID of the site. (Ex. `flooruuid`) Examples: `?siteId=id1`
                (single id requested) `?siteId=id1&siteId=id2&siteId=id3` (multiple ids requested) .
            site_hierarchy(str): siteHierarchy query parameter. The full hierarchical breakdown of the site tree
                starting from Global site name and ending with the specific site name. The Root site is
                named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`) This field supports
                wildcard asterisk (`*`) character search support. E.g. `*/San*, */San, /San*` Examples:
                `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy requested)
                `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global/AreaName2/Bu
                ildingName2/FloorName2` (multiple siteHierarchies requested) .
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site tree
                in id form starting from Global site UUID and ending with the specific site UUID. (Ex.
                `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk
                (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds requested) .
            device_category(str): deviceCategory query parameter. The list of device deviceCategories.  Examples:
                `deviceCategory=Switch` (single device family requested)
                `deviceCategory=Switch&deviceCategory=Router` (multiple device categories with comma
                separator) .
            device_sub_category(str): deviceSubCategory query parameter. The list of device sub categories.
                Examples: `deviceSubCategory=Cisco Catalyst 9300 Series Switches` (single device family
                requested) `deviceSubCategory=Cisco Catalyst 9300 Series
                Switches&deviceSubCategory=Cisco Catalyst 9400 Series Switches` .
            view(str): view query parameter. List of views. View and attribute work in union. Each view will include
                its attributes. For example, view device includes all the attributes related to device.
                Please refer to `NetworkDeviceEnergyView` model for supported list of views Examples:
                `view=device&view=energy` .
            attribute(str): attribute query parameter. List of attributes. Please refer to
                `NetworkDeviceEnergyAttribute` for supported list of attributes     Examples:
                `attribute=id&attribute=energyConsumed` .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-devices-energy
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(limit, int)
        check_type(cursor, str)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(id, str)
        check_type(site_id, str)
        check_type(site_hierarchy, str)
        check_type(site_hierarchy_id, str)
        check_type(device_category, str)
        check_type(device_sub_category, str)
        check_type(view, str)
        check_type(attribute, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "limit": limit,
            "cursor": cursor,
            "sortBy": sort_by,
            "order": order,
            "id": id,
            "siteId": site_id,
            "siteHierarchy": site_hierarchy,
            "siteHierarchyId": site_hierarchy_id,
            "deviceCategory": device_category,
            "deviceSubCategory": device_sub_category,
            "view": view,
            "attribute": attribute,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/energy/networkDevices"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dd2b645f354b88c7b519cdbd5c4c4_v3_2_3_0", json_data
        )

    def retrieves_specific_process_kpis_for_a_process_in_wlc_over_a_specified_period_of_time(
        self,
        id,
        network_device_id,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        page=None,
        startTime=None,
        trendInterval=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Retrieves the time series process kpis of a specific process in WLC by applying complex filters, aggregate
        functions, and grouping. The data will be grouped based on the specified trend time interval. If
        startTime and endTime are not provided, the API defaults to the last 24 hours.  **The input payload
        contains the following fields,** |Field Name | Description | | --| --| | `startTime` | The start time
        indicates when the API begins retrieving data related to the resource. It must be specified in the UNIX
        epoch time format, measured in milliseconds. This value is inclusive, and if left unspecified, the
        default is 1 day before the endTime. | | `endTime` | The end time indicates the upper limit until which
        the API retrieves data related to the resource. It must be defined in the UNIX epoch time format,
        measured in milliseconds. This value is inclusive, and if left unspecified, the default is the latest
        available data. | | `trendInterval` |  The time window for aggregating metrics. This is a mandatory
        request field. Possible values include *5 minutes, 10 minutes, 1 hour, 1 day, or 7 days*. If the start
        and end time range exceeds 1 day, the trendInterval defaults to 1 hour.| | `groupBy` | Specifies the
        attributes for grouping the data. Refer to `ProcessKpisGroupByField` model for the supported grouping
        attributes| | `attributes` | A list of attributes associated with the resource, which can be requested
        to be included in the response alongside the required attributes. Refer to `ProcessKpisAttribute` model
        for the supported attributes | | `aggregateAttributes` | This specifies the attribute name and the
        function to be applied during data querying. The aggregate function is then applied to data within the
        specified start and end times. Refer to `ProcessKpisAggregateField` model for the supported aggregate
        attributes | |`filters`| This is used to specify one or more conditions for filtering the queried data.
        Refer to `ProcessKpisFilterField` model for the supported filters | |`page`| It includes the **limit,
        cursor, and timeSortOrder** fields. *limit* denotes the number of records to retrieve per page, *cursor*
        signifies the initial data position, and *timeSortOrder* is used sort the response based on the
        timestamp either in ascending or descending order. |.

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's attributes (list of strings. Available values are 'siteHierarchy',
                'siteHierarchyId', 'lastUpdatedTime', 'pid', 'name', 'totalRunTime', 'cpuPercentage',
                'memoryPercentage', 'memoryUsage' and 'apCount').
            endTime(integer): Devices's End time to which the API queries the dataset related to the resource. It
                must be specified in terms of milliseconds since UNIX epoch. Value is inclusive.
            filters(list): Devices's filters (list of objects).
            groupBy(list): Devices's groupBy (list of strings. Available values are 'name').
            page(object): Devices's page.
            startTime(integer): Devices's Start time from which the API queries the dataset related to the resource.
                It must be specified in terms of milliseconds since UNIX epoch. Value is inclusive.
            trendInterval(string): Devices's The time window to aggregate the metrics.  Interval can be 5 minutes or
                10 minutes or 1 hour or 1 day or 7 days . Available values are '5MIN', '10MIN', '1HR',
                '1DAY' and '7DAY'.
            network_device_id(str): networkDeviceId path parameter. Network Device UUID.
            id(str): id path parameter. Process Name.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-specific-process-kpis-for-a-process-in-w-l-c-over-a-specified-period-of-time
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(network_device_id, str, may_be_none=False)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
            "id": id,
        }
        _payload = {
            "startTime": startTime,
            "endTime": endTime,
            "trendInterval": trendInterval,
            "groupBy": groupBy,
            "attributes": attributes,
            "filters": filters,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_bf8f647193561a883e1d9b24d5a61d_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/data/api/v1/networkDevices/{networkDeviceId}/proces"
            + "sKpis/{id}/trendAnalytics"
        )
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
            "bpm_bf8f647193561a883e1d9b24d5a61d_v3_2_3_0", json_data
        )

    def retrieve_the_total_number_of_scheduled_maintenance_windows(
        self, network_device_ids=None, status=None, headers=None, **request_parameters
    ):
        """Retrieve the total count of all scheduled maintenance windows for network devices.

        Args:
            network_device_ids(list, set, str, tuple): networkDeviceIds query parameter. List of network device ids.
            status(str): status query parameter. The status of the maintenance schedule. Possible values are:
                `UPCOMING`: The maintenance is scheduled and pending execution.  `IN_PROGRESS`: The
                maintenance is currently in progress.   `COMPLETED`: The maintenance window has been
                fully completed (For recurring maintenance, this indicates completion of the most recent
                occurrence).  `FAILED`: Updating the device's management state was not successful. For
                more information on failure use `GET /dna/intent/api/v1/activities/{id}` API with
                `startId` and `endId` value. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-the-total-number-of-scheduled-maintenance-windows
        """
        check_type(headers, dict)
        check_type(network_device_ids, (list, set, str, tuple))
        check_type(status, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "networkDeviceIds": network_device_ids,
            "status": status,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDeviceMaintenanceSchedules/cou" + "nt"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c0a858b81cc65ae4b0eb0e69995b8e8c_v3_2_3_0", json_data
        )

    def get_summary_analytics_data_of_dns_services_for_given_set_of_complex_filters(
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
        """Gets the summary analytics data related to DNS Services based on given filters and group by field. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-DNSServices-1.0.0-resolved.yaml.   Gets the summary
        analytics data related to DNS Services based on given filters and group by field. If startTime and
        endTime are not provided, the API defaults to the last 24 hours. Field Name Description startTime start
        time from which API queries the data set related to the resource. It must be specified in UNIX epochtime
        in milliseconds. Value is inclusive & the default is latest endTime end time to which API queries the
        data set related to the resource. It must be specified in UNIX epochtime in milliseconds. Value is
        inclusive & the default is latest groupBy specifies the attributes for grouping the data. filters used
        to define one or more conditions. Only the data that satisfy these conditions will be taken into
        consideration during the aggregation calculation. attributes attributes are used for obtaining one or
        more field's data in addition to the aggregated data. The supported attributes are listed in
        DNSServicesAnalyticsAttributeKey  model aggregateAttributes specifies the names of the attributes on
        which the aggregate function should be applied when querying the data. The supported attribute names are
        listed in  DNSServicesAggregateAttributeKey  model page contains  limit, offset and sortBy  fields.
        limit  Number of records to be returned in response,  offset  starting offset of data and  sortBy
        attribute name, order to sort.

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's attributes (list of strings).
            endTime(integer): Devices's endTime.
            filters(list): Devices's filters (list of objects).
            groupBy(list): Devices's groupBy (list of strings).
            page(object): Devices's page.
            startTime(integer): Devices's startTime.
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
            https://developer.cisco.com/docs/dna-center/#!get-summary-analytics-data-of-d-n-s-services-for-given-set-of-complex-filters
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
            "groupBy": groupBy,
            "filters": filters,
            "attributes": attributes,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e9c5c3e5515a2e1b2cdee6928ab_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/dnsServices/summaryAnalytics"
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
            "bpm_e9c5c3e5515a2e1b2cdee6928ab_v3_2_3_0", json_data
        )

    def deploys_the_wired_capture_configuration_intent(
        self, preview_activity_id, headers=None, **request_parameters
    ):
        """Deploys the wired capture configurations to the switch device.   Generating of device's CLIs for preview-approve
        is not available for this activity ID after using this POST API.

        Args:
            preview_activity_id(str): previewActivityId path parameter. activity from the POST
                /deviceConfigugrationModels task response.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!deploys-the-wired-capture-configuration-intent
        """
        check_type(headers, dict)
        check_type(preview_activity_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "previewActivityId": preview_activity_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/capture/wired/configurationModels/{pr"
            + "eviewActivityId}/deploy"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f670389fdd5ce394b65f76b907a2b5_v3_2_3_0", json_data
        )

    def delete_planned_access_point_for_floor(
        self, floor_id, planned_access_point_uuid, headers=None, **request_parameters
    ):
        """Allow to delete a planned access point from an existing floor map including its planned radio and antenna
        details.  Use the Get variant of this API to fetch the existing planned access points for the floor.
        The instanceUUID listed in each of the planned access point attributes acts as the path param input to
        this API to delete that specific instance.  API to delete an existing planned access point from a floor
        map.

        Args:
            floor_id(str): floorId path parameter. The instance UUID of the floor hierarchy element.
            planned_access_point_uuid(str): plannedAccessPointUuid path parameter. The instance UUID of the planned
                access point to delete.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!delete-planned-access-point-for-floor
        """
        check_type(headers, dict)
        check_type(floor_id, str, may_be_none=False)
        check_type(planned_access_point_uuid, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "floorId": floor_id,
            "plannedAccessPointUuid": planned_access_point_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/floors/{floorId}/planned-access-"
            + "points/{plannedAccessPointUuid}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cb644669ab8d5955826d23197015e208_v3_2_3_0", json_data
        )

    def retrieves_the_total_count_of_processes_by_applying_basic_filtering(
        self,
        network_device_id,
        end_time=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the number of Processes by applying basic filtering. If startTime and endTime are not provided, the
        API defaults to the last 24 hours.

        Args:
            network_device_id(str): networkDeviceId path parameter. Network Device UUID.
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-total-count-of-processes-by-applying-basic-filtering
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/data/api/v1/networkDevices/{networkDeviceId}/proces" + "sKpis/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c2a71dc4f584ab4b8aca46bf267be_v3_2_3_0", json_data
        )

    def get_device_interface_stats_info(
        self,
        device_id,
        endTime=None,
        query=None,
        startTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API returns the Interface Stats for the given Device Id. Please refer to the Feature tab for the Request
        Body usage and the API filtering support.   This API is used to get the list of interface stats data for
        the given deviceId. The input Request Body contains the following fields: •  startTime and endTime : The
        UTC epoch timestamps in milliseconds that represent the time range of the query. The default time range
        is 30 minutes. •  query : Contains information about the following query parameters: fields : An array
        of strings representing the fields that must be included in response. An empty array returns all the
        fields in response. filters : An array of objects representing the filters that should be applied to the
        query result. The object contains the following attributes: key : A string representing the name of the
        field on which the filter should be applied. operator : A string representing the operator that must be
        used in the filter. Supported operators are “eq”, “in” and “contains”. Please refer the table below for
        more information about the supported operators in each field. value : The value of the field. page :
        Contains the pagination parameters for the query results: limit : An integer representing the maximum
        number of items to return per page. The maximum is 1000. offset : An integer representing the index of
        the first item to return in the response. The default value is 0. orderBy : An array of objects
        representing the fields to order the results by. The maximum supported orderBy element count is 1.
        name : Name of the field used for sorting. order : Represents the order of the sort. Possible values are
        “asc” and “desc”. An empty Request Body returns details of all the interfaces on the given device Id,
        the maximum interface in the response is 1000. Example: The below example provides all the interfaces
        for the given device with filters of "trunk" or "access" port mode and "fullDuplex" duplex operational
        status, and the response contains all the relevant fields. The maximum number of the records is 1000 and
        the offset is 0. {   "startTime": 1676922780000,   "endTime": 1677009180000,   "query": {     "fields":
        [],     "filters": [       {         "key": "duplexOper",         "operator": "eq",         "value":
        "FullDuplex"       },       {         "key": "portMode",         "operator": "in",         "value":
        ["trunk", "access"]       }     ],     "page": {       "limit": 1000,       "offset": 0,
        "orderBy": [         {           "name": "name",           "order": "asc"         }       ]     }   } }
        The supported "filter" interface field names and the respective supported operator details are given
        below:     Field name   Supported Operators   Remarks       name   in, eq, contains   The name of the
        interface       description   in, eq, contains   The interface description       adminStatus   in, eq
        The desired state of the interface. Values: NOT_APPLICABLE, UP, DOWN, TESTING & UNKNOWN       vlanId
        in, eq   The Interface VLAN Id       duplexConfig   in, eq   The interface duplex config status. Values:
        HalfDuplex, FullDuplex, Disagree, AutoNegotiate & UNKNOWN       duplexOper   in,eq   The interface
        duplex operational status. Values: HalfDuplex, FullDuplex, Disagree, AutoNegotiate & UNKNOWN
        interfaceId   in, eq   A unique identifier of the interface, IfIndex       interfaceType   in, eq   The
        interface is a Physical or Virtual type       isL3Interface   in,eq   Interface is L3 or not. Values:
        True or False       isWan   in,eq   Interface is a WAN Link or not. Values: True or False       macAddr
        in,eq   The Mac Address of the interface       mediaType   in,eq   The interface media type
        operStatus   in,eq   The current operational state of the interface. Values: NOT_APPLICABLE, UP, DOWN,
        TESTING, UNKNOWN, DORMANT, NOTPRESENT & LOWERLAYERDOWN       portChannelId   in,eq   The interface Port
        Channel Id       portMode   in,eq   The interface Port Mode. Values: access, trunk, routed, dynamic_auto
        and dynamic_desirable        portType   in,eq   The interface ifType       speed   in,eq   Speed of the
        Interface in Kbps      .

        Args:
            endTime(integer): Devices's UTC epoch timestamp in milliseconds.
            query(object): Devices's query.
            startTime(integer): Devices's UTC epoch timestamp in milliseconds.
            device_id(str): deviceId path parameter. Network Device Id.
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
            https://developer.cisco.com/docs/dna-center/#!get-device-interface-stats-info
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(device_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceId": device_id,
        }
        _payload = {
            "startTime": startTime,
            "endTime": endTime,
            "query": query,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a9e0722d184658c592bd130ff03e1dde_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v2/networkDevices/{deviceId}/interfaces/" + "query"
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
            "bpm_a9e0722d184658c592bd130ff03e1dde_v3_2_3_0", json_data
        )

    def get_device_interface_stats_info_v2(
        self,
        device_id,
        endTime=None,
        query=None,
        startTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **query_parameters
    ):
        """Alias for `get_device_interface_stats_info <#catalystcentersdk.
        api.v3_2_3_0.devices.
        Devices.get_device_interface_stats_info>`_
        """
        return self.get_device_interface_stats_info(
            device_id=device_id,
            endTime=endTime,
            query=query,
            startTime=startTime,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def retrieves_the_details_of_a_specific_dns_service_matching_the_id_of_the_service(
        self, id, end_time=None, start_time=None, headers=None, **request_parameters
    ):
        """Retrieves the details of the DNS Service matching the given id. For detailed information about the usage of the
        API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        DNSServices-1.0.0-resolved.yaml.   Retrieves the details of the DNS Service matching the given id. If
        startTime and endTime are not provided, the API defaults to the last 24 hours. The data in the response
        is from latest available snapshot in the given time range.

        Args:
            id(str): id path parameter. Unique id of the DNS Service. It is the combination of DNS Server IP
                (`serverIp`) and Device UUID (`deviceId`) separated by underscore (`_`). Example: If
                `serverIp` is `10.76.81.33` and `deviceId` is `6bef213c-19ca-4170-8375-b694e251101c`,
                then the `id` would be `10.76.81.33_6bef213c-19ca-4170-8375-b694e251101c` .
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-details-of-a-specific-d-n-s-service-matching-the-id-of-the-service
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/dnsServices/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d6e70722df04553c9806af12c6d097db_v3_2_3_0", json_data
        )

    def get_organization_list_for_meraki(self, id, headers=None, **request_parameters):
        """Returns list of organizations for meraki dashboard.

        Args:
            id(str): id path parameter. Device Id.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-organization-list-for-meraki
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/{id}/meraki-" + "organization"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b4ba6d23d5e7eb62cbba4c9e1a29d_v3_2_3_0", json_data
        )

    def legit_operations_for_interface(
        self, interface_uuid, headers=None, **request_parameters
    ):
        """Get list of all properties & operations valid for an interface.

        Args:
            interface_uuid(str): interfaceUuid path parameter. Interface ID.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!legit-operations-for-interface
        """
        check_type(headers, dict)
        check_type(interface_uuid, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "interfaceUuid": interface_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/interface/{interfaceUuid}/legit-" + "operation"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fe6d62edcec25921926043ca25f75bed_v3_2_3_0", json_data
        )

    def get_device_config_count(self, headers=None, **request_parameters):
        """Returns the count of device configs.

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-device-config-count
        """
        check_type(headers, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/config/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dc0a72537a3578ca31cc5ef29131d35_v3_2_3_0", json_data
        )

    def deploys_the_wired_capture_without_preview(
        self,
        deploymentOptions=None,
        metadata=None,
        previewDescription=None,
        wiredCaptureSettings=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Deploy the wired capture sessions to the switch device without preview-aprove. This is currently only available
        for only 1 switch at a time.

        Args:
            deploymentOptions(object): Devices's Additional deployment options.
            metadata(object): Devices's Additional metadata for the deployment.
            previewDescription(string): Devices's The wired capture session's preview-deploy description string.
            wiredCaptureSettings(list): Devices's A list of wired capture session intents parameters that will be
                applied to switch (list of objects).
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
            https://developer.cisco.com/docs/dna-center/#!deploys-the-wired-capture-without-preview
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "wiredCaptureSettings": wiredCaptureSettings,
            "previewDescription": previewDescription,
            "deploymentOptions": deploymentOptions,
            "metadata": metadata,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_cb1d0502a0265b38941cb97c5c23ac1a_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/capture/wired/deploy"
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
            "bpm_cb1d0502a0265b38941cb97c5c23ac1a_v3_2_3_0", json_data
        )

    def partially_updates_an_existing_network_device(
        self,
        id,
        category=None,
        credentials=None,
        managementAddress=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Updates specified fields of an existing network device. Only include the fields you wish to update. Omitted
        fields remain unchanged. To unset a field, explicitly set it to null.  If a different
        `managementIpAddress` is provided, the device will be updated with the new `managementIpAddress`.

        Args:
            category(string): Devices's Category of the device. Used to determine the type of the device being
                added.   | Category             | Description
                | Required Credentials | Optional Credentials |   | -------------------|
                --------------------------------------------------------------------------------------|
                -------------------| -------------------|   | `NETWORK_DEVICE`     | Standard Cisco
                network devices like switches, routers, controllers                      | CLI, SNMP
                | HTTP, Netconf        |   | `COMPUTE_DEVICE`     | Server or computing system
                manufactured by Cisco such as Unified Computing System (UCS) | HTTP                 |
                CLI, SNMP            |   | `THIRD_PARTY_DEVICE` | Non-Cisco network devices that support
                SNMP monitoring                                  | SNMP                 |
                |   | `MERAKI_DASHBOARD`   | Cisco Meraki cloud-managed devices accessed via Meraki
                Dashboard                        | Meraki               |                    |   |
                `FIREWALL_MANAGEMENT_CENTER`                | Cisco Secure Firewall Management Center
                (FMC)                                           | HTTP                 |
                | . Available values are 'NETWORK_DEVICE', 'COMPUTE_DEVICE', 'THIRD_PARTY_DEVICE',
                'MERAKI_DASHBOARD' and 'FIREWALL_MANAGEMENT_CENTER'.
            credentials(object): Devices's Credentials used to access the network device. .
            managementAddress(): Devices's Management address of the network device. For meraki dashboard, this is
                the dashboard URL.
            id(str): id path parameter. Unique identifier of the network device.
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
            https://developer.cisco.com/docs/dna-center/#!partially-updates-an-existing-network-device
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "category": category,
            "managementAddress": managementAddress,
            "credentials": credentials,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_b2c5c14bd5ecba26b364716a91731_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDevices/{id}/update"
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
            "bpm_b2c5c14bd5ecba26b364716a91731_v3_2_3_0", json_data
        )

    def remove_the_wired_capture_configuration(
        self, id, headers=None, **request_parameters
    ):
        """Remove the wired capture configuration on the device without preview. This performs a manual STOP of the wired
        packet capture configuration. For this we need a disable activity ID. This activity ID is available by
        calling the GET capture for Wired.

        Args:
            id(str): id path parameter. This UUID is the activity or Task ID of the stop operation which is already
                scheduled when the start operation was deployed. It is also known as disableActivityId.
                To get this ID we should be invoking /dna/intent/api/v1/capture/wired and extract the
                disableActivityId.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!remove-the-wired-capture-configuration
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/capture/wired/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fd8a579fc335510ad5084eb7a1fac32_v3_2_3_0", json_data
        )

    def poe_details(self, device_uuid, headers=None, **request_parameters):
        """Returns POE details for device.

        Args:
            device_uuid(str): deviceUuid path parameter. UUID of the device.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!p-o-e-details
        """
        check_type(headers, dict)
        check_type(device_uuid, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceUuid": device_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/{deviceUuid}/poe"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f7a67aba0b365a1e9dae62d148511a25_v3_2_3_0", json_data
        )

    def retrieves_the_total_number_of_dns_services_for_given_set_of_complex_filters(
        self,
        endTime=None,
        filters=None,
        startTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Retrieves the total number of DNS Services and offers complex filtering and sorting capabilities. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-DNSServices-1.0.0-resolved.yaml.   Retrieves the total
        number of DNS Services and offers complex filtering and sorting capabilities. If startTime and endTime
        are not provided, the API defaults to the last 24 hours. Field Name Description startTime start time
        from which API queries the data set related to the resource. It must be specified in UNIX epochtime in
        milliseconds. Value is inclusive & the default is latest endTime end time to which API queries the data
        set related to the resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive
        & the default is latest filters used to define one or more conditions. Only the data that satisfy these
        conditions will be taken into consideration during the aggregation calculation.

        Args:
            endTime(integer): Devices's endTime.
            filters(list): Devices's filters (list of objects).
            startTime(integer): Devices's startTime.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-total-number-of-d-n-s-services-for-given-set-of-complex-filters
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
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d10535ed2045b9bb5c58882e6f43cb2_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/dnsServices/query/count"
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
            "bpm_d10535ed2045b9bb5c58882e6f43cb2_v3_2_3_0", json_data
        )

    def get_module_count(
        self,
        device_id,
        name_list=None,
        operational_state_code_list=None,
        part_number_list=None,
        vendor_equipment_type_list=None,
        headers=None,
        **request_parameters
    ):
        """Returns Module Count.

        Args:
            device_id(str): deviceId query parameter.
            name_list(list, set, str, tuple): nameList query parameter.
            vendor_equipment_type_list(list, set, str, tuple): vendorEquipmentTypeList query parameter.
            part_number_list(list, set, str, tuple): partNumberList query parameter.
            operational_state_code_list(list, set, str, tuple): operationalStateCodeList query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-module-count
        """
        check_type(headers, dict)
        check_type(device_id, str, may_be_none=False)
        check_type(name_list, (list, set, str, tuple))
        check_type(vendor_equipment_type_list, (list, set, str, tuple))
        check_type(part_number_list, (list, set, str, tuple))
        check_type(operational_state_code_list, (list, set, str, tuple))
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deviceId": device_id,
            "nameList": name_list,
            "vendorEquipmentTypeList": vendor_equipment_type_list,
            "partNumberList": part_number_list,
            "operationalStateCodeList": operational_state_code_list,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/module/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fb11f997009751c991884b5fc02087c5_v3_2_3_0", json_data
        )

    def delete_filter_group_association(self, id, headers=None, **request_parameters):
        """Deletes the association between filter group and entity.

        Args:
            id(str): id path parameter. Association id.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!delete-filter-group-association
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/filterGroupAssociations/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cd2af6200563ebad8849c5fac3efe_v3_2_3_0", json_data
        )

    def fetches_discovery_details_by_id(self, id, headers=None, **request_parameters):
        """API to get discovery details for the given discovery id.

        Args:
            id(str): id path parameter. The id of the discovery.    .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!fetches-discovery-details-by-id
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/discoverys/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory("bpm_a35e75534805604e0889f1583_v3_2_3_0", json_data)

    def edits_discovery(
        self,
        id,
        credentials=None,
        discoveryTypeDetails=None,
        managementIpSelectionMethod=None,
        onlyNewDevice=None,
        updateManagementIp=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """API to edit the discovery details of the given discovery id. Updating the discovery details while the discovery
        is in progress is not allowed.

        Args:
            credentials(object): Devices's Credentials to be used for discovering devices. If multiple credentials
                are provided, they will be prioritized based on specificity and protocol version.
                Device-specific credentials take precedence over global credentials. Among SNMP
                versions, SNMPv3 credentials are given higher priority over SNMPv2 credentials.
            discoveryTypeDetails(object): Devices's New ranges can be included for range discovery. IP address
                cannot be updated for SINGLE, CIDR, CDP or LLDP types. .
            managementIpSelectionMethod(string): Devices's When Catalyst Center discovers a device, it uses one of
                the device's IP addresses as the preferred management IP address for the device. The IP
                address can be that of a built-in management interface of the device, another physical
                interface, or a logical interface like Loopback0. You can configure Catalyst Center to
                log the device's loopback IP address as the preferred management IP address, provided
                the IP address is reachable from Catalyst Center.  `DEFAULT`    * Uses the IP address
                provided in the discovery request as the management IP.  `LOOPBACK`   If you choose to
                use a device's loopback IP address as the preferred management IP address, Catalyst
                Center determines the preferred management IP address as follows:   * If the device has
                one loopback interface, that loopback interface IP address is used.   * If the device
                has multiple loopback interfaces, the loopback interface with the highest IP address is
                used.   * If there are no loopback interfaces, the Ethernet interface with the highest
                IP address is used. (Subinterface IP addresses are not considered.)   * If there are no
                Ethernet interfaces, the serial interface with the highest IP address is used.  example:
                LOOPBACK     . Available values are 'DEFAULT' and 'LOOPBACK'.
            onlyNewDevice(boolean): Devices's This flag indicates to discover only new devices that are not in
                inventory.
            updateManagementIp(boolean): Devices's This flag indicates if the management IP address of existing
                devices to be updated as part of this discovery.  If set false devices get discovered
                with the existing management IP address. If set true it overwrites the management IP
                address with the new IP address used in discovery.
            id(str): id path parameter. The id of the discovery     .
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
            https://developer.cisco.com/docs/dna-center/#!edits-discovery
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "managementIpSelectionMethod": managementIpSelectionMethod,
            "discoveryTypeDetails": discoveryTypeDetails,
            "onlyNewDevice": onlyNewDevice,
            "updateManagementIp": updateManagementIp,
            "credentials": credentials,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_cf82058feef35cfabe601c3d51f01740_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/discoverys/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_cf82058feef35cfabe601c3d51f01740_v3_2_3_0", json_data
        )

    def deletes_discovery_by_id(self, id, headers=None, **request_parameters):
        """API to delete discovery by the given discovery id.

        Args:
            id(str): id path parameter. The id of the discovery.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!deletes-discovery-by-id
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/discoverys/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f547d78b6435e6a94e5ec41c70298c0_v3_2_3_0", json_data
        )

    def get_trend_analytics_data_for_a_given_dns_service_matching_the_id_of_the_service(
        self,
        id,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        page=None,
        startTime=None,
        trendInterval=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Gets the trend analytics data related to a particular DNS Service matching the id. For detailed information
        about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-DNSServices-1.0.0-resolved.yaml.   Gets the trend analytics
        data related to a particular DNS Service matching the id. If startTime and endTime are not provided, the
        API defaults to the last 24 hours. Field Name Description startTime start time from which API queries
        the data set related to the resource. It must be specified in UNIX epochtime in milliseconds. Value is
        inclusive & the default is latest endTime end time to which API queries the data set related to the
        resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive & the default is
        latest trendInterval the trend time interval in minutues. This is a mantadory field. The possible values
        in minutes are  30 minutes, 1 hour, 1 day . groupBy specifies the attributes for grouping the data.
        filters used to define one or more conditions. Only the data that satisfy these conditions will be taken
        into consideration during the aggregation calculation. attributes attributes are used for obtaining one
        or more field's data in addition to the aggregated data. The supported attributes are listed in
        DNSServicesAnalyticsAttributeKey  model aggregateAttributes specifies the names of the attributes on
        which the aggregate function should be applied when querying the data. The supported attribute names are
        listed in  DNSServicesAggregateAttributeKey  model page contains  limit, offset, and timestampOrder
        fields.  limit  number of records to be returned in response.  offset  starting offset of data.
        timestampOrder  to sort the response based on the timestamp either in ascending or descending order.

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's attributes (list of strings).
            endTime(integer): Devices's endTime.
            filters(list): Devices's filters (list of objects).
            groupBy(list): Devices's groupBy (list of strings).
            page(object): Devices's page.
            startTime(integer): Devices's startTime.
            trendInterval(string): Devices's trendInterval.
            id(str): id path parameter. Unique id of the DNS Service. It is the combination of DNS Server IP
                (`serverIp`) and Device UUID (`deviceId`) separated by underscore (`_`). Example: If
                `serverIp` is `10.76.81.33` and `deviceId` is `6bef213c-19ca-4170-8375-b694e251101c`,
                then the `id` would be `10.76.81.33_6bef213c-19ca-4170-8375-b694e251101c` .
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
            https://developer.cisco.com/docs/dna-center/#!get-trend-analytics-data-for-a-given-d-n-s-service-matching-the-id-of-the-service
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
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

        path_params = {
            "id": id,
        }
        _payload = {
            "startTime": startTime,
            "endTime": endTime,
            "trendInterval": trendInterval,
            "groupBy": groupBy,
            "filters": filters,
            "attributes": attributes,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f1debbfd4775faba3779c513181dfbf_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/dnsServices/{id}/trendAnalytics"
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
            "bpm_f1debbfd4775faba3779c513181dfbf_v3_2_3_0", json_data
        )

    def get_top_n_analytics_data_of_aaa_services_for_given_set_of_complex_filters(
        self,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        page=None,
        startTime=None,
        topN=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Gets the Top N analytics data related to AAA Services based on given filters and group by field. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-AAAServices-1.0.0-resolved.yaml.   Gets the Top N analytics
        data related to AAA Services based on given filters and group by field. If startTime and endTime are not
        provided, the API defaults to the last 24 hours. Field Name Description startTime start time from which
        API queries the data set related to the resource. It must be specified in UNIX epochtime in
        milliseconds. Value is inclusive & the default is 24 hours ago from end time endTime end time to which
        API queries the data set related to the resource. It must be specified in UNIX epochtime in
        milliseconds. Value is inclusive & the default is current time topN the total number of records to
        retrive. This is a mandatory field groupBy specifies the attributes for grouping the data. filters used
        to define one or more conditions. Only the data that satisfy these conditions will be taken into
        consideration during the aggregation calculation. attributes attributes are used for obtaining one or
        more field's data in addition to the aggregated data. The supported attributes are listed in
        AAAServicesAnalyticsAttributeKey  model aggregateAttributes specifies the names of the attributes on
        which the aggregate function should be applied when querying the data. The supported attribute names are
        listed in  AAAServicesAggregateAttributeKey  model page contains  limit, offset and sortBy  fields.
        limit  Number of records to be returned in response,  offset  starting offset of data and  sortBy
        attribute name, order to sort.

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's attributes (list of strings).
            endTime(integer): Devices's endTime.
            filters(list): Devices's filters (list of objects).
            groupBy(list): Devices's groupBy (list of strings).
            page(object): Devices's page.
            startTime(integer): Devices's startTime.
            topN(integer): Devices's topN.
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
            https://developer.cisco.com/docs/dna-center/#!get-top-n-analytics-data-of-a-a-a-services-for-given-set-of-complex-filters
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
            "topN": topN,
            "groupBy": groupBy,
            "filters": filters,
            "attributes": attributes,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_bdca1829ea705fa690922e3e0f8ff7b0_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/aaaServices/topNAnalytics"
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
            "bpm_bdca1829ea705fa690922e3e0f8ff7b0_v3_2_3_0", json_data
        )

    def network_device_insecure_configurations_count(
        self, id, module=None, headers=None, **request_parameters
    ):
        """API to get the count of insecure CLI configurations currently applied on the network device identified by
        network device `id`. Insecure configurations are CLI commands that use deprecated, weak, or non-
        compliant security settings and are restricted on IOS-XE devices beginning with release `26.1.1`. These
        include configurations that rely on outdated security protocols, insecure authentication mechanisms, or
        any commands flagged as non-secure by the device.

        Args:
            id(str): id path parameter. Unique identifier of the network device.
            module(list, set, str, tuple): module query parameter. The module names associated with insecure
                configurations. Examples AAA, BOOTP, HTTP, CDP, IP, TRANSPORT, TFTP, TELNET, RCMD, LINE,
                FTP, NTP, SNMP, SANET, CTS, PARSER, LOGGING, DSPFARM_PROFILE, STCAPP, SSH, HSRP, CAPWAP,
                MSDP, KEY_CHAIN, KEY_CHAIN_MACSEC, VOICE, HTTPCLIENT, CALLMANAGER, SIPUA, PMIPv6,
                TLS_TUNNEL, DEVICE_SENSOR, EPC, DHCP, SYSTEM, IFS, MPLS_LDP, ISIS, BGP, NMSP, EIGRP,
                OSPFV2, OSPFV3, IVR, GATEWAY_ACCOUNTING, CALL_LEG, APPLICATION_MONITOR, WEB_SERVICE,
                VRRP, GLBP, WCCP, LISP. Up to 10 filter values are allowed. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!network-device-insecure-configurations-count
        """
        check_type(headers, dict)
        check_type(module, (list, set, str, tuple))
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "module": module,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/networkDevices/{id}/insecureConfigura" + "tions/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_baef212f289b5e46986fb25037f121b5_v3_2_3_0", json_data
        )

    def query_devices_energy(
        self,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        page=None,
        startTime=None,
        views=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Retrieves a list of network devices along with their energy data for a specified time range, based on the
        filters provided in the request body. For detailed information about the usage of the API, please refer
        to the Open API specification document - https://github.com/cisco-en-programmability/catalyst-center-
        api-specs/blob/main/Assurance/CE_Cat_Center_Org-deviceEnergy_1.0-1.0.1-resolved.yaml.   Retrieves a list
        of network devices along with their energy data for a specified time range, based on the filters
        provided in the request body. The input payload contains the following fields Field Name Description
        startTime Start time from which API queries the data set related to the resource. It must be specified
        in UNIX epochtime in milliseconds. Value is inclusive. If  startTime  is not provided, API will default
        to one day before  endTime . endTime End time to which API queries the data set related to the resource.
        It must be specified in UNIX epochtime in milliseconds. Value is inclusive. If  endTime  is not
        provided, API will default to one day after  startTime . If  startTime  is not provided either, API will
        default to current time. attributes An optional field that is used to get certain attributes in the
        response. The supported attributes are listed in  networkDeviceEnergyAttributes  model. Note: When view
        and attributes have different variants, the attributes returned in the response will be the union of
        both sets. views An optional field, similar to attributes, is useful when a large number of fields are
        required in the response data. The supported logical views and their respective fields are available in
        networkDeviceEnergyViews . filters Used to define one or more filter conditions. Only devices that
        satisfy these conditions will be taken into consideration during the aggregation calculation. This field
        can be empty. The supported list of filter keys and operators are:  'id' [eq, in], 'deviceName' [eq, in,
        like], 'deviceCategory' [eq, in], 'deviceSubCategory' [eq, in], 'siteId' [eq, in], 'siteHierarchy' [eq,
        in, like], 'siteHierarchyId' [eq, in, like] . aggregateAttributes Specifies the name of the attribute on
        which the aggregate function should be applied when querying the data. The supported attribute names are
        listed in  DevicesEnergyAggregateAttribute  model. page Contains  limit, cursor and sortBy  fields.
        limit Number of records to fetch in a page,  cursor string field indicating the next record in the
        response list and  sortBy  attribute name, order and function if you want to sort by the aggregated
        field.  sortBy  field is a list, but only single field sorting is supported on this API. How the
        filtering behavior works The filters field in each post body can be used in numerous ways: Each filter
        in the list of filters will applied ''together'' In the example below, this would request filtering data
        from devices belonging to the ''Switch'' family  and  have series equal to ''cat9300'' or ''cat9400''.
        'filters': [   {     'key': 'deviceCategory',     'operator': 'eq',     'value': 'Switch'   },   {
        'key': 'deviceSubCategory',     'operator': 'in',     'value': ['cat9300', 'cat9400']   } ] Each filter
        object can contrastingly utilize its  logical operator  to provide nested filtering functionality. In
        the example below you can see a logical 'OR' filter being applied using the nested filtering
        functionality: The primary filter object does not have its 'key', 'value', or 'operator' fields
        populated. Only the 'logicalOperator' field is populated, to indicate the filters within the nested
        filters list are to be logically conjoined. 'filters': [   {     'logicalOperator': 'or',     'filters':
        [       {         'key': 'deviceCategory',         'operator': 'eq',         'value': 'Switch'       },
        {         'key': 'deviceSubCategory',         'operator': 'in',         'value': ['cat9300', 'cat9400']
        }     ]   } ] Please refer to the 'API Support Documentation' section to understand which fields and
        filters are supported. How Pagination Works 'limit' field, is the total number of records you want to
        retrieve. 'cursor' field, indicating the next record in the response list. If you have a limit of 100,
        each page would be viewed as 100 elements. So starting with an empty cursor, means look at the first
        page (starting from first record). To get the second page, you need to specify cursor returned in the
        response of the first request.  'sortBy' field is a list, but only single field sorting is supported on
        this API, with 'asc' (ascending), or 'desc' (descending) ordering. Example 1 Request body {
        'startTime': 1703195600000,   'endTime': 1707800400000,   'filters': [     {       'key': 'id',
        'operator': 'in',       'value': ['f4b8bceb-588b-490c-b726-3dd8caf65071']     }   ],   'views':
        ['device'],   'attributes': ['siteHierarchy'],   'page': {     'limit': 100,     'cursor': ''   } }
        Response: {   'response': [     {       'id': 'f4b8bceb-588b-490c-b726-3dd8caf65071',
        'deviceName': 'ott-sda-c9k-01.cisco.com',       'deviceCategory': 'Switch',       'deviceSubCategory':
        'Cisco Catalyst 9300 Switch',       'siteHierarchy': 'Global/Ottawa'     }   ],   'page': {     'limit':
        100,     'cursor': '',     'count': 1,     'sortBy': null   },   'version': '1.0' }.

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's attributes (list of strings).
            endTime(integer): Devices's endTime.
            filters(list): Devices's filters (list of objects).
            page(object): Devices's page.
            startTime(integer): Devices's startTime.
            views(list): Devices's views (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!query-devices-energy
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
            "views": views,
            "attributes": attributes,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_caeb723a074519498c6b08a1c9dacb3_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/energy/networkDevices/query"
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
            "bpm_caeb723a074519498c6b08a1c9dacb3_v3_2_3_0", json_data
        )

    def update_filter_group(
        self,
        id,
        filters=None,
        name=None,
        type=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Updates the filter group for given id. The request payload should contain complete definition of the Filter
        Group.

        Args:
            filters(list): Devices's List of filters used in this Filter Group (list of objects).
            name(string): Devices's Filter Group name. Only alphabhets, digits and space is allowed for name.
            type(string): Devices's The type of the Filter Group.. Available values are 'Generic', 'Site', 'Network'
                and 'Client'.
            id(str): id path parameter. The id of the filter group to be updated.
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
            https://developer.cisco.com/docs/dna-center/#!update-filter-group
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "name": name,
            "type": type,
            "filters": filters,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a69602efc6f4523d806ffb18fbcf5cee_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/filterGroups/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_a69602efc6f4523d806ffb18fbcf5cee_v3_2_3_0", json_data
        )

    def get_the_filter_group_details_for_the_given_id(
        self, id, headers=None, **request_parameters
    ):
        """Returns the details of filter group for the given id.

        Args:
            id(str): id path parameter. Filter Group id.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-the-filter-group-details-for-the-given-id
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/filterGroups/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_aa70871243c557adb53eb50be2d89f65_v3_2_3_0", json_data
        )

    def delete_a_filter_group(self, id, headers=None, **request_parameters):
        """Deletes the given filter group. Delete will fail and throws validation error if the given filter group is
        associated with any entity.

        Args:
            id(str): id path parameter. The id of the filter group to be deleted.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!delete-a-filter-group
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/filterGroups/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a4c1fbb8bd1f55cdb284c431f16660e9_v3_2_3_0", json_data
        )

    def get_trend_analytics_data_of_dhcp_services_for_given_set_of_complex_filters(
        self,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        page=None,
        startTime=None,
        trendInterval=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Gets the trend analytics data related to DHCP Services based on given filters and group by field. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-DHCPServices-1.0.0-resolved.yaml.   Gets the trend analytics
        data related to DHCP Services based on given filters and group by field. If startTime and endTime are
        not provided, the API defaults to the last 24 hours. Field Name Description startTime start time from
        which API queries the data set related to the resource. It must be specified in UNIX epochtime in
        milliseconds. Value is inclusive & the default is latest endTime end time to which API queries the data
        set related to the resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive
        & the default is latest trendInterval the trend time interval in minutues. This is a mantadory field.
        The possible values in minutes are  5 minutes, 15 minutes, 1 hour, 1 day . groupBy specifies the
        attributes for grouping the data. filters used to define one or more conditions. Only the data that
        satisfy these conditions will be taken into consideration during the aggregation calculation. attributes
        attributes are used for obtaining one or more field's data in addition to the aggregated data. The
        supported attributes are listed in  DHCPServicesAnalyticsAttributeKey  model aggregateAttributes
        specifies the names of the attributes on which the aggregate function should be applied when querying
        the data. The supported attribute names are listed in  DHCPServicesAggregateAttributeKey  model page
        contains  limit, offset, and timestampOrder  fields.  limit  number of records to be returned in
        response.  offset  starting offset of data.  timestampOrder  to sort the response based on the timestamp
        either in ascending or descending order.

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's attributes (list of strings).
            endTime(integer): Devices's endTime.
            filters(list): Devices's filters (list of objects).
            groupBy(list): Devices's groupBy (list of strings).
            page(object): Devices's page.
            startTime(integer): Devices's startTime.
            trendInterval(string): Devices's trendInterval.
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
            https://developer.cisco.com/docs/dna-center/#!get-trend-analytics-data-of-d-h-c-p-services-for-given-set-of-complex-filters
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
            "trendInterval": trendInterval,
            "groupBy": groupBy,
            "filters": filters,
            "attributes": attributes,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d58baa26bd5a6d9c461592c872d515_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/dhcpServices/trendAnalytics"
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
            "bpm_d58baa26bd5a6d9c461592c872d515_v3_2_3_0", json_data
        )

    def count_the_number_of_network_devices_with_filters(
        self,
        filter=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """API to fetch the count of network devices for the given filter query.  **How the filtering behavior works**  All
        items in the `filters` array are combined using the `AND` operator by default. This can be changed by
        setting the `operator` field in the `filter` object to `OR`.  Each item in the array is filtered on the
        `key`, `operator`, and `value` fields. For string fields, such as `hostname`, the operators `eq`,
        `contains`, and `in` are allowed. For numerical fields, such as timestamps, the operators `eq`, `in`
        `gt`, `lt`, `gte`, and `lte` are allowed. Array of values can be provided for the `value` field when
        using the `in` operator.  Network devices can be queried by `userDefinedFields` by providing the `key`
        as `userDefinedFields. ` and the `value`.  ### Examples of request body for the filter.  *Example 1:
        Multiple values for a filter item*  ```json {     "filter": {         "filters": [             {
        "key": "deviceSupportLevel",                 "operator": "in",                 "value": ["SUPPORTED",
        "THIRD_PARTY"]             }         ]     } } ```  The above example will return the count of network
        devices that have the deviceSupportLevel as `SUPPORTED` or `THIRD_PARTY`.  *Example 2: Multiple filter
        items* ```json {     "filter": {         "filters": [             {                 "key":
        "deviceSupportLevel",                 "operator": "in",                 "value": ["SUPPORTED",
        "THIRD_PARTY"]             },             {                 "key": "softwareVersion",
        "operator": "eq",                 "value": "16.12.1"             }         ]     } } ```  The above
        example will return the count of network devices with the deviceSupportLevel `SUPPORTED` or
        `THIRD_PARTY` AND the softwareVersion `16.12.1`.  *Example 3: Filtering based on multiple user-defined
        fields and values* ```json {     "filter": {         "filters": [             {                 "key":
        "deviceSupportLevel",                 "operator": "in",                 "value": ["SUPPORTED",
        "THIRD_PARTY"]             },             {                 "key": "userDefinedFields.Location",
        "operator": "eq",                 "value": Building 1"             },             {
        "key": "userDefinedFields.Department",                 "operator": "eq",                 "value":
        "Engineering"             }         ]     } } ``` The above example will return the count of network
        devices that have the user-defined field `Location` with values `Building 1` or `Building 2` and the
        user-defined field `Department` with value `Engineering` and the deviceSupportLevel as `SUPPORTED` or
        `THIRD_PARTY`.   **Supported filter keys and types** | Key                        | Value Type | Allowed
        Operators                |
        |----------------------------|------------|----------------------------------| | id
        | string     | eq, contains, in                 | | managementAddress          | string     | eq,
        contains, in                 | | hostname                   | string     | eq, contains, in
        | | macAddress                 | string     | eq, contains, in                 | | serialNumbers
        | string     | eq, contains, in                 | | type                       | string     | eq,
        contains, in                 | | family                     | string     | eq, contains, in
        | | series                     | string     | eq, contains, in                 | | status
        | string     | eq, contains, in                 | | platformIds                | string     | eq,
        contains, in                 | | softwareType               | string     | eq, contains, in
        | | softwareVersion            | string     | eq, contains, in                 | | stackDevice
        | boolean    | eq                               | | bootTime                   | string     | eq,
        contains, in                 | | role                       | string     | eq, contains, in
        | | roleSource                 | string     | eq, contains, in                 | | apWlcIpAddress
        | string     | eq, contains, in                 | | deviceSupportLevel         | string     | eq,
        contains, in                 | | reachabilityStatus         | string     | eq, contains, in
        | | managementState            | string     | eq, contains, in                 | | resyncEndTime
        | integer    | eq, lt, gt, lte, gte, in         | | resyncIntervalSource       | string     | eq,
        contains, in                 | | resyncIntervalMinutes      | integer    | eq, lt, gt, lte, gte, in
        | | errorCode                  | string     | eq, contains, in                 | |
        userDefinedFields.fieldName| string     | eq, contains                     | | secureMode
        | string     | eq, in                 |.

        Args:
            filter(object): Devices's Filter to query network devices. The result will contain the network devices
                that match ALL the filter criteria  (AND condition) unless specified in
                'logicalOperator'. Total number of filter criteria should not exceed 20. .
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
            https://developer.cisco.com/docs/dna-center/#!count-the-number-of-network-devices-with-filters
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "filter": filter,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a7283357c1657bf8ccb3d32a96249d4_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDevices/query/count"
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
            "bpm_a7283357c1657bf8ccb3d32a96249d4_v3_2_3_0", json_data
        )

    def get_isis_interfaces(self, headers=None, **request_parameters):
        """Returns the interfaces that has ISIS enabled.

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-i-s-i-s-interfaces
        """
        check_type(headers, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/interface/isis"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_af71ea437c8755869b00d26ba9234dff_v3_2_3_0", json_data
        )

    def get_summary_analytics_data_of_dhcp_services_for_given_set_of_complex_filters(
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
        """Gets the summary analytics data related to DHCP Services based on given filters and group by field. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-DHCPServices-1.0.0-resolved.yaml.   Gets the summary
        analytics data related to DHCP Services based on given filters and group by field. If startTime and
        endTime are not provided, the API defaults to the last 24 hours. Field Name Description startTime start
        time from which API queries the data set related to the resource. It must be specified in UNIX epochtime
        in milliseconds. Value is inclusive & the default is latest endTime end time to which API queries the
        data set related to the resource. It must be specified in UNIX epochtime in milliseconds. Value is
        inclusive & the default is latest groupBy specifies the attributes for grouping the data. filters used
        to define one or more conditions. Only the data that satisfy these conditions will be taken into
        consideration during the aggregation calculation. attributes attributes are used for obtaining one or
        more field's data in addition to the aggregated data. The supported attributes are listed in
        DHCPServicesAnalyticsAttributeKey  model aggregateAttributes specifies the names of the attributes on
        which the aggregate function should be applied when querying the data. The supported attribute names are
        listed in  DHCPServicesAggregateAttributeKey  model page contains  limit, offset and sortBy  fields.
        limit  Number of records to be returned in response,  offset  starting offset of data and  sortBy
        attribute name, order to sort.

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's attributes (list of strings).
            endTime(integer): Devices's endTime.
            filters(list): Devices's filters (list of objects).
            groupBy(list): Devices's groupBy (list of strings).
            page(object): Devices's page.
            startTime(integer): Devices's startTime.
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
            https://developer.cisco.com/docs/dna-center/#!get-summary-analytics-data-of-d-h-c-p-services-for-given-set-of-complex-filters
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
            "groupBy": groupBy,
            "filters": filters,
            "attributes": attributes,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a3fb2e7bb8aa50508425b1dd8818fda4_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/dhcpServices/summaryAnalytics"
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
            "bpm_a3fb2e7bb8aa50508425b1dd8818fda4_v3_2_3_0", json_data
        )

    def get_top_n_analytics_data_of_dns_services_for_given_set_of_complex_filters(
        self,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        page=None,
        startTime=None,
        topN=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Gets the Top N analytics data related to DNS Services based on given filters and group by field. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-DNSServices-1.0.0-resolved.yaml.   Gets the Top N analytics
        data related to DNS Services based on given filters and group by field. If startTime and endTime are not
        provided, the API defaults to the last 24 hours. Field Name Description startTime start time from which
        API queries the data set related to the resource. It must be specified in UNIX epochtime in
        milliseconds. Value is inclusive & the default is latest endTime end time to which API queries the data
        set related to the resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive
        & the default is latest topN the total number of records to retrive. This is a mandatory field groupBy
        specifies the attributes for grouping the data. filters used to define one or more conditions. Only the
        data that satisfy these conditions will be taken into consideration during the aggregation calculation.
        attributes attributes are used for obtaining one or more field's data in addition to the aggregated
        data. The supported attributes are listed in  DNSServicesAnalyticsAttributeKey  model
        aggregateAttributes specifies the names of the attributes on which the aggregate function should be
        applied when querying the data. The supported attribute names are listed in
        DNSServicesAggregateAttributeKey  model page contains  limit, offset and sortBy  fields.  limit  Number
        of records to be returned in response,  offset  starting offset of data and  sortBy  attribute name,
        order to sort.

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's attributes (list of strings).
            endTime(integer): Devices's endTime.
            filters(list): Devices's filters (list of objects).
            groupBy(list): Devices's groupBy (list of strings).
            page(object): Devices's page.
            startTime(integer): Devices's startTime.
            topN(integer): Devices's topN.
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
            https://developer.cisco.com/docs/dna-center/#!get-top-n-analytics-data-of-d-n-s-services-for-given-set-of-complex-filters
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
            "topN": topN,
            "groupBy": groupBy,
            "filters": filters,
            "attributes": attributes,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_b43e0f60e9ac5bd4960f9772cf7a497b_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/dnsServices/topNAnalytics"
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
            "bpm_b43e0f60e9ac5bd4960f9772cf7a497b_v3_2_3_0", json_data
        )

    def retrieves_the_number_of_wlcs_by_applying_complex_filters(
        self,
        endTime=None,
        filters=None,
        startTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Retrieves the number of WLCs by applying complex filters. If startTime and endTime are not provided, the API
        defaults to the last 24 hours.  **The input payload contains the following fields,** |Field Name |
        Description | | --| --| | `startTime` | The start time indicates when the API begins retrieving data
        related to the resource. It must be specified in the UNIX epoch time format, measured in milliseconds.
        This value is inclusive, and if left unspecified, the default is 1 day before the endTime. | | `endTime`
        | The end time indicates the upper limit until which the API retrieves data related to the resource. It
        must be defined in the UNIX epoch time format, measured in milliseconds. This value is inclusive, and if
        left unspecified, the default is the latest available data. | |`filters`| This is used to specify one or
        more conditions for filtering the queried data. Refer to `WlcStatsFilterField` model for the supported
        filters |.

        Args:
            endTime(integer): Devices's End time to which the API queries the dataset related to the resource. It
                must be specified in terms of milliseconds since UNIX epoch. Value is inclusive.
            filters(list): Devices's filters (list of objects).
            startTime(integer): Devices's Start time from which the API queries the dataset related to the resource.
                It must be specified in terms of milliseconds since UNIX epoch. Value is inclusive.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-number-of-w-l-cs-by-applying-complex-filters
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
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
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f822aba3f0530cbf89bc39e3197c2f_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/wirelessControllersStats/query/count"
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
            "bpm_f822aba3f0530cbf89bc39e3197c2f_v3_2_3_0", json_data
        )

    def gets_interfaces_along_with_statistics_and_poe_data_from_all_network_devices(
        self,
        attribute=None,
        end_time=None,
        interface_id=None,
        interface_name=None,
        limit=None,
        network_device_id=None,
        network_device_ip_address=None,
        network_device_mac_address=None,
        offset=None,
        order=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        sort_by=None,
        start_time=None,
        view=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the list of the interfaces from all network devices based on         the provided query parameters.
        The latest interfaces data in the         specified start and end time range will be returned. When
        there is no         start and end time specified returns the latest available data.
        The elements are grouped and sorted by deviceUuid first, and are then         sorted by the given sort
        field, or by the default value: name.                            The supported sorting options are:
        name, adminStatus, description, duplexConfig, duplexOper,         interfaceIfIndex,interfaceType,
        macAddress,mediaType, operStatus,         portChannelId, portMode, portType,speed, vlanId
        This API can paginate up to 500,000 records, please narrow matching results with additional filters
        beyond that value. The elements are grouped and sorted by deviceUuid first, and are then sorted by the
        given sort field, or by the default value: name.   The supported sorting options are: name, adminStatus,
        description, duplexConfig, duplexOper,interfaceIfIndex,interfaceType, macAddress,mediaType,
        operStatus,portChannelId, portMode, portType,speed, vlanId,pdPowerAdminMaxInWatt,pdPowerBudgetInWatt,pdP
        owerConsumedInWatt,pdPowerRemainingInWatt,pdMaxPowerDrawn. For detailed information about the usage of
        the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        interfaces-2.0.0-resolved.yaml.

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to current time. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            limit(int): limit query parameter. Maximum number of records to return.
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1.
            sort_by(str): sortBy query parameter. A field within the response to sort by.
            order(str): order query parameter. The sort order of the field ascending or descending.
            site_hierarchy(str): siteHierarchy query parameter. The full hierarchical breakdown of the site tree
                starting from Global site name and ending with the specific site name. The Root site is
                named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`) This field supports
                wildcard asterisk (`*`) character search support. E.g. `*/San*, */San, /San*` Examples:
                `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy requested)
                `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global/AreaName2/Bu
                ildingName2/FloorName2` (multiple siteHierarchies requested) .
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site tree
                in id form starting from Global site UUID and ending with the specific site UUID. (Ex.
                `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk
                (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds requested) .
            site_id(str): siteId query parameter. The UUID of the site. (Ex. `flooruuid`) Examples: `?siteId=id1`
                (single id requested) `?siteId=id1&siteId=id2&siteId=id3` (multiple ids requested) .
            view(str): view query parameter. Views which are supported by this API. Each view represents a specific
                data set.           ### Response data provided by each view:             1.
                **configuration**          [id,name,adminStatus,description,duplexConfig,duplexOper,inte
                rfaceIfIndex,interfaceType,ipv4Address,ipv6AddressList,isL3Interface,isWan,macAddress,me
                diaType,name,operStatus,         portChannelId,portMode,         portType,speed,timestam
                p,vlanId,networkDeviceId,networkDeviceIpAddress,networkDeviceMacAddress,siteName,siteHie
                rarchy,siteHierarchyId]             2. **statistics**          [id,name,rxDiscards,rxErr
                or,rxRate,rxUtilization,txDiscards,txError,txRate,txUtilization,networkDeviceId,networkD
                eviceIpAddress,networkDeviceMacAddress,siteName,siteHierarchy,siteHierarchyId]
                3. **stackPort**          [id,name,peerStackMember,peerStackPort,stackPortType,networkDe
                viceId,networkDeviceIpAddress,networkDeviceMacAddress,siteName,siteHierarchy,siteHierarc
                hyId]                   4. **poE**              [id, name,rxDiscards,rxError,rxRate,rxUt
                ilization,txDiscards,txError,txRate,txUtilization,networkDeviceId,networkDeviceIpAddress
                ,networkDeviceMacAddress,siteName,siteHierarchy,siteHierarchyId]              When this
                query parameter is not added by default all configuration attributes will be
                available in the response.     **[configuration,statistics,stackPort]**.
            attribute(str): attribute query parameter. The following list of attributes can be provided in the
                attribute field          [id,adminStatus, description,duplexConfig,duplexOper,interfaceI
                fIndex,interfaceType,ipv4Address,ipv6AddressList,isL3Interface,isWan,macAddress,mediaTyp
                e,name,operStatus,peerStackMember,peerStackPort, portChannelId,portMode, portType,rxDisc
                ards,rxError,rxRate,rxUtilization,speed,stackPortType,timestamp,txDiscards,txError,txRat
                e,txUtilization,vlanId,networkDeviceId,networkDeviceIpAddress,networkDeviceMacAddress,si
                teName,siteHierarchy,siteHierarchyId,poeAdminStatus,poeOperStatus,chassisId,moduleId,pdC
                lassSignal,pdClassSpare,pdDeviceType,pdDeviceModel,pdPowerAdminMaxInWatt,pdPowerBudgetIn
                Watt,pdPowerConsumedInWatt,pdPowerRemainingInWatt,pdMaxPowerDrawn,pdConnectedDeviceList,
                poeOperPriority,fastPoEEnabled,perpetualPoEEnabled,policingPoEEnabled,upoePlusEnabled,fo
                urPairEnabled,poeDataTimestamp,pdLocation,pdDeviceName,pdConnectedSwitch,connectedSwitch
                Uuid,ieeeCompliant,connectedSwitchType]          If length of attribute list is too
                long, please use 'views' param instead.          Examples:          attributes=name
                (single attribute requested)          attributes=name&description&duplexOper (multiple
                attributes with comma separator).
            network_device_id(str): networkDeviceId query parameter. The list of Network Device Uuids. (Ex.
                `6bef213c-19ca-4170-8375-b694e251101c`) Examples:
                `networkDeviceId=6bef213c-19ca-4170-8375-b694e251101c` (single networkDeviceId
                requested) `networkDeviceId=6bef213c-19ca-4170-8375-
                b694e251101c&networkDeviceId=32219612-819e-4b5e-a96b-
                cf22aca13dd9&networkDeviceId=2541e9a7-b80d-4955-8aa2-79b233318ba0` (multiple
                networkDeviceIds with & separator) .
            network_device_ip_address(str): networkDeviceIpAddress query parameter. The list of Network Device
                management IP Address. (Ex. `121.1.1.10`) This field supports wildcard (`*`) character-
                based search.  Ex: `*1.1*` or `1.1*` or `*1.1` Examples:
                `networkDeviceIpAddress=121.1.1.10` `networkDeviceIpAddress=121.1.1.10&networkDeviceIpAd
                dress=172.20.1.10&networkDeviceIpAddress=10.10.20.10` (multiple networkDevice IP Address
                with & separator) .
            network_device_mac_address(str): networkDeviceMacAddress query parameter. The list of Network Device MAC
                Address. (Ex. `64:f6:9d:07:9a:00`) This field supports wildcard (`*`) character-based
                search.  Ex: `*AB:AB:AB*` or `AB:AB:AB*` or `*AB:AB:AB` Examples:
                `networkDeviceMacAddress=64:f6:9d:07:9a:00`
                `networkDeviceMacAddress=64:f6:9d:07:9a:00&networkDeviceMacAddress=70:56:9d:07:ac:77`
                (multiple networkDevice MAC addresses with & separator) .
            interface_id(str): interfaceId query parameter. The list of Interface Uuids. (Ex.
                `6bef213c-19ca-4170-8375-b694e251101c`) Examples:
                `interfaceId=6bef213c-19ca-4170-8375-b694e251101c` (single interface uuid ) `interfaceId
                =6bef213c-19ca-4170-8375-b694e251101c&32219612-819e-4b5e-a96b-cf22aca13dd9&2541e9a7-
                b80d-4955-8aa2-79b233318ba0` (multiple Interface uuid with & separator) .
            interface_name(str): interfaceName query parameter. The list of Interface name (Ex.
                `GigabitEthernet1/0/1`) This field supports wildcard (`*`) character-based search.  Ex:
                `*1/0/1*` or `1/0/1*` or `*1/0/1` Examples: `interfaceNames=GigabitEthernet1/0/1`
                (single interface name)
                `interfaceNames=GigabitEthernet1/0/1&GigabitEthernet2/0/1&GigabitEthernet3/0/1`
                (multiple interface names with & separator) .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!gets-interfaces-along-with-statistics-and-poe-data-from-all-network-devices
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(limit, int)
        check_type(offset, int)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(site_hierarchy, str)
        check_type(site_hierarchy_id, str)
        check_type(site_id, str)
        check_type(view, str)
        check_type(attribute, str)
        check_type(network_device_id, str)
        check_type(network_device_ip_address, str)
        check_type(network_device_mac_address, str)
        check_type(interface_id, str)
        check_type(interface_name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "limit": limit,
            "offset": offset,
            "sortBy": sort_by,
            "order": order,
            "siteHierarchy": site_hierarchy,
            "siteHierarchyId": site_hierarchy_id,
            "siteId": site_id,
            "view": view,
            "attribute": attribute,
            "networkDeviceId": network_device_id,
            "networkDeviceIpAddress": network_device_ip_address,
            "networkDeviceMacAddress": network_device_mac_address,
            "interfaceId": interface_id,
            "interfaceName": interface_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/interfaces"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fc7a61a854f2b2015d3f1c059ce9_v3_2_3_0", json_data
        )

    def accepts_new_ssh_key_for_selected_devices_schedules_resync(
        self,
        networkDeviceIds=None,
        resync=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API allows users to approve new SSH keys for specified devices, ensuring the continuation of connection
        establishment. When the global setting `autoAcceptSshKeys` is set to `false`, users can manually approve
        new SSH keys for selected devices using this API. This approval is valid until the SSH key changes
        again. Users can monitor individual device requests using the
        `/dna/intent/api/v1/tasks?rootId=${taskId}` API. Additionally, if `resync` is set to `true`, the API
        will submit the device for resynchronization, which is queued and processed based on system load.

        Args:
            networkDeviceIds(list): Devices's Network Device ids for which to accept the new SSH Keys (list of
                strings).
            resync(boolean): Devices's Optional flag to determine if device resync is needed after accepting a new
                SSH key.
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
            https://developer.cisco.com/docs/dna-center/#!accepts-new-s-s-h-key-for-selected-devices_-schedules-resync
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "networkDeviceIds": networkDeviceIds,
            "resync": resync,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ca4a48877215cf39f292562243f3a4a_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDevices/acceptSshKeyChange"
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
            "bpm_ca4a48877215cf39f292562243f3a4a_v3_2_3_0", json_data
        )

    def delete_a_network_device_without_configuration_cleanup(
        self,
        id=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API endpoint facilitates the deletion of a network device without performing configuration cleanup on the
        device. To delete a device via API, you must have permission to provision the network device. Although
        the API operation does not change the device configuration, removing a device without cleaning up its
        configuration could lead to a network behaviour that is not consistent with the configurations that are
        known to the system.  This API endpoint facilitates the deletion of a network device without performing
        configuration cleanup on the device. To delete a device via API, you must have permission to provision
        the network device. Although the API operation does not change the device configuration, removing a
        device without cleaning up its configuration could lead to a network behaviour that is not consistent
        with the configurations that are known to the system.

        Args:
            id(string): Devices's The unique identifier of the network device to be deleted.
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
            https://developer.cisco.com/docs/dna-center/#!delete-a-network-device-without-configuration-cleanup
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "id": id,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ce6c2c14553f9a4a88f66a04c21c4_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDevices/deleteWithoutCleanup"
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
            "bpm_ce6c2c14553f9a4a88f66a04c21c4_v3_2_3_0", json_data
        )

    def get_all_health_score_definitions_for_given_filters(
        self,
        attribute=None,
        device_type=None,
        id=None,
        include_for_overall_health=None,
        limit=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """Get all health score defintions.  Supported filters are id, name and overall health include status. A health
        score definition can be different across device type. So, deviceType in the query param is important and
        default is all device types.  By default all supported attributes are listed in response. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-issueAndHealthDefinitions-1.0.0-resolved.yaml.   OpenAPI
        specification defined to get all health score defintions.Supported filters are id, name and overall
        health include status. A health score definition can be different across device type. So, deviceType in
        the query param is important and default is all device types.   API Support Documentation   Query
        Parameters:   deviceType   These are the device families/types supported for system issue definitions.
        If no input is made on device type, all device types are considered.    Supported values: ROUTER,
        SWITCH_AND_HUB, WIRELESS_CONTROLLER, UNIFIED_AP, WIRELESS_CLIENT, WIRED_CLIENT     Example :
        ?deviceType=ROUTER   id   The definition identifier.     Examples :
        ?id=015d9cba-4f53-4087-8317-7e49e5ffef46 (single id requested)
        ?id=T015d9cba-4f53-4087-8317-7e49e5ffef46&id=015d9cba-4f53-4087-8317-7e49e5ffef47 (multiple id
        requested)   includeForOverallHealth   The inclusion status of the issue definition, either true or
        false. true indicates that particular health metric is included in overall health computation, otherwise
        false. By default it's set to true.     Example :     ?includeForOverallHealth=true   attribute   The
        list of attributes that needs to be included in the response. By default, all properties are sent in
        response.   Supported Attributes:   id ,  name ,  displayName ,  deviceFamily ,  description ,
        includeForOverallHealth ,  definitionStatus ,  thresholdValue ,  synchronizeToIssueThreshold
        Examples :   ?attribute=id (single attribute requested)   ?attribute=id&attribute=name (multiple
        attribute requested)   offset   Specifies the starting point within all records returned by the API.
        It's one based offset. The starting value is 1.   limit   Maximum number of records to return.

        Args:
            device_type(str): deviceType query parameter. These are the device families supported for health score
                definitions. If no input is made on device family, all device families are considered.
            id(str): id query parameter. The definition identifier. Examples:
                id=015d9cba-4f53-4087-8317-7e49e5ffef46 (single entity id request)
                id=015d9cba-4f53-4087-8317-7e49e5ffef46&id=015d9cba-4f53-4087-8317-7e49e5ffef47
                (multiple ids in the query param) .
            include_for_overall_health(bool): includeForOverallHealth query parameter. The inclusion status of the
                issue definition, either true or false. true indicates that particular health metric is
                included in overall health computation, otherwise false. By default it's set to true. .
            attribute(str): attribute query parameter. These are the attributes supported in health score
                definitions response. By default, all properties are sent in response. .
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1.
            limit(int): limit query parameter. Maximum number of records to return.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-all-health-score-definitions-for-given-filters
        """
        check_type(headers, dict)
        check_type(device_type, str)
        check_type(id, str)
        check_type(include_for_overall_health, bool)
        check_type(attribute, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deviceType": device_type,
            "id": id,
            "includeForOverallHealth": include_for_overall_health,
            "attribute": attribute,
            "offset": offset,
            "limit": limit,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/healthScoreDefinitions"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dea15738b550f3b147965f64050c97_v3_2_3_0", json_data
        )

    def fetches_the_discovery_job_details_for_the_given_job_id(
        self, discovery_id, job_id, headers=None, **request_parameters
    ):
        """This API retrieves the details of a specific discovery job using the given job id and discovery id.

        Args:
            discovery_id(str): discoveryId path parameter. The id of the discovery. .
            job_id(str): jobId path parameter. The id of the discovery job. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!fetches-the-discovery-job-details-for-the-given-job-id
        """
        check_type(headers, dict)
        check_type(discovery_id, str, may_be_none=False)
        check_type(job_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "discoveryId": discovery_id,
            "jobId": job_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/discoverys/{discoveryId}/jobs/{jobId}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dbf7bf70e5556a590074784c2e0c7b1_v3_2_3_0", json_data
        )

    def get_modules(
        self,
        device_id,
        limit=None,
        name_list=None,
        offset=None,
        operational_state_code_list=None,
        part_number_list=None,
        vendor_equipment_type_list=None,
        headers=None,
        **request_parameters
    ):
        """Returns modules by specified device id. The API returns a paginated response based on 'limit' and 'offset'
        parameters, allowing up to 500 records per page. 'limit' specifies the number of records, and 'offset'
        sets the starting point using 1-based indexing. Use /dna/intent/api/v1/network-device/module/count API
        to get the total record count. For data sets over 500 records, make multiple calls, adjusting 'limit'
        and 'offset' to retrieve all records incrementally.

        Args:
            device_id(str): deviceId query parameter.
            limit(int): limit query parameter. The number of records to show for this page. Min: 1, Max: 500.
            offset(int): offset query parameter.
            name_list(list, set, str, tuple): nameList query parameter.
            vendor_equipment_type_list(list, set, str, tuple): vendorEquipmentTypeList query parameter.
            part_number_list(list, set, str, tuple): partNumberList query parameter.
            operational_state_code_list(list, set, str, tuple): operationalStateCodeList query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-modules
        """
        check_type(headers, dict)
        check_type(device_id, str, may_be_none=False)
        check_type(limit, int)
        check_type(offset, int)
        check_type(name_list, (list, set, str, tuple))
        check_type(vendor_equipment_type_list, (list, set, str, tuple))
        check_type(part_number_list, (list, set, str, tuple))
        check_type(operational_state_code_list, (list, set, str, tuple))
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deviceId": device_id,
            "limit": limit,
            "offset": offset,
            "nameList": name_list,
            "vendorEquipmentTypeList": vendor_equipment_type_list,
            "partNumberList": part_number_list,
            "operationalStateCodeList": operational_state_code_list,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/module"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ce9e547725c45c66824afda98179d12f_v3_2_3_0", json_data
        )

    def validates_a_network_device(
        self,
        category=None,
        credentials=None,
        managementAddress=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Validates the credentials and connectivity of a network device. This endpoint checks if the provided details are
        correct and if the device can be  reached. The task response contains status for HTTP, SNMP, CLI,
        NETCONF, Enable Password and CLI Priviledge 15.

        Args:
            category(string): Devices's Category of the device. Used to determine the type of the device being
                added. | Category                                    | Description
                | Required Credentials | Optional Credentials | |
                ------------------------------------------|
                --------------------------------------------------------------------------------------|
                -------------------| -------------------| | `NETWORK_DEVICE`
                | Standard Cisco network devices like switches, routers, controllers
                | CLI, SNMP            | HTTP, NETCONF        | | `COMPUTE_DEVICE`
                | Server or computing system manufactured by Cisco such as Unified Computing System
                (UCS) | HTTP                 | CLI, SNMP            | | `THIRD_PARTY_DEVICE`
                | Non-Cisco network devices that support SNMP monitoring
                | SNMP                 |                    | | `MERAKI_DASHBOARD`
                | Cisco Meraki cloud-managed devices accessed via Meraki Dashboard
                | Meraki               |                    | | `FIREWALL_MANAGEMENT_CENTER`
                | Cisco Secure Firewall Management Center (FMC)
                | HTTP                 |                    | . Available values are
                'FIREWALL_MANAGEMENT_CENTER'.
            credentials(object): Devices's Credentials used to access the network device. .
            managementAddress(): Devices's Management address of the network device. For meraki dashboard, this is
                the dashboard URL.
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
            https://developer.cisco.com/docs/dna-center/#!validates-a-network-device
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "category": category,
            "managementAddress": managementAddress,
            "credentials": credentials,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_edac26fbcb77539ebe8bc5bd4b49055b_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDevices/validateDevice"
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
            "bpm_edac26fbcb77539ebe8bc5bd4b49055b_v3_2_3_0", json_data
        )

    def get_network_device_by_pagination_range(
        self, records_to_return, start_index, headers=None, **request_parameters
    ):
        """Returns the list of network devices for the given pagination range. The maximum number of records that can be
        retrieved is 500.

        Args:
            start_index(int): startIndex path parameter. Start index [>=1].
            records_to_return(int): recordsToReturn path parameter. Number of records to return [1<= recordsToReturn
                <= 500].
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-network-device-by-pagination-range
        """
        check_type(headers, dict)
        check_type(start_index, int, may_be_none=False)
        check_type(records_to_return, int, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "startIndex": start_index,
            "recordsToReturn": records_to_return,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-" + "device/{startIndex}/{recordsToReturn}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d7b6ce5abd5dad837e22ace817a6f0_v3_2_3_0", json_data
        )

    def get_trend_analytics_data_for_a_given_aaa_service_matching_the_id_of_the_service(
        self,
        id,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        page=None,
        startTime=None,
        trendInterval=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Gets the trend analytics data related to a particular AAA Service matching the id. For detailed information
        about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-AAAServices-1.0.0-resolved.yaml.   Gets the trend analytics
        data related to a particular AAA Service matching the id. If startTime and endTime are not provided, the
        API defaults to the last 24 hours. Field Name Description startTime start time from which API queries
        the data set related to the resource. It must be specified in UNIX epochtime in milliseconds. Value is
        inclusive & the default is 24 hours ago from end time endTime end time to which API queries the data set
        related to the resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive &
        the default is current trendInterval the trend time interval in minutues. This is a mantadory field. The
        possible values in minutes are  5, 15, 60 . When the start and end Time range is greater than 1 day, the
        allowed interval value is 60 minutes. groupBy specifies the attributes for grouping the data. filters
        used to define one or more conditions. Only the data that satisfy these conditions will be taken into
        consideration during the aggregation calculation. attributes attributes are used for obtaining one or
        more field's data in addition to the aggregated data. The supported attributes are listed in
        AAAServicesAnalyticsAttributeKey  model aggregateAttributes specifies the names of the attributes on
        which the aggregate function should be applied when querying the data. The supported attribute names are
        listed in  AAAServicesAggregateAttributeKey  model page contains  limit, offset, and timestampOrder
        fields.  limit  number of records to be returned in response.  offset  starting offset of data.
        timestampOrder  to sort the response based on the timestamp either in ascending or descending order.

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's attributes (list of strings).
            endTime(integer): Devices's endTime.
            filters(list): Devices's filters (list of objects).
            groupBy(list): Devices's groupBy (list of strings).
            page(object): Devices's page.
            startTime(integer): Devices's startTime.
            trendInterval(string): Devices's trendInterval.
            id(str): id path parameter. Unique id of the AAA Service. It is the combination of AAA Server IP
                (`serverIp`) and Device UUID (`deviceId`) separated by underscore (`_`). Example: If
                `serverIp` is `10.76.81.33` and `deviceId` is `6bef213c-19ca-4170-8375-b694e251101c`,
                then the `id` would be `10.76.81.33_6bef213c-19ca-4170-8375-b694e251101c` .
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
            https://developer.cisco.com/docs/dna-center/#!get-trend-analytics-data-for-a-given-a-a-a-service-matching-the-id-of-the-service
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
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

        path_params = {
            "id": id,
        }
        _payload = {
            "startTime": startTime,
            "endTime": endTime,
            "trendInterval": trendInterval,
            "groupBy": groupBy,
            "filters": filters,
            "attributes": attributes,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f33d768d01586c9133b155da5e5ade_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/aaaServices/{id}/trendAnalytics"
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
            "bpm_f33d768d01586c9133b155da5e5ade_v3_2_3_0", json_data
        )

    def fetches_devices_that_support_wired_packet_capture_functional_capability(
        self,
        site_hierarchy_id,
        limit=None,
        offset=None,
        order=None,
        sort_by=None,
        headers=None,
        **request_parameters
    ):
        """Returns devices that support wired packet capture functional capability.

        Args:
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site tree
                in id form starting from Global site UUID and ending with the specific site UUID. (Ex.
                `globalUuid/areaUuid/buildingUuid/floorUuid`) This value can be obtained from the
                responses of APIs like `/dna/intent/api/v1/sites` or `intent/api/v1/areas/${id}` or
                `/dna/intent/api/v2/floors/${id}` or `dna/intent/api/v2/buildings/${id}` Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid` .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1.
            limit(int): limit query parameter. The number of records to show for this page.
            sort_by(str): sortBy query parameter. A property within the response to sort by.
            order(str): order query parameter. Whether ascending or descending order should be used to sort the
                response.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!fetches-devices-that-support-wired-packet-capture-functional-capability
        """
        check_type(headers, dict)
        check_type(site_hierarchy_id, str, may_be_none=False)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, str)
        check_type(order, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "siteHierarchyId": site_hierarchy_id,
            "offset": offset,
            "limit": limit,
            "sortBy": sort_by,
            "order": order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/flowAnalysis/packetCapture/supportedD" + "evices"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cb8be837c5f87be110634fe17dc4b_v3_2_3_0", json_data
        )

    def get_device_enrichment_details_v1(self, headers=None, **request_parameters):
        """Enriches a given network device context (device id or device Mac Address or device management IP address) with
        details about the device and neighbor topology.

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            list: JSON response. A list of MyDict objects.
            Access the object's properties by using the dot notation
            or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-device-enrichment-details-v1
        """
        check_type(headers, dict)
        if headers is not None:
            if "entity_type" in headers:
                check_type(headers.get("entity_type"), str, may_be_none=False)
            if "entity_value" in headers:
                check_type(headers.get("entity_value"), str, may_be_none=False)
            if "__persistbapioutput" in headers:
                check_type(headers.get("__persistbapioutput"), bool)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/device-enrichment-details"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a20c25e0fa518bb186fd7747450ef6_v3_2_3_0", json_data
        )

    def retrieves_the_total_count_of_wlcs_stats_by_applying_basic_filtering(
        self, end_time=None, start_time=None, headers=None, **request_parameters
    ):
        """Retrieves the number of WLCs Stats by applying basic filtering. If startTime and endTime are not provided, the
        API defaults to the last 24 hours.

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-total-count-of-w-l-cs-stats-by-applying-basic-filtering
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/wirelessControllersStats/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_af87c9430d555bbeb1ea358afdf73953_v3_2_3_0", json_data
        )

    def get_planned_access_points_for_building(
        self,
        building_id,
        limit=None,
        offset=None,
        radios=None,
        headers=None,
        **request_parameters
    ):
        """Provides a list of Planned Access Points for the Building it is requested for.

        Args:
            building_id(str): buildingId path parameter. The instance UUID of the building hierarchy element.
            limit(int): limit query parameter. The number of records to show for this page;The minimum is 1, and the
                maximum is 500.
            offset(int): offset query parameter. The page offset for the response. E.g. if limit=100, offset=0 will
                return first 100 records, offset=1 will return next 100 records, etc.
            radios(bool): radios query parameter. Whether to include the planned radio details of the planned access
                points.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-planned-access-points-for-building
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        check_type(radios, bool)
        check_type(building_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "limit": limit,
            "offset": offset,
            "radios": radios,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "buildingId": building_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/buildings/{buildingId}/planned-" + "access-points"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_efc372d6eb577ca47e8c86f30c3d2f_v3_2_3_0", json_data
        )

    def retrieves_the_list_of_aaa_services_for_given_parameters(
        self,
        device_id=None,
        device_name=None,
        device_site_hierarchy_id=None,
        end_time=None,
        limit=None,
        offset=None,
        order=None,
        server_ip=None,
        site_hierarchy=None,
        site_id=None,
        sort_by=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the list of AAA Services and offers basic filtering and sorting capabilities. For detailed information
        about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-AAAServices-1.0.0-resolved.yaml.   Retrieves the list of AAA
        Services and offers basic filtering and sorting capabilities. If startTime and endTime are not provided,
        the API defaults to the last 24 hours. The data in the response is calculated for the given time range.
        Transaction fields are summed up and latncy fields are averaged. It returns transaction and latency data
        for the two phases of the authentication process 1) EAP Extensible Authentication Protocol 2) MAB MAC
        Authentication Bypass.

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to current time. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            limit(int): limit query parameter. Maximum number of records to return.
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1.
            sort_by(str): sortBy query parameter. Field name on which sorting needs to be done.
            order(str): order query parameter. The sort order of the field ascending or descending.
            server_ip(str): serverIp query parameter. IP Address of the AAA Server. This parameter supports wildcard
                (`*`) character -based search. Example: `10.76.81.*` or `*56.78*` or `*50.28` Examples:
                serverIp=10.42.3.31 (single IP Address is requested)
                serverIp=10.42.3.31&serverIp=name2&fabricVnName=name3 (multiple IP Addresses are
                requested) .
            device_id(str): deviceId query parameter. The device UUID.  Examples:
                `deviceId=6bef213c-19ca-4170-8375-b694e251101c` (single deviceId is requested)  `deviceI
                d=6bef213c-19ca-4170-8375-b694e251101c&deviceId=32219612-819e-4b5e-a96b-cf22aca13dd9
                (multiple networkDeviceIds with & separator) .
            device_name(str): deviceName query parameter. Name of the device. This parameter supports wildcard (`*`)
                character -based search. Example: `wnbu-sjc*` or `*wnbu-sjc*` or `*wnbu-sjc` Examples:
                deviceName=wnbu-sjc24.cisco.com (single device name is requested) deviceName=wnbu-
                sjc24.cisco.com&deviceName=wnbu-sjc22.cisco.com (multiple device names are requested)
                .
            site_hierarchy(str): siteHierarchy query parameter. The full hierarchical breakdown of the site tree
                starting from Global site name and ending with the specific site name. The Root site is
                named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`) This field supports
                wildcard asterisk (`*`) character search support. E.g. `*/San*, */San, /San*` Examples:
                `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy requested)
                `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global/AreaName2/Bu
                ildingName2/FloorName2` (multiple siteHierarchies requested) .
            device_site_hierarchy_id(str): deviceSiteHierarchyId query parameter. The full hierarchy breakdown of
                the site tree in id form starting from Global site UUID and ending with the specific
                site UUID. (Ex. `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports
                wildcard asterisk (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?deviceSiteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single
                siteHierarchyId requested) `?deviceSiteHierarchyId=globalUuid/areaUuid/buildingUuid/floo
                rUuid&deviceSiteHierarchyId=globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple
                siteHierarchyIds requested) .
            site_id(str): siteId query parameter. The UUID of the site. (Ex. `flooruuid`) Examples: `?siteId=id1`
                (single id requested) `?siteId=id1&siteId=id2&siteId=id3` (multiple ids requested) .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-a-a-a-services-for-given-parameters
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(limit, int)
        check_type(offset, int)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(server_ip, str)
        check_type(device_id, str)
        check_type(device_name, str)
        check_type(site_hierarchy, str)
        check_type(device_site_hierarchy_id, str)
        check_type(site_id, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "limit": limit,
            "offset": offset,
            "sortBy": sort_by,
            "order": order,
            "serverIp": server_ip,
            "deviceId": device_id,
            "deviceName": device_name,
            "siteHierarchy": site_hierarchy,
            "deviceSiteHierarchyId": device_site_hierarchy_id,
            "siteId": site_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/aaaServices"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory("bpm_cc60533fba1ac9a077366acd_v3_2_3_0", json_data)

    def retrieves_the_number_of_processes_by_applying_complex_filters(
        self,
        network_device_id,
        endTime=None,
        filters=None,
        startTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Retrieves the number of processKpis by applying complex filters. If startTime and endTime are not provided, the
        API defaults to the last 24 hours.  **The input payload contains the following fields,** |Field Name |
        Description | | --| --| | `startTime` | The start time indicates when the API begins retrieving data
        related to the resource. It must be specified in the UNIX epoch time format, measured in milliseconds.
        This value is inclusive, and if left unspecified, the default is 1 day before the endTime. | | `endTime`
        | The end time indicates the upper limit until which the API retrieves data related to the resource. It
        must be defined in the UNIX epoch time format, measured in milliseconds. This value is inclusive, and if
        left unspecified, the default is the latest available data. | |`filters`| This is used to specify one or
        more conditions for filtering the queried data. Refer to `ProcessKpisFilterField` model for the
        supported filters |.

        Args:
            endTime(integer): Devices's End time to which the API queries the dataset related to the resource. It
                must be specified in terms of milliseconds since UNIX epoch. Value is inclusive.
            filters(list): Devices's filters (list of objects).
            startTime(integer): Devices's Start time from which the API queries the dataset related to the resource.
                It must be specified in terms of milliseconds since UNIX epoch. Value is inclusive.
            network_device_id(str): networkDeviceId path parameter. Network Device UUID.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-number-of-processes-by-applying-complex-filters
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
        }
        _payload = {
            "startTime": startTime,
            "endTime": endTime,
            "filters": filters,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_c9b971a355e780ef01ddc8269b13_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/data/api/v1/networkDevices/{networkDeviceId}/proces"
            + "sKpis/query/count"
        )
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
            "bpm_c9b971a355e780ef01ddc8269b13_v3_2_3_0", json_data
        )

    def get_interface_info_by_id(self, device_id, headers=None, **request_parameters):
        """Returns list of interfaces by specified device.

        Args:
            device_id(str): deviceId path parameter. Device ID.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-interface-info-by-id
        """
        check_type(headers, dict)
        check_type(device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceId": device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/interface/network-device/{deviceId}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e057192b97615f0d99a10e2b66bab13a_v3_2_3_0", json_data
        )

    def retrieves_the_list_of_dhcp_services_for_given_parameters(
        self,
        device_id=None,
        device_name=None,
        device_site_hierarchy=None,
        device_site_hierarchy_id=None,
        device_site_id=None,
        end_time=None,
        limit=None,
        offset=None,
        order=None,
        server_ip=None,
        sort_by=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the list of DHCP Services and offers basic filtering and sorting capabilities. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-DHCPServices-1.0.0-resolved.yaml.   Retrieves the list of
        DHCP Services and offers basic filtering and sorting capabilities. If startTime and endTime are not
        provided, the API defaults to the last 24 hours. The data in the response is calculated for the given
        time range.

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            limit(int): limit query parameter. Maximum number of records to return.
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1.
            sort_by(str): sortBy query parameter. Field name on which sorting needs to be done.
            order(str): order query parameter. The sort order of the field ascending or descending.
            server_ip(str): serverIp query parameter. IP Address of the DHCP Server. This parameter supports
                wildcard (`*`) character -based search. Example: `10.76.81.*` or `*56.78*` or `*50.28`
                Examples: serverIp=10.42.3.31 (single IP Address is requested)
                serverIp=10.42.3.31&serverIp=name2&fabricVnName=name3 (multiple IP Addresses are
                requested) .
            device_id(str): deviceId query parameter. The device UUID.  Examples:
                `deviceId=6bef213c-19ca-4170-8375-b694e251101c` (single deviceId is requested)  `deviceI
                d=6bef213c-19ca-4170-8375-b694e251101c&deviceId=32219612-819e-4b5e-a96b-cf22aca13dd9
                (multiple networkDeviceIds with & separator) .
            device_name(str): deviceName query parameter. Name of the device. This parameter supports wildcard (`*`)
                character -based search. Example: `wnbu-sjc*` or `*wnbu-sjc*` or `*wnbu-sjc` Examples:
                deviceName=wnbu-sjc24.cisco.com (single device name is requested) deviceName=wnbu-
                sjc24.cisco.com&deviceName=wnbu-sjc22.cisco.com (multiple device names are requested)
                .
            device_site_hierarchy(str): deviceSiteHierarchy query parameter. The full hierarchical breakdown of the
                site tree starting from Global site name and ending with the specific site name. The
                Root site is named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`) This field
                supports wildcard asterisk (`*`) character search support. E.g. `*/San*, */San, /San*`
                Examples: `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy
                requested) `?deviceSiteHierarchy=Global/AreaName/BuildingName/FloorName&deviceSiteHierar
                chy=Global/AreaName2/BuildingName2/FloorName2` (multiple siteHierarchies requested) .
            device_site_hierarchy_id(str): deviceSiteHierarchyId query parameter. The full hierarchy breakdown of
                the site tree in id form starting from Global site UUID and ending with the specific
                site UUID. (Ex. `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports
                wildcard asterisk (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?deviceSiteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single
                siteHierarchyId requested) `?deviceSiteHierarchyId=globalUuid/areaUuid/buildingUuid/floo
                rUuid&deviceSiteHierarchyId=globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple
                siteHierarchyIds requested) .
            device_site_id(str): deviceSiteId query parameter. The UUID of the site. (Ex. `flooruuid`) Examples:
                `?deviceSiteIds=id1` (single id requested)
                `?deviceSiteIds=id1&deviceSiteIds=id2&siteId=id3` (multiple ids requested) .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-d-h-c-p-services-for-given-parameters
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(limit, int)
        check_type(offset, int)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(server_ip, str)
        check_type(device_id, str)
        check_type(device_name, str)
        check_type(device_site_hierarchy, str)
        check_type(device_site_hierarchy_id, str)
        check_type(device_site_id, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "limit": limit,
            "offset": offset,
            "sortBy": sort_by,
            "order": order,
            "serverIp": server_ip,
            "deviceId": device_id,
            "deviceName": device_name,
            "deviceSiteHierarchy": device_site_hierarchy,
            "deviceSiteHierarchyId": device_site_hierarchy_id,
            "deviceSiteId": device_site_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/dhcpServices"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d9a96f4107695eec9ce303b039ed4747_v3_2_3_0", json_data
        )

    def get_top_n_analytics_data_of_dhcp_services_for_given_set_of_complex_filters(
        self,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        page=None,
        startTime=None,
        topN=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Gets the Top N analytics data related to DHCP Services based on given filters and group by field. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-DHCPServices-1.0.0-resolved.yaml.   Gets the Top N analytics
        data related to DHCP Services based on given filters and group by field. If startTime and endTime are
        not provided, the API defaults to the last 24 hours. Field Name Description startTime start time from
        which API queries the data set related to the resource. It must be specified in UNIX epochtime in
        milliseconds. Value is inclusive & the default is latest endTime end time to which API queries the data
        set related to the resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive
        & the default is latest topN the total number of records to retrive. This is a mandatory field groupBy
        specifies the attributes for grouping the data. filters used to define one or more conditions. Only the
        data that satisfy these conditions will be taken into consideration during the aggregation calculation.
        attributes attributes are used for obtaining one or more field's data in addition to the aggregated
        data. The supported attributes are listed in  DHCPServicesAnalyticsAttributeKey  model
        aggregateAttributes specifies the names of the attributes on which the aggregate function should be
        applied when querying the data. The supported attribute names are listed in
        DHCPServicesAggregateAttributeKey  model page contains  limit, offset and sortBy  fields.  limit  Number
        of records to be returned in response,  offset  starting offset of data and  sortBy  attribute name,
        order to sort.

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's attributes (list of strings).
            endTime(integer): Devices's endTime.
            filters(list): Devices's filters (list of objects).
            groupBy(list): Devices's groupBy (list of strings).
            page(object): Devices's page.
            startTime(integer): Devices's startTime.
            topN(integer): Devices's topN.
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
            https://developer.cisco.com/docs/dna-center/#!get-top-n-analytics-data-of-d-h-c-p-services-for-given-set-of-complex-filters
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
            "topN": topN,
            "groupBy": groupBy,
            "filters": filters,
            "attributes": attributes,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_edf997bb4bcc5dd6baca80647d8a47ce_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/dhcpServices/topNAnalytics"
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
            "bpm_edf997bb4bcc5dd6baca80647d8a47ce_v3_2_3_0", json_data
        )

    def get_functional_capability_for_devices(
        self, device_id, function_name=None, headers=None, **request_parameters
    ):
        """Returns the functional-capability for given devices.

        Args:
            device_id(str): deviceId query parameter. Accepts comma separated deviceid's and return list of
                functional-capabilities for the given id's. If invalid or not-found id's are provided,
                null entry will be returned in the list.
            function_name(list, set, str, tuple): functionName query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-functional-capability-for-devices
        """
        check_type(headers, dict)
        check_type(device_id, str, may_be_none=False)
        check_type(function_name, (list, set, str, tuple))
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deviceId": device_id,
            "functionName": function_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/functional-capability"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ad8cea95d71352f0842a2c869765e6cf_v3_2_3_0", json_data
        )

    def update_device_role(
        self,
        id=None,
        role=None,
        roleSource=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Updates the role of the device as access, core, distribution, border router.

        Args:
            id(string): Devices's DeviceId of the Device.
            role(string): Devices's Role of device as ACCESS, CORE, DISTRIBUTION, BORDER ROUTER.
            roleSource(string): Devices's Role source as MANUAL / AUTO.
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
            https://developer.cisco.com/docs/dna-center/#!update-device-role
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "id": id,
            "role": role,
            "roleSource": roleSource,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_aa11f09d28165f4ea6c81b8642e59cc4_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/brief"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_aa11f09d28165f4ea6c81b8642e59cc4_v3_2_3_0", json_data
        )

    def exports_the_credentials_of_network_devices(
        self,
        exportSshKey=None,
        networkDeviceIds=None,
        password=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Exports device credentials of all network devices in the inventory to an encrypted CSV file. To export
        credentials for selected devices only, provide the `networkDeviceIds` parameter in the request body.
        The exported file will be in zip format encrypted using the password provided in the request body. The
        ZIP file will contain a CSV file with the  credentials of the selected network devices.  If
        `networkDeviceIds` is not provided, then the credentials of all the network devices will be exported.
        Credentials for access points and Meraki devices cannot be exported.  The response contains a task ID.
        Use the `/dna/intent/api/v1/tasks/{taskId}` API to check the status of the task. The task will be
        completed when the file is ready for download. The download URL will be available in the
        `resultLocation` attribute of the task API response.

        Args:
            exportSshKey(boolean): Devices's Flag to export the SSH key. If not provided, the SSH key will not be
                exported.
            networkDeviceIds(list): Devices's List of network device IDs to export the credentials for. If not
                provided, all devices will be exported. (list of strings).
            password(string): Devices's Password to encrypt the CSV file.  A password must contain, at minimum: 8
                characters one lowercase letter one uppercase letter one number one special character
                (-=[];,./~!@#$%^&*()_+{}|:?) The password cannot contain spaces or the characters < > .
                Constraints: minLength set to 8.
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
            https://developer.cisco.com/docs/dna-center/#!exports-the-credentials-of-network-devices
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "networkDeviceIds": networkDeviceIds,
            "password": password,
            "exportSshKey": exportSshKey,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a542b2feed5259a2922ebd75ca99a141_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDevices/exportCredentials"
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
            "bpm_a542b2feed5259a2922ebd75ca99a141_v3_2_3_0", json_data
        )

    def query_assurance_events_with_filters(
        self,
        attributes=None,
        deviceFamily=None,
        endTime=None,
        filters=None,
        page=None,
        startTime=None,
        views=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Returns the list of events discovered by Catalyst Center, determined by the complex filters. Please refer to the
        'API Support Documentation' section to understand which fields are supported. For detailed information
        about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-AssuranceEvents-1.0.0-resolved.yaml.   OpenAPI specification
        defined to fetch the list of assurance events using complex filters present in Catalyst Center API
        Support Documentation Note that querying of data spanning more than 7 days is not allowed, so difference
        between startTime and endTime must not be more than that. The input payload contains the following
        fields: deviceFamily  Supported values: Switches and Hubs, Routers, Wireless Controller, Third Party
        Device, Unified AP, Wired Client, and  Wireless Client This is a mandatory field. Please note that
        multiple families across network device type and client type is not allowed.  For example, choosing
        'Routers' along with 'Wireless Client' or 'Unified AP' is not supported.   startTime Start time from
        which API queries the data set related to the resource. It must be specified in UNIX epochtime in
        milliseconds. Value is inclusive.  If 'startTime' is not provided, API will default to current time
        minus 24 hours. endTime End time to which API queries the data set related to the resource. It must be
        specified in UNIX epochtime in milliseconds. Value is inclusive.  If 'endTime' is not provided, API will
        default to current time. filters  Used to define one or more filter conditions. Only the data that
        satisfy these conditions will be taken into consideration during the aggregation calculation. The
        supported list of filters in defined in 'EventsFilterObj'. page  The 'page' includes 'limit', 'offset'
        and 'sortBy' fields. 'limit' indicates the number of records to retrieve per page, 'offset' signifies
        the starting position of the data, and 'sortBy' specifies the name and order. If 'sortBy' parameter is
        not provided, then the results are sorted by 'timestamp' in descending order.  Supported sortBy values
        based on device family       Network Device: name, messageType, severity, networkDeviceId,
        networkDeviceName, managementIpAddress, timestamp          Unified AP: name, messageType, severity,
        networkDeviceId, networkDeviceName, managementIpAddress, apMac, wlcId, wlcName, frequency, timestamp
        Wired Client: name, messageType, severity, ipv4, ipv6, identifier, connectedDeviceId,
        connectedDeviceName, connectedDeviceIp, connectedInterfaceName, vlanId, clientMac, timestamp
        Wireless Client: name, messageType, ipv4, ipv6, identifier, clientMac, apId, apName, apMac, wlcId,
        wlcName, frequency, ssid, username, dhcpServerIp, timestamp    views Specified 'views' can be requested.
        Each view correspondsto different sets of data. By default basic view attributes will be shown. 'views'
        an optional parameter which can be passed to get one or more of views.       View   Response Data
        basic   id, name, timestamp, details, messageType, siteHierarchyId, siteHierarchy, deviceFamily,
        networkDeviceId, networkDeviceName, managementIpAddress       network   id, name, severity, facility,
        mnemonic, eventStatus, timestamp, details, messageType, siteHierarchyId, siteHierarchy, deviceFamily,
        networkDeviceId, networkDeviceName, managementIpAddress, replacedDeviceSerialNumber,
        replacingDeviceSerialNumber, switchNumber       ap   id, name, eventStatus, timestamp, details,
        messageType, siteHierarchyId, siteHierarchy, deviceFamily, networkDeviceId, networkDeviceName,
        managementIpAddress, apMac, wlcName, frequency, apSwitchName, apSwitchId, wlcId, reasonDescription,
        lastApDisconnectReason, lastApResetType, apRadioOperationState, currentRadioPowerLevel,
        previousRadioPowerLevel, newRadioChannelList, newRadioChannelWidth, oldRadioChannelList,
        oldRadioChannelWidth, radioNoise, radioInterference, radioChannelUtilization, affectedClients
        wiredClient   id, name, severity, facility, mnemonic, eventStatus, timestamp, details, messageType,
        siteHierarchyId, siteHierarchy, deviceFamily, networkDeviceId, networkDeviceName, managementIpAddress,
        identifier, clientMac, connectedInterfaceName, ipv4, ipv6, vlanId, auditSessionId, reasonDescription
        wirelessClient   id, name, timestamp, details, messageType, siteHierarchyId, siteHierarchy,
        deviceFamily, networkDeviceId, networkDeviceName, identifier, clientMac, wirelessClientEventStartTime,
        wirelessClientEventEndTime, radioChannelSlot, isPrivateMac, vlanId, authServerIp, apRole, assocRssi,
        assocSnr, udnName, udnId, duid, failureIpAddress, roamType, subReasonDescription, invalidIeAPs,
        candidateAPs, missingResponseAPs, apMac, wlcName, wlcId, ssid, username, frequency, resultStatus,
        failureCategory, dhcpServerIp, ipv4, ipv6, reasonDescription, childEvents       Examples :
        views=["network","wiredClient"] attributes Specified 'attribute' can be requested Each attribute
        requested will be part of the API response. Supported Attributes: affectedClients ,  apMac ,
        apRadioOperationState ,  apRole ,  apSwitchName ,  apSwitchId ,  assocRssi ,  assocSnr ,  auditSessionId
        , authServerIp , bssid , candidateAPs ,  childEvents , clientMac ,  connectedInterfaceName ,
        currentRadioPowerLevel ,  details , deviceFamily ,  dhcpServerIp , duid ,  eventStatus ,  facility ,
        failureCategory ,  failureIpAddress ,  frequency , id ,  identifier , invalidIeAPs ,  ipv4 , ipv6 ,
        isPrivateMac ,  lastApDisconnectReason , lastApResetType ,  managementIpAddress , messageType ,
        missingResponseAPs ,  mnemonic , name ,  networkDeviceId ,  networkDeviceName , newRadioChannelList ,
        newRadioChannelWidth , oldRadioChannelList ,  oldRadioChannelWidth , previousRadioPowerLevel ,
        radioChannelSlot ,  radioChannelUtilization ,  radioInterference , radioNoise , reasonDescription ,
        replacedDeviceSerialNumber , replacingDeviceSerialNumber , resultStatus , roamType , severity ,
        siteHierarchy , siteHierarchyId , ssid , subReasonDescription , switchNumber , timestamp , udnId ,
        udnName , username , vlanId , wirelessClientEventEndTime , wirelessClientEventStartTime , wlcId wlcName
        If length of attribute list is too long, when using the field, please use  views  param instead.
        Examples : attributes=["id","name"].

        Args:
            attributes(list): Devices's attributes (list of strings).
            deviceFamily(list): Devices's deviceFamily (list of strings).
            endTime(integer): Devices's endTime.
            filters(list): Devices's filters (list of objects).
            page(object): Devices's page.
            startTime(integer): Devices's startTime.
            views(list): Devices's views (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!query-assurance-events-with-filters
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
            "deviceFamily": deviceFamily,
            "startTime": startTime,
            "endTime": endTime,
            "attributes": attributes,
            "views": views,
            "filters": filters,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ef94c2c20ba15fd38e129ac75067de1e_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/assuranceEvents/query"
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
            "bpm_ef94c2c20ba15fd38e129ac75067de1e_v3_2_3_0", json_data
        )

    def count_the_number_of_discovery_jobs_for_given_discovery_id(
        self, id, job_id=None, headers=None, **request_parameters
    ):
        """API to fetch the count of discovery jobs for given discovery  id. A discovery can have multiple discovery jobs,
        created against the same discovery id.

        Args:
            id(str): id path parameter. The id of the discovery.
            job_id(list, set, str, tuple): jobId query parameter. Optional list of the discovery job ids to filter
                by.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!count-the-number-of-discovery-jobs-for-given-discovery-id
        """
        check_type(headers, dict)
        check_type(job_id, (list, set, str, tuple))
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "jobId": job_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/discoverys/{id}/jobs/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ec84f99950b383bbcb694ac2002f_v3_2_3_0", json_data
        )

    def gets_the_network_device_details_based_on_the_provided_query_parameters(
        self,
        attribute=None,
        end_time=None,
        fabric_role=None,
        fabric_site_id=None,
        family=None,
        health_score=None,
        id=None,
        l2_vn=None,
        l3_vn=None,
        limit=None,
        mac_address=None,
        maintenance_mode=None,
        management_ip_address=None,
        offset=None,
        order=None,
        role=None,
        secure_mode=None,
        serial_number=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        software_version=None,
        sort_by=None,
        start_time=None,
        transit_network_id=None,
        type=None,
        view=None,
        headers=None,
        **request_parameters
    ):
        """Gets the Network Device details based on the provided query parameters.  When there is no start and end time
        specified returns the latest device details. For detailed information about the usage of the API, please
        refer to the Open API specification document https://github.com/cisco-en-programmability/catalyst-
        center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-AssuranceNetworkDevices-2.0.1-resolved.yaml.

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to current time. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            limit(int): limit query parameter. Maximum number of records to return.
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1.
            sort_by(str): sortBy query parameter. A field within the response to sort by.
            order(str): order query parameter. The sort order of the field ascending or descending.
            site_hierarchy(str): siteHierarchy query parameter. The full hierarchical breakdown of the site tree
                starting from Global site name and ending with the specific site name. The Root site is
                named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`) This field supports
                wildcard asterisk (*) character search support. E.g. */San*, */San, /San* Examples:
                `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy requested)
                `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global/AreaName2/Bu
                ildingName2/FloorName2` (multiple siteHierarchies requested) .
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site tree
                in id form starting from Global site UUID and ending with the specific site UUID. (Ex.
                `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk (*)
                character search support. E.g. `*uuid*, *uuid, uuid* Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds requested) .
            site_id(str): siteId query parameter. The UUID of the site. (Ex. `flooruuid`) This field supports
                wildcard asterisk (*) character search support. E.g.*flooruuid*, *flooruuid, flooruuid*
                Examples: `?siteId=id1` (single id requested) `?siteId=id1&siteId=id2&siteId=id3`
                (multiple ids requested) .
            id(str): id query parameter. The list of entity Uuids. (Ex."6bef213c-19ca-4170-8375-b694e251101c")
                Examples: id=6bef213c-19ca-4170-8375-b694e251101c (single entity uuid requested) id=6bef
                213c-19ca-4170-8375-b694e251101c&id=32219612-819e-4b5e-a96b-cf22aca13dd9&id=2541e9a7-
                b80d-4955-8aa2-79b233318ba0 (multiple entity uuid with '&' separator) .
            management_ip_address(str): managementIpAddress query parameter. The list of entity management IP
                Address. It can be either Ipv4 or Ipv6 address or combination of both(Ex. "121.1.1.10")
                This field supports wildcard (`*`) character-based search.  Ex: `*1.1*` or `1.1*` or
                `*1.1` Examples: managementIpAddresses=121.1.1.10 managementIpAddresses=121.1.1.10&manag
                ementIpAddresses=172.20.1.10&managementIpAddresses=200:10&=managementIpAddresses172.20.3
                .4 (multiple entity IP Address with & separator) .
            mac_address(str): macAddress query parameter. The macAddress of the network device or client This field
                supports wildcard (`*`) character-based search.  Ex: `*AB:AB:AB*` or `AB:AB:AB*` or
                `*AB:AB:AB` Examples: `macAddress=AB:AB:AB:CD:CD:CD` (single macAddress requested)
                `macAddress=AB:AB:AB:CD:CD:DC&macAddress=AB:AB:AB:CD:CD:FE` (multiple macAddress
                requested) .
            family(str): family query parameter. The list of network device family names Examples:family=Switches
                and Hubs (single network device family name )family=Switches and
                Hubs&family=Router&family=Wireless Controller (multiple Network device family names with
                & separator). This field is not case sensitive.
            type(str): type query parameter. The list of network device type This field supports wildcard (`*`)
                character-based search. Ex: `*9407R*` or `*9407R` or `9407R*` Examples:
                type=SwitchesCisco Catalyst 9407R Switch (single network device types ) type=Cisco
                Catalyst 38xx stack-able ethernet switch&type=Cisco 3945 Integrated Services Router G2
                (multiple Network device types with & separator) .
            role(str): role query parameter. The list of network device role. Examples:role=CORE,
                role=CORE&role=ACCESS&role=ROUTER (multiple Network device roles with & separator). This
                field is not case sensitive.
            serial_number(str): serialNumber query parameter. The list of network device serial numbers. This field
                supports wildcard (`*`) character-based search.  Ex: `*MS1SV*` or `MS1SV*` or `*MS1SV`
                Examples: serialNumber=9FUFMS1SVAX
                serialNumber=9FUFMS1SVAX&FCW2333Q0BY&FJC240617JX(multiple Network device serial number
                with & separator) .
            maintenance_mode(bool): maintenanceMode query parameter. The device maintenanceMode status true or
                false.
            software_version(str): softwareVersion query parameter. The list of network device software version This
                field supports wildcard (`*`) character-based search. Ex: `*17.8*` or `*17.8` or `17.8*`
                Examples: softwareVersion=2.3.4.0 (single network device software version )
                softwareVersion=17.9.3.23&softwareVersion=17.7.1.2&softwareVersion=*.17.7 (multiple
                Network device software versions with & separator) .
            health_score(str): healthScore query parameter. The list of entity health score categories Examples:
                healthScore=good, healthScore=good&healthScore=fair (multiple entity healthscore values
                with & separator). This field is not case sensitive. .
            view(str): view query parameter. The List of Network Device model views. Please refer to
                ```NetworkDeviceView``` section in the Open API specification document mentioned in the
                description.
            attribute(str): attribute query parameter. The List of Network Device model attributes. Please refer to
                ```NetworkDeviceAttribute``` section in the Open API specification document mentioned in
                the description.
            fabric_site_id(str): fabricSiteId query parameter. The fabric site Id or list to fabric site Ids to
                filter the data  This field supports wildcard asterisk (*) character search support.
                E.g. *uuid*, *uuid, uuid*  Examples:  `?fabricSiteId=fabricSiteUuid)
                ?fabricSiteId=fabricSiteUuid1&fabricSiteId=fabricSiteUuid2 (multiple fabricSiteIds
                requested).
            l2_vn(str): l2Vn query parameter. The L2 Virtual Network Id or list to Virtual Network Ids to filter the
                data  This field supports wildcard asterisk (*) character search support. E.g. *uuid*,
                *uuid, uuid*  Examples:  `?l2Vn=virtualNetworkId
                ?l2Vn=virtualNetworkId1&l2Vn=virtualNetworkId2 (multiple virtualNetworkId's requested).
            l3_vn(str): l3Vn query parameter. The L3 Virtual Network Id or list to Virtual Network Ids to filter the
                data  This field supports wildcard asterisk (*) character search support. E.g. *uuid*,
                *uuid, uuid*  Examples:  `?l3Vn=virtualNetworkId
                ?l3Vn=virtualNetworkId1&l3Vn=virtualNetworkId2 (multiple virtualNetworkId's requested).
            transit_network_id(str): transitNetworkId query parameter. The Transit Network Id or list to Transit
                Network Ids to filter the data  This field supports wildcard asterisk (*) character
                search support. E.g. *uuid*, *uuid, uuid*  Examples:
                `?transitNetworkId=transitNetworkId
                ?transitNetworkId=transitNetworkuuid1&transitNetworkId=transitNetworkuuid1 (multiple
                transitNetworkIds requested.
            fabric_role(str): fabricRole query parameter. The list of fabric device role. Examples:
                fabricRole=BORDER, fabricRole=BORDER&fabricRole=EDGE (multiple fabric device roles with
                & separator)  Available values : BORDER, EDGE, MAP-SERVER, LEAF, SPINE, TRANSIT-CP,
                EXTENDED-NODE, WLC, UNIFIED-AP.
            secure_mode(str): secureMode query parameter. The list of secureMode statuses. Examples:
                secureMode=ENABLED, secureMode=DISABLED&secureMode=NOT_APPLICABLE  Available values :
                ENABLED, DISABLED, NOT_APPLICABLE, UNKNOWN.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!gets-the-network-device-details-based-on-the-provided-query-parameters
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(limit, int)
        check_type(offset, int)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(site_hierarchy, str)
        check_type(site_hierarchy_id, str)
        check_type(site_id, str)
        check_type(id, str)
        check_type(management_ip_address, str)
        check_type(mac_address, str)
        check_type(family, str)
        check_type(type, str)
        check_type(role, str)
        check_type(serial_number, str)
        check_type(maintenance_mode, bool)
        check_type(software_version, str)
        check_type(health_score, str)
        check_type(view, str)
        check_type(attribute, str)
        check_type(fabric_site_id, str)
        check_type(l2_vn, str)
        check_type(l3_vn, str)
        check_type(transit_network_id, str)
        check_type(fabric_role, str)
        check_type(secure_mode, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "limit": limit,
            "offset": offset,
            "sortBy": sort_by,
            "order": order,
            "siteHierarchy": site_hierarchy,
            "siteHierarchyId": site_hierarchy_id,
            "siteId": site_id,
            "id": id,
            "managementIpAddress": management_ip_address,
            "macAddress": mac_address,
            "family": family,
            "type": type,
            "role": role,
            "serialNumber": serial_number,
            "maintenanceMode": maintenance_mode,
            "softwareVersion": software_version,
            "healthScore": health_score,
            "view": view,
            "attribute": attribute,
            "fabricSiteId": fabric_site_id,
            "l2Vn": l2_vn,
            "l3Vn": l3_vn,
            "transitNetworkId": transit_network_id,
            "fabricRole": fabric_role,
            "secureMode": secure_mode,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/networkDevices"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c7314fc7e15dab859eb66f45b1e95a_v3_2_3_0", json_data
        )

    def get_devices_registered_for_wsa_notification(
        self, macaddress=None, serial_number=None, headers=None, **request_parameters
    ):
        """It fetches devices which are registered to receive WSA notifications. The device serial number and/or MAC
        address are required to be provided as query parameters.

        Args:
            serial_number(str): serialNumber query parameter. Serial number of the device.
            macaddress(str): macaddress query parameter. Mac addres of the device.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-devices-registered-for-w-s-a-notification
        """
        check_type(headers, dict)
        check_type(serial_number, str)
        check_type(macaddress, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "serialNumber": serial_number,
            "macaddress": macaddress,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/tenantinfo/macaddress"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b2c39feb5e48913492c33add7f13_v3_2_3_0", json_data
        )

    def count_the_number_of_discoveries(
        self, id=None, name=None, headers=None, **request_parameters
    ):
        """API to fetch the count of discoveries using basic filters.  **How the filtering behavior works**  Each filter
        item provided in the query parameters will be applied simultaneously such that the result is the `AND`
        of all the filter items.

        Args:
            id(list, set, str, tuple): id query parameter. Optional list of the discovery ids to filter by.
            name(str): name query parameter. The name of the discovery job. This will be a unique value.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!count-the-number-of-discoveries
        """
        check_type(headers, dict)
        check_type(id, (list, set, str, tuple))
        check_type(name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "name": name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/discoverys/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b3dbd0479f145eb5aabafa688b019faf_v3_2_3_0", json_data
        )

    def get_the_interface_data_for_the_given_interface_idinstance_uuid_along_with_the_statistics_and_poe_data(
        self,
        id,
        attribute=None,
        end_time=None,
        start_time=None,
        view=None,
        headers=None,
        **request_parameters
    ):
        """Returns the interface data for the given interface instance Uuid along with the statistics data. The latest
        interface data in the specified start and end time range will be returned. When there is no start and
        end time specified returns the latest available data for the given interface Id. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-interfaces-2.0.0-resolved.yaml.

        Args:
            id(str): id path parameter. The interface Uuid.
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to current time. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            view(str): view query parameter. Interface data model views.
            attribute(str): attribute query parameter. The following list of attributes can be provided in the
                attribute field          [id,adminStatus, description,duplexConfig,duplexOper,interfaceI
                fIndex,interfaceType,ipv4Address,ipv6AddressList,isL3Interface,isWan,macAddress,mediaTyp
                e,name,operStatus,peerStackMember,peerStackPort, portChannelId,portMode, portType,rxDisc
                ards,rxError,rxRate,rxUtilization,speed,stackPortType,timestamp,txDiscards,txError,txRat
                e,txUtilization,vlanId,networkDeviceId,networkDeviceIpAddress,networkDeviceMacAddress,si
                teName,siteHierarchy,siteHierarchyId,poeAdminStatus,poeOperStatus,chassisId,moduleId,pdC
                lassSignal,pdClassSpare,pdDeviceType,pdDeviceModel,pdPowerAdminMaxInWatt,pdPowerBudgetIn
                Watt,pdPowerConsumedInWatt,pdPowerRemainingInWatt,pdMaxPowerDrawn,pdConnectedDeviceList,
                poeOperPriority,fastPoEEnabled,perpetualPoEEnabled,policingPoEEnabled,upoePlusEnabled,fo
                urPairEnabled,poeDataTimestamp,pdLocation,pdDeviceName,pdConnectedSwitch,connectedSwitch
                Uuid,ieeeCompliant,connectedSwitchType]          If length of attribute list is too
                long, please use 'views' param instead.          Examples:          attributes=name
                (single attribute requested)          attributes=name&description&duplexOper (multiple
                attributes with comma separator).
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-the-interface-data-for-the-given-interface-idinstance-uuid-along-with-the-statistics-and-poe-data
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(view, str)
        check_type(attribute, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "view": view,
            "attribute": attribute,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/interfaces/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_adcdf890505770af113b18b30c1b5f_v3_2_3_0", json_data
        )

    def get_trend_analytics_data_for_a_given_dhcp_service_matching_the_id_of_the_service(
        self,
        id,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        page=None,
        startTime=None,
        trendInterval=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Gets the trend analytics data related to a particular DHCP Service matching the id. For detailed information
        about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-DHCPServices-1.0.0-resolved.yaml.   Gets the trend analytics
        data related to a particular DHCP Service matching the id. If startTime and endTime are not provided,
        the API defaults to the last 24 hours. Field Name Description startTime start time from which API
        queries the data set related to the resource. It must be specified in UNIX epochtime in milliseconds.
        Value is inclusive & the default is latest endTime end time to which API queries the data set related to
        the resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive & the default
        is latest trendInterval the trend time interval in minutues. This is a mantadory field. The possible
        values in minutes are  5, 15, 60 . When the start and end Time range is greater than 1 day, the allowed
        interval value is 60 minutes. groupBy specifies the attributes for grouping the data. filters used to
        define one or more conditions. Only the data that satisfy these conditions will be taken into
        consideration during the aggregation calculation. attributes attributes are used for obtaining one or
        more field's data in addition to the aggregated data. The supported attributes are listed in
        DHCPServicesAnalyticsAttributeKey  model aggregateAttributes specifies the names of the attributes on
        which the aggregate function should be applied when querying the data. The supported attribute names are
        listed in  DHCPServicesAggregateAttributeKey  model page contains  limit, offset, and timestampOrder
        fields.  limit  number of records to be returned in response.  offset  starting offset of data.
        timestampOrder  to sort the response based on the timestamp either in ascending or descending order.

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's attributes (list of strings).
            endTime(integer): Devices's endTime.
            filters(list): Devices's filters (list of objects).
            groupBy(list): Devices's groupBy (list of strings).
            page(object): Devices's page.
            startTime(integer): Devices's startTime.
            trendInterval(string): Devices's trendInterval.
            id(str): id path parameter. Unique id of the DHCP Service. It is the combination of DHCP Server IP
                (`serverIp`) and Device UUID (`deviceId`) separated by underscore (`_`). Example: If
                `serverIp` is `10.76.81.33` and `deviceId` is `6bef213c-19ca-4170-8375-b694e251101c`,
                then the `id` would be `10.76.81.33_6bef213c-19ca-4170-8375-b694e251101c` .
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
            https://developer.cisco.com/docs/dna-center/#!get-trend-analytics-data-for-a-given-d-h-c-p-service-matching-the-id-of-the-service
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
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

        path_params = {
            "id": id,
        }
        _payload = {
            "startTime": startTime,
            "endTime": endTime,
            "trendInterval": trendInterval,
            "groupBy": groupBy,
            "filters": filters,
            "attributes": attributes,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_eb1227bb250799b6ca76ed4bee9d9_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/dhcpServices/{id}/trendAnalytics"
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
            "bpm_eb1227bb250799b6ca76ed4bee9d9_v3_2_3_0", json_data
        )

    def discards_the_wired_capture_configuration_intent(
        self, preview_activity_id, headers=None, **request_parameters
    ):
        """Discards the wired capture intent.   Note that the scheduled-disabled task cannot be discarded or cancelled
        because they have already deployed.  The feature can only be disabled by sending in a direct-deploy
        POST with API /dna/intent/api/v1/capture/wired/{id}/deleteDeploy.

        Args:
            preview_activity_id(str): previewActivityId path parameter. activity from the POST
                /deviceConfigugrationModels task response.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!discards-the-wired-capture-configuration-intent
        """
        check_type(headers, dict)
        check_type(preview_activity_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "previewActivityId": preview_activity_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/capture/wired/configurationModels/{pr"
            + "eviewActivityId}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bd83eea7b295eceb9a16cf8dacdfcd6_v3_2_3_0", json_data
        )

    def get_device_detail(
        self, identifier, search_by, timestamp=None, headers=None, **request_parameters
    ):
        """Returns detailed Network Device information retrieved by Mac Address, Device Name or UUID for any given point of
        time.

        Args:
            timestamp(int): timestamp query parameter. UTC timestamp of device data in milliseconds.
            identifier(str): identifier query parameter. One of "macAddress", "nwDeviceName", "uuid" (case
                insensitive).
            search_by(str): searchBy query parameter. MAC Address, device name, or UUID of the network device.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-device-detail
        """
        check_type(headers, dict)
        check_type(timestamp, int)
        check_type(identifier, str, may_be_none=False)
        check_type(search_by, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "timestamp": timestamp,
            "identifier": identifier,
            "searchBy": search_by,
        }

        if _params["timestamp"] is None:
            _params["timestamp"] = ""
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/device-detail"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c9ee787eb5a0391309f45ddf392ca_v3_2_3_0", json_data
        )

    def retrieves_the_list_of_port_channels_for_the_network_device(
        self, network_device_id, id=None, name=None, headers=None, **request_parameters
    ):
        """This API endpoint retrieves the list of port channels for the given network device.  ### Aggregation Protocol
        The protocol used for aggregating multiple physical links into the port channel:  | Protocol |
        Description | |----------|-------------| | LACP     | A dynamic, IEEE-standard protocol that aggregates
        multiple physical links into a single logical link. It provides automatic negotiation and configuration
        for increased bandwidth and redundancy. Commonly used in multi-vendor networks. | | PAGP     | A Cisco
        proprietary protocol that aggregates links into a logical link. It automatically negotiates link
        aggregation between Cisco devices. Typically used in Cisco-only environments. | | NONE     | Indicates
        no link aggregation protocol is used. Links are manually configured without protocol-based negotiation.
        |  ### Channel Mode  The mode of operation for the channel:  | Mode                 | Description |
        |----------------------|-------------| | ON                   | This mode forces the interface to
        channel without any negotiation protocol. It assumes the other side is also set to `ON`. This mode does
        not use LACP or PAgP, making it less flexible as both ends must be manually configured. | | ACTIVE
        | Used with LACP, this mode actively tries to form an EtherChannel by sending LACP packets. It requires
        the other side to be in either `ACTIVE` or `PASSIVE` mode. | | PASSIVE              | Also used with
        LACP, this mode waits for the other side to initiate the channel. It will form a channel if it receives
        LACP packets from a switch in `ACTIVE` mode. | | AUTO                 | Used with PAgP, this mode
        passively waits for the other side to initiate the EtherChannel. It requires the other side to be in
        `DESIRABLE` mode to form a channel. | | AUTO_NON_SILENT      | Similar to `AUTO`, but specifically for
        use in environments where devices do not send PAgP packets unless they detect PAgP packets from a
        neighbor. | | DESIRABLE            | Another PAgP mode, where the interface actively tries to negotiate
        the EtherChannel by sending PAgP packets. It will form a channel if the other side is in either `AUTO`
        or `DESIRABLE` mode. | | DESIRABLE_NON_SILENT | Similar to `DESIRABLE`, but requires explicit
        acknowledgment from the other side before forming a channel. It is used when the other device might not
        send PAgP packets unless it receives them. | | NONE                 | Refers to a state where no
        channeling protocol is configured. This is essentially a non-operational mode regarding EtherChannel
        formation. |.

        Args:
            network_device_id(str): networkDeviceId path parameter. Unique identifier for the network device.
            id(str): id query parameter. Optional list of the port channel ids to filter by.
            name(str): name query parameter. Optional name of the port channel to filter by. This supports partial
                search. For example, searching for "Port" will match "Port-channel1", "Port-channel2",
                etc. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-port-channels-for-the-network-device
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(name, str)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "name": name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDevices/{networkDeviceId}/port" + "Channels"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bbfe7b248059dca461333715ed62b4_v3_2_3_0", json_data
        )

    def export_device_list(
        self,
        deviceUuids=None,
        operationEnum=None,
        parameters=None,
        password=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Exports the selected network device to a file.

        Args:
            deviceUuids(list): Devices's List of device uuids (list of strings).
            operationEnum(string): Devices's 0 to export Device Credential Details Or 1 to export Device Details.
                Available values are 'CREDENTIALDETAILS' and 'DEVICEDETAILS'.
            parameters(list): Devices's List of device parameters that needs to be exported to file (list of
                strings).
            password(string): Devices's Password is required when the operationEnum value is 0 .
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
            https://developer.cisco.com/docs/dna-center/#!export-device-list
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "deviceUuids": deviceUuids,
            "operationEnum": operationEnum,
            "parameters": parameters,
            "password": password,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e6ec627d3c587288978990aae75228_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/file"
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
            "bpm_e6ec627d3c587288978990aae75228_v3_2_3_0", json_data
        )

    def get_network_device_by_ip(self, ip_address, headers=None, **request_parameters):
        """Returns the network device by specified IP address.

        Args:
            ip_address(str): ipAddress path parameter. Device IP address.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-network-device-by-i-p
        """
        check_type(headers, dict)
        check_type(ip_address, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "ipAddress": ip_address,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/ip-address/{ipAddress}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dc74c2052a3a4eb7e2a01eaa8e7_v3_2_3_0", json_data
        )

    def get_list_of_child_events_for_the_given_wireless_client_event(
        self, id, headers=None, **request_parameters
    ):
        """Wireless client event could have child events and this API can be used to fetch the same using parent event `id`
        as the input. For detailed information about the usage of the API, please refer to the Open API
        specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-AssuranceEvents-1.0.0-resolved.yaml.   OpenAPI specification
        defined to fetch the list of child wireless client events, assurance using event parent event 'id'   API
        Support Documentation   id   Unique identifier for the event.

        Args:
            id(str): id path parameter. Unique identifier for the event.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-list-of-child-events-for-the-given-wireless-client-event
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/assuranceEvents/{id}/childEvents"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d3cf1ace30895351b5b8c3f7919b972e_v3_2_3_0", json_data
        )

    def gets_the_list_of_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions(
        self,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        page=None,
        startTime=None,
        views=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Gets the list of Network Devices based on the provided complex filters and aggregation functions. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-AssuranceNetworkDevices-2.0.1-resolved.yaml.   How the
        filtering behavior works   The filters field in each post body can be used in numerous ways: Each filter
        in the list of filters will be applied ''together'' In the example below, this would request filtering
        to retrieve Switches         and Hubs device family  and  macAddress either 00:1E:49:81:6C:FF or
        34:1E:49:81:6C:F0.   Each filter object can contrastingly utilize its  logical operator  to provide
        nested filtering functionality.   Please refer to the 'API Support Documentation' section to understand
        which fields and filters are supported.   How Pagination Works   'limit' field, is the total number of
        records you want to retrieve.   'offset' field, is the record you want to start on.   If you have a
        limit of 100, each page would be viewed as 100 elements.         So starting with an offset of 1, means
        look at the first page of data.         Starting with an offset of 2, means start on page 2 (starting
        with the         101st element).    'sortBy' field is a list, but only single field sorting is supported
        on         this API.   with 'asc' (ascending), or 'desc' (descending) ordering.

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's attributes (list of strings).
            endTime(integer): Devices's endTime.
            filters(list): Devices's filters (list of objects).
            page(object): Devices's page.
            startTime(integer): Devices's startTime.
            views(list): Devices's views (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!gets-the-list-of-network-devices-based-on-the-provided-complex-filters-and-aggregation-functions
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "startTime": startTime,
            "endTime": endTime,
            "views": views,
            "attributes": attributes,
            "filters": filters,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_bd1c59e9be75ac4a40decaa95ee9efd_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/networkDevices/query"
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
            "bpm_bd1c59e9be75ac4a40decaa95ee9efd_v3_2_3_0", json_data
        )

    def get_all_interfaces(
        self,
        last_input_time=None,
        last_output_time=None,
        limit=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """Returns all available interfaces. This endpoint can return a maximum of 500 interfaces. The API returns a
        paginated response based on 'limit' and 'offset' parameters, allowing up to 500 records per page.
        'limit' specifies the number of records, and 'offset' sets the starting point using 1-based indexing.
        Use '/dna/intent/api/v1/interface/count' to get the total record count. For data sets over 500 records,
        make multiple calls, adjusting 'limit' and 'offset' to retrieve all records incrementally.

        Args:
            offset(int): offset query parameter.
            limit(int): limit query parameter. The number of records to show for this page. Min: 1, Max: 500.
            last_input_time(str): lastInputTime query parameter. Last Input Time.
            last_output_time(str): lastOutputTime query parameter. Last Output Time.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-all-interfaces
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(last_input_time, str)
        check_type(last_output_time, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "offset": offset,
            "limit": limit,
            "lastInputTime": last_input_time,
            "lastOutputTime": last_output_time,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/interface"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d3d71136d95562afc211b40004d109_v3_2_3_0", json_data
        )

    def get_wireless_lan_controller_details_by_id(
        self, id, headers=None, **request_parameters
    ):
        """Returns the wireless lan controller info with given device ID.

        Args:
            id(str): id path parameter. Device ID.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-wireless-lan-controller-details-by-id
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/{id}/wireless-info"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c01ee650fcf858789ca00c8deda969b9_v3_2_3_0", json_data
        )

    def retrieves_specific_stats_for_a_wlc_over_a_specified_period_of_time_know_your_network(
        self,
        id,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        page=None,
        startTime=None,
        trendInterval=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Retrieves the time series stats of a specific WLC by applying complex filters, aggregate functions, and
        grouping. The data will be grouped based on the specified trend time interval. If startTime and endTime
        are not provided, the API defaults to the last 24 hours.  **The input payload contains the following
        fields,** |Field Name | Description | | --| --| | `startTime` | The start time indicates when the API
        begins retrieving data related to the resource. It must be specified in the UNIX epoch time format,
        measured in milliseconds. This value is inclusive, and if left unspecified, the default is 1 day before
        the endTime. | | `endTime` | The end time indicates the upper limit until which the API retrieves data
        related to the resource. It must be defined in the UNIX epoch time format, measured in milliseconds.
        This value is inclusive, and if left unspecified, the default is the latest available data. | |
        `trendInterval` |  The time window for aggregating metrics. This is a mandatory request field. Possible
        values include *5 minutes, 10 minutes, 1 hour, 1 day, or 7 days*. If the start and end time range
        exceeds 1 day, the trendInterval defaults to 1 hour.| | `groupBy` | Specifies the attributes for
        grouping the data. Refer to `WlcStatsGroupByField` model for the supported grouping attributes| |
        `attributes` | A list of attributes associated with the resource, which can be requested to be included
        in the response alongside the required attributes. Refer to `WlcStatsAttribute` model for the supported
        attributes | | `aggregateAttributes` | This specifies the attribute name and the function to be applied
        during data querying. The aggregate function is then applied to data within the specified start and end
        times. Refer to `WlcStatsAggregateField` model for the supported aggregate attributes | |`filters`| This
        is used to specify one or more conditions for filtering the queried data. Refer to `WlcStatsFilterField`
        model for the supported filters | |`page`| It includes the **limit, cursor, and timeSortOrder** fields.
        *limit* denotes the number of records to retrieve per page, *cursor* signifies the initial data
        position, and *timeSortOrder* is used sort the response based on the timestamp either in ascending or
        descending order. |.

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's attributes (list of strings. Available values are 'id', 'name',
                'siteHierarchy', 'siteHierarchyId', 'lastUpdatedTime', '24ghzClients', '5ghzClients',
                '6ghzClients', 'totalClientCount', 'assocAttempts', 'assocFailures', 'assocRespAccepts',
                'assocRespRejects', 'assocRespErrors', 'startAttempts', 'associationAttempts',
                'localAuthAttempts', 'l2AuthAttempts', 'l2AuthFailures', 'mabAttempts', 'mabFailures',
                'ipLearnAttempts', 'ipLearnFailures', 'l3AuthAttempts', 'l3AuthFailures',
                'sessionPushAttempts', 'sessionPushFailures', 'runAttempts', 'deletedAttempts', 'roams',
                'cckmRoams', 'dot11rRoams', 'dot11iFastRoams', 'dot11iSlowRoams', 'failedRoams',
                'mdnsTxPackets', 'mdnsRxPackets', 'mdnsDropPackets', 'l2Roams', 'l3Roams',
                'interWncdRoams', 'hwDropsCapwapControl', 'hwDropsCapwapData', 'hwDropsmobilityControl',
                'hwDropsmobilityData', 'hwDropsIpGlean', 'hwDropsIpSg', 'hwDropsIpLearn',
                'hwDropsL2Bridging', 'hwDropsClientUidb', 'hwDropsClientNotFound', 'hwDropsP2PBlock',
                'swDropsCapwapControl', 'swDropsCapwapData', 'swDropsmobilityControl',
                'swDropsmobilityData', 'swDropsIpGlean', 'swDropsIpSg', 'swDropsIpLearn',
                'swDropsL2Bridging', 'swDropsClientUidb', 'swDropsClientNotFound', 'swDropsP2PBlock',
                'puntCapwapControl', 'puntCapwapData', 'puntmobilityControl', 'puntmobilityData',
                'puntDot11IAPP', 'puntDot11RRM', 'puntDot11Dot1x', 'puntWebAuth',
                'puntDot11ProbeRequest', 'puntDot11Rfid', 'puntDot11Mgmt', 'puntCapwapKeepAlive',
                'puntMobilityKeepAlive', 'puntArp', 'puntDhcp', 'puntDhcp6', 'puntIpv6Nd',
                'puntDataGlean', 'puntDataGlean6', 'puntDhcpRelay', 'txBytes', 'rxBytes', 'txPackets',
                'rxPackets', 'txErrorPackets', 'rxErrorPackets', 'txErrorPercentage' and
                'rxErrorPercentage').
            endTime(integer): Devices's End time to which the API queries the dataset related to the resource. It
                must be specified in terms of milliseconds since UNIX epoch. Value is inclusive.
            filters(list): Devices's filters (list of objects).
            groupBy(list): Devices's groupBy (list of strings. Available values are 'id').
            page(object): Devices's page.
            startTime(integer): Devices's Start time from which the API queries the dataset related to the resource.
                It must be specified in terms of milliseconds since UNIX epoch. Value is inclusive.
            trendInterval(string): Devices's The time window to aggregate the metrics.  Interval can be 5 minutes or
                10 minutes or 1 hour or 1 day or 7 days . Available values are '5MIN', '10MIN', '1HR',
                '1DAY' and '7DAY'.
            id(str): id path parameter. The WLC device UUID.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-specific-stats-for-a-w-l-c-over-a-specified-period-of-time-know-your-network
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "startTime": startTime,
            "endTime": endTime,
            "trendInterval": trendInterval,
            "groupBy": groupBy,
            "attributes": attributes,
            "filters": filters,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d811b703a1458fb8c57f7bf6d9f6189_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/wirelessControllersStats/{id}/trendAnal" + "ytics"
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
            "bpm_d811b703a1458fb8c57f7bf6d9f6189_v3_2_3_0", json_data
        )

    def get_trend_analytics_data_of_dns_services_for_given_set_of_complex_filters(
        self,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        page=None,
        startTime=None,
        trendInterval=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Gets the trend analytics data related to DNS Services based on given filters and group by field. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-DNSServices-1.0.0-resolved.yaml.   Gets the trend analytics
        data related to DNS Services based on given filters and group by field. If startTime and endTime are not
        provided, the API defaults to the last 24 hours. Field Name Description startTime start time from which
        API queries the data set related to the resource. It must be specified in UNIX epochtime in
        milliseconds. Value is inclusive & the default is latest endTime end time to which API queries the data
        set related to the resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive
        & the default is latest trendInterval the trend time interval in minutues. This is a mantadory field.
        The possible values in minutes are  30 minutes, 1 hour, 1 day . groupBy specifies the attributes for
        grouping the data. filters used to define one or more conditions. Only the data that satisfy these
        conditions will be taken into consideration during the aggregation calculation. attributes attributes
        are used for obtaining one or more field's data in addition to the aggregated data. The supported
        attributes are listed in  DNSServicesAnalyticsAttributeKey  model aggregateAttributes specifies the
        names of the attributes on which the aggregate function should be applied when querying the data. The
        supported attribute names are listed in  DNSServicesAggregateAttributeKey  model page contains  limit,
        offset, and timestampOrder  fields.  limit  number of records to be returned in response.  offset
        starting offset of data.  timestampOrder  to sort the response based on the timestamp either in
        ascending or descending order.

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's attributes (list of strings).
            endTime(integer): Devices's endTime.
            filters(list): Devices's filters (list of objects).
            groupBy(list): Devices's groupBy (list of strings).
            page(object): Devices's page.
            startTime(integer): Devices's startTime.
            trendInterval(string): Devices's trendInterval.
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
            https://developer.cisco.com/docs/dna-center/#!get-trend-analytics-data-of-d-n-s-services-for-given-set-of-complex-filters
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
            "trendInterval": trendInterval,
            "groupBy": groupBy,
            "filters": filters,
            "attributes": attributes,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a837b8a46cd459c8b429d16fb17f1370_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/dnsServices/trendAnalytics"
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
            "bpm_a837b8a46cd459c8b429d16fb17f1370_v3_2_3_0", json_data
        )

    def get_device_enrichment_details(self, headers=None, **request_parameters):
        """Enriches a given network device context (device id or device Mac Address or device management IP address) with
        details about the device and neighbor topology.

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            list: JSON response. A list of MyDict objects.
            Access the object's properties by using the dot notation
            or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-device-enrichment-details
        """
        check_type(headers, dict)
        if headers is not None:
            if "entity_type" in headers:
                check_type(headers.get("entity_type"), str, may_be_none=False)
            if "entity_value" in headers:
                check_type(headers.get("entity_value"), str, may_be_none=False)
            if "__persistbapioutput" in headers:
                check_type(headers.get("__persistbapioutput"), bool)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v2/device-enrichment-details"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ed54ba7565b85835b0d810f764ac79b7_v3_2_3_0", json_data
        )

    def get_device_enrichment_details_v2(self, headers=None, **query_parameters):
        """Alias for `get_device_enrichment_details <#catalystcentersdk.
        api.v3_2_3_0.devices.
        Devices.get_device_enrichment_details>`_
        """
        return self.get_device_enrichment_details(headers=headers, **query_parameters)

    def the_trend_analytcis_data_for_the_interfaces_in_the_specified_time_range(
        self,
        id,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        startTime=None,
        timestampOrder=None,
        trendIntervalInMinutes=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """The Trend analytcis data for the interface, identified by its instanceUuid, in the specified time range. The
        data is grouped based on the trend time Interval, other input parameters like attributes and aggregate
        attributes. The default time interval range is 3 hours when start and endTime is not provided.  The
        field trendIntervalInMinutes is requiered and either the attributes or the aggregateAttributes fields is
        also required.   For detailed information about the usage of the API, please refer to the Open API
        specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-interfaces-2.0.0-resolved.yaml.   How the filtering behavior
        works   The filters field in each post body can be used in numerous ways:   Each filter in the list of
        filters will applied ''together''   In the example below, this would request filtering the cpu data by
        the  switch 1  cpu indexes.   "filters" : [     {        "key" :  "cpuName" ,        "operator" :
        "like" ,        "value" :  "Switch 1"      } ] .

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's attributes (list of strings).
            endTime(integer): Devices's endTime.
            filters(list): Devices's filters (list of objects).
            startTime(integer): Devices's startTime.
            timestampOrder(string): Devices's timestampOrder.
            trendIntervalInMinutes(integer): Devices's trendIntervalInMinutes.
            id(str): id path parameter. The interface instance Uuid.
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
            https://developer.cisco.com/docs/dna-center/#!the-trend-analytcis-data-for-the-interfaces-in-the-specified-time-range
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "startTime": startTime,
            "endTime": endTime,
            "trendIntervalInMinutes": trendIntervalInMinutes,
            "attributes": attributes,
            "filters": filters,
            "aggregateAttributes": aggregateAttributes,
            "timestampOrder": timestampOrder,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_b9be51e25efc9f41d4f68451f9a6_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/interfaces/{id}/trendAnalytics"
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
            "bpm_b9be51e25efc9f41d4f68451f9a6_v3_2_3_0", json_data
        )

    def gets_the_total_network_device_counts_based_on_the_provided_query_parameters(
        self,
        attribute=None,
        end_time=None,
        family=None,
        health_score=None,
        id=None,
        mac_address=None,
        maintenance_mode=None,
        management_ip_address=None,
        role=None,
        secure_mode=None,
        serial_number=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        software_version=None,
        start_time=None,
        type=None,
        view=None,
        headers=None,
        **request_parameters
    ):
        """Gets the total Network device counts. When there is no start and end time specified returns the latest
        interfaces total count. For detailed information about the usage of the API, please refer to the Open
        API specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-AssuranceNetworkDevices-2.0.1-resolved.yaml.

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to current time. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            id(str): id query parameter. The list of entity Uuids. (Ex."6bef213c-19ca-4170-8375-b694e251101c")
                Examples: id=6bef213c-19ca-4170-8375-b694e251101c (single entity uuid requested) id=6bef
                213c-19ca-4170-8375-b694e251101c&id=32219612-819e-4b5e-a96b-cf22aca13dd9&id=2541e9a7-
                b80d-4955-8aa2-79b233318ba0 (multiple entity uuid with '&' separator) .
            site_hierarchy(str): siteHierarchy query parameter. The full hierarchical breakdown of the site tree
                starting from Global site name and ending with the specific site name. The Root site is
                named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`) This field supports
                wildcard asterisk (*) character search support. E.g. */San*, */San, /San* Examples:
                `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy requested)
                `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global/AreaName2/Bu
                ildingName2/FloorName2` (multiple siteHierarchies requested) .
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site tree
                in id form starting from Global site UUID and ending with the specific site UUID. (Ex.
                `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk (*)
                character search support. E.g. `*uuid*, *uuid, uuid* Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds requested) .
            site_id(str): siteId query parameter. The UUID of the site. (Ex. `flooruuid`) This field supports
                wildcard asterisk (*) character search support. E.g.*flooruuid*, *flooruuid, flooruuid*
                Examples: `?siteId=id1` (single id requested) `?siteId=id1&siteId=id2&siteId=id3`
                (multiple ids requested) .
            management_ip_address(str): managementIpAddress query parameter. The list of entity management IP
                Address. It can be either Ipv4 or Ipv6 address or combination of both(Ex. "121.1.1.10")
                This field supports wildcard (`*`) character-based search.  Ex: `*1.1*` or `1.1*` or
                `*1.1` Examples: managementIpAddresses=121.1.1.10 managementIpAddresses=121.1.1.10&manag
                ementIpAddresses=172.20.1.10&managementIpAddresses=200:10&=managementIpAddresses172.20.3
                .4 (multiple entity IP Address with & separator) .
            mac_address(str): macAddress query parameter. The macAddress of the network device or client This field
                supports wildcard (`*`) character-based search.  Ex: `*AB:AB:AB*` or `AB:AB:AB*` or
                `*AB:AB:AB` Examples: `macAddress=AB:AB:AB:CD:CD:CD` (single macAddress requested)
                `macAddress=AB:AB:AB:CD:CD:DC&macAddress=AB:AB:AB:CD:CD:FE` (multiple macAddress
                requested) .
            family(str): family query parameter. The list of network device family names Examples:family=Switches
                and Hubs (single network device family name )family=Switches and
                Hubs&family=Router&family=Wireless Controller (multiple Network device family names with
                & separator). This field is not case sensitive.
            type(str): type query parameter. The list of network device type This field supports wildcard (`*`)
                character-based search. Ex: `*9407R*` or `*9407R` or `9407R*`Examples:type=SwitchesCisco
                Catalyst 9407R Switch (single network device types )type=Cisco Catalyst 38xx stack-able
                ethernet switch&type=Cisco 3945 Integrated Services Router G2 (multiple Network device
                types with & separator).
            role(str): role query parameter. The list of network device role. Examples:role=CORE,
                role=CORE&role=ACCESS&role=ROUTER (multiple Network device roles with & separator). This
                field is not case sensitive.
            serial_number(str): serialNumber query parameter. The list of network device serial numbers. This field
                supports wildcard (`*`) character-based search.  Ex: `*MS1SV*` or `MS1SV*` or `*MS1SV`
                Examples: serialNumber=9FUFMS1SVAX
                serialNumber=9FUFMS1SVAX&FCW2333Q0BY&FJC240617JX(multiple Network device serial number
                with & separator) .
            maintenance_mode(bool): maintenanceMode query parameter. The device maintenanceMode status true or
                false.
            software_version(str): softwareVersion query parameter. The list of network device software version This
                field supports wildcard (`*`) character-based search. Ex: `*17.8*` or `*17.8` or `17.8*`
                Examples: softwareVersion=2.3.4.0 (single network device software version )
                softwareVersion=17.9.3.23&softwareVersion=17.7.1.2&softwareVersion=*.17.7 (multiple
                Network device software versions with & separator) .
            health_score(str): healthScore query parameter. The list of entity health score categories
                Examples:healthScore=good,healthScore=good&healthScore=fair (multiple entity healthscore
                values with & separator). This field is not case sensitive.
            secure_mode(str): secureMode query parameter. The list of secureMode statuses. Examples:
                secureMode=ENABLED, secureMode=DISABLED&secureMode=NOT_APPLICABLE  Available values :
                ENABLED, DISABLED, NOT_APPLICABLE, UNKNOWN.
            view(str): view query parameter. The List of Network Device model views. Please refer to
                ```NetworkDeviceView``` for the supported list.
            attribute(str): attribute query parameter. The List of Network Device model attributes. This is helps to
                specify the interested fields in the request.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!gets-the-total-network-device-counts-based-on-the-provided-query-parameters
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(id, str)
        check_type(site_hierarchy, str)
        check_type(site_hierarchy_id, str)
        check_type(site_id, str)
        check_type(management_ip_address, str)
        check_type(mac_address, str)
        check_type(family, str)
        check_type(type, str)
        check_type(role, str)
        check_type(serial_number, str)
        check_type(maintenance_mode, bool)
        check_type(software_version, str)
        check_type(health_score, str)
        check_type(secure_mode, str)
        check_type(view, str)
        check_type(attribute, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "id": id,
            "siteHierarchy": site_hierarchy,
            "siteHierarchyId": site_hierarchy_id,
            "siteId": site_id,
            "managementIpAddress": management_ip_address,
            "macAddress": mac_address,
            "family": family,
            "type": type,
            "role": role,
            "serialNumber": serial_number,
            "maintenanceMode": maintenance_mode,
            "softwareVersion": software_version,
            "healthScore": health_score,
            "secureMode": secure_mode,
            "view": view,
            "attribute": attribute,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/networkDevices/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d8782f4d285506d9e1391f0190ff738_v3_2_3_0", json_data
        )

    def retrieves_the_total_number_of_aaa_services_for_given_set_of_complex_filters(
        self,
        endTime=None,
        filters=None,
        startTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Retrieves the total number of AAA Services and offers complex filtering and sorting capabilities. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-AAAServices-1.0.0-resolved.yaml.   Retrieves the total
        number of AAA Services and offers complex filtering and sorting capabilities. If startTime and endTime
        are not provided, the API defaults to the last 24 hours. Field Name Description startTime start time
        from which API queries the data set related to the resource. It must be specified in UNIX epochtime in
        milliseconds. Value is inclusive & the default is 24 hours ago from end time endTime end time to which
        API queries the data set related to the resource. It must be specified in UNIX epochtime in
        milliseconds. Value is inclusive & the default is current time filters used to define one or more
        conditions. Only the data that satisfy these conditions will be taken into consideration during the
        aggregation calculation.

        Args:
            endTime(integer): Devices's endTime.
            filters(list): Devices's filters (list of objects).
            startTime(integer): Devices's startTime.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-total-number-of-a-a-a-services-for-given-set-of-complex-filters
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
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator("jsd_adfc115d6888722b71811ac96e_v3_2_3_0").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/aaaServices/query/count"
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
            "bpm_adfc115d6888722b71811ac96e_v3_2_3_0", json_data
        )

    def get_device_values_that_match_fully_or_partially_an_attribute(
        self,
        associated_wlc_ip=None,
        collection_interval=None,
        collection_status=None,
        error_code=None,
        family=None,
        hostname=None,
        limit=None,
        mac_address=None,
        management_ip_address=None,
        offset=None,
        platform_id=None,
        reachability_failure_reason=None,
        reachability_status=None,
        role=None,
        role_source=None,
        serial_number=None,
        series=None,
        software_type=None,
        software_version=None,
        type=None,
        up_time=None,
        vrf_name=None,
        headers=None,
        **request_parameters
    ):
        """Returns the list of values of the first given required parameter. You can use the .* in any value to conduct a
        wildcard search. For example, to get all the devices with the management IP address starting with 10.10.
        , issue the following request: GET /dna/intent/api/v1/network-
        device/autocomplete?managementIpAddress=10.10..* It will return the device management IP addresses that
        match fully or partially the provided attribute. {[10.10.1.1, 10.10.20.2, …]}. The API returns a
        paginated response based on 'limit' and 'offset' parameters, allowing up to 500 records per page.
        'limit' specifies the number of records, and 'offset' sets the starting point using 1-based indexing.
        For data sets over 500 records, make multiple calls, adjusting 'limit' and 'offset' to retrieve all
        records incrementally.

        Args:
            vrf_name(str): vrfName query parameter.
            management_ip_address(str): managementIpAddress query parameter.
            hostname(str): hostname query parameter.
            mac_address(str): macAddress query parameter.
            family(str): family query parameter.
            collection_status(str): collectionStatus query parameter.
            collection_interval(str): collectionInterval query parameter.
            software_version(str): softwareVersion query parameter.
            software_type(str): softwareType query parameter.
            reachability_status(str): reachabilityStatus query parameter.
            reachability_failure_reason(str): reachabilityFailureReason query parameter.
            error_code(str): errorCode query parameter.
            platform_id(str): platformId query parameter.
            series(str): series query parameter.
            type(str): type query parameter.
            serial_number(str): serialNumber query parameter.
            up_time(str): upTime query parameter.
            role(str): role query parameter.
            role_source(str): roleSource query parameter.
            associated_wlc_ip(str): associatedWlcIp query parameter.
            offset(int): offset query parameter.
            limit(int): limit query parameter. The number of records to show for this page. Min: 1, Max: 500.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-device-values-that-match-fully-or-partially-an-attribute
        """
        check_type(headers, dict)
        check_type(vrf_name, str)
        check_type(management_ip_address, str)
        check_type(hostname, str)
        check_type(mac_address, str)
        check_type(family, str)
        check_type(collection_status, str)
        check_type(collection_interval, str)
        check_type(software_version, str)
        check_type(software_type, str)
        check_type(reachability_status, str)
        check_type(reachability_failure_reason, str)
        check_type(error_code, str)
        check_type(platform_id, str)
        check_type(series, str)
        check_type(type, str)
        check_type(serial_number, str)
        check_type(up_time, str)
        check_type(role, str)
        check_type(role_source, str)
        check_type(associated_wlc_ip, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "vrfName": vrf_name,
            "managementIpAddress": management_ip_address,
            "hostname": hostname,
            "macAddress": mac_address,
            "family": family,
            "collectionStatus": collection_status,
            "collectionInterval": collection_interval,
            "softwareVersion": software_version,
            "softwareType": software_type,
            "reachabilityStatus": reachability_status,
            "reachabilityFailureReason": reachability_failure_reason,
            "errorCode": error_code,
            "platformId": platform_id,
            "series": series,
            "type": type,
            "serialNumber": serial_number,
            "upTime": up_time,
            "role": role,
            "roleSource": role_source,
            "associatedWlcIp": associated_wlc_ip,
            "offset": offset,
            "limit": limit,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/autocomplete"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b5a5c8da4aaa526da6a06e97c80a38be_v3_2_3_0", json_data
        )

    def device_enrichment_details(self, headers=None, **request_parameters):
        """Enriches a given network device context (device id or device Mac Address or device management IP address) with
        details about the device and neighbor topology.

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            list: JSON response. A list of MyDict objects.
            Access the object's properties by using the dot notation
            or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!device-enrichment-details
        """
        check_type(headers, dict)
        if headers is not None:
            if "entityType" in headers:
                check_type(headers.get("entityType"), str, may_be_none=False)
            if "entityValue" in headers:
                check_type(headers.get("entityValue"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/deviceEnrichmentDetails"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e0994dc92565d2a865dd2eac9c06c41_v3_2_3_0", json_data
        )
