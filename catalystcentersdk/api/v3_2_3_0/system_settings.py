"""Cisco Catalyst Center System Settings API wrapper.

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


class SystemSettings:
    """Cisco Catalyst Center System Settings API (version: 3.2.3.0).

    Wraps the Catalyst Center System Settings
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new SystemSettings
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

    def delete_authentication_and_policy_server_access_configuration(
        self, id, headers=None, **request_parameters
    ):
        """API to delete AAA/ISE server access configuration.

        Args:
            id(str): id path parameter. Authentication and Policy Server Identifier. Use 'Get Authentication and
                Policy Servers' intent API to find the identifier.
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
            https://developer.cisco.com/docs/dna-center/#!delete-authentication-and-policy-server-access-configuration
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

        e_url = "/dna/intent/api/v1/authentication-policy-servers/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b5ce4c02a525aa98e49940d5aa006a7_v3_2_3_0", json_data
        )

    def edit_authentication_and_policy_server_access_configuration(
        self,
        id,
        accountingPort=None,
        authenticationPort=None,
        ciscoIseDtos=None,
        externalCiscoIseIpAddrDtos=None,
        port=None,
        protocol=None,
        pxgridEnabled=None,
        retries=None,
        timeoutSeconds=None,
        useDnacCertForPxgrid=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """API to edit AAA/ISE server access configuration. After edit, use ‘Cisco ISE Server Integration Status’ Intent
        API to check the integration status.

        Args:
            accountingPort(integer): System Settings's Accounting port of RADIUS server. It is required for RADIUS
                server. The range is from 1 to 65535. E.g. 1813.
            authenticationPort(integer): System Settings's Authentication port of RADIUS server. It is required for
                RADIUS server. The range is from 1 to 65535. E.g. 1812.
            ciscoIseDtos(list): System Settings's Cisco ISE Server DTOs (list of objects).
            externalCiscoIseIpAddrDtos(list): System Settings's For future use (list of objects).
            port(integer): System Settings's Port of TACACS server. It is required for TACACS server. The range is
                from 1 to 65535.
            protocol(string): System Settings's Type of protocol for authentication and policy server. If already
                saved with RADIUS, can update to RADIUS_TACACS. If already saved with TACACS, can update
                to RADIUS_TACACS . Available values are 'TACACS', 'RADIUS' and 'RADIUS_TACACS'.
            pxgridEnabled(boolean): System Settings's Value true for enable, false for disable. Default value is
                true.
            retries(string): System Settings's Number of communication retries between devices and authentication
                and policy server. The range is from 1 to 3.
            timeoutSeconds(string): System Settings's Number of seconds before timing out between devices and
                authentication and policy server. The range is from 2 to 20.
            useDnacCertForPxgrid(boolean): System Settings's Value true to use Catalyst Center certificate for
                Pxgrid. Default value is false.
            id(str): id path parameter. Authentication and Policy Server Identifier. Use 'Get Authentication and
                Policy Servers' intent API to find the identifier.
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
            https://developer.cisco.com/docs/dna-center/#!edit-authentication-and-policy-server-access-configuration
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
            "ciscoIseDtos": ciscoIseDtos,
            "pxgridEnabled": pxgridEnabled,
            "protocol": protocol,
            "retries": retries,
            "timeoutSeconds": timeoutSeconds,
            "externalCiscoIseIpAddrDtos": externalCiscoIseIpAddrDtos,
            "authenticationPort": authenticationPort,
            "accountingPort": accountingPort,
            "port": port,
            "useDnacCertForPxgrid": useDnacCertForPxgrid,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_fbdd94fbecd256c08e1d9f6e1a7657ac_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/authentication-policy-servers/{id}"
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
            "bpm_fbdd94fbecd256c08e1d9f6e1a7657ac_v3_2_3_0", json_data
        )

    def retrieves_cisco_spaces_accounts(
        self,
        limit=None,
        offset=None,
        order=None,
        region_name=None,
        headers=None,
        **request_parameters
    ):
        """Gets the names of existing Cisco Spaces accounts of the active registered Cisco.com Credential user. This is a
        pass-through to Cisco Spaces API, and the result could dynamically change. Accounts can be created and
        managed by visiting Cisco Spaces https://ciscospaces.io. A new account can also be created on behalf of
        the active Cisco.com Credential setting of Catalyst Center by integrating Catalyst Center to Cisco
        Spaces, using `POST /dna/intent/api/v1/locationServers/spaces` API.    `Prerequisite:` For this process
        to be successful, it is essential to have access to Cisco.com, and for the user to have access as well.
        It is of utmost importance to include the Cisco.com Credentials in the Catalyst Center for this API to
        operate correctly. All trusted certificates from Cisco.com need to be up-to-date in Catalyst Center.
        **Error Codes** | Code | Condition | | ---| --------| | **NCMP10050** | If there is no default Cisco.com
        Credential configured in System Settings |.

        Args:
            limit(int): limit query parameter. The number of records to show for this page.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1.
            order(str): order query parameter. Whether ascending or descending order should be used to sort the
                response.
            region_name(str): regionName query parameter. The Cisco Spaces region name to list accounts of.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-cisco-spaces-accounts
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        check_type(order, str)
        check_type(region_name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "limit": limit,
            "offset": offset,
            "order": order,
            "regionName": region_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/locationServers/spaces/accounts"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c68d6309e8af527280ec7ee6d5fb3e5d_v3_2_3_0", json_data
        )

    def custom_prompt_support_get_api(self, headers=None, **request_parameters):
        """Returns supported custom prompts by Catalyst Center.

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
            https://developer.cisco.com/docs/dna-center/#!custom-prompt-support-g-e-t-a-p-i
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

        e_url = "/dna/intent/api/v1/network-device/custom-prompt"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ada20dc4915d5901b50634628392e79f_v3_2_3_0", json_data
        )

    def custom_prompt_post_api(
        self,
        passwordPrompt=None,
        usernamePrompt=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Save custom prompt added by user in Catalyst Center. API will always override the existing prompts. User should
        provide all the custom prompt in case of any update.

        Args:
            passwordPrompt(string): System Settings's Password for Custom Prompt.
            usernamePrompt(string): System Settings's Username for Custom Prompt.
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
            https://developer.cisco.com/docs/dna-center/#!custom-prompt-p-o-s-t-a-p-i
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
            "usernamePrompt": usernamePrompt,
            "passwordPrompt": passwordPrompt,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d2ea814bfae85da1b77872d095fc8221_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/custom-prompt"
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
            "bpm_d2ea814bfae85da1b77872d095fc8221_v3_2_3_0", json_data
        )

    def activates_with_cisco_spaces_using_token_authentication(
        self,
        oneTimeUseToken=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Activate or re-activate Cisco Spaces integration using a one-time-use token generated from Cisco Spaces User
        Interface. Please refer to Cisco Spaces Configuration Guide at https://www.cisco.com for more
        information on generating a one-time-use token. Once activated, you can associate Cisco Spaces to one or
        more Site(s), using '/dna/intent/api/v1/sites/{id}/locationServerSettings'.  `Note:` The connection to
        Cisco Spaces will always flow through the configured System Proxy. When activating via this method,
        Catalyst Center or its configured Proxy Server must have access to https://ciscospaces.io, as well as
        the final account region url (e.g. https://ciscospaces.eu).  `Note:` The PKI Trustpool should contain
        all required TLS certificates to connect to Cisco Spaces prior to activation. Use
        '/dna/intent/api/v1/trustedCertificates/import' to import certificates.  `Note:` Re-activation is only
        permitted against the same Cisco Spaces account. To integrate a different account, first delete the
        Cisco Spaces integration, and then re-activate.

        Args:
            oneTimeUseToken(string): System Settings's Used during Cisco Spaces activation when activating using a
                one-time-use token generated from Cisco Spaces User Interface. Please refer to Cisco
                Spaces Configuration Guide at https://www.cisco.com for more information on generating a
                one-time-use token. .
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
            https://developer.cisco.com/docs/dna-center/#!activates-with-cisco-spaces-using-token-authentication
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
            "oneTimeUseToken": oneTimeUseToken,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_b1e014b05ac15c878c0ca4d93babebd6_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/locationServers/spaces/activateViaOne" + "TimeToken"
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
            "bpm_b1e014b05ac15c878c0ca4d93babebd6_v3_2_3_0", json_data
        )

    def delete_a_cmx_server_setting(self, id, headers=None, **request_parameters):
        """Delete the CMX Server.

        Args:
            id(str): id path parameter. The CMX Server resource Id.
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
            https://developer.cisco.com/docs/dna-center/#!delete-a-c-m-x-server-setting
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

        e_url = "/dna/intent/api/v1/locationServers/cmxServers/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cf5275474cb5580ba73bd64ba6244f3_v3_2_3_0", json_data
        )

    def updates_a_cmx_server_setting(
        self,
        id,
        connectionAddress=None,
        password=None,
        username=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Updates the CMX Server.

        Args:
            connectionAddress(): System Settings's The CMX Server connection address.
            id(string): System Settings's Cisco Spaces or CMX Server resource Id.
            password(string): System Settings's The password of the CMX Server user given.
            username(string): System Settings's The CMX Server username. This user must have full API read and write
                access.
            id(str): id path parameter. The CMX Server resource Id.
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
            https://developer.cisco.com/docs/dna-center/#!updates-a-c-m-x-server-setting
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
            "connectionAddress": connectionAddress,
            "username": username,
            "password": password,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e0fa184df58678ccbef5a68ed9d42_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/locationServers/cmxServers/{id}"
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
            "bpm_e0fa184df58678ccbef5a68ed9d42_v3_2_3_0", json_data
        )

    def gets_a_cmx_server_setting(self, id, headers=None, **request_parameters):
        """Gets a single CMX Server by Id.

        Args:
            id(str): id path parameter. The CMX Server resource Id.
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
            https://developer.cisco.com/docs/dna-center/#!gets-a-c-m-x-server-setting
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

        e_url = "/dna/intent/api/v1/locationServers/cmxServers/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ce47319bdcff5f7c9eeac6524f865900_v3_2_3_0", json_data
        )

    def add_authentication_and_policy_server_access_configuration(
        self,
        accountingPort=None,
        authenticationPort=None,
        ciscoIseDtos=None,
        encryptionKey=None,
        encryptionScheme=None,
        externalCiscoIseIpAddrDtos=None,
        ipAddress=None,
        isIseEnabled=None,
        messageKey=None,
        port=None,
        protocol=None,
        pxgridEnabled=None,
        retries=None,
        role=None,
        sharedSecret=None,
        timeoutSeconds=None,
        useDnacCertForPxgrid=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """API to add AAA/ISE server access configuration. Protocol can be configured as either RADIUS OR TACACS OR
        RADIUS_TACACS. If configuring Cisco ISE server, after configuration, use ‘Cisco ISE Server Integration
        Status’ Intent API to check the integration status. Based on integration status, if require use 'Accept
        Cisco ISE Server Certificate for Cisco ISE Server Integration' Intent API to accept the Cisco ISE
        certificate for Cisco ISE server integration, then use again ‘Cisco ISE Server Integration Status’
        Intent API to check the integration status.

        Args:
            accountingPort(integer): System Settings's Accounting port of RADIUS server. It is required for RADIUS
                server. The range is from 1 to 65535. E.g. 1813.
            authenticationPort(integer): System Settings's Authentication port of RADIUS server. It is required for
                RADIUS server. The range is from 1 to 65535. E.g. 1812.
            ciscoIseDtos(list): System Settings's Cisco ISE Server DTOs (list of objects).
            encryptionKey(string): System Settings's Encryption key used to encrypt shared secret.
            encryptionScheme(string): System Settings's Type of encryption scheme for additional security. Available
                values are 'KEYWRAP' and 'RADSEC'.
            externalCiscoIseIpAddrDtos(list): System Settings's For future use (list of objects).
            ipAddress(string): System Settings's IP address of authentication and policy server.
            isIseEnabled(boolean): System Settings's Value true for Cisco ISE Server. Default value is false.
            messageKey(string): System Settings's Message key used to encrypt shared secret.
            port(integer): System Settings's Port of TACACS server. It is required for TACACS server. The range is
                from 1 to 65535.
            protocol(string): System Settings's Type of protocol for authentication and policy server. If already
                saved with RADIUS, can update to RADIUS_TACACS. If already saved with TACACS, can update
                to RADIUS_TACACS . Available values are 'TACACS', 'RADIUS' and 'RADIUS_TACACS'.
            pxgridEnabled(boolean): System Settings's Value true for enable, false for disable. Default value is
                true.
            retries(string): System Settings's Number of communication retries between devices and authentication
                and policy server. The range is from 1 to 3.
            role(string): System Settings's Role of authentication and policy server. E.g. primary, secondary.
            sharedSecret(string): System Settings's Shared secret between devices and authentication and policy
                server .
            timeoutSeconds(string): System Settings's Number of seconds before timing out between devices and
                authentication and policy server. The range is from 2 to 20.
            useDnacCertForPxgrid(boolean): System Settings's Value true to use Catalyst Center certificate for
                Pxgrid. Default value is false.
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
            https://developer.cisco.com/docs/dna-center/#!add-authentication-and-policy-server-access-configuration
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
            "authenticationPort": authenticationPort,
            "accountingPort": accountingPort,
            "ciscoIseDtos": ciscoIseDtos,
            "ipAddress": ipAddress,
            "pxgridEnabled": pxgridEnabled,
            "useDnacCertForPxgrid": useDnacCertForPxgrid,
            "isIseEnabled": isIseEnabled,
            "port": port,
            "protocol": protocol,
            "retries": retries,
            "role": role,
            "sharedSecret": sharedSecret,
            "timeoutSeconds": timeoutSeconds,
            "encryptionScheme": encryptionScheme,
            "messageKey": messageKey,
            "encryptionKey": encryptionKey,
            "externalCiscoIseIpAddrDtos": externalCiscoIseIpAddrDtos,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_fa3975be5af25501abb40339d96917eb_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/authentication-policy-servers"
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
            "bpm_fa3975be5af25501abb40339d96917eb_v3_2_3_0", json_data
        )

    def get_authentication_and_policy_servers(
        self,
        is_ise_enabled=None,
        role=None,
        state=None,
        headers=None,
        **request_parameters
    ):
        """API to get Authentication and Policy Servers.

        Args:
            is_ise_enabled(bool): isIseEnabled query parameter. Valid values are : true, false.
            state(str): state query parameter. Valid values are: ACTIVE, DELETED, FAILED, INACTIVE, INPROGRESS,
                RBAC-FAILURE, RBAC-SUCCESS.
            role(str): role query parameter. Authentication and Policy Server Role (Example: primary, secondary).
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
            https://developer.cisco.com/docs/dna-center/#!get-authentication-and-policy-servers
        """
        check_type(headers, dict)
        check_type(is_ise_enabled, bool)
        check_type(state, str)
        check_type(role, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "isIseEnabled": is_ise_enabled,
            "state": state,
            "role": role,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/authentication-policy-servers"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f7cc2592721f5b9b9f99795a26130147_v3_2_3_0", json_data
        )

    def get_provisioning_settings(self, headers=None, **request_parameters):
        """Returns provisioning settings.

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
            https://developer.cisco.com/docs/dna-center/#!get-provisioning-settings
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

        e_url = "/dna/intent/api/v1/provisioningSettings"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b2e5d0e7f80b555f865bb1f72c4d7bdd_v3_2_3_0", json_data
        )

    def set_provisioning_settings(
        self,
        requireItsmApproval=None,
        requirePreview=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Sets provisioning settings.

        Args:
            requireItsmApproval(boolean): System Settings's If require ITSM approval is enabled, the planned
                configurations must be submitted for ITSM approval. Also if enabled, requirePreview will
                default to enabled.
            requirePreview(boolean): System Settings's If require preview is enabled, the device configurations must
                be reviewed before deploying them.
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
            https://developer.cisco.com/docs/dna-center/#!set-provisioning-settings
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
            "requireItsmApproval": requireItsmApproval,
            "requirePreview": requirePreview,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_b3ab480a3f485ecc9fef1bd2f8c9d109_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/provisioningSettings"
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
            "bpm_b3ab480a3f485ecc9fef1bd2f8c9d109_v3_2_3_0", json_data
        )

    def counts_cisco_spaces_accounts(
        self, region_name=None, headers=None, **request_parameters
    ):
        """Gets the count of existing Cisco Spaces accounts of the active registered Cisco.com Credential user. This is a
        pass-through to Cisco Spaces API, and the result could dynamically change.    `Prerequisite:` For this
        process to be successful, it is essential to have access to Cisco.com, and for the user to have access
        as well. It is of utmost importance to include the Cisco.com Credentials in the Catalyst Center for this
        API to operate correctly. All trusted certificates from Cisco.com need to be up-to-date in Catalyst
        Center.

        Args:
            region_name(str): regionName query parameter. The Cisco Spaces region name to list accounts of.
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
            https://developer.cisco.com/docs/dna-center/#!counts-cisco-spaces-accounts
        """
        check_type(headers, dict)
        check_type(region_name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "regionName": region_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/locationServers/spaces/accounts/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_aded9fcbdfb53a69ce3f93861851459_v3_2_3_0", json_data
        )

    def activates_existing_cisco_spaces_account_using_cisco_com_credentials(
        self,
        accountName=None,
        inviteAdminEmails=None,
        region=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Activate or Re-activate with an existing Cisco Spaces account by using using the Catalyst Center configured
        Cisco.com Credentials. To get the list of users current accounts, use `GET
        /dna/intent/api/v1/locationServers/spaces/accounts` API. Once activated, you can associate Cisco Spaces
        to one or more Site(s), using '/dna/intent/api/v1/sites/{id}/locationServerSettings'.  `Note:`
        Activating with Cisco Spaces using Cisco.com credentials permits Cisco Spaces to make API calls back to
        Catalyst Center on behalf of the user using the Cisco.com Credential SSO context.  `Note:` The
        connection to Cisco Spaces will always flow through the configured System Proxy. When activating via
        this method, Catalyst Center or its configured Proxy Server must have access to https://ciscospaces.io,
        as well as the final account region url (e.g. https://ciscospaces.eu).  `Note:` The PKI Trustpool should
        contain all required TLS certificates to connect to Cisco Spaces prior to activation. Use
        '/dna/intent/api/v1/trustedCertificates/import' to import certificates.  `Note:` Re-activation is only
        permitted against the same Cisco Spaces account. To integrate a different account, first delete the
        Cisco Spaces integration, and then re-activate.

        Args:
            accountName(string): System Settings's The name of an existing Cisco Spaces account to activate with. To
                get a list of accounts of the current user, use `GET
                /dna/intent/api/v1/locationServers/spaces/accounts` API.
            inviteAdminEmails(list): System Settings's Optional list of email addresses to make as administrators of
                the Cisco Spaces account. Cisco Spaces will send an automated email to invite the users
                to the Cisco Spaces account. (list of strings).
            region(string): System Settings's The Cisco Spaces region the account is in. Must be one of 'regions'
                values from `GET /dna/intent/api/v1/locationServers/spaces/regions`, and must be valid
                for the account name given. Note that the same account name can exist across multiple
                regions.
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
            https://developer.cisco.com/docs/dna-center/#!activates-existing-cisco-spaces-account-using-cisco-com-credentials
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
            "accountName": accountName,
            "region": region,
            "inviteAdminEmails": inviteAdminEmails,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_b41b600bf4ee50cea7277f3410ad5266_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/locationServers/spaces/activateViaCco"
            + "CredentialsWithExistingAccount"
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
            "bpm_b41b600bf4ee50cea7277f3410ad5266_v3_2_3_0", json_data
        )

    def cisco_ise_server_integration_status(self, headers=None, **request_parameters):
        """API to check Cisco ISE server integration status.

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
            https://developer.cisco.com/docs/dna-center/#!cisco-i-s-e-server-integration-status
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

        e_url = "/dna/intent/api/v1/ise-integration-status"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a1bc4f82533a5d909ed345b4703cff8a_v3_2_3_0", json_data
        )

    def retrieves_cmx_server_settings(
        self,
        connection_address=None,
        limit=None,
        offset=None,
        order=None,
        headers=None,
        **request_parameters
    ):
        """Gets the Cisco Connected Mobile Experiences (CMX) Servers list. To learn more about CMX Servers, visit
        https://www.cisco.com.

        Args:
            limit(int): limit query parameter. The number of records to show for this page.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1.
            order(str): order query parameter. Whether ascending or descending order should be used to sort the
                response.
            connection_address(str): connectionAddress query parameter. The CMX Server connection address.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-c-m-x-server-settings
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        check_type(order, str)
        check_type(connection_address, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "limit": limit,
            "offset": offset,
            "order": order,
            "connectionAddress": connection_address,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/locationServers/cmxServers"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d451c0b1e0445fe3a458791df8e9d409_v3_2_3_0", json_data
        )

    def creates_a_cmx_server_setting(
        self,
        connectionAddress=None,
        id=None,
        password=None,
        username=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Creates a CMX Server connection. Once added, you can associate the CMX Server to one or more Site(s), using
        '/dna/intent/api/v1/sites/{id}/locationServerSettings'.  `Note:` The connection to CMX Server does not
        leverage the configured System Proxy. Catalyst Center must have direct network access to the CMX Server.
        `Note:` The PKI Trustpool should contain all required TLS certificates to connect to the CMX Server
        prior to activation. Use '/dna/intent/api/v1/trustedCertificates/import' to import certificates. The CMX
        Server must list the connection address given as the Common Name or as a Subject Alternative Name in its
        configured certificate. See CMX Configuration Guide  at https://www.cisco.com for information on
        configuring the CMX TLS certificate.

        Args:
            connectionAddress(): System Settings's The CMX Server connection address.
            id(string): System Settings's Cisco Spaces or CMX Server resource Id.
            password(string): System Settings's The password of the CMX Server user given.
            username(string): System Settings's The CMX Server username. This user must have full API read and write
                access.
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
            https://developer.cisco.com/docs/dna-center/#!creates-a-c-m-x-server-setting
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
            "connectionAddress": connectionAddress,
            "username": username,
            "password": password,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_fbefd8666583d81cba5dadd05b93f_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/locationServers/cmxServers"
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
            "bpm_fbefd8666583d81cba5dadd05b93f_v3_2_3_0", json_data
        )

    def counts_cmx_server_settings(
        self,
        connection_address=None,
        limit=None,
        offset=None,
        order=None,
        headers=None,
        **request_parameters
    ):
        """Gets the count of CMX Servers.

        Args:
            limit(int): limit query parameter. The number of records to show for this page.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1.
            order(str): order query parameter. Whether ascending or descending order should be used to sort the
                response.
            connection_address(str): connectionAddress query parameter. The CMX Server connection address.
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
            https://developer.cisco.com/docs/dna-center/#!counts-c-m-x-server-settings
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        check_type(order, str)
        check_type(connection_address, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "limit": limit,
            "offset": offset,
            "order": order,
            "connectionAddress": connection_address,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/locationServers/cmxServers/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f015139af3c3555f8ecb15fec5c0cfc8_v3_2_3_0", json_data
        )

    def creates_configuration_details_of_the_external_ipam_server(
        self,
        password=None,
        provider=None,
        serverName=None,
        serverUrl=None,
        state=None,
        syncView=None,
        userName=None,
        view=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Creates configuration details of the external IPAM server. You should only create one external IPAM server;
        delete any existing external server before creating a new one.  To enable communication with an external
        IPAM server that has a certificate that may not be trusted, add the certificate via `POST
        /intent/api/v1/trustedCertificates/import`.

        Args:
            password(string): System Settings's The password for the external IPAM server login username.
            provider(): System Settings's provider.
            serverName(string): System Settings's A descriptive name of this external server, used for
                identification purposes.
            serverUrl(string): System Settings's The URL of this external server.
            state(string): System Settings's State of the the external IPAM. * OK indicates success of most recent
                periodic communication check with external IPAM. * CRITICAL indicates failure of most
                recent attempt to communicate with the external IPAM. * SYNCHRONIZING indicates that the
                process of synchronizing the external IPAM database with the local IPAM database is
                running and all other IPAM processes will be blocked until the completes. * DISCONNECTED
                indicates the external IPAM is no longer being used.. Available values are 'OK',
                'CRITICAL', 'SYNCHRONIZING' and 'DISCONNECTED'.
            syncView(boolean): System Settings's Synchronize the IP pools from the local IPAM to this external
                server.
            userName(string): System Settings's The external IPAM server login username.
            view(string): System Settings's The view under which pools are created in the external IPAM server.
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
            https://developer.cisco.com/docs/dna-center/#!creates-configuration-details-of-the-external-i-p-a-m-server
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
            "serverName": serverName,
            "serverUrl": serverUrl,
            "userName": userName,
            "password": password,
            "view": view,
            "syncView": syncView,
            "state": state,
            "provider": provider,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator("jsd_d6d7d5c8983c1d3c9815bfd35_v3_2_3_0").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/ipam/serverSetting"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory("bpm_d6d7d5c8983c1d3c9815bfd35_v3_2_3_0", json_data)

    def retrieves_configuration_details_of_the_external_ipam_server(
        self, headers=None, **request_parameters
    ):
        """Retrieves configuration details of the external IPAM server.  If an external IPAM server has not been created,
        this resource will return a `404` response.

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
            https://developer.cisco.com/docs/dna-center/#!retrieves-configuration-details-of-the-external-i-p-a-m-server
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

        e_url = "/dna/intent/api/v1/ipam/serverSetting"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f06b38c5915162acc31afbf33b843e_v3_2_3_0", json_data
        )

    def updates_configuration_details_of_the_external_ipam_server(
        self,
        password=None,
        provider=None,
        serverName=None,
        serverUrl=None,
        state=None,
        syncView=None,
        userName=None,
        view=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Updates configuration details of the external IPAM server.

        Args:
            password(string): System Settings's The password for the external IPAM server login username.
            provider(): System Settings's provider.
            serverName(string): System Settings's A descriptive name of this external server, used for
                identification purposes.
            serverUrl(string): System Settings's The URL of this external server.
            state(string): System Settings's State of the the external IPAM. * OK indicates success of most recent
                periodic communication check with external IPAM. * CRITICAL indicates failure of most
                recent attempt to communicate with the external IPAM. * SYNCHRONIZING indicates that the
                process of synchronizing the external IPAM database with the local IPAM database is
                running and all other IPAM processes will be blocked until the completes. * DISCONNECTED
                indicates the external IPAM is no longer being used.. Available values are 'OK',
                'CRITICAL', 'SYNCHRONIZING' and 'DISCONNECTED'.
            syncView(boolean): System Settings's Synchronize the IP pools from the local IPAM to this external
                server.
            userName(string): System Settings's The external IPAM server login username.
            view(string): System Settings's The view under which pools are created in the external IPAM server.
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
            https://developer.cisco.com/docs/dna-center/#!updates-configuration-details-of-the-external-i-p-a-m-server
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
            "serverName": serverName,
            "serverUrl": serverUrl,
            "userName": userName,
            "password": password,
            "view": view,
            "syncView": syncView,
            "state": state,
            "provider": provider,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ba98ed72975099b39dd2dc4cb65ed8_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/ipam/serverSetting"
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
            "bpm_ba98ed72975099b39dd2dc4cb65ed8_v3_2_3_0", json_data
        )

    def deletes_configuration_details_of_the_external_ipam_server(
        self, headers=None, **request_parameters
    ):
        """Deletes configuration details of the external IPAM server.

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
            https://developer.cisco.com/docs/dna-center/#!deletes-configuration-details-of-the-external-i-p-a-m-server
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

        e_url = "/dna/intent/api/v1/ipam/serverSetting"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f47e2181ce5957818a97f135a5eb9f_v3_2_3_0", json_data
        )

    def creates_new_cisco_spaces_account_using_cisco_com_credentials(
        self,
        accountName=None,
        inviteAdminEmails=None,
        region=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Activate Cisco Spaces integration by using the Catalyst Center configured Cisco.com Credentials. When creating a
        new account, you must not give the name of an existing account, and the Cisco Spaces 'region' must also
        be provided, in which case it is taken to mean that a new account will be created within the requested
        region. To get the list of users current accounts, use `GET
        /dna/intent/api/v1/locationServers/spaces/accounts` API. Once activated, you can associate Cisco Spaces
        to one or more Site(s), using '/dna/intent/api/v1/sites/{id}/locationServerSettings'.  `Note:`
        Activating with Cisco Spaces using Cisco.com credentials permits Cisco Spaces to make API calls back to
        Catalyst Center on behalf of the user using the Cisco.com Credential SSO context.  `Note:` The
        connection to Cisco Spaces will always flow through the configured System Proxy. When activating via
        this method, Catalyst Center or its configured Proxy Server must have access to https://ciscospaces.io,
        as well as the final account region url (e.g. https://ciscospaces.eu).  `Note:` The PKI Trustpool should
        contain all required TLS certificates to connect to Cisco Spaces prior to activation. Use
        '/dna/intent/api/v1/trustedCertificates/import' to import certificates.  `Note:` If the connection to
        Cisco Spaces expires, and needs to re-reactivated, do not use this API again. Use `POST
        /dna/intent/api/v1/locationServers/spaces/activateViaCcoCredentialsWithExistingAccount` API to re-
        activate with Cisco Spaces to the previously created account.  `Note:` Re-activation is only permitted
        against the same Cisco Spaces account. To integrate a different account, first delete the Cisco Spaces
        integration, and then re-activate.

        Args:
            accountName(string): System Settings's The name of the account to create in Cisco Spaces. Must not be
                the name of an existing account of the user. To get a list of accounts of current user,
                use `GET /dna/intent/api/v1/locationServers/spaces/accounts` API.
            inviteAdminEmails(list): System Settings's Optional list of email addresses to make as administrators of
                the Cisco Spaces account. Cisco Spaces will send an automated email to invite the users
                to the Cisco Spaces account. (list of strings).
            region(string): System Settings's The Cisco Spaces region to create the account in. Must be one of
                'regions' values from `GET /dna/intent/api/v1/locationServers/spaces/regions` API.
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
            https://developer.cisco.com/docs/dna-center/#!creates-new-cisco-spaces-account-using-cisco-com-credentials
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
            "accountName": accountName,
            "region": region,
            "inviteAdminEmails": inviteAdminEmails,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_fa1905c13f0d5c54b5b854eaf94d8eda_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/locationServers/spaces/activateViaCco"
            + "CredentialsWithNewAccount"
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
            "bpm_fa1905c13f0d5c54b5b854eaf94d8eda_v3_2_3_0", json_data
        )

    def retrieves_cisco_spaces_regions(
        self, limit=None, offset=None, order=None, headers=None, **request_parameters
    ):
        """Gets the list of supported Cisco Spaces regions, which can be used when activating a new Cisco Spaces account.
        This is a pass-through to Cisco Spaces API, and the result could dynamically change.    `Prerequisite:`
        For this process to be successful, it is essential to have access to Cisco.com, and for the user to have
        access as well. It is of utmost importance to include the Cisco.com Credentials in the Catalyst Center
        for this API to operate correctly. All trusted certificates from Cisco.com need to be up-to-date in
        Catalyst Center.

        Args:
            limit(int): limit query parameter. The number of records to show for this page.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-cisco-spaces-regions
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        check_type(order, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
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

        e_url = "/dna/intent/api/v1/locationServers/spaces/regions"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c84c07b1411e51b1b26eb27ebff35a0f_v3_2_3_0", json_data
        )

    def gets_a_cmx_server_ca_certificate(
        self, connection_address, headers=None, **request_parameters
    ):
        """Gets the CA certificate details, if available, of a CMX Server by connection address. This can be used to
        establish trust with the CMX Server within Catalyst Center, by saving the `certificate` attribute as a
        `.pem` file and uploading through `POST /dna/intent/api/v1/trustedCertificates/import` API. The content
        of the certificate must be reviewed and validated by the end user to ensure they trust the certificate
        that is presented prior to importing into Catalyst Center.

        Args:
            connection_address(str): connectionAddress query parameter. The CMX Server connection address, same as
                would be entered by user when adding a CMX Server integration and through `POST
                /dna/intent/api/v1/locationServers/cmxServers` API.
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
            https://developer.cisco.com/docs/dna-center/#!gets-a-c-m-x-server-c-a-certificate
        """
        check_type(headers, dict)
        check_type(connection_address, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "connectionAddress": connection_address,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/locationServers/cmxServers/certificat" + "e"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_af7c1bebc571faa064106ebedb7f2_v3_2_3_0", json_data
        )

    def counts_cisco_spaces_regions(self, headers=None, **request_parameters):
        """Gets the number of supported Cisco Spaces regions, which can be used when activating a new Cisco Spaces account.
        This is a pass-through to Cisco Spaces API, and the result could dynamically change.    `Prerequisite:`
        For this process to be successful, it is essential to have access to Cisco.com, and for the user to have
        access as well. It is of utmost importance to include the Cisco.com Credentials in the Catalyst Center
        for this API to operate correctly. All trusted certificates from Cisco.com need to be up-to-date in
        Catalyst Center.

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
            https://developer.cisco.com/docs/dna-center/#!counts-cisco-spaces-regions
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

        e_url = "/dna/intent/api/v1/locationServers/spaces/regions/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ca7a1f8c2154ffa55a7dd6e4cd1102_v3_2_3_0", json_data
        )

    def retrieves_cisco_spaces_settings(self, headers=None, **request_parameters):
        """Gets the current Cisco Spaces integration setting. To learn more about Cisco Spaces, visit
        https://spaces.cisco.com.

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
            https://developer.cisco.com/docs/dna-center/#!retrieves-cisco-spaces-settings
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

        e_url = "/dna/intent/api/v1/locationServers/spaces"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f96d291f9c05acab29b44ace7f870d0_v3_2_3_0", json_data
        )

    def deletes_cisco_spaces_settings(self, headers=None, **request_parameters):
        """Deactivate Catalyst Center from Cisco Spaces.  `Note:` This does not delete your Cisco Spaces account, this
        simply stops the integration between the Catalyst Center and Cisco Spaces. In the case that the
        integration was performed using a one-time-use token, a request is sent to Cisco Spaces to revoke the
        API Key that was exchanged during initial integration so that it becomes inactive. In the case that the
        integration was performed using Cisco.com Credential, a request is sent to Cisco Spaces to de-activate
        the SSO context. If API calls back to Catalyst Center were permitted during initial activation, the same
        request is taken to mean by Cisco Spaces it is no longer permitted to make API calls to Catalyst Center
        with that context.

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
            https://developer.cisco.com/docs/dna-center/#!deletes-cisco-spaces-settings
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

        e_url = "/dna/intent/api/v1/locationServers/spaces"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a0e604aa7ce3522db24cb3e5392f8cb0_v3_2_3_0", json_data
        )

    def accept_cisco_ise_server_certificate_for_cisco_ise_server_integration(
        self,
        id,
        isCertAcceptedByUser=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """API to accept Cisco ISE server certificate for Cisco ISE server integration. Use ‘Cisco ISE Server Integration
        Status’ Intent API to check the integration status. This API can be used to retry the failed
        integration.

        Args:
            isCertAcceptedByUser(boolean): System Settings's Value true for accept, false for deny. Remove this
                field and send empty request payload ( {} ) to retry the failed integration.
            id(str): id path parameter. Cisco ISE Server Identifier. Use 'Get Authentication and Policy Servers'
                intent API to find the identifier.
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
            https://developer.cisco.com/docs/dna-center/#!accept-cisco-i-s-e-server-certificate-for-cisco-i-s-e-server-integration
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
            "isCertAcceptedByUser": isCertAcceptedByUser,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e0ed6b9a530ea05d77a199ded4e3_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/integrate-ise/{id}"
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
            "bpm_e0ed6b9a530ea05d77a199ded4e3_v3_2_3_0", json_data
        )
