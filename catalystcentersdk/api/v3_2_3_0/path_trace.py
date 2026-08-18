"""Cisco Catalyst Center Path Trace API wrapper.

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


class PathTrace:
    """Cisco Catalyst Center Path Trace API (version: 3.2.3.0).

    Wraps the Catalyst Center Path Trace
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new PathTrace
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

    def retrieves_previous_path_trace_result(
        self, id, view=None, headers=None, **request_parameters
    ):
        """Returns result of a previously requested path trace by its ID.  This response contains the detailed calculated
        path represented as a directed acyclic graph with all nodes and links.  In case of error, it contains
        details on the reason for failure.  **Note:** Path Trace requests are automatically deleted after 24
        hours.

        Args:
            id(str): id path parameter. Unique identifier for the path trace request to be retrieved. .
            view(list, set, str, tuple): view query parameter. Specifies which detailed information to include in
                the response. (Value: Description: Fields),  (acl: Include Access Control List (ACL)
                information: aclStatus, aclName, aclResult, aclRules),  (qos: Include Quality of Service
                (QoS) information: dropRate, numBytes, numPackets, offeredRate, queueBandwidthInBps,
                queueDepth, queueNoBufferDrops, queueTotalDrops),  (flexConnect: Include FlexConnect
                information for wireless access points: dataSwitching, authentication,
                wirelessLanControllerId, ingressAclAnalysis, egressAclAnalysis,
                wirelessLanControllerName),  (accuracyList: Include accuracy assessment information:
                List of [accuracy(percentage), reason(reason for decrease in accuracy)] computed using
                Netflow),  (deviceStatistics: Include CPU and memory statistics for devices:
                cpuStatistics fiveMinUsageInPercentage. fiveSecsUsageInPercentage,
                oneMinUsageInPercentage, refreshedAt; memoryStatistics memoryUsed, totalMemory,
                refreshedAt),  (performanceMonitorStatistics: Include performance monitoring statistics:
                packetCount, byteRate, packetLoss, packetLossPercentage, rtpJitterMean, rtpJitterMin,
                rtpJitterMax, ipv4DSCP, ipv4TTL, inputInterface, outputInterface, refreshedAt,
                sourceIpAddress, destIpAddress, protocol, sourcePort, destPort, packetBytes),
                (interfaceStatistics: Include interface statistics information: adminStatus,
                inputPackets, inputQueueDrops, inputQueueMaxDepth, inputQueueCount, inputQueueFlushes,
                inputRateInBps, operationalStatus, outputDrop, outputPackets, outputQueueCount,
                outputQueueDepth, outputRateInBps, refreshedAt),   If no view is specified, only the
                default fields are returned. Multiple views can be specified as exploded query
                parameters. e.g. : `view=qos&view=acl` .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-previous-path-trace-result
        """
        check_type(headers, dict)
        check_type(view, (list, set, str, tuple))
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
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

        e_url = "/dna/intent/api/v1/pathTraces/{id}/result"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d7cc6ea2f45cd9b213b244de5c59bf_v3_2_3_0", json_data
        )

    def retrieves_the_count_of_path_traces_matching_filter_criteria(
        self,
        destination_ip_address=None,
        destination_mac_address=None,
        destination_port=None,
        greater_than_create_time=None,
        last_update_time=None,
        less_than_create_time=None,
        periodic_refresh=None,
        protocol=None,
        source_ip_address=None,
        source_mac_address=None,
        source_port=None,
        status=None,
        headers=None,
        **request_parameters
    ):
        """Returns the count of path traces that match the specified filter parameters.  This endpoint accepts the same
        filter parameters as the GET /pathTraces endpoint, but instead of returning the details of the path
        traces, it returns only the count.  **Note:** Path Trace requests are automatically deleted after 24
        hours.

        Args:
            periodic_refresh(bool): periodicRefresh query parameter. Indicates whether the analysis is periodically
                refreshed. (false: Analysis is performed once),  .
            source_ip_address(str): sourceIpAddress query parameter. Source IP address used in the path trace.
                Format can be IPv4 (e.g., 192.168.1.1) or IPv6. .
            source_mac_address(str): sourceMacAddress query parameter. Source MAC address used in the path trace.
                Format should be XX:XX:XX:XX:XX:XX (e.g., 00:1A:2B:3C:4D:5E). .
            destination_ip_address(str): destinationIpAddress query parameter. Destination IP address used in the
                path trace. Format can be IPv4 (e.g., 192.168.1.1) or IPv6. .
            destination_mac_address(str): destinationMacAddress query parameter. Destination MAC address used in the
                path trace. Format should be XX:XX:XX:XX:XX:XX (e.g., 00:1A:2B:3C:4D:5E). .
            source_port(int): sourcePort query parameter. Source port used in the path trace. Valid range is
                1-65535. .
            destination_port(int): destinationPort query parameter. Destination port used in the path trace. Valid
                range is 1-65535. .
            greater_than_create_time(int): greaterThanCreateTime query parameter. Retrieves analyses requested after
                this time. Value is in epoch milliseconds. .
            less_than_create_time(int): lessThanCreateTime query parameter. Retrieves analyses requested before this
                time. Value is in epoch milliseconds. .
            protocol(str): protocol query parameter. Protocol used in the path trace. (UDP: User Datagram Protocol),
                .
            status(str): status query parameter. Status of the path trace. (SCHEDULED: Path trace is scheduled to
                run),  (PENDING: Path trace is pending execution),  (COMPLETED: Path trace has
                completed),  .
            last_update_time(int): lastUpdateTime query parameter. Retrieves analyses that were last updated at this
                time. Value is in epoch milliseconds. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-count-of-path-traces-matching-filter-criteria
        """
        check_type(headers, dict)
        check_type(periodic_refresh, bool)
        check_type(source_ip_address, str)
        check_type(source_mac_address, str)
        check_type(destination_ip_address, str)
        check_type(destination_mac_address, str)
        check_type(source_port, int)
        check_type(destination_port, int)
        check_type(greater_than_create_time, int)
        check_type(less_than_create_time, int)
        check_type(protocol, str)
        check_type(status, str)
        check_type(last_update_time, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "periodicRefresh": periodic_refresh,
            "sourceIpAddress": source_ip_address,
            "sourceMacAddress": source_mac_address,
            "destinationIpAddress": destination_ip_address,
            "destinationMacAddress": destination_mac_address,
            "sourcePort": source_port,
            "destinationPort": destination_port,
            "greaterThanCreateTime": greater_than_create_time,
            "lessThanCreateTime": less_than_create_time,
            "protocol": protocol,
            "status": status,
            "lastUpdateTime": last_update_time,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/pathTraces/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c1ab1b11f541090f55245ecd327fb_v3_2_3_0", json_data
        )

    def deletes_path_trace_by_id(self, id, headers=None, **request_parameters):
        """Deletes a path trace request by its id.  **Note:** Path Trace requests are automatically deleted after 24 hours
        regardless of this operation.

        Args:
            id(str): id path parameter. Unique identifier for the path trace request to be deleted. .
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
            https://developer.cisco.com/docs/dna-center/#!deletes-path-trace-by-i-d
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

        e_url = "/dna/intent/api/v1/pathTraces/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a202e493b5d7899cc77bbdab1c409_v3_2_3_0", json_data
        )

    def retrieves_the_summary_of_a_specific_path_trace(
        self, id, headers=None, **request_parameters
    ):
        """Returns a summary of a specific path trace by its ID without the detailed path trace information.  The summary
        response contains the original path trace request data, along with the current status of its execution.
        It does not contain the entire resultant path in case of success. Please use the `GET
        /dna/intent/api/v1/pathTraces/{id}/result` instead for path details.  **Note:** Path Trace requests are
        automatically deleted after 24 hours.

        Args:
            id(str): id path parameter. Unique identifier for the path trace request summary to be retrieved. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-summary-of-a-specific-path-trace
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

        e_url = "/dna/intent/api/v1/pathTraces/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a249ce703a589dae0b88ce5fb9ac9a_v3_2_3_0", json_data
        )

    def initiate_a_new_pathtrace(
        self,
        controlPath=None,
        destIP=None,
        destPort=None,
        inclusions=None,
        periodicRefresh=None,
        protocol=None,
        sourceIP=None,
        sourcePort=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Initiates a new flow analysis with periodic refresh and stat collection options. Returns a request id and a task
        id to get results and follow progress.     Deprecated since CatC-3.2.1. Please use this instead: POST
        /dna/intent/api/v1/pathTraces.

        Args:
            controlPath(boolean): Path Trace's Control path tracing.
            destIP(string): Path Trace's Destination IP address.
            destPort(string): Path Trace's Destination Port, range: 1-65535.
            inclusions(list): Path Trace's Subset of {INTERFACE-STATS, QOS-STATS, DEVICE-STATS, PERFORMANCE-STATS,
                ACL-TRACE} (list of strings).
            periodicRefresh(boolean): Path Trace's Periodic refresh of path for every 30 sec.
            protocol(string): Path Trace's Protocol one of [TCP, UDP] checks both when left blank.
            sourceIP(string): Path Trace's Source IP address.
            sourcePort(string): Path Trace's Source Port, range: 1-65535.
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
            https://developer.cisco.com/docs/dna-center/#!initiate-a-new-pathtrace
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
            "controlPath": controlPath,
            "destIP": destIP,
            "destPort": destPort,
            "inclusions": inclusions,
            "periodicRefresh": periodicRefresh,
            "protocol": protocol,
            "sourceIP": sourceIP,
            "sourcePort": sourcePort,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a54fce1a0c305bdabfe91a8a6161e539_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/flow-analysis"
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
            "bpm_a54fce1a0c305bdabfe91a8a6161e539_v3_2_3_0", json_data
        )

    def retrieves_all_previous_pathtraces_summary(
        self,
        dest_ip=None,
        dest_port=None,
        gt_create_time=None,
        last_update_time=None,
        limit=None,
        lt_create_time=None,
        offset=None,
        order=None,
        periodic_refresh=None,
        protocol=None,
        sort_by=None,
        source_ip=None,
        source_port=None,
        status=None,
        task_id=None,
        headers=None,
        **request_parameters
    ):
        """Returns a summary of all flow analyses stored. Results can be filtered by specified parameters.  Deprecated
        since CatC-3.2.1. Please use this instead: GET /dna/intent/api/v1/pathTraces.

        Args:
            periodic_refresh(bool): periodicRefresh query parameter. Is analysis periodically refreshed?.
            source_ip(str): sourceIP query parameter. Source IP address.
            dest_ip(str): destIP query parameter. Destination IP address.
            source_port(int): sourcePort query parameter. Source port.
            dest_port(int): destPort query parameter. Destination port.
            gt_create_time(int): gtCreateTime query parameter. Analyses requested after this time.
            lt_create_time(int): ltCreateTime query parameter. Analyses requested before this time.
            protocol(str): protocol query parameter.
            status(str): status query parameter.
            task_id(str): taskId query parameter. Task ID.
            last_update_time(int): lastUpdateTime query parameter. Last update time.
            limit(int): limit query parameter. Number of resources returned.
            offset(int): offset query parameter. Start index of resources returned (1-based).
            order(str): order query parameter. Order by this field.
            sort_by(str): sortBy query parameter. Sort by this field.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-all-previous-pathtraces-summary
        """
        check_type(headers, dict)
        check_type(periodic_refresh, bool)
        check_type(source_ip, str)
        check_type(dest_ip, str)
        check_type(source_port, int)
        check_type(dest_port, int)
        check_type(gt_create_time, int)
        check_type(lt_create_time, int)
        check_type(protocol, str)
        check_type(status, str)
        check_type(task_id, str)
        check_type(last_update_time, int)
        check_type(limit, int)
        check_type(offset, int)
        check_type(order, str)
        check_type(sort_by, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "periodicRefresh": periodic_refresh,
            "sourceIP": source_ip,
            "destIP": dest_ip,
            "sourcePort": source_port,
            "destPort": dest_port,
            "gtCreateTime": gt_create_time,
            "ltCreateTime": lt_create_time,
            "protocol": protocol,
            "status": status,
            "taskId": task_id,
            "lastUpdateTime": last_update_time,
            "limit": limit,
            "offset": offset,
            "order": order,
            "sortBy": sort_by,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/flow-analysis"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a75e4b27171c5c6782e84f902da9e5be_v3_2_3_0", json_data
        )

    def retrieves_the_summary_of_all_previous_path_traces(
        self,
        destination_ip_address=None,
        destination_mac_address=None,
        destination_port=None,
        greater_than_create_time=None,
        last_update_time=None,
        less_than_create_time=None,
        limit=None,
        offset=None,
        order=None,
        periodic_refresh=None,
        protocol=None,
        sort_by=None,
        source_ip_address=None,
        source_mac_address=None,
        source_port=None,
        status=None,
        headers=None,
        **request_parameters
    ):
        """Returns a summary of all path traces stored. Results can be filtered by specified parameters.  The summary
        response contains the original path trace request data, along with the current status of its execution.
        It does not contain the entire resultant path in case of success. Please use the `GET
        /dna/intent/api/v1/pathTraces/{id}/result` instead for path details.  **Note:** Path Trace requests are
        automatically deleted after 24 hours.

        Args:
            periodic_refresh(bool): periodicRefresh query parameter. Indicates whether the analysis is periodically
                refreshed. (Value: Description),  (true: Analysis is refreshed every 30 seconds),
                (false: Analysis is performed once),  .
            source_ip_address(str): sourceIpAddress query parameter. Source IP address used in the path trace.
                Format can be IPv4 (e.g., 192.168.1.1) or IPv6. .
            source_mac_address(str): sourceMacAddress query parameter. Source MAC address used in the path trace.
                Format should be XX:XX:XX:XX:XX:XX (e.g., 00:1A:2B:3C:4D:5E). .
            destination_ip_address(str): destinationIpAddress query parameter. Destination IP address used in the
                path trace. Format can be IPv4 (e.g., 192.168.1.1) or IPv6. .
            destination_mac_address(str): destinationMacAddress query parameter. Destination MAC address used in the
                path trace. Format should be XX:XX:XX:XX:XX:XX (e.g., 00:1A:2B:3C:4D:5E). .
            source_port(int): sourcePort query parameter. Source port used in the path trace. Valid range is
                1-65535. .
            destination_port(int): destinationPort query parameter. Destination port used in the path trace. Valid
                range is 1-65535. .
            greater_than_create_time(int): greaterThanCreateTime query parameter. Retrieves analyses requested after
                this time. Value is in epoch milliseconds. .
            less_than_create_time(int): lessThanCreateTime query parameter. Retrieves analyses requested before this
                time. Value is in epoch milliseconds. .
            protocol(str): protocol query parameter. Protocol used in the path trace. (Value: Description),  (TCP:
                Transmission Control Protocol),  (UDP: User Datagram Protocol),  .
            status(str): status query parameter. Status of the path trace. (Value: Description),  (SUCCESS: Path
                trace completed successfully),  (INPROGRESS: Path trace is currently running),  (FAILED:
                Path trace failed to complete),  (SCHEDULED: Path trace is scheduled to run),  (PENDING:
                Path trace is pending execution),  (COMPLETED: Path trace has completed),  .
            last_update_time(int): lastUpdateTime query parameter. Retrieves analyses that were last updated at this
                time. Value is in epoch milliseconds. .
            limit(int): limit query parameter. Maximum number of resources to return in the response. Use for
                pagination. .
            offset(int): offset query parameter. Starting index of resources to be returned (1-based). Use for
                pagination. .
            order(str): order query parameter. Sorting order for the returned results. (Value: Description),  (asc:
                Ascending order),  (desc: Descending order),  .
            sort_by(str): sortBy query parameter. Field to sort the results by. Common values include: createTime,
                status, sourceIpAddress, destinationIpAddress. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-summary-of-all-previous-path-traces
        """
        check_type(headers, dict)
        check_type(periodic_refresh, bool)
        check_type(source_ip_address, str)
        check_type(source_mac_address, str)
        check_type(destination_ip_address, str)
        check_type(destination_mac_address, str)
        check_type(source_port, int)
        check_type(destination_port, int)
        check_type(greater_than_create_time, int)
        check_type(less_than_create_time, int)
        check_type(protocol, str)
        check_type(status, str)
        check_type(last_update_time, int)
        check_type(limit, int)
        check_type(offset, int)
        check_type(order, str)
        check_type(sort_by, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "periodicRefresh": periodic_refresh,
            "sourceIpAddress": source_ip_address,
            "sourceMacAddress": source_mac_address,
            "destinationIpAddress": destination_ip_address,
            "destinationMacAddress": destination_mac_address,
            "sourcePort": source_port,
            "destinationPort": destination_port,
            "greaterThanCreateTime": greater_than_create_time,
            "lessThanCreateTime": less_than_create_time,
            "protocol": protocol,
            "status": status,
            "lastUpdateTime": last_update_time,
            "limit": limit,
            "offset": offset,
            "order": order,
            "sortBy": sort_by,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/pathTraces"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c53cecf7e5b54cb8d23310ecd049e15_v3_2_3_0", json_data
        )

    def initiate_a_new_path_trace(
        self,
        controlPath=None,
        destinationIpAddress=None,
        destinationMacAddress=None,
        destinationPort=None,
        inclusions=None,
        periodicRefresh=None,
        protocol=None,
        sourceIpAddress=None,
        sourceMacAddress=None,
        sourcePort=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Initiates a new path trace with periodic refresh and stat collection options. Returns a request id and a task id
        to get results and follow progress.  **Important Notes:** The source and destination IP addresses must
        both be either IPv4 or IPv6. Mixing IPv4 and IPv6 addresses is not allowed. Maximum number of IN-
        PROGRESS path trace requests that can exist at any time is 25. If this limit is reached, new requests
        will be rejected with a 500 error until existing requests complete or are deleted. Path Trace requests
        are automatically deleted after 24 hours.  ### Request Body Properties  | Property | Type | Required |
        Description | |----------|------|----------|-------------| | `sourceIpAddress` | string | Yes | The
        source IP address for the path trace. This is where the path trace will start. Must be a valid IPv4
        (e.g., 192.168.1.1) or IPv6 address. This field is required for all path traces. The client/device must
        be visible on Catalyst Center | | `destinationIpAddress` | string | Yes | The destination IP address for
        the path trace. This is where the path trace will end. Must be a valid IPv4 (e.g., 192.168.1.1) or IPv6
        address. This field is required for all path traces. | | `sourceMacAddress` | string | No | The MAC
        address of the source device in XX:XX:XX:XX:XX:XX format (e.g., 00:1A:2B:3C:4D:5E). It is required in
        case of overlapping IPs. | | `destinationMacAddress` | string | No | The MAC address of the destination
        device in XX:XX:XX:XX:XX:XX format (e.g., AA:BB:CC:DD:EE:FF). It is required in case of overlapping IPs.
        | | `sourcePort` | string | No | The source port for the traffic flow, ranging from 1 to 65535. Useful
        for path traces involving specific application traffic. | | `destinationPort` | string | No | The
        destination port for the traffic flow, ranging from 1 to 65535. Useful for path traces involving
        specific application traffic or services. | | `protocol` | string | No | The transport protocol to use
        for the path trace. Valid values are "TCP" or "UDP". If not specified, both protocols will be checked. |
        | `controlPath` | boolean | No | Indicates whether to trace the control plane path (true) or the data
        plane path (false). Control plane traces follow routing protocol decisions, while data plane traces
        follow forwarding decisions. Default is false. | | `periodicRefresh` | boolean | No | Specifies whether
        the path trace should be refreshed periodically (true) or performed once (false). When set to true, the
        path trace is refreshed every 30 seconds. Default is false. If enabled, the status will only show
        INPROGRESS the first time around. During subsequent calls, it will show the last status received.
        **NOTE: The refresh only occurs a maximum of 30 times** | | `inclusions` | array | No | Additional data
        to include in the path trace results. Array may include any of the following values: "INTERFACE_STATS":
        Include interface statistics (throughput, utilization) "QOS_STATS": Include Quality of Service
        statistics "DEVICE_STATS": Include device statistics (CPU, memory) "PERFORMANCE_STATS": Include
        performance statistics "ACL_TRACE": Include Access Control List trace information |  ### Usage Examples
        #### Basic Path Trace ```json {   "sourceIpAddress": "10.1.15.10",   "destinationIpAddress":
        "10.1.25.10",   "protocol": "TCP" } ```  #### Detailed Path Trace with Statistics ```json {
        "sourceIpAddress": "10.1.15.10",   "destinationIpAddress": "10.1.25.10",   "sourceMacAddress":
        "00:1A:2B:3C:4D:5E",   "destinationMacAddress": "AA:BB:CC:DD:EE:FF",   "sourcePort": "443",
        "destinationPort": "8080",   "protocol": "TCP",   "periodicRefresh": true,   "inclusions":
        ["INTERFACE_STATS", "DEVICE_STATS", "ACL_TRACE"] } ```  #### Control Plane Path Trace ```json {
        "sourceIpAddress": "10.1.15.10",   "destinationIpAddress": "10.1.25.10",   "controlPath": true } ```
        #### Path Trace with IPV6 ```json {   "sourceIpAddress": "2001:db8::1",   "destinationIpAddress":
        "2001:db8::2",   "protocol": "TCP" } ```.

        Args:
            controlPath(boolean): Path Trace's Indicates whether to perform control path tracing. Control path
                traces follow routing table decisions rather than data path forwarding decisions.  |
                Value | Description | | ----| ----------| | true  | Trace control path | | false | Trace
                data path (default) | .
            destinationIpAddress(string): Path Trace's Destination IP address for the path trace. Format can be IPv4
                (e.g., 192.168.1.1) or IPv6. .
            destinationMacAddress(string): Path Trace's Destination MAC address for the path trace. Format should be
                XX:XX:XX:XX:XX:XX (e.g., 00:1A:2B:3C:4D:5E). .
            destinationPort(string): Path Trace's Destination port for the path trace. Must be between 1-65535. .
            inclusions(list): Path Trace's Additional data to include in the path trace results.  | Value |
                Description | | ----| ----------| | INTERFACE_STATS | Include interface statistics
                (throughput, utilization) | | QOS_STATS | Include Quality of Service statistics | |
                DEVICE_STATS | Include device statistics (CPU, memory) | | PERFORMANCE_STATS | Include
                performance statistics | | ACL_TRACE | Include Access Control List trace information |
                (list of strings).
            periodicRefresh(boolean): Path Trace's Indicates whether to periodically refresh the path trace.  |
                Value | Description | | ----| ----------| | true  | Refresh the path trace every 30
                seconds | | false | Perform the path trace once (default) | .
            protocol(string): Path Trace's Network protocol to use for the path trace.  | Value | Description | |
                ----| ----------| | TCP   | Transmission Control Protocol | | UDP   | User Datagram
                Protocol | | (blank) | Check both TCP and UDP | .
            sourceIpAddress(string): Path Trace's Source IP address for the path trace. Format can be IPv4 (e.g.,
                192.168.1.1) or IPv6. .
            sourceMacAddress(string): Path Trace's Source MAC address for the path trace. Format should be
                XX:XX:XX:XX:XX:XX (e.g., 00:1A:2B:3C:4D:5E). .
            sourcePort(string): Path Trace's Source port for the path trace. Must be between 1-65535. .
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
            https://developer.cisco.com/docs/dna-center/#!initiate-a-new-path-trace
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
            "controlPath": controlPath,
            "destinationIpAddress": destinationIpAddress,
            "destinationPort": destinationPort,
            "destinationMacAddress": destinationMacAddress,
            "inclusions": inclusions,
            "periodicRefresh": periodicRefresh,
            "protocol": protocol,
            "sourceIpAddress": sourceIpAddress,
            "sourcePort": sourcePort,
            "sourceMacAddress": sourceMacAddress,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_aface7a4f75552cc9e167e2126979261_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/pathTraces"
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
            "bpm_aface7a4f75552cc9e167e2126979261_v3_2_3_0", json_data
        )

    def retrieves_previous_pathtrace(
        self, flow_analysis_id, headers=None, **request_parameters
    ):
        """Returns result of a previously requested flow analysis by its Flow Analysis id.  Deprecated since CatC-3.2.1.
        Please use this instead: GET /dna/intent/api/v1/pathTraces/{id}/result.

        Args:
            flow_analysis_id(str): flowAnalysisId path parameter. Flow analysis request id.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-previous-pathtrace
        """
        check_type(headers, dict)
        check_type(flow_analysis_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "flowAnalysisId": flow_analysis_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/flow-analysis/{flowAnalysisId}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ed5cbafc332a5efa97547736ba8b6044_v3_2_3_0", json_data
        )

    def deletes_pathtrace_by_id(
        self, flow_analysis_id, headers=None, **request_parameters
    ):
        """Deletes a flow analysis request by its id.  Deprecated since CatC-3.2.1. Please use this instead: DELETE
        /dna/intent/api/v1/pathTraces/{id}.

        Args:
            flow_analysis_id(str): flowAnalysisId path parameter. Flow analysis request id.
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
            https://developer.cisco.com/docs/dna-center/#!deletes-pathtrace-by-id
        """
        check_type(headers, dict)
        check_type(flow_analysis_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "flowAnalysisId": flow_analysis_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/flow-analysis/{flowAnalysisId}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a7ae984f943507ba621abe155e6e744_v3_2_3_0", json_data
        )
