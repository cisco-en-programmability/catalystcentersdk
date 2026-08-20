"""Cisco Catalyst Center Applications API wrapper.

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


class Applications:
    """Cisco Catalyst Center Applications API (version: 3.2.3.0).

    Wraps the Catalyst Center Applications
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Applications
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

    def retrieves_the_list_of_network_applications_along_with_experience_and_health_metrics(
        self,
        site_id,
        application_name=None,
        attribute=None,
        business_relevance=None,
        end_time=None,
        exporter_network_device_id=None,
        health_score=None,
        limit=None,
        offset=None,
        order=None,
        sort_by=None,
        ssid=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the list of network applications along with experience and health metrics. If startTime and endTime
        are not provided, the API defaults to the last 24 hours. `siteId` is mandatory. `siteId` must be a site
        UUID of a building. For detailed information about the usage of the API, please refer to the Open API
        specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-NetworkApplications-1.0.2-resolved.yaml.

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            limit(int): limit query parameter. Maximum number of records to return.
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1. .
            sort_by(str): sortBy query parameter. A field within the response to sort by.
            order(str): order query parameter. The sort order of the field ascending or descending.
            site_id(str): siteId query parameter. The site UUID without the top level hierarchy. `siteId` is
                mandatory. `siteId` must be a site UUID of a building. (Ex."buildingUuid") Examples:
                `siteId=buildingUuid` (single siteId requested)
                `siteId=buildingUuid1&siteId=buildingUuid2` (multiple siteId requested).
            exporter_network_device_id(str): exporterNetworkDeviceId query parameter. Unique ID of the netflow
                exporter device. Examples:
                `exporterNetworkDeviceId=5b234dbc-583e-491b-bf1a-318bba6c017f` (single
                exporterNetworkDeviceId requested) `exporterNetworkDeviceId=5b234dbc-583e-491b-bf1a-
                318bba6c017f&exporterNetworkDeviceId=8b234dbc-583e-491b-bf1a-318bba6c017f` (multiple
                exporterNetworkDeviceId requested) .
            ssid(str): ssid query parameter. In the context of a network application, SSID refers to the name of the
                wireless network to which the client connects. Examples: `ssid=Alpha` (single ssid
                requested) `ssid=Alpha&ssid=Guest` (multiple ssid requested) .
            application_name(str): applicationName query parameter. Name of the application for which the experience
                data is intended. Examples: `applicationName=webex` (single applicationName requested)
                `applicationName=webex&applicationName=teams` (multiple applicationName requested) .
            business_relevance(str): businessRelevance query parameter. The application can be chosen to be
                categorized as business-relevant, irrelevant, or default (neutral). By doing so, the
                assurance application prioritizes the monitoring and analysis of business-relevant data,
                ensuring critical insights are captured. Applications marked as irrelevant or default
                are selectively excluded from certain data sets, streamlining focus on what's most
                important for business outcomes. .
            health_score(int): healthScore query parameter. Application health score. Examples: `healthScore=7`
                (single healthScore requested) `healthScore=7&healthScore=3` (multiple healthScore
                requested) .
            attribute(str): attribute query parameter. List of attributes related to resource that can be requested
                to only be part of the response along with the required attributes. Supported attributes
                are applicationName, siteId, exporterIpAddress, exporterNetworkDeviceId, healthScore,
                businessRelevance, usage, throughput, packetLossPercent, networkLatency,
                applicationServerLatency, clientNetworkLatency, serverNetworkLatency, trafficClass,
                jitter, ssid Examples: `attribute=healthScore` (single attribute requested)
                `attribute=healthScore&attribute=ssid&attribute=jitter` (multiple attribute requested).
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-network-applications-along-with-experience-and-health-metrics
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(limit, int)
        check_type(offset, int)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(site_id, str, may_be_none=False)
        check_type(exporter_network_device_id, str)
        check_type(ssid, str)
        check_type(application_name, str)
        check_type(business_relevance, str)
        check_type(health_score, int)
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
            "siteId": site_id,
            "exporterNetworkDeviceId": exporter_network_device_id,
            "ssid": ssid,
            "applicationName": application_name,
            "businessRelevance": business_relevance,
            "healthScore": health_score,
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

        e_url = "/dna/data/api/v1/networkApplications"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fb02436a6c935d5d8a536b86de8b2846_v3_2_3_0", json_data
        )

    def the_trend_analytics_data_for_thousand_eyes_test_results_in_the_specified_time_range(
        self,
        agent_id=None,
        attribute=None,
        end_time=None,
        limit=None,
        network_device_name=None,
        offset=None,
        order=None,
        site_id=None,
        start_time=None,
        test_id=None,
        test_name=None,
        test_type=None,
        trend_interval=None,
        headers=None,
        **request_parameters
    ):
        """Get trend time series for ThousandEyes test results.  The data will be grouped based on the specified trend time
        interval. If `startTime` and `endTime` are not provided, the API defaults to the last 24 hours.  By
        default the number of records returned will be 100 and the records will be sorted by time in ascending
        (`asc`) order .  For detailed information about the usage of the API, please refer to the Open API
        specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-thousandEyesTestResults-1.0.1-resolved.yaml.

        Args:
            site_id(str): siteId query parameter. The site UUID without the top level hierarchy. `siteId` must be a
                site UUID of a building. The list of buildings can be fetched using API `GET
                /dna/intent/api/v1/sites?type=building`. Examples: `siteId=buildingUuid` (single siteId
                requested) `siteId=buildingUuid1&siteId=buildingUuid2` (multiple siteId requested) .
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            trend_interval(str): trendInterval query parameter. The time interval to aggregate the metrics.
                Available values : 5MIN, 30MIN, 1HR, 3HR  Recommendation: (Time duration: Recommended
                `trendInterval`),  (Up to 6 hr: `5MIN`),  (6 hr to 2 days: `1HR`),  (More than 2 days:
                `3HR`),  .
            attribute(str): attribute query parameter. List of attributes related to resource that can be requested
                to only be part of the response. Supported attributes are failurePercentage,
                averagePacketLoss, latestPacketLoss, maxPacketLoss, averageJitter, latestJitter,
                maxJitter, averageLatency, latestLatency, maxLatency Examples:
                attribute=failurePercentage (single attribute requested)
                attribute=failurePercentage&attribute=maxLatency (multiple attribute requested).
            test_id(str): testId query parameter. Unique identifier of the ThousandEyes test. Examples:
                `testId=2043918` (filter for single testId) `testId=2043918&testId=129440` (filter for
                multiple testIds) .
            test_name(str): testName query parameter. Name of the ThousandEyes test. This supports `*` wildcard, and
                filtering is case-insensitve. Examples: `testName=Cisco Webex` (exact match)
                `testName=Microsoft*` (starts with given string) .
            test_type(str): testType query parameter. Type of the ThousandEyes test. Please note that Catalyst
                Center supports only a subset of all possible ThousandEyes test types. .
            agent_id(str): agentId query parameter. Unique identifier of the ThousandEyes agent. Examples:
                `agentId=199345` (filter for single agentId) `agentId=1993458&agentId=499387` (filter
                for multiple agentIds) .
            network_device_name(str): networkDeviceName query parameter. Name of the network device as per the
                inventory. This supports `*` wildcard, and filtering is case-insensitve. .
            limit(int): limit query parameter. Maximum number of records to return.
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1.
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
            https://developer.cisco.com/docs/dna-center/#!the-trend-analytics-data-for-thousand-eyes-test-results-in-the-specified-time-range
        """
        check_type(headers, dict)
        check_type(site_id, str)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(trend_interval, str)
        check_type(attribute, str)
        check_type(test_id, str)
        check_type(test_name, str)
        check_type(test_type, str)
        check_type(agent_id, str)
        check_type(network_device_name, str)
        check_type(limit, int)
        check_type(offset, int)
        check_type(order, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "siteId": site_id,
            "startTime": start_time,
            "endTime": end_time,
            "trendInterval": trend_interval,
            "attribute": attribute,
            "testId": test_id,
            "testName": test_name,
            "testType": test_type,
            "agentId": agent_id,
            "networkDeviceName": network_device_name,
            "limit": limit,
            "offset": offset,
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

        e_url = "/dna/data/api/v1/thousandEyesTestResults/trendAnalytics"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_af0e7bab8659f19c619fae31772d15_v3_2_3_0", json_data
        )

    def retrieves_the_list_of_thousand_eyes_test_results_along_with_related_metrics(
        self,
        agent_id=None,
        attribute=None,
        end_time=None,
        limit=None,
        network_device_name=None,
        offset=None,
        order=None,
        site_id=None,
        sort_by=None,
        start_time=None,
        test_id=None,
        test_name=None,
        test_type=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the list of ThousandEyes test results along with related metrics. If `startTime` and `endTime` are not
        provided, the API defaults to the last 24 hours.  Please note that `siteId` filter (if used) should be
        using only site UUIDs of buildings.   For detailed information about the usage of the API, please refer
        to the Open API specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-thousandEyesTestResults-1.0.1-resolved.yaml.

        Args:
            site_id(str): siteId query parameter. The site UUID without the top level hierarchy. `siteId` must be a
                site UUID of a building. The list of buildings can be fetched using API `GET
                /dna/intent/api/v1/sites?type=building`. Examples: `siteId=buildingUuid` (single siteId
                requested) `siteId=buildingUuid1&siteId=buildingUuid2` (multiple siteId requested) .
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            test_id(str): testId query parameter. Unique identifier of the ThousandEyes test. Examples:
                `testId=2043918` (filter for single testId) `testId=2043918&testId=129440` (filter for
                multiple testIds) .
            test_name(str): testName query parameter. Name of the ThousandEyes test. This supports `*` wildcard, and
                filtering is case-insensitve. Examples: `testName=Cisco Webex` (exact match)
                `testName=Microsoft*` (starts with given string) .
            test_type(str): testType query parameter. Type of the ThousandEyes test. Please note that Catalyst
                Center supports only a subset of all possible ThousandEyes test types. .
            agent_id(str): agentId query parameter. Unique identifier of the ThousandEyes agent. Examples:
                `agentId=199345` (filter for single agentId) `agentId=1993458&agentId=499387` (filter
                for multiple agentIds) .
            network_device_name(str): networkDeviceName query parameter. Name of the network device as per the
                inventory. This supports `*` wildcard, and filtering is case-insensitve. .
            attribute(str): attribute query parameter. List of attributes related to resource that can be requested
                to only be part of the response along with the required attributes. Examples:
                `attribute=testName` (single attribute requested)
                `attribute=testId&attribute=testName&attribute=averageLatency` (multiple attributes
                requested) . For valid attributes, verify the documentation.
            limit(int): limit query parameter. Maximum number of records to return.
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1.
            sort_by(str): sortBy query parameter. Attribute name by which the results should be sorted.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-thousand-eyes-test-results-along-with-related-metrics
        """
        check_type(headers, dict)
        check_type(site_id, str)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(test_id, str)
        check_type(test_name, str)
        check_type(test_type, str)
        check_type(agent_id, str)
        check_type(network_device_name, str)
        check_type(attribute, str)
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
            "siteId": site_id,
            "startTime": start_time,
            "endTime": end_time,
            "testId": test_id,
            "testName": test_name,
            "testType": test_type,
            "agentId": agent_id,
            "networkDeviceName": network_device_name,
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

        e_url = "/dna/data/api/v1/thousandEyesTestResults"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a499ab977fea5c139c9344227c7769a5_v3_2_3_0", json_data
        )

    def retrieves_the_total_count_of_thousand_eyes_test_results(
        self,
        agent_id=None,
        end_time=None,
        network_device_name=None,
        site_id=None,
        start_time=None,
        test_id=None,
        test_name=None,
        test_type=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the total count of ThousandEyes test results for the given filters. If `startTime` and `endTime` are
        not provided, the API defaults to the last 24 hours.  For detailed information about the usage of the
        API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        thousandEyesTestResults-1.0.1-resolved.yaml.

        Args:
            site_id(str): siteId query parameter. The site UUID without the top level hierarchy. `siteId` must be a
                site UUID of a building. The list of buildings can be fetched using API `GET
                /dna/intent/api/v1/sites?type=building`. Examples: `siteId=buildingUuid` (single siteId
                requested) `siteId=buildingUuid1&siteId=buildingUuid2` (multiple siteId requested) .
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            test_id(str): testId query parameter. Unique identifier of the ThousandEyes test. Examples:
                `testId=2043918` (filter for single testId) `testId=2043918&testId=129440` (filter for
                multiple testIds) .
            test_name(str): testName query parameter. Name of the ThousandEyes test. This supports `*` wildcard, and
                filtering is case-insensitve. Examples: `testName=Cisco Webex` (exact match)
                `testName=Microsoft*` (starts with given string) .
            test_type(str): testType query parameter. Type of the ThousandEyes test. Please note that Catalyst
                Center supports only a subset of all possible ThousandEyes test types. .
            agent_id(str): agentId query parameter. Unique identifier of the ThousandEyes agent. Examples:
                `agentId=199345` (filter for single agentId) `agentId=1993458&agentId=499387` (filter
                for multiple agentIds) .
            network_device_name(str): networkDeviceName query parameter. Name of the network device as per the
                inventory. This supports `*` wildcard, and filtering is case-insensitve. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-total-count-of-thousand-eyes-test-results
        """
        check_type(headers, dict)
        check_type(site_id, str)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(test_id, str)
        check_type(test_name, str)
        check_type(test_type, str)
        check_type(agent_id, str)
        check_type(network_device_name, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "siteId": site_id,
            "startTime": start_time,
            "endTime": end_time,
            "testId": test_id,
            "testName": test_name,
            "testType": test_type,
            "agentId": agent_id,
            "networkDeviceName": network_device_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/thousandEyesTestResults/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ef366ca484355d15937dd851a67c88e3_v3_2_3_0", json_data
        )

    def retrieves_the_total_count_of_network_applications_by_applying_basic_filtering(
        self,
        site_id,
        application_name=None,
        business_relevance=None,
        end_time=None,
        exporter_network_device_id=None,
        health_score=None,
        ssid=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the number of network applications by applying basic filtering. If startTime and endTime are not
        provided, the API defaults to the last 24 hours. `siteId` is mandatory. `siteId` must be a site UUID of
        a building. For detailed information about the usage of the API, please refer to the Open API
        specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-NetworkApplications-1.0.2-resolved.yaml.

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            site_id(str): siteId query parameter. The site UUID without the top level hierarchy. `siteId` is
                mandatory. `siteId` must be a site UUID of a building. (Ex."buildingUuid") Examples:
                `siteId=buildingUuid` (single siteId requested)
                `siteId=buildingUuid1&siteId=buildingUuid2` (multiple siteId requested).
            exporter_network_device_id(str): exporterNetworkDeviceId query parameter. Unique ID of the netflow
                exporter device. Examples:
                `exporterNetworkDeviceId=5b234dbc-583e-491b-bf1a-318bba6c017f` (single
                exporterNetworkDeviceId requested) `exporterNetworkDeviceId=5b234dbc-583e-491b-bf1a-
                318bba6c017f&exporterNetworkDeviceId=8b234dbc-583e-491b-bf1a-318bba6c017f` (multiple
                exporterNetworkDeviceId requested) .
            ssid(str): ssid query parameter. In the context of a network application, SSID refers to the name of the
                wireless network to which the client connects. Examples: `ssid=Alpha` (single ssid
                requested) `ssid=Alpha&ssid=Guest` (multiple ssid requested) .
            application_name(str): applicationName query parameter. Name of the application for which the experience
                data is intended. Examples: `applicationName=webex` (single applicationName requested)
                `applicationName=webex&applicationName=teams` (multiple applicationName requested) .
            business_relevance(str): businessRelevance query parameter. The application can be chosen to be
                categorized as business-relevant, irrelevant, or default (neutral). By doing so, the
                assurance application prioritizes the monitoring and analysis of business-relevant data,
                ensuring critical insights are captured. Applications marked as irrelevant or default
                are selectively excluded from certain data sets, streamlining focus on what's most
                important for business outcomes. .
            health_score(int): healthScore query parameter. Application health score. Examples: `healthScore=7`
                (single healthScore requested) `healthScore=7&healthScore=3` (multiple healthScore
                requested) .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-total-count-of-network-applications-by-applying-basic-filtering
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(site_id, str, may_be_none=False)
        check_type(exporter_network_device_id, str)
        check_type(ssid, str)
        check_type(application_name, str)
        check_type(business_relevance, str)
        check_type(health_score, int)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "siteId": site_id,
            "exporterNetworkDeviceId": exporter_network_device_id,
            "ssid": ssid,
            "applicationName": application_name,
            "businessRelevance": business_relevance,
            "healthScore": health_score,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/networkApplications/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c50def6b3a58e5acab3ae592a57da8_v3_2_3_0", json_data
        )

    def retrieves_summary_analytics_data_related_to_network_applications_along_with_health_metrics(
        self,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        page=None,
        siteIds=None,
        startTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Retrieves summary analytics data related to network applications while applying complex filtering, aggregate
        functions, and grouping.  This API facilitates obtaining consolidated insights into the performance and
        status of the network applications. If startTime and endTime are not provided, the API defaults to the
        last 24 hours. For detailed information about the usage of the API, please refer to the Open API
        specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-NetworkApplications-1.0.2-resolved.yaml.    The input
        payload contains the following fields,         Field Name   Description           startTime   The start
        time indicates when the API begins retrieving data related to the resource. It must be specified in the
        UNIX epoch time format, measured in milliseconds. This value is inclusive, and if left unspecified, the
        default is 1 day before the endTime.       endTime   The end time indicates the upper limit until which
        the API retrieves data related to the resource. It must be defined in the UNIX epoch time format,
        measured in milliseconds. This value is inclusive, and if left unspecified, the default is the latest
        available data.       siteIds   The list of site UUIDs. This is a mandatory field. Please note that only
        Building UUIDs are allowed for this field. This is a mandatory field.       groupBy   Specifies the
        attributes for grouping the data. Refer to  NetworkApplicationGroupByField  model for the supported
        grouping attributes       attributes   A list of attributes associated with the resource, which can be
        requested to be included in the response alongside the required attributes. Refer to
        NetworkApplicationSummaryAttributes  model for the supported attributes       aggregateAttributes   This
        specifies the attribute name and the function to be applied during data querying. The aggregate function
        is then applied to data within the specified start and end times. Refer to
        NetworkApplicationAggregateField  model for the supported aggregate attributes       filters   This is
        used to specify one or more conditions for filtering the queried data. Refer to
        NetworkApplicationFilterField  model for the supported filters       page   It includes the  limit,
        cursor, and sortBy  fields.  limit  denotes the number of records to retrieve per page,  cursor
        signifies the initial data position, and  sortBy  is used to sort the response based on the sortBy
        fields. It contains the attribute name, order, and optional function for sorting by the aggregated
        field. Refer to  NetworkApplicationSortByObj  model for the supported sortBy names. Default page limit
        is 100 and sortBy is applicationName      .

        Args:
            aggregateAttributes(list): Applications's aggregateAttributes (list of objects).
            attributes(list): Applications's attributes (list of strings).
            endTime(integer): Applications's endTime.
            filters(list): Applications's filters (list of objects).
            page(object): Applications's page.
            siteIds(list): Applications's siteIds (list of strings).
            startTime(integer): Applications's startTime.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-summary-analytics-data-related-to-network-applications-along-with-health-metrics
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
            "siteIds": siteIds,
            "attributes": attributes,
            "filters": filters,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ded95db0af275081801b54e0ce105c71_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/networkApplications/summaryAnalytics"
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
            "bpm_ded95db0af275081801b54e0ce105c71_v3_2_3_0", json_data
        )

    def retrieves_the_trend_analytics_data_related_to_network_applications(
        self,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        page=None,
        siteIds=None,
        startTime=None,
        trendInterval=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Retrieves the trend analytics of applications experience data for the specified time range. The data will be
        grouped based on the given trend time interval. This API facilitates obtaining consolidated insights
        into the performance and status of the network applications over the specified start and end time. If
        startTime and endTime are not provided, the API defaults to the last 24 hours. `siteId` and
        `trendInterval` are mandatory. `siteId` must be a site UUID of a building. For detailed information
        about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-NetworkApplications-1.0.2-resolved.yaml.  The input payload
        contains the following fields,         Field Name   Description           startTime   The start time
        indicates when the API begins retrieving data related to the resource. It must be specified in the UNIX
        epoch time format, measured in milliseconds. This value is inclusive, and if left unspecified, the
        default is 1 day before the endTime.       endTime   The end time indicates the upper limit until which
        the API retrieves data related to the resource. It must be defined in the UNIX epoch time format,
        measured in milliseconds. This value is inclusive, and if left unspecified, the default is the latest
        available data.       siteIds   The list of Building UUID. This is a mandatory field.
        trendInterval   The time window for aggregating metrics. This is a mandatory request field. Possible
        values include *5 minutes, 10 minutes, 1 hour or 3 hour. Upto 3 hours time window allowed intervals 5MIN
        and 10MIN and more than 3 hours time window allowed intervals 1HR and 3HR .       groupBy   Specifies
        the attributes for grouping the data. Refer to  NetworkApplicationGroupByField  model for the supported
        grouping attributes       attributes   A list of attributes associated with the resource, which can be
        requested to be included in the response alongside the required attributes. Refer to
        NetworkApplicationTrendAttribute  model for the supported attributes       aggregateAttributes   This
        specifies the attribute name and the function to be applied during data querying. The aggregate function
        is then applied to data within the specified start and end times. Refer to
        NetworkApplicationAggregateField  model for the supported aggregate attributes       filters   This is
        used to specify one or more conditions for filtering the queried data. Refer to
        NetworkApplicationFilterField  model for the supported filters       page   It includes the  limit,
        cursor, and timeSortOrder  fields.  limit  denotes the number of records to retrieve per page,  cursor
        signifies the initial data position, and  timeSortOrder  is used sort the response based on the
        timestamp either in ascending or descending order. Default page limit is 100 and order is asc      .

        Args:
            aggregateAttributes(list): Applications's aggregateAttributes (list of objects).
            attributes(list): Applications's attributes (list of strings).
            endTime(integer): Applications's endTime.
            filters(list): Applications's filters (list of objects).
            groupBy(list): Applications's groupBy (list of strings).
            page(object): Applications's page.
            siteIds(list): Applications's siteIds (list of strings).
            startTime(integer): Applications's startTime.
            trendInterval(string): Applications's trendInterval.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-trend-analytics-data-related-to-network-applications
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
            "siteIds": siteIds,
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
            self._request_validator("jsd_6ce35f19bc4c1d058aa01536_v3_2_3_0").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/networkApplications/trendAnalytics"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory("bpm_6ce35f19bc4c1d058aa01536_v3_2_3_0", json_data)

    def retrieves_the_list_of_clients_metrics_for_the_given_application(
        self,
        id,
        site_id,
        attribute=None,
        end_time=None,
        exporter_network_device_id=None,
        limit=None,
        offset=None,
        order=None,
        sort_by=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the list of clients metrics for the given application. If startTime and endTime are not provided, the
        API defaults to the last 24 hours. `siteId` is mandatory. `siteId` must be a site UUID of a building.
        For the given time range and filters, the API will get the list of unique clients which matched the
        filter criteria. For detailed information about the usage of the API, please refer to the Open API
        specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-NetworkApplications-1.0.2-resolved.yaml.

        Args:
            id(str): id path parameter. id is the network application name. .
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            site_id(str): siteId query parameter. The site UUID without the top level hierarchy.`siteId` is
                mandatory. `siteId` must be a site UUID of a building. (Ex."buildingUuid") Examples:
                `siteId=buildingUuid` (single siteId requested)
                `siteId=buildingUuid1&siteId=buildingUuid2` (multiple siteId requested).
            exporter_network_device_id(str): exporterNetworkDeviceId query parameter. Unique ID of the netflow
                exporter device. Examples:
                `exporterNetworkDeviceId=5b234dbc-583e-491b-bf1a-318bba6c017f` (single
                exporterNetworkDeviceId requested) `exporterNetworkDeviceId=5b234dbc-583e-491b-bf1a-
                318bba6c017f&exporterNetworkDeviceId=8b234dbc-583e-491b-bf1a-318bba6c017f` (multiple
                exporterNetworkDeviceId requested) .
            attribute(str): attribute query parameter. List of attributes related to resource that can be requested
                to only be part of the response along with the required attributes. Supported attributes
                are id, name, ipAddress,osType, usage, siteName, macAddress, type, appHealthScore,
                clientHealthScore, exporterNetworkDeviceId, siteId,connectedNetworkDeviceName,
                connectedNetworkDeviceId, vlanId Examples: `attribute=name` (single attribute requested)
                `attribute=name&attribute=macAddress` (multiple attribute requested).
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-clients-metrics-for-the-given-application
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(site_id, str, may_be_none=False)
        check_type(exporter_network_device_id, str)
        check_type(attribute, str)
        check_type(limit, int)
        check_type(offset, int)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "siteId": site_id,
            "exporterNetworkDeviceId": exporter_network_device_id,
            "attribute": attribute,
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

        e_url = "/dna/data/api/v1/networkApplications/{id}/clients"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a8102ea97535f25b4919d714a3af5d3_v3_2_3_0", json_data
        )

    def bulk_update_application_health_score_definitions(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Caller ID is used to trace the origin of API calls and their associated queries executed on the database. It's
        an optional header parameter that can be added to an API request.  For detailed information about the
        usage of the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        ApplicationHealthScoreDefinitions-1.0.0-resolved.yaml.

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
            https://developer.cisco.com/docs/dna-center/#!bulk-update-application-health-score-definitions
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
                "jsd_cfff77e00e75fc6a3970bf71bf9e0b8_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/applicationHealthScoreDefinitions/bul" + "kUpdate"
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
            "bpm_cfff77e00e75fc6a3970bf71bf9e0b8_v3_2_3_0", json_data
        )

    def update_application_health_score_definition_for_the_given_id(
        self,
        id,
        badDefaultValue=None,
        badMaxValue=None,
        badMinValue=None,
        badValue=None,
        definitionType=None,
        goodDefaultValue=None,
        goodMaxValue=None,
        goodMinValue=None,
        goodValue=None,
        greatDefaultValue=None,
        greatMaxValue=None,
        greatMinValue=None,
        greatValue=None,
        includeForHealthScore=None,
        includeForHealthScoreDefault=None,
        kpiName=None,
        lastModified=None,
        poorDefaultValue=None,
        poorMaxValue=None,
        poorMinValue=None,
        poorValue=None,
        trafficClass=None,
        unit=None,
        weightDefaultValue=None,
        weightValue=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Update application health score definition for the given id.  For detailed information about the usage of the
        API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        ApplicationHealthScoreDefinitions-1.0.0-resolved.yaml.

        Args:
            badDefaultValue(number): Applications's The default upper threshold value of the KPI for poor (1-3)
                health score. .
            badMaxValue(number): Applications's Maximum value allowed for upper threshold value of the KPI for poor
                (1-3) health score. .
            badMinValue(number): Applications's Minimum value allowed for upper threshold value of the KPI for poor
                (1-3) health score. .
            badValue(number): Applications's The upper threshold value of the KPI for poor (1-3) health score. .
            definitionType(string): Applications's Definition type to indicate whether the health score definition
                has been customized or not.. Available values are 'CUSTOM' and 'DEFAULT'.
            goodDefaultValue(number): Applications's The default lower threshold value of the KPI for fair (4-7)
                health score. .
            goodMaxValue(number): Applications's Maximum value allowed for lower threshold value of the KPI for fair
                (4-7) health score. .
            goodMinValue(number): Applications's Minimum value allowed for lower threshold value of the KPI for fair
                (4-7) health score. .
            goodValue(number): Applications's The lower threshold value of the KPI for fair (4-7) health score. This
                would be same as the upper threshold value of the KPI for good (8-10) health score. .
            greatDefaultValue(number): Applications's The default lower threshold value of the KPI for good (8-10)
                health score. .
            greatMaxValue(number): Applications's Maximum value allowed for the lower threshold value of the KPI for
                good (8-10) health score. .
            greatMinValue(number): Applications's Minimum value allowed for the lower threshold value of the KPI for
                good (8-10) health score. .
            greatValue(number): Applications's The lower threshold value of the KPI for good (8-10) health score. .
            id(string): Applications's Application health score definition id.
            includeForHealthScore(boolean): Applications's Flag to indicate whether the KPI is included for the
                application health score calulation or not. .
            includeForHealthScoreDefault(boolean): Applications's Default flag to indicate whether the KPI is
                included for application health calulation or not.  .
            kpiName(string): Applications's Application health KPI name.. Available values are 'packetLoss',
                'jitter', 'latency' and 'appDelay'.
            lastModified(integer): Applications's Last modification time in milliseconds since UNIX epoch. This is
                applicable only for modified thresholds. .
            poorDefaultValue(number): Applications's The default lower threshold value of the KPI for poor (1-3)
                health score. .
            poorMaxValue(number): Applications's Maximum value allowed for lower threshold value of the KPI for poor
                (1-3) health score. .
            poorMinValue(number): Applications's Minimum value allowed for lower threshold value of the KPI for poor
                (1-3) health score. .
            poorValue(number): Applications's The lower threshold value of the KPI for poor (1-3) health score. This
                would be same as the upper threshold value of the KPI for fair (4-7) health score. .
            trafficClass(string): Applications's Traffic class for application health score definition.. Available
                values are 'voip-telephony', 'multimedia-conferencing', 'multimedia-streaming', 'real-
                time-interactive', 'broadcast-video', 'signaling', 'network-control', 'ops-admin-mgmt',
                'transactional-data' and 'bulk-data'.
            unit(string): Applications's Application Health score definition unit.. Available values are 'sec',
                'msec' and 'percent'.
            weightDefaultValue(integer): Applications's The default weightage of the KPI used for application health
                score calculation. .
            weightValue(integer): Applications's The weightage of the KPI used for application health score
                calculation. .
            id(str): id path parameter. Application health score definition id.
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
            https://developer.cisco.com/docs/dna-center/#!update-application-health-score-definition-for-the-given-id
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
            "id": id,
            "kpiName": kpiName,
            "trafficClass": trafficClass,
            "includeForHealthScore": includeForHealthScore,
            "includeForHealthScoreDefault": includeForHealthScoreDefault,
            "definitionType": definitionType,
            "unit": unit,
            "weightValue": weightValue,
            "weightDefaultValue": weightDefaultValue,
            "badValue": badValue,
            "badDefaultValue": badDefaultValue,
            "badMinValue": badMinValue,
            "badMaxValue": badMaxValue,
            "poorValue": poorValue,
            "poorDefaultValue": poorDefaultValue,
            "poorMinValue": poorMinValue,
            "poorMaxValue": poorMaxValue,
            "goodValue": goodValue,
            "goodDefaultValue": goodDefaultValue,
            "goodMinValue": goodMinValue,
            "goodMaxValue": goodMaxValue,
            "greatValue": greatValue,
            "greatDefaultValue": greatDefaultValue,
            "greatMinValue": greatMinValue,
            "greatMaxValue": greatMaxValue,
            "lastModified": lastModified,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a776c50bb5fb397e47d3e5f63a371_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/applicationHealthScoreDefinitions/{id" + "}"
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
            "bpm_a776c50bb5fb397e47d3e5f63a371_v3_2_3_0", json_data
        )

    def get_application_health_score_definition_for_the_given_id(
        self, id, attribute=None, headers=None, **request_parameters
    ):
        """Get application health score definition for the given id. By default all supported attributes are listed in the
        response.  For detailed information about the usage of the API, please refer to the Open API
        specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-ApplicationHealthScoreDefinitions-1.0.0-resolved.yaml.

        Args:
            id(str): id path parameter. Application health score definition id.
            attribute(str): attribute query parameter. These are the attributes supported in application health
                score definitions response. By default, all properties are sent in response. .
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
            https://developer.cisco.com/docs/dna-center/#!get-application-health-score-definition-for-the-given-id
        """
        check_type(headers, dict)
        check_type(attribute, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
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

        e_url = "/dna/intent/api/v1/applicationHealthScoreDefinitions/{id" + "}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b01c993595cb5d8e9cfc55b92f4dd7e7_v3_2_3_0", json_data
        )

    def counts_the_number_of_path_traces_for_the_given_thousand_eyes_test_result(
        self, id, client_mac_address=None, headers=None, **request_parameters
    ):
        """Retrieves the count of path traces for the given ThousandEyes test result.  For detailed information about the
        usage of the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        thousandEyesPathViz-1.0.0-resolved.yaml.

        Args:
            id(str): id path parameter. Unique identifier of the test result.
            client_mac_address(str): clientMacAddress query parameter. Optional client MAC address. If this is
                provided the the path trace would start from the given client, otherwise the path trace
                starts from the switch where ThousanEyes agent is running. .
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
            https://developer.cisco.com/docs/dna-center/#!counts-the-number-of-path-traces-for-the-given-thousand-eyes-test-result
        """
        check_type(headers, dict)
        check_type(client_mac_address, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "clientMacAddress": client_mac_address,
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

        e_url = "/dna/data/api/v1/thousandEyesTestResults/{id}/pathTraces" + "/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b73ac9ff65584bb0971d3e7d4d656_v3_2_3_0", json_data
        )

    def get_all_application_health_score_definitions(
        self,
        attribute=None,
        include_for_health_score=None,
        limit=None,
        offset=None,
        traffic_class=None,
        headers=None,
        **request_parameters
    ):
        """Get all application health score definitions for given filter.  By default all supported attributes are listed
        in the response.  Following diagram explains the various thresholds, and corresponding health score
        range:  ``` badThreshold            poorThreshold             goodThreshold            greatThreshold
        |-------------------------|-------------------------|-------------------------|             Poor (1-3)
        Fair (4-7)                Good (8-10) ```  Final health score is calcuated as follows: * For each KPI
        (e.g. jitter), KPI-specific health score is calculated using thresholds explained above. * Overall
        health score is derived by performing weighted average of all KPIs.  For detailed information about the
        usage of the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        ApplicationHealthScoreDefinitions-1.0.0-resolved.yaml.

        Args:
            traffic_class(str): trafficClass query parameter. The traffic class for the application health score
                definition. If this is not provided then all traffic class application health score
                definitions will be included.
            include_for_health_score(bool): includeForHealthScore query parameter. The inclusion of application
                health score definition, either true or false. true indicates that particular
                application health metric is included in in the application health score computation,
                otherwise false.
            attribute(str): attribute query parameter. These are the attributes supported in application health
                score definitions response. By default, all properties are sent in response. .
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
            https://developer.cisco.com/docs/dna-center/#!get-all-application-health-score-definitions
        """
        check_type(headers, dict)
        check_type(traffic_class, str)
        check_type(include_for_health_score, bool)
        check_type(attribute, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "trafficClass": traffic_class,
            "includeForHealthScore": include_for_health_score,
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

        e_url = "/dna/intent/api/v1/applicationHealthScoreDefinitions"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ac6832a5e6790991958bedebcd4_v3_2_3_0", json_data
        )

    def get_the_count_of_application_health_score_definitions(
        self,
        include_for_health_score=None,
        traffic_class=None,
        headers=None,
        **request_parameters
    ):
        """Get the count of application health score definitions based on provided filters.  For detailed information about
        the usage of the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        ApplicationHealthScoreDefinitions-1.0.0-resolved.yaml.

        Args:
            traffic_class(str): trafficClass query parameter. The traffic class for the application health score
                definition. If this is not provided then all traffic class application health score
                definitions will be included.
            include_for_health_score(bool): includeForHealthScore query parameter. The inclusion of application
                health score definition, either true or false. true indicates that particular
                application health metric is included in in the application health score computation,
                otherwise false.
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
            https://developer.cisco.com/docs/dna-center/#!get-the-count-of-application-health-score-definitions
        """
        check_type(headers, dict)
        check_type(traffic_class, str)
        check_type(include_for_health_score, bool)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "trafficClass": traffic_class,
            "includeForHealthScore": include_for_health_score,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/applicationHealthScoreDefinitions/cou" + "nt"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f35518c9315f5a94872a8e062f717011_v3_2_3_0", json_data
        )

    def retrieves_the_trend_analytics_related_to_specific_network_application(
        self,
        id,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        page=None,
        siteIds=None,
        startTime=None,
        trendInterval=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Retrieves the trend analytics of applications experience data to specific network application for the specified
        time range. The data will be grouped based on the given trend time interval. This API facilitates
        obtaining consolidated insights into the performance and status of the network applications over the
        specified start and end time. If startTime and endTime are not provided, the API defaults to the last 24
        hours.`siteId` and `trendInterval` are mandatory. `siteId` must be a site UUID of a building.For
        detailed information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-NetworkApplications-1.0.2-resolved.yaml.    The input
        payload contains the following fields,         Field Name   Description           startTime   The start
        time indicates when the API begins retrieving data related to the resource. It must be specified in the
        UNIX epoch time format, measured in milliseconds. This value is inclusive, and if left unspecified, the
        default is 1 day before the endTime.       endTime   The end time indicates the upper limit until which
        the API retrieves data related to the resource. It must be defined in the UNIX epoch time format,
        measured in milliseconds. This value is inclusive, and if left unspecified, the default is the latest
        available data.       siteIds   The list of site UUIDs. This is a mandatory field. Please note that only
        Building UUIDs are allowed for this field.       trendInterval   The time window for aggregating
        metrics. This is a mandatory request field. Possible values include *5 minutes, 10 minutes, 1 hour or 3
        hour. Upto 1 day time window allowed intervals 5MIN and 10MIN and more than 1 day time window allowed
        intervals 1HR and 3HR .       groupBy   Specifies the attributes for grouping the data. Refer to
        NetworkApplicationGroupByField  model for the supported grouping attributes       attributes   A list of
        attributes associated with the resource, which can be requested to be included in the response alongside
        the required attributes. Refer to  NetworkApplicationTrendAttribute  model for the supported attributes
        aggregateAttributes   This specifies the attribute name and the function to be applied during data
        querying. The aggregate function is then applied to data within the specified start and end times. Refer
        to  NetworkApplicationAggregateField  model for the supported aggregate attributes       filters   This
        is used to specify one or more conditions for filtering the queried data. Refer to
        NetworkApplicationFilterField  model for the supported filters       page   It includes the  limit,
        cursor, and timeSortOrder  fields.  limit  denotes the number of records to retrieve per page,  cursor
        signifies the initial data position, and  timeSortOrder  is used sort the response based on the
        timestamp either in ascending or descending order. Default page limit is 100 and order is asc      .

        Args:
            aggregateAttributes(list): Applications's aggregateAttributes (list of objects).
            attributes(list): Applications's attributes (list of strings).
            endTime(integer): Applications's endTime.
            filters(list): Applications's filters (list of objects).
            page(object): Applications's page.
            siteIds(list): Applications's siteIds (list of strings).
            startTime(integer): Applications's startTime.
            trendInterval(string): Applications's trendInterval.
            id(str): id path parameter. id is the network application name. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-trend-analytics-related-to-specific-network-application
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
            "siteIds": siteIds,
            "trendInterval": trendInterval,
            "attributes": attributes,
            "filters": filters,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_b33956f3e56c6b8d234e7ed6a20e6_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/networkApplications/{id}/trendAnalytics"
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
            "bpm_b33956f3e56c6b8d234e7ed6a20e6_v3_2_3_0", json_data
        )

    def retrieves_the_list_of_path_traces_for_the_given_thousand_eyes_test_result(
        self, id, client_mac_address=None, headers=None, **request_parameters
    ):
        """Retrieves the list of path traces for the given ThousandEyes test result.  Notes: * For each trace there would
        be a list of hops in the path. * The hop index starts from 1. * It is possible that some hop indexes are
        missing in the trace. This could happen when details of the hop could not be determined. * If
        `clientMacAddress` parameter is provided, then the trace would start from the given client. But if the
        given client is not connected to the switch where ThousandEyes agent is running, then the path trace
        will not be accurate. The path from agent onwards will be correct though. * The last hop for each trace
        would be the target server hop, but in case the trace did not complete (packet lost), then the
        penultimate hop would have attribute `traceTerminated: true`, and it means that the packet was not
        forwarded till the target.  For detailed information about the usage of the API, please refer to the
        Open API specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-thousandEyesPathViz-1.0.0-resolved.yaml.

        Args:
            id(str): id path parameter. Unique identifier of the test result.
            client_mac_address(str): clientMacAddress query parameter. Optional client MAC address. If this is
                provided the the path trace would start from the given client, otherwise the path trace
                starts from the switch where ThousanEyes agent is running. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-path-traces-for-the-given-thousand-eyes-test-result
        """
        check_type(headers, dict)
        check_type(client_mac_address, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "clientMacAddress": client_mac_address,
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

        e_url = "/dna/data/api/v1/thousandEyesTestResults/{id}/pathTraces"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c616c07cbda559194d82311fb2ec7cc_v3_2_3_0", json_data
        )

    def retrieves_the_client_count_for_the_given_application(
        self,
        id,
        site_id,
        end_time=None,
        exporter_network_device_id=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the client count for the given application. If startTime and endTime are not provided, the API
        defaults to the last 24 hours. `siteId` is mandatory. `siteId` must be a site UUID of a building. For
        detailed information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-NetworkApplications-1.0.2-resolved.yaml.

        Args:
            id(str): id path parameter. id is the network application name. .
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            site_id(str): siteId query parameter. The site UUID without the top level hierarchy.`siteId` is
                mandatory. `siteId` must be a site UUID of a building. (Ex."buildingUuid") Examples:
                `siteId=buildingUuid` (single siteId requested)
                `siteId=buildingUuid1&siteId=buildingUuid2` (multiple siteId requested).
            exporter_network_device_id(str): exporterNetworkDeviceId query parameter. Unique ID of the netflow
                exporter device. Examples:
                `exporterNetworkDeviceId=5b234dbc-583e-491b-bf1a-318bba6c017f` (single
                exporterNetworkDeviceId requested) `exporterNetworkDeviceId=5b234dbc-583e-491b-bf1a-
                318bba6c017f&exporterNetworkDeviceId=8b234dbc-583e-491b-bf1a-318bba6c017f` (multiple
                exporterNetworkDeviceId requested) .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-client-count-for-the-given-application
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(site_id, str, may_be_none=False)
        check_type(exporter_network_device_id, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "siteId": site_id,
            "exporterNetworkDeviceId": exporter_network_device_id,
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

        e_url = "/dna/data/api/v1/networkApplications/{id}/clients/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b36ae8285d45e3da3c22e1d77eb2bb2_v3_2_3_0", json_data
        )

    def applications(
        self,
        application_health=None,
        application_name=None,
        device_id=None,
        end_time=None,
        limit=None,
        mac_address=None,
        offset=None,
        site_id=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Intent API to get a list of applications for a specific site, a device, or a client device's MAC address. For a
        combination of a specific application with site and/or device the API gets list of
        issues/devices/endpoints.

        Args:
            site_id(str): siteId query parameter. Assurance site UUID value (Cannot be submitted together with
                deviceId and clientMac).
            device_id(str): deviceId query parameter. Assurance device UUID value (Cannot be submitted together with
                siteId and clientMac).
            mac_address(str): macAddress query parameter. Client device's MAC address (Cannot be submitted together
                with siteId and deviceId).
            start_time(int): startTime query parameter. Starting epoch time in milliseconds of time window.
            end_time(int): endTime query parameter. Ending epoch time in milliseconds of time window.
            application_health(str): applicationHealth query parameter. Application health category (POOR, FAIR, or
                GOOD.  Optionally use with siteId only).
            offset(int): offset query parameter. The offset of the first application in the returned data
                (optionally used with siteId only).
            limit(int): limit query parameter. The max number of application entries in returned data [1, 1000]
                (optionally used with siteId only).
            application_name(str): applicationName query parameter. The name of the application to get information
                on.
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
            https://developer.cisco.com/docs/dna-center/#!applications
        """
        check_type(headers, dict)
        check_type(site_id, str)
        check_type(device_id, str)
        check_type(mac_address, str)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(application_health, str)
        check_type(offset, int)
        check_type(limit, int)
        check_type(application_name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "siteId": site_id,
            "deviceId": device_id,
            "macAddress": mac_address,
            "startTime": start_time,
            "endTime": end_time,
            "applicationHealth": application_health,
            "offset": offset,
            "limit": limit,
            "applicationName": application_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/application-health"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b85e4ce533d5ff49ddd3b2f9657cfa5_v3_2_3_0", json_data
        )
