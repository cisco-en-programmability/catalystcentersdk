"""Cisco Catalyst Center Industrial Configuration API wrapper.

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


class IndustrialConfiguration:
    """Cisco Catalyst Center Industrial Configuration API (version: 3.2.3.0).

    Wraps the Catalyst Center Industrial Configuration
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new IndustrialConfiguration
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

    def create_configuration_model_for_adding_prp_configuration(
        self,
        activity_description=None,
        allowedVlans=None,
        channelNumber=None,
        description=None,
        interfaceNames=None,
        isPtpEnabled=None,
        isStpBpduFilter=None,
        isStpPortfastTrunk=None,
        lanBDeviceDetails=None,
        networkDeviceId=None,
        supervisionFrameOption=None,
        switchPortMode=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API creates a configuration model needed for performing PRP creation. This is a pre-requisite if you want
        to preview the generated config for the provisioning intent.  The field `networkDeviceId` is the
        identifier of the network device. It is the `id` attribute in the response of GET API
        `/dna/intent/api/v1/networkDevices`. It must be networkDeviceId of the Redbox device.  **Response
        Details**:     The response of this API includes the information of the task created for this operation
        and contains a URL to fetch task details.  Follow the below steps once you get the response of this API
        to complete the PRP creation activity:   1. **Fetch Task ID**:    The response will include a `taskId`
        and a `url`. Use the `url` to fetch the task details.    ``` json    {         "response": {
        "taskId": "85c95140-50fc-4a57-994d-db58d3afe6b3",           "url":
        "/dna/intent/api/v1/task/85c95140-50fc-4a57-994d-db58d3afe6b3"         },         "version": "1.0"    }
        2. **Fetch Task Details**:    The task details will include a `resultLocation` URL. Use this URL to
        fetch the activity details.      ``` json     {        "response": {            "endTime":
        1718644901921,            "status": "SUCCESS",            "startTime": 1718644900114,
        "resultLocation": "/dna/intent/api/v1/activities/9e26f845-8a10-41aa-84bd-f944c86ef86b",            "id":
        "9e26f845-8a10-41aa-84bd-f944c86ef86b"        },        "version": "1.0"    } 3. **Fetch Activity ID**:
        The activity details will include `id` attribute which is `previewActivityId` that can be used in the
        subsequent APIs.        ``` json    {     "response": {       "recurring": false,       "description":
        "PRP configuration for device: FOC2316VO9J",       "startTime": 1718644900114       "id":
        "9e26f845-8a10-41aa-84bd-f944c86ef86b",       "endTime": 1718644901921,       "type": "ACTIONABLE",
        "status": "READY"     },     "version": "1.0"    }.

        Args:
            allowedVlans(string): Industrial Configuration's VLANs that are permitted on the PRP channel.
            channelNumber(integer): Industrial Configuration's Identifies a channel group that aggregates two
                physical interfaces for redundancy. Value can be either 1 or 2.
            description(string): Industrial Configuration's Information about the PRP request.. Constraints:
                maxLength set to 128.
            interfaceNames(list): Industrial Configuration's List of interface names. Must contain exactly 2
                interfaces. (list of strings).
            isPtpEnabled(boolean): Industrial Configuration's Indicates whether PTP alarms are enabled.
            isStpBpduFilter(boolean): Industrial Configuration's Indicates whether BPDU filtering is enabled on the
                port-channel interface.
            isStpPortfastTrunk(boolean): Industrial Configuration's Indicates whether PortFast is enabled on the
                interface in trunk mode.
            lanBDeviceDetails(object): Industrial Configuration's LAN-B Device Information.
            networkDeviceId(string): Industrial Configuration's Identifier of the network device. It is the `id`
                attribute in the response of API `/dna/intent/api/v1/networkDevices`. It must be
                networkDeviceId of the Redbox device.
            supervisionFrameOption(object): Industrial Configuration's PRP supervision frame option.
            switchPortMode(string): Industrial Configuration's Trunking mode of the interface. Available values are
                'TRUNK' and 'ACCESS'.
            activity_description(str): activityDescription query parameter. Optional free-form description that is
                recorded in the audit log for this activity. If omitted, a default description is
                generated by the server based on the target device.
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
            https://developer.cisco.com/docs/dna-center/#!create-configuration-model-for-adding-p-r-p-configuration
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(activity_description, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "activityDescription": activity_description,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "networkDeviceId": networkDeviceId,
            "channelNumber": channelNumber,
            "isStpBpduFilter": isStpBpduFilter,
            "isStpPortfastTrunk": isStpPortfastTrunk,
            "allowedVlans": allowedVlans,
            "switchPortMode": switchPortMode,
            "isPtpEnabled": isPtpEnabled,
            "description": description,
            "interfaceNames": interfaceNames,
            "supervisionFrameOption": supervisionFrameOption,
            "lanBDeviceDetails": lanBDeviceDetails,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_b3075d19b55fd6a86994e01364c6dc_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/iot/fabric/prp/configurationModels/cr" + "eate"
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
            "bpm_b3075d19b55fd6a86994e01364c6dc_v3_2_3_0", json_data
        )

    def retrieves_the_list_of_mrp_rings(
        self,
        network_device_id,
        id=None,
        limit=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """This API returns the list of the MRP rings when no input parameters are provided and returns the details of a
        single MRP ring based on the given fields networkDeviceId (Network device ID of the MRP ring member. The
        networkDeviceId is the instanceUuid attribute in the response of API /dna/intent/api/v1/networkDevices)
        and id (ID of the MRP ring).  This API returns the list of the MRP rings when no input parameters are
        provided and returns the details of a single MRP ring based on the given fields networkDeviceId (Network
        device ID of the MRP ring member. The networkDeviceId is the instanceUuid attribute in the response of
        API /dna/intent/api/v1/networkDevices) and id (ID of the MRP ring). .

        Args:
            network_device_id(str): networkDeviceId path parameter. Network device ID of the MRP ring member.
            id(int): id query parameter. ID of the MRP ring.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1.
            limit(int): limit query parameter. The number of records to show for this page.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-m-r-p-rings
        """
        check_type(headers, dict)
        check_type(id, int)
        check_type(offset, int)
        check_type(limit, int)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "offset": offset,
            "limit": limit,
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

        e_url = "/dna/intent/api/v1/iot/networkDevices/{networkDeviceId}/" + "mrpRings"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ef907f6fb75c9187c6377b24549af5_v3_2_3_0", json_data
        )

    def create_configuration_model_for_deleting_prp_configuration(
        self,
        activity_description=None,
        interfaceName=None,
        networkDeviceId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API creates a configuration model required to delete existing PRP configuration from the device. This is a
        pre-requisite if you want to preview the generated config for the provisioning intent.  The field
        `networkDeviceId` is the identifier of the network device. It is the `id` attribute in the response of
        GET API `/dna/intent/api/v1/networkDevices`. It must be networkDeviceId of the LAN-A or LAN-B device.
        **Response Details**:     The response of this API includes the information of the task created for this
        operation and contains a URL to fetch task details.  Follow the below steps once you get the response of
        this API to complete the PRP delete activity:   1. **Fetch Task ID**:    The response will include a
        `taskId` and a `url`. Use the `url` to fetch the task details.    ``` json    {         "response": {
        "taskId": "85c95140-50fc-4a57-994d-db58d3afe6b3",           "url":
        "/dna/intent/api/v1/task/85c95140-50fc-4a57-994d-db58d3afe6b3"         },         "version": "1.0"    }
        2. **Fetch Task Details**:    The task details will include a `resultLocation` URL. Use this URL to
        fetch the activity details.      ``` json     {        "response": {            "endTime":
        1718644901921,            "status": "SUCCESS",            "startTime": 1718644900114,
        "resultLocation": "/dna/intent/api/v1/activities/9e26f845-8a10-41aa-84bd-f944c86ef86b",            "id":
        "9e26f845-8a10-41aa-84bd-f944c86ef86b"        },        "version": "1.0"    } 3. **Fetch Activity ID**:
        The activity details will include `id` attribute which is `previewActivityId` that can be used in the
        subsequent APIs.        ``` json    {     "response": {       "recurring": false,       "description":
        "PRP configuration for device: FOC2316VO9J",       "startTime": 1718644900114       "id":
        "9e26f845-8a10-41aa-84bd-f944c86ef86b",       "endTime": 1718644901921,       "type": "ACTIONABLE",
        "status": "READY"     },     "version": "1.0"    }.

        Args:
            interfaceName(string): Industrial Configuration's Name of the interface. It can be identified in the
                response of API `/dna/intent/api/v1/iot/fabric/prp/query`. The corresponding LAN-A or
                LAN-B interface name can be retrieved from the `prpLanDevicesInfo` object in the
                response.
            networkDeviceId(string): Industrial Configuration's Identifier of the network device. It is the `id`
                attribute in the response of API `/dna/intent/api/v1/networkDevices`. It must be
                networkDeviceId of the LAN-A / LAN-B device.
            activity_description(str): activityDescription query parameter. Optional free-form description that is
                recorded in the audit log for this activity. If omitted, a default description is
                generated by the server based on the target device.
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
            https://developer.cisco.com/docs/dna-center/#!create-configuration-model-for-deleting-p-r-p-configuration
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(activity_description, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "activityDescription": activity_description,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "networkDeviceId": networkDeviceId,
            "interfaceName": interfaceName,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_cd1d97aed055c34a568c6d3e51f641a_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/iot/fabric/prp/configurationModels/de" + "lete"
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
            "bpm_cd1d97aed055c34a568c6d3e51f641a_v3_2_3_0", json_data
        )

    def configure_a_rep_ring_on_non_fabric_deployment(
        self,
        deploymentMode=None,
        id=None,
        macsecConfig=None,
        networkDeviceId=None,
        repSegmentId=None,
        repZtpMsg=None,
        ringMembers=None,
        ringName=None,
        rootNeighbourNetworkDeviceIds=None,
        rootNetworkDeviceId=None,
        status=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """**This API configures a REP ring on NON-FABRIC deployment. The input payload contains the following fields-**  |
        Field      | Description |  | ---------------| ------------|  | **ringName**         | Unique ring name.
        | **rootNetworkDeviceId** | Network device ID of the root node of the REP Ring. |  |
        **rootNeighbourNetworkDeviceIds** | Network device IDs of the two immediate neighbour devices of the
        root node of the REP Ring.|   The **networkDeviceId** is the instanceUuid attribute in the response of
        API `/dna/intent/api/v1/networkDevices`.  ---  **MACsec Configuration (macsecConfig) Optional:**  To
        enable MACsec on the REP ring, include a `macsecConfig` object with the following fields:  | Field |
        Description | |-------|-------------| | **encryptionMode** | MACsec encryption mode. Only `PSK` (Pre-
        Shared Key) is currently supported. | | **accessControlMode** | MACsec access control mode. Only
        `SHOULD_SECURE` is currently supported for PSK Encryption mode. | | **ciphersuite** | MACsec cipher
        suite `GCM_AES_128` or `GCM_AES_256`. | | **keys** | List of MACsec keys for the keychain (maximum 12
        keys). |  **Keys Configuration for PSK mode:**  | Field | Description | |-------|-------------| | **id**
        | Unique integer identifier for the key in the keychain. | | **cryptoAlgo** | Cryptographic algorithm:
        `AES_128_CMAC` or `AES_256_CMAC`. | | **passPhrase** | MACsec pre-shared key in cleartext hex. Must be
        exactly 32 hex digits for `AES_128_CMAC` or 64 hex digits for `AES_256_CMAC`. This value is write-only
        and is not returned in GET responses. | | **startTime** | Activation date/time for the key in `HH:mm:ss
        dd MMM yyyy` format (e.g., `00:00:00 09 Apr 2026`). Lifetime is set to infinite. |  > **Note:** To
        create a REP ring without MACsec, omit the `macsecConfig` field entirely or pass an empty object `{}`.

        Args:
            deploymentMode(string): Industrial Configuration's FABRIC as well as NON_FABRIC deployments.
            id(string): Industrial Configuration's REP ring identifier.
            macsecConfig(object): Industrial Configuration's MACsec configuration for REP Ring create requests (PSK
                / SHOULD_SECURE only).
            networkDeviceId(string): Industrial Configuration's Network device id of the REP ring member. It is the
                `instanceUuid` attribute in the response of `/dna/intent/api/v1/networkDevices` API.
            repSegmentId(integer): Industrial Configuration's REP segment is a chain of ports connected to each
                other and configured with a segment ID.
            repZtpMsg(string): Industrial Configuration's Summary of REP ring members that either do not have REP
                ZTP supported and those that have REP ZTP supported but not enabled.
            ringMembers(list): Industrial Configuration's Discovered member nodes in the REP ring. (list of
                objects).
            ringName(string): Industrial Configuration's Unique name of REP ring configured.
            rootNeighbourNetworkDeviceIds(list): Industrial Configuration's Hostname of the root node neighbor
                device. (list of strings).
            rootNetworkDeviceId(string): Industrial Configuration's Root node network device id of the REP ring
                member. It is the `instanceUuid` attribute in the response of
                `/dna/intent/api/v1/networkDevices` API.
            status(string): Industrial Configuration's status of the previous REP ring operation.. Available values
                are 'DISCOVERY_REQUEST_RECEIVED', 'DISCOVERY_REQUEST_ACCEPTED',
                'REMAINING_PORT_CHANNEL_IN_PROGRESS', 'REP_CONVERSION_IN_PROGRESS',
                'REP_CONVERSION_COMPLETED', 'REP_CONVERSION_FAILED', 'REP_RING_DELETE_REQUEST_RECEIVED',
                'REP_RING_DELETION_INPROGRESS', 'REP_RING_DELETION_ABORTED', 'REP_RING_DELETED',
                'REP_RING_DELETION_FAILED', 'REP_RING_DELETED_WITH_ERRS' and
                'DISCOVERY_REQUEST_COMPLETED'.
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
            https://developer.cisco.com/docs/dna-center/#!configure-a-r-e-p-ring-on-n-o-n-f-a-b-r-i-c-deployment
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
            "networkDeviceId": networkDeviceId,
            "rootNetworkDeviceId": rootNetworkDeviceId,
            "rootNeighbourNetworkDeviceIds": rootNeighbourNetworkDeviceIds,
            "status": status,
            "repSegmentId": repSegmentId,
            "deploymentMode": deploymentMode,
            "ringName": ringName,
            "ringMembers": ringMembers,
            "macsecConfig": macsecConfig,
            "repZtpMsg": repZtpMsg,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_bbc4dab8193c546ab116e19863dff621_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/iot/nonFabric/repRings"
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
            "bpm_bbc4dab8193c546ab116e19863dff621_v3_2_3_0", json_data
        )

    def create_a_configuration_model_for_performing_en_to_pen_upgrade(
        self,
        networkDeviceId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API creates configuration model needed for performing EN to PEN upgrade. This is a pre-requisite if you
        want to preview the generated config for the provisioning intent.  The field `networkDeviceId` is
        identifier of the network device which is the extended node. It is the `id` attribute in the response of
        GET API `/dna/intent/api/v1/networkDevices`.  **Response Details**:     The response of this API
        includes the information of the task created for this operation and contains a URL to fetch task
        details.  Follow the below steps once you get the response of this API to complete the EN to PEN upgrade
        activity:   1. **Fetch Task ID**:    The response will include a `taskId` and a `url`. Use the `url` to
        fetch the task details.    ``` json    {         "response": {           "taskId":
        "85c95140-50fc-4a57-994d-db58d3afe6b3",           "url":
        "/dna/intent/api/v1/task/85c95140-50fc-4a57-994d-db58d3afe6b3"         },         "version": "1.0"    }
        2. **Fetch Task Details**:    The task details will include a `resultLocation` URL. Use this URL to
        fetch the activity details.      ``` json     {        "response": {            "endTime":
        1718644901921,            "status": "SUCCESS",            "startTime": 1718644900114,
        "resultLocation": "/dna/intent/api/v1/activities/9e26f845-8a10-41aa-84bd-f944c86ef86b",            "id":
        "9e26f845-8a10-41aa-84bd-f944c86ef86b"        },        "version": "1.0"    } 3. **Fetch Activity Id**:
        The activity details will include `id` attribute which is `previewActivityId` that can be used in the
        subsequent APIs.        ``` json    {     "response": {       "recurring": false,       "description":
        "EN to PEN Upgrade for device: FOC2316VO9J",       "startTime": 1718644900114       "id":
        "9e26f845-8a10-41aa-84bd-f944c86ef86b",       "endTime": 1718644901921,       "type": "ACTIONABLE",
        "status": "READY"     },     "version": "1.0"    }.

        Args:
            networkDeviceId(string): Industrial Configuration's Identifier of the network device which is the
                extended node. It is the `id` attribute in the response of API
                `/dna/intent/api/v1/networkDevices`.
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
            https://developer.cisco.com/docs/dna-center/#!create-a-configuration-model-for-performing-e-n-to-p-e-n-upgrade
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
            "networkDeviceId": networkDeviceId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_c69fd433ce0a5e3b86d1627f32ea3722_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/iot/fabric/penUpgrade/configurationMo" + "dels"
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
            "bpm_c69fd433ce0a5e3b86d1627f32ea3722_v3_2_3_0", json_data
        )

    def perform_en_to_pen_upgrade_without_generating_a_config_preview(
        self,
        networkDeviceId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API performs EN to PEN upgrade without generating a config preview.  The field `networkDeviceId` is
        identifier of the network device which is the extended node. It is the `id` attribute in the response of
        GET API `/dna/intent/api/v1/networkDevices`.

        Args:
            networkDeviceId(string): Industrial Configuration's Identifier of the network device which is the
                extended node. It is the `id` attribute in the response of API
                `/dna/intent/api/v1/networkDevices`.
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
            https://developer.cisco.com/docs/dna-center/#!perform-e-n-to-p-e-n-upgrade-without-generating-a-config-preview
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
            "networkDeviceId": networkDeviceId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_efd80bab13e5e1b927973e73b04300a_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/iot/fabric/penUpgrade/deploy"
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
            "bpm_efd80bab13e5e1b927973e73b04300a_v3_2_3_0", json_data
        )

    def retrieves_the_count_of_mrp_rings(
        self, network_device_id, headers=None, **request_parameters
    ):
        """This API returns the count of MRP rings for the given fields networkDeviceId (Network device ID of the MRP ring
        member. The networkDeviceId is the instanceUuid attribute in the response of API
        /dna/intent/api/v1/networkDevices).  This API returns the count of MRP rings for the given fields
        networkDeviceId (Network device ID of the MRP ring member. The networkDeviceId is the instanceUuid
        attribute in the response of API /dna/intent/api/v1/networkDevices).

        Args:
            network_device_id(str): networkDeviceId path parameter. Network device ID of the MRP ring member.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-count-of-m-r-p-rings
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

        e_url = (
            "/dna/intent/api/v1/iot/networkDevices/{networkDeviceId}/"
            + "mrpRings/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f4d2ca417d50d7912fb8ea4a31662d_v3_2_3_0", json_data
        )

    def deploy_prp_configuration_without_generating_config_preview(
        self,
        activity_description=None,
        allowedVlans=None,
        channelNumber=None,
        description=None,
        interfaceNames=None,
        isPtpEnabled=None,
        isStpBpduFilter=None,
        isStpPortfastTrunk=None,
        lanBDeviceDetails=None,
        networkDeviceId=None,
        supervisionFrameOption=None,
        switchPortMode=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API configures PRP without generating a config preview.  The field `networkDeviceId` is the identifier of
        the network device. It is the `id` attribute in the response of GET API
        `/dna/intent/api/v1/networkDevices`. It must be networkDeviceId of the Redbox device.

        Args:
            allowedVlans(string): Industrial Configuration's VLANs that are permitted on the PRP channel.
            channelNumber(integer): Industrial Configuration's Identifies a channel group that aggregates two
                physical interfaces for redundancy. Value can be either 1 or 2.
            description(string): Industrial Configuration's Information about the PRP request.. Constraints:
                maxLength set to 128.
            interfaceNames(list): Industrial Configuration's List of interface names. Must contain exactly 2
                interfaces. (list of strings).
            isPtpEnabled(boolean): Industrial Configuration's Indicates whether PTP alarms are enabled.
            isStpBpduFilter(boolean): Industrial Configuration's Indicates whether BPDU filtering is enabled on the
                port-channel interface.
            isStpPortfastTrunk(boolean): Industrial Configuration's Indicates whether PortFast is enabled on the
                interface in trunk mode.
            lanBDeviceDetails(object): Industrial Configuration's LAN-B Device Information.
            networkDeviceId(string): Industrial Configuration's Identifier of the network device. It is the `id`
                attribute in the response of API `/dna/intent/api/v1/networkDevices`. It must be
                networkDeviceId of the Redbox device.
            supervisionFrameOption(object): Industrial Configuration's PRP supervision frame option.
            switchPortMode(string): Industrial Configuration's Trunking mode of the interface. Available values are
                'TRUNK' and 'ACCESS'.
            activity_description(str): activityDescription query parameter. Optional free-form description that is
                recorded in the audit log for this activity. If omitted, a default description is
                generated by the server based on the target device.
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
            https://developer.cisco.com/docs/dna-center/#!deploy-p-r-p-configuration-without-generating-config-preview
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(activity_description, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "activityDescription": activity_description,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "networkDeviceId": networkDeviceId,
            "channelNumber": channelNumber,
            "isStpBpduFilter": isStpBpduFilter,
            "isStpPortfastTrunk": isStpPortfastTrunk,
            "allowedVlans": allowedVlans,
            "switchPortMode": switchPortMode,
            "isPtpEnabled": isPtpEnabled,
            "description": description,
            "interfaceNames": interfaceNames,
            "supervisionFrameOption": supervisionFrameOption,
            "lanBDeviceDetails": lanBDeviceDetails,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f7bdc0b40fda5f378b9fef5b185fd92d_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/iot/fabric/prp/deploy"
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
            "bpm_f7bdc0b40fda5f378b9fef5b185fd92d_v3_2_3_0", json_data
        )

    def update_prp_configuration_without_generating_config_preview(
        self,
        activity_description=None,
        allowedVlans=None,
        networkDeviceId=None,
        supervisionFrameOption=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API updates PRP configuration without generating a config preview.  The field `networkDeviceId` is the
        identifier of the network device. It is the `id` attribute in the response of GET API
        `/dna/intent/api/v1/networkDevices`. It must be networkDeviceId of the Redbox device.

        Args:
            allowedVlans(string): Industrial Configuration's VLANs that are permitted on the PRP channel.
            networkDeviceId(string): Industrial Configuration's Identifier of the network device. It is the `id`
                attribute in the response of API `/dna/intent/api/v1/networkDevices`. It must be
                networkDeviceId of the Redbox device.
            supervisionFrameOption(object): Industrial Configuration's PRP supervision frame option.
            activity_description(str): activityDescription query parameter. Optional free-form description that is
                recorded in the audit log for this activity. If omitted, a default description is
                generated by the server based on the target device.
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
            https://developer.cisco.com/docs/dna-center/#!update-p-r-p-configuration-without-generating-config-preview
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(activity_description, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "activityDescription": activity_description,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "networkDeviceId": networkDeviceId,
            "allowedVlans": allowedVlans,
            "supervisionFrameOption": supervisionFrameOption,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator("jsd_f44c345eaeb144e095610cc8e2_v3_2_3_0").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/iot/fabric/prp/deploy"
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
            "bpm_f44c345eaeb144e095610cc8e2_v3_2_3_0", json_data
        )

    def delete_prp_configuration_without_generating_a_config_preview(
        self,
        interface_name,
        network_device_id,
        activity_description=None,
        headers=None,
        **request_parameters
    ):
        """This API deletes the PRP configuration without generating a config preview.  The field `networkDeviceId` is the
        identifier of the network device. It is the `id` attribute in the response of GET API
        `/dna/intent/api/v1/networkDevices`. It must be networkDeviceId of the LAN-A or LAN-B device.

        Args:
            network_device_id(str): networkDeviceId query parameter. Identifier of the network device. It is the
                `id` attribute in the response of API `/dna/intent/api/v1/networkDevices`.
            interface_name(str): interfaceName query parameter. Name of the interface. It can be identified in the
                response of API `/dna/intent/api/v1/iot/fabric/prp/query`. The corresponding LAN-A or
                LAN-B interface name can be retrieved from the `prpLanDevicesInfo` object in the
                response.
            activity_description(str): activityDescription query parameter. Optional free-form description that is
                recorded in the audit log for this activity. If omitted, a default description is
                generated by the server based on the target device.
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
            https://developer.cisco.com/docs/dna-center/#!delete-p-r-p-configuration-without-generating-a-config-preview
        """
        check_type(headers, dict)
        check_type(network_device_id, str, may_be_none=False)
        check_type(interface_name, str, may_be_none=False)
        check_type(activity_description, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "networkDeviceId": network_device_id,
            "interfaceName": interface_name,
            "activityDescription": activity_description,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/iot/fabric/prp/deploy"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ce4520dc1ca6557cba608f925ba58a08_v3_2_3_0", json_data
        )

    def generate_prp_configuration_for_the_given_network_device_and_prp_configuration_model(
        self, network_device_id, preview_activity_id, headers=None, **request_parameters
    ):
        """This API triggers generation of the configuration preview for a specific network device for the given PRP
        configuration model, identified by `previewActivityId` and `networkDeviceId`.

        Args:
            preview_activity_id(str): previewActivityId path parameter. The unique identifier for the PRP
                configuration model activity. It can be retrieved by following the **Response Details**
                steps in one of the following APIs and using the `activityId` value returned in the
                activity details as the `previewActivityId`: `POST
                /dna/intent/api/v1/iot/fabric/prp/configurationModels/create` `POST
                /dna/intent/api/v1/iot/fabric/prp/configurationModels/update` `POST
                /dna/intent/api/v1/iot/fabric/prp/configurationModels/delete` .
            network_device_id(str): networkDeviceId path parameter. Identifier of the network device. It is the `id`
                attribute in the response of API `/dna/intent/api/v1/networkDevices`.
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
            https://developer.cisco.com/docs/dna-center/#!generate-p-r-p-configuration-for-the-given-network-device-and-p-r-p-configuration-model
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
            "/dna/intent/api/v1/iot/fabric/prp/configurationModels/{p"
            + "reviewActivityId}/networkDevices/{networkDeviceId}/confi"
            + "g"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ce4e7dde6c5f778337e1fd02f02e1a_v3_2_3_0", json_data
        )

    def retrieve_generated_prp_configuration_for_the_given_network_device_and_prp_configuration_model(
        self, network_device_id, preview_activity_id, headers=None, **request_parameters
    ):
        """This API retrieves the configuration preview for a specific network device for the given PRP configuration
        model, identified by `previewActivityId` and `networkDeviceId`.

        Args:
            preview_activity_id(str): previewActivityId path parameter. The unique identifier for the PRP
                configuration model activity. It can be retrieved by following the **Response Details**
                steps in one of the following APIs and using the `activityId` value returned in the
                activity details as the `previewActivityId`: `POST
                /dna/intent/api/v1/iot/fabric/prp/configurationModels/create` `POST
                /dna/intent/api/v1/iot/fabric/prp/configurationModels/update` `POST
                /dna/intent/api/v1/iot/fabric/prp/configurationModels/delete` .
            network_device_id(str): networkDeviceId path parameter. Identifier of the network device. It is the `id`
                attribute in the response of API `/dna/intent/api/v1/networkDevices`.
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-generated-p-r-p-configuration-for-the-given-network-device-and-p-r-p-configuration-model
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
            "/dna/intent/api/v1/iot/fabric/prp/configurationModels/{p"
            + "reviewActivityId}/networkDevices/{networkDeviceId}/confi"
            + "g"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ad98489d498a5c8e9a963a348df8634b_v3_2_3_0", json_data
        )

    def delete_rep_ring_configured_in_the_non_fabric_deployment(
        self, id, force_delete=None, headers=None, **request_parameters
    ):
        """This API deletes the REP ring configured in the NON-FABRIC deployment for the given id. The **id** of configured
        REP ring can be retrieved using the API `/dna/intent/api/v1/iot/repRings/query`.   The **taskid**
        returned can be used to monitor the status of delete operation using following API
        `/intent/api/v1/task/{taskId}`.  ---  **Force Delete (forceDelete) Optional:**  When `forceDelete=true`,
        REP Ring force delete will be invoked. `Force Delete` is supported only after REP Ring delete has been
        attempted and has either failed or partially completed where REP configurations are not cleared from all
        the REP Ring members. Force Delete of REP Ring would delete the REP Ring from Catalyst Center alone, it
        would not remove REP configurations from any REP Ring members. Manual cleanup would be needed to clear
        REP configuration on the failed or unreachable devices.

        Args:
            id(str): id path parameter. Ring ID of configured REP ring can be fetched using the API
                `/dna/intent/api/v1/iot/repRings/query`.
            force_delete(bool): forceDelete query parameter. When set as true, REP Ring force delete will be
                invoked. `Force Delete` is supported only after REP Ring delete has been attempted and
                has either failed or partially completed where REP configurations are not cleared from
                all the REP Ring members. Force Delete of REP Ring would delete the REP Ring from
                Catalyst center alone, it would not remove REP configurations from any REP Ring members.
                Manual cleanup would be needed to clear REP configuration on the failed or unreachable
                devices.
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
            https://developer.cisco.com/docs/dna-center/#!delete-r-e-p-ring-configured-in-the-n-o-n-f-a-b-r-i-c-deployment
        """
        check_type(headers, dict)
        check_type(force_delete, bool)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "forceDelete": force_delete,
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

        e_url = "/dna/intent/api/v1/iot/nonFabric/repRings/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dcf9b8fecdd57f0bb7a33d358e6be37_v3_2_3_0", json_data
        )

    def retrieve_details_of_the_prp_topologies_configured(
        self,
        limit=None,
        network_device_id=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """This API retrieves details of the PRP topologies configured.

        Args:
            network_device_id(str): networkDeviceId query parameter. Identifier of the network device. It is the
                `id` attribute in the response of API `/dna/intent/api/v1/networkDevices`. It must be
                networkDeviceId of the Redbox device.
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-details-of-the-p-r-p-topologies-configured
        """
        check_type(headers, dict)
        check_type(network_device_id, str)
        check_type(limit, int)
        check_type(offset, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "networkDeviceId": network_device_id,
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

        e_url = "/dna/intent/api/v1/iot/fabric/prp"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a89ad22a95243a978ce374fd6b874_v3_2_3_0", json_data
        )

    def delete_the_configuration_model_created_for_en_to_pen_upgrade(
        self, preview_activity_id, headers=None, **request_parameters
    ):
        """This API deletes configuration model created for performing EN to PEN upgrade.

        Args:
            preview_activity_id(str): previewActivityId path parameter. The unique identifier for the activity. It
                can be retrieved by following the steps mentioned in **Response Details** section of
                POST API `/dna/intent/api/v1/fabric/penUpgrade/configurationModels`.
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
            https://developer.cisco.com/docs/dna-center/#!delete-the-configuration-model-created-for-e-n-to-p-e-n-upgrade
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
            "/dna/intent/api/v1/iot/fabric/penUpgrade/configurationMo"
            + "dels/{previewActivityId}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ff004631966055a2a9754de6ab56ef59_v3_2_3_0", json_data
        )

    def get_the_rep_ring_based_on_the_ring_id(
        self, id, headers=None, **request_parameters
    ):
        """This API returns REP ring for the given id (The id of configured REP ring can be retrieved using the API
        `/dna/intent/api/v1/iot/repRings/query`).   Response also includes the details of the ports that are
        part of REP ring along with the REP ZTP (Zero touch provisioning) status.    Below contains value and
        description of status    | Value                            |Description of status
        |-------------------------|---------|  | `DISCOVERY_REQUEST_RECEIVED`          | Discovery request
        received for the REP ring.   |  | `DISCOVERY_REQUEST_COMPLETED`         | Discovery request completed
        for the REP ring.   |  | `REP_CONVERSION_IN_PROGRESS`          | Ring conversion from STP to REP ring.
        |  | `REMAINING_PORT_CHANNEL_IN_PROGRESS`  | Ports are getting configured for the REP ring
        configuration. |  | `REP_CONVERSION_COMPLETED`            | REP ring created successfully.   |  |
        `REP_RING_DELETE_REQUEST_RECEIVED`    | REP ring deletion request received. |
        |`REP_RING_DELETION_INPROGRESS`         | REP ring configuration is getting deleted from the device. |
        |`REP_RING_DELETION_ABORTED`             | REP ring deletion is aborted. |  |`REP_RING_DELETED`
        | REP ring is successfully deleted. |  |`REP_RING_DELETION_FAILED`              | REP ring deletion
        failed. |  |`REP_RING_DELETED_WITH_ERRS`            | REP ring deletion failed with errors. |  ---
        **MACsec Configuration (macsecConfig) Optional:**  If MACsec is enabled on the REP ring, response would
        include a `macsecConfig` object with the following fields:  | Field | Description |
        |-------|-------------| | **encryptionMode** | MACsec encryption mode. Only `PSK` (Pre-Shared Key) is
        currently supported. | | **accessControlMode** | MACsec access control mode. Only `SHOULD_SECURE` is
        currently supported for PSK Encryption mode. | | **ciphersuite** | MACsec cipher suite `GCM_AES_128` or
        `GCM_AES_256`. | | **keys** | List of MACsec keys for the keychain (maximum 12 keys). |  **Keys
        Configuration for PSK mode:**  | Field | Description | |-------|-------------| | **id** | Unique integer
        identifier for the key in the keychain. | | **cryptoAlgo** | Cryptographic algorithm: `AES_128_CMAC` or
        `AES_256_CMAC`. | | **passPhrase** | MACsec pre-shared key masked value will be displayed as `********`.
        | | **startTime** | Activation date/time for the key in `HH:mm:ss dd MMM yyyy` format (e.g., `00:00:00
        09 Apr 2026`). Lifetime is set to infinite. |  > **Note:** `passPhrase` values are write-only and are
        always returned as `********` in GET/query responses.

        Args:
            id(str): id path parameter. Ring ID of configured REP ring can be fetched using the API
                `/dna/intent/api/v1/iot/repRings/query`.
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
            https://developer.cisco.com/docs/dna-center/#!get-the-r-e-p-ring-based-on-the-ring-id
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

        e_url = "/dna/intent/api/v1/iot/repRings/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ce1469c515d8a72455779e3a484_v3_2_3_0", json_data
        )

    def retrieve_total_count_of_prp_topologies(
        self, network_device_id=None, headers=None, **request_parameters
    ):
        """This API retrieves total count of PRP topologies.

        Args:
            network_device_id(str): networkDeviceId query parameter. Identifier of the network device. It is the
                `id` attribute in the response of API `/dna/intent/api/v1/networkDevices`. It must be
                networkDeviceId of the Redbox device.
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-total-count-of-p-r-p-topologies
        """
        check_type(headers, dict)
        check_type(network_device_id, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "networkDeviceId": network_device_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/iot/fabric/prp/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b9d8e8fcb8f6533e9bbaf025b1d569b4_v3_2_3_0", json_data
        )

    def deploy_the_configuration_model_for_en_to_pen_upgrade_on_network_devices(
        self, preview_activity_id, headers=None, **request_parameters
    ):
        """This API deploys the configuration model for EN to PEN upgrade on network devices.

        Args:
            preview_activity_id(str): previewActivityId path parameter. The unique identifier for the activity. It
                can be retrieved by following the steps mentioned in **Response Details** section of
                POST API `/dna/intent/api/v1/fabric/penUpgrade/configurationModels`.
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
            https://developer.cisco.com/docs/dna-center/#!deploy-the-configuration-model-for-e-n-to-p-e-n-upgrade-on-network-devices
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
            "/dna/intent/api/v1/iot/fabric/penUpgrade/configurationMo"
            + "dels/{previewActivityId}/deploy"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f8db82368e8549587fb1f9b5e96fdb2_v3_2_3_0", json_data
        )

    def retrieve_the_config_of_network_device_for_en_to_pen_upgrade_configuration_model(
        self, network_device_id, preview_activity_id, headers=None, **request_parameters
    ):
        """This API retrieves the configuration for specific network device for a given EN to PEN upgrade configuration
        model using `previewActivityId` and `networkDeviceId`.

        Args:
            preview_activity_id(str): previewActivityId path parameter. The unique identifier for the activity. It
                can be retrieved by following the steps mentioned in **Response Details** section of
                POST API `/dna/intent/api/v1/fabric/penUpgrade/configurationModels`.
            network_device_id(str): networkDeviceId path parameter. Identifier of the network device which is the
                extended node. It is the `id` attribute in the response of API
                `/dna/intent/api/v1/networkDevices`.
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-the-config-of-network-device-for-e-n-to-p-e-n-upgrade-configuration-model
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
            "/dna/intent/api/v1/iot/fabric/penUpgrade/configurationMo"
            + "dels/{previewActivityId}/networkDevices/{networkDeviceId"
            + "}/config"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ef916e655545d8aac01b351ee8a7f0d_v3_2_3_0", json_data
        )

    def generate_the_config_of_network_device_for_en_to_pen_upgrade_configuration_model(
        self, network_device_id, preview_activity_id, headers=None, **request_parameters
    ):
        """This API generates the configuration for specific network device for a given EN to PEN upgrade configuration
        model using `previewActivityId` and `networkDeviceId`.

        Args:
            preview_activity_id(str): previewActivityId path parameter. The unique identifier for the activity. It
                can be retrieved by following the steps mentioned in **Response Details** section of
                POST API `/dna/intent/api/v1/fabric/penUpgrade/configurationModels`.
            network_device_id(str): networkDeviceId path parameter. Identifier of the network device which is the
                extended node. It is the `id` attribute in the response of API
                `/dna/intent/api/v1/networkDevices`.
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
            https://developer.cisco.com/docs/dna-center/#!generate-the-config-of-network-device-for-e-n-to-p-e-n-upgrade-configuration-model
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
            "/dna/intent/api/v1/iot/fabric/penUpgrade/configurationMo"
            + "dels/{previewActivityId}/networkDevices/{networkDeviceId"
            + "}/config"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f7c2678207695930a67fb326d09e13db_v3_2_3_0", json_data
        )

    def delete_aprp_configuration_model(
        self, preview_activity_id, headers=None, **request_parameters
    ):
        """This API deletes configuration model created for PRP.

        Args:
            preview_activity_id(str): previewActivityId path parameter. The unique identifier for the PRP
                configuration model activity. It can be retrieved by following the **Response Details**
                steps in one of the following APIs and using the `activityId` value returned in the
                activity details as the `previewActivityId`: `POST
                /dna/intent/api/v1/iot/fabric/prp/configurationModels/create` `POST
                /dna/intent/api/v1/iot/fabric/prp/configurationModels/update` `POST
                /dna/intent/api/v1/iot/fabric/prp/configurationModels/delete` .
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
            https://developer.cisco.com/docs/dna-center/#!delete-a-p-r-p-configuration-model
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
            "/dna/intent/api/v1/iot/fabric/prp/configurationModels/{p"
            + "reviewActivityId}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a07eff6b9d8513f9313dca39c733d73_v3_2_3_0", json_data
        )

    def retrieve_the_list_rep_rings(
        self,
        deploymentMode=None,
        limit=None,
        networkDeviceId=None,
        offset=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API returns the list of REP rings for the given fields networkDeviceId (Network device ID of the REP ring
        member. In case of successful REP ring creation, any of the REP ring member networkDeviceId can be
        provided. In case of failed REP ring creation, provide only root node networkDeviceId. The
        networkDeviceId is the instanceUuid attribute in the response of API /dna/intent/api/v1/networkDevice)
        and deploymentMode (FABRIC/NON_FABRIC).  Retrieve the list REP rings. This API returns the list of REP
        rings for the given fields networkDeviceId (Network device ID of the REP ring member. In case of
        successful REP ring creation, any of the REP ring member networkDeviceId can be provided. In case of
        failed REP ring creation, provide only root node networkDeviceId. The networkDeviceId is the
        instanceUuid attribute in the response of API /dna/intent/api/v1/networkDevice) and deploymentMode
        (FABRIC/NON_FABRIC).

        Args:
            deploymentMode(string): Industrial Configuration's Deployment mode of the configured REP ring..
                Available values are 'FABRIC' and 'NON_FABRIC'.
            limit(integer): Industrial Configuration's The number of records to show for this page.
            networkDeviceId(string): Industrial Configuration's Network device id of the REP ring member. API
                `/dna/intent/api/v1/networkDevices` can be used to get the list of networkDeviceIds of
                the neighbors , `instanceUuid` attribute in the response contains networkDeviceId.
            offset(integer): Industrial Configuration's The first record to show for this page; the first record is
                numbered 1.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-the-list-r-e-p-rings
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
            "networkDeviceId": networkDeviceId,
            "deploymentMode": deploymentMode,
            "limit": limit,
            "offset": offset,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_fa2127b55124a3a00b2991b77db6_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/iot/repRings/query"
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
            "bpm_fa2127b55124a3a00b2991b77db6_v3_2_3_0", json_data
        )

    def retrieve_configuration_model_generation_status_for_en_to_pen_upgrade(
        self, preview_activity_id, headers=None, **request_parameters
    ):
        """This API retrieves the status of the configuration model for network devices in EN to PEN upgrade.

        Args:
            preview_activity_id(str): previewActivityId path parameter. The unique identifier for the activity. It
                can be retrieved by following the steps mentioned in **Response Details** section of
                POST API `/dna/intent/api/v1/fabric/penUpgrade/configurationModels`.
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-configuration-model-generation-status-for-e-n-to-p-e-n-upgrade
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
            "/dna/intent/api/v1/iot/fabric/penUpgrade/configurationMo"
            + "dels/{previewActivityId}/networkDeviceStatusDetails"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_af1303a4275fe4b3c028cb0933e813_v3_2_3_0", json_data
        )

    def create_configuration_model_for_updating_prp_configuration(
        self,
        activity_description=None,
        allowedVlans=None,
        networkDeviceId=None,
        supervisionFrameOption=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API creates a configuration model required to update existing PRP configuration on the device. This is a
        pre-requisite if you want to preview the generated config for the provisioning intent.  The field
        `networkDeviceId` is the identifier of the network device. It is the `id` attribute in the response of
        GET API `/dna/intent/api/v1/networkDevices`. It must be networkDeviceId of the Redbox device.
        **Response Details**:     The response of this API includes the information of the task created for this
        operation and contains a URL to fetch task details.  Follow the below steps once you get the response of
        this API to complete the PRP edit activity:   1. **Fetch Task ID**:    The response will include a
        `taskId` and a `url`. Use the `url` to fetch the task details.    ``` json    {         "response": {
        "taskId": "85c95140-50fc-4a57-994d-db58d3afe6b3",           "url":
        "/dna/intent/api/v1/task/85c95140-50fc-4a57-994d-db58d3afe6b3"         },         "version": "1.0"    }
        2. **Fetch Task Details**:    The task details will include a `resultLocation` URL. Use this URL to
        fetch the activity details.      ``` json     {        "response": {            "endTime":
        1718644901921,            "status": "SUCCESS",            "startTime": 1718644900114,
        "resultLocation": "/dna/intent/api/v1/activities/9e26f845-8a10-41aa-84bd-f944c86ef86b",            "id":
        "9e26f845-8a10-41aa-84bd-f944c86ef86b"        },        "version": "1.0"    } 3. **Fetch Activity ID**:
        The activity details will include `id` attribute which is `previewActivityId` that can be used in the
        subsequent APIs.        ``` json    {     "response": {       "recurring": false,       "description":
        "PRP configuration for device: FOC2316VO9J",       "startTime": 1718644900114       "id":
        "9e26f845-8a10-41aa-84bd-f944c86ef86b",       "endTime": 1718644901921,       "type": "ACTIONABLE",
        "status": "READY"     },     "version": "1.0"    }.

        Args:
            allowedVlans(string): Industrial Configuration's VLANs that are permitted on the PRP channel.
            networkDeviceId(string): Industrial Configuration's Identifier of the network device. It is the `id`
                attribute in the response of API `/dna/intent/api/v1/networkDevices`. It must be
                networkDeviceId of the Redbox device.
            supervisionFrameOption(object): Industrial Configuration's PRP supervision frame option.
            activity_description(str): activityDescription query parameter. Optional free-form description that is
                recorded in the audit log for this activity. If omitted, a default description is
                generated by the server based on the target device.
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
            https://developer.cisco.com/docs/dna-center/#!create-configuration-model-for-updating-p-r-p-configuration
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(activity_description, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "activityDescription": activity_description,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "networkDeviceId": networkDeviceId,
            "allowedVlans": allowedVlans,
            "supervisionFrameOption": supervisionFrameOption,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_b43efd6a99a55b27a83d6288f6ea0fb6_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/iot/fabric/prp/configurationModels/up" + "date"
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
            "bpm_b43efd6a99a55b27a83d6288f6ea0fb6_v3_2_3_0", json_data
        )

    def retrieves_the_count_of_mrp_ring_members(
        self, id, network_device_id, headers=None, **request_parameters
    ):
        """This API returns the count of MRP ring members for the given fields networkDeviceId (Network device ID of the
        MRP ring member. The networkDeviceId is the instanceUuid attribute in the response of API
        /dna/intent/api/v1/networkDevices) and id (ID of the MRP ring).  This API returns the count of MRP ring
        members for the given fields networkDeviceId (Network device ID of the MRP ring member. The
        networkDeviceId is the instanceUuid attribute in the response of API /dna/intent/api/v1/networkDevices)
        and id (ID of the MRP ring).

        Args:
            network_device_id(str): networkDeviceId path parameter. Network device ID of the MRP ring member.
            id(int): id path parameter. ID of the MRP ring.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-count-of-m-r-p-ring-members
        """
        check_type(headers, dict)
        check_type(network_device_id, str, may_be_none=False)
        check_type(id, int, may_be_none=False)
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
            "/dna/intent/api/v1/iot/networkDevices/{networkDeviceId}/"
            + "mrpRings/{id}/members/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bc1b3345f259e9859ac21a1ec694fe_v3_2_3_0", json_data
        )

    def retrieves_the_list_of_network_devices_part_of_mrp_ring(
        self,
        id,
        network_device_id,
        limit=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """This API returns the list of MRP ring members for the given fields networkDeviceId (Network device ID of the MRP
        ring member. The networkDeviceId is the instanceUuid attribute in the response of API
        /dna/intent/api/v1/networkDevices) and id (ID of the MRP ring).  This API returns the list of MRP ring
        members for the given fields networkDeviceId (Network device ID of the MRP ring member. The
        networkDeviceId is the instanceUuid attribute in the response of API /dna/intent/api/v1/networkDevices)
        and id (ID of the MRP ring).

        Args:
            network_device_id(str): networkDeviceId path parameter. Network device ID of the MRP ring member.
            id(int): id path parameter. ID of the MRP ring.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1.
            limit(int): limit query parameter. The number of records to show for this page.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-network-devices-part-of-m-r-p-ring
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(network_device_id, str, may_be_none=False)
        check_type(id, int, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "offset": offset,
            "limit": limit,
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
            "/dna/intent/api/v1/iot/networkDevices/{networkDeviceId}/"
            + "mrpRings/{id}/members"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bf87f6cb9efb5451b84253593e548f98_v3_2_3_0", json_data
        )

    def configure_a_rep_ring_on_fabric_deployment(
        self,
        deploymentMode=None,
        id=None,
        macsecConfig=None,
        networkDeviceId=None,
        repSegmentId=None,
        repZtpMsg=None,
        ringMembers=None,
        ringName=None,
        rootNeighbourNetworkDeviceIds=None,
        rootNetworkDeviceId=None,
        status=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """**This API configures a REP ring on FABRIC deployment. The input payload contains the following fields-**  |
        Field      | Description |  | ---------------| ------------| | **ringName**         | Unique ring name.
        | **rootNetworkDeviceId** | Network device ID of the root node of the REP Ring. |  |
        **rootNeighbourNetworkDeviceIds** | Network device IDs of the two immediate neighbour devices of the
        root node of the REP Ring.|   The **networkDeviceId** is the instanceUuid attribute in the response of
        API `/dna/intent/api/v1/networkDevices`.

        Args:
            deploymentMode(string): Industrial Configuration's FABRIC as well as NON_FABRIC deployments.
            id(string): Industrial Configuration's REP ring identifier.
            macsecConfig(object): Industrial Configuration's MACsec configuration for REP Ring create requests (PSK
                / SHOULD_SECURE only).
            networkDeviceId(string): Industrial Configuration's Network device id of the REP ring member. It is the
                `instanceUuid` attribute in the response of `/dna/intent/api/v1/networkDevices` API.
            repSegmentId(integer): Industrial Configuration's REP segment is a chain of ports connected to each
                other and configured with a segment ID.
            repZtpMsg(string): Industrial Configuration's Summary of REP ring members that either do not have REP
                ZTP supported and those that have REP ZTP supported but not enabled.
            ringMembers(list): Industrial Configuration's Discovered member nodes in the REP ring. (list of
                objects).
            ringName(string): Industrial Configuration's Unique name of REP ring configured.
            rootNeighbourNetworkDeviceIds(list): Industrial Configuration's Hostname of the root node neighbor
                device. (list of strings).
            rootNetworkDeviceId(string): Industrial Configuration's Root node network device id of the REP ring
                member. It is the `instanceUuid` attribute in the response of
                `/dna/intent/api/v1/networkDevices` API.
            status(string): Industrial Configuration's status of the previous REP ring operation.. Available values
                are 'DISCOVERY_REQUEST_RECEIVED', 'DISCOVERY_REQUEST_ACCEPTED',
                'REMAINING_PORT_CHANNEL_IN_PROGRESS', 'REP_CONVERSION_IN_PROGRESS',
                'REP_CONVERSION_COMPLETED', 'REP_CONVERSION_FAILED', 'REP_RING_DELETE_REQUEST_RECEIVED',
                'REP_RING_DELETION_INPROGRESS', 'REP_RING_DELETION_ABORTED', 'REP_RING_DELETED',
                'REP_RING_DELETION_FAILED', 'REP_RING_DELETED_WITH_ERRS' and
                'DISCOVERY_REQUEST_COMPLETED'.
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
            https://developer.cisco.com/docs/dna-center/#!configure-a-r-e-p-ring-on-f-a-b-r-i-c-deployment
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
            "networkDeviceId": networkDeviceId,
            "rootNetworkDeviceId": rootNetworkDeviceId,
            "rootNeighbourNetworkDeviceIds": rootNeighbourNetworkDeviceIds,
            "status": status,
            "repSegmentId": repSegmentId,
            "deploymentMode": deploymentMode,
            "ringName": ringName,
            "ringMembers": ringMembers,
            "macsecConfig": macsecConfig,
            "repZtpMsg": repZtpMsg,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f200dc9a10d25beab1243a5b29f99c7d_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/iot/fabric/repRings"
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
            "bpm_f200dc9a10d25beab1243a5b29f99c7d_v3_2_3_0", json_data
        )

    def retrieve_configuration_model_generation_status_for_prp(
        self, preview_activity_id, headers=None, **request_parameters
    ):
        """This API retrieves the configuration model generation status for all network devices participating in PRP for
        the specified previewActivityId.

        Args:
            preview_activity_id(str): previewActivityId path parameter. The unique identifier for the PRP
                configuration model activity. It can be retrieved by following the **Response Details**
                steps in one of the following APIs and using the `activityId` value returned in the
                activity details as the `previewActivityId`: `POST
                /dna/intent/api/v1/iot/fabric/prp/configurationModels/create` `POST
                /dna/intent/api/v1/iot/fabric/prp/configurationModels/update` `POST
                /dna/intent/api/v1/iot/fabric/prp/configurationModels/delete` .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-configuration-model-generation-status-for-p-r-p
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
            "/dna/intent/api/v1/iot/fabric/prp/configurationModels/{p"
            + "reviewActivityId}/networkDeviceStatusDetails"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d1950132e25b1881cfabdd34719ee5_v3_2_3_0", json_data
        )

    def retrieves_the_count_of_rep_rings(
        self,
        deploymentMode=None,
        networkDeviceId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """**This API returns the count of REP rings for the given fields-**  | Field      | Description |  |
        ---------------| ------------| | **networkDeviceId**         | Network device ID of the REP ring member.
        The **networkDeviceId** is the instanceUuid attribute in the response of API
        `/dna/intent/api/v1/networkDevices`.     | **deploymentMode** | FABRIC/NON_FABRIC |.

        Args:
            deploymentMode(string): Industrial Configuration's deploymentMode (FABRIC/NON_FABRIC) of the configured
                REP ring.
            networkDeviceId(string): Industrial Configuration's Network device id of the REP ring member. It is the
                `instanceUuid` attribute in the response of `/dna/intent/api/v1/networkDevices` API.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-count-of-r-e-p-rings
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
            "networkDeviceId": networkDeviceId,
            "deploymentMode": deploymentMode,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d9f276a532e5eeb86bb591f8537fcc7_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/iot/repRings/query/count"
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
            "bpm_d9f276a532e5eeb86bb591f8537fcc7_v3_2_3_0", json_data
        )

    def delete_rep_ring_configured_in_the_fabric_deployment(
        self, id, force_delete=None, headers=None, **request_parameters
    ):
        """This API deletes the REP ring configured in the FABRIC deployment for the given id. The **id** of configured REP
        ring can be retrieved using the API `/dna/intent/api/v1/iot/repRings/query`.   The **taskid** returned
        can be used to monitor the status of delete operation using following API -
        `/intent/api/v1/task/{taskId}`.  ---  **Force Delete (forceDelete) Optional:**  When `forceDelete=true`,
        REP Ring force delete will be invoked. `Force Delete` is supported only after REP Ring delete has been
        attempted and has either failed or partially completed where REP configurations are not cleared from all
        the REP Ring members. Force Delete of REP Ring would delete the REP Ring from Catalyst Center alone, it
        would not remove REP configurations from any REP Ring members. Manual cleanup would be needed to clear
        REP configuration on the failed or unreachable devices.

        Args:
            id(str): id path parameter. Ring ID of configured REP ring can be fetched using the API
                `/dna/intent/api/v1/iot/repRings/query`.
            force_delete(bool): forceDelete query parameter. When set as true, REP Ring force delete will be
                invoked. `Force Delete` is supported only after REP Ring delete has been attempted and
                has either failed or partially completed where REP configurations are not cleared from
                all the REP Ring members. Force Delete of REP Ring would delete the REP Ring from
                Catalyst center alone, it would not remove REP configurations from any REP Ring members.
                Manual cleanup would be needed to clear REP configuration on the failed or unreachable
                devices.
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
            https://developer.cisco.com/docs/dna-center/#!delete-r-e-p-ring-configured-in-the-f-a-b-r-i-c-deployment
        """
        check_type(headers, dict)
        check_type(force_delete, bool)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "forceDelete": force_delete,
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

        e_url = "/dna/intent/api/v1/iot/fabric/repRings/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_aca1b387f556ca0c87d563b3df8f2_v3_2_3_0", json_data
        )

    def deploy_the_configuration_model_for_prp_on_network_devices(
        self, preview_activity_id, headers=None, **request_parameters
    ):
        """This API deploys the configuration model for PRP on network devices.

        Args:
            preview_activity_id(str): previewActivityId path parameter. The unique identifier for the PRP
                configuration model activity. It can be retrieved by following the **Response Details**
                steps in one of the following APIs and using the `activityId` value returned in the
                activity details as the `previewActivityId`: `POST
                /dna/intent/api/v1/iot/fabric/prp/configurationModels/create` `POST
                /dna/intent/api/v1/iot/fabric/prp/configurationModels/update` `POST
                /dna/intent/api/v1/iot/fabric/prp/configurationModels/delete` .
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
            https://developer.cisco.com/docs/dna-center/#!deploy-the-configuration-model-for-p-r-p-on-network-devices
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
            "/dna/intent/api/v1/iot/fabric/prp/configurationModels/{p"
            + "reviewActivityId}/deploy"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dbfa788ae5dfe849b7b4784aa8297_v3_2_3_0", json_data
        )
