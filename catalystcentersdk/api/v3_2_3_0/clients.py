"""Cisco Catalyst Center Clients API wrapper.

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


class Clients:
    """Cisco Catalyst Center Clients API (version: 3.2.3.0).

    Wraps the Catalyst Center Clients
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Clients
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

    def get_client_detail(
        self, mac_address, timestamp=None, headers=None, **request_parameters
    ):
        """Returns detailed Client information retrieved by Mac Address for any given point of time.  Returns detailed
        Client information retrieved by Mac Address for any given point of time.

        Args:
            mac_address(str): macAddress query parameter. MAC Address of the client.
            timestamp(int): timestamp query parameter. Epoch time(in milliseconds) when the Client health data is
                required.
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
            https://developer.cisco.com/docs/dna-center/#!get-client-detail
        """
        check_type(headers, dict)
        check_type(mac_address, str, may_be_none=False)
        check_type(timestamp, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "macAddress": mac_address,
            "timestamp": timestamp,
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

        e_url = "/dna/intent/api/v1/client-detail"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f2c6333d8eb05491a16c2d32095e4352_v3_2_3_0", json_data
        )

    def count_clients_energy_from_query(
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
        """Retrieves the total count of client devices based on the specified complex filters. For detailed information
        about the usage of the API, please refer to the Open API specification document
        - https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-deviceEnergy_1.0-1.0.1-resolved.yaml.  Retrieves the total
        count of client devices based on the specified complex filters. The request payload format is similar to
        that used with the query API.

        Args:
            aggregateAttributes(list): Clients's aggregateAttributes (list of objects).
            attributes(list): Clients's attributes (list of strings).
            endTime(integer): Clients's endTime.
            filters(list): Clients's filters (list of objects).
            page(object): Clients's page.
            startTime(integer): Clients's startTime.
            views(list): Clients's views (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!count-clients-energy-from-query
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
                "jsd_c765afc72581d862cd61f5139d224_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/energy/clients/query/count"
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
            "bpm_c765afc72581d862cd61f5139d224_v3_2_3_0", json_data
        )

    def retrieves_the_trend_analytics_data_related_to_clients(
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
        """Retrieves the trend analytics of client data for the specified time range. The data will be grouped based on the
        given trend time interval. This API facilitates obtaining consolidated insights into the performance and
        status of the clients over the specified start and end time. For detailed information about the usage of
        the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        clients1-3.2.3-resolved.yaml.   Retrieves the trend analytics of client data for the specified time
        range. The data will be grouped based on the given trend time interval. This API facilitates obtaining
        consolidated insights into the performance and status of the clients over the specified start and end
        time. If startTime and endTime are not provided, the API defaults to the last 24 hours.   The input
        payload contains the following fields,         Field Name   Description           startTime   The start
        time indicates when the API begins retrieving data related to the resource. It must be specified in the
        UNIX epoch time format, measured in milliseconds. This value is inclusive, and if left unspecified, the
        default is 1 day before the  endTime.       endTime   The end time indicates the upper limit until which
        the API retrieves data related to the resource. It must be defined in the UNIX epoch time format,
        measured in milliseconds. This value is inclusive, and if left unspecified, the default is the latest
        available data.       trendInterval   The time window for aggregating metrics. This is a mandatory
        request field. Possible values include  5 minutes, 10 minutes, 1 hour, 1 day, or 7 days .       groupBy
        Specifies the attributes for grouping the data. Refer to  ClientGroupByField  model for the supported
        grouping attributes       attributes   A list of attributes associated with the resource, which can be
        requested to be included in the response alongside the required attributes. Refer to  ClientAttribute
        model for the supported attributes       aggregateAttributes   This specifies the attribute name and the
        function to be applied during data querying. The aggregate function is then applied to data within the
        specified start and end times. Refer to  ClientAggregateField  model for the supported aggregate
        attributes       filters   This is used to specify one or more conditions for filtering the queried
        data. Refer to  ClientFilterField  model for the supported filters       page   It includes the  limit,
        cursor, and timeSortOrder  fields.  limit  denotes the number of records to retrieve per page,  cursor
        signifies the initial data position, and  timeSortOrder  is used sort the response based on the
        timestamp either in ascending or descending order.      .

        Args:
            aggregateAttributes(list): Clients's aggregateAttributes (list of objects).
            attributes(list): Clients's attributes (list of strings).
            endTime(integer): Clients's endTime.
            filters(list): Clients's filters (list of objects).
            groupBy(list): Clients's groupBy (list of strings).
            page(object): Clients's page.
            startTime(integer): Clients's startTime.
            trendInterval(string): Clients's trendInterval.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-trend-analytics-data-related-to-clients
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
            "attributes": attributes,
            "filters": filters,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ffd2fefb57d5523c87a5d941eb93ddc3_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/clients/trendAnalytics"
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
            "bpm_ffd2fefb57d5523c87a5d941eb93ddc3_v3_2_3_0", json_data
        )

    def retrieves_specific_client_information_matching_the_macaddress(
        self,
        id,
        attribute=None,
        end_time=None,
        start_time=None,
        view=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves specific client information matching the MAC address. For detailed information about the usage of the
        API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        clients1-3.2.3-resolved.yaml.   Retrieves specific client information matching the MAC address. Mac can
        be specified is any notational conventions  01:23:45:67:89:AB  or  01-23-45-67-89-AB  or  0123.4567.89AB
        and is case insensitive. If startTime and endTime are not provided, the API defaults to the last 24
        hours.

        Args:
            id(str): id path parameter. id is the client mac address. It can be specified is any notational
                conventions  01:23:45:67:89:AB or 01-23-45-67-89-AB or 0123.4567.89AB and is case
                insensitive .
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to current time. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            view(str): view query parameter. Client related Views Refer to ClientView schema for list of views
                supported Examples: `view=Wireless` (single view requested)
                `view=WirelessHealth&view=WirelessTraffic` (multiple view requested) .
            attribute(str): attribute query parameter. List of attributes related to resource that can be requested
                to only be part of the response along with the required attributes. Refer to
                ClientAttribute schema for list of attributes supported Examples: `attribute=band`
                (single attribute requested) `attribute=band&attribute=ssid&attribute=overallScore`
                (multiple attribute requested).
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-specific-client-information-matching-the-m-a-c-address
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

        e_url = "/dna/data/api/v1/clients/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ee00176282fd54ef90fc96a2c23d50ec_v3_2_3_0", json_data
        )

    def retrieves_the_number_of_clients_by_applying_complex_filters(
        self,
        endTime=None,
        filters=None,
        startTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Retrieves the number of clients by applying complex filters. For detailed information about the usage of the
        API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        clients1-3.2.3-resolved.yaml.   Retrieves the number of clients by applying complex filters. If
        startTime and endTime are not provided, the API defaults to the last 24 hours.   The input payload
        contains the following fields,         Field Name   Description           startTime   The start time
        indicates when the API begins retrieving data related to the resource. It must be specified in the UNIX
        epoch time format, measured in milliseconds. This value is inclusive, and if left unspecified, the
        default is 1 day before the endTime.       endTime   The end time indicates the upper limit until which
        the API retrieves data related to the resource. It must be defined in the UNIX epoch time format,
        measured in milliseconds. This value is inclusive, and if left unspecified, the default is the latest
        available data.       filters   This is used to specify one or more conditions for filtering the queried
        data. Refer to  ClientFilterField  model for the supported filters         How the filtering behavior
        works   The  filters  field in each post body can be used in various ways:   Each filter in the list of
        filters will be applied simultaneously.   For instance, the following example would request filtering to
        retrieve clients with an RSSI value greater than -50 dBm and a osType of either iOS or Android.
        "filters" : [   {      "key" :  "rssi" ,      "operator" :  "gt" ,      "value" :  -50    },   {
        "key" :  "osType" ,      "operator" :  "in" ,      "value" : [        "iOS" ,        "Android"      ]
        } ]  Each filter object can utilize its logical operator differently to offer nested filtering
        functionality.   In the example below, you can observe a logical  OR  filter being applied using the
        nested filtering functionality:   The main filter object doesn't have its  key ,  value , or  operator
        fields populated. Only the  logicalOperator  field is populated to indicate that the filters within the
        nested filters list are to be logically combined.   "filters" : [   {      "logicalOperator" :  "or" ,
        "filters" : [       {          "key" :  "vlanId" ,          "operator" :  "eq" ,          "value" :  187
        },       {          "key" :  "siteHierarchy" ,          "operator" :  "in" ,          "value" : [
        "Global/San Jose" ,  "Global/SFO" ]       }     ]   } ] .

        Args:
            endTime(integer): Clients's endTime.
            filters(list): Clients's filters (list of objects).
            startTime(integer): Clients's startTime.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-number-of-clients-by-applying-complex-filters
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
                "jsd_a2131eae5c1d8e73cd55eebf6a83_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/clients/query/count"
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
            "bpm_a2131eae5c1d8e73cd55eebf6a83_v3_2_3_0", json_data
        )

    def bulk_partially_update_tracked_client_configurations(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Partially updates multiple MAC-based tracked-client configurations in one request. Catalyst Center supports up
        to 2000 tracked-client configurations at a time. Each item is processed independently. Omitted fields
        keep their existing values. Each item must include `clientMacAddress` and at least one of `description`,
        `trackingStartTime`, `trackingEndTime`, or `notificationModes`. Use `trackingStartTime: 0` to restart
        tracking at the current server time and `trackingEndTime: 0` for never-expiring tracking. Unknown
        `clientMacAddress` targets are returned as item-level `FAILURE` results and are not created as a side
        effect of bulk update.

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
            https://developer.cisco.com/docs/dna-center/#!bulk-partially-update-tracked-client-configurations
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
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
                "jsd_af6fde67f553adb676018b3faa4b99_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/trackedClients/bulkUpdate"
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
            "bpm_af6fde67f553adb676018b3faa4b99_v3_2_3_0", json_data
        )

    def bulk_create_tracked_client_configurations(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Creates multiple MAC-based tracked-client configurations in one request. Catalyst Center supports up to 2000
        tracked-client configurations at a time.  All fields in each create item are mandatory. Use an empty
        string for `description` when no description is needed, `trackingStartTime: 0` to start tracking at the
        current server time, and `trackingEndTime: 0` for never-expiring tracking. Each item is processed
        independently. If processing an item would cause the total tracked-client configuration count to exceed
        2000, that item is returned as a failed result.

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
            https://developer.cisco.com/docs/dna-center/#!bulk-create-tracked-client-configurations
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
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
                "jsd_c1221ca877851709e4bd9c9018b5eb4_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/trackedClients/bulkCreate"
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
            "bpm_c1221ca877851709e4bd9c9018b5eb4_v3_2_3_0", json_data
        )

    def get_overall_client_health(
        self, timestamp=None, headers=None, **request_parameters
    ):
        """Returns Overall Client Health information by Client type (Wired and Wireless) for any given point of time.
        Returns Overall Client Health information by Client type (Wired and Wireless) for any given point of
        time.

        Args:
            timestamp(int): timestamp query parameter. Epoch time(in milliseconds) when the Client health data is
                required.
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
            https://developer.cisco.com/docs/dna-center/#!get-overall-client-health
        """
        check_type(headers, dict)
        check_type(timestamp, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "timestamp": timestamp,
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

        e_url = "/dna/intent/api/v1/client-health"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f58ddf5cee095688aed79a9bb26e21e8_v3_2_3_0", json_data
        )

    def query_clients_energy(
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
        """Retrieves a list of client devices along with their energy data for a specified time range, based on the filters
        provided in the request body. For detailed information about the usage of the API, please refer to the
        Open API specification document - https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-deviceEnergy_1.0-1.0.1-resolved.yaml.   Retrieves a list of
        client devices along with their energy data for a specified time range, based on the filters provided in
        the request body. The input payload contains the following fields: Field Name Description startTime
        Start time from which API queries the data set related to the resource. It must be specified in UNIX
        epochtime in milliseconds. Value is inclusive. If startTime is not provided, API will default to one day
        before endTime . endTime End time to which API queries the data set related to the resource. It must be
        specified in UNIX epochtime in milliseconds. Value is inclusive. If endTime is not provided, API will
        default to one day after startTime . If startTime is not provided either, API will default to current
        time. attributes An optional filed that is used to get certain attributes in the response. The supported
        attributes are listed in clientDeviceEnergyAttributes model. Note: When view and attributes have
        different variants, the attributes returned in the response will be the union of both sets. views An
        optional field, similar to attributes, is useful when a large number of fields are required in the
        response data. The supported logical views and their respective fields are available in
        clientDeviceEnergyViews filters Used to define one or more filter conditions. Only devices that satisfy
        these conditions will be taken into consideration during the aggregation calculation. This field can be
        empty. The supported list of filter keys and operators are: "siteId" ["eq", "in"],"siteHierarchy"-["in",
        "eq", "like"], "siteHierarchyId" ["in", "eq", "like"], "deviceCategory" [in, eq], "deviceSubCategory"
        [in, eq], "Id" [in, eq] . aggregateAttributes specifies the name of the attribute on which the aggregate
        function should be applied when querying the data. The supported attribute names are listed in
        DevicesEnergyAggregateAttribute model. Supported functions today are just sum page Contains  limit,
        cursor and sortBy  fields.  limit Number of records to fetch in a page,  cursor string field indicating
        the next record in the response list and  sortBy  attribute name, order and function if you want to sort
        by the aggregated field.  sortBy  field is a list, but only single field sorting is supported on this
        API. Please refer to the 'API Support Documentation' section to understand which fields and filters are
        supported. How Pagination Works 'limit' field, is the total number of records you want to retrieve.
        'cursor' field, indicating the next record in the response list. If you have a limit of 100, each page
        would be viewed as 100 elements. So starting with an empty cursor, means look at the first page
        (starting from first record). To get the second page, you need to specify cursor returned in the
        response of the first request.  'sortBy' field is a list, but only single field sorting is supported on
        this API, with 'asc' (ascending), or 'desc' (descending) ordering.

        Args:
            aggregateAttributes(list): Clients's aggregateAttributes (list of objects).
            attributes(list): Clients's attributes (list of strings).
            endTime(integer): Clients's endTime.
            filters(list): Clients's filters (list of objects).
            page(object): Clients's page.
            startTime(integer): Clients's startTime.
            views(list): Clients's views (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!query-clients-energy
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
            self._request_validator("jsd_c536ac5a318629fc3d6b3dc236_v3_2_3_0").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/energy/clients/query"
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
            "bpm_c536ac5a318629fc3d6b3dc236_v3_2_3_0", json_data
        )

    def bulk_delete_tracked_client_configurations(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Deletes multiple tracked-client configurations in one request. Supports up to 2000 items. Returns one result per
        input item, including item-level validation or processing failures.

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
            https://developer.cisco.com/docs/dna-center/#!bulk-delete-tracked-client-configurations
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
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
                "jsd_b9fc70165c74b2ceadefc8e865d8_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/trackedClients/bulkDelete"
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
            "bpm_b9fc70165c74b2ceadefc8e865d8_v3_2_3_0", json_data
        )

    def delete_a_tracked_client_configuration(
        self, id, headers=None, **request_parameters
    ):
        """Deletes the tracked-client configuration for the given client identifier.

        Args:
            id(str): id path parameter. Tracked-client identifier. This is the MAC address stored on the tracked-
                client configuration. The stored identifier may be either the client's canonical MAC
                address or a randomized MAC address. Correlated randomized MACs listed in
                `randomizedMacAddresses` are not interchangeable resource identifiers for this path.
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
            https://developer.cisco.com/docs/dna-center/#!delete-a-tracked-client-configuration
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

        e_url = "/dna/intent/api/v1/trackedClients/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d151416d357d585e86311d5ac83b2_v3_2_3_0", json_data
        )

    def partially_update_a_tracked_client_configuration(
        self,
        id,
        description=None,
        notificationModes=None,
        trackingEndTime=None,
        trackingStartTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Partially updates a MAC-based tracked-client configuration for the given client identifier. Omitted fields keep
        their existing values. At least one of `description`, `trackingStartTime`, `trackingEndTime`, or
        `notificationModes` must be supplied. Use `trackingStartTime: 0` to restart tracking at the current
        server time and `trackingEndTime: 0` for never-expiring tracking.

        Args:
            description(string): Clients's User-provided description for the tracked client. Omit to keep the
                current value.
            notificationModes(list): Clients's Enabled notification modes for the tracked client. Omit to keep the
                current value. (list of strings. Available values are 'CONNECT_FIRST', 'CONNECT_EVERY'
                and 'DISCONNECT_EVERY').
            trackingEndTime(integer): Clients's End time of the active tracking interval in UNIX epoch time
                milliseconds. Use `0` for never-expiring tracking. Omit to keep the current value.
            trackingStartTime(integer): Clients's Start time of the active tracking interval in UNIX epoch time
                milliseconds. Use `0` to restart tracking at the current server time. Omit to keep the
                current value.
            id(str): id path parameter. Tracked-client identifier. This is the MAC address stored on the tracked-
                client configuration. The stored identifier may be either the client's canonical MAC
                address or a randomized MAC address. Correlated randomized MACs listed in
                `randomizedMacAddresses` are not interchangeable resource identifiers for this path.
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
            https://developer.cisco.com/docs/dna-center/#!partially-update-a-tracked-client-configuration
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
            "description": description,
            "trackingStartTime": trackingStartTime,
            "trackingEndTime": trackingEndTime,
            "notificationModes": notificationModes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_b8a6230e35dfcb963789b9224665c_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/trackedClients/{id}"
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
            "bpm_b8a6230e35dfcb963789b9224665c_v3_2_3_0", json_data
        )

    def read_a_tracked_client_configuration_by_client_identifier(
        self, id, headers=None, **request_parameters
    ):
        """Returns one tracked-client configuration for the given client identifier.

        Args:
            id(str): id path parameter. Tracked-client identifier. This is the MAC address stored on the tracked-
                client configuration. The stored identifier may be either the client's canonical MAC
                address or a randomized MAC address. Correlated randomized MACs listed in
                `randomizedMacAddresses` are not interchangeable resource identifiers for this path.
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
            https://developer.cisco.com/docs/dna-center/#!read-a-tracked-client-configuration-by-client-identifier
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

        e_url = "/dna/intent/api/v1/trackedClients/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d281f68f97eb5c0786c62a37169e8e05_v3_2_3_0", json_data
        )

    def read_tracked_client_configurations(
        self,
        client_mac_address=None,
        description=None,
        duid=None,
        is_present_on_network=None,
        limit=None,
        notification_modes=None,
        offset=None,
        randomized_mac_addresses=None,
        headers=None,
        **request_parameters
    ):
        """Returns tracked-client configurations for the customer-facing intent API.

        Args:
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1.
            limit(int): limit query parameter. Maximum number of records to return.
            client_mac_address(list, set, str, tuple): clientMacAddress query parameter. Up to 10 stored tracked-
                client identifiers to match. Each value is matched against the MAC address stored on the
                tracked-client configuration. The stored identifier may be either the client's canonical
                MAC address or a randomized MAC address. To filter by correlated randomized MAC aliases,
                use `randomizedMacAddresses`. Invalid MAC address values are rejected.
            duid(list, set, str, tuple): duid query parameter. Up to 10 DUID values to match. A DUID is the device
                identifier used to correlate related randomized MACs for the same client.
            description(str): description query parameter. Exact-match description value for tracked-client
                configurations. This parameter uses `eq` semantics only. For partial matching or other
                request-body filter combinations, use `POST /intent/api/v1/trackedClients/query`.
            notification_modes(list, set, str, tuple): notificationModes query parameter. One or more notification
                modes to match. Supported values are `CONNECT_FIRST`, `CONNECT_EVERY`, and
                `DISCONNECT_EVERY`.
            is_present_on_network(bool): isPresentOnNetwork query parameter. Match tracked-client configurations by
                whether the client is present on the network within the last 28 days.
            randomized_mac_addresses(list, set, str, tuple): randomizedMacAddresses query parameter. Up to 10
                randomized MAC addresses to match against the tracked client. These addresses are
                matched through the client-correlation data associated with the DUID when available.
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
            https://developer.cisco.com/docs/dna-center/#!read-tracked-client-configurations
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(client_mac_address, (list, set, str, tuple))
        check_type(duid, (list, set, str, tuple))
        check_type(description, str)
        check_type(notification_modes, (list, set, str, tuple))
        check_type(is_present_on_network, bool)
        check_type(randomized_mac_addresses, (list, set, str, tuple))
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "offset": offset,
            "limit": limit,
            "clientMacAddress": client_mac_address,
            "duid": duid,
            "description": description,
            "notificationModes": notification_modes,
            "isPresentOnNetwork": is_present_on_network,
            "randomizedMacAddresses": randomized_mac_addresses,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/trackedClients"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ad83217ad85b4797701edcc9b11ebc_v3_2_3_0", json_data
        )

    def create_a_tracked_client_configuration(
        self,
        clientMacAddress=None,
        description=None,
        notificationModes=None,
        trackingEndTime=None,
        trackingStartTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Creates one MAC-based tracked-client configuration through the customer-facing intent API. All create fields are
        mandatory. Use an empty string for `description` when no description is needed, `trackingStartTime: 0`
        to start tracking at the current server time, and `trackingEndTime: 0` for never-expiring tracking.

        Args:
            clientMacAddress(string): Clients's MAC address stored as the tracked-client configuration identifier.
                The stored identifier may be either the client's canonical MAC address or a randomized
                MAC address.
            description(string): Clients's User-provided description for the tracked client. Use an empty string
                when no description is needed.
            notificationModes(list): Clients's Enabled notification modes for the tracked client. (list of strings.
                Available values are 'CONNECT_FIRST', 'CONNECT_EVERY' and 'DISCONNECT_EVERY').
            trackingEndTime(integer): Clients's End time of the active tracking interval in UNIX epoch time
                milliseconds. Use `0` for never-expiring tracking.
            trackingStartTime(integer): Clients's Start time of the active tracking interval in UNIX epoch time
                milliseconds. Use `0` to start tracking at the current server time.
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
            https://developer.cisco.com/docs/dna-center/#!create-a-tracked-client-configuration
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
            "clientMacAddress": clientMacAddress,
            "description": description,
            "trackingStartTime": trackingStartTime,
            "trackingEndTime": trackingEndTime,
            "notificationModes": notificationModes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_b42c79f45e21549aa5845b3656852de8_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/trackedClients"
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
            "bpm_b42c79f45e21549aa5845b3656852de8_v3_2_3_0", json_data
        )

    def count_clients_energy(
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
        """Retrieves the total count of client devices that provide energy data, filtered according to the specified query
        parameters. For detailed information about the usage of the API, please refer to the Open API
        specification document - https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-deviceEnergy_1.0-1.0.1-resolved.yaml.  Retrieves the total
        count of client devices that provide energy data, filtered according to the specified query parameters.

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to one day before `endTime`.
                .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. If
                `endTime` is not provided, API will default to one day after `startTime`. If `startTime`
                is not provided either, API will default to current time. .
            id(str): id query parameter. The list of Mac addresses (e.g., `54:9F:C6:43:FF:80`). Examples:
                `id=54:9F:C6:43:FF:80` (single device requested)
                `id=54:9F:C6:43:FF:80&id=01:23:45:67:89:AB` .
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
                `deviceCategory=AccessPoint` (single device family requested)
                `deviceCategory=AccessPoint&deviceCategory=OtherPOEDevice` (multiple device categories
                with comma separator) .
            device_sub_category(str): deviceSubCategory query parameter. The list of device sub categories.
                Examples: `deviceSubCategory=IP Phone 7821` (single sub category requested)
                `deviceSubCategory=IP Phone 7821&deviceSubCategory=IEEE PD` .
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
            https://developer.cisco.com/docs/dna-center/#!count-clients-energy
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

        e_url = "/dna/data/api/v1/energy/clients/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bc8798815ab89147f2054720da4d_v3_2_3_0", json_data
        )

    def retrieves_the_list_of_clients_while_also_offering_basic_filtering_and_sorting_capabilities(
        self,
        attribute=None,
        band=None,
        connected_network_device_name=None,
        end_time=None,
        ipv4_address=None,
        ipv6_address=None,
        limit=None,
        mac_address=None,
        offset=None,
        order=None,
        os_type=None,
        os_version=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        sort_by=None,
        ssid=None,
        start_time=None,
        type=None,
        view=None,
        wlc_name=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the list of clients, while also offering basic filtering and sorting capabilities. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-clients1-3.2.3-resolved.yaml.   Retrieves the list of
        clients, while also offering basic filtering and sorting capabilities. If startTime and endTime are not
        provided, the API defaults to the last 24 hours.

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
            type(str): type query parameter. The client device type whether client is connected to network through
                Wired or Wireless medium. .
            os_type(str): osType query parameter. Client device operating system type. This field supports wildcard
                (`*`) character-based search. If the value contains the (`*`) character, please use the
                /query API for regex search.  Ex: `*iOS*` or `iOS*` or `*iOS` Examples: `osType=iOS`
                (single osType requested) `osType=iOS&osType=Android` (multiple osType requested) .
            os_version(str): osVersion query parameter. Client device operating system version This field supports
                wildcard (`*`) character-based search. If the value contains the (`*`) character, please
                use the /query API for regex search.  Ex: `*14.3*` or `14.3*` or `*14.3` Examples:
                `osVersion=14.3` (single osVersion requested) `osVersion=14.3&osVersion=10.1` (multiple
                osVersion requested) .
            site_hierarchy(str): siteHierarchy query parameter. The full hierarchical breakdown of the site tree
                starting from Global site name and ending with the specific site name. The Root site is
                named "Global" (Ex. "Global/AreaName/BuildingName/FloorName") This field supports
                wildcard (`*`) character-based search. If the value contains the (`*`) character, please
                use the /query API for regex search.  Ex: `*BuildingName*` or `BuildingName*` or
                `*BuildingName` Examples: `siteHierarchy=Global/AreaName/BuildingName/FloorName` (single
                siteHierarchy requested) `siteHierarchy=Global/AreaName/BuildingName1/FloorName1&siteHie
                rarchy=Global/AreaName/BuildingName1/FloorName2` (multiple siteHierarchy requested).
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site tree
                in id form starting from Global site UUID and ending with the specific site UUID. (Ex.
                "globalUuid/areaUuid/buildingUuid/floorUuid") This field supports wildcard (`*`)
                character-based search.  Ex: `*buildingUuid*` or `buildingUuid*` or `*buildingUuid`
                Examples: `siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid` (single
                siteHierarchyId requested) `siteHierarchyId=globalUuid/areaUuid/buildingUuid1/floorUuid1
                &siteHierarchyId=globalUuid/areaUuid/buildingUuid1/floorUuid2` (multiple siteHierarchyId
                requested).
            site_id(str): siteId query parameter. The site UUID without the top level hierarchy. (Ex."floorUuid")
                Examples: `siteId=floorUuid` (single siteId requested)
                `siteId=floorUuid1&siteId=floorUuid2` (multiple siteId requested).
            ipv4_address(str): ipv4Address query parameter. IPv4 Address of the network entity either network device
                or client This field supports wildcard (`*`) character-based search.  Ex: `*1.1*` or
                `1.1*` or `*1.1` Examples: `ipv4Address=1.1.1.1` (single ipv4Address requested)
                `ipv4Address=1.1.1.1&ipv4Address=2.2.2.2` (multiple ipv4Address requested) .
            ipv6_address(str): ipv6Address query parameter. IPv6 Address of the network entity either network device
                or client This field supports wildcard (`*`) character-based search. Ex: `*2001:db8*` or
                `2001:db8*` or `*2001:db8` Examples: `ipv6Address=2001:db8:0:0:0:0:2:1` (single
                ipv6Address requested)
                `ipv6Address=2001:db8:0:0:0:0:2:1&ipv6Address=2001:db8:85a3:8d3:1319:8a2e:370:7348`
                (multiple ipv6Address requested) .
            mac_address(str): macAddress query parameter. The macAddress of the network device or client This field
                supports wildcard (`*`) character-based search.  Ex: `*AB:AB:AB*` or `AB:AB:AB*` or
                `*AB:AB:AB` Examples: `macAddress=AB:AB:AB:CD:CD:CD` (single macAddress requested)
                `macAddress=AB:AB:AB:CD:CD:DC&macAddress=AB:AB:AB:CD:CD:FE` (multiple macAddress
                requested) .
            wlc_name(str): wlcName query parameter. Wireless Controller name that reports the wireless client. This
                field supports wildcard (`*`) character-based search. If the value contains the (`*`)
                character, please use the /query API for regex search. Ex: `*wlc-25*` or `wlc-25*` or
                `*wlc-25` Examples: `wlcName=wlc-25` (single wlcName requested) `wlcName=wlc-25&wlc-34`
                (multiple wlcName requested) .
            connected_network_device_name(str): connectedNetworkDeviceName query parameter. Name of the neighbor
                network device that client is connected to. This field supports wildcard (`*`)
                character-based search. If the value contains the (`*`) character, please use the /query
                API for regex search. Ex: `*ap-25*` or `ap-25*` or `*ap-25` Examples:
                `connectedNetworkDeviceName=ap-25` (single connectedNetworkDeviceName requested)
                `connectedNetworkDeviceName=ap-25&ap-34` (multiple connectedNetworkDeviceName requested)
                .
            ssid(str): ssid query parameter. SSID is the name of wireless network to which client connects to. It is
                also referred to as WLAN ID Wireless Local Area Network Identifier. This field supports
                wildcard (`*`) character-based search. If the value contains the (`*`) character, please
                use the /query API for regex search.  Ex: `*Alpha*` or `Alpha*` or `*Alpha` Examples:
                `ssid=Alpha` (single ssid requested) `ssid=Alpha&ssid=Guest` (multiple ssid requested) .
            band(str): band query parameter. WiFi frequency band that client or Access Point operates. Band value is
                represented in Giga Hertz GHz Examples: `band=5GHZ` (single band requested)
                `band=2.4GHZ&band=6GHZ` (multiple band requested) .
            view(str): view query parameter. Client related Views Refer to ClientView schema for list of views
                supported Examples: `view=Wireless` (single view requested)
                `view=WirelessHealth&view=WirelessTraffic` (multiple view requested) .
            attribute(str): attribute query parameter. List of attributes related to resource that can be requested
                to only be part of the response along with the required attributes. Refer to
                ClientAttribute schema for list of attributes supported Examples: `attribute=band`
                (single attribute requested) `attribute=band&attribute=ssid&attribute=overallScore`
                (multiple attribute requested).
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-clients_-while-also-offering-basic-filtering-and-sorting-capabilities
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(limit, int)
        check_type(offset, int)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(type, str)
        check_type(os_type, str)
        check_type(os_version, str)
        check_type(site_hierarchy, str)
        check_type(site_hierarchy_id, str)
        check_type(site_id, str)
        check_type(ipv4_address, str)
        check_type(ipv6_address, str)
        check_type(mac_address, str)
        check_type(wlc_name, str)
        check_type(connected_network_device_name, str)
        check_type(ssid, str)
        check_type(band, str)
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
            "offset": offset,
            "sortBy": sort_by,
            "order": order,
            "type": type,
            "osType": os_type,
            "osVersion": os_version,
            "siteHierarchy": site_hierarchy,
            "siteHierarchyId": site_hierarchy_id,
            "siteId": site_id,
            "ipv4Address": ipv4_address,
            "ipv6Address": ipv6_address,
            "macAddress": mac_address,
            "wlcName": wlc_name,
            "connectedNetworkDeviceName": connected_network_device_name,
            "ssid": ssid,
            "band": band,
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

        e_url = "/dna/data/api/v1/clients"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dfcf64acc1815459acc146cd924e9877_v3_2_3_0", json_data
        )

    def query_tracked_client_configurations_with_request_body_filters(
        self,
        filters=None,
        page=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Returns tracked-client configurations matching the provided request-body filters. Top-level filters are combined
        with logical AND. To express OR logic, wrap child clauses inside a filter object that contains
        `logicalOperator` and nested `filters`. Only one level of nested filters is supported. Child filters
        inside a group cannot contain nested `filters` of their own. Supported filter keys are
        `clientMacAddress`, `duid`, `description`, `notificationModes`, `trackingStartTime`, `trackingEndTime`,
        `isPresentOnNetwork`, and `randomizedMacAddresses`. Supported operators by field are:
        `clientMacAddress`, `duid`, `description`: `eq`, `neq`, `in`, `notIn`, `like` `trackingStartTime`,
        `trackingEndTime`: `eq`, `neq`, `lt`, `gt`, `lte`, `gte` `isPresentOnNetwork`: `eq`, `neq`
        `randomizedMacAddresses`: `eq`, `neq`, `in`, `notIn`, `like` `notificationModes`: `in`, `notIn` Use
        `like` on this request-body API for partial matching on `description`, `clientMacAddress`, `duid`, and
        `randomizedMacAddresses`. For `trackingEndTime`, value `0` represents never-expiring tracking.    The
        `page.sortBy` field accepts only tracked-client fields that produce stable, meaningful ordering for the
        configuration list: `clientMacAddress`, `duid`, `description`, `trackingStartTime`, `trackingEndTime`,
        `lastOnboardedTime`, `lastDisconnectedTime`, and `isPresentOnNetwork`. Only single-field sorting is
        supported on this API.

        Args:
            filters(list): Clients's List of filters to apply when querying tracked-client configurations.
                Supported operators by field are: `clientMacAddress`, `duid`, `description`: [eq, neq,
                in, notIn, like, liker] `trackingStartTime`, `trackingEndTime`: [eq, neq, lt, gt, lte,
                gte] `isPresentOnNetwork`: [eq, neq] `randomizedMacAddresses`: [eq, neq, in, notIn,
                like, liker] `notificationModes`: [in, notIn]  For `trackingEndTime`, value `0`
                represents never-expiring tracking.  Nested filter composition is supported through
                `logicalOperator` and nested `filters`. Only one level of nested filters is supported.
                (list of objects).
            page(object): Clients's Pagination input for tracked-client queries.
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
            https://developer.cisco.com/docs/dna-center/#!query-tracked-client-configurations-with-request-body-filters
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
            "filters": filters,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_edd1bedf1dc5dc9a7db8ecfe92d20d2_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/trackedClients/query"
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
            "bpm_edd1bedf1dc5dc9a7db8ecfe92d20d2_v3_2_3_0", json_data
        )

    def get_client_enrichment_details_v1(self, headers=None, **request_parameters):
        """Enriches a given network End User context (a network user-id or end user’s device Mac Address) with details
        about the user, the devices that the user is connected to and the assurance issues that the user is
        impacted by.

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
            https://developer.cisco.com/docs/dna-center/#!get-client-enrichment-details-v1
        """
        check_type(headers, dict)
        if headers is not None:
            if "entity_type" in headers:
                check_type(headers.get("entity_type"), str, may_be_none=False)
            if "entity_value" in headers:
                check_type(headers.get("entity_value"), str, may_be_none=False)
            if "issueCategory" in headers:
                check_type(headers.get("issueCategory"), str)
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

        e_url = "/dna/intent/api/v1/client-enrichment-details"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dfd2751065bfb8c2367dd726df316_v3_2_3_0", json_data
        )

    def get_clients_energy(
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
        """Retrieves a list of client devices with energy data based on the specified query parameters. For detailed
        information about the usage of the API, please refer to the Open API specification document
        - https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-deviceEnergy_1.0-1.0.1-resolved.yaml.  Retrieves a list of
        client devices with energy data based on the specified query parameters. It returns the most recent
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
            id(str): id query parameter. The list of Mac addresses (e.g., `54:9F:C6:43:FF:80`). Examples:
                `id=54:9F:C6:43:FF:80` (single device requested)
                `id=54:9F:C6:43:FF:80&id=01:23:45:67:89:AB` .
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
                `deviceCategory=AccessPoint` (single device family requested)
                `deviceCategory=AccessPoint&deviceCategory=OtherPOEDevice` (multiple device categories
                with comma separator) .
            device_sub_category(str): deviceSubCategory query parameter. The list of device sub categories.
                Examples: `deviceSubCategory=IP Phone 7821` (single sub category requested)
                `deviceSubCategory=IP Phone 7821&deviceSubCategory=IEEE PD` .
            view(str): view query parameter. List of views. View and attribute work in union. Each view will include
                its attributes. For example, view device includes all the attributes related to device.
                Please refer to `ClientDeviceEnergyView` model for supported list of views Examples:
                `view=device&view=energy` .
            attribute(str): attribute query parameter. List of attributes. Please refer to
                `ClientDeviceEnergyAttribute` for supported list of attributes     Examples:
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
            https://developer.cisco.com/docs/dna-center/#!get-clients-energy
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

        e_url = "/dna/data/api/v1/energy/clients"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dddfb3bc2f59f1905e64f5905e2296_v3_2_3_0", json_data
        )

    def retrieves_the_total_count_of_clients_by_applying_basic_filtering(
        self,
        band=None,
        connected_network_device_name=None,
        end_time=None,
        ipv4_address=None,
        ipv6_address=None,
        mac_address=None,
        os_type=None,
        os_version=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        ssid=None,
        start_time=None,
        type=None,
        wlc_name=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the number of clients by applying basic filtering. For detailed information about the usage of the
        API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        clients1-3.2.3-resolved.yaml.   Retrieves the number of clients by applying basic filtering. If
        startTime and endTime are not provided, the API defaults to the last 24 hours.

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to current time. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            type(str): type query parameter. The client device type whether client is connected to network through
                Wired or Wireless medium. .
            os_type(str): osType query parameter. Client device operating system type. This field supports wildcard
                (`*`) character-based search. If the value contains the (`*`) character, please use the
                /query API for regex search.  Ex: `*iOS*` or `iOS*` or `*iOS` Examples: `osType=iOS`
                (single osType requested) `osType=iOS&osType=Android` (multiple osType requested) .
            os_version(str): osVersion query parameter. Client device operating system version This field supports
                wildcard (`*`) character-based search. If the value contains the (`*`) character, please
                use the /query API for regex search.  Ex: `*14.3*` or `14.3*` or `*14.3` Examples:
                `osVersion=14.3` (single osVersion requested) `osVersion=14.3&osVersion=10.1` (multiple
                osVersion requested) .
            site_hierarchy(str): siteHierarchy query parameter. The full hierarchical breakdown of the site tree
                starting from Global site name and ending with the specific site name. The Root site is
                named "Global" (Ex. "Global/AreaName/BuildingName/FloorName") This field supports
                wildcard (`*`) character-based search. If the value contains the (`*`) character, please
                use the /query API for regex search.  Ex: `*BuildingName*` or `BuildingName*` or
                `*BuildingName` Examples: `siteHierarchy=Global/AreaName/BuildingName/FloorName` (single
                siteHierarchy requested) `siteHierarchy=Global/AreaName/BuildingName1/FloorName1&siteHie
                rarchy=Global/AreaName/BuildingName1/FloorName2` (multiple siteHierarchy requested).
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site tree
                in id form starting from Global site UUID and ending with the specific site UUID. (Ex.
                "globalUuid/areaUuid/buildingUuid/floorUuid") This field supports wildcard (`*`)
                character-based search.  Ex: `*buildingUuid*` or `buildingUuid*` or `*buildingUuid`
                Examples: `siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid` (single
                siteHierarchyId requested) `siteHierarchyId=globalUuid/areaUuid/buildingUuid1/floorUuid1
                &siteHierarchyId=globalUuid/areaUuid/buildingUuid1/floorUuid2` (multiple siteHierarchyId
                requested).
            site_id(str): siteId query parameter. The site UUID without the top level hierarchy. (Ex."floorUuid")
                Examples: `siteId=floorUuid` (single siteId requested)
                `siteId=floorUuid1&siteId=floorUuid2` (multiple siteId requested).
            ipv4_address(str): ipv4Address query parameter. IPv4 Address of the network entity either network device
                or client This field supports wildcard (`*`) character-based search.  Ex: `*1.1*` or
                `1.1*` or `*1.1` Examples: `ipv4Address=1.1.1.1` (single ipv4Address requested)
                `ipv4Address=1.1.1.1&ipv4Address=2.2.2.2` (multiple ipv4Address requested) .
            ipv6_address(str): ipv6Address query parameter. IPv6 Address of the network entity either network device
                or client This field supports wildcard (`*`) character-based search. Ex: `*2001:db8*` or
                `2001:db8*` or `*2001:db8` Examples: `ipv6Address=2001:db8:0:0:0:0:2:1` (single
                ipv6Address requested)
                `ipv6Address=2001:db8:0:0:0:0:2:1&ipv6Address=2001:db8:85a3:8d3:1319:8a2e:370:7348`
                (multiple ipv6Address requested) .
            mac_address(str): macAddress query parameter. The macAddress of the network device or client This field
                supports wildcard (`*`) character-based search.  Ex: `*AB:AB:AB*` or `AB:AB:AB*` or
                `*AB:AB:AB` Examples: `macAddress=AB:AB:AB:CD:CD:CD` (single macAddress requested)
                `macAddress=AB:AB:AB:CD:CD:DC&macAddress=AB:AB:AB:CD:CD:FE` (multiple macAddress
                requested) .
            wlc_name(str): wlcName query parameter. Wireless Controller name that reports the wireless client. This
                field supports wildcard (`*`) character-based search. If the value contains the (`*`)
                character, please use the /query API for regex search. Ex: `*wlc-25*` or `wlc-25*` or
                `*wlc-25` Examples: `wlcName=wlc-25` (single wlcName requested) `wlcName=wlc-25&wlc-34`
                (multiple wlcName requested) .
            connected_network_device_name(str): connectedNetworkDeviceName query parameter. Name of the neighbor
                network device that client is connected to. This field supports wildcard (`*`)
                character-based search. If the value contains the (`*`) character, please use the /query
                API for regex search. Ex: `*ap-25*` or `ap-25*` or `*ap-25` Examples:
                `connectedNetworkDeviceName=ap-25` (single connectedNetworkDeviceName requested)
                `connectedNetworkDeviceName=ap-25&ap-34` (multiple connectedNetworkDeviceName requested)
                .
            ssid(str): ssid query parameter. SSID is the name of wireless network to which client connects to. It is
                also referred to as WLAN ID Wireless Local Area Network Identifier. This field supports
                wildcard (`*`) character-based search. If the value contains the (`*`) character, please
                use the /query API for regex search.  Ex: `*Alpha*` or `Alpha*` or `*Alpha` Examples:
                `ssid=Alpha` (single ssid requested) `ssid=Alpha&ssid=Guest` (multiple ssid requested) .
            band(str): band query parameter. WiFi frequency band that client or Access Point operates. Band value is
                represented in Giga Hertz GHz Examples: `band=5GHZ` (single band requested)
                `band=2.4GHZ&band=6GHZ` (multiple band requested) .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-total-count-of-clients-by-applying-basic-filtering
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(type, str)
        check_type(os_type, str)
        check_type(os_version, str)
        check_type(site_hierarchy, str)
        check_type(site_hierarchy_id, str)
        check_type(site_id, str)
        check_type(ipv4_address, str)
        check_type(ipv6_address, str)
        check_type(mac_address, str)
        check_type(wlc_name, str)
        check_type(connected_network_device_name, str)
        check_type(ssid, str)
        check_type(band, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "type": type,
            "osType": os_type,
            "osVersion": os_version,
            "siteHierarchy": site_hierarchy,
            "siteHierarchyId": site_hierarchy_id,
            "siteId": site_id,
            "ipv4Address": ipv4_address,
            "ipv6Address": ipv6_address,
            "macAddress": mac_address,
            "wlcName": wlc_name,
            "connectedNetworkDeviceName": connected_network_device_name,
            "ssid": ssid,
            "band": band,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/clients/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ed18d78d455f9a51049a09ae12d48_v3_2_3_0", json_data
        )

    def get_client_energy_by_id(
        self,
        id,
        attribute=None,
        end_time=None,
        start_time=None,
        view=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves client device energy data for a specified time range based on the client ID. For detailed information
        about the usage of the API, please refer to the Open API specification document
        - https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-deviceEnergy_1.0-1.0.1-resolved.yaml.  Retrieves client
        device energy data for a specified time range based on the client ID. Returns the latest available
        snapshot of energy data between the provided start and end times. If no start and end times are
        specified, it defaults to returning the latest available energy data for the past 24 hours.

        Args:
            id(str): id path parameter. Mac address of a client device (e.g., 54:9F:C6:43:FF:80). It can be
                specified is any notational conventions    01:23:45:67:89:AB or 01-23-45-67-89-AB or
                0123.4567.89AB and is case insensitive.
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
                Please refer to `ClientDeviceEnergyView` model for supported list of views Examples:
                `view=device&view=energy` .
            attribute(str): attribute query parameter. List of attributes. Please refer to
                `ClientDeviceEnergyAttribute` for supported list of attributes     Examples:
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
            https://developer.cisco.com/docs/dna-center/#!get-client-energy-by-i-d
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

        e_url = "/dna/data/api/v1/energy/clients/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f090c2a6b325d32be55209cd6839f30_v3_2_3_0", json_data
        )

    def retrieves_specific_client_information_over_a_specified_period_of_time(
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
        """Retrieves the time series information of a specific client by applying complex filters, aggregate functions, and
        grouping. The data will be grouped based on the specified trend time interval. For detailed information
        about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-clients1-3.2.3-resolved.yaml.   Retrieves the time series
        information of a specific client by applying complex filters, aggregate functions, and grouping. The
        data will be grouped based on the specified trend time interval. If startTime and endTime are not
        provided, the API defaults to the last 24 hours.   The input payload contains the following fields,
        Field Name   Description           startTime   The start time indicates when the API begins retrieving
        data related to the resource. It must be specified in the UNIX epoch time format, measured in
        milliseconds. This value is inclusive, and if left unspecified, the default is 1 day before the endTime.
        endTime   The end time indicates the upper limit until which the API retrieves data related to the
        resource. It must be defined in the UNIX epoch time format, measured in milliseconds. This value is
        inclusive, and if left unspecified, the default is the latest available data.       trendInterval   The
        time window for aggregating metrics. This is a mandatory request field. Possible values include  5
        minutes, 10 minutes, 1 hour, 1 day, or 7 days . If the start and end time range exceeds 1 day, the
        trendInterval defaults to 1 hour.       groupBy   Specifies the attributes for grouping the data. Refer
        to  ClientGroupByField  model for the supported grouping attributes       attributes   A list of
        attributes associated with the resource, which can be requested to be included in the response alongside
        the required attributes. Refer to  ClientAttribute  model for the supported attributes
        aggregateAttributes   This specifies the attribute name and the function to be applied during data
        querying. The aggregate function is then applied to data within the specified start and end times. Refer
        to  ClientAggregateField  model for the supported aggregate attributes       filters   This is used to
        specify one or more conditions for filtering the queried data. Refer to  ClientFilterField  model for
        the supported filters       page   It includes the  limit, cursor, and timeSortOrder  fields.  limit
        denotes the number of records to retrieve per page,  cursor  signifies the initial data position, and
        timeSortOrder  is used sort the response based on the timestamp either in ascending or descending order.
        .

        Args:
            aggregateAttributes(list): Clients's aggregateAttributes (list of objects).
            attributes(list): Clients's attributes (list of strings).
            endTime(integer): Clients's endTime.
            filters(list): Clients's filters (list of objects).
            groupBy(list): Clients's groupBy (list of strings).
            page(object): Clients's page.
            startTime(integer): Clients's startTime.
            trendInterval(string): Clients's trendInterval.
            id(str): id path parameter. id is the client mac address. It can be specified in one of the notational
                conventions  01:23:45:67:89:AB or 01-23-45-67-89-AB or 0123.4567.89AB and is case
                insensitive .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-specific-client-information-over-a-specified-period-of-time
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
            "attributes": attributes,
            "filters": filters,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator("jsd_d9a13d575abdc26d485af708e7_v3_2_3_0").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/clients/{id}/trendAnalytics"
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
            "bpm_d9a13d575abdc26d485af708e7_v3_2_3_0", json_data
        )

    def retrieves_summary_analytics_data_related_to_clients(
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
        """Retrieves summary analytics data related to clients while applying complex filtering, aggregate functions, and
        grouping. This API facilitates obtaining consolidated insights into the performance and status of the
        clients. For detailed information about the usage of the API, please refer to the Open API specification
        document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-clients1-3.2.3-resolved.yaml.   Retrieves summary analytics
        data related to clients while applying complex filtering, aggregate functions, and grouping. This API
        facilitates obtaining consolidated insights into the performance and status of the clients. If startTime
        and endTime are not provided, the API defaults to the last 24 hours.   The input payload contains the
        following fields,         Field Name   Description           startTime   The start time indicates when
        the API begins retrieving data related to the resource. It must be specified in the UNIX epoch time
        format, measured in milliseconds. This value is inclusive, and if left unspecified, the default is 1 day
        before the endTime.       endTime   The end time indicates the upper limit until which the API retrieves
        data related to the resource. It must be defined in the UNIX epoch time format, measured in
        milliseconds. This value is inclusive, and if left unspecified, the default is the latest available
        data.       groupBy   Specifies the attributes for grouping the data. Refer to  ClientGroupByField
        model for the supported grouping attributes.       attributes   A list of attributes associated with the
        resource, which can be requested to be included in the response alongside the required attributes. Refer
        to  ClientAttribute  model for the supported attributes       aggregateAttributes   This specifies the
        attribute name and the function to be applied during data querying. The aggregate function is then
        applied to data within the specified start and end times. Refer to  ClientAggregateField  model for the
        supported aggregate attributes       filters   This is used to specify one or more conditions for
        filtering the queried data. Refer to  ClientFilterField  model for the supported filters       page   It
        includes the  limit, cursor, and sortBy  fields.  limit  denotes the number of records to retrieve per
        page,  cursor  signifies the initial data position, and  sortBy  is used to sort the response based on
        the sortBy fields. It contains the attribute name, order, and optional function for sorting by the
        aggregated field. Refer to  ClientSortByField  model for the supported sortBy names.      .

        Args:
            aggregateAttributes(list): Clients's aggregateAttributes (list of objects).
            attributes(list): Clients's attributes (list of strings).
            endTime(integer): Clients's endTime.
            filters(list): Clients's filters (list of objects).
            groupBy(list): Clients's groupBy (list of strings).
            page(object): Clients's page.
            startTime(integer): Clients's startTime.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-summary-analytics-data-related-to-clients
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
            "attributes": attributes,
            "filters": filters,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f210ff2d89425b4790ce56f19da7be92_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/clients/summaryAnalytics"
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
            "bpm_f210ff2d89425b4790ce56f19da7be92_v3_2_3_0", json_data
        )

    def retrieves_the_top_n_analytics_data_related_to_clients(
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
        """Retrieves the top N analytics data related to clients based on the provided input data. This API facilitates
        obtaining insights into the top-performing or most impacted clients. For detailed information about the
        usage of the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        clients1-3.2.3-resolved.yaml.   Retrieves the top N analytics data related to clients based on the
        provided input data. This API facilitates obtaining insights into the top-performing or most impacted
        clients. If startTime and endTime are not provided, the API defaults to the last 24 hours.   The input
        payload contains the following fields,         Field Name   Description           startTime   The start
        time indicates when the API begins retrieving data related to the resource. It must be specified in the
        UNIX epoch time format, measured in milliseconds. This value is inclusive, and if left unspecified, the
        default is 1 day before the endTime.       endTime   The end time indicates the upper limit until which
        the API retrieves data related to the resource. It must be defined in the UNIX epoch time format,
        measured in milliseconds. This value is inclusive, and if left unspecified, the default is the latest
        available data.       topN   The number of top records to retrieve. This is a required request field.
        groupBy   Specifies the attributes for grouping the data. Refer to  ClientGroupByField  model for the
        supported grouping attributes. This is a required request field.       attributes   A list of attributes
        associated with the resource, which can be requested to be included in the response alongside the
        required attributes. Refer to  ClientAttribute  model for the supported attributes
        aggregateAttributes   This specifies the attribute name and the function to be applied during data
        querying. The aggregate function is then applied to data within the specified start and end times. Refer
        to  ClientAggregateField  model for the supported aggregate attributes       filters   This is used to
        specify one or more conditions for filtering the queried data. Refer to  ClientFilterField  model for
        the supported filters       page   It includes the  limit, cursor, and sortBy  fields.  limit  denotes
        the number of records to retrieve per page,  cursor  signifies the initial data position, and  sortBy
        is used to sort the response based on the sortBy fields. It contains the attribute name, order, and
        optional function for sorting by the aggregated field. Refer to  ClientSortByField  model for the
        supported sortBy names.      .

        Args:
            aggregateAttributes(list): Clients's aggregateAttributes (list of objects).
            attributes(list): Clients's attributes (list of strings).
            endTime(integer): Clients's endTime.
            filters(list): Clients's filters (list of objects).
            groupBy(list): Clients's groupBy (list of strings).
            page(object): Clients's page.
            startTime(integer): Clients's startTime.
            topN(integer): Clients's topN.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-top-n-analytics-data-related-to-clients
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
            "attributes": attributes,
            "filters": filters,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f44ddd3c38c5a9484f5cb4e125447bc_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/clients/topNAnalytics"
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
            "bpm_f44ddd3c38c5a9484f5cb4e125447bc_v3_2_3_0", json_data
        )

    def retrieves_the_list_of_clients_by_applying_complex_filters_while_also_supporting_aggregate_attributes(
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
        """Retrieves the list of clients by applying complex filters while also supporting aggregate attributes. For
        detailed information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-clients1-3.2.3-resolved.yaml.   Retrieves the list of
        clients by applying complex filters while also supporting aggregate attributes. If startTime and endTime
        are not provided, the API defaults to the last 24 hours.   The input payload contains the following
        fields,         Field Name   Description           startTime   The start time indicates when the API
        begins retrieving data related to the resource. It must be specified in the UNIX epoch time format,
        measured in milliseconds. This value is inclusive, and if left unspecified, the default is 1 day before
        the endTime.       endTime   The end time indicates the upper limit until which the API retrieves data
        related to the resource. It must be defined in the UNIX epoch time format, measured in milliseconds.
        This value is inclusive, and if left unspecified, the default is the latest available data.       views
        A collection of attributes classified as "view" associated with the resource, which can be requested to
        be included in the response alongside the required attributes. Each view comprises a predetermined set
        of attributes. Refer to  ClientView  for the supported views       attributes   A list of attributes
        associated with the resource, which can be requested to be included in the response alongside the
        required attributes. Refer to  ClientAttribute  model for the supported attributes
        aggregateAttributes   This specifies the attribute name and the function to be applied during data
        querying. The aggregate function is then applied to data within the specified start and end times. Refer
        to  ClientAggregateField  model for the supported aggregate attributes       filters   This is used to
        specify one or more conditions for filtering the queried data. Refer to  ClientFilterField  model for
        the supported filters       page   It includes the  limit, offset, and sortBy  fields.  limit  denotes
        the number of records to retrieve per page,  offset  signifies the initial data position, and  sortBy
        is used to sort the response based on the sortBy fields. It contains the attribute name, order, and
        optional function for sorting by the aggregated field. Refer to  ClientSortByField  model for the
        supported sortBy names.         How the filtering behavior works   The  filters  field in each post body
        can be used in various ways:   Each filter in the list of filters will be applied simultaneously. For
        instance, the following example would request filtering to retrieve clients with an RSSI value greater
        than -50 dBm and a osType of either iOS or Android.            "filters" : [             {
        "key" :  "rssi" ,                "operator" :  "gt" ,                "value" :  -50              },
        {                "key" :  "osType" ,                "operator" :  "in" ,                "value" : [
        "iOS" ,                  "Android"                ]             }         ]  Each filter object can
        utilize its logical operator differently to offer nested filtering functionality.   In the example
        below, you can observe a logical  OR  filter being applied using the nested filtering functionality:
        The main filter object doesn't have its  key ,  value , or  operator  fields populated. Only the
        logicalOperator  field is populated to indicate that the filters within the nested filters list are to
        be logically combined.            "filters" : [             {                "logicalOperator" :  "or" ,
        "filters" : [                 {                    "key" :  "vlanId" ,                    "operator" :
        "eq" ,                    "value" :  187                  },                 {                    "key"
        :  "siteHierarchy" ,                    "operator" :  "in" ,                    "value" : [ "Global/San
        Jose" ,  "Global/SFO" ]                 }               ]             }         ] .

        Args:
            aggregateAttributes(list): Clients's aggregateAttributes (list of objects).
            attributes(list): Clients's attributes (list of strings).
            endTime(integer): Clients's endTime.
            filters(list): Clients's filters (list of objects).
            page(object): Clients's page.
            startTime(integer): Clients's startTime.
            views(list): Clients's views (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-clients-by-applying-complex-filters-while-also-supporting-aggregate-attributes
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
                "jsd_ea5f116c0cd152bbb4a92c043738ea57_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/clients/query"
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
            "bpm_ea5f116c0cd152bbb4a92c043738ea57_v3_2_3_0", json_data
        )

    def client_proximity(
        self,
        username,
        number_days=None,
        time_resolution=None,
        headers=None,
        **request_parameters
    ):
        """This intent API will provide client proximity information for a specific wireless user. Proximity is defined as
        presence on the same floor at the same time as the specified wireless user. The Proximity workflow
        requires the subscription to the following event (via the Event Notification workflow) prior to making
        this API call: NETWORK-CLIENTS-3-506 Client Proximity Report.

        Args:
            username(str): username query parameter. Wireless client username for which proximity information is
                required.
            number_days(int): number_days query parameter. Number of days to track proximity until current date.
                Defaults and maximum up to 14 days.
            time_resolution(int): time_resolution query parameter. Time interval (in minutes) to measure proximity.
                Defaults to 15 minutes with a minimum 5 minutes.
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
            https://developer.cisco.com/docs/dna-center/#!client-proximity
        """
        check_type(headers, dict)
        check_type(username, str, may_be_none=False)
        check_type(number_days, int)
        check_type(time_resolution, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "username": username,
            "number_days": number_days,
            "time_resolution": time_resolution,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/client-proximity"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c141467ea25ec0aa91cbcaff070354_v3_2_3_0", json_data
        )

    def get_client_enrichment_details(self, headers=None, **request_parameters):
        """Enriches a given network End User context (a network user-id or end user’s device Mac Address) with details
        about the user, the devices that the user is connected to and the assurance issues that the user is
        impacted by.

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
            https://developer.cisco.com/docs/dna-center/#!get-client-enrichment-details
        """
        check_type(headers, dict)
        if headers is not None:
            if "entity_type" in headers:
                check_type(headers.get("entity_type"), str, may_be_none=False)
            if "entity_value" in headers:
                check_type(headers.get("entity_value"), str, may_be_none=False)
            if "issueCategory" in headers:
                check_type(headers.get("issueCategory"), str)
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

        e_url = "/dna/intent/api/v2/client-enrichment-details"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_abd964fa042b5788b8986afd148552fa_v3_2_3_0", json_data
        )

    def get_client_enrichment_details_v2(self, headers=None, **query_parameters):
        """Alias for `get_client_enrichment_details <#catalystcentersdk.
        api.v3_2_3_0.clients.
        Clients.get_client_enrichment_details>`_
        """
        return self.get_client_enrichment_details(headers=headers, **query_parameters)

    def client_enrichment_details(self, headers=None, **request_parameters):
        """Enriches a given network End User context (a network user-id or end user’s device Mac Address) with details
        about the user, the devices that the user is connected to and the assurance issues that the user is
        impacted by.

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
            https://developer.cisco.com/docs/dna-center/#!client-enrichment-details
        """
        check_type(headers, dict)
        if headers is not None:
            if "entityType" in headers:
                check_type(headers.get("entityType"), str, may_be_none=False)
            if "entityValue" in headers:
                check_type(headers.get("entityValue"), str, may_be_none=False)
            if "issueCategory" in headers:
                check_type(headers.get("issueCategory"), str)
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

        e_url = "/dna/intent/api/v1/clientEnrichmentDetails"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e95677d5d4a567c960066fae739f7a7_v3_2_3_0", json_data
        )
