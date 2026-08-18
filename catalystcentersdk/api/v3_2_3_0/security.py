"""Cisco Catalyst Center Security API wrapper.

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


class Security:
    """Cisco Catalyst Center Security API (version: 3.2.3.0).

    Wraps the Catalyst Center Security
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Security
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

    def retrieve_the_count_of_traffic_steering_policies(
        self, site_id=None, headers=None, **request_parameters
    ):
        """This API fetches the total number of steering policies.

        Args:
            site_id(str): siteId query parameter. A property to determine the count of policies associated with a
                given siteId.
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-the-count-of-traffic-steering-policies
        """
        check_type(headers, dict)
        check_type(site_id, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
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

        e_url = "/dna/intent/api/v1/trafficSteeringPolicys/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a4a399bbf5999a8736ff4b6c6c82e_v3_2_3_0", json_data
        )

    def delete_a_traffic_steering_contract(
        self, id, headers=None, **request_parameters
    ):
        """This API removes a steering contract using the specified ID.  The response includes a task object containing a
        taskId property and a URL for further details about the task. The deletion status of this steering
        contract can be found by accessing the provided URL.

        Args:
            id(str): id path parameter. The ID of the steering contract to delete.
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
            https://developer.cisco.com/docs/dna-center/#!delete-a-traffic-steering-contract
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

        e_url = "/dna/intent/api/v1/trafficSteeringContracts/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory("bpm_87145e63bf0ae35131894563_v3_2_3_0", json_data)

    def modify_a_traffic_steering_contract(
        self,
        id,
        createdTime=None,
        description=None,
        lastUpdatedTime=None,
        name=None,
        policyReferenceCount=None,
        ruleCount=None,
        rules=None,
        siteReferenceCount=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API modifies a steering contract using the given ID.   The `rules` must be organized in a specific order,
        with their priority based on this sequence. A contract can include a maximum of 250 `rules`.  To create
        a rule, the application must have predefined ports and protocols. If you need to specify the transport
        protocol, source port, and destination port, select the application with the advanced option to create
        the rule.  The response includes a task object with a taskId property and a URL for more details about
        the task. The update status of this steering contract can be found by accessing the provided URL.  Note:
        A maximum of 6 `ports` are supported as a comma-separated list.

        Args:
            createdTime(integer): Security's Create time of the traffic steering contract record; as measured in
                milliseconds since Unix epoch. During the contract creation, the `createdTime` and
                `lastUpdatedTime` values are identical.
            description(string): Security's The description for the traffic steering contract.
            id(string): Security's The unique identifier for the traffic steering contract.
            lastUpdatedTime(integer): Security's Last update time of the traffic steering contract record; as
                measured in milliseconds since Unix epoch. During the contract creation, the
                `createdTime` and `lastUpdatedTime` values are identical.
            name(string): Security's The unique name for the traffic steering contract.
            policyReferenceCount(integer): Security's Number of policies associated with this contract.
            ruleCount(integer): Security's Number of rules associated with this contract.
            rules(list): Security's rules (list of objects).
            siteReferenceCount(integer): Security's Number of sites associated with this contract.
            id(str): id path parameter. The ID of the steering contract to update.
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
            https://developer.cisco.com/docs/dna-center/#!modify-a-traffic-steering-contract
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
            "name": name,
            "description": description,
            "policyReferenceCount": policyReferenceCount,
            "ruleCount": ruleCount,
            "siteReferenceCount": siteReferenceCount,
            "rules": rules,
            "createdTime": createdTime,
            "lastUpdatedTime": lastUpdatedTime,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d53bf319d5e4984e4fc65ab016726_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/trafficSteeringContracts/{id}"
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
            "bpm_d53bf319d5e4984e4fc65ab016726_v3_2_3_0", json_data
        )

    def retrieve_a_traffic_steering_contract_by_its_id(
        self, id, views=None, headers=None, **request_parameters
    ):
        """This API fetches a  steering contract using a given id. The API supports views to fetch only the required
        fields.  **How views work**  The `views` parameter is an optional field to specify which attributes to
        retrieve. If this is not provided, then it will default to `DETAILED` views.  Attributes covered by the
        views are:  * `BASIC` : id, description, name, policyReferenceCount, ruleCount, siteReferenceCount,
        version.  * `DETAILED`: id, description, name, policyReferenceCount, ruleCount, siteReferenceCount,
        rules, createdTime, lastUpdatedTime, version.

        Args:
            id(str): id path parameter. The ID of the steering contract to retrieve.
            views(str): views query parameter. The specific views being requested. This is an optional parameter
                which can be passed. If this is not provided, then it will default to `DETAILED` views.
                Attributes covered by the views are: * `BASIC` : id, description, name,
                policyReferenceCount, ruleCount, siteReferenceCount, version.  * `DETAILED`: id,
                description, name, policyReferenceCount, ruleCount, siteReferenceCount, rules,
                createdTime, lastUpdatedTime, version. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-a-traffic-steering-contract-by-its-i-d
        """
        check_type(headers, dict)
        check_type(views, str)
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

        e_url = "/dna/intent/api/v1/trafficSteeringContracts/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cbd1deda0a53669c2546c954403c59_v3_2_3_0", json_data
        )

    def retrieves_the_top_n_analytics_data_related_to_contracts(
        self,
        limit=None,
        offset=None,
        order=None,
        sort_by=None,
        headers=None,
        **request_parameters
    ):
        """This API retrieves the top traffic steering contracts used by policies across network switches and firewalls.
        These contracts define the rules and conditions for managing network traffic, ensuring data flows
        efficiently and securely in accordance with organizational policies. By analyzing the usage of these
        contracts, the API provides valuable insights into how they are employed to optimize network performance
        and maintain security.

        Args:
            limit(int): limit query parameter. The number of top records to retrieve.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-top-n-analytics-data-related-to-contracts
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        check_type(sort_by, str)
        check_type(order, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
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

        e_url = "/dna/data/api/v1/trafficSteeringContracts/topNAnalytics"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ecaa42b157d557e7bc770de8e04a5f7c_v3_2_3_0", json_data
        )

    def retrieves_the_top_n_analytics_data_related_to_nodes(
        self,
        limit=None,
        offset=None,
        order=None,
        sort_by=None,
        headers=None,
        **request_parameters
    ):
        """This API retrieves the top switches data used by traffic steering policies across the network. It provides
        detailed analytics on the most utilized network nodes, focusing on switches that play a critical role in
        managing and directing network traffic. By accessing this data, network administrators can gain valuable
        insights into network performance and usage patterns. This information is essential for optimizing
        network operations, identifying potential bottlenecks, and ensuring efficient traffic flow. The API
        supports strategic planning and resource allocation by highlighting which switches are most actively
        involved in traffic management.

        Args:
            limit(int): limit query parameter. The number of top records to retrieve.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-top-n-analytics-data-related-to-nodes
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        check_type(sort_by, str)
        check_type(order, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
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

        e_url = "/dna/data/api/v1/trafficSteeringNodes/topNAnalytics"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ef26dc241f55b2b9d3e73aaafe20e46_v3_2_3_0", json_data
        )

    def retrieve_traffic_steering_contracts(
        self,
        limit=None,
        name=None,
        offset=None,
        order=None,
        sort_by=None,
        views=None,
        headers=None,
        **request_parameters
    ):
        """This API fetches a list of steering contracts. The response data can be sorted by `name`, `creationTime`, or
        `lastUpdatedTime`.  The API supports views to fetch only the required fields.  **How views work**  The
        `views` parameter is an optional field to specify which attributes to retrieve. If this is not provided,
        then it will default to `DETAILED` views.  Attributes covered by the views are:  * `BASIC` : id,
        description, name, policyReferenceCount, ruleCount, siteReferenceCount, version.   * `DETAILED`: id,
        description, name, policyReferenceCount, ruleCount, siteReferenceCount, rules, createdTime,
        lastUpdatedTime, version.  The API supports retrieving contract details with an optional `name` filter.

        Args:
            views(str): views query parameter. The specific views being requested. This is an optional parameter
                which can be passed. If this is not provided, then it will default to `DETAILED` views.
                Attributes covered by the views are: * `BASIC` : id, description, name,
                policyReferenceCount, ruleCount, siteReferenceCount, version.  * `DETAILED`: id,
                description, name, policyReferenceCount, ruleCount, siteReferenceCount, rules,
                createdTime, lastUpdatedTime, version. .
            name(str): name query parameter. A property to filter the response by contract name.
            limit(int): limit query parameter. The number of records to show for this page.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1.
            sort_by(str): sortBy query parameter. A property within the response to sortby.
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-traffic-steering-contracts
        """
        check_type(headers, dict)
        check_type(views, str)
        check_type(name, str)
        check_type(limit, int)
        check_type(offset, int)
        check_type(sort_by, str)
        check_type(order, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "views": views,
            "name": name,
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

        e_url = "/dna/intent/api/v1/trafficSteeringContracts"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c931889d86105c9998e82db6c2576e09_v3_2_3_0", json_data
        )

    def creates_a_traffic_steering_contract(
        self,
        createdTime=None,
        description=None,
        id=None,
        lastUpdatedTime=None,
        name=None,
        policyReferenceCount=None,
        ruleCount=None,
        rules=None,
        siteReferenceCount=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Creates the specified Traffic Steering contract.   The `rules` must be organized in a specific order, with their
        priority based on this sequence. A contract can include a maximum of 250 `rules`.  To create a rule, the
        application must have predefined ports and protocols. If you need to specify the transport protocol,
        source port, and destination port, select the application with the advanced option to create the rule.
        The response includes a task object with a taskId property and a URL for additional task details. You
        can verify the creation status of the steering contract by accessing the provided URL.   Note: A maximum
        of 6 `ports` are supported as a comma-separated list.

        Args:
            createdTime(integer): Security's Create time of the traffic steering contract record; as measured in
                milliseconds since Unix epoch. During the contract creation, the `createdTime` and
                `lastUpdatedTime` values are identical.
            description(string): Security's The description for the traffic steering contract.
            id(string): Security's The unique identifier for the traffic steering contract.
            lastUpdatedTime(integer): Security's Last update time of the traffic steering contract record; as
                measured in milliseconds since Unix epoch. During the contract creation, the
                `createdTime` and `lastUpdatedTime` values are identical.
            name(string): Security's The unique name for the traffic steering contract.
            policyReferenceCount(integer): Security's Number of policies associated with this contract.
            ruleCount(integer): Security's Number of rules associated with this contract.
            rules(list): Security's rules (list of objects).
            siteReferenceCount(integer): Security's Number of sites associated with this contract.
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
            https://developer.cisco.com/docs/dna-center/#!creates-a-traffic-steering-contract
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
            "description": description,
            "policyReferenceCount": policyReferenceCount,
            "ruleCount": ruleCount,
            "siteReferenceCount": siteReferenceCount,
            "rules": rules,
            "createdTime": createdTime,
            "lastUpdatedTime": lastUpdatedTime,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator("jsd_861f5414a7c5818844cb4d1a_v3_2_3_0").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/trafficSteeringContracts"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory("bpm_861f5414a7c5818844cb4d1a_v3_2_3_0", json_data)

    def update_a_steering_policy(
        self,
        id,
        contractId=None,
        contractName=None,
        createdTime=None,
        destinationId=None,
        destinationName=None,
        lastUpdatedTime=None,
        siteId=None,
        sourceId=None,
        sourceName=None,
        virtualNetworkFirewall=None,
        virtualNetworkFirewallCount=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API updates a steering policy using the specified ID.  To retrieve the list of possible values for
        `virtualNetworkFirewall` when creating a policy, the user should utilize the intent API
        `/dna/intent/api/v1/securityServiceInsertions`  To obtain the list of potential values for `contactId`
        when establishing a policy, the user should use the intent API endpoint
        `/dna/intent/api/v1/trafficSteeringContracts`.  Note that `siteId` and `sourceId` cannot be modified.
        Any time a customer updates a traffic-steering policy, a deployment must be explicitly triggered using
        `/dna/intent/api/v1/trafficSteeringPolicys/deploy` for the updated configuration to  propagate to the
        network devices.

        Args:
            contractId(string): Security's A unique identifier for a specific steering contract.
            contractName(string): Security's Name of the steering contract.
            createdTime(integer): Security's Create time of the traffic steering policy record; as measured in
                milliseconds since Unix epoch. During the policy creation, the `createdTime` and
                `lastUpdatedTime` values are identical.
            destinationId(string): Security's A unique identifier for a selected destination.
            destinationName(string): Security's Name of the destination.
            id(string): Security's The unique identifier for the traffic steering policy.
            lastUpdatedTime(integer): Security's Last update time of the traffic steering policy record; as measured
                in milliseconds since Unix epoch. During the contract creation, the `createdTime` and
                `lastUpdatedTime` values are identical.
            siteId(string): Security's A site identifier for a specific fabric site.
            sourceId(string): Security's A unique identifier for a selected source.
            sourceName(string): Security's Name of the source.
            virtualNetworkFirewall(list): Security's It includes details related to the virtual network, such as the
                virtual network ID, which are linked to a steering policy and contract. (list of
                objects).
            virtualNetworkFirewallCount(integer): Security's The count of virtual firewalls linked to this policy.
            id(str): id path parameter. The ID of the steering policy to update.
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
            https://developer.cisco.com/docs/dna-center/#!update-a-steering-policy
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
            "contractId": contractId,
            "contractName": contractName,
            "createdTime": createdTime,
            "destinationId": destinationId,
            "destinationName": destinationName,
            "lastUpdatedTime": lastUpdatedTime,
            "siteId": siteId,
            "sourceId": sourceId,
            "sourceName": sourceName,
            "virtualNetworkFirewall": virtualNetworkFirewall,
            "virtualNetworkFirewallCount": virtualNetworkFirewallCount,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_fedddf05435682aeb8606e13d00ecd_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/trafficSteeringPolicys/{id}"
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
            "bpm_fedddf05435682aeb8606e13d00ecd_v3_2_3_0", json_data
        )

    def retrieve_a_traffic_steering_policy(
        self, id, views=None, headers=None, **request_parameters
    ):
        """This API fetches a steering policy using a given id.  **How views work**  The `views` parameter is an optional
        field to specify which attributes to retrieve. If this is not provided, then it will default to
        `DETAILED` views.   Attributes covered by the views are:   * `BASIC` : id, contractName,
        destinationName, sourceName,   virtualNetworkFirewallCount, version.    * `DETAILED`:id, contractId,
        contractName, createdTime, destinationName, destinationId,  siteId, sourceId, sourceName,
        lastUpdatedTime, virtualNetworkFirewallCount, virtualNetworkFirewall, version.".

        Args:
            id(str): id path parameter. The ID of the steering policy to retrieve.
            views(str): views query parameter.  The specific views being requested. This is an optional parameter
                which can be passed. If this is not provided, then it will default to `DETAILED` views.
                Attributes covered by the views are: * `BASIC` : id, contractName, destinationName,
                sourceName,   virtualNetworkFirewallCount, version.  * `DETAILED`:id, contractId,
                contractName, createdTime, destinationName, destinationId,  siteId, sourceId,
                sourceName, lastUpdatedTime, virtualNetworkFirewallCount, virtualNetworkFirewall,
                version." .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-a-traffic-steering-policy
        """
        check_type(headers, dict)
        check_type(views, str)
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

        e_url = "/dna/intent/api/v1/trafficSteeringPolicys/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a45d7e58f4175ebd9df1322f769150f7_v3_2_3_0", json_data
        )

    def delete_a_steering_policy(self, id, headers=None, **request_parameters):
        """This API deletes a steering policy using the specified ID.  Any time a customer deletes a traffic-steering
        policy, a deployment must be explicitly triggered using
        `/dna/intent/api/v1/trafficSteeringPolicys/deploy` for the updated configuration to  propagate to the
        network devices.

        Args:
            id(str): id path parameter. The ID of the steering policy to delete.
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
            https://developer.cisco.com/docs/dna-center/#!delete-a-steering-policy
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

        e_url = "/dna/intent/api/v1/trafficSteeringPolicys/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b86a66f5a355cbe8727b5026f3e2386_v3_2_3_0", json_data
        )

    def retrieve_the_count_of_traffic_steering_contracts(
        self, headers=None, **request_parameters
    ):
        """This API fetches the total number of traffic steering contracts.

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
            https://developer.cisco.com/docs/dna-center/#!retrieve-the-count-of-traffic-steering-contracts
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

        e_url = "/dna/intent/api/v1/trafficSteeringContracts/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ab4f06dfba25e38993beb7dc6c40e17_v3_2_3_0", json_data
        )

    def creates_a_traffic_steering_policy(
        self,
        contractId=None,
        contractName=None,
        createdTime=None,
        destinationId=None,
        destinationName=None,
        id=None,
        lastUpdatedTime=None,
        siteId=None,
        sourceId=None,
        sourceName=None,
        virtualNetworkFirewall=None,
        virtualNetworkFirewallCount=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API is used to create a steering policy.  To retrieve the list of possible values for
        `virtualNetworkFirewall` when creating a policy, the user should utilize the intent API
        `/dna/intent/api/v1/securityServiceInsertions`  To obtain the list of potential values for `contractId`
        when establishing a policy, the user should use the intent API endpoint
        `/dna/intent/api/v1/trafficSteeringContracts`.  Any time a customer creates traffic-steering policy, a
        deployment must be explicitly triggered using `/dna/intent/api/v1/trafficSteeringPolicys/deploy` for the
        updated configuration to  propagate to the network devices.

        Args:
            contractId(string): Security's A unique identifier for a specific steering contract.
            contractName(string): Security's Name of the steering contract.
            createdTime(integer): Security's Create time of the traffic steering policy record; as measured in
                milliseconds since Unix epoch. During the policy creation, the `createdTime` and
                `lastUpdatedTime` values are identical.
            destinationId(string): Security's A unique identifier for a selected destination.
            destinationName(string): Security's Name of the destination.
            id(string): Security's The unique identifier for the traffic steering policy.
            lastUpdatedTime(integer): Security's Last update time of the traffic steering policy record; as measured
                in milliseconds since Unix epoch. During the contract creation, the `createdTime` and
                `lastUpdatedTime` values are identical.
            siteId(string): Security's A site identifier for a specific fabric site.
            sourceId(string): Security's A unique identifier for a selected source.
            sourceName(string): Security's Name of the source.
            virtualNetworkFirewall(list): Security's It includes details related to the virtual network, such as the
                virtual network ID, which are linked to a steering policy and contract. (list of
                objects).
            virtualNetworkFirewallCount(integer): Security's The count of virtual firewalls linked to this policy.
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
            https://developer.cisco.com/docs/dna-center/#!creates-a-traffic-steering-policy
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
            "contractId": contractId,
            "contractName": contractName,
            "createdTime": createdTime,
            "destinationId": destinationId,
            "destinationName": destinationName,
            "lastUpdatedTime": lastUpdatedTime,
            "siteId": siteId,
            "sourceId": sourceId,
            "sourceName": sourceName,
            "virtualNetworkFirewall": virtualNetworkFirewall,
            "virtualNetworkFirewallCount": virtualNetworkFirewallCount,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d965a3ad0a645aa3951189baf7329480_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/trafficSteeringPolicys"
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
            "bpm_d965a3ad0a645aa3951189baf7329480_v3_2_3_0", json_data
        )

    def retrieve_traffic_steering_policies(
        self,
        contract_name=None,
        destination_name=None,
        limit=None,
        offset=None,
        order=None,
        site_id=None,
        sort_by=None,
        source_name=None,
        views=None,
        headers=None,
        **request_parameters
    ):
        """This API retrieves the list of steering policies. The response data can be sorted by the time the instance was
        created or updated.  The API supports views to fetch only the required fields.  **How views work**  The
        `views` parameter is an optional field to specify which attributes to retrieve. If this is not provided,
        then it will default to `DETAILED` views.  Attributes covered by the views are:  * `BASIC` : id,
        contractName, destinationName, sourceName,   virtualNetworkFirewallCount, version.   * `DETAILED`:id,
        contractId, contractName, createdTime, destinationName, destinationId,  siteId, sourceId, sourceName,
        lastUpdatedTime, virtualNetworkFirewallCount, virtualNetworkFirewall, version.".

        Args:
            views(str): views query parameter. The specific views being requested. This is an optional parameter
                which can be passed. If this is not provided, then it will default to `DETAILED` views.
                Attributes covered by the views are: * `BASIC` : id, contractName, destinationName,
                sourceName,   virtualNetworkFirewallCount, version.  * `DETAILED`:id, contractId,
                contractName, createdTime, destinationName, destinationId,  siteId, sourceId,
                sourceName, lastUpdatedTime, virtualNetworkFirewallCount, virtualNetworkFirewall,
                version." .
            site_id(str): siteId query parameter. A property to filter the response by the site ID.
            source_name(str): sourceName query parameter. A property to filter the response by the sourceName.
            destination_name(str): destinationName query parameter. A property to filter the response by the
                destinationName.
            contract_name(str): contractName query parameter. A property to filter the response by the contractName.
            limit(int): limit query parameter. The number of records to show for this page.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1.
            sort_by(str): sortBy query parameter. A property within the response to sortby.
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-traffic-steering-policies
        """
        check_type(headers, dict)
        check_type(views, str)
        check_type(site_id, str)
        check_type(source_name, str)
        check_type(destination_name, str)
        check_type(contract_name, str)
        check_type(limit, int)
        check_type(offset, int)
        check_type(sort_by, str)
        check_type(order, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "views": views,
            "siteId": site_id,
            "sourceName": source_name,
            "destinationName": destination_name,
            "contractName": contract_name,
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

        e_url = "/dna/intent/api/v1/trafficSteeringPolicys"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ef1b2329f56e51b69b02e8f913c87e6b_v3_2_3_0", json_data
        )

    def create_multiple_traffic_steering_policies_in_bulk(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """This endpoint enables the creation of several policies within a single request. The maximum number of supported
        policies is 12,500.  To retrieve the list of possible values for `virtualNetworkFirewall` when creating
        a policy, the user should utilize the intent API `/dna/intent/api/v1/securityServiceInsertions`  To
        obtain the list of potential values for `contactId` when establishing a policy, the user should use the
        intent API endpoint `/dna/intent/api/v1/trafficSteeringContracts`.  Any time a customer creates traffic-
        steering policy, a deployment must be explicitly triggered using
        `/dna/intent/api/v1/trafficSteeringPolicys/deploy` for the updated configuration to  propagate to the
        network devices.

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
            https://developer.cisco.com/docs/dna-center/#!create-multiple-traffic-steering-policies-in-bulk
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_ebc24be555d90b775c0070622ce24_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/trafficSteeringPolicys/bulk"
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
            "bpm_ebc24be555d90b775c0070622ce24_v3_2_3_0", json_data
        )

    def retrieves_the_top_n_analytics_data_related_to_firewalls(
        self,
        limit=None,
        offset=None,
        order=None,
        sort_by=None,
        headers=None,
        **request_parameters
    ):
        """This API retrieves the top firewalls used by traffic steering policies across the network. It provides
        comprehensive analytics on firewalls that are most frequently utilized in directing and managing network
        traffic. By accessing this data, network administrators can gain valuable insights into how firewalls
        are performing, which ones are most active, and how they contribute to overall network security and
        efficiency. This information is crucial for optimizing network security policies, identifying potential
        vulnerabilities, and ensuring effective traffic management. The API supports strategic decision-making
        and resource allocation by highlighting the firewalls that play a key role in maintaining network
        integrity and performance.

        Args:
            limit(int): limit query parameter. The number of top records to retrieve.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-top-n-analytics-data-related-to-firewalls
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        check_type(sort_by, str)
        check_type(order, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
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

        e_url = "/dna/data/api/v1/trafficSteeringFirewalls/topNAnalytics"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cb0938df3f5602ae040dd1e42920e2_v3_2_3_0", json_data
        )
