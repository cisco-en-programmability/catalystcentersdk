"""Cisco Catalyst Center Issues API wrapper.

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


class Issues:
    """Cisco Catalyst Center Issues API (version: 3.2.3.0).

    Wraps the Catalyst Center Issues
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Issues
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

    def issue_trigger_definition_update(
        self,
        id,
        issueEnabled=None,
        priority=None,
        synchronizeToHealthThreshold=None,
        thresholdValue=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Update issue trigger threshold, priority for the given id.  Also enable or disable issue trigger for the given
        id. For detailed information about the usage of the API, please refer to the Open API specification
        document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-issueAndHealthDefinitions-1.0.0-resolved.yaml.   OpenAPI
        specification defined to update issue trigger threshold, priority for the given id, also enable or
        disable issue trigger for the given id.   API Support Documentation   id   Issue trigger definition id.
        The supported attributes of payload defined in  'IssueTriggerDefinition'.

        Args:
            issueEnabled(boolean): Issues's issueEnabled.
            priority(string): Issues's priority.
            synchronizeToHealthThreshold(boolean): Issues's synchronizeToHealthThreshold.
            thresholdValue(number): Issues's thresholdValue.
            id(str): id path parameter. Issue trigger definition id.
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
            https://developer.cisco.com/docs/dna-center/#!issue-trigger-definition-update
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
            "synchronizeToHealthThreshold": synchronizeToHealthThreshold,
            "priority": priority,
            "issueEnabled": issueEnabled,
            "thresholdValue": thresholdValue,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f25c825ca6e58a5b1c2294b11558e7b_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/systemIssueDefinitions/{id}"
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
            "bpm_f25c825ca6e58a5b1c2294b11558e7b_v3_2_3_0", json_data
        )

    def get_issue_trigger_definition_for_given_id(
        self, id, headers=None, **request_parameters
    ):
        """Get system issue defintion for the given id. Definition includes all properties from IssueTriggerDefinition
        schema by default. For detailed information about the usage of the API, please refer to the Open API
        specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-issueAndHealthDefinitions-1.0.0-resolved.yaml.   OpenAPI
        specification defined to get system issue defintion for the given id. Definition includes all properties
        from IssueTriggerDefinition schema by default.   API Support Documentation   id   Issue trigger
        definition id.

        Args:
            id(str): id path parameter. Issue trigger definition id.
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
            https://developer.cisco.com/docs/dna-center/#!get-issue-trigger-definition-for-given-id
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

        e_url = "/dna/intent/api/v1/systemIssueDefinitions/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cccbb5d35c9c5be9b837a0c1a33cbff8_v3_2_3_0", json_data
        )

    def get_all_the_custom_issue_definitions_based_on_the_given_filters(
        self,
        facility=None,
        id=None,
        is_enabled=None,
        limit=None,
        mnemonic=None,
        name=None,
        offset=None,
        order=None,
        priority=None,
        profile_id=None,
        severity=None,
        sort_by=None,
        headers=None,
        **request_parameters
    ):
        """Retrieve the existing syslog-based custom issue definitions. The supported filters are id, name, profileId,
        definition enable status, priority, severity, facility and mnemonic. The issue definition configurations
        may vary across profiles, hence specifying the profile Id in the query parameter is important and the
        default profile is global.    The assurance profile definitions can be obtain via the API endpoint:
        /api/v1/siteprofile?namespace=assurance. For detailed information about the usage of the API, please
        refer to the Open API specification document https://github.com/cisco-en-programmability/catalyst-
        center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        AssuranceUserDefinedIssueAPIs-1.0.0-resolved.yaml.   Retrieve the existing syslog-based custom issue
        definitions. The supported filters are id, name, profileId,  definition enable status, priority,
        severity, facility and mnemonic. The issue definition configurations may vary across profiles, hence
        specifying the profile Id in the query parameter is important and the profile is  global .   The
        assurance profile definitions can be obtain via the API endpoint
        /api/v1/siteprofile?namespace=assurance .   The details about the each fields are below,     Field name
        Description id The issue definition identifier name The name of the issue definition description The
        description about the issue definition profileId The issue definition  associated profile Id rules One
        or more rules contain conditions for generating issues. Currently, the supported limit for rules is set
        to 1. A rule contains severity, facility, mnemonic pattern, occurrences and durationInMinutes fields.
        severity The syslog severity levels supported include  0, 1, 2, 3, 4, 5, 6 0 Emergency 1 Alert 2
        Critical 3 Error 4 Warning 5 Notice 6 Info facility The syslog facility name pattern The message pattern
        specified within the issue definition. occurrences The number of occurrences count required for the
        issue to trigger. The default occurrences count is 1 durationInMinutes The duration in minutes for which
        the issue must persist to trigger. The maximum supported duration is 15 minutes. The default is 1
        minutes isEnabled The status of issue definition, can be either enabled or disabled. The default is
        disabled. priority The Issue definition priority level. The supported levels are  P1, P2, P3, P4 .
        isDeletable Specifies whether the definition can be deleted using the DELETE Post API. The deletion is
        only supported for the  default  profile associated definitions. isNotificationEnabled The status of
        notification enablement can be either enabled or disabled. The default is disabled. createdTime The
        creation time of the issue definition, represented in UNIX epoch time in milliseconds lastUpdatedTime
        The last time of the issue definition, represented in UNIX epoch time in milliseconds.

        Args:
            id(str): id query parameter. The custom issue definition identifier and unique identifier across the
                profile.Examples: id=6bef213c-19ca-4170-8375-b694e251101c (single entity uuid requested)
                id=6bef213c-19ca-4170-8375-b694e251101c&id=19ca-4170-8375-b694e251101c-6bef213c
                (multiple Id request in the query param) .
            profile_id(str): profileId query parameter. The profile identifier to fetch the profile associated
                custom issue definitions. The default is global. For the custom profile, it is profile
                UUID. Example : 3fa85f64-5717-4562-b3fc-2c963f66afa6 .
            name(str): name query parameter. The list of UDI issue names.
            priority(str): priority query parameter. The Issue priority value, possible values are P1, P2, P3, P4.
                P1: A critical issue that needs immediate attention and can have a wide impact on
                network operations. P2: A major issue that can potentially impact multiple devices or
                clients. P3: A minor issue that has a localized or minimal impact. P4: A warning issue
                that may not be an immediate problem but addressing it can optimize the network
                performance.
            is_enabled(bool): isEnabled query parameter. The enable status of the custom issue definition, either
                true or false.
            severity(int): severity query parameter. The syslog severity level. 0: Emergency 1: Alert, 2: Critical.
                3: Error, 4: Warning, 5: Notice, 6: Info. Examples:severity=1&severity=2 (multi value
                support with & separator) .
            facility(str): facility query parameter. The syslog facility name.
            mnemonic(str): mnemonic query parameter. The syslog mnemonic name.
            limit(int): limit query parameter. The maximum number of records to return.
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
            https://developer.cisco.com/docs/dna-center/#!get-all-the-custom-issue-definitions-based-on-the-given-filters
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(profile_id, str)
        check_type(name, str)
        check_type(priority, str)
        check_type(is_enabled, bool)
        check_type(severity, int)
        check_type(facility, str)
        check_type(mnemonic, str)
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
            "id": id,
            "profileId": profile_id,
            "name": name,
            "priority": priority,
            "isEnabled": is_enabled,
            "severity": severity,
            "facility": facility,
            "mnemonic": mnemonic,
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

        e_url = "/dna/intent/api/v1/customIssueDefinitions"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a51b856ea8005c8cbf42ab64da3e1786_v3_2_3_0", json_data
        )

    def creates_a_new_user_defined_issue_definitions(
        self,
        description=None,
        isEnabled=None,
        isNotificationEnabled=None,
        name=None,
        priority=None,
        rules=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Create a new custom issue definition using the provided input request data. The unique identifier for this issue
        definition is id. Please note that the issue names cannot be duplicated. The definition is based on the
        syslog. For detailed information about the usage of the API, please refer to the Open API specification
        document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-AssuranceUserDefinedIssueAPIs-1.0.0-resolved.yaml.   Create
        a new custom issue definition using the provided input request data. The unique identifier for this
        issue definition is  id . Please note that the issue names cannot be duplicated. The definition is based
        on the syslog. The request should have the following details and Severity, facility, mnemonic & pattern
        should match.     Field name   Description name The name of the issue definition description The
        description about the issue definition isEnabled The status of issue definition, can be either enabled
        or disabled. Issues will be generated solely when this flag is enabled, based on the specified pattern.
        The default is disabled. priority The Issue definition priority level. The supported levels are  P1, P2,
        P3, P4 . isNotificationEnabled The status of notification enablement can be either enabled or disabled.
        The default is disabled. severity The syslog severity levels supported include  0, 1, 2, 3, 4, 5, 6   0
        Emergency 1 Alert 2 Critical 3 Error 4 Warning 5 Notice 6 Info facility The syslog facility name pattern
        The pattern is anticipated to encompass the message text, where dynamic values are substituted with  *
        For example, in Syslog message " 111769: *08 Mar 2024 19:59:14 GMT: %BGP-5-ADJCHANGE: neighbor
        11.10.10.1 Down . Input  neighbor 11.10.10.1 * , if you expect to track BGP up/down messages with remote
        11.10.10.1. Input  neighbor * Down , if you expect to track all BGP down messages with all remote IPs.
        Input  neighbor * * , if you expect to track all BGP down/up messages with all remote IPs occurrences
        The number of occurrences count required for the issue to trigger. The default occurrences count is 1
        durationInMinute The duration in minutes for which the issue must persist to trigger. The maximum
        supported duration is 15 minute. The default is 1 minutes.

        Args:
            description(string): Issues's description.
            isEnabled(boolean): Issues's isEnabled.
            isNotificationEnabled(boolean): Issues's isNotificationEnabled.
            name(string): Issues's name.
            priority(string): Issues's priority.
            rules(list): Issues's rules (list of objects).
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
            https://developer.cisco.com/docs/dna-center/#!creates-a-new-user-defined-issue-definitions
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
            "name": name,
            "description": description,
            "rules": rules,
            "isEnabled": isEnabled,
            "priority": priority,
            "isNotificationEnabled": isNotificationEnabled,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a4d8313a955433858e0137ba7ef672_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/customIssueDefinitions"
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
            "bpm_a4d8313a955433858e0137ba7ef672_v3_2_3_0", json_data
        )

    def get_top_n_analytics_data_of_issues(
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
        """Gets the Top N analytics data related to issues based on given filters and group by field. This data can be used
        to find top sites which has most issues or top device types with most issue etc,. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-IssuesList-3.2.2-resolved.yaml.   Gets the Top N analytics
        data related to issues based on given filters and group by field. This data can be used to find top
        sites which has most issues or top device types with most issue etc,. The input payload contains the
        following fields Field Name Description startTime start time from which API queries the data set related
        to the resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive & the
        default is latest endTime end time to which API queries the data set related to the resource. It must be
        specified in UNIX epochtime in milliseconds. Value is inclusive & the default is latest topN the total
        number of records to retrive. This is a required input for this Top-N analytcis endpoint groupBy
        specifies the attributes for grouping the issues. This is mandatory field filters used to define one or
        more conditions. Only the data that satisfy these conditions will be taken into consideration during the
        aggregation calculation. attributes attributes are used for obtaining one or more field's data in
        addition to the aggregated data. The supported attributes are listed in  IssuesAnalyticsAttributeKey
        model aggregateAttributes specifies the names of the attributes on which the aggregate function should
        be applied when querying the data. The supported attribute names are listed in
        IssuesAnalyticsAggregateAttribute  model page contains  limit, offset and sortBy  fields.  limit  Number
        of records to be returned in response,  offset  starting offset of data and  sortBy  attribute name,
        order to sort.

        Args:
            aggregateAttributes(list): Issues's aggregateAttributes (list of objects).
            attributes(list): Issues's attributes (list of strings).
            endTime(integer): Issues's endTime.
            filters(list): Issues's filters (list of objects).
            groupBy(list): Issues's groupBy (list of strings).
            page(object): Issues's page.
            startTime(integer): Issues's startTime.
            topN(integer): Issues's topN.
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
            https://developer.cisco.com/docs/dna-center/#!get-top-n-analytics-data-of-issues
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "Accept-Language" in headers:
                check_type(headers.get("Accept-Language"), str)
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
                "jsd_e7af120721c7519a84b13bbe4a1a0362_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/assuranceIssues/topNAnalytics"
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
            "bpm_e7af120721c7519a84b13bbe4a1a0362_v3_2_3_0", json_data
        )

    def get_the_details_of_issues_for_given_set_of_filters(
        self,
        endTime=None,
        filters=None,
        startTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Returns all details of each issue along with suggested actions for given set of filters specified in request
        body. If there is no start and/or end time, then end time will be defaulted to current time and start
        time will be defaulted to 24-hours ago from end time. https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        IssuesList-3.2.2-resolved.yaml.   Returns all details of each issue along with suggested actions for
        given set of filters specified in request body. If there is no start and/or end time, then end time will
        be defaulted to current time and start time will be defaulted to 24-hours ago from end time. Field Name
        Description startTime start time from which API queries the data set related to the resource. It must be
        specified in UNIX epochtime in milliseconds. Value is inclusive & the default is latest endTime end time
        to which API queries the data set related to the resource. It must be specified in UNIX epochtime in
        milliseconds. Value is inclusive & the default is latest filters used to define one or more conditions.
        Only the data that satisfy these conditions will be taken into consideration during the aggregation
        calculation. attributes List of attributes related to the issue. If these are provided, then only those
        attributes will be part of response along with the default attributes. Please refer to the
        IssuesResponseAttribute  Model for supported attributes. views View is predefined set of attributes
        supported by the API. Only the attributes related to the given view will be part of the API response
        along with default attributes. If multiple views are provided, then response will contain attributes
        from all those views. Please refer to the  IssuesView  Model for supported attributes. If no views are
        specified, all attributes will be returned. page contains  limit, offset and sortBy  fields.  limit
        Number of records to be returned in response,  offset  starting offset of data and  sortBy  attribute
        name, order to sort  .

        Args:
            endTime(integer): Issues's endTime.
            filters(list): Issues's filters (list of objects).
            startTime(integer): Issues's startTime.
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
            https://developer.cisco.com/docs/dna-center/#!get-the-details-of-issues-for-given-set-of-filters
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "Accept-Language" in headers:
                check_type(headers.get("Accept-Language"), str)
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
                "jsd_b818044610579a9b74ec582e7739ab_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/assuranceIssues/query"
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
            "bpm_b818044610579a9b74ec582e7739ab_v3_2_3_0", json_data
        )

    def get_the_details_of_issues_for_given_set_of_filters_know_your_network(
        self,
        ai_driven=None,
        attribute=None,
        category=None,
        device_family=None,
        device_type=None,
        end_time=None,
        entity_id=None,
        entity_type=None,
        fabric_driven=None,
        fabric_site_driven=None,
        fabric_site_id=None,
        fabric_transit_driven=None,
        fabric_transit_site_id=None,
        fabric_vn_driven=None,
        fabric_vn_name=None,
        is_global=None,
        issue_id=None,
        limit=None,
        mac_address=None,
        name=None,
        network_device_id=None,
        network_device_ip_address=None,
        offset=None,
        order=None,
        priority=None,
        severity=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        site_name=None,
        sort_by=None,
        start_time=None,
        status=None,
        updated_by=None,
        view=None,
        headers=None,
        **request_parameters
    ):
        """Returns all details of each issue along with suggested actions for given set of filters specified in query
        parameters. If there is no start and/or end time, then end time will be defaulted to current time and
        start time will be defaulted to 24-hours ago from end time. All string type query parameters support
        wildcard search (using *). For example: siteHierarchy=Global/San Jose/* returns issues under all sites
        whole siteHierarchy starts with "Global/San Jose/". https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        IssuesList-3.2.2-resolved.yaml.

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to current time. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            limit(int): limit query parameter. Maximum number of issues to return.
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1.
            sort_by(str): sortBy query parameter.
            order(str): order query parameter. The sort order of the field ascending or descending.
            is_global(bool): isGlobal query parameter. Global issues are those issues which impacts across many
                devices, sites. They are also displayed on Issue Dashboard in Catalyst Center UI. Non-
                Global issues are displayed only on Client 360 or Device 360 pages. If this flag is
                'true', only global issues are returned. If it if 'false', all issues are returned. .
            priority(str): priority query parameter. Priority of the issue. Supports single priority and multiple
                priorities Examples: priority=P1 (single priority requested)
                priority=P1&priority=P2&priority=P3 (multiple priorities requested) .
            severity(str): severity query parameter. Severity of the issue. Supports single severity and multiple
                severities. Examples: severity=high (single severity requested)
                severity=high&severity=medium (multiple severities requested) .
            status(str): status query parameter. Status of the issue. Supports single status and multiple statuses.
                Examples: status=active (single status requested) status=active&status=resolved
                (multiple statuses requested) .
            entity_type(str): entityType query parameter. Entity type of the issue. Supports single entity type and
                multiple entity types. Examples: entityType=networkDevice (single entity type requested)
                entityType=network device&entityType=client (multiple entity types requested) .
            category(str): category query parameter. Categories of the issue. Supports single category and multiple
                categories. Examples: category=availability (single status requested)
                category=availability&category=onboarding (multiple categories requested) .
            device_type(str): deviceType query parameter. Device Type of the device to which this issue belongs to.
                Supports single device type and multiple device types. Examples: deviceType=wireless
                controller (single device type requested) deviceType=wireless controller&deviceType=core
                (multiple device types requested) .
            device_family(str): deviceFamily query parameter. Device Family of the device to which this issue
                belongs to. Supports single device type and multiple device types. Examples:
                deviceFamily=Unified AP (single device type requested) deviceFamily=Unified
                AP&deviceFamily=Routers (multiple device types requested) .
            name(str): name query parameter. The name of the issue Examples: name=ap_down (single issue name
                requested) name=ap_down&name=wlc_monitor (multiple issue names requested) Issue names
                can be retrieved using the API /data/api/v1/assuranceIssueConfigurations .
            issue_id(str): issueId query parameter. UUID of the issue Examples:
                issueId=e52aecfe-b142-4287-a587-11a16ba6dd26 (single issue id requested) issueId=e52aecf
                e-b142-4287-a587-11a16ba6dd26&issueId=864d0421-02c0-43a6-9c52-81cad45f66d8 (multiple
                issue ids requested) .
            entity_id(str): entityId query parameter. Id of the entity for which this issue belongs to. For example,
                it     could be mac address of AP or UUID of Sensor   example: 68:ca:e4:79:3f:20
                4de02167-901b-43cf-8822-cffd3caa286f Examples: entityId=68:ca:e4:79:3f:20 (single entity
                id requested) entityId=68:ca:e4:79:3f:20&entityId=864d0421-02c0-43a6-9c52-81cad45f66d8
                (multiple entity ids requested) .
            updated_by(str): updatedBy query parameter. The user who last updated this issue. Examples:
                updatedBy=admin (single updatedBy requested) updatedBy=admin&updatedBy=john (multiple
                updatedBy requested) .
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
            site_name(str): siteName query parameter. The name of the site. (Ex. `FloorName`) This field supports
                wildcard asterisk (*) character search support. E.g. *San*, *San, San* Examples:
                `?siteName=building1` (single siteName requested)
                `?siteName=building1&siteName=building2&siteName=building3` (multiple siteNames
                requested) .
            site_id(str): siteId query parameter. The UUID of the site. (Ex. `flooruuid`) This field supports
                wildcard asterisk (*) character search support. E.g.*flooruuid*, *flooruuid, flooruuid*
                Examples: `?siteId=id1` (single id requested) `?siteId=id1&siteId=id2&siteId=id3`
                (multiple ids requested) .
            fabric_site_id(str): fabricSiteId query parameter. The UUID of the fabric site. (Ex. "flooruuid")
                Examples: fabricSiteId=e52aecfe-b142-4287-a587-11a16ba6dd26 (single id requested)
                fabricSiteId=e52aecfe-b142-4287-a587-11a16ba6dd26,864d0421-02c0-43a6-9c52-81cad45f66d8
                (multiple ids requested) .
            fabric_vn_name(str): fabricVnName query parameter. The name of the fabric virtual network Examples:
                fabricVnName=name1 (single fabric virtual network name requested)
                fabricVnName=name1&fabricVnName=name2&fabricVnName=name3 (multiple fabric virtual
                network names requested) .
            fabric_transit_site_id(str): fabricTransitSiteId query parameter. The UUID of the fabric transit site.
                (Ex. "flooruuid") Examples: fabricTransitSiteId=e52aecfe-b142-4287-a587-11a16ba6dd26
                (single id requested) fabricTransitSiteId=e52aecfe-b142-4287-a587-
                11a16ba6dd26&fabricTransitSiteId=864d0421-02c0-43a6-9c52-81cad45f66d8 (multiple ids
                requested) .
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
            mac_address(str): macAddress query parameter. The macAddress of the network device or client This field
                supports wildcard (`*`) character-based search.  Ex: `*AB:AB:AB*` or `AB:AB:AB*` or
                `*AB:AB:AB` Examples: `macAddress=AB:AB:AB:CD:CD:CD` (single macAddress requested)
                `macAddress=AB:AB:AB:CD:CD:DC&macAddress=AB:AB:AB:CD:CD:FE` (multiple macAddress
                requested) .
            view(str): view query parameter. The name of the View. Each view represents a specific data set. Please
                refer to the `IssuesView` Model for supported views. View is predefined set of
                attributes supported by the API. Only the attributes related to the given view will be
                part of the API response along with default attributes. If multiple views are provided,
                then response will contain attributes from all those views. If no views are specified,
                all attributes will be returned. (View Name: Included Attributes),  (`update`:
                updatedTime, updatedBy),  (`site`: siteName, siteHierarchy, siteId, siteHierarchyId),
                Examples: `view=update` (single view requested) `view=update&view=site` (multiple views
                requested)        .
            attribute(str): attribute query parameter. List of attributes related to the issue. If these are
                provided, then only those attributes will be part of response along with the default
                attributes. Please refer to the `IssuesResponseAttribute` Model for supported
                attributes. Examples: `attribute=deviceType` (single attribute requested)
                `attribute=deviceType&attribute=updatedBy` (multiple attributes requested) .
            ai_driven(bool): aiDriven query parameter. Flag whether the issue is AI driven issue.
            fabric_driven(bool): fabricDriven query parameter. Flag whether the issue is related to a Fabric site, a
                virtual network or a transit.
            fabric_site_driven(bool): fabricSiteDriven query parameter. Flag whether the issue is Fabric site driven
                issue.
            fabric_vn_driven(bool): fabricVnDriven query parameter. Flag whether the issue is Fabric Virtual Network
                driven issue.
            fabric_transit_driven(bool): fabricTransitDriven query parameter. Flag whether the issue is Fabric
                Transit driven issue.
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
            https://developer.cisco.com/docs/dna-center/#!get-the-details-of-issues-for-given-set-of-filters-know-your-network
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(limit, int)
        check_type(offset, int)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(is_global, bool)
        check_type(priority, str)
        check_type(severity, str)
        check_type(status, str)
        check_type(entity_type, str)
        check_type(category, str)
        check_type(device_type, str)
        check_type(device_family, str)
        check_type(name, str)
        check_type(issue_id, str)
        check_type(entity_id, str)
        check_type(updated_by, str)
        check_type(site_hierarchy, str)
        check_type(site_hierarchy_id, str)
        check_type(site_name, str)
        check_type(site_id, str)
        check_type(fabric_site_id, str)
        check_type(fabric_vn_name, str)
        check_type(fabric_transit_site_id, str)
        check_type(network_device_id, str)
        check_type(network_device_ip_address, str)
        check_type(mac_address, str)
        check_type(view, str)
        check_type(attribute, str)
        check_type(ai_driven, bool)
        check_type(fabric_driven, bool)
        check_type(fabric_site_driven, bool)
        check_type(fabric_vn_driven, bool)
        check_type(fabric_transit_driven, bool)
        if headers is not None:
            if "Accept-Language" in headers:
                check_type(headers.get("Accept-Language"), str)
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
            "isGlobal": is_global,
            "priority": priority,
            "severity": severity,
            "status": status,
            "entityType": entity_type,
            "category": category,
            "deviceType": device_type,
            "deviceFamily": device_family,
            "name": name,
            "issueId": issue_id,
            "entityId": entity_id,
            "updatedBy": updated_by,
            "siteHierarchy": site_hierarchy,
            "siteHierarchyId": site_hierarchy_id,
            "siteName": site_name,
            "siteId": site_id,
            "fabricSiteId": fabric_site_id,
            "fabricVnName": fabric_vn_name,
            "fabricTransitSiteId": fabric_transit_site_id,
            "networkDeviceId": network_device_id,
            "networkDeviceIpAddress": network_device_ip_address,
            "macAddress": mac_address,
            "view": view,
            "attribute": attribute,
            "aiDriven": ai_driven,
            "fabricDriven": fabric_driven,
            "fabricSiteDriven": fabric_site_driven,
            "fabricVnDriven": fabric_vn_driven,
            "fabricTransitDriven": fabric_transit_driven,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/assuranceIssues"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fe0609bc1db7594aabd91218a84f7cbf_v3_2_3_0", json_data
        )

    def get_the_total_number_of_issues_for_given_set_of_filters(
        self,
        endTime=None,
        filters=None,
        startTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Returns the total number issues for given set of filters. If there is no start and/or end time, then end time
        will be defaulted to current time and start time will be defaulted to 24-hours ago from end time. For
        detailed information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-IssuesList-3.2.2-resolved.yaml.   Returns the total number
        issues for given set of filters. If there is nostart and/or end time, then end time will be defaulted to
        current timeand start time will be defaulted to 24-hours ago from end time. The input payload contains
        the following fields: Field Name Description startTime start time from which API queries the data set
        related to the resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive &
        the default is latest endTime end time to which API queries the data set related to the resource. It
        must be specified in UNIX epochtime in milliseconds. Value is inclusive & the default is latest filters
        used to define one or more conditions. Only the data that satisfy these conditions will be taken into
        consideration during the aggregation calculation.

        Args:
            endTime(integer): Issues's endTime.
            filters(list): Issues's filters (list of objects).
            startTime(integer): Issues's startTime.
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
            https://developer.cisco.com/docs/dna-center/#!get-the-total-number-of-issues-for-given-set-of-filters
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
                "jsd_c14a815ec5938950343f6188f0785_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/assuranceIssues/query/count"
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
            "bpm_c14a815ec5938950343f6188f0785_v3_2_3_0", json_data
        )

    def get_the_total_number_of_issues_for_given_set_of_filters_know_your_network(
        self,
        ai_driven=None,
        category=None,
        device_family=None,
        device_type=None,
        end_time=None,
        entity_id=None,
        entity_type=None,
        fabric_driven=None,
        fabric_site_driven=None,
        fabric_site_id=None,
        fabric_transit_driven=None,
        fabric_transit_site_id=None,
        fabric_vn_driven=None,
        fabric_vn_name=None,
        is_global=None,
        issue_id=None,
        mac_address=None,
        name=None,
        network_device_id=None,
        network_device_ip_address=None,
        priority=None,
        severity=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        site_name=None,
        start_time=None,
        status=None,
        updated_by=None,
        headers=None,
        **request_parameters
    ):
        """Returns the total number issues for given set of filters. If there is no start and/or end time, then end time
        will be defaulted to current time and start time will be defaulted to 24-hours ago from end time.
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-IssuesList-3.2.2-resolved.yaml.

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to current time. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            is_global(bool): isGlobal query parameter. Global issues are those issues which impacts across many
                devices, sites. They are also displayed on Issue Dashboard in Catalyst Center UI. Non-
                Global issues are displayed only on Client 360 or Device 360 pages. If this flag is
                'true', only global issues are returned. If it if 'false', all issues are returned. .
            priority(str): priority query parameter. Priority of the issue. Supports single priority and multiple
                priorities Examples: priority=P1 (single priority requested)
                priority=P1&priority=P2&priority=P3 (multiple priorities requested) .
            severity(str): severity query parameter. Severity of the issue. Supports single severity and multiple
                severities. Examples: severity=high (single severity requested)
                severity=high&severity=medium (multiple severities requested) .
            status(str): status query parameter. Status of the issue. Supports single status and multiple statuses.
                Examples: status=active (single status requested) status=active&status=resolved
                (multiple statuses requested) .
            entity_type(str): entityType query parameter. Entity type of the issue. Supports single entity type and
                multiple entity types. Examples: entityType=networkDevice (single entity type requested)
                entityType=network device&entityType=client (multiple entity types requested) .
            category(str): category query parameter. Categories of the issue. Supports single category and multiple
                categories. Examples: category=availability (single status requested)
                category=availability&category=onboarding (multiple categories requested) .
            device_type(str): deviceType query parameter. Device Type of the device to which this issue belongs to.
                Supports single device type and multiple device types. Examples: deviceType=wireless
                controller (single device type requested) deviceType=wireless controller&deviceType=core
                (multiple device types requested) .
            device_family(str): deviceFamily query parameter. Device Family of the device to which this issue
                belongs to. Supports single device type and multiple device types. Examples:
                deviceFamily=Unified AP (single device type requested) deviceFamily=Unified
                AP&deviceFamily=Routers (multiple device types requested) .
            name(str): name query parameter. The name of the issue Examples: name=ap_down (single issue name
                requested) name=ap_down&name=wlc_monitor (multiple issue names requested) Issue names
                can be retrieved using the API /data/api/v1/assuranceIssueConfigurations .
            issue_id(str): issueId query parameter. UUID of the issue Examples:
                issueId=e52aecfe-b142-4287-a587-11a16ba6dd26 (single issue id requested) issueId=e52aecf
                e-b142-4287-a587-11a16ba6dd26&issueId=864d0421-02c0-43a6-9c52-81cad45f66d8 (multiple
                issue ids requested) .
            entity_id(str): entityId query parameter. Id of the entity for which this issue belongs to. For example,
                it     could be mac address of AP or UUID of Sensor   example: 68:ca:e4:79:3f:20
                4de02167-901b-43cf-8822-cffd3caa286f Examples: entityId=68:ca:e4:79:3f:20 (single entity
                id requested) entityId=68:ca:e4:79:3f:20&entityId=864d0421-02c0-43a6-9c52-81cad45f66d8
                (multiple entity ids requested) .
            updated_by(str): updatedBy query parameter. The user who last updated this issue. Examples:
                updatedBy=admin (single updatedBy requested) updatedBy=admin&updatedBy=john (multiple
                updatedBy requested) .
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
            site_name(str): siteName query parameter. The name of the site. (Ex. `FloorName`) This field supports
                wildcard asterisk (*) character search support. E.g. *San*, *San, San* Examples:
                `?siteName=building1` (single siteName requested)
                `?siteName=building1&siteName=building2&siteName=building3` (multiple siteNames
                requested) .
            site_id(str): siteId query parameter. The UUID of the site. (Ex. `flooruuid`) This field supports
                wildcard asterisk (*) character search support. E.g.*flooruuid*, *flooruuid, flooruuid*
                Examples: `?siteId=id1` (single id requested) `?siteId=id1&siteId=id2&siteId=id3`
                (multiple ids requested) .
            fabric_site_id(str): fabricSiteId query parameter. The UUID of the fabric site. (Ex. "flooruuid")
                Examples: fabricSiteId=e52aecfe-b142-4287-a587-11a16ba6dd26 (single id requested)
                fabricSiteId=e52aecfe-b142-4287-a587-11a16ba6dd26,864d0421-02c0-43a6-9c52-81cad45f66d8
                (multiple ids requested) .
            fabric_vn_name(str): fabricVnName query parameter. The name of the fabric virtual network Examples:
                fabricVnName=name1 (single fabric virtual network name requested)
                fabricVnName=name1&fabricVnName=name2&fabricVnName=name3 (multiple fabric virtual
                network names requested) .
            fabric_transit_site_id(str): fabricTransitSiteId query parameter. The UUID of the fabric transit site.
                (Ex. "flooruuid") Examples: fabricTransitSiteId=e52aecfe-b142-4287-a587-11a16ba6dd26
                (single id requested) fabricTransitSiteId=e52aecfe-b142-4287-a587-
                11a16ba6dd26&fabricTransitSiteId=864d0421-02c0-43a6-9c52-81cad45f66d8 (multiple ids
                requested) .
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
            mac_address(str): macAddress query parameter. The macAddress of the network device or client This field
                supports wildcard (`*`) character-based search.  Ex: `*AB:AB:AB*` or `AB:AB:AB*` or
                `*AB:AB:AB` Examples: `macAddress=AB:AB:AB:CD:CD:CD` (single macAddress requested)
                `macAddress=AB:AB:AB:CD:CD:DC&macAddress=AB:AB:AB:CD:CD:FE` (multiple macAddress
                requested) .
            ai_driven(bool): aiDriven query parameter. Flag whether the issue is AI driven issue.
            fabric_driven(bool): fabricDriven query parameter. Flag whether the issue is related to a Fabric site, a
                virtual network or a transit.
            fabric_site_driven(bool): fabricSiteDriven query parameter. Flag whether the issue is Fabric site driven
                issue.
            fabric_vn_driven(bool): fabricVnDriven query parameter. Flag whether the issue is Fabric Virtual Network
                driven issue.
            fabric_transit_driven(bool): fabricTransitDriven query parameter. Flag whether the issue is Fabric
                Transit driven issue.
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
            https://developer.cisco.com/docs/dna-center/#!get-the-total-number-of-issues-for-given-set-of-filters-know-your-network
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(is_global, bool)
        check_type(priority, str)
        check_type(severity, str)
        check_type(status, str)
        check_type(entity_type, str)
        check_type(category, str)
        check_type(device_type, str)
        check_type(device_family, str)
        check_type(name, str)
        check_type(issue_id, str)
        check_type(entity_id, str)
        check_type(updated_by, str)
        check_type(site_hierarchy, str)
        check_type(site_hierarchy_id, str)
        check_type(site_name, str)
        check_type(site_id, str)
        check_type(fabric_site_id, str)
        check_type(fabric_vn_name, str)
        check_type(fabric_transit_site_id, str)
        check_type(network_device_id, str)
        check_type(network_device_ip_address, str)
        check_type(mac_address, str)
        check_type(ai_driven, bool)
        check_type(fabric_driven, bool)
        check_type(fabric_site_driven, bool)
        check_type(fabric_vn_driven, bool)
        check_type(fabric_transit_driven, bool)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "isGlobal": is_global,
            "priority": priority,
            "severity": severity,
            "status": status,
            "entityType": entity_type,
            "category": category,
            "deviceType": device_type,
            "deviceFamily": device_family,
            "name": name,
            "issueId": issue_id,
            "entityId": entity_id,
            "updatedBy": updated_by,
            "siteHierarchy": site_hierarchy,
            "siteHierarchyId": site_hierarchy_id,
            "siteName": site_name,
            "siteId": site_id,
            "fabricSiteId": fabric_site_id,
            "fabricVnName": fabric_vn_name,
            "fabricTransitSiteId": fabric_transit_site_id,
            "networkDeviceId": network_device_id,
            "networkDeviceIpAddress": network_device_ip_address,
            "macAddress": mac_address,
            "aiDriven": ai_driven,
            "fabricDriven": fabric_driven,
            "fabricSiteDriven": fabric_site_driven,
            "fabricVnDriven": fabric_vn_driven,
            "fabricTransitDriven": fabric_transit_driven,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/assuranceIssues/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ada8eb3ff5b8db9eccfb778cc578e_v3_2_3_0", json_data
        )

    def returns_all_issue_trigger_definitions_for_given_filters(
        self,
        attribute=None,
        device_type=None,
        id=None,
        issue_enabled=None,
        limit=None,
        name=None,
        offset=None,
        order=None,
        priority=None,
        profile_id=None,
        sort_by=None,
        headers=None,
        **request_parameters
    ):
        """Get all system issue defintions. The supported filters are id, name, profileId and definition enable status. An
        issue trigger definition can be different across the profile and device type. So, `profileId` and
        `deviceType` in the query param is important and default is global profile and all device type. For
        detailed information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-issueAndHealthDefinitions-1.0.0-resolved.yaml.   OpenAPI
        specification defined to get all system issue defintions. API Support Documentation Query Parameters:
        deviceType These are the device families/types supported for system issue definitions. If no input is
        made on device type, all device types are considered.  Supported values: ROUTER, SWITCH_AND_HUB,
        WIRELESS_CONTROLLER, UNIFIED_AP, WIRELESS_CLIENT, WIRED_CLIENT, SENSOR, APPLICATION, THIRD_PARTY_DEVICE
        Example :   ?deviceType=ROUTER profileId The profile identier to fetch the profile associated issue
        defintions. The default is 'global'. Please refer Network design profiles documentation for more
        details.   Example :   ?profileId=profileid id The definition identifier.   Examples :
        ?id=015d9cba-4f53-4087-8317-7e49e5ffef46 (single id requested)
        ?id=T015d9cba-4f53-4087-8317-7e49e5ffef46&id=015d9cba-4f53-4087-8317-7e49e5ffef47 (multiple id
        requested) name The list of system defined issue names. (Ex. 'BGP_Down') Examples :   ?name=BGP_Down
        (single issue name requested)  ?name=BGP_Down&name=BGP_Flap(multiple issue names requested) priority
        Issue priority, possible values are P1, P2, P3, P4. 'P1': A critical issue that needs immediate
        attention and can have a wide impact on network operations.  'P2': A major issue that can potentially
        impact multiple devices or clients.  'P3': A minor issue that has a localized or minimal impact.  'P4':
        A warning issue that may not be an immediate problem but addressing it can optimize the network
        performance.   Example :   ?priority=P1 issueEnabled The profile identier to fetch the profile
        associated issue defintions. The default is 'global'. Please refer Network design profiles documentation
        for more details.   Example :   ?issueEnabled=true attribute The list of attributes that needs to be
        included in the response. By default, all properties are sent in response. Supported Attributes:
        categoryName ,  definitionStatus ,  defaultPriority ,  deviceType ,  id ,  issueEnabled ,  name ,
        priority , profileId , synchronizeToHealthThreshold , thresholdValue     Examples :
        ?attribute=categoryName (single attribute requested) ?attribute=categoryName&attribute=definitionStatus
        (multiple attribute requested) offset Specifies the starting point within all records returned by the
        API. It's one based offset. The starting value is 1. Default value: 1  limit Maximum number of records
        to return. Default value: 500 sortBy A field within the response to sortBy. Default value : timestamp
        order The sort order of the field ascending or descending. Default value : asc.

        Args:
            device_type(str): deviceType query parameter. These are the device families/types supported for system
                issue definitions. If no input is made on device type, all device types are considered.
            profile_id(str): profileId query parameter. The profile identier to fetch the profile associated issue
                defintions. The default is `global`. Please refer Network design profiles documentation
                for more details.
            id(str): id query parameter. The definition identifier. Examples:
                id=015d9cba-4f53-4087-8317-7e49e5ffef46 (single entity id request)
                id=015d9cba-4f53-4087-8317-7e49e5ffef46&id=015d9cba-4f53-4087-8317-7e49e5ffef47
                (multiple ids in the query param) .
            name(str): name query parameter. The list of system defined issue names. (Ex."BGP_Down") Examples:
                name=BGP_Down (single entity uuid requested) name=BGP_Down&name=BGP_Flap (multiple issue
                names separated by & operator) .
            priority(str): priority query parameter. Issue priority, possible values are P1, P2, P3, P4. `P1`: A
                critical issue that needs immediate attention and can have a wide impact on network
                operations. `P2`: A major issue that can potentially impact multiple devices or clients.
                `P3`: A minor issue that has a localized or minimal impact. `P4`: A warning issue that
                may not be an immediate problem but addressing it can optimize the network performance.
                .
            issue_enabled(bool): issueEnabled query parameter. The enablement status of the issue definition, either
                true or false.
            attribute(str): attribute query parameter. These are the attributes supported in system issue
                definitions response. By default, all properties are sent in response. .
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
            https://developer.cisco.com/docs/dna-center/#!returns-all-issue-trigger-definitions-for-given-filters
        """
        check_type(headers, dict)
        check_type(device_type, str)
        check_type(profile_id, str)
        check_type(id, str)
        check_type(name, str)
        check_type(priority, str)
        check_type(issue_enabled, bool)
        check_type(attribute, str)
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
            "deviceType": device_type,
            "profileId": profile_id,
            "id": id,
            "name": name,
            "priority": priority,
            "issueEnabled": issue_enabled,
            "attribute": attribute,
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

        e_url = "/dna/intent/api/v1/systemIssueDefinitions"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d97f6433e45a53d2a56a958ba83faab5_v3_2_3_0", json_data
        )

    def get_the_custom_issue_definition_for_the_given_custom_issue_definition_id(
        self, id, headers=None, **request_parameters
    ):
        """Get the custom issue definition for the given custom issue definition Id. For detailed information about the
        usage of the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        AssuranceUserDefinedIssueAPIs-1.0.0-resolved.yaml.  Get the custom issue definition for the given custom
        issue definition Id.

        Args:
            id(str): id path parameter. Get the custom issue definition for the given custom issue definition Id.
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
            https://developer.cisco.com/docs/dna-center/#!get-the-custom-issue-definition-for-the-given-custom-issue-definition-id
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

        e_url = "/dna/intent/api/v1/customIssueDefinitions/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b9df2373a5d4bba8e04a6c14367ec_v3_2_3_0", json_data
        )

    def updates_an_existing_custom_issue_definition_based_on_the_provided_id(
        self,
        id,
        description=None,
        isEnabled=None,
        isNotificationEnabled=None,
        name=None,
        priority=None,
        rules=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Updates an existing custom issue definition based on the provided Id. For detailed information about the usage
        of the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        AssuranceUserDefinedIssueAPIs-1.0.0-resolved.yaml.  Updates an existing custom issue definition based on
        the provided Id.

        Args:
            description(string): Issues's description.
            isEnabled(boolean): Issues's isEnabled.
            isNotificationEnabled(boolean): Issues's isNotificationEnabled.
            name(string): Issues's name.
            priority(string): Issues's priority.
            rules(list): Issues's rules (list of objects).
            id(str): id path parameter. The custom issue definition Identifier.
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
            https://developer.cisco.com/docs/dna-center/#!updates-an-existing-custom-issue-definition-based-on-the-provided-id
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
            "name": name,
            "description": description,
            "rules": rules,
            "isEnabled": isEnabled,
            "priority": priority,
            "isNotificationEnabled": isNotificationEnabled,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_c0204c665262a712caef988d7d88_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/customIssueDefinitions/{id}"
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
            "bpm_c0204c665262a712caef988d7d88_v3_2_3_0", json_data
        )

    def deletes_an_existing_custom_issue_definition(
        self, id, headers=None, **request_parameters
    ):
        """Deletes an existing custom issue definition based on the Id. Only the Global profile issue has the access to
        delete the issue definition, so no profile id is required. For detailed information about the usage of
        the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        AssuranceUserDefinedIssueAPIs-1.0.0-resolved.yaml.  Deletes an existing custom issue definition based on
        the Id. Only the Global profile issue has the access to delete the issue definition, so no profile id is
        required.

        Args:
            id(str): id path parameter. The custom issue definition unique identifier.
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
            https://developer.cisco.com/docs/dna-center/#!deletes-an-existing-custom-issue-definition
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

        e_url = "/dna/intent/api/v1/customIssueDefinitions/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f5ace826dd39514dbb0e0dde0599c1f5_v3_2_3_0", json_data
        )

    def ignore_the_given_list_of_issues(
        self,
        ignoreHours=None,
        issueIds=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Ignores the given list of issues. The response contains the list of issues which were successfully ignored as
        well as the issues which are failed to ignore. After this API returns success response, it may take few
        seconds for the issue status to be updated if the system is heavily loaded. Please use `GET
        /dna/data/api/v1/assuranceIssues/{id}` API to fetch the details of a particular issue and verify
        `updatedTime`. For detailed information about the usage of the API, please refer to the Open API
        specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-IssuesLifecycle-1.0.0-resolved.yaml.

        Args:
            ignoreHours(integer): Issues's ignoreHours.
            issueIds(list): Issues's issueIds (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!ignore-the-given-list-of-issues
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
            "issueIds": issueIds,
            "ignoreHours": ignoreHours,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f2c49c69c53e7b4f57f2af9a6f597_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/assuranceIssues/ignore"
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
            "bpm_f2c49c69c53e7b4f57f2af9a6f597_v3_2_3_0", json_data
        )

    def get_all_the_details_and_suggested_actions_of_an_issue_for_the_given_issue_id(
        self, id, attribute=None, view=None, headers=None, **request_parameters
    ):
        """Returns all the details and suggested actions of an issue for the given issue id. https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        IssuesList-1.0.0-resolved.yaml.

        Args:
            id(str): id path parameter. The issue Uuid.
            view(str): view query parameter. The name of the View. Each view represents a specific data set. Please
                refer to the `IssuesView` Model for supported views. View is predefined set of
                attributes supported by the API. Only the attributes related to the given view will be
                part of the API response along with default attributes. If multiple views are provided,
                then response will contain attributes from all those views. If no views are specified,
                all attributes will be returned. (View Name: Included Attributes),  (`update`:
                updatedTime, updatedBy),  (`site`: siteName, siteHierarchy, siteId, siteHierarchyId),
                Examples: `view=update` (single view requested) `view=update&view=site` (multiple views
                requested)        .
            attribute(str): attribute query parameter. List of attributes related to the issue. If these are
                provided, then only those attributes will be part of response along with the default
                attributes. Please refer to the `IssuesResponseAttribute` Model for supported
                attributes. Examples: `attribute=deviceType` (single attribute requested)
                `attribute=deviceType&attribute=updatedBy` (multiple attributes requested) .
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
            https://developer.cisco.com/docs/dna-center/#!get-all-the-details-and-suggested-actions-of-an-issue-for-the-given-issue-id
        """
        check_type(headers, dict)
        check_type(view, str)
        check_type(attribute, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "Accept-Language" in headers:
                check_type(headers.get("Accept-Language"), str)
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
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

        e_url = "/dna/data/api/v1/assuranceIssues/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e350bcc73ba5202aeaeed88175f0d44_v3_2_3_0", json_data
        )

    def get_the_total_custom_issue_definitions_count_based_on_the_provided_filters(
        self,
        facility=None,
        id=None,
        is_enabled=None,
        mnemonic=None,
        name=None,
        priority=None,
        profile_id=None,
        severity=None,
        headers=None,
        **request_parameters
    ):
        """Get the total number of Custom issue definitions count based on the provided filters. The supported filters are
        id, name, profileId and definition enable status, severity, facility and mnemonic. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-AssuranceUserDefinedIssueAPIs-1.0.0-resolved.yaml.  Get the
        total number of Custom issue definitions count based on the provided filters. The supported filters are
        id, name, profileId and definition enable status, severity, facility and mnemonic.

        Args:
            id(str): id query parameter. The custom issue definition identifier and unique identifier across the
                profile. Examples: id=6bef213c-19ca-4170-8375-b694e251101c (single entity uuid
                requested)
                id=6bef213c-19ca-4170-8375-b694e251101c&id=19ca-4170-8375-b694e251101c-6bef213c
                (multiple Id request in the query param) .
            profile_id(str): profileId query parameter. The profile identifier to fetch the profile associated
                custom issue definitions. The default is global. For the custom profile, it is profile
                UUID. Example : 3fa85f64-5717-4562-b3fc-2c963f66afa6 .
            name(str): name query parameter. The list of UDI issue names. (Ex."TestUdiIssues") .
            priority(str): priority query parameter. The Issue priority value, possible values are P1, P2, P3, P4.
                P1: A critical issue that needs immediate attention and can have a wide impact on
                network operations. P2: A major issue that can potentially impact multiple devices or
                clients. P3: A minor issue that has a localized or minimal impact. P4: A warning issue
                that may not be an immediate problem but addressing it can optimize the network
                performance.
            is_enabled(bool): isEnabled query parameter. The enable status of the custom issue definition, either
                true or false.
            severity(int): severity query parameter. The syslog severity level. 0: Emergency 1: Alert, 2: Critical.
                3: Error, 4: Warning, 5: Notice, 6: Info. Examples:severity=1&severity=2 (multi value
                support with & separator) .
            facility(str): facility query parameter. The syslog facility name.
            mnemonic(str): mnemonic query parameter. The syslog mnemonic name.
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
            https://developer.cisco.com/docs/dna-center/#!get-the-total-custom-issue-definitions-count-based-on-the-provided-filters
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(profile_id, str)
        check_type(name, str)
        check_type(priority, str)
        check_type(is_enabled, bool)
        check_type(severity, int)
        check_type(facility, str)
        check_type(mnemonic, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "profileId": profile_id,
            "name": name,
            "priority": priority,
            "isEnabled": is_enabled,
            "severity": severity,
            "facility": facility,
            "mnemonic": mnemonic,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/customIssueDefinitions/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ae1668865945349b9dcef2d60b7ba03_v3_2_3_0", json_data
        )

    def get_summary_analytics_data_of_issues(
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
        """Gets the summary analytics data related to issues based on given filters and group by field. This data can be
        used to find issue counts grouped by different keys. For detailed information about the usage of the
        API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        IssuesList-3.2.2-resolved.yaml.   Gets the summary analytics data related to issues based on given
        filters and group by field. This data can be used to find issue counts grouped by different keys. The
        input payload contains the following fields Field Name Description startTime start time from which API
        queries the data set related to the resource. It must be specified in UNIX epochtime in milliseconds.
        Value is inclusive & the default is latest endTime end time to which API queries the data set related to
        the resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive & the default
        is latest groupBy specifies the attributes for grouping the issues. filters used to define one or more
        conditions. Only the data that satisfy these conditions will be taken into consideration during the
        aggregation calculation. attributes attributes are used for obtaining one or more field's data in
        addition to the aggregated data. The supported attributes are listed in  IssuesAnalyticsAttributeKey
        model aggregateAttributes specifies the name of the attribute on which the aggregate function should be
        applied when querying the data. The supported attribute names are listed in
        IssuesAnalyticsAggregateAttributeKey` model page contains  limit, offset and sortBy  fields.  limit
        Number of records to be returned in response,  offset  starting offset of data and  sortBy  attribute
        name, order to sort.

        Args:
            aggregateAttributes(list): Issues's aggregateAttributes (list of objects).
            attributes(list): Issues's attributes (list of strings).
            endTime(integer): Issues's endTime.
            filters(list): Issues's filters (list of objects).
            groupBy(list): Issues's groupBy (list of strings).
            page(object): Issues's page.
            startTime(integer): Issues's startTime.
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
            https://developer.cisco.com/docs/dna-center/#!get-summary-analytics-data-of-issues
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "Accept-Language" in headers:
                check_type(headers.get("Accept-Language"), str)
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
                "jsd_b269afaaa855d3291b825f724fc8ea9_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/assuranceIssues/summaryAnalytics"
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
            "bpm_b269afaaa855d3291b825f724fc8ea9_v3_2_3_0", json_data
        )

    def get_issue_enrichment_details_v1(self, headers=None, **request_parameters):
        """Enriches a given network issue context (an issue id or end user’s Mac Address) with details about the issue(s),
        impacted hosts and suggested actions for remediation.

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
            https://developer.cisco.com/docs/dna-center/#!get-issue-enrichment-details-v1
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

        e_url = "/dna/intent/api/v1/issue-enrichment-details"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f2f039811951c0af53e3381ae91225_v3_2_3_0", json_data
        )

    def execute_suggested_actions_commands(
        self,
        entity_type=None,
        entity_value=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API fetches the issue details and suggested actions for an issue, given the Issue Id, executes the commands
        associated with the suggested actions to remediate the issue.

        Args:
            entity_type(string): Issues's Commands provided as part of the suggested actions for an issue can be
                executed based on issue id. The value here must be issue_id.
            entity_value(string): Issues's Contains the actual value for the entity type that has been defined.
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
            https://developer.cisco.com/docs/dna-center/#!execute-suggested-actions-commands
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
            "entity_type": entity_type,
            "entity_value": entity_value,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator("jsd_bc55e6552fac58cc0aaacd773a_v3_2_3_0").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/execute-suggested-actions-commands"
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
            "bpm_bc55e6552fac58cc0aaacd773a_v3_2_3_0", json_data
        )

    def get_the_count_of_system_defined_issue_definitions_based_on_provided_filters(
        self,
        device_type=None,
        id=None,
        issue_enabled=None,
        name=None,
        priority=None,
        profile_id=None,
        headers=None,
        **request_parameters
    ):
        """Get the count of system defined issue definitions based on provided filters. Supported filters are id, name,
        profileId and definition enable status. For detailed information about the usage of the API, please
        refer to the Open API specification document https://github.com/cisco-en-programmability/catalyst-
        center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-issueAndHealthDefinitions-1.0.0-resolved.yaml.
        OpenAPI specification defined to get the count of system defined issue definitions. API Support
        Documentation Query Parameters: deviceType These are the device families/types supported for system
        issue definitions. If no input is made on device type, all device types are considered.  Supported
        values: ROUTER, SWITCH_AND_HUB, WIRELESS_CONTROLLER, UNIFIED_AP, WIRELESS_CLIENT, WIRED_CLIENT, SENSOR,
        APPLICATION, THIRD_PARTY_DEVICE   Example :   ?deviceType=Router profileId The profile identier to fetch
        the profile associated issue defintions. The default is 'global'. Please refer Network design profiles
        documentation for more details.   Example :   ?profileId=profileid id The definition identifier.
        Examples :   ?id=015d9cba-4f53-4087-8317-7e49e5ffef46 (single id requested)
        ?id=T015d9cba-4f53-4087-8317-7e49e5ffef46&id=015d9cba-4f53-4087-8317-7e49e5ffef47 (multiple id
        requested) name The list of system defined issue names. (Ex. 'BGP_Down') Examples :   ?name=BGP_Down
        (single issue name requested)  ?name=BGP_Down&name=BGP_Flap(multiple issue names requested) priority
        Issue priority, possible values are P1, P2, P3, P4. 'P1': A critical issue that needs immediate
        attention and can have a wide impact on network operations.  'P2': A major issue that can potentially
        impact multiple devices or clients.  'P3': A minor issue that has a localized or minimal impact.  'P4':
        A warning issue that may not be an immediate problem but addressing it can optimize the network
        performance.   Example :   ?priority=P1 issueEnabled The profile identier to fetch the profile
        associated issue defintions. The default is 'global'. Please refer Network design profiles documentation
        for more details.   Example :   ?issueEnabled=true.

        Args:
            device_type(str): deviceType query parameter. These are the device families/types supported for system
                issue definitions. If no input is made on device type, all device types are considered.
            profile_id(str): profileId query parameter. The profile identier to fetch the profile associated issue
                defintions. The default is `global`. Please refer Network design profiles documentation
                for more details.
            id(str): id query parameter. The definition identifier. Examples:
                id=015d9cba-4f53-4087-8317-7e49e5ffef46 (single entity id request)
                id=015d9cba-4f53-4087-8317-7e49e5ffef46&id=015d9cba-4f53-4087-8317-7e49e5ffef47
                (multiple ids in the query param) .
            name(str): name query parameter. The list of system defined issue names. (Ex."BGP_Down") Examples:
                name=BGP_Down (single entity uuid requested) name=BGP_Down&name=BGP_Flap (multiple issue
                names separated by & operator) .
            priority(str): priority query parameter. Issue priority, possible values are P1, P2, P3, P4. `P1`: A
                critical issue that needs immediate attention and can have a wide impact on network
                operations. `P2`: A major issue that can potentially impact multiple devices or clients.
                `P3`: A minor issue that has a localized or minimal impact. `P4`: A warning issue that
                may not be an immediate problem but addressing it can optimize the network performance.
                .
            issue_enabled(bool): issueEnabled query parameter. The enablement status of the issue definition, either
                true or false.
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
            https://developer.cisco.com/docs/dna-center/#!get-the-count-of-system-defined-issue-definitions-based-on-provided-filters
        """
        check_type(headers, dict)
        check_type(device_type, str)
        check_type(profile_id, str)
        check_type(id, str)
        check_type(name, str)
        check_type(priority, str)
        check_type(issue_enabled, bool)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deviceType": device_type,
            "profileId": profile_id,
            "id": id,
            "name": name,
            "priority": priority,
            "issueEnabled": issue_enabled,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/systemIssueDefinitions/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cdb71530b2359e2bcb1e212aad71b6d_v3_2_3_0", json_data
        )

    def update_the_given_issue_by_updating_selected_fields(
        self,
        id,
        notes=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Updates selected fields in the given issue. Currently the only field that can be updated is 'notes' field. After
        this API returns success response, it may take few seconds for the issue details to be updated if the
        system is heavily loaded. Please use `GET /dna/data/api/v1/assuranceIssues/{id}` API to fetch the
        details of a particular issue and verify `updatedTime`. For detailed information about the usage of the
        API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        IssuesLifecycle-1.0.0-resolved.yaml.

        Args:
            notes(string): Issues's notes.
            id(str): id path parameter. The issue Uuid.
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
            https://developer.cisco.com/docs/dna-center/#!update-the-given-issue-by-updating-selected-fields
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "Accept-Language" in headers:
                check_type(headers.get("Accept-Language"), str)
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
            "notes": notes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator("jsd_bece53a182b45ffa4a1a435e_v3_2_3_0").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/assuranceIssues/{id}/update"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory("bpm_bece53a182b45ffa4a1a435e_v3_2_3_0", json_data)

    def resolve_the_given_lists_of_issues(
        self,
        issueIds=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Resolves the given list of issues. The response contains the list of issues which were successfully resolved as
        well as the issues which are failed to resolve. After this API returns success response, it may take few
        seconds for the issue status to be updated if the system is heavily loaded. Please use `GET
        /dna/data/api/v1/assuranceIssues/{id}` API to fetch the details of a particular issue and verify
        `updatedTime`. For detailed information about the usage of the API, please refer to the Open API
        specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-IssuesLifecycle-1.0.0-resolved.yaml.

        Args:
            issueIds(list): Issues's issueIds (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!resolve-the-given-lists-of-issues
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
            "issueIds": issueIds,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator("jsd_c10072541e94bd16f1aebffe32_v3_2_3_0").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/assuranceIssues/resolve"
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
            "bpm_c10072541e94bd16f1aebffe32_v3_2_3_0", json_data
        )

    def issues(
        self,
        ai_driven=None,
        device_id=None,
        end_time=None,
        issue_status=None,
        mac_address=None,
        priority=None,
        site_id=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Intent API to get a list of global issues, issues for a specific device, or issue for a specific client device's
        MAC address.   Deprecated since release Catalyst Center 3.2.1 Alternatives: GET
        /dna/data/api/v1/assuranceIssues POST /dna/data/api/v1/assuranceIssues/query   This API gets a list of
        issues in a time window.  By default, the time window is last 24 hours ending at the time the API is
        used.  This API supports the following filters: •  Site ID :  Get a list of global issues that have
        occurred in a specific site.  When a site ID value is not provided, the API returns global issues of
        site Global. •  Device ID :  Get a list of issues that have occurred for a specific device. •  Client
        MAC address :  Get a list of issues that have occurred for a specific client device, which is identified
        by the device's MAC address. Note: Mix and match of site ID, device ID, and client MAC address is not
        supported.  In addition to one of site ID, device ID, and client MAC address, additional filter for
        Priority (P1-P4), Issue Status (Active, Ignored, Resolved), and AI Driven (Yes/No) can be used. •
        Priority :  Get a list of issues that have specific priority value.  The default is to get all issues
        regardless of issue priority.  Supported priority is P1, P2, P3, and P4 (Support with site ID only) •
        Issue Status :  Get a list of issues that have specific status value.  Supported status is one of
        Ignored, Resolved, Active •  AI Driven :  Yes/No (Support with site ID only) The output is a list of
        issues.  Each issue has the following fields: • Issue ID • Issue Name • Issue Occurrence Count • Issue
        Status • Priority • Category • Last Occurrence Time   [' Deprecated since release Catalyst Center
        3.2.1\nAlternatives:\nGET /dna/data/api/v1/assuranceIssues\nPOST /dna/data/api/v1/assuranceIssues/query
        \n\n '].

        Args:
            start_time(int): startTime query parameter. Starting epoch time in milliseconds of query time window.
            end_time(int): endTime query parameter. Ending epoch time in milliseconds of query time window.
            site_id(str): siteId query parameter. Assurance UUID value of the site in the issue content.
            device_id(str): deviceId query parameter. Assurance UUID value of the device in the issue content.
            mac_address(str): macAddress query parameter. Client's device MAC address of the issue (format
                xx:xx:xx:xx:xx:xx).
            priority(str): priority query parameter. The issue's priority value: P1, P2, P3, or P4 (case
                insensitive) (Use only when macAddress and deviceId are not provided).
            issue_status(str): issueStatus query parameter. The issue's status value: ACTIVE, IGNORED, RESOLVED
                (case insensitive).
            ai_driven(str): aiDriven query parameter. The issue's AI driven value: YES or NO (case insensitive) (Use
                only when macAddress and deviceId are not provided).
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
            https://developer.cisco.com/docs/dna-center/#!issues
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(site_id, str)
        check_type(device_id, str)
        check_type(mac_address, str)
        check_type(priority, str)
        check_type(issue_status, str)
        check_type(ai_driven, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "siteId": site_id,
            "deviceId": device_id,
            "macAddress": mac_address,
            "priority": priority,
            "issueStatus": issue_status,
            "aiDriven": ai_driven,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/issues"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_aaef3b519ba8b9fb2cbf43b985_v3_2_3_0", json_data
        )

    def get_trend_analytics_data_of_issues(
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
        """Gets the trend analytics data related to issues based on given filters and group by field. This data can be used
        to find issue counts in different intervals over a period of time. For detailed information about the
        usage of the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        IssuesList-3.2.2-resolved.yaml.   Gets the trend analytics data related to issues based on given filters
        and group by field. This data can be used to find issue counts in different intervals over a period of
        time. The input payload contains the following fields Field Name Description startTime start time from
        which API queries the data set related to the resource. It must be specified in UNIX epochtime in
        milliseconds. Value is inclusive & the default is latest endTime end time to which API queries the data
        set related to the resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive
        & the default is latest trendInterval the trend time interval in minutues. This is a mantadory field.
        The possible values in minutes are  15, 30, 60 . When the start and end Time range is greater than 1
        day, the expected interval value is 60 minutes. groupBy specifies the attributes for grouping the
        issues. filters used to define one or more conditions. Only the data that satisfy these conditions will
        be taken into consideration during the aggregation calculation. attributes attributes are used for
        obtaining one or more field's data in addition to the aggregated data. The supported attributes are
        listed in  IssuesAnalyticsAttributeKey  model aggregateAttributes specifies the name of the attribute on
        which the aggregate function should be applied when querying the data. The supported attribute names are
        listed in   IssuesAnalyticsAggregateAttributeKey  model page contains  limit, offset and sortBy  fields.
        limit  Number of records to be returned in response,  offset  starting offset of data and  sortBy
        attribute name, order to sort.

        Args:
            aggregateAttributes(list): Issues's aggregateAttributes (list of objects).
            attributes(list): Issues's attributes (list of strings).
            endTime(integer): Issues's endTime.
            filters(list): Issues's filters (list of objects).
            groupBy(list): Issues's groupBy (list of strings).
            page(object): Issues's page.
            startTime(integer): Issues's startTime.
            trendInterval(string): Issues's trendInterval.
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
            https://developer.cisco.com/docs/dna-center/#!get-trend-analytics-data-of-issues
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "Accept-Language" in headers:
                check_type(headers.get("Accept-Language"), str)
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
                "jsd_fee1860b4d509585956565df54a91a_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/assuranceIssues/trendAnalytics"
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
            "bpm_fee1860b4d509585956565df54a91a_v3_2_3_0", json_data
        )

    def get_issue_enrichment_details(self, headers=None, **request_parameters):
        """Enriches a given network issue context (an issue id or end user’s Mac Address) with details about the issue(s),
        impacted hosts and suggested actions for remediation.

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
            https://developer.cisco.com/docs/dna-center/#!get-issue-enrichment-details
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

        e_url = "/dna/intent/api/v2/issue-enrichment-details"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e1d1e9c4be7581abd837e9ce02e29cc_v3_2_3_0", json_data
        )

    def get_issue_enrichment_details_v2(self, headers=None, **query_parameters):
        """Alias for `get_issue_enrichment_details <#catalystcentersdk.
        api.v3_2_3_0.issues.
        Issues.get_issue_enrichment_details>`_
        """
        return self.get_issue_enrichment_details(headers=headers, **query_parameters)

    def issue_enrichment_details(self, headers=None, **request_parameters):
        """Enriches a given network issue context (an issue id or end user’s Mac Address) with details about the issue(s),
        impacted hosts and suggested actions for remediation.

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
            https://developer.cisco.com/docs/dna-center/#!issue-enrichment-details
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

        e_url = "/dna/intent/api/v1/issueEnrichmentDetails"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a7fd3cc0defe587893a862afa6ed8664_v3_2_3_0", json_data
        )
