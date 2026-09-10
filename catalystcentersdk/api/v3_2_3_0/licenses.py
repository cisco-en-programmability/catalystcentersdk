"""Cisco Catalyst Center Licenses API wrapper.

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


class Licenses:
    """Cisco Catalyst Center Licenses API (version: 3.2.3.0).

    Wraps the Catalyst Center Licenses
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Licenses
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

    def retrieves_cssm_connection_mode(self, headers=None, **request_parameters):
        """Retrieves Cisco Smart Software Manager (CSSM) connection mode setting.           CSSM Connection Mode Setting
        Retrieves Cisco Smart Software Manager (CSSM) connection mode setting.           Connection Mode
        Description           DIRECT   Requires all smart-enabled devices to have direct internet access to the
        cloud-based CSSM.  DIRECT  is the default connection mode, set in a fresh setup.       ON_PREMISE
        Allows access to a subset of CSSM functionality without using a direct internet connection to manage
        licenses with the cloud-based CSSM. Devices connect to on-premise CSSM for license operations.
        SMART_PROXY   Smart-enabled network devices do not need direct internet access. Cisco Catalyst Center
        proxies the requests from the device to the CSSM cloud through itself.        .

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
            https://developer.cisco.com/docs/dna-center/#!retrieves-c-s-s-m-connection-mode
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

        e_url = "/dna/intent/api/v1/connectionModeSetting"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a32ed6ebdd945af9889223196c925a17_v3_2_3_0", json_data
        )

    def retrieves_c_s_s_m_connection_mode(self, headers=None, **query_parameters):
        """Alias for `retrieves_cssm_connection_mode <#catalystcentersdk.
        api.v3_2_3_0.licenses.
        Licenses.retrieves_cssm_connection_mode>`_
        """
        return self.retrieves_cssm_connection_mode(headers=headers, **query_parameters)

    def update_cssm_connection_mode(
        self,
        connectionMode=None,
        parameters=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Update Cisco Smart Software Manager (CSSM) connection mode for the system.           Update CSSM Connection Mode
        Setting       Update CSSM connection mode setting  Configures CSSM connection mode for the system.   If
        any other licensing operation is running, the API will return a response with HTTP status code  409 .
        To set the CSSM Connection Mode to  ON_PREMISE , parameters  onPremiseHost ,  smartAccountName ,
        clientId ,  clientSecret  are required. For information about how to retrieve the client ID and client
        secret, see the  Cisco Smart Software Manager On-Prem User Guide .   The input payload contains the
        following fields:           Parameter Name   Description           connectionMode   The CSSM connection
        modes of Catalyst Center are DIRECT, ON_PREMISE, and SMART_PROXY.       onPremiseHost   The hostname or
        IP address of the on-premise CSSM.       smartAccountName   The name of the CSSM on-premise local Smart
        Account.       clientId   The client id for the on-premise CSSM.       clientSecret   The client secret
        for the on-premise CSSM.        .

        Args:
            connectionMode(string): Licenses's The CSSM connection modes of Catalyst Center are DIRECT, ON_PREMISE
                and SMART_PROXY.. Available values are 'DIRECT', 'ON_PREMISE' and 'SMART_PROXY'.
            parameters(object): Licenses's On-premise CSSM parameters.
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
            https://developer.cisco.com/docs/dna-center/#!update-c-s-s-m-connection-mode
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
            "connectionMode": connectionMode,
            "parameters": parameters,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_c85b39d6bae0536695992ddbb91ea96d_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/connectionModeSetting"
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
            "bpm_c85b39d6bae0536695992ddbb91ea96d_v3_2_3_0", json_data
        )

    def update_c_s_s_m_connection_mode(
        self,
        connectionMode=None,
        parameters=None,
        headers=None,
        payload=None,
        active_validation=True,
        **query_parameters
    ):
        """Alias for `update_cssm_connection_mode <#catalystcentersdk.
        api.v3_2_3_0.licenses.
        Licenses.update_cssm_connection_mode>`_
        """
        return self.update_cssm_connection_mode(
            connectionMode=connectionMode,
            parameters=parameters,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def query_network_devices_licenses_count_with_filters(
        self,
        filter=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """API to retrieve the number of network devices, determined by the filters. It is possible to get the number of
        network device's licenses based on various parameters, such as device family, software version, license
        mode, license level, registration status, etc.  **How the filtering behavior works**  All items in the
        `filters` array are combined using the `AND` operator by default. This can be changed by setting the
        `logicalOperator` field in the `filter` object to `OR`.  Each item in the array is filtered on the
        `key`, `operator`, and `value` fields.  For numerical fields, such as timestamps, the operators `eq`,
        `in`, `gt`, `lt`, `gte`, and `lte` are allowed.  Array of values can be provided for the `value` field
        when using the `in` operator. For string fields, such as `hostname`, the operators `eq`, `contains`, and
        `in` are allowed but for `softwareVersion`, the additional operators `gt`, `lt`, `gte`, and `lte` are
        also allowed.  Network devices count can be queried by `customerTags` by providing the `key` as
        `customerTags.fieldName` where `fieldName` can be any of `tag1`, `tag2`, `tag3` or `tag4` and the
        `value`. Only `eq` and `in` operator is allowed.  ### Examples of request body for the filter.  *Example
        1: Multiple values for a filter item*   The below example will return the count of network devices that
        don't have the proper registration stautus.  ```json {     "filter": {         "filters": [
        {                 "key": "registrationStatus",                 "operator": "in",
        "value": ["UNREGISTERED", "REGISTRATION_EXPIRED"]             }         ]     } } ```  *Example 2:
        Multiple filter items*  The below example will return count of network devices with DNA license or the
        softwareVersion less than `17.15.3`. ```json {     "filter": {         "filter": [             {
        "key": "licenseType",                 "operator": "in",                 "value": ["DNA_ESSENTIALS",
        "DNA_ADVANTAGE"]             },             {                 "key": "softwareVersion",
        "operator": "lt",                 "value": "17.15.3"             }         ],         "logicalOperator":
        "OR"     } } ```  *Example 3: Filtering based on multiple user-defined fields and values*  The below
        example will return the count of network devices that have the customerTags field `tag1` with values
        `branch` or `edge` and the customerTags field `tag2` with value `gold`. ```json {     "filter": {
        "filter":[             {                 "key": "customerTags.tag1",                 "operator": "in",
        "value": ["branch", "edge"]             },             {                 "key": "customerTags.tag2",
        "operator": "eq",                 "value": "gold"             }         ],         "logicalOperator":
        "OR"     } } ```   **Supported filter keys and types** | Key                             | Type    |
        Allowed values    | | --------------------------------| ------| ------ | | `id`
        | string  |     | | `managementAddress`             | string  |     | | `hostname`
        | string  |     | | `family`                        | string  |`ROUTERS`, `SWITCHES_AND_HUBS`,
        `WIRELESS_CONTROLLER`, `UNIFIED_AP` | | `series`                        | string  |     | |
        `softwareVersion`               | string  |     | | `licenseMode`                   | string
        |`SMART_LICENSE`, `RIGHT_TO_USE`, `UNKNOWN` | | `licenseType`                  | string
        |`NETWORK_ESSENTIALS`, `NETWORK_ADVANTAGE`, `AIR_NETWORK_ESSENTIALS`, `AIR_NETWORK_ADVANTAGE`,
        `DNA_ESSENTIALS`, `DNA_ADVANTAGE`, `AIR_DNA_ESSENTIALS`, `AIR_DNA_ADVANTAGE`, `CNS_ESSENTIALS`,
        `CNS_ADVANTAGE` |  | `licenseStatus`                | string  |`IN_USE`, `NOT_IN_USE`, `EXPIRED_IN_USE`,
        `EXPIRED_NOT_IN_USE`, `USAGE_COUNT_CONSUMED`, `OUT_OF_COMPLIANCE`, `EVALUATION_IN_USE`, `INACTIVE` |
        `licenseCount`                 | integer |     | | `registrationStatus`            | string
        |`REGISTERED`, `UNREGISTERED`, `REGISTRATION_EXPIRED`, `RESERVATION_IN_PROGRESS`, `REGISTERED_SLR`,
        `REGISTERED_PLR`, `REGISTERED_SATELLITE`, `NA`, `UNKNOWN` | | `smartAccountId`                | string
        |     | | `virtualAccountId`              | string  |     | | `authCodeStatus`                | string
        |`INSTALLED`, `NOT_INSTALLED`, `NA` | | `throughputValue`               | string  |     | |
        `lastSuccessfulUsageReportingTime`  | integer |     | | `customerTags`.`fieldName`      | string  |
        | | `siteHierarchy`                 | string  |     |.

        Args:
            filter(): Licenses's filter.
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
            https://developer.cisco.com/docs/dna-center/#!query-network-devices-licenses-count-with-filters
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
                "jsd_d5d06be5a5cb72ba22e8ee5226c_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDeviceLicenses/query/count"
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
            "bpm_d5d06be5a5cb72ba22e8ee5226c_v3_2_3_0", json_data
        )

    def query_network_devices_licenses_with_filters(
        self,
        filter=None,
        page=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """API to retrieve the list of network devices and their licenses, determined by the filters. It is possible to
        filter the network device's licenses based on various parameters, such as device family, software
        version, license mode, license level, registration status, etc.  **How the filtering behavior works**
        All items in the `filters` array are combined using the `AND` operator by default. This can be changed
        by setting the `logicalOperator` field in the `filter` object to `OR`.  Each item in the array is
        filtered on the `key`, `operator`, and `value` fields.  For numerical fields, such as timestamps, the
        operators `eq`, `in`, `gt`, `lt`, `gte`, and `lte` are allowed.  Array of values can be provided for the
        `value` field when using the `in` operator. For string fields, such as `hostname`, the operators `eq`,
        `contains`, and `in` are allowed but for `softwareVersion`, the additional operators `gt`, `lt`, `gte`,
        and `lte` are also allowed.  Network devices can be queried by `customerTags` by providing the `key` as
        `customerTags.fieldName` where `fieldName` can be any of `tag1`, `tag2`, `tag3` or `tag4` and the
        `value` only `eq` and `in` operator is allowed.  ### Examples of request body for the filter.  *Example
        1: Multiple values for a filter item*    The below example will return the first 10 network devices that
        dont have the proper registration stautus.  ```json {     "filter": {         "filters": [             {
        "key": "registrationStatus",                 "operator": "in",                 "value": ["UNREGISTERED",
        "REGISTRATION_EXPIRED"]             }         ]     },     "page": {         "limit": 10,
        "offset": 1,         "sortBy": {           "name": "id",           "order": "asc"         }     } } ```
        *Example 2: Multiple filter items*    The below example will return the first 10 network devices with
        DNA license OR the softwareVersion less than 17.15.3. ```json {     "filter": {         "filter": [
        {                 "key": "licenseType",                 "operator": "in",                 "value":
        ["DNA_ESSENTIALS", "DNA_ADVANTAGE"]             },             {                 "key":
        "softwareVersion",                 "operator": "lt",                 "value": "17.15.3"             }
        ],         "logicalOperator": "OR"     },     "page": {         "limit": 10,         "offset": 1,
        "sortBy": {           "name": "id",           "order": "asc"         }     } } ```  *Example 3:
        Filtering based on multiple user-defined fields and values*       The below example will return the
        first 10 network devices that have the customerTags field `tag1` with values `branch` or `edge` AND the
        customerTags field `tag2` with value `gold`. ```json {     "filter": {         "filters":[             {
        "key": "customerTags.tag1",                 "operator": "in",                 "value": ["branch",
        "edge"]             },             {                 "key": "customerTags.tag2",
        "operator": "eq",                 "value": "gold"             }         ],         "logicalOperator":
        "AND"     },     "page": {         "limit": 10,         "offset": 1,         "sortBy": {
        "name": "id",           "order": "asc"         }     } } ```   **Supported filter keys and types** | Key
        | Type    | Allowed values    | | --------------------------------| ------| ------ | | `id`
        | string  |     | | `managementAddress`             | string  |     | | `hostname`
        | string  |     | | `family`                        | string  |`ROUTERS`, `SWITCHES_AND_HUBS`,
        `WIRELESS_CONTROLLER`, `UNIFIED_AP` | | `series`                        | string  |     | |
        `softwareVersion`               | string  |     | | `licenseMode`                   | string
        |`SMART_LICENSE`, `RIGHT_TO_USE`, `UNKNOWN` | | `licenseType`                  | string
        |`NETWORK_ESSENTIALS`, `NETWORK_ADVANTAGE`, `AIR_NETWORK_ESSENTIALS`, `AIR_NETWORK_ADVANTAGE`,
        `DNA_ESSENTIALS`, `DNA_ADVANTAGE`, `AIR_DNA_ESSENTIALS`, `AIR_DNA_ADVANTAGE`, `CNS_ESSENTIALS`,
        `CNS_ADVANTAGE` |  | `licenseStatus`                | string  |`IN_USE`, `NOT_IN_USE`, `EXPIRED_IN_USE`,
        `EXPIRED_NOT_IN_USE`, `USAGE_COUNT_CONSUMED`, `OUT_OF_COMPLIANCE`, `EVALUATION_IN_USE`, `INACTIVE` |
        `licenseCount`                 | integer |     | | `registrationStatus`            | string
        |`REGISTERED`, `UNREGISTERED`, `REGISTRATION_EXPIRED`, `RESERVATION_IN_PROGRESS`, `REGISTERED_SLR`,
        `REGISTERED_PLR`, `REGISTERED_SATELLITE`, `NA`, `UNKNOWN` | | `smartAccountId`                | string
        |     | | `virtualAccountId`              | string  |     | | `authCodeStatus`                | string
        |`INSTALLED`, `NOT_INSTALLED`, `NA` | | `throughputValue`               | string  |     | |
        `lastSuccessfulUsageReportingTime`  | integer |     | | `customerTags`.`fieldName`      | string  |
        | | `siteHierarchy`                 | string  |     |.

        Args:
            filter(object): Licenses's filter.
            page(object): Licenses's Query filter for pagination and sorting.
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
            https://developer.cisco.com/docs/dna-center/#!query-network-devices-licenses-with-filters
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
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e53572ee6f5f739677c6008d8bfdee_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDeviceLicenses/query"
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
            "bpm_e53572ee6f5f739677c6008d8bfdee_v3_2_3_0", json_data
        )

    def retrieves_summary_of_network_device_licenses(
        self, headers=None, **request_parameters
    ):
        """Retrieves the summary of consumed network, DNA, and Cisco Networking Subscription (CNS) licenses, along with the
        counts of unregistered and out-of-compliance network devices, and expired and expiring network device
        licenses.  Released for gathering feedbacks from early adopters. API design is not final and future
        updates of this API may implement changes to any aspects of the API design.

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
            https://developer.cisco.com/docs/dna-center/#!retrieves-summary-of-network-device-licenses
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

        e_url = "/dna/intent/api/v1/networkDeviceLicenses/summary"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_df7151bbd7053ef8b010321bfa2bb84_v3_2_3_0", json_data
        )

    def device_registration(
        self,
        virtual_account_name,
        device_uuids=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Register device(s) in CSSM(Cisco Smart Software Manager).   Device Registration : It will register device(s) in
        CSSM(Cisco Smart Software Manager).

        Args:
            device_uuids(list): Licenses's Comma separated device ids (list of strings).
            virtual_account_name(str): virtual_account_name path parameter. Name of virtual account.
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
            https://developer.cisco.com/docs/dna-center/#!device-registration
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(virtual_account_name, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "virtual_account_name": virtual_account_name,
        }
        _payload = {
            "device_uuids": device_uuids,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_df26f516755a50b5b5477324cf5cb649_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/licenses/smartAccount/virtualAccount/"
            + "{virtual_account_name}/register"
        )
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
            "bpm_df26f516755a50b5b5477324cf5cb649_v3_2_3_0", json_data
        )

    def retrieves_license_details_of_network_devices(
        self,
        auth_codestatus=None,
        authorization_status=None,
        family=None,
        id=None,
        license_mode=None,
        license_status=None,
        license_type=None,
        limit=None,
        offset=None,
        order=None,
        registration_status=None,
        smart_account_id=None,
        sort_by=None,
        virtual_account_id=None,
        headers=None,
        **request_parameters
    ):
        """API to retrieve the list of network devices and their licenses based on given filters.

        Args:
            id(str): id query parameter. Unique ID of the license details of the network device.
            family(str): family query parameter. Product family of the network device. (Family: Description),
                (`ROUTERS`: Router product family),  (`SWITCHES_AND_HUBS`: Switches and Hubs product
                family),  (`WIRELESS_CONTROLLER`: Wireless controller product family),  (`UNIFIED_AP`:
                Unified Access Point product family),  .
            license_mode(str): licenseMode query parameter. Mode of license on the device. (License Mode:
                Description),  (`SMART_LICENSE`: Smart License mode),  (`RIGHT_TO_USE`: Right to use),
                (`UNKNOWN`: Mode of license on the device is not known.),  .
            license_type(str): licenseType query parameter. Type of license available on the network device.
                (License Type: Description),  (`NETWORK_ESSENTIALS`: Network Essentials license),
                (`NETWORK_ADVANTAGE`: Network Advantage license),  (`AIR_NETWORK_ESSENTIALS`: Air
                Network Essentials license. It is applicable for wireless controllers or switches having
                wireless capability.),  (`AIR_NETWORK_ADVANTAGE`: Air Network Advantage license. It is
                applicable for wireless controllers or switches having wireless capability.),
                (`DNA_ESSENTIALS`: DNA Essentials license),  (`DNA_ADVANTAGE`: DNA Advantage license),
                (`AIR_DNA_ESSENTIALS`: Air DNA Essentials license. It is applicable for wireless
                controllers or switches having wireless capability.),  (`AIR_DNA_ADVANTAGE`: Air DNA
                Advantage license. It is applicable for wireless controllers or switches having wireless
                capability),  (`CNS_ESSENTIALS`: Cisco Networking Subscription  Essentials license),
                (`CNS_ADVANTAGE`: Cisco Networking Subscription  Advantage license),  .
            license_status(str): licenseStatus query parameter. Status of license on the network device. (License
                Status: Description),  (`IN_USE`: A license is actively being used by a Cisco device and
                is currently authorized for features it enables.),  (`NOT_IN_USE`: A license is
                available on the device but is not currently being used by device.),  (`EXPIRED_IN_USE`:
                A license has expired but the device continues to use its features.),
                (`EXPIRED_NOT_IN_USE`: A license has expired and its features are not currently being
                utilized on the device.),  (`USAGE_COUNT_CONSUMED`: The allowed usage limit for the
                license has been fully utilized. It is only applicable for Cisco Nexus devices.),
                (`OUT_OF_COMPLIANCE`: A device is using features that require licenses it does not have
                assigned to it, potentially leading to functionality limitations.),
                (`EVALUATION_IN_USE`: A device is currently using a trial or evaluation license for its
                features.),  (`INACTIVE`: A license is available on the device but is not currently
                being used by device. This license status is only applicable for virtual wireless
                controllers.),  .
            registration_status(str): registrationStatus query parameter. Smart License registration status
                (Registration status: Description),  (`REGISTERED`: The network device instance is
                registered with CSSM.),  (`UNREGISTERED`: Smart Licensing is enabled on the network
                device, but the network device is not registered with CSSM.),  (`REGISTRATION_EXPIRED`:
                The registration has expired.),  (`RESERVATION_IN_PROGRESS`: The license reservation is
                in progress on the network device.),  (`REGISTERED_SLR`: The device has successfully
                completed the process of SLR and is now registered.),  (`REGISTERED_PLR`: The device has
                successfully completed the process of PLR and is now registered.),
                (`REGISTERED_SATELLITE`: The device is successfully registered with a On Prem CSSM
                server for Smart Licensing.),  (`NA`: The registration is not applicable for device.
                'NA' can be seen for devices having RTU license mode or device for which smart licensing
                using policy is applicable.),  (`UNKNOWN`: The registration state is not known on the
                device.),  .
            authorization_status(str): authorizationStatus query parameter. Smart License authorization status
                (Authorization Status: Description),  (`AUTHORIZED`: Registration has been completed
                with a valid Smart Account and license consumption has begun. The number of licenses
                consumed is less than the licenses available for use. This is an indication of being in
                compliance.),  (`EVALUATION_MODE`: The network device is running in evaluation mode when
                it is not registered.),  (`OUT_OF_COMPLIANCE`: The device's license consumption has
                exceeded the number of licenses that were purchased. The virtual account containing the
                product instance has a shortage of one or more of license types used.),
                (`EVALUATION_EXPIRED`: The evaluation period has expired and the device will be in
                unlicensed state.),  (`AUTHORIZATION_EXPIRED`: The authorization has expired.),
                (`NOT_AUTHORIZED`: The authorization is not valid.),  (`AUTHORIZED_RESERVED`:
                Registration of device has been completed using SLR/PLR with a valid Smart Account and
                license consumption has begun. The number of licenses consumed is less than the licenses
                available for use. This is an indication of being in compliance.),  (`NA`: The
                authorization is not applicable for device. 'NA' can be seen for devices having RTU mode
                or device for which smart licensing using policy is applicable),  (`UNKNOWN`: The
                authorization state is not known on the device.),  .
            smart_account_id(str): smartAccountId query parameter. Smart Account id where device is registered. Use
                `GET /dna/intent/api/v1/licenses/smartAccounts` intent API to find the smart account Id.
            virtual_account_id(str): virtualAccountId query parameter. Virtual Account id where device is
                registered. Use `GET /dna/intent/api/v1/licenses/smartAccount/${id}/virtualAccounts`
                intent API to find the virtual account Id.
            auth_codestatus(str): authCodeStatus query parameter. Status of authorization code for network device.
                Smart Licensing authorization code enables the use of a HSEC license on the device. It
                is applicable for routers only. (Auth Code Status: Description),  (`INSTALLED`: If
                authorization code is installed on the device, the status will be INSTALLED.),
                (`NOT_INSTALLED`: If authorization code is not installed, the status will be
                NOT_INSTALLED.),  (`NA`: If authorization code is not applicable for the device, then
                the status will be NA.),  .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-license-details-of-network-devices
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(family, str)
        check_type(license_mode, str)
        check_type(license_type, str)
        check_type(license_status, str)
        check_type(registration_status, str)
        check_type(authorization_status, str)
        check_type(smart_account_id, str)
        check_type(virtual_account_id, str)
        check_type(auth_codestatus, str)
        check_type(limit, int)
        check_type(offset, int)
        check_type(sort_by, str)
        check_type(order, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "family": family,
            "licenseMode": license_mode,
            "licenseType": license_type,
            "licenseStatus": license_status,
            "registrationStatus": registration_status,
            "authorizationStatus": authorization_status,
            "smartAccountId": smart_account_id,
            "virtualAccountId": virtual_account_id,
            "authCodeStatus": auth_codestatus,
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

        e_url = "/dna/intent/api/v1/networkDeviceLicenses"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c8f08e56f59f8bd737056e5f1c_v3_2_3_0", json_data
        )

    def smart_account_details(self, headers=None, **request_parameters):
        """Retrieve details of all smart accounts.   Smart Account Details : It provides details of all smart accounts.

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
            https://developer.cisco.com/docs/dna-center/#!smart-account-details
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

        e_url = "/dna/intent/api/v1/licenses/smartAccounts"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ea3fdbde23325051a76b9d062c2962a0_v3_2_3_0", json_data
        )

    def retrieve_license_setting(self, headers=None, **request_parameters):
        """Retrieves license setting Default smart account id and virtual account id for auto registration of devices for
        smart license flow. If default smart account is not configured, 'defaultSmartAccountId' is 'null'.
        Similarly, if auto registration of devices for smart license flow is not enabled,
        'autoRegistrationVirtualAccountId' is 'null'. For smart proxy connection mode,
        'autoRegistrationVirtualAccountId' is always 'null'.

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
            https://developer.cisco.com/docs/dna-center/#!retrieve-license-setting
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

        e_url = "/dna/intent/api/v1/licenseSetting"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b5ef334945074a609698223cf05db_v3_2_3_0", json_data
        )

    def update_license_setting(
        self,
        autoRegistrationVirtualAccountId=None,
        defaultSmartAccountId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Update license setting Configure default smart account id  and/or virtual account id for auto registration of
        devices for smart license flow. Virtual account should be part of default smart account. Default smart
        account id cannot be set to 'null'. Auto registration of devices for smart license flow is applicable
        only for direct or on-prem SSM connection mode.

        Args:
            autoRegistrationVirtualAccountId(string): Licenses's Virtual account id.
            defaultSmartAccountId(string): Licenses's Default smart account id.
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
            https://developer.cisco.com/docs/dna-center/#!update-license-setting
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
            "defaultSmartAccountId": defaultSmartAccountId,
            "autoRegistrationVirtualAccountId": autoRegistrationVirtualAccountId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d9bd7c527d254ecb63d2b709c428043_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/licenseSetting"
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
            "bpm_d9bd7c527d254ecb63d2b709c428043_v3_2_3_0", json_data
        )

    def api_to_fetch_the_count_of_license_usage_records_based_on_given_filters(
        self,
        product_family=None,
        smart_account_id=None,
        virtual_account_id=None,
        headers=None,
        **request_parameters
    ):
        """API to fetch the count of license usage records based on given filters.

        Args:
            smart_account_id(str): smartAccountId query parameter. Id of the smart account. Use `GET
                /dna/intent/api/v1/licenses/smartAccounts` intent API to find the smart account Id.
            virtual_account_id(str): virtualAccountId query parameter. Id of the virtual account. Use `GET
                /dna/intent/api/v1/licenses/smartAccount/${id}/virtualAccounts` intent API to find the
                virtual account Id.
            product_family(str): productFamily query parameter. Family of the product (Family: Description),
                (`SWITCH`: Switch product family),  (`ROUTER`: Router product family),  (`UNIFIED_AP`:
                Unified Access Point product family),  (`ISE`: ISE product family),  .
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
            https://developer.cisco.com/docs/dna-center/#!a-p-i-to-fetch-the-count-of-license-usage-records-based-on-given-filters
        """
        check_type(headers, dict)
        check_type(smart_account_id, str)
        check_type(virtual_account_id, str)
        check_type(product_family, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "smartAccountId": smart_account_id,
            "virtualAccountId": virtual_account_id,
            "productFamily": product_family,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/licenseUsage/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f989680cc5405ede844ab8f544700aff_v3_2_3_0", json_data
        )

    def api_to_obtain_license_counts_grouped_by_product_family_and_license_type(
        self,
        limit=None,
        offset=None,
        product_family=None,
        smart_account_id=None,
        virtual_account_id=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the count of purchased, used, and available licenses (Cisco DNA, Network, and CNS licenses) for a
        smart account/virtual account in CSSM. Additionally, it provides information on the number of licenses
        consumed by devices managed through Cisco Catalyst Center.

        Args:
            smart_account_id(str): smartAccountId query parameter. Id of the smart account. Use `GET
                /dna/intent/api/v1/licenses/smartAccounts` intent API to find the smart account Id.
            virtual_account_id(str): virtualAccountId query parameter. Id of the virtual account. Use `GET
                /dna/intent/api/v1/licenses/smartAccount/${id}/virtualAccounts` intent API to find the
                virtual account Id.
            product_family(str): productFamily query parameter. Family of the product (Family: Description),
                (`SWITCH`: Switch product family),  (`ROUTER`: Router product family),  (`UNIFIED_AP`:
                Unified Access Point product family),  (`ISE`: ISE product family),  .
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
            https://developer.cisco.com/docs/dna-center/#!a-p-i-to-obtain-license-counts_-grouped-by-product-family-and-license-type
        """
        check_type(headers, dict)
        check_type(smart_account_id, str)
        check_type(virtual_account_id, str)
        check_type(product_family, str)
        check_type(limit, int)
        check_type(offset, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "smartAccountId": smart_account_id,
            "virtualAccountId": virtual_account_id,
            "productFamily": product_family,
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

        e_url = "/dna/intent/api/v1/licenseUsage"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b80ddb79df757ce922364fdf8a288c3_v3_2_3_0", json_data
        )

    def license_usage_details(
        self,
        device_type,
        smart_account_id,
        virtual_account_name,
        headers=None,
        **request_parameters
    ):
        """Get count of purchased and in use Cisco DNA and Network licenses.   License Usage Details : It gives count of
        purchased and in use DNA and Network licenses.

        Args:
            smart_account_id(str): smart_account_id path parameter. Id of smart account.
            virtual_account_name(str): virtual_account_name path parameter. Name of virtual account. Putting "All"
                will give license term detail for all virtual accounts.
            device_type(str): device_type query parameter. Type of device like router, switch, wireless or ise.
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
            https://developer.cisco.com/docs/dna-center/#!license-usage-details
        """
        check_type(headers, dict)
        check_type(device_type, str, may_be_none=False)
        check_type(smart_account_id, str, may_be_none=False)
        check_type(virtual_account_name, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "device_type": device_type,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "smart_account_id": smart_account_id,
            "virtual_account_name": virtual_account_name,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/licenses/usage/smartAccount/{smart_ac"
            + "count_id}/virtualAccount/{virtual_account_name}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e55ecbbda454c6a01d905e6f4cce16_v3_2_3_0", json_data
        )

    def device_license_summary(
        self,
        limit,
        order,
        page_number,
        device_type=None,
        device_uuid=None,
        dna_level=None,
        registration_status=None,
        smart_account_id=None,
        sort_by=None,
        virtual_account_name=None,
        headers=None,
        **request_parameters
    ):
        """Show license summary of device(s). Deprecated since release 3.2.1 Alternatives: GET
        /dna/intent/api/v1/networkDeviceLicenses POST /dna/intent/api/v1/networkDeviceLicenses/query
        Deprecated since release 3.2.1. Alternatives: GET /dna/intent/api/v1/networkDeviceLicenses, POST
        /dna/intent/api/v1/networkDeviceLicenses/query.

        Args:
            page_number(int): page_number query parameter. Page number of response.
            order(str): order query parameter. Sorting order.
            sort_by(str): sort_by query parameter. Sort result by field.
            dna_level(str): dna_level query parameter. Device Cisco DNA license level.
            device_type(str): device_type query parameter. Type of device.
            limit(int): limit query parameter. Specifies the maximum number of device license summaries to return
                per page. Must be an integer between 1 and 500, inclusive.
            registration_status(str): registration_status query parameter. Smart license registration status of
                device.
            virtual_account_name(str): virtual_account_name query parameter. Name of virtual account.
            smart_account_id(int): smart_account_id query parameter. Id of smart account.
            device_uuid(str): device_uuid query parameter. Id of device.
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
            https://developer.cisco.com/docs/dna-center/#!device-license-summary
        """
        check_type(headers, dict)
        check_type(page_number, int, may_be_none=False)
        check_type(order, str, may_be_none=False)
        check_type(sort_by, str)
        check_type(dna_level, str)
        check_type(device_type, str)
        check_type(limit, int, may_be_none=False)
        check_type(registration_status, str)
        check_type(virtual_account_name, str)
        check_type(smart_account_id, int)
        check_type(device_uuid, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "page_number": page_number,
            "order": order,
            "sort_by": sort_by,
            "dna_level": dna_level,
            "device_type": device_type,
            "limit": limit,
            "registration_status": registration_status,
            "virtual_account_name": virtual_account_name,
            "smart_account_id": smart_account_id,
            "device_uuid": device_uuid,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/licenses/device/summary"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f4ba64eef4085d518a612835e128fe3c_v3_2_3_0", json_data
        )

    def system_licensing_last_operation_status(
        self, headers=None, **request_parameters
    ):
        """Retrieves the status of the last system licensing operation. If the operation does not exist or has not been
        triggered, the API responds with an HTTP 404 (Not Found) error.  Retrieves the status of the last system
        licensing operation. If the operation does not exist or has not been triggered, the API responds with an
        HTTP 404 (Not Found) error.

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
            https://developer.cisco.com/docs/dna-center/#!system-licensing-last-operation-status
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

        e_url = "/dna/system/api/v1/license/lastOperationStatus"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory("bpm_d1275a6eacbbda807ec535c5_v3_2_3_0", json_data)

    def device_deregistration(
        self,
        device_uuids=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Deregister device(s) from CSSM(Cisco Smart Software Manager).   Device Deregistration: It will deregister
        device(s) from CSSM(Cisco Smart Software Manager).

        Args:
            device_uuids(list): Licenses's Comma separated device ids (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!device-deregistration
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "device_uuids": device_uuids,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_b2f15d0c54c2862a60a904289ddd_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/licenses/smartAccount/virtualAccount/" + "deregister"
        )
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
            "bpm_b2f15d0c54c2862a60a904289ddd_v3_2_3_0", json_data
        )

    def device_count_details(
        self,
        device_type=None,
        dna_level=None,
        registration_status=None,
        smart_account_id=None,
        virtual_account_name=None,
        headers=None,
        **request_parameters
    ):
        """Get total number of managed device(s) based on the given filters. Deprecated since release 3.2.1 Alternatives:
        GET /dna/intent/api/v1/networkDeviceLicenses/count POST
        /dna/intent/api/v1/networkDeviceLicenses/query/count   Deprecated since release 3.2.1. Alternatives: GET
        /dna/intent/api/v1/networkDeviceLicenses/count, POST
        /dna/intent/api/v1/networkDeviceLicenses/query/count.

        Args:
            device_type(str): device_type query parameter. Type of device.
            registration_status(str): registration_status query parameter. Smart license registration status of
                device.
            dna_level(str): dna_level query parameter. Device Cisco DNA License Level.
            virtual_account_name(str): virtual_account_name query parameter. Virtual account name.
            smart_account_id(str): smart_account_id query parameter. Smart account id.
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
            https://developer.cisco.com/docs/dna-center/#!device-count-details
        """
        check_type(headers, dict)
        check_type(device_type, str)
        check_type(registration_status, str)
        check_type(dna_level, str)
        check_type(virtual_account_name, str)
        check_type(smart_account_id, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "device_type": device_type,
            "registration_status": registration_status,
            "dna_level": dna_level,
            "virtual_account_name": virtual_account_name,
            "smart_account_id": smart_account_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/licenses/device/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c0cf04bdc758b29bb11abbdacbd921_v3_2_3_0", json_data
        )

    def system_licensing_status(self, headers=None, **request_parameters):
        """Fetches registration status, authorization status and entitlements of the system with Cisco Smart Software
        Manage (CSSM).  Fetches registration status, authorization status and entitlements of the system with
        Cisco Smart Software Manage (CSSM).

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
            https://developer.cisco.com/docs/dna-center/#!system-licensing-status
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

        e_url = "/dna/system/api/v1/license/status"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ad6565535c567d951cdaf7bdaf7972_v3_2_3_0", json_data
        )

    def retrieves_the_number_of_network_devices(
        self,
        auth_codestatus=None,
        authorization_status=None,
        family=None,
        id=None,
        license_mode=None,
        license_status=None,
        license_type=None,
        registration_status=None,
        smart_account_id=None,
        virtual_account_id=None,
        headers=None,
        **request_parameters
    ):
        """API to retrieve the number of network devices based on given filters.

        Args:
            id(str): id query parameter. Unique ID of the license details of the network device.
            family(str): family query parameter. Product family of the network device. (Family: Description),
                (`ROUTERS`: Router product family),  (`SWITCHES_AND_HUBS`: Switches and Hubs product
                family),  (`WIRELESS_CONTROLLER`: Wireless controller product family),  (`UNIFIED_AP`:
                Unified Access Point product family),  .
            license_mode(str): licenseMode query parameter. Mode of license on the device. (License Mode:
                Description),  (`SMART_LICENSE`: Smart License mode),  (`RIGHT_TO_USE`: Right to use),
                (`UNKNOWN`: Mode of license on the device is not known.),  .
            license_type(str): licenseType query parameter. Type of license available on the network device.
                (License Type: Description),  (`NETWORK_ESSENTIALS`: Network Essentials license),
                (`NETWORK_ADVANTAGE`: Network Advantage license),  (`AIR_NETWORK_ESSENTIALS`: Air
                Network Essentials license. It is applicable for wireless controllers or switches having
                wireless capability.),  (`AIR_NETWORK_ADVANTAGE`: Air Network Advantage license. It is
                applicable for wireless controllers or switches having wireless capability.),
                (`DNA_ESSENTIALS`: DNA Essentials license),  (`DNA_ADVANTAGE`: DNA Advantage license),
                (`AIR_DNA_ESSENTIALS`: Air DNA Essentials license. It is applicable for wireless
                controllers or switches having wireless capability.),  (`AIR_DNA_ADVANTAGE`: Air DNA
                Advantage license. It is applicable for wireless controllers or switches having wireless
                capability),  (`CNS_ESSENTIALS`: Cisco Networking Subscription  Essentials license),
                (`CNS_ADVANTAGE`: Cisco Networking Subscription  Advantage license),  .
            license_status(str): licenseStatus query parameter. Status of license on the network device. (License
                Status: Description),  (`IN_USE`: A license is actively being used by a Cisco device and
                is currently authorized for features it enables.),  (`NOT_IN_USE`: A license is
                available on the device but is not currently being used by device.),  (`EXPIRED_IN_USE`:
                A license has expired but the device continues to use its features.),
                (`EXPIRED_NOT_IN_USE`: A license has expired and its features are not currently being
                utilized on the device.),  (`USAGE_COUNT_CONSUMED`: The allowed usage limit for the
                license has been fully utilized. It is only applicable for Cisco Nexus devices.),
                (`OUT_OF_COMPLIANCE`: A device is using features that require licenses it does not have
                assigned to it, potentially leading to functionality limitations.),
                (`EVALUATION_IN_USE`: A device is currently using a trial or evaluation license for its
                features.),  (`INACTIVE`: A license is available on the device but is not currently
                being used by device. This license status is only applicable for virtual wireless
                controllers.),  .
            registration_status(str): registrationStatus query parameter. Smart License registration status
                (Registration status: Description),  (`REGISTERED`: The network device instance is
                registered with CSSM.),  (`UNREGISTERED`: Smart Licensing is enabled on the network
                device, but the network device is not registered with CSSM.),  (`REGISTRATION_EXPIRED`:
                The registration has expired.),  (`RESERVATION_IN_PROGRESS`: The license reservation is
                in progress on the network device.),  (`REGISTERED_SLR`: The device has successfully
                completed the process of SLR and is now registered.),  (`REGISTERED_PLR`: The device has
                successfully completed the process of PLR and is now registered.),
                (`REGISTERED_SATELLITE`: The device is successfully registered with a On Prem CSSM
                server for Smart Licensing.),  (`NA`: The registration is not applicable for device.
                'NA' can be seen for devices having RTU license mode or device for which smart licensing
                using policy is applicable.),  (`UNKNOWN`: The registration state is not known on the
                device.),  .
            authorization_status(str): authorizationStatus query parameter. Smart License authorization status
                (Authorization Status: Description),  (`AUTHORIZED`: Registration has been completed
                with a valid Smart Account and license consumption has begun. The number of licenses
                consumed is less than the licenses available for use. This is an indication of being in
                compliance.),  (`EVALUATION_MODE`: The network device is running in evaluation mode when
                it is not registered.),  (`OUT_OF_COMPLIANCE`: The device's license consumption has
                exceeded the number of licenses that were purchased. The virtual account containing the
                product instance has a shortage of one or more of license types used.),
                (`EVALUATION_EXPIRED`: The evaluation period has expired and the device will be in
                unlicensed state.),  (`AUTHORIZATION_EXPIRED`: The authorization has expired.),
                (`NOT_AUTHORIZED`: The authorization is not valid.),  (`AUTHORIZED_RESERVED`:
                Registration of device has been completed using SLR/PLR with a valid Smart Account and
                license consumption has begun. The number of licenses consumed is less than the licenses
                available for use. This is an indication of being in compliance.),  (`NA`: The
                authorization is not applicable for device. 'NA' can be seen for devices having RTU mode
                or device for which smart licensing using policy is applicable),  (`UNKNOWN`: The
                authorization state is not known on the device.),  .
            auth_codestatus(str): authCodeStatus query parameter. Status of authorization code for network device.
                Smart Licensing authorization code enables the use of a HSEC license on the device. It
                is applicable for routers only. (Auth Code Status: Description),  (`INSTALLED`: If
                authorization code is installed on the device, the status will be INSTALLED.),
                (`NOT_INSTALLED`: If authorization code is not installed, the status will be
                NOT_INSTALLED.),  (`NA`: If authorization code is not applicable for the device, then
                the status will be NA.),  .
            smart_account_id(str): smartAccountId query parameter. Smart Account id where device is registered. Use
                `GET /dna/intent/api/v1/licenses/smartAccounts` intent API to find the smart account Id.
            virtual_account_id(str): virtualAccountId query parameter. Virtual Account id where device is
                registered. Use `GET /dna/intent/api/v1/licenses/smartAccount/${id}/virtualAccounts`
                intent API to find the virtual account Id.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-number-of-network-devices
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(family, str)
        check_type(license_mode, str)
        check_type(license_type, str)
        check_type(license_status, str)
        check_type(registration_status, str)
        check_type(authorization_status, str)
        check_type(auth_codestatus, str)
        check_type(smart_account_id, str)
        check_type(virtual_account_id, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "family": family,
            "licenseMode": license_mode,
            "licenseType": license_type,
            "licenseStatus": license_status,
            "registrationStatus": registration_status,
            "authorizationStatus": authorization_status,
            "authCodeStatus": auth_codestatus,
            "smartAccountId": smart_account_id,
            "virtualAccountId": virtual_account_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDeviceLicenses/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bf9cb870c41525b9c6a3546f0c3c65e_v3_2_3_0", json_data
        )

    def virtual_account_details(
        self, smart_account_id, headers=None, **request_parameters
    ):
        """Get virtual account details of a smart account.   Virtual Account Details : It gives virtual account details of
        a smart account.

        Args:
            smart_account_id(str): smart_account_id path parameter. Id of smart account.
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
            https://developer.cisco.com/docs/dna-center/#!virtual-account-details
        """
        check_type(headers, dict)
        check_type(smart_account_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "smart_account_id": smart_account_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/licenses/smartAccount/{smart_account_"
            + "id}/virtualAccounts"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ab450b197375fa9bcd95219113a3075_v3_2_3_0", json_data
        )

    def smart_licensing_deregistration(self, headers=None, **request_parameters):
        """Deregisters the system with Cisco Smart Software Manager (CSSM).               Deregisters the system with CSSM.
        If any other system license operation is in progress, then this API will result in HTTP status code  409
        .    .

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
            https://developer.cisco.com/docs/dna-center/#!smart-licensing-deregistration
        """
        check_type(headers, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
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

        e_url = "/dna/system/api/v1/license/deregister"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_df787402ab25f32b53dcf395b2742a8_v3_2_3_0", json_data
        )

    def license_term_details(
        self,
        device_type,
        smart_account_id,
        virtual_account_name,
        headers=None,
        **request_parameters
    ):
        """Get license term details. Deprecated since release 3.2.1 Alternatives: GET /dna/intent/api/v1/licenseUsage
        Deprecated since release 3.2.1. Alternatives: GET /dna/intent/api/v1/licenseUsage.

        Args:
            smart_account_id(str): smart_account_id path parameter. Id of smart account.
            virtual_account_name(str): virtual_account_name path parameter. Name of virtual account. Putting "All"
                will give license term detail for all virtual accounts.
            device_type(str): device_type query parameter. Type of device like router, switch, wireless or ise.
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
            https://developer.cisco.com/docs/dna-center/#!license-term-details
        """
        check_type(headers, dict)
        check_type(device_type, str, may_be_none=False)
        check_type(smart_account_id, str, may_be_none=False)
        check_type(virtual_account_name, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "device_type": device_type,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "smart_account_id": smart_account_id,
            "virtual_account_name": virtual_account_name,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/licenses/term/smartAccount/{smart_acc"
            + "ount_id}/virtualAccount/{virtual_account_name}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_df2d278e89b45c8ea0ca0a945c001f08_v3_2_3_0", json_data
        )

    def retrieves_license_details_of_a_network_device(
        self, id, headers=None, **request_parameters
    ):
        """API to retrieve the details of a network device and their licenses.

        Args:
            id(str): id path parameter. Unique ID of the license details of the network device.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-license-details-of-a-network-device
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

        e_url = "/dna/intent/api/v1/networkDeviceLicenses/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a6fd6f401759bc8f2dd6e751698eda_v3_2_3_0", json_data
        )

    def update_network_device_licenses(
        self,
        id,
        authCodeStatus=None,
        authorizationStatus=None,
        changeWirelessLicense=None,
        customerTags=None,
        family=None,
        hostname=None,
        lastSuccessfulUsageReportingTime=None,
        licenseLevel=None,
        licenseManagedBy=None,
        licenseMode=None,
        licenses=None,
        managementAddress=None,
        networkDeviceId=None,
        registrationStatus=None,
        series=None,
        siteHierarchy=None,
        smartAccountId=None,
        softwareVersion=None,
        throughputValue=None,
        triggerReboot=None,
        virtualAccountId=None,
        wirelessCapable=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """API to add, remove or update the license of a network device. This will update the Network, DNA, AIR-DNA and CNS
        licenses.

        Args:
            authCodeStatus(string): Licenses's Status of authorization code for network device. Smart Licensing
                authorization code enables the use of a HSEC license on the device. It is applicable for
                routers only. * `INSTALLED` If authorization code is installed on the device, status
                will be INSTALLED. * `NOT_INSTALLED` If authorization code is not installed, status will
                be NOT_INSTALLED. * `NA` If authorization code is not applicable for device then status
                will be NA. . Available values are 'INSTALLED', 'NOT_INSTALLED' and 'NA'.
            authorizationStatus(string): Licenses's Smart License authorization status.  | Authorization status
                | Description  | | ---------------------| ----------------------------------------------
                ----------------------------------------------------------------------------------------
                ------------------------------------------------------------------| | `AUTHORIZED`     |
                Registration has been completed with a valid Smart Account and license consumption has
                begun. The number of licenses consumed is less than the licenses available for use. This
                is an indication of being in compliance. | | `EVALUATION_MODE`              | The
                network device is running in evaluation mode when it is not registered. | |
                `OUT_OF_COMPLIANCE`     | The device's license consumption has exceeded the number of
                licenses that were purchased. The virtual account containing the product instance has a
                shortage of one or more of license types used. |    | `EVALUATION_EXPIRED`     | The
                evaluation period has expired and the device will be in unlicensed state. |    |
                `AUTHORIZATION_EXPIRED`     | The authorization has expired. | | `NOT_AUTHORIZED`     |
                The authorization is not valid.  | | `AUTHORIZED_RESERVED`     | Registration of device
                has been completed using SLR/PLR with a valid Smart Account and license consumption has
                begun. The number of licenses consumed is less than the licenses available for use. This
                is an indication of being in compliance. | | `NA`     | The authorization is not
                applicable for device. Authorization is not applicable for device having RTU mode or
                device for which smart licensing using policy is applicable | | `UNKNOWN`     | The
                authorization state is not known on the device. | . Available values are 'AUTHORIZED',
                'EVALUATION_MODE', 'OUT_OF_COMPLIANCE', 'EVALUATION_EXPIRED', 'AUTHORIZATION_EXPIRED',
                'NOT_AUTHORIZED', 'AUTHORIZED_RESERVED', 'NA' and 'UNKNOWN'.
            changeWirelessLicense(boolean): Licenses's This is only applicable to switches with wireless
                capabilities. It does not affect the operations performed for any other types of
                devices.  Setting this to true will modify the wireless license on the switch, while
                setting it to false will modify the switching license. .
            customerTags(object): Licenses's User defined tags that can be set to network devices to help identify
                telemetry data for a product instance.
            family(string): Licenses's Product family of the network device. | Family | Description
                | |--------------|------------------------------------------| | `ROUTERS`         |
                Router product family                       | | `SWITCHES_AND_HUBS`        | Switches
                and Hubs product family                             | | `WIRELESS_CONTROLLER`    |
                Wireless controller product family   | | `UNFIED_AP`    | Unified Access Point product
                family   | . Available values are 'ROUTERS', 'SWITCHES_AND_HUBS', 'WIRELESS_CONTROLLER'
                and 'UNIFIED_AP'.
            hostname(string): Licenses's Hostname of the network device.
            id(string): Licenses's Unique ID of the license details of the network device.
            lastSuccessfulUsageReportingTime(): Licenses's lastSuccessfulUsageReportingTime.
            licenseLevel(string): Licenses's The license level to be applied on the network device. Passing the
                license level as `NONE` will result in one of the following outcomes: 1. For wireless
                devices consuming CNS licenses, the license will be reset to the CNS Advantage license.
                2. For devices consuming DNA licenses, the DNA license will be removed, and the Network
                license will remain unaffected.  For more details, please refer to the "Change license
                level" section under the "Manage Licenses" chapter of this product's Administrator
                Guide. . Available values are 'ESSENTIALS', 'ADVANTAGE' and 'NONE'.
            licenseManagedBy(string): Licenses's A unique identifier for the network device responsible for managing
                licenses. For example, for an AP,  licenses are managed by a WLC.
            licenseMode(string): Licenses's Mode of license on the device. | License Mode | Description
                | |--------------|------------------------------------------| | `SMART_LICENSE`
                | Smart License mode                       | | `RIGHT_TO_USE`        | Right to use
                | | `UNKNOWN`    | Mode of license on the device is not known   | . Available values are
                'SMART_LICENSE', 'RIGHT_TO_USE' and 'UNKNOWN'.
            licenses(list): Licenses's List of licenses associated with the network device. For wireless controllers
                having access points which are consuming CNS license and DNA license both, it will have
                details of either `AIR_DNA_ESSENTIALS` or `AIR_DNA_ADVANTAGE`.  For switches having
                wireless capability, it will show wireless license which can be
                `AIR_DNA_ESSENTIALS`/`AIR_DNA_ADVANTAGE` and
                `AIR_NETWORK_ESSENTIALS`/`AIR_NETWORK_ADVANTAGE`.  (list of objects).
            managementAddress(): Licenses's managementAddress.
            networkDeviceId(string): Licenses's A unique identifier for the network device.
            registrationStatus(string): Licenses's Smart License registration status.  | Registration status
                | Description | | ---------------------| -----------------------------------------------
                ----------------------------------------------------------------------------------------
                -----------------------------------------------------------------| | `REGISTERED`
                | The network device instance is registered with CSSM.| | `UNREGISTERED`     | Smart
                Licensing is enabled on the network device, but the network device is not registered
                with CSSM. | | `REGISTRATION_EXPIRED`     | The registration has expired. | |
                `RESERVATION_IN_PROGRESS`     | The license reservation is in progress on the network
                device. | | `REGISTERED_SLR`     | The device has successfully completed the process of
                SLR and is now registered. | | `REGISTERED_PLR`     | The device has successfully
                completed the process of PLR and is now registered. | | `REGISTERED_SATELLITE`     | The
                device is successfully registered with a On Prem CSSM server for Smart Licensing. | |
                `NA`     | The registration is not applicable for device. 'NA' can be seen for devices
                having RTU license mode or device for which smart licensing using policy is applicable.
                | | `UNKNOWN`     | The registration state is not known on the device. | . Available
                values are 'REGISTERED', 'UNREGISTERED', 'REGISTRATION_EXPIRED',
                'RESERVATION_IN_PROGRESS', 'REGISTERED_SLR', 'REGISTERED_PLR', 'REGISTERED_SATELLITE',
                'NA' and 'UNKNOWN'.
            series(string): Licenses's The model range or series of the network device.
            siteHierarchy(string): Licenses's Site associated with device.
            smartAccountId(string): Licenses's Smart Account id where device is registered. Use
                `/dna/intent/api/v1/licenses/smartAccounts` intent API to find the smart account Id.
            softwareVersion(string): Licenses's Version of software running on the network device.
            throughputValue(string): Licenses's Current throughput level of the network device. It is only
                applicable for routers.
            triggerReboot(boolean): Licenses's Determines if a network device is to be rebooted after the license
                change operation has been completed. .
            virtualAccountId(string): Licenses's Virtual Account id where device is registered. Use
                `/dna/intent/api/v1/licenses/smartAccount/${id}/virtualAccounts` intent API to find the
                virtual account Id.
            wirelessCapable(boolean): Licenses's It indicates whether a switch is having wireless capability
                enabled. This field is present and set to `true` or `false` for switches. For other
                device types such as routers, wireless controllers and access points, this field is
                omitted.
            id(str): id path parameter. Unique ID of the license details of the network device.
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
            https://developer.cisco.com/docs/dna-center/#!update-network-device-licenses
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
            "managementAddress": managementAddress,
            "hostname": hostname,
            "family": family,
            "series": series,
            "siteHierarchy": siteHierarchy,
            "softwareVersion": softwareVersion,
            "licenseMode": licenseMode,
            "licenses": licenses,
            "licenseLevel": licenseLevel,
            "triggerReboot": triggerReboot,
            "changeWirelessLicense": changeWirelessLicense,
            "registrationStatus": registrationStatus,
            "authorizationStatus": authorizationStatus,
            "smartAccountId": smartAccountId,
            "virtualAccountId": virtualAccountId,
            "customerTags": customerTags,
            "authCodeStatus": authCodeStatus,
            "throughputValue": throughputValue,
            "lastSuccessfulUsageReportingTime": lastSuccessfulUsageReportingTime,
            "licenseManagedBy": licenseManagedBy,
            "wirelessCapable": wirelessCapable,
            "networkDeviceId": networkDeviceId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a437395e0d56988a527b6fefeadbfc_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDeviceLicenses/{id}"
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
            "bpm_a437395e0d56988a527b6fefeadbfc_v3_2_3_0", json_data
        )

    def change_virtual_account(
        self,
        smart_account_id,
        virtual_account_name,
        device_uuids=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Transfer device(s) from one virtual account to another within same smart account.   Change Virtual Account : It
        will transfer device(s) from one virtual account to another  virtual account within same smart account.

        Args:
            device_uuids(list): Licenses's Comma separated device ids (list of strings).
            smart_account_id(str): smart_account_id path parameter. Id of smart account.
            virtual_account_name(str): virtual_account_name path parameter. Name of target virtual account.
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
            https://developer.cisco.com/docs/dna-center/#!change-virtual-account
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(smart_account_id, str, may_be_none=False)
        check_type(virtual_account_name, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "smart_account_id": smart_account_id,
            "virtual_account_name": virtual_account_name,
        }
        _payload = {
            "device_uuids": device_uuids,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_bd5b507f58a50aab614e3d7409eec4c_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/licenses/smartAccount/{smart_account_"
            + "id}/virtualAccount/{virtual_account_name}/device/transfe"
            + "r"
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
            "bpm_bd5b507f58a50aab614e3d7409eec4c_v3_2_3_0", json_data
        )

    def smart_licensing_renew_operation(self, headers=None, **request_parameters):
        """Renews license registration and authorization status of the system with Cisco Smart Software Manager (CSSM).
        Renews the license registration and authorization status of the system with CSSM.   Use this API to sync
        the latest registration/authorization status in case there is a change in the system license
        count/status in the CSSM.   If not run, the license registration and authorization status will be
        renewed at its scheduled time.   If any other system license operation is in progress, then this API
        will result in HTTP status code  409 .    .

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
            https://developer.cisco.com/docs/dna-center/#!smart-licensing-renew-operation
        """
        check_type(headers, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
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

        e_url = "/dna/system/api/v1/license/renew"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f059aef5236f531b918cf6f8bd766f79_v3_2_3_0", json_data
        )

    def device_license_details(self, device_uuid, headers=None, **request_parameters):
        """Get detailed license information of a device. Deprecated since release 3.2.1 Alternatives: GET
        /dna/intent/api/v1/networkDeviceLicenses/{id}   Deprecated since release 3.2.1. Alternatives: GET
        /dna/intent/api/v1/networkDeviceLicenses/{id}.

        Args:
            device_uuid(str): device_uuid path parameter. Id of device.
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
            https://developer.cisco.com/docs/dna-center/#!device-license-details
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
            "device_uuid": device_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/licenses/device/{device_uuid}/details"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f04f865c01d5c17a5f0cb5abe620dd8_v3_2_3_0", json_data
        )

    def system_licensing_registration(
        self,
        smartAccountId=None,
        virtualAccountId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Registers the system with Cisco Smart Software Manager (CSSM).               Registers the system with CSSM. On
        registering the system, it will be able to communicate with CSSM. Only one system license operation can
        be run at a time. If any system license operation is already running, the API will return response in
        HTTP status code  409 .    .

        Args:
            smartAccountId(string): Licenses's The ID of the Smart Account to which the system is registered.
            virtualAccountId(string): Licenses's The ID of the Virtual Account to which the system is registered.
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
            https://developer.cisco.com/docs/dna-center/#!system-licensing-registration
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
            "smartAccountId": smartAccountId,
            "virtualAccountId": virtualAccountId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e6bca55256a0aac288486e38049b_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/system/api/v1/license/register"
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
            "bpm_e6bca55256a0aac288486e38049b_v3_2_3_0", json_data
        )
