"""Cisco Catalyst Center Sensors API wrapper.

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


class Sensors:
    """Cisco Catalyst Center Sensors API (version: 3.2.3.0).

    Wraps the Catalyst Center Sensors
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Sensors
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

    def downloads_a_specific_icap_packet_capture_file(
        self,
        id,
        dirpath=None,
        save_file=None,
        filename=None,
        headers=None,
        **request_parameters
    ):
        """Downloads a specific ICAP packet capture file. For detailed information about the usage of the API, please refer
        to the Open API specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-icap-1.0.0-resolved.yaml.

        Args:
            id(str): id path parameter. The name of the packet capture file, as given by the GET /captureFiles API
                response. .
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
            https://developer.cisco.com/docs/dna-center/#!downloads-a-specific-i-c-a-p-packet-capture-file
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

        e_url = "/dna/data/api/v1/icap/captureFiles/{id}/download"
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
            "bpm_aeb8cee149c55a4a49506e07b6c4385_v3_2_3_0", json_data
        )

    def get_icap_configuration_intent_status_per_network_device(
        self, preview_activity_id, headers=None, **request_parameters
    ):
        """Get ICAP configuration intent status per network device.  Get ICAP configuration intent status per network
        device using the  previewActivityId , which is the task UUID obtained from the  POST
        /dna/intent/api/v1/icapSettings/configurationModels  task output.  This API must be used to check
        whether the submitted preview-approve workflow, identified by  previewActivityId , can be proceeded to
        the next step.  A failure in the status means the preview-approve workflow has conflicting configuration
        intent with other pending task(s) in the system, and the workflow should be discarded.  Try the preview-
        approve workflow again after pending task(s) in the system have been completed.    For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-ICAP_APIs-1.0.0-resolved.yaml .

        Args:
            preview_activity_id(str): previewActivityId path parameter. Activity ID value from the POST
                /dna/intent/api/v1/icapSettings/configurationModels task response.
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
            https://developer.cisco.com/docs/dna-center/#!get-i-c-a-p-configuration-intent-status-per-network-device
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
            "/dna/intent/api/v1/icapSettings/configurationModels/{pre"
            + "viewActivityId}/networkDeviceStatusDetails"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c6f94fda3501dbb0055d06e71e025_v3_2_3_0", json_data
        )

    def retrieves_the_total_number_of_packet_capture_files_matching_specified_criteria(
        self,
        type,
        ap_mac=None,
        client_mac=None,
        end_time=None,
        start_time=None,
        switch_mac=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the total number of packet capture files matching the specified criteria. For detailed information
        about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-icap-1.0.0-resolved.yaml.   Retrieves the total number of
        packet capture files matching the specified criteria. Packet capture file names follow the naming
        pattern  {macAddress}_{linkType}_{timestamp}.pcap . Each type of capture file can only be filtered based
        on specific MAC address types, as follows:         Capture Type   MAC Address Type           ANOMALY
        Client MAC or AP Base Radio MAC       FULL   Client MAC       ONBOARDING   Client MAC or AP Base Radio
        MAC       OTA   AP Base Radio MAC       WIRED   Switch Base MAC         At least one MAC address filter
        must be specified. An error is returned if the capture type and MAC address(es) specified are
        incompatible. For  WIRED  capture type, switchMac must be provided, but not clientMac and apMac. For
        ANOMALY  and  ONBOARDING  capture types, if both client MAC and AP MAC are specified, then only the
        capture files that match both criteria are counted.   Note that  ONBOARDING  capture files are created
        per-AP and contain onboarding packets for multiple clients attempting to connect to that AP. As a
        result, when  ONBOARDING  captures are filtered based on client MAC, the list of capture files returned
        are the ones that contain packets for the client of interest (but may also contain packets for other
        clients as well) and the count returned is for this list of files.

        Args:
            type(str): type query parameter. Capture Type.
            client_mac(str): clientMac query parameter. The macAddress of client .
            ap_mac(str): apMac query parameter. The base radio macAddress of the access point .
            switch_mac(str): switchMac query parameter. The base macAddress of the switch .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-total-number-of-packet-capture-files-matching-specified-criteria
        """
        check_type(headers, dict)
        check_type(type, str, may_be_none=False)
        check_type(client_mac, str)
        check_type(ap_mac, str)
        check_type(switch_mac, str)
        check_type(start_time, int)
        check_type(end_time, int)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "type": type,
            "clientMac": client_mac,
            "apMac": ap_mac,
            "switchMac": switch_mac,
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

        e_url = "/dna/data/api/v1/icap/captureFiles/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cbb6ff54e6605629a0a8a3555be72613_v3_2_3_0", json_data
        )

    def discards_the_icap_configuration_intent_by_activity_id(
        self, preview_activity_id, headers=None, **request_parameters
    ):
        """Discard the ICAP configuration intent by preview activity ID.  Discard the ICAP configuration intent using
        preview activity ID.  The preview activity ID was returned in TaskResponse's property "taskId" at the
        beginning of the preview-approve workflow.  Discarding the intent can only be applied to intent
        activities that have not been deployed.    Note :  ICAP type FULL, ONBOARDING, OTA, and SPECTRUM have
        duration.  A disable task is scheduled to be deployed when the duration expires.  This scheduled-
        disabled task cannot be discarded.  The feature can only be disabled by sending in a direct-deploy  POST
        /dna/intent/api/v1/icapSettings/{id}/deleteDeploy .  The path property  id  can be retrieved from  GET
        /dna/intent/api/v1/icapSettings     For detailed information about the usage of the API, please refer to
        the Open API specification document  https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-ICAP_APIs-1.0.0-resolved.yaml . .

        Args:
            preview_activity_id(str): previewActivityId path parameter. Activity ID value from the POST
                /dna/intent/api/v1/icapSettings/deviceConfigugrationModels task response.
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
            https://developer.cisco.com/docs/dna-center/#!discards-the-i-c-a-p-configuration-intent-by-activity-i-d
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
            "/dna/intent/api/v1/icapSettings/configurationModels/{pre"
            + "viewActivityId}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cd924ed4c4ed5fd3a463d5251896d31c_v3_2_3_0", json_data
        )

    def retrieves_the_devices_clis_of_the_icapintent(
        self, network_device_id, preview_activity_id, headers=None, **request_parameters
    ):
        """Returns the device's CLIs of the ICAP intent.  This API returns a list of CLI commands that will be applied at
        the network device with UUID in  networkDeviceId .  The UUID is the value of property  wlcId  in the
        intent object.    For detailed information about the usage of the API, please refer to the Open API
        specification document  https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-ICAP_APIs-1.0.0-resolved.yaml .

        Args:
            preview_activity_id(str): previewActivityId path parameter. Activity ID value from the POST
                /dna/intent/api/v1/icapSettings/deviceConfigugrationModels task response.
            network_device_id(str): networkDeviceId path parameter. Network device UUID, used in ICAP configuration
                intent wlcId property.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-devices-c-l-is-of-the-i-c-a-p-intent
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
            "/dna/intent/api/v1/icapSettings/configurationModels/{pre"
            + "viewActivityId}/networkDevices/{networkDeviceId}/config"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f657ae3d75ecd87e97be0a1571923_v3_2_3_0", json_data
        )

    def generates_the_devices_clis_of_the_icap_configuration_intent(
        self,
        network_device_id,
        preview_activity_id,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Generates the device's CLIs of the ICAP configuration intent.  This API triggers a task to generate a set of
        device CLIs of the ICAP intent for preview and approve.  The CLIs are for the network device with the
        UUID value defined in  wlcId  property of the intent object.  This API must be used prior to deploying
        the ICAP configuration intent to the device in the preview-approve workflow.  After deploying the
        configuration intent, generating intent CLIs is not available.  To get the device CLI list generated by
        this API, use  GET /dna/intent/api/v1/icapSettings/configurationModels/{previewActivityId}/networkDevice
        s/{networkDeviceId}/config .  The previewActivityId is the task UUID obtained from the  POST
        /dna/intent/api/v1/icapSettings/configurationModels  task output. The networkDeviceId is the UUID of the
        WLC device (wlcId)    For detailed information about the usage of the API, please refer to the Open API
        specification document  https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-ICAP_APIs-1.0.0-resolved.yaml . .

        Args:
            preview_activity_id(str): previewActivityId path parameter. activity from the POST
                /dna/intent/api/v1/icapSettings/configurationModels task response.
            network_device_id(str): networkDeviceId path parameter. device id (wlcId) from intent/api/v1/network-
                device.
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
            https://developer.cisco.com/docs/dna-center/#!generates-the-devices-c-l-is-of-the-i-c-a-p-configuration-intent
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(preview_activity_id, str, may_be_none=False)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "previewActivityId": preview_activity_id,
            "networkDeviceId": network_device_id,
        }
        _payload = {}
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ac98aec39c95c2d97532514ee9b9f3e_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/icapSettings/configurationModels/{pre"
            + "viewActivityId}/networkDevices/{networkDeviceId}/config"
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
            "bpm_ac98aec39c95c2d97532514ee9b9f3e_v3_2_3_0", json_data
        )

    def retrieves_the_count_of_deployed_icap_configurations_while_supporting_basic_filtering(
        self,
        capture_status,
        apid=None,
        capture_type=None,
        client_mac=None,
        wlc_id=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the count of deployed ICAP configurations while supporting basic filtering. For detailed information
        about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-ICAP_APIs-1.0.0-resolved.yaml.

        Args:
            capture_type(str): captureType query parameter. Catalyst Center ICAP type.
            capture_status(str): captureStatus query parameter. Catalyst Center ICAP status.
            client_mac(str): clientMac query parameter. The client device MAC address in ICAP configuration.
            apid(str): apId query parameter. The AP device's UUID.
            wlc_id(str): wlcId query parameter. The wireless controller device's UUID.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-count-of-deployed-i-c-a-p-configurations-while-supporting-basic-filtering
        """
        check_type(headers, dict)
        check_type(capture_type, str)
        check_type(capture_status, str, may_be_none=False)
        check_type(client_mac, str)
        check_type(apid, str)
        check_type(wlc_id, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "captureType": capture_type,
            "captureStatus": capture_status,
            "clientMac": client_mac,
            "apId": apid,
            "wlcId": wlc_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/icapSettings/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d122ab38d3758cba132f5e883d607c3_v3_2_3_0", json_data
        )

    def get_device_deployment_status_know_your_network(
        self,
        deploy_activity_id=None,
        limit=None,
        network_device_ids=None,
        offset=None,
        order=None,
        sort_by=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves ICAP configuration deployment status(s) per device based on filter criteria. For detailed information
        about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-ICAP_APIs-1.0.0-resolved.yaml.

        Args:
            deploy_activity_id(str): deployActivityId query parameter. activity from the /deploy task response.
            network_device_ids(str): networkDeviceIds query parameter. device ids, retrievable from the id attribute
                in intent/api/v1/network-device.
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
            https://developer.cisco.com/docs/dna-center/#!get-device-deployment-status-know-your-network
        """
        check_type(headers, dict)
        check_type(deploy_activity_id, str)
        check_type(network_device_ids, str)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, str)
        check_type(order, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deployActivityId": deploy_activity_id,
            "networkDeviceIds": network_device_ids,
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

        e_url = "/dna/intent/api/v1/icapSettings/deviceDeployments"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bebb4e5aaf8ba6e5284cdbeafb_v3_2_3_0", json_data
        )

    def retrieves_details_of_a_specific_icap_packet_capture_file(
        self, id, headers=None, **request_parameters
    ):
        """Retrieves details of a specific ICAP packet capture file. For detailed information about the usage of the API,
        please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        icap-1.0.0-resolved.yaml.

        Args:
            id(str): id path parameter. The name of the packet capture file, as given by the GET /captureFiles API
                response. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-details-of-a-specific-i-c-a-p-packet-capture-file
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

        e_url = "/dna/data/api/v1/icap/captureFiles/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_be18fdce21365e3ab6833963fefbaa96_v3_2_3_0", json_data
        )

    def get_device_deployment_status_count(
        self,
        deploy_activity_id=None,
        network_device_ids=None,
        headers=None,
        **request_parameters
    ):
        """Returns the count of device deployment status(s) based on filter criteria. For detailed information about the
        usage of the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        ICAP_APIs-1.0.0-resolved.yaml.

        Args:
            deploy_activity_id(str): deployActivityId query parameter. activity from the /deploy task response.
            network_device_ids(str): networkDeviceIds query parameter. device ids, retrievable from the id attribute
                in intent/api/v1/network-device.
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
            https://developer.cisco.com/docs/dna-center/#!get-device-deployment-status-count
        """
        check_type(headers, dict)
        check_type(deploy_activity_id, str)
        check_type(network_device_ids, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deployActivityId": deploy_activity_id,
            "networkDeviceIds": network_device_ids,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/icapSettings/deviceDeployments/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d04eba6a847958ae9c883f6957081ead_v3_2_3_0", json_data
        )

    def remove_the_icap_configuration_on_the_device_without_preview(
        self,
        id,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Remove the ICAP configuration from the device using  id  without preview-deploy.  Note : This API is obsoleted.
        Use  POST /dna/intent/api/v1/icapSettings/{id}/deleteDeploy .  The 2 APIs have identical functionality.
        Remove the ICAP configuration from the device using  id  without preview-deploy. The path parameter  id
        can be retrieved from  GET /dna/intent/api/v1/icapSettings  API. The response body of this API contains
        a task object with a taskId and a URL. Use the URL to check the task status.    Note :  ICAP FULL,
        ONBOARDING, OTA, and SPECTRUM configurations have a durationInMins property. A disable task is scheduled
        to remove the configuration from the device at the durationInMins time. To remove these ICAP features
        from device before the durationInMins time, it is best to use  GET /dna/intent/api/v1/icapSettings  API
        to retrieve the disable activity ID.  Use the obtained activity ID value ( disableActivityId ) in  POST
        /dna/intent/api/v1/icapSettings/configurationModels/{id}/deploy .  It may take a few minutes for the
        disableActivityId  value to appear in the output of  GET /dna/intent/api/v1/icapSettings .  Use  POST
        /dna/intent/api/v1/icapSettings/{id}/deleteDeploy  when  disableActivityId  cannot be located after 10
        minutes from enable completion time.    For detailed information about the usage of the API, please
        refer to the Open API specification document  https://github.com/cisco-en-programmability/catalyst-
        center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-ICAP_APIs-1.0.0-resolved.yaml . .

        Args:
            id(str): id path parameter. A unique ID of the deployed ICAP object, which can be obtained from **GET
                /dna/intent/api/v1/icapSettings**.
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
            https://developer.cisco.com/docs/dna-center/#!remove-the-i-c-a-p-configuration-on-the-device-without-preview
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
        _payload = {}
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e2ec291c2e775df3895aadc639713eea_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/icapSettings/deploy/{id}/deleteDeploy"
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
            "bpm_e2ec291c2e775df3895aadc639713eea_v3_2_3_0", json_data
        )

    def retrieves_the_spectrum_interference_devices_reports_sent_by_wlc_for_provided_ap_mac(
        self,
        ap_mac,
        end_time=None,
        limit=None,
        offset=None,
        start_time=None,
        time_sort_order=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the spectrum interference devices reports sent by WLC for provided AP Mac. For detailed information
        about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-icap-1.0.0-resolved.yaml.

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            ap_mac(str): apMac query parameter. The base ethernet macAddress of the access point .
            limit(int): limit query parameter. Maximum number of records to return.
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1.
            time_sort_order(str): timeSortOrder query parameter. The sort order of the field ascending or
                descending.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-spectrum-interference-devices-reports-sent-by-w-l-c-for-provided-a-p-mac
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(ap_mac, str, may_be_none=False)
        check_type(limit, int)
        check_type(offset, int)
        check_type(time_sort_order, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "apMac": ap_mac,
            "limit": limit,
            "offset": offset,
            "timeSortOrder": time_sort_order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/icap/spectrumInterferenceDeviceReports"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d1233df7e65d6b93c17b6568a9be4f_v3_2_3_0", json_data
        )

    def deploys_the_given_icap_configuration_intent_without_preview_and_approve(
        self,
        preview_description=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Deploys the given ICAP configuration intent without preview and approve.  ICAP Features Overview        APIs to
        manage Catalyst Center Assurance Intelligent Capture (ICAP) configurations. Catalyst Center (CatC) ICAP
        is a suite of features for troubleshooting client onboarding issues by capturing client Wi-Fi packets
        and statistics for offline analysis.      Supported ICAP Configurations :      ANOMALY :  This
        proactively monitors client onboarding issues. When an issue occurs, the AP device sends a client
        anomaly event, including a set of client Wi-Fi packets from the time of the event.   FULL :  This is to
        capture all Wi-Fi packets to and from a specific client MAC address.   ONBOARDING :  This captures
        client onboarding packets and client RF statistics with a 5-second granularity.   OTA :  This captures
        all Wi-Fi packets on a specific Wi-Fi band and channel. This feature can be used on up to two
        neighboring AP devices of an AP experiencing client-serving band or channel issues.   RFSTATS :  This
        captures both client and AP radio RF statistics with a 30-second granularity.   SPECTRUM :  This
        captures Wi-Fi Layer 2 signal strength and sources of interference across all supported Wi-Fi bands and
        channels.     ICAP Configuration Limitations :      The minimum duration for FULL packet capture is 30
        minutes, and the maximum is 8 hours.   The duration for OTA packet capture is 15 minutes   ONBOARDING
        packet capture supports 16 unique client MAC addresses with up to 3 WLCs for each client MAC address.
        The duration of capture can be set between 30 minutes and 8 hours.   SPECTRUM settings can be enabled on
        a maximum of 10 APs.  The duration of SPECTRUM data is 10 minutes.   RFSTATS settings:          At AP
        level, the feature can be enabled on a maximum of 1000 APs   At WLC level, the feature can be enabled
        only if Catalyst Center does not have more than 1,000 managed APs.   Mixture of AP and WLC level
        configuration is not supported.       OTA settings:          Prior to Catalyst Center 3.2.1, OTA
        supports up to 2 APs with both AP radio role sniffer, but 1 AP with AP mode sniffer. Consult AP
        hardware/software documetation about packet sniffing limitations. Minimum required AP software is IOSxe
        17.11.  AP running AireOS is not supported.  AP must be in client-serving mode prior to enabling OTA on
        the AP.  Changing an AP from client-serving to AP mode sniffer is not supported when the AP supports
        radio role sniffer.  Most AP platforms support radio role sniffer at radio slot 0.  The radio must be
        admin/oper UP and in client-serving mode prior to using ICAP OTA on the AP radio.  Changing 2 or more
        radios of 1 AP from client-serving mode to radio role sniffer is not supported.   Begining Catalyst
        Center 3.2.1, OTA allows to change up to 4 client-serving radios to sniffer mode across up to 2 AP
        devices.  It is best to select radios that support **radio role sniffer** to capture packets.  Any
        selected AP radio that does not support radio role sniffer will reset and change the AP from mode
        client-serving to mode sniffer.  The selected radios must be in client-serving, admin/oper UP, and
        managed by Catalyst Center. WARNING : Depending on the AP radio capability, enalbing OTA will reset
        either the AP or the radios.  The reset will force all clients who are associating with the AP radio to
        roam to other AP devices.  Clients WIFI network experiences will be impacted.       ANOMALY Settings:
        Highly recommend to apply at the WLC level, although AP-level ANOMALY is also supported. Applying
        ANOMALY at the AP level is intended for troubleshooting a specific client at a specific AP. Catalyst
        Center does not allow applying ANOMALY at both the WLC and AP levels simultaneously. The feature can be
        disabled on demand.   Mixture of AP and WLC level configuration is not supported.       Applying ICAP
        configurations at the WLC level is to apply the configurations to all AP profiles known to the Catalyst
        Center.  Wireless controller devices must be managed and in good health prior to use ICAP features for
        troubleshooting client WIFI issues.       Description   This API deploys the given ICAP intent without
        preview and approval. The response body contains a task object with a taskId and a URL for more
        information about the task. The deployment status of this ICAP intent can be found in the output of the
        URL.      FULL, ONBOARDING, OTA, and SPECTRUM configurations have a durationInMins field. A disable task
        is scheduled to remove the configuration from the device. Although the enablement of this ICAP
        configuration deployment has skipped the preview-deploy workflow, the disable task can still be
        previewed and deployed using the disableActivityId in the preview-deploy APIs to view the CLIs. See
        Step 3  and  Step 4  in the POST /dna/intent/api/v1/icapSettings/configurationModels description for
        more information. Use the  GET /dna/intent/api/v1/icapSettings?captureStatus=INPROGRESS  API to obtain
        the disableActivityId value. It may take a few minutes for the disableActivityId (a UUID string) to
        become available. When it is not available, the  POST
        /dna/intent/api/v1/icapSettings/deploy/{id}/deleteDeploy  API is not ready to remove the ICAP
        configuration from the device.        POST Body   Depending on the ICAP feature (captureType) that the
        list of required fields in POST body is different.  All object items in the POST body array must contain
        the same captureType value.  A mixture of captureType values in the POST body is not supported.  POST
        body array's item object must have the following fields:     ANOMALY :            At AP level:
        captureType=ANOMALY, wlcId, apId   At WLC level: captureType=ANOMALY, wlcId       FULL :
        captureType=FULL, wlcId, clientMac, durationInMins   ONBOARDING : captureType=ONBOARDING, wlcId,
        clientMac, durationInMins (30-480)   OTA : captureType=OTA, wlcId, apId, otaBand, otaChannel,
        otaChannelWidth, slots (1 element), durationInMins=15 (optional) Warning : Depending on the AP radio
        capability, enalbing OTA will reset either the AP or the radios.  The reset will force all clients who
        are associating with the AP radio to roam to other AP devices.  Clients WIFI network experiences will be
        impacted. Note :     Before CatC-3.2.1, POST body for OTA must satisfy the following:                The
        slots  property must be the radio slot number that supports  radio role sniffer  when AP has such radio.
        If AP does not have  radio role sniffer  capable radio, the AP will be converted to  mode sniffer  by an
        additional body property  otaMode: AP . The AP radio at  slots  must be admin UP, oper UP, serving
        clients, and managed by CatC.   The body must contain 1 object when the object has  otaMode: AP .   The
        body could contain up to 2 objects when both do not have  otaMode  property, but the 2 objects must have
        different  apId  value.   The  durationInMins  is always 15 (in minutes).       Beginning CatC-3.2.1,
        POST body for OTA could have up to 4 objects.  Each object defines a packet capturing radio on the AP.
        The object's property  apId  is the packet capturing AP's UUID value.  CatC allows up to 2 capturing
        APs.  Property  otaMode  will not have effect.  CatC determines to use either  radio role sniffer  or
        mode sniffer  depending on the packet capturing AP radio's capability.  Of up to 4 radios (objects) in
        the POST body, a radio object that does not support  radio role sniffer  will convert the whole AP to
        mode sniffer  regardless of other  radio role sniffer  capable radios of the same AP exist in the POST
        body.  When all radios of the same AP support  radio role sniffer , the AP will not be converted to
        mode sniffer , and the radios are converted to  radio role sniffer .  Prior to using OTA, the radio must
        be in client-serving mode, admin/oper UP, and managed by CatC. Some AP platforms, such as AP9130,
        support dual-radio which has 2 radios serving-client at the same WIFI band.  The 2 radios internally has
        primary-secondary relationship.  When dual-radio is enabled, both primary and secondary radios are in
        client-serving mode.  When dual-radio is disable, the secondary radio is in monitor mode, and the
        primary radio is client-serving.  For these kind of AP platforms, the body of OTA must NOT use  primary
        radio  when dual-radio is enable, and use  secondary radio  when dual-radio is disable.     RFSTATS :
        At AP level: captureType=RFSTATS, wlcId, apId   At WLC level: captureType=RFSTATS, wlcId       SPECTRUM
        : captureType=SPECTRUM, wlcId, apId, slots, durationInMins=10 (Optional)  .

        Args:
            preview_description(str): previewDescription query parameter. The ICAP intent's preview-deploy
                description string.
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
            https://developer.cisco.com/docs/dna-center/#!deploys-the-given-i-c-a-p-configuration-intent-without-preview-and-approve
        """
        check_type(headers, dict)
        check_type(payload, list)
        check_type(preview_description, str)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "previewDescription": preview_description,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_eea45fca32f5f12adc30a9d03c43ac6_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/icapSettings/deploy"
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
            "bpm_eea45fca32f5f12adc30a9d03c43ac6_v3_2_3_0", json_data
        )

    def retrieves_specific_client_statistics_over_specified_period_of_time(
        self,
        id,
        endTime=None,
        filters=None,
        page=None,
        startTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Retrieves the time series statistics of a specific client by applying complex filters. If startTime and endTime
        are not provided, the API defaults to the last 24 hours. For detailed information about the usage of the
        API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        icap-1.0.0-resolved.yaml.   Retrieves the time series statistics of a specific client by applying
        complex filters. If startTime and endTime are not provided, the API defaults to the last 24 hours.   The
        input payload contains the following fields,         Field Name   Description           startTime   The
        start time indicates when the API begins retrieving data related to the resource. It must be specified
        in the UNIX epoch time format, measured in milliseconds. This value is inclusive, and if left
        unspecified, the default is 1 day before the endTime.       endTime   The end time indicates the upper
        limit until which the API retrieves data related to the resource. It must be defined in the UNIX epoch
        time format, measured in milliseconds. This value is inclusive, and if left unspecified, the default is
        the latest available data.       filters   This is used to specify one or more conditions for filtering
        the queried data. Refer to  ClientStatsFilterField  model for the supported filters       page   It
        includes the  limit, offset, and timeSortOrder  fields.  limit  denotes the number of records to
        retrieve per page,  offset  signifies the initial data position, and  timeSortOrder  is used sort the
        response based on the timestamp either in ascending or descending order.      .

        Args:
            endTime(integer): Sensors's endTime.
            filters(list): Sensors's filters (list of objects).
            page(object): Sensors's page.
            startTime(integer): Sensors's startTime.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-specific-client-statistics-over-specified-period-of-time
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
            "filters": filters,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_cca68e89d0545dac01a8c7a461ac6e_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/icap/clients/{id}/stats"
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
            "bpm_cca68e89d0545dac01a8c7a461ac6e_v3_2_3_0", json_data
        )

    def retrieves_specific_radio_statistics_over_specified_period_of_time(
        self,
        id,
        endTime=None,
        filters=None,
        page=None,
        startTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Retrieves the time series statistics of a specific radio by applying complex filters. If startTime and endTime
        are not provided, the API defaults to the last 24 hours. For detailed information about the usage of the
        API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        icap-1.0.0-resolved.yaml.   Retrieves the time series statistics of a specific radio by applying complex
        filters. If startTime and endTime are not provided, the API defaults to the last 24 hours.   The input
        payload contains the following fields,         Field Name   Description           startTime   The start
        time indicates when the API begins retrieving data related to the resource. It must be specified in the
        UNIX epoch time format, measured in milliseconds. This value is inclusive, and if left unspecified, the
        default is 1 day before the endTime.       endTime   The end time indicates the upper limit until which
        the API retrieves data related to the resource. It must be defined in the UNIX epoch time format,
        measured in milliseconds. This value is inclusive, and if left unspecified, the default is the latest
        available data.       filters   This is used to specify one or more conditions for filtering the queried
        data. Refer to  RadioStatsFilterField  model for the supported filters       page   It includes the
        limit, offset, and timeSortOrder  fields.  limit  denotes the number of records to retrieve per page,
        offset  signifies the initial data position, and  timeSortOrder  is used sort the response based on the
        timestamp either in ascending or descending order.      .

        Args:
            endTime(integer): Sensors's endTime.
            filters(list): Sensors's filters (list of objects).
            page(object): Sensors's page.
            startTime(integer): Sensors's startTime.
            id(str): id path parameter. id is the composite key made of AP Base Ethernet macAddress and Radio Slot
                Id. Format apMac_RadioId .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-specific-radio-statistics-over-specified-period-of-time
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
            "filters": filters,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f71d0b2527b8cd13123f9a68cf3_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/icap/radios/{id}/stats"
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
            "bpm_f71d0b2527b8cd13123f9a68cf3_v3_2_3_0", json_data
        )

    def deploys_the_icap_configuration_intent_by_activity_id(
        self,
        preview_activity_id,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Deploys the ICAP configuration intent by preview activity ID.  Deploys the ICAP configuration intent using
        preview activity ID.  The preview activity ID was returned in property "taskId" of the TaskResponse
        object from  POST /dna/intent/api/v1/icapSettings/configurationModels .  This API must be used after the
        generating CLIs of the ICAP configuration intent task has been successfully completed.    Generating of
        device's CLIs for preview-approve is not available for this activity ID after using this POST API.  For
        detailed information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-ICAP_APIs-1.0.0-resolved.yaml . .

        Args:
            preview_activity_id(str): previewActivityId path parameter. Activity ID value from POST
                /dna/intent/api/v1/icapSettings/deviceConfigugrationModels task response.
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
            https://developer.cisco.com/docs/dna-center/#!deploys-the-i-c-a-p-configuration-intent-by-activity-i-d
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(preview_activity_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "previewActivityId": preview_activity_id,
        }
        _payload = {}
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_de1769e2886b5948b408100225b4a034_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/icapSettings/configurationModels/{pre"
            + "viewActivityId}/deploy"
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
            "bpm_de1769e2886b5948b408100225b4a034_v3_2_3_0", json_data
        )

    def create_sensor_test_template(
        self,
        apCoverage=None,
        connection=None,
        encryptionMode=None,
        locationInfoList=None,
        modelVersion=None,
        name=None,
        profiles=None,
        runNow=None,
        sensors=None,
        ssids=None,
        version=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Intent API to create a SENSOR test template with a new SSID, existing SSID, or both new and existing SSID.

        Args:
            apCoverage(list): Sensors's The WIFI bands where the test will be run (list of objects).
            connection(string): Sensors's connection type of test: WIRED, WIRELESS, BOTH.
            encryptionMode(string): Sensors's Encryption mode.
            locationInfoList(list): Sensors's Location information list (list of objects).
            modelVersion(integer): Sensors's Test template object model version (must be 2).
            name(string): Sensors's The sensor test template name.
            profiles(list): Sensors's Used for wired: the profileName, deviceType, vlan, testMacAddress to use
                authentication info, etc. (list of objects).
            runNow(string): Sensors's Run now (YES, NO).
            sensors(list): Sensors's Sensors (list of objects).
            ssids(list): Sensors's The list of SSIDs. Each SSID map has the ssid specific information as well as the
                test configurations to be used in each ssid.  Required at least 1 element (list of
                objects).
            version(integer): Sensors's The sensor test template version (must be 2).
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
            https://developer.cisco.com/docs/dna-center/#!create-sensor-test-template
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
            "version": version,
            "modelVersion": modelVersion,
            "connection": connection,
            "ssids": ssids,
            "profiles": profiles,
            "encryptionMode": encryptionMode,
            "runNow": runNow,
            "locationInfoList": locationInfoList,
            "sensors": sensors,
            "apCoverage": apCoverage,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f7dd6a6cf8d57499168aae05847ad34_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sensor"
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
            "bpm_f7dd6a6cf8d57499168aae05847ad34_v3_2_3_0", json_data
        )

    def sensors(self, site_id=None, headers=None, **request_parameters):
        """Intent API to get a list of SENSOR devices.

        Args:
            site_id(str): siteId query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!sensors
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

        e_url = "/dna/intent/api/v1/sensor"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cda740c5bdc92fd150c334d0e4e_v3_2_3_0", json_data
        )

    def delete_sensor_test(self, template_name, headers=None, **request_parameters):
        """Intent API to delete an existing SENSOR test template.

        Args:
            template_name(str): templateName query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!delete-sensor-test
        """
        check_type(headers, dict)
        check_type(template_name, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "templateName": template_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sensor"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a1c0ac4386555300b7f4a541d8dba625_v3_2_3_0", json_data
        )

    def lists_icap_packet_capture_files_matching_specified_criteria(
        self,
        type,
        ap_mac=None,
        client_mac=None,
        end_time=None,
        limit=None,
        offset=None,
        order=None,
        sort_by=None,
        start_time=None,
        switch_mac=None,
        headers=None,
        **request_parameters
    ):
        """Lists the ICAP packet capture (pcap) files matching the specified criteria. For detailed information about the
        usage of the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        icap-1.0.0-resolved.yaml.   Lists the ICAP packet capture (pcap) files matching the specified criteria.
        Packet capture file names follow the naming pattern  {macAddress}_{linkType}_{timestamp}.pcap .   Each
        type of capture file can only be filtered based on specific MAC address types, as follows:
        Capture Type   MAC Address Type           ANOMALY   Client MAC and/or AP Base Radio MAC       FULL
        Client MAC       ONBOARDING   Client MAC and/or AP Base Radio MAC       OTA   AP Base Radio MAC
        WIRED   Switch Base MAC         At least one MAC address filter must be specified. An error is returned
        if the capture type and MAC address(es) specified are incompatible. For  WIRED  capture type, switchMac
        must be provided, but not clientMac and apMac. For  ANOMALY  and  ONBOARDING  capture types, if both
        client MAC and AP MAC are specified, then only the capture files that match both criteria are returned.
        Note that  ONBOARDING  capture files are created per-AP and contain onboarding packets for multiple
        clients attempting to connect to that AP. As a result, when  ONBOARDING  captures are filtered based on
        client MAC, the list of capture files returned are the ones that contain packets for the client of
        interest (but may also contain packets for other clients as well). Therefore, it may be necessary to
        perform additional post-processing of the pcap file after retrieval. Common pcap analysis tools like
        Wireshark should also be able to easily display only packets for a certain MAC address.

        Args:
            type(str): type query parameter. Capture Type.
            client_mac(str): clientMac query parameter. The macAddress of client .
            ap_mac(str): apMac query parameter. The base radio macAddress of the access point .
            switch_mac(str): switchMac query parameter. The base macAddress of the switch .
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
            https://developer.cisco.com/docs/dna-center/#!lists-i-c-a-p-packet-capture-files-matching-specified-criteria
        """
        check_type(headers, dict)
        check_type(type, str, may_be_none=False)
        check_type(client_mac, str)
        check_type(ap_mac, str)
        check_type(switch_mac, str)
        check_type(start_time, int)
        check_type(end_time, int)
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
            "type": type,
            "clientMac": client_mac,
            "apMac": ap_mac,
            "switchMac": switch_mac,
            "startTime": start_time,
            "endTime": end_time,
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

        e_url = "/dna/data/api/v1/icap/captureFiles"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dbaeabc535e1a8587c92b593cefc3_v3_2_3_0", json_data
        )

    def retrieves_deployed_icap_configurations_while_supporting_basic_filtering(
        self,
        capture_status,
        apid=None,
        capture_type=None,
        client_mac=None,
        limit=None,
        offset=None,
        wlc_id=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves deployed ICAP configurations while supporting basic filtering.  This API returns deployed ICAP
        configurations while supporting basic filtering.  Property  captureStatus  must be one of the fofllowing
        values:      INPROGRESS : Configuration is deployed on the device. ICAP data is being sent by the device
        to the Catalyst Center. Supported filters include captureType, clientMac, apId, and wlcId.   COMPLETE :
        Configuration has been removed from device. The output information is used to retrieve ICAP data
        collected by the Catalyst Center when the features were enabled on the device. Supported filters include
        captureType, clientMac, apId, and wlcId.   SCHEDULED :  The configuration is scheduled to be deployed in
        the near future. Configurations in this state do not support filters, but pagination with limit and
        offset is supported.       Note : There are quite a few properties in the output.  Depending on the
        captureType  value that a few of the output properties do not have values.  Property 'name' in the
        output is not supported.    For detailed information about the usage of the API, please refer to the
        Open API specification document  https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-ICAP_APIs-1.0.0-resolved.yaml . .

        Args:
            capture_status(str): captureStatus query parameter. Catalyst Center ICAP status.
            capture_type(str): captureType query parameter. Catalyst Center ICAP type.
            client_mac(str): clientMac query parameter. The client device MAC address in ICAP configuration.
            apid(str): apId query parameter. The AP device's UUID.
            wlc_id(str): wlcId query parameter. The wireless controller device's UUID.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1.
            limit(int): limit query parameter. The number of records to show for this page.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-deployed-i-c-a-p-configurations-while-supporting-basic-filtering
        """
        check_type(headers, dict)
        check_type(capture_status, str, may_be_none=False)
        check_type(capture_type, str)
        check_type(client_mac, str)
        check_type(apid, str)
        check_type(wlc_id, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "captureStatus": capture_status,
            "captureType": capture_type,
            "clientMac": client_mac,
            "apId": apid,
            "wlcId": wlc_id,
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

        e_url = "/dna/intent/api/v1/icapSettings"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fdb9138f5aea88430fda95cbf865_v3_2_3_0", json_data
        )

    def creates_an_icap_configuration_intent_for_preview_approve(
        self,
        preview_description=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Creates an ICAP configuration intent for preview-approve.  This creates an ICAP configuration intent for preview
        approve workflow. The intent is not deployed to the device until further preview-approve APIs are
        applied. This API is the first step in the preview-approve workflow, which consists of several APIs.
        Skipping any API in the process is not recommended for a complete preview-approve use case.    For
        detailed information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-ICAP_APIs-1.0.0-resolved.yaml .    POST Body :  See
        /dna/intent/api/v1/icapSettings/deploy  description section for required properties of each captureType.
        The general guidline for preview-approve workflow is below     Step 1 : Use this API to POST the intent
        request.  The intent is not deployed to the device yet.  The TaskResponse body has the taskId UUID.
        This taskId value is the  previewAcitivityId  in all subsequent APIs.  After this POST API,  DELETE
        /dna/intent/api/v1/icapSettings/configurationModels/{previewActivityId}   API could be used at any step
        to discard/cancel the intent.  A discarded intent complete the prevew-approve workflow, and so ICAP
        intent is not applied to the device.  The API response body includes a URL which should be used to GET
        the status of the task.  The task must be successfully complete before proceeding to the next step.
        Otherwise, subsequent API in the preview-approve process may not be functioning well due to internal
        task timing.  A failed task at any step completes the preview-approve workflow process.        Step 2 :
        Use  GET
        /dna/intent/api/v1/icapSettings/configurationModels/{previewActivityId}/networkDeviceStatusDetails  to
        check potential conficts with existing ongoing tasks.  When the output shows conflicts, this preview-
        approve workflow must be discarded, complete or discard the ongoing conflicting tasks, and try a new
        preview-approve workflow.        Step 3 : Use  POST
        /dna/intent/api/v1/icapSettings/{previewActivityId}/networkDevices/{networkDeviceId}/config  to generate
        device CLIs for preview-approve.  The response body of this POST has a task ID and a URL for checking
        the task status.  Task must be successfully complete before using the GET API to view CLIs.  A failed
        task at this step completes the preview-approve workflow.  This POST API requires the networkDeviceId,
        which is the value of the property wlcId in the  POST /dna/intent/api/icapSettings/configurationModels .
        Multiple POST requests, each with different wlcId value of the same previewActivityId, could be applied
        to generate CLIs for the device.  Each POST returns a task and must be checked before proceeding to the
        next step.  It is not recommended to proceed when there is one ore more task failure in this step.  When
        there is any task failure at this step, use  DELETE
        /dna/intent/api/v1/icapSettings/configurationModels/{previewActivityId}  to discard activity.
        Step 4 : Use  GET /dna/intent/api/v1/icapSettings/configurationModels/{previewAcitivityId}/networkDevice
        s/{networkDeviceId}/config  to view the CLIs that will be applied to the device.        Step 5 : Use
        POST /dna/intent/api/v1/icapSettings/configurationModels/{previewActivityId}/deploy  to push the intent
        to device.  This complete the preview/approve workflow.  This POST returns a task, which should be
        checked for task status.          Note :  ONBOARDING, FULL, OTA, and SPECTRUM  have duration.  A
        "disable" task is scheduled to remove the ICAP intent at the duration expiring time.  Use  GET
        /dna/intent/api/v1/icapSettings  API to retrieve the "disable" task's preview activity ID, which could
        be used to preview the CLIs of the "disable" task.  However, steps of preview-approve workflow are not
        available after the duration has expired. .

        Args:
            preview_description(str): previewDescription query parameter. The ICAP intent's preview-deploy
                description string.
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
            https://developer.cisco.com/docs/dna-center/#!creates-an-i-c-a-p-configuration-intent-for-preview-approve
        """
        check_type(headers, dict)
        check_type(payload, list)
        check_type(preview_description, str)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "previewDescription": preview_description,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_cb38886d0236502783d431455e3fb880_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/icapSettings/configurationModels"
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
            "bpm_cb38886d0236502783d431455e3fb880_v3_2_3_0", json_data
        )

    def creates_an_icap_configuration_intent_to_remove_icap_rf_stats_or_anomaly_on_the_device_with_preview_approve(
        self,
        id,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Creates an ICAP configuration intent to remove ICAP RFSTATS or ANOMALY on the device with preview-approve.
        Creates an ICAP configuration intent to remove ICAP RFSTATS or ANOMALY configuration from the device
        with preview-approve.  The task has not been applied to the device yet.  Subsequent preview-approve
        workflow APIs must be used to complete the preview-approve process.  The path parameter 'id' can be
        retrieved from  GET /dna/intent/api/v1/icapSettings  API.    For detailed information about the usage of
        the API, please refer to the Open API specification document  https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        ICAP_APIs-1.0.0-resolved.yaml .    The response body has the taskId value for preview-approve.  The same
        workflow API steps (2 thru 5) as documented in the  POST
        /dna/intent/api/icapSettings/configurationModesl  apply after this POST API.    Note :  ICAP
        configuration types (captureType) FULL, ONBOADING, OTA, and SPECTRUM have duration 'durationInMins'.  A
        "disable" task has been deployed to be triggered at 'durantionInMins' time for removing the ICAP
        configuration on the device.  to remove the configuration from the device if a shorter capture duration
        is desired, use      POST /dna/intent/api/v1/icapSettings/{id}/deleteDeploy , or   POST
        /dna/intent/api/v1/icapSettings/configurationModels/{disableActivityId}/deleteDeploy      Although the
        disabled task is pre-scheduled for deployment, the CLIs are not yet available for preview. To preview
        the CLIs that will be applied to the device for the disabled task, use the same information in   Step 3
        and  Step 4  of the  POST /dna/intent/api/v1/icapSettings/configurationModels/deploy .  The disable
        task's activity ID value can be obtained from  GET /dna/intent/api/v1/icapSettings     The API does not
        have a request body. If your API utility needs request body to run the API, send an empty array [] in
        the body as a workaround. .

        Args:
            id(str): id path parameter. A unique ID of the deployed ICAP object, which can be obtained from **GET
                /dna/intent/api/v1/icapSettings**.
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
            https://developer.cisco.com/docs/dna-center/#!creates-an-i-c-a-p-configuration-intent-to-remove-i-c-a-p-r-f-s-t-a-t-s-or-a-n-o-m-a-l-y-on-the-device-with-preview-approve
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
        _payload = {}
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f924b4c27d18500b9b23df516b55c182_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/icapSettings/configurationModels/{id}" + "/deleteDeploy"
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
            "bpm_f924b4c27d18500b9b23df516b55c182_v3_2_3_0", json_data
        )

    def retrieves_the_spectrum_sensor_reports_sent_by_wlc_for_provided_ap_mac(
        self,
        ap_mac,
        data_type=None,
        end_time=None,
        limit=None,
        offset=None,
        start_time=None,
        time_sort_order=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the spectrum sensor reports sent by WLC for provided AP Mac. For detailed information about the usage
        of the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        icap-1.0.0-resolved.yaml.

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            ap_mac(str): apMac query parameter. The base ethernet macAddress of the access point .
            data_type(int): dataType query parameter. Data type reported by the sensor (Data Type: Description),
                (`0`: Duty Cycle),  (`1`: Max Power),  (`2`: Average Power),  (`3`: Max Power in dBm
                with adjusted base of +48),  (`4`: Average Power in dBm with adjusted base of +48),  .
            limit(int): limit query parameter. Maximum number of records to return.
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1.
            time_sort_order(str): timeSortOrder query parameter. The sort order of the field ascending or
                descending.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-spectrum-sensor-reports-sent-by-w-l-c-for-provided-a-p-mac
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(ap_mac, str, may_be_none=False)
        check_type(data_type, int)
        check_type(limit, int)
        check_type(offset, int)
        check_type(time_sort_order, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "apMac": ap_mac,
            "dataType": data_type,
            "limit": limit,
            "offset": offset,
            "timeSortOrder": time_sort_order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/icap/spectrumSensorReports"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ba6a51cf3055d0da0ba65e43b3030b6_v3_2_3_0", json_data
        )

    def edit_sensor_test_template(
        self,
        _id=None,
        actionInProgress=None,
        apCoverage=None,
        connection=None,
        encryptionMode=None,
        frequency=None,
        lastModifiedTime=None,
        location=None,
        locationInfoList=None,
        modelVersion=None,
        name=None,
        numAssociatedSensor=None,
        numNeighborAPThreshold=None,
        profiles=None,
        radioAsSensorRemoved=None,
        rssiThreshold=None,
        runNow=None,
        scheduleInDays=None,
        sensors=None,
        showWlcUpgradeBanner=None,
        siteHierarchy=None,
        ssids=None,
        startTime=None,
        status=None,
        templateName=None,
        testScheduleMode=None,
        version=None,
        wlans=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Intent API to deploy, schedule, or edit and existing SENSOR test template.

        Args:
            _id(string): Sensors's The sensor test template unique identifier, generated at test creation time.
            actionInProgress(string): Sensors's Indication of inprogress action.
            apCoverage(list): Sensors's The WIFI bands where the test will be run (list of objects).
            connection(string): Sensors's connection type of test: WIRED, WIRELESS, BOTH.
            encryptionMode(string): Sensors's Encryption mode.
            frequency(object): Sensors's Frequency of the test.
            lastModifiedTime(integer): Sensors's Last modify time.
            location(string): Sensors's Location string.
            locationInfoList(list): Sensors's Location information list (list of objects).
            modelVersion(integer): Sensors's Test template object model version (must be 2).
            name(string): Sensors's The sensor test template name, which is the same as in 'templateName'.
            numAssociatedSensor(integer): Sensors's Number of associated sensor.
            numNeighborAPThreshold(integer): Sensors's Number of neighboring AP threshold.
            profiles(list): Sensors's Used for wired: the profileName, deviceType, vlan, testMacAddress to use
                authentication info, etc. (list of objects).
            radioAsSensorRemoved(boolean): Sensors's Radio as sensor removed.
            rssiThreshold(integer): Sensors's RSSI threshold.
            runNow(string): Sensors's Run now (YES, NO).
            scheduleInDays(integer): Sensors's Bit-wise value of scheduled test days.
            sensors(list): Sensors's Sensors (list of objects).
            showWlcUpgradeBanner(boolean): Sensors's Show WLC upgrade banner.
            siteHierarchy(string): Sensors's Site hierarchy.
            ssids(list): Sensors's The list of SSIDs. Each SSID map has the ssid specific information as well as the
                test configurations to be used in each ssid.  Required at least 1 element (list of
                objects).
            startTime(integer): Sensors's Start time.
            status(string): Sensors's Status of the test (RUNNING, NOTRUNNING).
            templateName(string): Sensors's The test template name that is to be edited.
            testScheduleMode(string): Sensors's Test schedule mode (ONDEMAND, DEDICATED, SCHEDULED, CONTINUOUS,
                RUNNOW).
            version(integer): Sensors's The sensor test template version (must be 2).
            wlans(list): Sensors's WLANs list (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!edit-sensor-test-template
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
            "templateName": templateName,
            "name": name,
            "_id": _id,
            "version": version,
            "modelVersion": modelVersion,
            "startTime": startTime,
            "lastModifiedTime": lastModifiedTime,
            "numAssociatedSensor": numAssociatedSensor,
            "location": location,
            "siteHierarchy": siteHierarchy,
            "status": status,
            "connection": connection,
            "actionInProgress": actionInProgress,
            "frequency": frequency,
            "rssiThreshold": rssiThreshold,
            "numNeighborAPThreshold": numNeighborAPThreshold,
            "scheduleInDays": scheduleInDays,
            "wlans": wlans,
            "ssids": ssids,
            "profiles": profiles,
            "testScheduleMode": testScheduleMode,
            "showWlcUpgradeBanner": showWlcUpgradeBanner,
            "radioAsSensorRemoved": radioAsSensorRemoved,
            "encryptionMode": encryptionMode,
            "runNow": runNow,
            "locationInfoList": locationInfoList,
            "sensors": sensors,
            "apCoverage": apCoverage,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e2f9718de3d050819cdc6355a3a43200_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/AssuranceScheduleSensorTest"
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
            "bpm_e2f9718de3d050819cdc6355a3a43200_v3_2_3_0", json_data
        )

    def duplicate_sensor_test_template(
        self,
        newTemplateName=None,
        templateName=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Intent API to duplicate an existing SENSOR test template.

        Args:
            newTemplateName(string): Sensors's Destination test template name.
            templateName(string): Sensors's Source test template name.
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
            https://developer.cisco.com/docs/dna-center/#!duplicate-sensor-test-template
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
            "templateName": templateName,
            "newTemplateName": newTemplateName,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a352f6280e445075b3ea7cbf868c2d94_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sensorTestTemplate"
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
            "bpm_a352f6280e445075b3ea7cbf868c2d94_v3_2_3_0", json_data
        )

    def run_now_sensor_test(
        self,
        templateName=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Intent API to run a deployed SENSOR test.

        Args:
            templateName(string): Sensors's templateName.
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
            https://developer.cisco.com/docs/dna-center/#!run-now-sensor-test
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
            "templateName": templateName,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_cfadc5e4c912588389f4f63d2fb6e4ed_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sensor-run-now"
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
            "bpm_cfadc5e4c912588389f4f63d2fb6e4ed_v3_2_3_0", json_data
        )
