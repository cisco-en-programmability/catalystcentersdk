"""Cisco Catalyst Center User and Roles API wrapper.

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


class UserAndRoles:
    """Cisco Catalyst Center User and Roles API (version: 3.2.3.0).

    Wraps the Catalyst Center User and Roles
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new UserAndRoles
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

    def add_role(
        self,
        description=None,
        name=None,
        permissions=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Add a new role into system (v2).This API is intended to allow users to create roles based on the new set of
        permissions returned by the v2 Get permissions API (GET /dna/system/api/v2/roles/permissions). There are
        a few key differences between the v1 Get permissions API and the v2 version. Please refer to the v2 Get
        permissions API for more details. The JSON payload for this API accepts a list of permissions. Every
        permission can be assigned either "Read", "Write", or "Deny" privilege. Any permissions from the v2 Get
        permissions API that are not included in the payload, will be assigned a privilege based on the on the
        following priority: 1. The minium privilege of the permission. 2. The privilege assigned to the parent
        permission (if provided in the JSON payload). 3. The minimum privilege required to satisfy all inbound
        dependencies. 4. The default privilege of the permission.

        Args:
            description(string): User and Roles's Description of role.
            name(string): User and Roles's Name of the role.
            permissions(list): User and Roles's List of permissions to be associated with the role. (list of
                objects).
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
            https://developer.cisco.com/docs/dna-center/#!add-role
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
            "name": name,
            "description": description,
            "permissions": permissions,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ae10ec6705f368476f7b35918122c_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/system/api/v2/roles"
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
            "bpm_ae10ec6705f368476f7b35918122c_v3_2_3_0", json_data
        )

    def add_role_v2(
        self,
        description=None,
        name=None,
        permissions=None,
        headers=None,
        payload=None,
        active_validation=True,
        **query_parameters
    ):
        """Alias for `add_role <#catalystcentersdk.
        api.v3_2_3_0.user_and_roles.
        UserAndRoles.add_role>`_
        """
        return self.add_role(
            description=description,
            name=name,
            permissions=permissions,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_roles(self, headers=None, **request_parameters):
        """Get all roles in the system (v2).This API is the successor to the v1 Get roles API (GET
        /dna/system/api/v1/role). It can be used to get all roles that exist in the system, regardless of
        whether it was created using the v1 Add role API (POST /dna/system/api/v1/role) or the v2 Add role API
        (POST /dna/system/api/v2/roles).

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
            https://developer.cisco.com/docs/dna-center/#!get-roles
        """
        check_type(headers, dict)
        if headers is not None:
            if "invokeSource" in headers:
                check_type(headers.get("invokeSource"), str, may_be_none=False)
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

        e_url = "/dna/system/api/v2/roles"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b161299c9bf53a6a7e3a96423078979_v3_2_3_0", json_data
        )

    def get_roles_v2(self, headers=None, **query_parameters):
        """Alias for `get_roles <#catalystcentersdk.
        api.v3_2_3_0.user_and_roles.
        UserAndRoles.get_roles>`_
        """
        return self.get_roles(headers=headers, **query_parameters)

    def get_access_group(self, id, headers=None, **request_parameters):
        """Get an access group in the system.This API provides the ability to get an access group that has already been
        created. Please refer to the Add access group API for more details about access groups.

        Args:
            id(str): id path parameter. Id of the access group to query.
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
            https://developer.cisco.com/docs/dna-center/#!get-access-group
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

        e_url = "/dna/system/api/v1/accessGroups/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dd672e37d95873b4e2e421337c0021_v3_2_3_0", json_data
        )

    def delete_access_group(self, id, headers=None, **request_parameters):
        """Delete an access group from the system.

        Args:
            id(str): id path parameter. Id of the access group to be deleted.
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
            https://developer.cisco.com/docs/dna-center/#!delete-access-group
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

        e_url = "/dna/system/api/v1/accessGroups/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ce98bb0519af5ae0b6db8711fa21dfc1_v3_2_3_0", json_data
        )

    def update_access_group(
        self,
        id,
        description=None,
        resourceGroups=None,
        role=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Update an access group in the system.

        Args:
            description(string): User and Roles's Description of the access group.
            resourceGroups(list): User and Roles's List of sites to be associated with the access group. (list of
                objects).
            role(list): User and Roles's List of role names. (list of strings).
            id(str): id path parameter. Id of the access group to update.
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
            https://developer.cisco.com/docs/dna-center/#!update-access-group
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
            "description": description,
            "resourceGroups": resourceGroups,
            "role": role,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f6255ed55aab8b55879cda83511_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/system/api/v1/accessGroups/{id}"
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
            "bpm_f6255ed55aab8b55879cda83511_v3_2_3_0", json_data
        )

    def delete_user_api(self, user_id, headers=None, **request_parameters):
        """Delete a user in the system.

        Args:
            user_id(str): userId path parameter. The id of the user to be deleted.
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
            https://developer.cisco.com/docs/dna-center/#!delete-user-a-p-i
        """
        check_type(headers, dict)
        check_type(user_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "userId": user_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/system/api/v1/user/{userId}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c65c6cc65f068766cbb8a42ad387_v3_2_3_0", json_data
        )

    def get_roles_api_v1(self, headers=None, **request_parameters):
        """Get all roles in the system.

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
            https://developer.cisco.com/docs/dna-center/#!get-roles-a-p-i-v1
        """
        check_type(headers, dict)
        if headers is not None:
            if "invokeSource" in headers:
                check_type(headers.get("invokeSource"), str, may_be_none=False)
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

        e_url = "/dna/system/api/v1/roles"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bef02e8f6f8354dc99e375826a87c88c_v3_2_3_0", json_data
        )

    def get_roles_api(self, headers=None, **query_parameters):
        """Alias for `get_roles_api_v1 <#catalystcentersdk.
        api.v3_2_3_0.user_and_roles.
        UserAndRoles.get_roles_api_v1>`_
        """
        return self.get_roles_api_v1(headers=headers, **query_parameters)

    def get_access_group_count(self, headers=None, **request_parameters):
        """Get the total number of access groups in the system.

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
            https://developer.cisco.com/docs/dna-center/#!get-access-group-count
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

        e_url = "/dna/system/api/v1/accessGroups/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_aeaa97a391359e9aa046d39f163bed2_v3_2_3_0", json_data
        )

    def get_permissions_api(self, headers=None, **request_parameters):
        """Get permissions for a role in the system.

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
            https://developer.cisco.com/docs/dna-center/#!get-permissions-a-p-i
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

        e_url = "/dna/system/api/v1/role/permissions"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ec0b30eca9d540a845848cffd7c602a_v3_2_3_0", json_data
        )

    def get_users_api(self, auth_source=None, headers=None, **request_parameters):
        """Get all users in the system.

        Args:
            auth_source(str): authSource query parameter. The source that authenticates the user. The value of this
                query parameter can be set to "internal" or "external". If not provided, then all users
                will be returned in the response.
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
            https://developer.cisco.com/docs/dna-center/#!get-users
        """
        check_type(headers, dict)
        check_type(auth_source, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "authSource": auth_source,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/system/api/v1/user"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fa405b6d1be56739f2dfeea63212015_v3_2_3_0", json_data
        )

    def add_user_api(
        self,
        accessGroups=None,
        email=None,
        firstName=None,
        lastName=None,
        password=None,
        roleList=None,
        username=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Add a new user in the system.This API provides the ability create a user in the system. A user represents a
        human that desires to access and manage resources provided by the system. It is recommended to use
        'accessGroups' (list of access group ids) in the input instead of role's name in roleList from the
        current release onwards.

        Args:
            accessGroups(list): User and Roles's List of access groups that will be assigned to the user. The first
                access group in the list will be the default access group activated when the user
                authenticates. (list of strings).
            email(string): User and Roles's The email address of the user.
            firstName(string): User and Roles's The first name of the user.
            lastName(string): User and Roles's The last name of the user.
            password(string): User and Roles's The password of the user.
            roleList(list): User and Roles's Role id list. (list of strings).
            username(string): User and Roles's The username of the user.
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
            https://developer.cisco.com/docs/dna-center/#!add-user
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
            "firstName": firstName,
            "lastName": lastName,
            "username": username,
            "password": password,
            "email": email,
            "roleList": roleList,
            "accessGroups": accessGroups,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d82755e5e03510daf0951c1f42c2702_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/system/api/v1/user"
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
            "bpm_d82755e5e03510daf0951c1f42c2702_v3_2_3_0", json_data
        )

    def update_user_api(
        self,
        accessGroups=None,
        email=None,
        firstName=None,
        lastName=None,
        roleList=None,
        userId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Update a user in the system. It is recommended to use 'accessGroups' (list of access group ids) in the input
        instead of role's name in roleList from the current release onwards. Please refer to the add user API
        (POST /dna/system/api/v1/user) for more details about users.

        Args:
            accessGroups(list): User and Roles's Access group id list. (list of strings).
            email(string): User and Roles's email should be set if the original value is not empty.
            firstName(string): User and Roles's firstName should be set if the original value is not empty.
            lastName(string): User and Roles's lastName should be set if the original value is not empty.
            roleList(list): User and Roles's Role id list. (list of strings).
            userId(string): User and Roles's userId.
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
            https://developer.cisco.com/docs/dna-center/#!update-user
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
            "firstName": firstName,
            "lastName": lastName,
            "email": email,
            "userId": userId,
            "roleList": roleList,
            "accessGroups": accessGroups,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d2bd5f05bd535a89ebadb30e2ede9e_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/system/api/v1/user"
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
            "bpm_d2bd5f05bd535a89ebadb30e2ede9e_v3_2_3_0", json_data
        )

    def add_role_api(
        self,
        description=None,
        resourceTypes=None,
        role=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Add a new role in the system.

        Args:
            description(string): User and Roles's Description of role.
            resourceTypes(list): User and Roles's Only include resourceTypes that you wish to grant one or more of
                the four operations mentioned below. Exclude any resourceTypes that you do not want to
                grant permission to. (list of objects).
            role(string): User and Roles's Name of the role.
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
            https://developer.cisco.com/docs/dna-center/#!add-role-a-p-i
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
            "role": role,
            "description": description,
            "resourceTypes": resourceTypes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a88c7510a15578b8eb2df183a92d5d_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/system/api/v1/role"
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
            "bpm_a88c7510a15578b8eb2df183a92d5d_v3_2_3_0", json_data
        )

    def update_role_api(
        self,
        description=None,
        resourceTypes=None,
        roleId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Update a role in the system. Deprecated since release 3.1.3. Alternative: PUT /dna/system/api/v2/roles/${id}.

        Args:
            description(string): User and Roles's Description of the role.
            resourceTypes(list): User and Roles's Only include resourceTypes that you wish to grant one or more of
                the four operations mentioned below. Exclude any resourceTypes that you do not want to
                grant permission to. (list of objects).
            roleId(string): User and Roles's Id of the role.
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
            https://developer.cisco.com/docs/dna-center/#!update-role-a-p-i
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
            "roleId": roleId,
            "description": description,
            "resourceTypes": resourceTypes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ff5bf5a67c6c5c0aa9e7ba84c088e1a6_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/system/api/v1/role"
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
            "bpm_ff5bf5a67c6c5c0aa9e7ba84c088e1a6_v3_2_3_0", json_data
        )

    def get_aaa_attribute_api(self, headers=None, **request_parameters):
        """Get the current value of the custom AAA attribute.

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
            https://developer.cisco.com/docs/dna-center/#!get-a-a-a-attribute-a-p-i
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

        e_url = "/dna/system/api/v1/users/external-servers/aaa-attribute"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bedf83096a45ad1beaaa1fc6c192103_v3_2_3_0", json_data
        )

    def add_and_update_aaa_attribute_api(
        self,
        attributeName=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Add or update the custom AAA attribute for external authentication. Note that if you decide not to set the
        custom AAA attribute, a default AAA attribute will be used for authentication based on the protocol
        supported by your server. For TACACS servers it will be "cisco-av-pair" and for RADIUS servers it will
        be "Cisco-AVPair".

        Args:
            attributeName(string): User and Roles's name of the custom AAA attribute.
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
            https://developer.cisco.com/docs/dna-center/#!add-and-update-a-a-a-attribute-a-p-i
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
            "attributeName": attributeName,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f5bfccc7e30550baa7046f74daa1ef2_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/system/api/v1/users/external-servers/aaa-attribute"
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
            "bpm_f5bfccc7e30550baa7046f74daa1ef2_v3_2_3_0", json_data
        )

    def delete_aaa_attribute_api(self, headers=None, **request_parameters):
        """Delete the custom AAA attribute that was added. Note that by deleting the AAA attribute, a default AAA attribute
        will be used for authentication based on the protocol supported by your server. For TACACS servers it
        will be "cisco-av-pair" and for RADIUS servers it will be "Cisco-AVPair".

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
            https://developer.cisco.com/docs/dna-center/#!delete-a-a-a-attribute-a-p-i
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

        e_url = "/dna/system/api/v1/users/external-servers/aaa-attribute"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f20c99b436bd5be8bdb9094db3a47f01_v3_2_3_0", json_data
        )

    def manage_external_authentication_setting_api(
        self,
        enable=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Enable or disable external authentication in the System.  Please find the Administrator Guide for your
        particular release from the list linked below and follow the steps required to enable external
        authentication before trying to do so from this API.  https://www.cisco.com/c/en/us/support/cloud-
        systems-management/dna-center/products-maintenance-guides-list.html.

        Args:
            enable(boolean): User and Roles's Enable/disable External Authentication.
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
            https://developer.cisco.com/docs/dna-center/#!manage-external-authentication-setting-a-p-i
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
            "enable": enable,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e4f57e8f06856ee9a7e490d01f7f692_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/system/api/v1/users/external-authentication"
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
            "bpm_e4f57e8f06856ee9a7e490d01f7f692_v3_2_3_0", json_data
        )

    def get_external_authentication_setting_api(
        self, headers=None, **request_parameters
    ):
        """Get the External Authentication setting.

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
            https://developer.cisco.com/docs/dna-center/#!get-external-authentication-setting-a-p-i
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

        e_url = "/dna/system/api/v1/users/external-authentication"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ac03ba045f60925fd7843bf9e279_v3_2_3_0", json_data
        )

    def add_access_group(
        self,
        description=None,
        name=None,
        resourceGroups=None,
        role=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Add an access group into the system.This API provides the ability to create an access group. An access group is
        an entity that provides RBAC and site access to users on the system. Each access group is associated
        with a role and a site. Each role must be based on the permissions returned by the Get permissions v2
        API (GET /dna/system/api/v2/roles/permissions) and must be created using the Add role v2 API (POST
        /dna/system/api/v2/roles). The site details can be obtained from the get sites API (GET
        /dna/intent/api/v1/sites). The full site hierarchy should a / delimited list of site ids.  For example:
        {site id 1}/{site id 2}/.../{site id n}.

        Args:
            description(string): User and Roles's Description of the access group.
            name(string): User and Roles's Name of the access group.
            resourceGroups(list): User and Roles's List of resources to be associated with the access group. (list
                of objects).
            role(list): User and Roles's List of role names. (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!add-access-group
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
            "name": name,
            "description": description,
            "resourceGroups": resourceGroups,
            "role": role,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_c05f721266f5264869d10ac0e663812_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/system/api/v1/accessGroups"
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
            "bpm_c05f721266f5264869d10ac0e663812_v3_2_3_0", json_data
        )

    def get_access_groups(
        self,
        ids=None,
        limit=None,
        names=None,
        offset=None,
        source_resource_ids=None,
        type=None,
        user_count=None,
        headers=None,
        **request_parameters
    ):
        """Get all access groups in the system.

        Args:
            user_count(str): userCount query parameter. If set to true, it will return number of users associated
                with each access group. Default is false.
            names(str): names query parameter. Get access groups by passing comma separated list of names. It
                performs an exact character match.
            type(str): type query parameter. Get access groups by passing the type of the resource such as site.
            source_resource_ids(str): sourceResourceIds query parameter. Get access groups by passing the ids of the
                resource associated with it such as the site hierarchy id.
            ids(str): ids query parameter. Get access groups by passing a comma separated list of their ids.
            offset(int): offset query parameter. An integer representing the starting access group in the page
                returned.
            limit(int): limit query parameter. Limit on the number of access groups on a page. Default page size is
                20. .
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
            https://developer.cisco.com/docs/dna-center/#!get-access-groups
        """
        check_type(headers, dict)
        check_type(user_count, str)
        check_type(names, str)
        check_type(type, str)
        check_type(source_resource_ids, str)
        check_type(ids, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "userCount": user_count,
            "names": names,
            "type": type,
            "sourceResourceIds": source_resource_ids,
            "ids": ids,
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

        e_url = "/dna/system/api/v1/accessGroups"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d61e43a8723a51e08e33ddc2286aa4ba_v3_2_3_0", json_data
        )

    def delete_role(self, id, headers=None, **request_parameters):
        """Delete a role in the system.This API is the successor to the v1 delete role API (DELETE
        /dna/system/api/v1/role). It can be used to delete any role system, including roles created using the v1
        Add role API (POST /dna/system/api/v1/role) and the v2 Add role API (POST /dna/system/api/v2/roles).

        Args:
            id(str): id path parameter. The Id of the role to be deleted.
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
            https://developer.cisco.com/docs/dna-center/#!delete-role
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

        e_url = "/dna/system/api/v2/roles/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ba21979a54d4878a270dbf105a69_v3_2_3_0", json_data
        )

    def delete_role_v2(self, id, headers=None, **query_parameters):
        """Alias for `delete_role <#catalystcentersdk.
        api.v3_2_3_0.user_and_roles.
        UserAndRoles.delete_role>`_
        """
        return self.delete_role(id=id, headers=headers, **query_parameters)

    def get_role(self, id, headers=None, **request_parameters):
        """Get a role in the system (v2).This API is the successor to the v1 get role API (GET
        /dna/system/api/v1/role/${id}). It can be used to get a role that exists in the system, regardless of
        whether it was created using the v1 Add role API (POST /dna/system/api/v1/role) or the v2 Add role API
        (POST /dna/system/api/v2/roles).

        Args:
            id(str): id path parameter. Id of the role to look up.
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
            https://developer.cisco.com/docs/dna-center/#!get-role
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

        e_url = "/dna/system/api/v2/roles/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dacb094ae6b15207acd1f389eff65960_v3_2_3_0", json_data
        )

    def get_role_v2(self, id, headers=None, **query_parameters):
        """Alias for `get_role <#catalystcentersdk.
        api.v3_2_3_0.user_and_roles.
        UserAndRoles.get_role>`_
        """
        return self.get_role(id=id, headers=headers, **query_parameters)

    def update_role(
        self,
        id,
        description=None,
        name=None,
        permissions=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Update a role in the system (v2).This API is the successor to the v1 Update role API (PUT
        /dna/system/api/v1/role). It can be used to update a role that exists in the system, regardless of
        whether it was created using the v1 Add role API (POST /dna/system/api/v1/role) or the v2 Add role API
        (POST /dna/system/api/v2/roles). The JSON payload for this API accepts a list of permissions. Every
        permission that requires read or write privilege should be included in the JSON payload. If the
        intention is to give read privilege for a particular permission, please set the privilege to "Read".
        Similarly, if the intention is to give write privilege for a particular permission, please set the
        privilege to "Write".

        Args:
            description(string): User and Roles's Description of role.
            name(string): User and Roles's Name of the role.
            permissions(list): User and Roles's List of permissions to be associated with the role. (list of
                objects).
            id(str): id path parameter. The id of the role to be updated.
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
            https://developer.cisco.com/docs/dna-center/#!update-role
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
        _payload = {
            "name": name,
            "description": description,
            "permissions": permissions,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_b8b02e13a5281934aecf58df4682d_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/system/api/v2/roles/{id}"
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
            "bpm_b8b02e13a5281934aecf58df4682d_v3_2_3_0", json_data
        )

    def update_role_v2(
        self,
        id,
        description=None,
        name=None,
        permissions=None,
        headers=None,
        payload=None,
        active_validation=True,
        **query_parameters
    ):
        """Alias for `update_role <#catalystcentersdk.
        api.v3_2_3_0.user_and_roles.
        UserAndRoles.update_role>`_
        """
        return self.update_role(
            id=id,
            description=description,
            name=name,
            permissions=permissions,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_permissions(self, headers=None, **request_parameters):
        """Get all v2 permissions that can be used to create or update a custom role in the system.

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
            https://developer.cisco.com/docs/dna-center/#!get-permissions
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

        e_url = "/dna/system/api/v2/roles/permissions"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e5d8a09a353a1a853fc7222c20dc1_v3_2_3_0", json_data
        )

    def get_permissions_v2(self, headers=None, **query_parameters):
        """Alias for `get_permissions <#catalystcentersdk.
        api.v3_2_3_0.user_and_roles.
        UserAndRoles.get_permissions>`_
        """
        return self.get_permissions(headers=headers, **query_parameters)

    def get_external_authentication_servers_api(
        self, invoke_source, headers=None, **request_parameters
    ):
        """Get external users authentication servers.

        Args:
            invoke_source(str): invokeSource query parameter. The source that invokes this API. The value of this
                query parameter must be set to "external".
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
            https://developer.cisco.com/docs/dna-center/#!get-external-authentication-servers-a-p-i
        """
        check_type(headers, dict)
        check_type(invoke_source, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "invokeSource": invoke_source,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/system/api/v1/users/external-servers"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_def9045d4d9c96bcd42172a79c_v3_2_3_0", json_data
        )

    def delete_role_api(self, role_id, headers=None, **request_parameters):
        """Delete a role in the system.

        Args:
            role_id(str): roleId path parameter. The Id of the role to be deleted.
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
            https://developer.cisco.com/docs/dna-center/#!delete-role-a-p-i
        """
        check_type(headers, dict)
        check_type(role_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "roleId": role_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/system/api/v1/role/{roleId}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_da9e850c44d353f78ab002a640e5604f_v3_2_3_0", json_data
        )


# Alias Functions
UserAndRoles.get_users = UserAndRoles.get_users_api
UserAndRoles.add_user = UserAndRoles.add_user_api
UserAndRoles.update_user = UserAndRoles.update_user_api
UserandRoles = UserAndRoles
