"""Cisco Catalyst Center Reports API wrapper.

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


class Reports:
    """Cisco Catalyst Center Reports API (version: 3.2.3.0).

    Wraps the Catalyst Center Reports
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Reports
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

    def delete_a_scheduled_report(self, report_id, headers=None, **request_parameters):
        """Delete a scheduled report configuration. Deletes the report executions also.

        Args:
            report_id(str): reportId path parameter. reportId of report.
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
            https://developer.cisco.com/docs/dna-center/#!delete-a-scheduled-report
        """
        check_type(headers, dict)
        check_type(report_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "reportId": report_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/data/reports/{reportId}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a6a151b68d450dfaf1e8a92e0f5cc68_v3_2_3_0", json_data
        )

    def get_a_scheduled_report(self, report_id, headers=None, **request_parameters):
        """Get scheduled report configuration by reportId.

        Args:
            report_id(str): reportId path parameter. reportId of report.
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
            https://developer.cisco.com/docs/dna-center/#!get-a-scheduled-report
        """
        check_type(headers, dict)
        check_type(report_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "reportId": report_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/data/reports/{reportId}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f9cb7c424b5502b4ad54ccbb1ca4f4_v3_2_3_0", json_data
        )

    def get_flexible_report_schedule_by_report_id(
        self, report_id, headers=None, **request_parameters
    ):
        """Get flexible report schedule by report ID.  ### Schedule types and examples  #### Run now:  ```json "schedule":
        {   "type": "SCHEDULE_NOW",   "timeZoneId": "Asia/Calcutta",   "scheduledServiceId":
        "3aa8ac39-1f9c-4059-ad56-d82b97234c3a",   "dateTime": 1711014210457 } ```  schedule Schedule details
        type Schedule type timeZoneId TimeZone for scheduler scheduledServiceId ScheduledServiceId (Unique UUID)
        dateTime Report start time (milliseconds since epoch)  #### Run later once: Run later at the time
        mentioned in `dateTime` field.  ```json "schedule": {   "type": "SCHEDULE_LATER",   "timeZoneId":
        "Asia/Calcutta",   "scheduledServiceId": "df7bf2c7-a502-44e3-a2c1-06f4973afe77",   "dateTime":
        1711014600000 } ```  schedule Schedule details type Schedule type timeZoneId TimeZone for scheduler
        scheduledServiceId ScheduledServiceId (Unique UUID) dateTime Report start time (milliseconds since
        epoch)  #### Run recurring (daily): Run every day at the time mentioned in `time` field.  ```json
        "schedule": {   "type": "SCHEDULE_RECURRENCE",   "timeZoneId": "Asia/Calcutta",   "scheduledServiceId":
        "48f93e8b-48ab-4134-bb28-4be5ea7465e1",   "startDate": 1711016497726,   "endDate": 0,
        "endAfterOccurrences": 0,   "time": 1711016700000,   "recurrence": {     "days": ["MONDAY", "TUESDAY",
        "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"],     "type": "WEEKLY",     "dayOfMonth": 0,
        "lastDayOfMonth": false   } } ```  schedule Schedule details type Schedule type timeZoneId TimeZone for
        scheduler scheduledServiceId ScheduledServiceId (Unique UUID) startDate Start date (milliseconds since
        epoch) endDate End date (milliseconds since epoch) endAfterOccurrences Number of occurrences time Report
        run time (milliseconds since epoch) recurrence Recurrence details  #### Run recurring (monthly): Run
        every month on `dayOfMonth` at `time`.  ```json "schedule": {   "type": "SCHEDULE_RECURRENCE",
        "timeZoneId": "Asia/Calcutta",   "scheduledServiceId": "b9562ddc-9874-46c7-89b9-896208ab011c",
        "startDate": 1711016604040,   "endDate": 0,   "endAfterOccurrences": 0,   "time": 1711017000000,
        "recurrence": {     "days": [],     "type": "MONTHLY",     "dayOfMonth": 21,     "lastDayOfMonth": false
        } } ```  schedule Schedule details type Schedule type timeZoneId TimeZone for scheduler
        scheduledServiceId ScheduledServiceId (Unique UUID) startDate Start date (milliseconds since epoch)
        endDate End date (milliseconds since epoch) endAfterOccurrences Number of occurrences time Report run
        time (milliseconds since epoch) recurrence Recurrence details  #### Run recurring (last day of month):
        Run on last day of every month at `time`.  ```json "schedule": {   "type": "SCHEDULE_RECURRENCE",
        "timeZoneId": "Asia/Calcutta",   "scheduledServiceId": "b9562ddc-9874-46c7-89b9-896208ab011c",
        "startDate": 1711016604040,   "endDate": 0,   "endAfterOccurrences": 0,   "time": 1711017000000,
        "recurrence": {     "days": [],     "type": "MONTHLY",     "dayOfMonth": 0,     "lastDayOfMonth": true
        } } ```  schedule Schedule details type Schedule type timeZoneId TimeZone for scheduler
        scheduledServiceId ScheduledServiceId (Unique UUID) startDate Start date (milliseconds since epoch)
        endDate End date (milliseconds since epoch) endAfterOccurrences Number of occurrences time Report run
        time (milliseconds since epoch) recurrence Recurrence details.

        Args:
            report_id(str): reportId path parameter. Id of the report.
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
            https://developer.cisco.com/docs/dna-center/#!get-flexible-report-schedule-by-report-id
        """
        check_type(headers, dict)
        check_type(report_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "reportId": report_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/flexible-report/schedule/{reportId}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a2a4b5bdcace5b55a5962ae85ff59d87_v3_2_3_0", json_data
        )

    def update_schedule_of_flexible_report(
        self,
        report_id,
        schedule=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Update schedule of flexible report.  ### Schedule types and examples  #### Run now: ```json "schedule": {
        "type": "SCHEDULE_NOW",   "timeZoneId": "Asia/Calcutta",   "scheduledServiceId":
        "3aa8ac39-1f9c-4059-ad56-d82b97234c3a",   "dateTime": 1711014210457 } ``` schedule – Schedule details
        type – Schedule type timeZoneId – TimeZone for scheduler scheduledServiceId – ScheduledServiceId (Unique
        UUID) dateTime – Report start time (milliseconds since epoch)  #### Run later once: Run later at the
        time mentioned in `dateTime` field. ```json "schedule": {   "type": "SCHEDULE_LATER",   "timeZoneId":
        "Asia/Calcutta",   "scheduledServiceId": "df7bf2c7-a502-44e3-a2c1-06f4973afe77",   "dateTime":
        1711014600000 } ``` schedule – Schedule details type – Schedule type timeZoneId – TimeZone for scheduler
        scheduledServiceId – ScheduledServiceId (Unique UUID) dateTime – Report start time (milliseconds since
        epoch)  #### Run recurring (daily): Run every day at the time mentioned in `time` field. ```json
        "schedule": {   "type": "SCHEDULE_RECURRENCE",   "timeZoneId": "Asia/Calcutta",   "scheduledServiceId":
        "48f93e8b-48ab-4134-bb28-4be5ea7465e1",   "startDate": 1711016497726,   "endDate": 0,
        "endAfterOccurrences": 0,   "time": 1711016700000,   "recurrence": {     "days": ["MONDAY", "TUESDAY",
        "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"],     "type": "WEEKLY",     "dayOfMonth": 0,
        "lastDayOfMonth": false   } } ``` schedule – Schedule details type – Schedule type timeZoneId – TimeZone
        for scheduler scheduledServiceId – ScheduledServiceId (Unique UUID) startDate – Start date (milliseconds
        since epoch) endDate – End date (milliseconds since epoch) endAfterOccurrences – Number of occurrences
        time – Time of day to run report (milliseconds since epoch) recurrence – Recurrence details  #### Run
        recurring (monthly on specific date): Run every month on `dayOfMonth` at the time mentioned in `time`.
        ```json "schedule": {   "type": "SCHEDULE_RECURRENCE",   "timeZoneId": "Asia/Calcutta",
        "scheduledServiceId": "b9562ddc-9874-46c7-89b9-896208ab011c",   "startDate": 1711016604040,   "endDate":
        0,   "endAfterOccurrences": 0,   "time": 1711017000000,   "recurrence": {     "days": [],     "type":
        "MONTHLY",     "dayOfMonth": 21,     "lastDayOfMonth": false   } } ``` schedule – Schedule details type
        – Schedule type timeZoneId – TimeZone for scheduler scheduledServiceId – ScheduledServiceId (Unique
        UUID) startDate – Start date (milliseconds since epoch) endDate – End date (milliseconds since epoch)
        endAfterOccurrences – Number of occurrences time – Time of day to run report (milliseconds since epoch)
        recurrence – Recurrence details  #### Run recurring (last day of every month): Run on the last day of
        every month at the time mentioned in `time`. ```json "schedule": {   "type": "SCHEDULE_RECURRENCE",
        "timeZoneId": "Asia/Calcutta",   "scheduledServiceId": "b9562ddc-9874-46c7-89b9-896208ab011c",
        "startDate": 1711016604040,   "endDate": 0,   "endAfterOccurrences": 0,   "time": 1711017000000,
        "recurrence": {     "days": [],     "type": "MONTHLY",     "dayOfMonth": 0,     "lastDayOfMonth": true
        } } ``` schedule – Schedule details type – Schedule type timeZoneId – TimeZone for scheduler
        scheduledServiceId – ScheduledServiceId (Unique UUID) startDate – Start date (milliseconds since epoch)
        endDate – End date (milliseconds since epoch) endAfterOccurrences – Number of occurrences time – Time of
        day to run report (milliseconds since epoch) recurrence – Recurrence details.

        Args:
            schedule(): Reports's Schedule information.
            report_id(str): reportId path parameter. Id of the report.
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
            https://developer.cisco.com/docs/dna-center/#!update-schedule-of-flexible-report
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(report_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "reportId": report_id,
        }
        _payload = {
            "schedule": schedule,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a93d01238de0537dbb3d358f9cce0bd2_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/flexible-report/schedule/{reportId}"
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
            "bpm_a93d01238de0537dbb3d358f9cce0bd2_v3_2_3_0", json_data
        )

    def get_views_for_a_given_view_group(
        self, view_group_id, headers=None, **request_parameters
    ):
        """Gives a list of summary of all views in a viewgroup. Use "Get all view groups" API to get the viewGroupIds
        (required as a query param for this API) for available viewgroups.

        Args:
            view_group_id(str): viewGroupId path parameter. viewGroupId of viewgroup.
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
            https://developer.cisco.com/docs/dna-center/#!get-views-for-a-given-view-group
        """
        check_type(headers, dict)
        check_type(view_group_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "viewGroupId": view_group_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/data/view-groups/{viewGroupId}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c5879612ddc05cd0a0de09d29da4907e_v3_2_3_0", json_data
        )

    def download_report_content(
        self,
        execution_id,
        report_id,
        dirpath=None,
        save_file=None,
        filename=None,
        headers=None,
        **request_parameters
    ):
        """Returns report content. Save the response to a file by converting the response data as a blob and setting the
        file format available from content-disposition response header.

        Args:
            report_id(str): reportId path parameter. reportId of report.
            execution_id(str): executionId path parameter. executionId of report execution.
            dirpath(str): Directory absolute path. Defaults to os.getcwd().
            save_file(bool): Enable or disable automatic file creation of
                raw response.
            filename(str): The filename used to save the download file.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            DownloadResponse: The DownloadResponse wrapper. Wraps the urllib3.response.HTTPResponse. For more
            information check the `urlib3 documentation <https://urllib3.readthedocs.io/en/latest/reference/urllib3.response.html>`_

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Catalyst Center cloud returns an error.
            DownloadFailure: If was not able to download the raw
            response to a file.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!download-report-content
        """
        check_type(headers, dict)
        check_type(report_id, str, may_be_none=False)
        check_type(execution_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "reportId": report_id,
            "executionId": execution_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/data/reports/{reportId}/executions/{e" + "xecutionId}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url,
                params=_params,
                headers=_headers,
                stream=True,
                dirpath=dirpath,
                save_file=save_file,
                filename=filename,
            )
        else:
            json_data = self._session.get(
                endpoint_full_url,
                params=_params,
                stream=True,
                dirpath=dirpath,
                save_file=save_file,
                filename=filename,
            )

        return self._object_factory(
            "bpm_b2790cdb5abf98c8e00011de86a4_v3_2_3_0", json_data
        )

    def get_all_view_groups(self, headers=None, **request_parameters):
        """Gives a list of summary of all view groups.

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
            https://developer.cisco.com/docs/dna-center/#!get-all-view-groups
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

        e_url = "/dna/intent/api/v1/data/view-groups"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bbff833d5d5756698f4764a9d488cc98_v3_2_3_0", json_data
        )

    def get_view_details_for_a_given_view_group_and_view(
        self, view_group_id, view_id, headers=None, **request_parameters
    ):
        """Gives complete information of the view that is required to configure a report. Use "Get views for a given view
        group" API to get the viewIds  (required as a query param for this API) for available views.

        Args:
            view_group_id(str): viewGroupId path parameter. viewGroupId of viewgroup.
            view_id(str): viewId path parameter. view id of view.
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
            https://developer.cisco.com/docs/dna-center/#!get-view-details-for-a-given-view-group_-view
        """
        check_type(headers, dict)
        check_type(view_group_id, str, may_be_none=False)
        check_type(view_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "viewGroupId": view_group_id,
            "viewId": view_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/data/view-" + "groups/{viewGroupId}/views/{viewId}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d1944177c95598ebd1986582dc8069a_v3_2_3_0", json_data
        )

    def get_list_of_scheduled_reports(
        self, view_group_id=None, view_id=None, headers=None, **request_parameters
    ):
        """Get list of scheduled report configurations.

        Args:
            view_group_id(str): viewGroupId query parameter. viewGroupId of viewgroup for report.
            view_id(str): viewId query parameter. viewId of view for report.
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
            https://developer.cisco.com/docs/dna-center/#!get-list-of-scheduled-reports
        """
        check_type(headers, dict)
        check_type(view_group_id, str)
        check_type(view_id, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "viewGroupId": view_group_id,
            "viewId": view_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/data/reports"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d89e1c3e150ef9faaff44fa483de5_v3_2_3_0", json_data
        )

    def create_or_schedule_a_report(
        self,
        dataCategory=None,
        deliveries=None,
        name=None,
        schedule=None,
        tags=None,
        view=None,
        viewGroupId=None,
        viewGroupVersion=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Create/Schedule a report configuration. Use "Get view details for a given view group & view" API to get the
        metadata required to configure a report.   This API is used to generate a report using the metadata
        available for the report. The request body contains the following fields. name (string, required) : Name
        of the report viewGroupId (string, required) : viewGroupId of the viewgroup for the report view
        (map, required) : Filters, format, fields(for non-pdf reports), for the report are mentioned in this
        object. schedule (map, required) : A map containing the schedule information of the report. deliveries
        (array, required) : Array of delivery channels to be used for the report viewGroupVersion
        (string, required) : version of viewgroup for the report tags (array of strings, optional): array of
        tags for report   Example :    {   "name": "Sample Inventory report",   "viewGroupId":
        "d1f59396-bfd7-4de6-829f-0b3abcc7bd17",   "view": {     "viewId":
        "910037b4-91f5-4ad7-b8cf-32f9d3ee43b1",     "name": "All Data",     "format": {       "name": "CSV",
        "formatType": "CSV"     },     "filters": [       {         "name": "Location",         "displayName":
        "Location",         "type": "MULTI_SELECT_TREE",         "value": []       },       {         "name":
        "DeviceFamily",         "displayName": "Device Family",         "type": "MULTI_SELECT",         "value":
        []       },       {         "name": "DeviceType",         "displayName": "Device Type",         "type":
        "MULTI_SELECT",         "value": []       },       {         "name": "SoftwareVersion",
        "displayName": "Software  Version",         "type": "MULTI_SELECT",         "value": []       }     ],
        "fieldGroups": [       {         "fieldGroupName": "inventoryAllData",         "fieldGroupDisplayName":
        "All Data",         "fields": [           {             "name": "type",             "displayName":
        "Device Type"           },           {             "name": "hostname",             "displayName":
        "Device Name"           },           {             "name": "ipAddress",             "displayName": "IP
        Address"           }         ]       }     ]   },   "schedule": {     "type": "SCHEDULE_NOW",
        "timeZoneId": "Asia/Calcutta"   },   "deliveries": [     {       "type": "DOWNLOAD"     }   ],
        "viewGroupVersion": "2.0.0",   "tags": [],   "dataCategory": "Inventory" }   Schedule types and
        examples:   Run now :   {   "type": "SCHEDULE_NOW",   "timeZoneId": "Asia/Calcutta" }   Run later once:
        Run later at the time mentioned in "dateTime" field.   {   "type": "SCHEDULE_LATER",   "dateTime":
        1687945010004,   "timeZoneId": "Asia/Calcutta" }   Run recurring: Run everyday at time mentioned in
        "time" field   {   "type": "SCHEDULE_RECURRENCE",   "time": 1687945010004,   "startDate": 1687945010004,
        "timeZoneId": "Asia/Calcutta",   "recurrence": {     "type": "WEEKLY",     "days": [       "MONDAY",
        "TUESDAY",       "WEDNESDAY",       "THURSDAY",       "FRIDAY",       "SATURDAY",       "SUNDAY"     ]
        } }   Run Recurring: Run every month at date mentioned in "dayOfMonth" field and at time mentioned in
        "time" field   {   "type": "SCHEDULE_RECURRENCE",   "time": 1687945010004,   "startDate": 1687945010004,
        "timeZoneId": "Asia/Calcutta",   "recurrence": {     "type": "MONTHLY",     "dayOfMonth": 12,
        "lastDayOfMonth": false   } }   Run Recurring: Run last day of every month at time mentioned in "time"
        field   {   "type": "SCHEDULE_RECURRENCE",   "time": 1687945010004,   "startDate": 1687945010004,
        "timeZoneId": "Asia/Calcutta",   "recurrence": {     "type": "MONTHLY",     "dayOfMonth": 12,
        "lastDayOfMonth": true   } }   Delivery types and examples:   Deliveries field's value has to be an
        array with only one object corresponding to a delivery type.   Download: Mention this type by default if
        no other delivery type is selected.   [   {     "type": "DOWNLOAD"   } ]   Email:  Sends email
        notification to the email addresses mentioned in emailAddresses field on change in statuses of report
        mentioned in notify array field. Mention emailAttach as true if report file need to be attached in the
        email on completion. Email attachment is supported only for pdf format with a file size less than 20mb.
        [   {     "type": "NOTIFICATION",     "notificationEndpoints": [       {         "type": "EMAIL",
        "emailAddresses": ["abc@xyz.com"]       }     ],     "emailAttach": false,     "notify": ["IN_QUEUE",
        "IN_PROGRESS", "COMPLETED"]   } ]   Webhook: Triggers webhook with id mentioned in webhookId field   [
        {     "type": "WEBHOOK",     "webhookId": "e17e1659-760f-4f57-9bb2-bb13977bd305"   } ]      .

        Args:
            dataCategory(string): Reports's category of viewgroup for the report.
            deliveries(list): Reports's Array of available delivery channels (list of any objects).
            name(string): Reports's report name.
            schedule(): Reports's schedule.
            tags(list): Reports's array of tags for report (list of strings).
            view(object): Reports's view.
            viewGroupId(string): Reports's viewGroupId of the viewgroup for the report.
            viewGroupVersion(string): Reports's version of viewgroup for the report.
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
            https://developer.cisco.com/docs/dna-center/#!create-or-schedule-a-report
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
            "tags": tags,
            "deliveries": deliveries,
            "name": name,
            "schedule": schedule,
            "view": view,
            "viewGroupId": viewGroupId,
            "viewGroupVersion": viewGroupVersion,
            "dataCategory": dataCategory,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_fa310ab095148bdb00d7d3d5e1676_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/data/reports"
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
            "bpm_fa310ab095148bdb00d7d3d5e1676_v3_2_3_0", json_data
        )

    def executing_the_flexible_report(
        self, report_id, headers=None, **request_parameters
    ):
        """This API is used for executing the report.  ### Process status and request status types and meanings  ####
        Process status: `IN_PROGRESS` – Report generation is in progress `SUCCESS` – Report is successfully
        generated `FAILURE` – Report generation failed `CANCELLED` – Report generation is cancelled `SUSPENDED`
        – Report generation is suspended `NOTIFIED` – Subsystem is notified to prepare data needed for report
        generation `PARTIALLY_COMPLETED` – Report generation is partially completed `RETRY_FAILED` – Report
        generation retry failed `RETRY_CANCELLED` – Report generation retry is cancelled  #### Request status:
        `ACCEPT` – Report generation request is accepted `REJECT` – Report generation request is rejected  ###
        Errors and Warnings Example ```json "errors": [   "Error while fetching Report Execution Details" ],
        "warnings": [   "Deprecated symbol used" ] ```.

        Args:
            report_id(str): reportId path parameter. Id of the Report.
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
            https://developer.cisco.com/docs/dna-center/#!executing-the-flexible-report
        """
        check_type(headers, dict)
        check_type(report_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "reportId": report_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/flexible-" + "report/report/{reportId}/execute"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory("bpm_c2c0c5f9fa208985865f05eca_v3_2_3_0", json_data)

    def get_execution_id_by_report_id(
        self, report_id, headers=None, **request_parameters
    ):
        """Get Execution ID by Report ID.  ### Process status and request status types and meanings  #### Process status:
        `IN_PROGRESS` – Report generation is in progress `SUCCESS` – Report is successfully generated `FAILURE`
        – Report generation failed `CANCELLED` – Report generation is cancelled `SUSPENDED` – Report generation
        is suspended `NOTIFIED` – Subsystem is notified to prepare data needed for report generation
        `PARTIALLY_COMPLETED` – Report generation is partially completed `RETRY_FAILED` – Report generation
        retry failed `RETRY_CANCELLED` – Report generation retry is cancelled  #### Request status: `ACCEPT` –
        Report generation request is accepted `REJECT` – Report generation request is rejected  ### Errors and
        Warnings Example ```json "errors": [   "Error while fetching Report Execution Details" ], "warnings": [
        "Deprecated symbol used" ] ```.

        Args:
            report_id(str): reportId path parameter. Id of the report.
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
            https://developer.cisco.com/docs/dna-center/#!get-execution-id-by-report-id
        """
        check_type(headers, dict)
        check_type(report_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "reportId": report_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/flexible-" + "report/report/{reportId}/executions"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_edf3c4d58586fb15a5b62256f94a6_v3_2_3_0", json_data
        )

    def get_all_flexible_report_schedules(self, headers=None, **request_parameters):
        """Get all flexible report schedules.  ### Schedule types and examples  #### Run now: ```json {   "reportId":
        "26882b09-7d07-47ca-95a4-d51024b4a6f4",   "schedule": {     "type": "SCHEDULE_NOW",     "timeZoneId":
        "Asia/Calcutta",     "scheduledServiceId": "b28beccf-da77-4331-b87b-7075ae40ca87",     "dateTime":
        1710731294709   },   "reportName": "Flexible Report Mar 18 2024 08:37 am" } ``` reportId – Report ID
        (UUID) schedule – Schedule details type – Schedule type timeZoneId – Time zone for scheduler
        scheduledServiceId – Scheduled service ID (UUID) dateTime – Report start time (epoch millis) reportName
        – Name of the report  #### Run later once: Run later at the time mentioned in `dateTime`. ```json {
        "reportId": "52ef84fe-c3d1-4628-b66d-6a2186893396",   "schedule": {     "type": "SCHEDULE_LATER",
        "timeZoneId": "Asia/Calcutta",     "scheduledServiceId": "df7bf2c7-a502-44e3-a2c1-06f4973afe77",
        "dateTime": 1711014600000   },   "reportName": "Flexible Report Mar 21 2024 03:13 pm" } ``` reportId,
        schedule, type, timeZoneId, scheduledServiceId, dateTime, reportName – as above  #### Run recurring
        (daily): Run every day at the time mentioned in `time`. ```json {   "reportId":
        "8d2c9b20-45b1-439d-bff3-60d807fd1fb8",   "schedule": {     "type": "SCHEDULE_RECURRENCE",
        "timeZoneId": "Asia/Calcutta",     "scheduledServiceId": "48f93e8b-48ab-4134-bb28-4be5ea7465e1",
        "startDate": 1711016497726,     "endDate": 0,     "endAfterOccurrences": 0,     "time": 1711016700000,
        "recurrence": {       "days": ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY",
        "SUNDAY"],       "type": "WEEKLY",       "dayOfMonth": 0,       "lastDayOfMonth": false     }   },
        "reportName": "Flexible Report Mar 21 2024 03:45 pm" } ``` Includes recurrence details with weekly
        frequency  #### Run recurring (monthly on a specific date): ```json {   "reportId":
        "ae1472b0-6987-4689-90e9-6be835cd5811",   "schedule": {     "type": "SCHEDULE_RECURRENCE",
        "timeZoneId": "Asia/Calcutta",     "scheduledServiceId": "b9562ddc-9874-46c7-89b9-896208ab011c",
        "startDate": 1711016604040,     "endDate": 0,     "endAfterOccurrences": 0,     "time": 1711017000000,
        "recurrence": {       "days": [],       "type": "MONTHLY",       "dayOfMonth": 21,
        "lastDayOfMonth": false     }   },   "reportName": "Flexible Report Mar 21 2024 03:51 pm" } ``` Monthly
        schedule on day 21 of each month  #### Run recurring (last day of month): ```json {   "reportId":
        "bd9bd33b-678c-4d49-af43-cebe1e9a0869",   "schedule": {     "type": "SCHEDULE_RECURRENCE",
        "timeZoneId": "Asia/Calcutta",     "scheduledServiceId": "87d9f680-d715-45ec-a7c6-68d1d954c82f",
        "startDate": 1711016658239,     "endDate": 0,     "endAfterOccurrences": 0,     "time": 1711016773000,
        "recurrence": {       "days": [],       "type": "MONTHLY",       "dayOfMonth": 0,
        "lastDayOfMonth": true     }   },   "reportName": "Flexible Report Mar 21 2024 03:53 pm" } ``` Executes
        on last day of each month.

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
            https://developer.cisco.com/docs/dna-center/#!get-all-flexible-report-schedules
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

        e_url = "/dna/data/api/v1/flexible-report/schedules"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dfd5cfd8a985505aaa606be4599319f_v3_2_3_0", json_data
        )

    def get_all_execution_details_for_a_given_report(
        self, report_id, headers=None, **request_parameters
    ):
        """Get details of all executions for a given report.

        Args:
            report_id(str): reportId path parameter. reportId of report.
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
            https://developer.cisco.com/docs/dna-center/#!get-all-execution-details-for-a-given-report
        """
        check_type(headers, dict)
        check_type(report_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "reportId": report_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/data/reports/{reportId}/executions"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a4b1ca0320185570bc12da238f0e88bb_v3_2_3_0", json_data
        )

    def download_flexible_report(
        self,
        execution_id,
        report_id,
        dirpath=None,
        save_file=None,
        filename=None,
        headers=None,
        **request_parameters
    ):
        """This is used to download the flexible report. The API returns report content. Save the response to a file by
        converting the response data as a blob and setting the file format available from content-disposition
        response header.

        Args:
            report_id(str): reportId path parameter. Id of the report.
            execution_id(str): executionId path parameter. Id of execution.
            dirpath(str): Directory absolute path. Defaults to
                os.getcwd().
            save_file(bool): Enable or disable automatic file creation of
                raw response.
            filename(str): The filename used to save the download
                file.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            DownloadResponse: The DownloadResponse wrapper. Wraps the urllib3.response.HTTPResponse. For more
            information check the `urlib3 documentation <https://urllib3.readthedocs.io/en/latest/reference/urllib3.response.html>`_

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Catalyst Center cloud returns an error.
            DownloadFailure: If was not able to download the raw
            response to a file.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!download-flexible-report
        """
        check_type(headers, dict)
        check_type(report_id, str, may_be_none=False)
        check_type(execution_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "reportId": report_id,
            "executionId": execution_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/data/api/v1/flexible-"
            + "report/report/content/{reportId}/{executionId}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url,
                params=_params,
                headers=_headers,
                stream=True,
                dirpath=dirpath,
                save_file=save_file,
                filename=filename,
            )
        else:
            json_data = self._session.get(
                endpoint_full_url,
                params=_params,
                stream=True,
                dirpath=dirpath,
                save_file=save_file,
                filename=filename,
            )

        return self._object_factory(
            "bpm_fc4acf45953f5b68be682c3c5906bf14_v3_2_3_0", json_data
        )
