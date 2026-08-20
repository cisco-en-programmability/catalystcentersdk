"""Cisco Catalyst Center Wired API wrapper.

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


class Wired:
    """Cisco Catalyst Center Wired API (version: 3.2.3.0).

    Wraps the Catalyst Center Wired
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Wired
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

    def get_deployed_security_config_count(
        self, feature, id, headers=None, **request_parameters
    ):
        """Returns the number of deployed configuration entries for the specified security feature on the switch.

        Args:
            id(str): id path parameter. Network device id of the switch. The Network device id can be identified
                from the GET network device API /dna/intent/api/v1/network-device response.
            feature(str): feature path parameter. Name of the feature to retrieve configuration for. The API
                /api/v1/switches/{id}/configs/supported/security. can be used to get the list of
                features supported on a device.
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
            https://developer.cisco.com/docs/dna-center/#!get-deployed-security-config-count
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/campus/api/v1/switches/{id}/configs/deployed/securi"
            + "ty/{feature}/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_beb58a142cab5335907622914f56fca4_v3_2_3_0", json_data
        )

    def get_intended_security_configurations(
        self, feature, id, limit=None, offset=None, headers=None, **request_parameters
    ):
        """This API returns the configurations for an intended Security feature on a switch. Even after the intended
        configurations are deployed using the API /api/v1/switches/{id}/configs/intended/deploy, they continue
        to be a part of the intended features on the device.

        Args:
            id(str): id path parameter. Network device id of the switch. The Network device id can be identified
                from the GET network device API /dna/intent/api/v1/network-device response.
            feature(str): feature path parameter. Name of the feature to configure. The API
                /api/v1/switches/{id}/configs/supported/security can be used to get the list of features
                supported on a device.
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
            https://developer.cisco.com/docs/dna-center/#!get-intended-security-configurations
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
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
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/campus/api/v1/switches/{id}/configs/intended/securi" + "ty/{feature}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ca61c56055259bd48e61f6bbeac29_v3_2_3_0", json_data
        )

    def update_intended_security_configurations(
        self,
        feature,
        id,
        arpInspectionConfig=None,
        ctsConfig=None,
        deviceTrackingConfig=None,
        deviceTrackingVlanConfig=None,
        dhcpSnoopingConfig=None,
        dot1xConfig=None,
        ipV4ExtendedAccessListConfig=None,
        ipV4RoleBasedAccessListConfig=None,
        ipV4StandardAccessListConfig=None,
        ipV6AccessListConfig=None,
        ipV6RoleBasedAccessListConfig=None,
        macExtendedAccessListConfig=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API updates the configurations for an intended feature on a switch. Updates to other intended features can
        be done over several iterations. Once all the updates to intended features are complete, they can be
        deployed to a device using the API /api/v1/switches/{id}/configs/intended/deploy. When the intended
        features are deployed, they are applied on top of the existing configurations on the device. Any
        existing configurations on the device which are not included in the intended features, are retained on
        the device.

        Args:
            arpInspectionConfig(object): Wired's This feature for configuring ARP Inspection protocol on the device,
                which monitors and validates ARP packets to prevent ARP spoofing and ensure network
                security.
            ctsConfig(object): Wired's This feature is for configuring CTS.
            deviceTrackingConfig(object): Wired's This feature is for configuring Device Tracking Settings.
            deviceTrackingVlanConfig(object): Wired's This feature is for configuring Device Tracking Vlan Settings.
            dhcpSnoopingConfig(object): Wired's This feature is for configuring DHCP Snooping. DHCP Snooping is a
                security feature that acts as a firewall between untrusted hosts and trusted DHCP
                servers. It helps to prevent malicious or malformed DHCP traffic and ensures that only
                valid DHCP servers can assign IP addresses.
            dot1xConfig(object): Wired's This feature is for configuring 802.1x. IEEE 802.1x is a standard which
                facilitates access control between a client and a server. Before services can be
                provided to a client by a Local Access Network (LAN) or switch, the client connected to
                the switch port has to be authenticated by the authentication server which runs Remote
                Authentication Dial-In User Service (RADIUS). 802.1x authentication restricts
                unauthorized clients from connecting to a LAN through publicly-accessible ports.
            ipV4ExtendedAccessListConfig(object): Wired's This feature is for configuring IP Access List Extended
                settings. It allows defining extended access control lists for more granular traffic
                control.
            ipV4RoleBasedAccessListConfig(object): Wired's This feature is for configuring IP ACL Role Based
                settings. It allows defining access control lists based on roles to enhance network
                security.
            ipV4StandardAccessListConfig(object): Wired's This feature is for configuring IP Access List Standard
                settings. It allows defining standard access control lists for basic traffic control.
            ipV6AccessListConfig(object): Wired's This feature is for configuring IP Named ACL settings. It allows
                defining named access control lists for easier management and configuration.
            ipV6RoleBasedAccessListConfig(object): Wired's This feature is for configuring IPv6 Acc List Role Seq
                Rule Gen settings. It allows defining role-based access control lists for easier
                management and configuration.
            macExtendedAccessListConfig(object): Wired's This feature is for configuring MAC Acc List Extended Gen
                settings. It allows defining extended MAC access control lists for easier management and
                configuration.
            id(str): id path parameter. Network device id of the switch. The Network device id can be identified
                from the GET network device API /dna/intent/api/v1/network-device response.
            feature(str): feature path parameter. Name of the feature to configure.
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
            https://developer.cisco.com/docs/dna-center/#!update-intended-security-configurations
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }
        _payload = {
            "dot1xConfig": dot1xConfig,
            "arpInspectionConfig": arpInspectionConfig,
            "dhcpSnoopingConfig": dhcpSnoopingConfig,
            "ctsConfig": ctsConfig,
            "ipV4ExtendedAccessListConfig": ipV4ExtendedAccessListConfig,
            "ipV4StandardAccessListConfig": ipV4StandardAccessListConfig,
            "ipV6AccessListConfig": ipV6AccessListConfig,
            "ipV6RoleBasedAccessListConfig": ipV6RoleBasedAccessListConfig,
            "macExtendedAccessListConfig": macExtendedAccessListConfig,
            "ipV4RoleBasedAccessListConfig": ipV4RoleBasedAccessListConfig,
            "deviceTrackingConfig": deviceTrackingConfig,
            "deviceTrackingVlanConfig": deviceTrackingVlanConfig,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e43e520b26ad52b8b99dd1a9a97f2eff_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/campus/api/v1/switches/{id}/configs/intended/securi" + "ty/{feature}"
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
            "bpm_e43e520b26ad52b8b99dd1a9a97f2eff_v3_2_3_0", json_data
        )

    def add_intended_security_configurations(
        self,
        feature,
        id,
        arpInspectionConfig=None,
        ctsConfig=None,
        deviceTrackingConfig=None,
        deviceTrackingVlanConfig=None,
        dhcpSnoopingConfig=None,
        dot1xConfig=None,
        ipV4ExtendedAccessListConfig=None,
        ipV4RoleBasedAccessListConfig=None,
        ipV4StandardAccessListConfig=None,
        ipV6AccessListConfig=None,
        ipV6RoleBasedAccessListConfig=None,
        macExtendedAccessListConfig=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API creates configurations for an intended feature on a wired device. Once all the updates to intended
        features are complete, they can be deployed to a device using the API
        /api/v1/switches/{id}/configs/intended/deploy. When the intended features are deployed, they are applied
        on top of the existing configurations on the device. Any existing configurations on the device which are
        not included in the intended features, are retained on the device. The device config learning must have
        enabled for the switch using the API /dna/campus/api/v1/switches/configs/deployed/enable and Error code
        NCCO15475 can be observed if not enabled.

        Args:
            arpInspectionConfig(object): Wired's This feature for configuring ARP Inspection protocol on the device,
                which monitors and validates ARP packets to prevent ARP spoofing and ensure network
                security.
            ctsConfig(object): Wired's This feature is for configuring CTS.
            deviceTrackingConfig(object): Wired's This feature is for configuring Device Tracking Settings.
            deviceTrackingVlanConfig(object): Wired's This feature is for configuring Device Tracking Vlan Settings.
            dhcpSnoopingConfig(object): Wired's This feature is for configuring DHCP Snooping. DHCP Snooping is a
                security feature that acts as a firewall between untrusted hosts and trusted DHCP
                servers. It helps to prevent malicious or malformed DHCP traffic and ensures that only
                valid DHCP servers can assign IP addresses.
            dot1xConfig(object): Wired's This feature is for configuring 802.1x. IEEE 802.1x is a standard which
                facilitates access control between a client and a server. Before services can be
                provided to a client by a Local Access Network (LAN) or switch, the client connected to
                the switch port has to be authenticated by the authentication server which runs Remote
                Authentication Dial-In User Service (RADIUS). 802.1x authentication restricts
                unauthorized clients from connecting to a LAN through publicly-accessible ports.
            ipV4ExtendedAccessListConfig(object): Wired's This feature is for configuring IP Access List Extended
                settings. It allows defining extended access control lists for more granular traffic
                control.
            ipV4RoleBasedAccessListConfig(object): Wired's This feature is for configuring IP ACL Role Based
                settings. It allows defining access control lists based on roles to enhance network
                security.
            ipV4StandardAccessListConfig(object): Wired's This feature is for configuring IP Access List Standard
                settings. It allows defining standard access control lists for basic traffic control.
            ipV6AccessListConfig(object): Wired's This feature is for configuring IP Named ACL settings. It allows
                defining named access control lists for easier management and configuration.
            ipV6RoleBasedAccessListConfig(object): Wired's This feature is for configuring IPv6 Acc List Role Seq
                Rule Gen settings. It allows defining role-based access control lists for easier
                management and configuration.
            macExtendedAccessListConfig(object): Wired's This feature is for configuring MAC Acc List Extended Gen
                settings. It allows defining extended MAC access control lists for easier management and
                configuration.
            id(str): id path parameter. Network device id of the switch. The Network device id can be identified
                from the GET network device API /dna/intent/api/v1/network-device response.
            feature(str): feature path parameter. Name of the feature to configure. The API
                /api/v1/switches/{id}/configs/supported/security can be used to get the list of features
                supported on a device.
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
            https://developer.cisco.com/docs/dna-center/#!add-intended-security-configurations
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }
        _payload = {
            "dot1xConfig": dot1xConfig,
            "arpInspectionConfig": arpInspectionConfig,
            "dhcpSnoopingConfig": dhcpSnoopingConfig,
            "ctsConfig": ctsConfig,
            "ipV4ExtendedAccessListConfig": ipV4ExtendedAccessListConfig,
            "ipV4StandardAccessListConfig": ipV4StandardAccessListConfig,
            "ipV6AccessListConfig": ipV6AccessListConfig,
            "ipV6RoleBasedAccessListConfig": ipV6RoleBasedAccessListConfig,
            "macExtendedAccessListConfig": macExtendedAccessListConfig,
            "ipV4RoleBasedAccessListConfig": ipV4RoleBasedAccessListConfig,
            "deviceTrackingConfig": deviceTrackingConfig,
            "deviceTrackingVlanConfig": deviceTrackingVlanConfig,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_fd1548d678db5fc89ff81116d3eb64de_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/campus/api/v1/switches/{id}/configs/intended/securi" + "ty/{feature}"
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
            "bpm_fd1548d678db5fc89ff81116d3eb64de_v3_2_3_0", json_data
        )

    def delete_intended_security_configurations(
        self, feature, id, headers=None, **request_parameters
    ):
        """This API deletes the configurations for an intended feature on a switch. Once all the updates to intended
        features are complete, they can be deployed to a device using the API
        /api/v1/switches/{id}/configs/intended/deploy. When the intended features are deployed, they are applied
        on top of the existing configurations on the device. Any existing configurations on the device which are
        not included in the intended features, are retained on the device.

        Args:
            id(str): id path parameter. Network device id of the switch. The Network device id can be identified
                from the GET network device API /dna/intent/api/v1/network-device response.
            feature(str): feature path parameter. Name of the feature to delete. The API
                /api/v1/switches/{id}/configs/supported/security can be used to get the list of features
                supported on a device.
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
            https://developer.cisco.com/docs/dna-center/#!delete-intended-security-configurations
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/campus/api/v1/switches/{id}/configs/intended/securi" + "ty/{feature}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d75e159daf8153d8943ddc640fd2b1eb_v3_2_3_0", json_data
        )

    def get_deployed_security_configurations(
        self, feature, id, limit=None, offset=None, headers=None, **request_parameters
    ):
        """Returns deployed configuration entries for the specified security feature on the switch. The device config
        learning must have enabled for the switch using the API
        /dna/campus/api/v1/switches/configs/deployed/enable.

        Args:
            id(str): id path parameter. Network device id of the switch. The Network device id can be identified
                from the GET network device API /dna/intent/api/v1/network-device response.
            feature(str): feature path parameter. Name of the feature to retrieve security configuration for. The
                API /api/v1/switches/{id}/configs/supported/security can be used to get the list of
                features supported on a device.
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
            https://developer.cisco.com/docs/dna-center/#!get-deployed-security-configurations
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
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
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/campus/api/v1/switches/{id}/configs/deployed/securi" + "ty/{feature}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ed4975052bc522dba1deb2622d9f32f_v3_2_3_0", json_data
        )

    def get_intended_layer2_configurations(
        self, feature, id, limit=None, offset=None, headers=None, **request_parameters
    ):
        """This API returns the configurations for an intended layer 2 feature on a switch. Even after the intended
        configurations are deployed using the API /api/v1/switches/{id}/configs/intended/deploy, they continue
        to be a part of the intended features on the device.

        Args:
            id(str): id path parameter. Network device ID of the switch to configure.
            feature(str): feature path parameter. Name of the feature to configure. The API
                /api/v1/switches/{id}/configs/supported/layer2 can be used to get the list of features
                supported on a device.
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
            https://developer.cisco.com/docs/dna-center/#!get-intended-layer2-configurations
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
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
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/campus/api/v1/switches/{id}/configs/intended/layer2" + "/{feature}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d1d6fcb35d1dab928a35dac6dbb1_v3_2_3_0", json_data
        )

    def delete_intended_layer2_configurations(
        self, feature, id, headers=None, **request_parameters
    ):
        """This API deletes the configurations for an intended feature on a switch. Once all the updates to intended
        features are complete, they can be deployed to a device using the API
        /api/v1/switches/{id}/configs/intended/deploy. When the intended features are deployed, they are applied
        on top of the existing configurations on the device. Any existing configurations on the device which are
        not included in the intended features, are retained on the device.

        Args:
            id(str): id path parameter. Network device id of the switch. The Network device id can be identified
                from the GET network device API /dna/intent/api/v1/network-device response.
            feature(str): feature path parameter. Name of the feature to delete.
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
            https://developer.cisco.com/docs/dna-center/#!delete-intended-layer2-configurations
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/campus/api/v1/switches/{id}/configs/intended/layer2" + "/{feature}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d58ffeab64f5677a135fd95bf37c554_v3_2_3_0", json_data
        )

    def update_intended_layer2_configurations(
        self,
        feature,
        id,
        cdpConfig=None,
        etherchannelConfig=None,
        igmpSnoopingConfig=None,
        lldpConfig=None,
        macAddressTableConfig=None,
        mldSnoopingConfig=None,
        stpConfig=None,
        udldConfig=None,
        vlanConfig=None,
        vtpConfig=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API updates the configurations for an intended feature on a switch. Updates to other intended features can
        be done over several iterations. Once all the updates to intended features are complete, they can be
        deployed to a device using the API /api/v1/switches/{id}/configs/intended/deploy. When the intended
        features are deployed, they are applied on top of the existing configurations on the device. Any
        existing configurations on the device which are not included in the intended features, are retained on
        the device.

        Args:
            cdpConfig(object): Wired's This feature is for configuring CDP. Cisco Discovery Protocol (CDP) is a
                device discovery protocol that runs over Layer 2 on all Cisco devices and allows network
                management applications to discover Cisco devices that are neighbors of already known
                devices. A CDP-enabled device sends periodic messages to a multicast address,
                advertising at least one address at which it can receive SNMP messages. The
                advertisements also contain time-to-live, or holdtime information, which is the length
                of time a receiving device holds CDP information before discarding it. Each device also
                listens to the messages sent by other devices to learn about neighboring devices.
            etherchannelConfig(object): Wired's This feature is for configuring etherchannels global config on
                device.
            igmpSnoopingConfig(object): Wired's This feature is for configuring IGMP Snooping.
            lldpConfig(object): Wired's This feature is for configuring LLDP. Link Layer Discovery Protocol (LLDP)
                is a  protocol used to advertise and discover information about neighboring network
                devices on a local area network (LAN). LLDP allows devices to exchange information such
                as device capabilities, system information, and network connectivity details.
            macAddressTableConfig(object): Wired's This feature is for configuring MAC address table settings.
            mldSnoopingConfig(object): Wired's This feature is for configuring MLD Snooping.
            stpConfig(object): Wired's This feature is for configuring Spanning Tree Protocol (STP), which provides
                path redundancy while preventing loops in the network.
            udldConfig(object): Wired's This feature is for configuring UDLD.
            vlanConfig(object): Wired's This feature is for configuring VLANs. VLANs are switched networks that are
                logically segmented by function or application.
            vtpConfig(object): Wired's This feature is for configuring VTP. VLAN Trunking Protocol (VTP) is a Layer
                2 messaging protocol that maintains VLAN configuration consistency by managing the
                addition, deletion, and renaming of VLANs on a network-wide basis. It can be used to
                make vlan configuration changes centrally on one or more devices and have those changes
                automatically communicated to all the other devices in the network. VTP does not work
                well in a situation where multiple updates to the VLANs occur simultaneously on devices
                in the same domain, which would result in an inconsistency in the VLAN database. With
                VTP, trunk ports must be configured on the device so that the device can send and
                receive VTP advertisements to and from other devices in the domain.
            id(str): id path parameter. Network device id of the switch. The Network device id can be identified
                from the GET network device API /dna/intent/api/v1/network-device response.
            feature(str): feature path parameter. Name of the feature to configure.
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
            https://developer.cisco.com/docs/dna-center/#!update-intended-layer2-configurations
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }
        _payload = {
            "vlanConfig": vlanConfig,
            "cdpConfig": cdpConfig,
            "lldpConfig": lldpConfig,
            "stpConfig": stpConfig,
            "vtpConfig": vtpConfig,
            "udldConfig": udldConfig,
            "macAddressTableConfig": macAddressTableConfig,
            "igmpSnoopingConfig": igmpSnoopingConfig,
            "mldSnoopingConfig": mldSnoopingConfig,
            "etherchannelConfig": etherchannelConfig,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_c576d6792fd3532cb34cb6e1e2abb125_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/campus/api/v1/switches/{id}/configs/intended/layer2" + "/{feature}"
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
            "bpm_c576d6792fd3532cb34cb6e1e2abb125_v3_2_3_0", json_data
        )

    def add_intended_layer2_configurations(
        self,
        feature,
        id,
        cdpConfig=None,
        etherchannelConfig=None,
        igmpSnoopingConfig=None,
        lldpConfig=None,
        macAddressTableConfig=None,
        mldSnoopingConfig=None,
        stpConfig=None,
        udldConfig=None,
        vlanConfig=None,
        vtpConfig=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API creates configurations for an intended feature on a switch. Once all the updates to intended features
        are complete, they can be deployed to a device using the API
        /api/v1/switches/{id}/configs/intended/deploy. When the intended features are deployed, they are applied
        on top of the existing configurations on the device. Any existing configurations on the device which are
        not included in the intended features, are retained on the device. The device config learning must have
        enabled for the switch using the API /dna/campus/api/v1/switches/configs/deployed/enable and Error code
        NCCO15475 can be observed if not enabled.

        Args:
            cdpConfig(object): Wired's This feature is for configuring CDP. Cisco Discovery Protocol (CDP) is a
                device discovery protocol that runs over Layer 2 on all Cisco devices and allows network
                management applications to discover Cisco devices that are neighbors of already known
                devices. A CDP-enabled device sends periodic messages to a multicast address,
                advertising at least one address at which it can receive SNMP messages. The
                advertisements also contain time-to-live, or holdtime information, which is the length
                of time a receiving device holds CDP information before discarding it. Each device also
                listens to the messages sent by other devices to learn about neighboring devices.
            etherchannelConfig(object): Wired's This feature is for configuring etherchannels global config on
                device.
            igmpSnoopingConfig(object): Wired's This feature is for configuring IGMP Snooping.
            lldpConfig(object): Wired's This feature is for configuring LLDP. Link Layer Discovery Protocol (LLDP)
                is a  protocol used to advertise and discover information about neighboring network
                devices on a local area network (LAN). LLDP allows devices to exchange information such
                as device capabilities, system information, and network connectivity details.
            macAddressTableConfig(object): Wired's This feature is for configuring MAC address table settings.
            mldSnoopingConfig(object): Wired's This feature is for configuring MLD Snooping.
            stpConfig(object): Wired's This feature is for configuring Spanning Tree Protocol (STP), which provides
                path redundancy while preventing loops in the network.
            udldConfig(object): Wired's This feature is for configuring UDLD.
            vlanConfig(object): Wired's This feature is for configuring VLANs. VLANs are switched networks that are
                logically segmented by function or application.
            vtpConfig(object): Wired's This feature is for configuring VTP. VLAN Trunking Protocol (VTP) is a Layer
                2 messaging protocol that maintains VLAN configuration consistency by managing the
                addition, deletion, and renaming of VLANs on a network-wide basis. It can be used to
                make vlan configuration changes centrally on one or more devices and have those changes
                automatically communicated to all the other devices in the network. VTP does not work
                well in a situation where multiple updates to the VLANs occur simultaneously on devices
                in the same domain, which would result in an inconsistency in the VLAN database. With
                VTP, trunk ports must be configured on the device so that the device can send and
                receive VTP advertisements to and from other devices in the domain.
            id(str): id path parameter. Network device id of the switch. The Network device id can be identified
                from the GET network device API /dna/intent/api/v1/network-device response.
            feature(str): feature path parameter. Name of the feature to configure. The API
                /api/v1/switches/{id}/configs/supported/layer2 can be used to get the list of features
                supported on a device.
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
            https://developer.cisco.com/docs/dna-center/#!add-intended-layer2-configurations
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }
        _payload = {
            "vlanConfig": vlanConfig,
            "cdpConfig": cdpConfig,
            "lldpConfig": lldpConfig,
            "stpConfig": stpConfig,
            "vtpConfig": vtpConfig,
            "udldConfig": udldConfig,
            "macAddressTableConfig": macAddressTableConfig,
            "igmpSnoopingConfig": igmpSnoopingConfig,
            "mldSnoopingConfig": mldSnoopingConfig,
            "etherchannelConfig": etherchannelConfig,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator("jsd_a251b25925b0c317ae1bf2bacd_v3_2_3_0").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/campus/api/v1/switches/{id}/configs/intended/layer2" + "/{feature}"
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
            "bpm_a251b25925b0c317ae1bf2bacd_v3_2_3_0", json_data
        )

    def get_device_deployment_status_connectivity(
        self, id, deploy_activity_id=None, headers=None, **request_parameters
    ):
        """Returns device deployment status based on filter criteria.

        Args:
            id(str): id path parameter. Network device id of the switch to provision. The API
                /intent/api/v1/network-device can be used to get the network device ID.
            deploy_activity_id(str): deployActivityId query parameter. Activity from the /deploy task response.
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
            https://developer.cisco.com/docs/dna-center/#!get-device-deployment-status-connectivity
        """
        check_type(headers, dict)
        check_type(deploy_activity_id, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deployActivityId": deploy_activity_id,
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

        e_url = (
            "/dna/campus/api/v1/provision/switches/{id}/configs/inten"
            + "ded/deviceDeployments"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f0b54311312e5a699a0828417088c9a4_v3_2_3_0", json_data
        )

    def update_intended_port_configurations(
        self,
        feature,
        id,
        ethernetInterfaceConfig=None,
        portChannelInterfaceConfig=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API updates the configurations for an intended feature on a switch. Updates to other intended features can
        be done over several iterations. Once all the updates to intended features are complete, they can be
        deployed to a device using the API /api/v1/switches/{id}/configs/intended/deploy. When the intended
        features are deployed, they are applied on top of the existing configurations on the device. Any
        existing configurations on the device which are not included in the intended features, are retained on
        the device.

        Args:
            ethernetInterfaceConfig(object): Wired's This feature is for configuring ethernet interface config on
                device.
            portChannelInterfaceConfig(object): Wired's This feature is for configuring port-channels on a switch.
                Portchannel allows grouping of several physical Ethernet interfaces to create one
                logical Ethernet interface for the purpose of providing fault-tolerance and high-speed
                links between switches, routers, and servers.
            id(str): id path parameter. Network device id of the switch to configure. The Network device id is
                identified from the GET network device API /dna/intent/api/v1/network-device response.
            feature(str): feature path parameter. Name of the feature to configure.
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
            https://developer.cisco.com/docs/dna-center/#!update-intended-port-configurations
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }
        _payload = {
            "portChannelInterfaceConfig": portChannelInterfaceConfig,
            "ethernetInterfaceConfig": ethernetInterfaceConfig,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_c502bd27faaa506ea2ab28177996f094_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/campus/api/v1/switches/{id}/configs/intended/port/{" + "feature}"
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
            "bpm_c502bd27faaa506ea2ab28177996f094_v3_2_3_0", json_data
        )

    def delete_intended_port_configurations(
        self, feature, id, headers=None, **request_parameters
    ):
        """This API deletes the configurations for an intended feature on a switch. Once all the updates to intended
        features are complete, they can be deployed to a device using the API
        /api/v1/switches/{id}/configs/intended/deploy. When the intended features are deployed, they are applied
        on top of the existing configurations on the device. Any existing configurations on the device which are
        not included in the intended features, are retained on the device.

        Args:
            id(str): id path parameter. Network device id of the switch to configure. The Network device id is
                identified from the GET network device API /dna/intent/api/v1/network-device response.
            feature(str): feature path parameter. Name of the feature to delete.
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
            https://developer.cisco.com/docs/dna-center/#!delete-intended-port-configurations
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/campus/api/v1/switches/{id}/configs/intended/port/{" + "feature}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ccaa0b85d619300dca40cf09973_v3_2_3_0", json_data
        )

    def add_intended_port_configurations(
        self,
        feature,
        id,
        ethernetInterfaceConfig=None,
        portChannelInterfaceConfig=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API creates configurations for an intended feature on a switch. Once all the updates to intended features
        are complete, they can be deployed to a device using the API
        /api/v1/switches/{id}/configs/intended/deploy. When the intended features are deployed, they are applied
        on top of the existing configurations on the device. Any existing configurations on the device which are
        not included in the intended features, are retained on the device. The device config learning must have
        enabled for the switch using the API /dna/campus/api/v1/switches/configs/deployed/enable and Error code
        NCCO15475 can be observed if not enabled.

        Args:
            ethernetInterfaceConfig(object): Wired's This feature is for configuring ethernet interface config on
                device.
            portChannelInterfaceConfig(object): Wired's This feature is for configuring port-channels on a switch.
                Portchannel allows grouping of several physical Ethernet interfaces to create one
                logical Ethernet interface for the purpose of providing fault-tolerance and high-speed
                links between switches, routers, and servers.
            id(str): id path parameter. Network device id of the switch to configure. The Network device id is
                identified from the GET network device API /dna/intent/api/v1/network-device response.
            feature(str): feature path parameter. Name of the feature to configure. The API
                /api/v1/switches/{id}/configs/supported/port can be used to get the list of features
                supported on a device.
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
            https://developer.cisco.com/docs/dna-center/#!add-intended-port-configurations
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }
        _payload = {
            "portChannelInterfaceConfig": portChannelInterfaceConfig,
            "ethernetInterfaceConfig": ethernetInterfaceConfig,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_bac13e35d2b556488b0485ea174e11d2_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/campus/api/v1/switches/{id}/configs/intended/port/{" + "feature}"
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
            "bpm_bac13e35d2b556488b0485ea174e11d2_v3_2_3_0", json_data
        )

    def get_intended_port_configurations(
        self, feature, id, limit=None, offset=None, headers=None, **request_parameters
    ):
        """This API returns the configurations for an intended port feature on a switch. Even after the intended
        configurations are deployed using the API /api/v1/switches/{id}/configs/intended/deploy, they continue
        to be a part of the intended features on the device.

        Args:
            id(str): id path parameter. Network device id of the switch to configure. The Network device id is
                identified from the GET network device API /dna/intent/api/v1/network-device response.
            feature(str): feature path parameter. Name of the feature to configure. The API
                /api/v1/switches/{id}/configs/supported/port can be used to get the list of features
                supported on a device.
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
            https://developer.cisco.com/docs/dna-center/#!get-intended-port-configurations
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
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
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/campus/api/v1/switches/{id}/configs/intended/port/{" + "feature}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d1f7bd92b654ee8a8549f868b7225f_v3_2_3_0", json_data
        )

    def get_deployed_layer3_config_count(
        self, feature, id, headers=None, **request_parameters
    ):
        """Returns the number of deployed configuration entries for the specified layer 3 feature on the switch. The device
        config learning must have enabled for the switch using the API
        /dna/campus/api/v1/switches/configs/deployed/enable and Error code NCCO15475 can be observed if not
        enabled.

        Args:
            id(str): id path parameter. Network device id of the switch. The Network device id can be identified
                from the GET network device API /dna/intent/api/v1/network-device response.
            feature(str): feature path parameter. Name of the feature to retrieve configuration for. The API
                /api/v1/switches/{id}/configs/supported/layer3 can be used to get the list of features
                supported on a device.
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
            https://developer.cisco.com/docs/dna-center/#!get-deployed-layer3-config-count
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/campus/api/v1/switches/{id}/configs/deployed/layer3"
            + "/{feature}/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d058f2e619f65a379fc9027ccb76bd09_v3_2_3_0", json_data
        )

    def get_deployed_port_feature_configurations(
        self, feature, id, limit=None, offset=None, headers=None, **request_parameters
    ):
        """Returns deployed configuration entries for the specified port feature on the switch. The device config learning
        must have enabled for the switch using the API /dna/campus/api/v1/switches/configs/deployed/enable and
        Error code NCCO15475 can be observed if not enabled.

        Args:
            id(str): id path parameter. Network device id of the switch. The Network device id can be identified
                from the GET network device API /dna/intent/api/v1/network-device response.
            feature(str): feature path parameter. Name of the feature to retrieve port configuration for. The API
                /api/v1/switches/{id}/configs/supported/port can be used to get the list of features
                supported on a device.
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
            https://developer.cisco.com/docs/dna-center/#!get-deployed-port-feature-configurations
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
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
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/campus/api/v1/switches/{id}/configs/deployed/port/{" + "feature}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a97e7b02905657d8ac61790110b0f057_v3_2_3_0", json_data
        )

    def get_intended_port_config_count(
        self, feature, id, headers=None, **request_parameters
    ):
        """Returns the number of intended configuration entries for the specified port feature on the switch. The feature
        configuration entries can be retrieved using
        /dna/campus/api/v1/switches/{id}/configs/intended/port/{feature}.

        Args:
            id(str): id path parameter. Network device id of the switch to configure. The Network device id is
                identified from the GET network device API /dna/intent/api/v1/network-device response.
            feature(str): feature path parameter. Name of the feature to configure. The API
                /api/v1/switches/{id}/configs/supported/port can be used to get the list of features
                supported on a device.
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
            https://developer.cisco.com/docs/dna-center/#!get-intended-port-config-count
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/campus/api/v1/switches/{id}/configs/intended/port/{"
            + "feature}/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c51594e9b965f27a6e579c66d9f6c5d_v3_2_3_0", json_data
        )

    def get_configurations_for_an_intended_layer2_feature_on_a_wired_device(
        self, feature, id, headers=None, **request_parameters
    ):
        """This API returns the configurations for an intended layer 2 feature on a wired device. Even after the intended
        configurations are deployed using the API
        /dna/intent/api/v1/networkDevices/{id}/configFeatures/intended/deploy, they continue to be a part of the
        intended features on the device.  Released for gathering feedbacks from early adopters. API design is
        not final and future updates of this API may implement changes to any aspects of the API design.

        Args:
            id(str): id path parameter. Network device ID of the wired device to configure.
            feature(str): feature path parameter. The name of the feature to be retrieved.
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
            https://developer.cisco.com/docs/dna-center/#!get-configurations-for-an-intended-layer2-feature-on-a-wired-device
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wired/networkDevices/{id}/configFeatu"
            + "res/intended/layer2/{feature}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d1b2d399192a5da39b4ae3fe0f5288d4_v3_2_3_0", json_data
        )

    def delete_configurations_for_an_intended_layer2_feature_on_a_wired_device(
        self, feature, id, headers=None, **request_parameters
    ):
        """This API deletes the configurations for an intended feature on a wired device. Once all the updates to intended
        features are complete, they can be deployed to a device using the API
        /dna/intent/api/v1/networkDevices/{id}/configFeatures/intended/deploy. When the intended features are
        deployed, they are applied on top of the existing configurations on the device. Any existing
        configurations on the device which are not included in the intended features, are retained on the
        device.  Released for gathering feedbacks from early adopters. API design is not final and future
        updates of this API may implement changes to any aspects of the API design.

        Args:
            id(str): id path parameter. Network device ID of the wired device to configure.
            feature(str): feature path parameter. Name of the feature to delete.
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
            https://developer.cisco.com/docs/dna-center/#!delete-configurations-for-an-intended-layer2-feature-on-a-wired-device
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wired/networkDevices/{id}/configFeatu"
            + "res/intended/layer2/{feature}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d4649fef20535193fd86c95925bcf8_v3_2_3_0", json_data
        )

    def update_configurations_for_an_intended_layer2_feature_on_a_wired_device(
        self,
        feature,
        id,
        cdpGlobalConfig=None,
        cdpInterfaceConfig=None,
        dhcpSnoopingGlobalConfig=None,
        dhcpSnoopingInterfaceConfig=None,
        dot1xGlobalConfig=None,
        dot1xInterfaceConfig=None,
        igmpSnoopingGlobalConfig=None,
        lldpGlobalConfig=None,
        lldpInterfaceConfig=None,
        mabInterfaceConfig=None,
        mldSnoopingGlobalConfig=None,
        portChannelConfig=None,
        stpGlobalConfig=None,
        stpInterfaceConfig=None,
        switchportInterfaceConfig=None,
        trunkInterfaceConfig=None,
        vlanConfig=None,
        vtpGlobalConfig=None,
        vtpInterfaceConfig=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API updates the configurations for an intended feature on a wired device. Updates to other intended
        features can be done over several iterations. Once all the updates to intended features are complete,
        they can be deployed to a device using the API
        /dna/intent/api/v1/networkDevices/{id}/configFeatures/intended/deploy. When the intended features are
        deployed, they are applied on top of the existing configurations on the device. Any existing
        configurations on the device which are not included in the intended features, are retained on the
        device.  Released for gathering feedbacks from early adopters. API design is not final and future
        updates of this API may implement changes to any aspects of the API design.

        Args:
            cdpGlobalConfig(object): Wired's This feature is for configuring CDP. Cisco Discovery Protocol (CDP) is
                a device discovery protocol that runs over Layer 2 on all Cisco devices and allows
                network management applications to discover Cisco devices that are neighbors of already
                known devices. A CDP-enabled device sends periodic messages to a multicast address,
                advertising at least one address at which it can receive SNMP messages. The
                advertisements also contain time-to-live, or holdtime information, which is the length
                of time a receiving device holds CDP information before discarding it. Each device also
                listens to the messages sent by other devices to learn about neighboring devices.
            cdpInterfaceConfig(object): Wired's Configure CDP settings of an interface.
            dhcpSnoopingGlobalConfig(object): Wired's This feature is for configuring DHCP Snooping, which secures
                networks by monitoring DHCP traffic, blocking unauthorized servers, and enhancing
                overall security.
            dhcpSnoopingInterfaceConfig(object): Wired's This feature is for configuring DHCP Snooping on
                interfaces, ensuring secure and reliable IP address assignment by controlling packet
                filtering, rate limiting, logging, and violation actions.
            dot1xGlobalConfig(object): Wired's This feature is for configuring 802.1x. IEEE 802.1x is a standard
                which facilitates access control between a client and a server. Before services can be
                provided to a client by a Local Access Network (LAN) or switch, the client connected to
                the switch port has to be authenticated by the authentication server which runs Remote
                Authentication Dial-In User Service (RADIUS). 802.1x authentication restricts
                unauthorized clients from connecting to a LAN through publicly-accessible ports.
            dot1xInterfaceConfig(object): Wired's This feature is for configuring 802.1x on interfaces.
            igmpSnoopingGlobalConfig(object): Wired's This feature is for configuring IGMP Snooping, which tracks
                which ports are attached to multicast-capable routers to help the routers forward IGMP
                membership reports. By default, IGMP snooping is enabled on the device.
            lldpGlobalConfig(object): Wired's This feature is for configuring LLDP. Link Layer Discovery Protocol
                (LLDP) is a protocol used to advertise and discover information about neighboring
                network devices on a local area network (LAN). LLDP allows devices to exchange
                information such as device capabilities, system information, and network connectivity
                details.
            lldpInterfaceConfig(object): Wired's This feature is for configuring LLDP on an interface.
            mabInterfaceConfig(object): Wired's This feature is for configuring MAC Authentication Bypass (MAB), an
                alternative for devices that don't support 802.1X. The switch checks the MAC address of
                an endpoint with RADIUS server.
            mldSnoopingGlobalConfig(object): Wired's This feature is for configuring MLD Snooping. Multicast
                Listener Discovery(MLD) is a protocol used by IPv6 multicast routersto discover the
                presence of multicast listeners (nodes wishing to receive IPv6 multicast packets) on the
                links that are directly attached to the routers and to discover which multicast packets
                are of interest to neighboring nodes. MLD snooping allows the switch to examine MLD
                packets and make forwarding decisions based on their content.
            portChannelConfig(object): Wired's This feature is for configuring port-channels on a wired device.
                Portchannel allows grouping of several physical Ethernet interfaces to create one
                logical Ethernet interface for the purpose of providing fault-tolerance and high-speed
                links between switches, routers, and servers.
            stpGlobalConfig(object): Wired's This feature is for configuring Spanning Tree Protocol (STP), which
                provides path redundancy while preventing loops in the network.
            stpInterfaceConfig(object): Wired's This feature is for configuring STP on interfaces.
            switchportInterfaceConfig(object): Wired's This feature is for configuring switchport on interfaces.
            trunkInterfaceConfig(object): Wired's This feature is for trunk interface configurations on interfaces.
            vlanConfig(object): Wired's This feature is for configuring VLANs. VLANs are switched networks that are
                logically segmented by function or application.
            vtpGlobalConfig(object): Wired's This feature is for configuring VTP. VLAN Trunking Protocol (VTP) is a
                Layer 2 messaging protocol that maintains VLAN configuration consistency by managing the
                addition, deletion, and renaming of VLANs on a network-wide basis. It can be used to
                make vlan configuration changes centrally on one or more devices and have those changes
                automatically communicated to all the other devices in the network. VTP does not work
                well in a situation where multiple updates to the VLANs occur simultaneously on devices
                in the same domain, which would result in an inconsistency in the VLAN database. With
                VTP, trunk ports must be configured on the device so that the device can send and
                receive VTP advertisements to and from other devices in the domain.
            vtpInterfaceConfig(object): Wired's Configure VTP settings on a per-port basis to control the VTP
                traffic on trunk interfaces.
            id(str): id path parameter. Network device ID of the wired device to configure.
            feature(str): feature path parameter. Name of the feature to update configuration for. The feature must
                be already created.
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
            https://developer.cisco.com/docs/dna-center/#!update-configurations-for-an-intended-layer2-feature-on-a-wired-device
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
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
            "feature": feature,
        }
        _payload = {
            "cdpGlobalConfig": cdpGlobalConfig,
            "cdpInterfaceConfig": cdpInterfaceConfig,
            "dhcpSnoopingInterfaceConfig": dhcpSnoopingInterfaceConfig,
            "dhcpSnoopingGlobalConfig": dhcpSnoopingGlobalConfig,
            "dot1xInterfaceConfig": dot1xInterfaceConfig,
            "dot1xGlobalConfig": dot1xGlobalConfig,
            "lldpGlobalConfig": lldpGlobalConfig,
            "lldpInterfaceConfig": lldpInterfaceConfig,
            "mabInterfaceConfig": mabInterfaceConfig,
            "mldSnoopingGlobalConfig": mldSnoopingGlobalConfig,
            "igmpSnoopingGlobalConfig": igmpSnoopingGlobalConfig,
            "stpGlobalConfig": stpGlobalConfig,
            "stpInterfaceConfig": stpInterfaceConfig,
            "trunkInterfaceConfig": trunkInterfaceConfig,
            "vtpGlobalConfig": vtpGlobalConfig,
            "vtpInterfaceConfig": vtpInterfaceConfig,
            "vlanConfig": vlanConfig,
            "portChannelConfig": portChannelConfig,
            "switchportInterfaceConfig": switchportInterfaceConfig,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ee7664344f50cb8f2c94beaa01629d_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wired/networkDevices/{id}/configFeatu"
            + "res/intended/layer2/{feature}"
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
            "bpm_ee7664344f50cb8f2c94beaa01629d_v3_2_3_0", json_data
        )

    def create_configurations_for_an_intended_layer2_feature_on_a_wired_device(
        self,
        feature,
        id,
        cdpGlobalConfig=None,
        cdpInterfaceConfig=None,
        dhcpSnoopingGlobalConfig=None,
        dhcpSnoopingInterfaceConfig=None,
        dot1xGlobalConfig=None,
        dot1xInterfaceConfig=None,
        igmpSnoopingGlobalConfig=None,
        lldpGlobalConfig=None,
        lldpInterfaceConfig=None,
        mabInterfaceConfig=None,
        mldSnoopingGlobalConfig=None,
        portChannelConfig=None,
        stpGlobalConfig=None,
        stpInterfaceConfig=None,
        switchportInterfaceConfig=None,
        trunkInterfaceConfig=None,
        vlanConfig=None,
        vtpGlobalConfig=None,
        vtpInterfaceConfig=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API creates configurations for an intended feature on a wired device. Once all the updates to intended
        features are complete, they can be deployed to a device using the API
        /dna/intent/api/v1/networkDevices/{id}/configFeatures/intended/deploy. When the intended features are
        deployed, they are applied on top of the existing configurations on the device. Any existing
        configurations on the device which are not included in the intended features, are retained on the
        device.  Released for gathering feedbacks from early adopters. API design is not final and future
        updates of this API may implement changes to any aspects of the API design.

        Args:
            cdpGlobalConfig(object): Wired's This feature is for configuring CDP. Cisco Discovery Protocol (CDP) is
                a device discovery protocol that runs over Layer 2 on all Cisco devices and allows
                network management applications to discover Cisco devices that are neighbors of already
                known devices. A CDP-enabled device sends periodic messages to a multicast address,
                advertising at least one address at which it can receive SNMP messages. The
                advertisements also contain time-to-live, or holdtime information, which is the length
                of time a receiving device holds CDP information before discarding it. Each device also
                listens to the messages sent by other devices to learn about neighboring devices.
            cdpInterfaceConfig(object): Wired's Configure CDP settings of an interface.
            dhcpSnoopingGlobalConfig(object): Wired's This feature is for configuring DHCP Snooping, which secures
                networks by monitoring DHCP traffic, blocking unauthorized servers, and enhancing
                overall security.
            dhcpSnoopingInterfaceConfig(object): Wired's This feature is for configuring DHCP Snooping on
                interfaces, ensuring secure and reliable IP address assignment by controlling packet
                filtering, rate limiting, logging, and violation actions.
            dot1xGlobalConfig(object): Wired's This feature is for configuring 802.1x. IEEE 802.1x is a standard
                which facilitates access control between a client and a server. Before services can be
                provided to a client by a Local Access Network (LAN) or switch, the client connected to
                the switch port has to be authenticated by the authentication server which runs Remote
                Authentication Dial-In User Service (RADIUS). 802.1x authentication restricts
                unauthorized clients from connecting to a LAN through publicly-accessible ports.
            dot1xInterfaceConfig(object): Wired's This feature is for configuring 802.1x on interfaces.
            igmpSnoopingGlobalConfig(object): Wired's This feature is for configuring IGMP Snooping, which tracks
                which ports are attached to multicast-capable routers to help the routers forward IGMP
                membership reports. By default, IGMP snooping is enabled on the device.
            lldpGlobalConfig(object): Wired's This feature is for configuring LLDP. Link Layer Discovery Protocol
                (LLDP) is a protocol used to advertise and discover information about neighboring
                network devices on a local area network (LAN). LLDP allows devices to exchange
                information such as device capabilities, system information, and network connectivity
                details.
            lldpInterfaceConfig(object): Wired's This feature is for configuring LLDP on an interface.
            mabInterfaceConfig(object): Wired's This feature is for configuring MAC Authentication Bypass (MAB), an
                alternative for devices that don't support 802.1X. The switch checks the MAC address of
                an endpoint with RADIUS server.
            mldSnoopingGlobalConfig(object): Wired's This feature is for configuring MLD Snooping. Multicast
                Listener Discovery(MLD) is a protocol used by IPv6 multicast routersto discover the
                presence of multicast listeners (nodes wishing to receive IPv6 multicast packets) on the
                links that are directly attached to the routers and to discover which multicast packets
                are of interest to neighboring nodes. MLD snooping allows the switch to examine MLD
                packets and make forwarding decisions based on their content.
            portChannelConfig(object): Wired's This feature is for configuring port-channels on a wired device.
                Portchannel allows grouping of several physical Ethernet interfaces to create one
                logical Ethernet interface for the purpose of providing fault-tolerance and high-speed
                links between switches, routers, and servers.
            stpGlobalConfig(object): Wired's This feature is for configuring Spanning Tree Protocol (STP), which
                provides path redundancy while preventing loops in the network.
            stpInterfaceConfig(object): Wired's This feature is for configuring STP on interfaces.
            switchportInterfaceConfig(object): Wired's This feature is for configuring switchport on interfaces.
            trunkInterfaceConfig(object): Wired's This feature is for trunk interface configurations on interfaces.
            vlanConfig(object): Wired's This feature is for configuring VLANs. VLANs are switched networks that are
                logically segmented by function or application.
            vtpGlobalConfig(object): Wired's This feature is for configuring VTP. VLAN Trunking Protocol (VTP) is a
                Layer 2 messaging protocol that maintains VLAN configuration consistency by managing the
                addition, deletion, and renaming of VLANs on a network-wide basis. It can be used to
                make vlan configuration changes centrally on one or more devices and have those changes
                automatically communicated to all the other devices in the network. VTP does not work
                well in a situation where multiple updates to the VLANs occur simultaneously on devices
                in the same domain, which would result in an inconsistency in the VLAN database. With
                VTP, trunk ports must be configured on the device so that the device can send and
                receive VTP advertisements to and from other devices in the domain.
            vtpInterfaceConfig(object): Wired's Configure VTP settings on a per-port basis to control the VTP
                traffic on trunk interfaces.
            id(str): id path parameter. Network device ID of the wired device to configure.
            feature(str): feature path parameter. Name of the feature to configure. The API
                /dna/intent/api/v1/networkDevices/{id}/configFeatures/supported/layer2 can be used to
                get the list of features supported on a device.
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
            https://developer.cisco.com/docs/dna-center/#!create-configurations-for-an-intended-layer2-feature-on-a-wired-device
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
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
            "feature": feature,
        }
        _payload = {
            "cdpGlobalConfig": cdpGlobalConfig,
            "cdpInterfaceConfig": cdpInterfaceConfig,
            "dhcpSnoopingInterfaceConfig": dhcpSnoopingInterfaceConfig,
            "dhcpSnoopingGlobalConfig": dhcpSnoopingGlobalConfig,
            "dot1xInterfaceConfig": dot1xInterfaceConfig,
            "dot1xGlobalConfig": dot1xGlobalConfig,
            "lldpGlobalConfig": lldpGlobalConfig,
            "lldpInterfaceConfig": lldpInterfaceConfig,
            "mabInterfaceConfig": mabInterfaceConfig,
            "mldSnoopingGlobalConfig": mldSnoopingGlobalConfig,
            "igmpSnoopingGlobalConfig": igmpSnoopingGlobalConfig,
            "stpGlobalConfig": stpGlobalConfig,
            "stpInterfaceConfig": stpInterfaceConfig,
            "trunkInterfaceConfig": trunkInterfaceConfig,
            "vtpGlobalConfig": vtpGlobalConfig,
            "vtpInterfaceConfig": vtpInterfaceConfig,
            "vlanConfig": vlanConfig,
            "portChannelConfig": portChannelConfig,
            "switchportInterfaceConfig": switchportInterfaceConfig,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator("jsd_d7b57050bdb98e9340d0bc4dba_v3_2_3_0").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wired/networkDevices/{id}/configFeatu"
            + "res/intended/layer2/{feature}"
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
            "bpm_d7b57050bdb98e9340d0bc4dba_v3_2_3_0", json_data
        )

    def add_intended_network_settings_configurations(
        self,
        feature,
        id,
        dhcpExcludedAddressConfig=None,
        dhcpGeneralConfig=None,
        domainConfig=None,
        ipV4DhcpPoolConfig=None,
        ipV6DhcpPoolConfig=None,
        nameServerConfig=None,
        ntpAuthenticationKeyConfig=None,
        ntpGeneralConfig=None,
        ntpPerVrfServerConfig=None,
        ntpServerConfig=None,
        ntpTrustedKeyConfig=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API creates configurations for an intended feature on a switch. Once all the updates to intended features
        are complete, they can be deployed to a device using the API
        /api/v1/switches/{id}/configs/intended/deploy. When the intended features are deployed, they are applied
        on top of the existing configurations on the device. Any existing configurations on the device which are
        not included in the intended features, are retained on the device. The device config learning must have
        enabled for the switch using the API /dna/campus/api/v1/switches/configs/deployed/enable and Error code
        NCCO15475 can be observed if not enabled.

        Args:
            dhcpExcludedAddressConfig(object): Wired's Feature configures mapping to Excluded addresses, both
                excluded low-address IP and excluded low-high IP ranges.
            dhcpGeneralConfig(object): Wired's This feature is for configuring DHCP BOOTP protocol.
            domainConfig(object): Wired's This feature is for configuring IP domain.
            ipV4DhcpPoolConfig(object): Wired's This feature is for configuring IP DHCP pools.
            ipV6DhcpPoolConfig(object): Wired's This feature is for configuring IPv6 DHCP pools.
            nameServerConfig(object): Wired's This feature is for configuring name server.
            ntpAuthenticationKeyConfig(object): Wired's This feature is for configuring NTP which synchronizes the
                system clock with network time servers to ensure accurate timekeeping.
            ntpGeneralConfig(object): Wired's This feature is for configuring NTP which synchronizes the system
                clock with network time servers to ensure accurate timekeeping.
            ntpPerVrfServerConfig(object): Wired's This feature is for configuring NTP which synchronizes the system
                clock with network time servers to ensure accurate timekeeping.
            ntpServerConfig(object): Wired's This feature is for configuring NTP which synchronizes the system clock
                with network time servers to ensure accurate timekeeping.
            ntpTrustedKeyConfig(object): Wired's This feature is for configuring NTP which synchronizes the system
                clock with network time servers to ensure accurate timekeeping.
            id(str): id path parameter. Network device id of the switch to configure. The Network device id is
                identified from the GET network device API /dna/intent/api/v1/network-device response.
            feature(str): feature path parameter. Name of the feature to configure. The API
                /api/v1/switches/{id}/configs/supported/networkSettings can be used to get the list of
                features supported on a device.
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
            https://developer.cisco.com/docs/dna-center/#!add-intended-network-settings-configurations
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }
        _payload = {
            "ntpGeneralConfig": ntpGeneralConfig,
            "ntpAuthenticationKeyConfig": ntpAuthenticationKeyConfig,
            "ntpTrustedKeyConfig": ntpTrustedKeyConfig,
            "ntpServerConfig": ntpServerConfig,
            "ntpPerVrfServerConfig": ntpPerVrfServerConfig,
            "nameServerConfig": nameServerConfig,
            "domainConfig": domainConfig,
            "ipV4DhcpPoolConfig": ipV4DhcpPoolConfig,
            "ipV6DhcpPoolConfig": ipV6DhcpPoolConfig,
            "dhcpExcludedAddressConfig": dhcpExcludedAddressConfig,
            "dhcpGeneralConfig": dhcpGeneralConfig,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f527ec1c3b08547e9a1d1138ff1c3f25_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/campus/api/v1/switches/{id}/configs/intended/networ"
            + "kSettings/{feature}"
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
            "bpm_f527ec1c3b08547e9a1d1138ff1c3f25_v3_2_3_0", json_data
        )

    def get_intended_network_settings_configurations(
        self, feature, id, limit=None, offset=None, headers=None, **request_parameters
    ):
        """This API returns the configurations for an intended network settings feature on a switch. Even after the
        intended configurations are deployed using the API /api/v1/switches/{id}/configs/intended/deploy, they
        continue to be a part of the intended features on the device.

        Args:
            id(str): id path parameter. Network device id of the switch to configure. The Network device id is
                identified from the GET network device API /dna/intent/api/v1/network-device response.
            feature(str): feature path parameter. Name of the feature to configure. The API
                /api/v1/switches/{id}/configs/supported/networkSettings can be used to get the list of
                features supported on a device.
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
            https://developer.cisco.com/docs/dna-center/#!get-intended-network-settings-configurations
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
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
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/campus/api/v1/switches/{id}/configs/intended/networ"
            + "kSettings/{feature}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b851dc7a9bc352a680e8ca37fb8b4fcc_v3_2_3_0", json_data
        )

    def delete_intended_network_settings_configurations(
        self, feature, id, headers=None, **request_parameters
    ):
        """This API deletes the configurations for an intended feature on a switch. Once all the updates to intended
        features are complete, they can be deployed to a device using the API
        /api/v1/switches/{id}/configs/intended/deploy. When the intended features are deployed, they are applied
        on top of the existing configurations on the device. Any existing configurations on the device which are
        not included in the intended features, are retained on the device.

        Args:
            id(str): id path parameter. Network device id of the switch to configure. The Network device id is
                identified from the GET network device API /dna/intent/api/v1/network-device response.
            feature(str): feature path parameter. Name of the feature to delete.
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
            https://developer.cisco.com/docs/dna-center/#!delete-intended-network-settings-configurations
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/campus/api/v1/switches/{id}/configs/intended/networ"
            + "kSettings/{feature}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c7cb6993eea05af1b710666f8e257a8e_v3_2_3_0", json_data
        )

    def update_intended_network_settings_configurations(
        self,
        feature,
        id,
        dhcpExcludedAddressConfig=None,
        dhcpGeneralConfig=None,
        domainConfig=None,
        ipV4DhcpPoolConfig=None,
        ipV6DhcpPoolConfig=None,
        nameServerConfig=None,
        ntpAuthenticationKeyConfig=None,
        ntpGeneralConfig=None,
        ntpPerVrfServerConfig=None,
        ntpServerConfig=None,
        ntpTrustedKeyConfig=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API updates the configurations for an intended feature on a switch. Updates to other intended features can
        be done over several iterations. Once all the updates to intended features are complete, they can be
        deployed to a device using the API /api/v1/switches/{id}/configs/intended/deploy. When the intended
        features are deployed, they are applied on top of the existing configurations on the device. Any
        existing configurations on the device which are not included in the intended features, are retained on
        the device.

        Args:
            dhcpExcludedAddressConfig(object): Wired's Feature configures mapping to Excluded addresses, both
                excluded low-address IP and excluded low-high IP ranges.
            dhcpGeneralConfig(object): Wired's This feature is for configuring DHCP BOOTP protocol.
            domainConfig(object): Wired's This feature is for configuring IP domain.
            ipV4DhcpPoolConfig(object): Wired's This feature is for configuring IP DHCP pools.
            ipV6DhcpPoolConfig(object): Wired's This feature is for configuring IPv6 DHCP pools.
            nameServerConfig(object): Wired's This feature is for configuring name server.
            ntpAuthenticationKeyConfig(object): Wired's This feature is for configuring NTP which synchronizes the
                system clock with network time servers to ensure accurate timekeeping.
            ntpGeneralConfig(object): Wired's This feature is for configuring NTP which synchronizes the system
                clock with network time servers to ensure accurate timekeeping.
            ntpPerVrfServerConfig(object): Wired's This feature is for configuring NTP which synchronizes the system
                clock with network time servers to ensure accurate timekeeping.
            ntpServerConfig(object): Wired's This feature is for configuring NTP which synchronizes the system clock
                with network time servers to ensure accurate timekeeping.
            ntpTrustedKeyConfig(object): Wired's This feature is for configuring NTP which synchronizes the system
                clock with network time servers to ensure accurate timekeeping.
            id(str): id path parameter. Network device id of the switch to configure. The Network device id is
                identified from the GET network device API /dna/intent/api/v1/network-device response.
            feature(str): feature path parameter. Name of the feature to configure.
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
            https://developer.cisco.com/docs/dna-center/#!update-intended-network-settings-configurations
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }
        _payload = {
            "ntpGeneralConfig": ntpGeneralConfig,
            "ntpAuthenticationKeyConfig": ntpAuthenticationKeyConfig,
            "ntpTrustedKeyConfig": ntpTrustedKeyConfig,
            "ntpServerConfig": ntpServerConfig,
            "ntpPerVrfServerConfig": ntpPerVrfServerConfig,
            "nameServerConfig": nameServerConfig,
            "domainConfig": domainConfig,
            "ipV4DhcpPoolConfig": ipV4DhcpPoolConfig,
            "ipV6DhcpPoolConfig": ipV6DhcpPoolConfig,
            "dhcpExcludedAddressConfig": dhcpExcludedAddressConfig,
            "dhcpGeneralConfig": dhcpGeneralConfig,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a43a9f24a3705db1a74241b01ebc991d_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/campus/api/v1/switches/{id}/configs/intended/networ"
            + "kSettings/{feature}"
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
            "bpm_a43a9f24a3705db1a74241b01ebc991d_v3_2_3_0", json_data
        )

    def get_deployed_configuration_learning_status(
        self,
        deviceUuids=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Returns the deployed configuration learning status for each requested device UUID. Device status is available
        after an enable or disable request has been accepted.

        Args:
            deviceUuids(list): Wired's One or more switch UUIDs. The Network device id can be identified from the
                GET network device API /dna/intent/api/v1/network-device response. (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!get-deployed-configuration-learning-status
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
            "deviceUuids": deviceUuids,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ead369243e89557580bd605ba8e110b6_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/campus/api/v1/switches/configs/status"
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
            "bpm_ead369243e89557580bd605ba8e110b6_v3_2_3_0", json_data
        )

    def get_supported_network_settings_features(
        self, id, headers=None, **request_parameters
    ):
        """Returns the list of supported network settings features for the specified switch.

        Args:
            id(str): id path parameter. Network device id of the switch. The Network device id is identified from
                the GET network device API /dna/intent/api/v1/network-device response.
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
            https://developer.cisco.com/docs/dna-center/#!get-supported-network-settings-features
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

        e_url = (
            "/dna/campus/api/v1/switches/{id}/configs/supported/netwo" + "rkSettings"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d399a5429f0536ab4250374a75d1973_v3_2_3_0", json_data
        )

    def get_deployed_network_settings_configurations(
        self, feature, id, limit=None, offset=None, headers=None, **request_parameters
    ):
        """Returns deployed configuration entries for the specified network settings feature on the switch. The device
        config learning must have enabled for the switch using the API
        /dna/campus/api/v1/switches/configs/deployed/enable and Error code NCCO15475 can be observed if not
        enabled.

        Args:
            id(str): id path parameter. Network device id of the switch to retrieve configuration. The Network
                device id is identified from the GET network device API /dna/intent/api/v1/network-
                device response. for.
            feature(str): feature path parameter. Name of the feature to retrieve Network Settings configuration
                for. The API /api/v1/switches/{id}/configs/supported/networkSettings can be used to get
                the list of features supported on a device.
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
            https://developer.cisco.com/docs/dna-center/#!get-deployed-network-settings-configurations
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
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
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/campus/api/v1/switches/{id}/configs/deployed/networ"
            + "kSettings/{feature}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c6400c350f5b06bc0719c938a10e7b_v3_2_3_0", json_data
        )

    def get_number_of_configurations_for_an_intended_layer2_feature_on_a_wired_device(
        self, feature, id, headers=None, **request_parameters
    ):
        """This API returns the count of the instances of the configurations for an intended layer 2 feature on a wired
        device.  Released for gathering feedbacks from early adopters. API design is not final and future
        updates of this API may implement changes to any aspects of the API design.

        Args:
            id(str): id path parameter. Network device ID of the wired device to configure.
            feature(str): feature path parameter. Name of the feature to configure. The API
                /dna/intent/api/v1/networkDevices/{id}/configFeatures/supported/layer2 can be used to
                get the list of features supported on a device.
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
            https://developer.cisco.com/docs/dna-center/#!get-number-of-configurations-for-an-intended-layer2-feature-on-a-wired-device
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wired/networkDevices/{id}/configFeatu"
            + "res/intended/layer2/{feature}/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory("bpm_d2cca58398312cb0129d39d8c_v3_2_3_0", json_data)

    def get_intended_security_config_count(
        self, feature, id, headers=None, **request_parameters
    ):
        """Returns the number of intended configuration feature entries for the specified security feature on the switch.
        The feature entriesconfiguration can be retrieved using
        /dna/campus/api/v1/switches/{id}/configs/intended/security/{feature}.

        Args:
            id(str): id path parameter. Network device id of the switch. The Network device id can be identified
                from the GET network device API /dna/intent/api/v1/network-device response.
            feature(str): feature path parameter. Name of the feature to configure. The API
                /api/v1/switches/{id}/configs/supported/security can be used to get the list of features
                supported on a device.
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
            https://developer.cisco.com/docs/dna-center/#!get-intended-security-config-count
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/campus/api/v1/switches/{id}/configs/intended/securi"
            + "ty/{feature}/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f8e5737305424add787cbd20fe2bc_v3_2_3_0", json_data
        )

    def delete_intended_layer3_configurations(
        self, feature, id, headers=None, **request_parameters
    ):
        """This API deletes the configurations for an intended feature on a switch. Once all the updates to intended
        features are complete, they can be deployed to a device using the API
        /api/v1/switches/{id}/configs/intended/deploy. When the intended features are deployed, they are applied
        on top of the existing configurations on the device. Any existing configurations on the device which are
        not included in the intended features, are retained on the device.

        Args:
            id(str): id path parameter. Network device id of the switch. The Network device id can be identified
                from the GET network device API /dna/intent/api/v1/network-device response.
            feature(str): feature path parameter. Name of the feature to delete. The API
                /api/v1/switches/{id}/configs/supported/layer3 can be used to get the list of features
                supported on a device.
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
            https://developer.cisco.com/docs/dna-center/#!delete-intended-layer3-configurations
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/campus/api/v1/switches/{id}/configs/intended/layer3" + "/{feature}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c0d437df555638b0fcac4cb8e04750_v3_2_3_0", json_data
        )

    def update_intended_layer3_configurations(
        self,
        feature,
        id,
        bfdConfig=None,
        bfdTemplateSingleHopConfig=None,
        dhcpRelayConfig=None,
        ipv4RoutesConfig=None,
        ipv4RoutingConfig=None,
        ipv4VrfConfig=None,
        ipv4VrfRoutesConfig=None,
        ipv6RoutesConfig=None,
        ipv6RoutingConfig=None,
        ipv6VrfRoutesConfig=None,
        loopbackConfig=None,
        sviConfig=None,
        vrfConfig=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API updates the configurations for an intended feature on a switch. Updates to other intended features can
        be done over several iterations. Once all the updates to intended features are complete, they can be
        deployed to a device using the API /api/v1/switches/{id}/configs/intended/deploy. When the intended
        features are deployed, they are applied on top of the existing configurations on the device. Any
        existing configurations on the device which are not included in the intended features, are retained on
        the device.

        Args:
            bfdConfig(object): Wired's This feature is for configuring BFD globally. BFD (Bidirectional Forwarding
                Detection) is a network protocol that detects link failures in a network and rapidly
                notifies the network devices so that they can reroute traffic. BFD is used to detect
                failures in the forwarding path between two network devices, such as routers or
                switches.
            bfdTemplateSingleHopConfig(object): Wired's This feature is for configuring BFD on a single hop. BFD
                (Bidirectional Forwarding Detection) is a network protocol that detects link failures in
                a network and rapidly notifies the network devices so that they can reroute traffic. BFD
                is used to detect failures in the forwarding path between two network devices, such as
                routers or switches.
            dhcpRelayConfig(object): Wired's This feature is for configuring DHCP Relay. DHCP Relay is a feature
                that allows DHCP messages to be relayed from one subnet to another. This is useful when
                the DHCP server is not on the same subnet as the client. The DHCP relay agent listens
                for DHCP messages on the local subnet and forwards them to the DHCP server. The DHCP
                server then sends the DHCP response back to the relay agent, which forwards it to the
                client.
            ipv4RoutesConfig(object): Wired's This feature is for configuring IPv4 routes. A route is a path that
                network traffic takes from one network device to another. Routes are used to determine
                the best path for forwarding packets between networks. IPv4 routes are used to forward
                IPv4 packets between networks.
            ipv4RoutingConfig(object): Wired's This feature is for configuring routing. Routing is the process of
                selecting paths in a network along which to send network traffic. Routing is performed
                by routers, which are network devices that forward data packets between networks.
                Routers use routing tables to determine the best path for forwarding packets.
            ipv4VrfConfig(object): Wired's This feature is for configuring IPv4 VRFs. A VRF (Virtual Routing and
                Forwarding) is a technology that allows multiple instances of a routing table to coexist
                within the same router at the same time. VRFs are used to isolate network traffic and
                provide network segmentation and security.
            ipv4VrfRoutesConfig(object): Wired's This feature is for configuring IPv4 VRF routes. A route is a path
                that network traffic takes from one network device to another. Routes are used to
                determine the best path for forwarding packets between networks. IPv4 VRF routes are
                used to forward IPv4 packets between networks within a Virtual Routing and Forwarding
                (VRF) instance.
            ipv6RoutesConfig(object): Wired's This feature is for configuring IPv6 routes. A route is a path that
                network traffic takes from one network device to another. Routes are used to determine
                the best path for forwarding packets between networks. IPv6 routes are used to forward
                IPv6 packets between networks.
            ipv6RoutingConfig(object): Wired's This feature is for configuring routing. Routing is the process of
                selecting paths in a network along which to send network traffic. Routing is performed
                by routers, which are network devices that forward data packets between networks.
                Routers use routing tables to determine the best path for forwarding packets.
            ipv6VrfRoutesConfig(object): Wired's This feature is for configuring IPv6 VRF routes. A route is a path
                that network traffic takes from one network device to another. Routes are used to
                determine the best path for forwarding packets between networks. IPv6 VRF routes are
                used to forward IPv6 packets between networks within a Virtual Routing and Forwarding
                (VRF) instance.
            loopbackConfig(object): Wired's This feature is for configuring loopback interfaces. A loopback
                interface is a virtual interface that is always up and allows a device to communicate
                with itself. Loopback interfaces are used for management, routing, and testing purposes.
            sviConfig(object): Wired's This feature is for configuring Switched Virtual Interfaces (SVIs). SVIs are
                virtual interfaces that represent VLANs on a switch. They are used to route traffic
                between VLANs. SVIs are used for inter-VLAN routing and are associated with a VLAN.
            vrfConfig(object): Wired's This feature is for configuring VRFs. A VRF (Virtual Routing and Forwarding)
                is a technology that allows multiple instances of a routing table to coexist within the
                same router at the same time. VRFs are used to isolate network traffic and provide
                network segmentation and security.
            id(str): id path parameter. Network device id of the switch. The Network device id can be identified
                from the GET network device API /dna/intent/api/v1/network-device response.
            feature(str): feature path parameter. Name of the feature to configure. The API
                /api/v1/switches/{id}/configs/supported/layer3 can be used to get the list of features
                supported on a device.
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
            https://developer.cisco.com/docs/dna-center/#!update-intended-layer3-configurations
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }
        _payload = {
            "dhcpRelayConfig": dhcpRelayConfig,
            "loopbackConfig": loopbackConfig,
            "sviConfig": sviConfig,
            "bfdTemplateSingleHopConfig": bfdTemplateSingleHopConfig,
            "bfdConfig": bfdConfig,
            "ipv4RoutingConfig": ipv4RoutingConfig,
            "ipv6RoutingConfig": ipv6RoutingConfig,
            "ipv4RoutesConfig": ipv4RoutesConfig,
            "ipv4VrfRoutesConfig": ipv4VrfRoutesConfig,
            "ipv6RoutesConfig": ipv6RoutesConfig,
            "ipv6VrfRoutesConfig": ipv6VrfRoutesConfig,
            "vrfConfig": vrfConfig,
            "ipv4VrfConfig": ipv4VrfConfig,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_fb6660c599b5b12832f5e82b1e5b56a_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/campus/api/v1/switches/{id}/configs/intended/layer3" + "/{feature}"
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
            "bpm_fb6660c599b5b12832f5e82b1e5b56a_v3_2_3_0", json_data
        )

    def get_intended_layer3_configurations(
        self, feature, id, limit=None, offset=None, headers=None, **request_parameters
    ):
        """This API returns the configurations for an intended layer 3 feature on a switch. Even after the intended
        configurations are deployed using the API /api/v1/switches/{id}/configs/intended/deploy, they continue
        to be a part of the intended features on the device.

        Args:
            id(str): id path parameter. Network device id of the switch. The Network device id can be identified
                from the GET network device API /dna/intent/api/v1/network-device response.
            feature(str): feature path parameter. Name of the feature to configure. The API
                /api/v1/switches/{id}/configs/supported/layer3 can be used to get the list of features
                supported on a device.
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
            https://developer.cisco.com/docs/dna-center/#!get-intended-layer3-configurations
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
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
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/campus/api/v1/switches/{id}/configs/intended/layer3" + "/{feature}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory("bpm_bf8dd5f23a9a13ab8fde04c16_v3_2_3_0", json_data)

    def add_intended_layer3_configurations(
        self,
        feature,
        id,
        bfdConfig=None,
        bfdTemplateSingleHopConfig=None,
        dhcpRelayConfig=None,
        ipv4RoutesConfig=None,
        ipv4RoutingConfig=None,
        ipv4VrfConfig=None,
        ipv4VrfRoutesConfig=None,
        ipv6RoutesConfig=None,
        ipv6RoutingConfig=None,
        ipv6VrfRoutesConfig=None,
        loopbackConfig=None,
        sviConfig=None,
        vrfConfig=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API creates configurations for an intended feature on a wired device. Once all the updates to intended
        features are complete, they can be deployed to a device using the API
        /api/v1/switches/{id}/configs/intended/deploy. When the intended features are deployed, they are applied
        on top of the existing configurations on the device. Any existing configurations on the device which are
        not included in the intended features, are retained on the device. The device config learning must have
        enabled for the switch using the API /dna/campus/api/v1/switches/configs/enable and Error code NCCO15475
        can be observed if not enabled.

        Args:
            bfdConfig(object): Wired's This feature is for configuring BFD globally. BFD (Bidirectional Forwarding
                Detection) is a network protocol that detects link failures in a network and rapidly
                notifies the network devices so that they can reroute traffic. BFD is used to detect
                failures in the forwarding path between two network devices, such as routers or
                switches.
            bfdTemplateSingleHopConfig(object): Wired's This feature is for configuring BFD on a single hop. BFD
                (Bidirectional Forwarding Detection) is a network protocol that detects link failures in
                a network and rapidly notifies the network devices so that they can reroute traffic. BFD
                is used to detect failures in the forwarding path between two network devices, such as
                routers or switches.
            dhcpRelayConfig(object): Wired's This feature is for configuring DHCP Relay. DHCP Relay is a feature
                that allows DHCP messages to be relayed from one subnet to another. This is useful when
                the DHCP server is not on the same subnet as the client. The DHCP relay agent listens
                for DHCP messages on the local subnet and forwards them to the DHCP server. The DHCP
                server then sends the DHCP response back to the relay agent, which forwards it to the
                client.
            ipv4RoutesConfig(object): Wired's This feature is for configuring IPv4 routes. A route is a path that
                network traffic takes from one network device to another. Routes are used to determine
                the best path for forwarding packets between networks. IPv4 routes are used to forward
                IPv4 packets between networks.
            ipv4RoutingConfig(object): Wired's This feature is for configuring routing. Routing is the process of
                selecting paths in a network along which to send network traffic. Routing is performed
                by routers, which are network devices that forward data packets between networks.
                Routers use routing tables to determine the best path for forwarding packets.
            ipv4VrfConfig(object): Wired's This feature is for configuring IPv4 VRFs. A VRF (Virtual Routing and
                Forwarding) is a technology that allows multiple instances of a routing table to coexist
                within the same router at the same time. VRFs are used to isolate network traffic and
                provide network segmentation and security.
            ipv4VrfRoutesConfig(object): Wired's This feature is for configuring IPv4 VRF routes. A route is a path
                that network traffic takes from one network device to another. Routes are used to
                determine the best path for forwarding packets between networks. IPv4 VRF routes are
                used to forward IPv4 packets between networks within a Virtual Routing and Forwarding
                (VRF) instance.
            ipv6RoutesConfig(object): Wired's This feature is for configuring IPv6 routes. A route is a path that
                network traffic takes from one network device to another. Routes are used to determine
                the best path for forwarding packets between networks. IPv6 routes are used to forward
                IPv6 packets between networks.
            ipv6RoutingConfig(object): Wired's This feature is for configuring routing. Routing is the process of
                selecting paths in a network along which to send network traffic. Routing is performed
                by routers, which are network devices that forward data packets between networks.
                Routers use routing tables to determine the best path for forwarding packets.
            ipv6VrfRoutesConfig(object): Wired's This feature is for configuring IPv6 VRF routes. A route is a path
                that network traffic takes from one network device to another. Routes are used to
                determine the best path for forwarding packets between networks. IPv6 VRF routes are
                used to forward IPv6 packets between networks within a Virtual Routing and Forwarding
                (VRF) instance.
            loopbackConfig(object): Wired's This feature is for configuring loopback interfaces. A loopback
                interface is a virtual interface that is always up and allows a device to communicate
                with itself. Loopback interfaces are used for management, routing, and testing purposes.
            sviConfig(object): Wired's This feature is for configuring Switched Virtual Interfaces (SVIs). SVIs are
                virtual interfaces that represent VLANs on a switch. They are used to route traffic
                between VLANs. SVIs are used for inter-VLAN routing and are associated with a VLAN.
            vrfConfig(object): Wired's This feature is for configuring VRFs. A VRF (Virtual Routing and Forwarding)
                is a technology that allows multiple instances of a routing table to coexist within the
                same router at the same time. VRFs are used to isolate network traffic and provide
                network segmentation and security.
            id(str): id path parameter. Network device id of the switch. The Network device id can be identified
                from the GET network device API /dna/intent/api/v1/network-device response.
            feature(str): feature path parameter. Name of the feature to configure. The API
                /api/v1/switches/{id}/configs/supported/layer3 can be used to get the list of features
                supported on a device.
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
            https://developer.cisco.com/docs/dna-center/#!add-intended-layer3-configurations
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }
        _payload = {
            "dhcpRelayConfig": dhcpRelayConfig,
            "loopbackConfig": loopbackConfig,
            "sviConfig": sviConfig,
            "bfdTemplateSingleHopConfig": bfdTemplateSingleHopConfig,
            "bfdConfig": bfdConfig,
            "ipv4RoutingConfig": ipv4RoutingConfig,
            "ipv6RoutingConfig": ipv6RoutingConfig,
            "ipv4RoutesConfig": ipv4RoutesConfig,
            "ipv4VrfRoutesConfig": ipv4VrfRoutesConfig,
            "ipv6RoutesConfig": ipv6RoutesConfig,
            "ipv6VrfRoutesConfig": ipv6VrfRoutesConfig,
            "vrfConfig": vrfConfig,
            "ipv4VrfConfig": ipv4VrfConfig,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_eccb282c36ab52739f4bd3ea3a8217d9_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/campus/api/v1/switches/{id}/configs/intended/layer3" + "/{feature}"
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
            "bpm_eccb282c36ab52739f4bd3ea3a8217d9_v3_2_3_0", json_data
        )

    def get_intended_network_settings_config_count(
        self, feature, id, headers=None, **request_parameters
    ):
        """Returns the number of intended configuration entries for the specified layer 3 feature on the switch. The
        feature configuration entries can be retrieved using
        /dna/campus/api/v1/switches/{id}/configs/intended/networkSettings/{feature}.

        Args:
            id(str): id path parameter. Network device id of the switch to configure. The Network device id is
                identified from the GET network device API /dna/intent/api/v1/network-device response.
            feature(str): feature path parameter. Name of the feature to configure. The API
                /api/v1/switches/{id}/configs/supported/networkSettings can be used to get the list of
                features supported on a device.
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
            https://developer.cisco.com/docs/dna-center/#!get-intended-network-settings-config-count
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/campus/api/v1/switches/{id}/configs/intended/networ"
            + "kSettings/{feature}/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_aa604b7528954c0b504a4404fd7779f_v3_2_3_0", json_data
        )

    def gets_the_device_config_for_the_configuration_model(
        self, network_device_id, preview_activity_id, headers=None, **request_parameters
    ):
        """Gets the device config for the configuration model. This API is 'Step 3' in the following workflow. Step 1Use
        'POST /intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels'
        to start the provision of intended features. The response has a taskId which is the previewActivityId in
        all subsequent APIs. The task must be successfully complete before proceeding to the next step. It is
        not recommended to proceed when there is any task failure in this step. The API 'DELETE /intent/api/v1/w
        ired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivityId}'
        can be used at any step to discard/cancel the provision of intended features. Step 2Use 'POST /intent/ap
        i/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivity
        Id}/networkDevices/{networkDeviceId}/config' to generate device CLIs for preview. The response has a
        task ID. The task must be successfully complete before using the GET API to view CLIs. It is not
        recommended to proceed when there is any task failure(s) in this step. The API 'DELETE /intent/api/v1/wi
        red/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivityId}'
        can be used at any step to discard/cancel the provision of intended features. Step 3Use 'GET /intent/api
        /v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivityI
        d}/networkDevices/{networkDeviceId}/config' to view the CLIs that will be applied to the device. Step
        4Use 'POST /intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationMo
        dels/{previewActivityId}/deploy' to deploy the intent to the device.  Released for gathering feedbacks
        from early adopters. API design is not final and future updates of this API may implement changes to any
        aspects of the API design.

        Args:
            network_device_id(str): networkDeviceId path parameter. Network device ID of the wired device to
                provision. The API /intent/api/v1/network-device can be used to get the network device
                ID.
            preview_activity_id(str): previewActivityId path parameter. Activity id is the taskId from Step 2'POST /
                intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurati
                onModels/{previewActivityId}/networkDevices/{networkDeviceId}/config.
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
            https://developer.cisco.com/docs/dna-center/#!gets-the-device-config-for-the-configuration-model
        """
        check_type(headers, dict)
        check_type(network_device_id, str, may_be_none=False)
        check_type(preview_activity_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
            "previewActivityId": preview_activity_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wired/networkDevices/{networkDeviceId"
            + "}/configFeatures/intended/configurationModels/{previewAc"
            + "tivityId}/config"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f7fdcd6e2dd5f4eaf7ceed5e5856ba2_v3_2_3_0", json_data
        )

    def generate_the_device_config_for_the_configuration_model(
        self, network_device_id, preview_activity_id, headers=None, **request_parameters
    ):
        """Generates the device config for the configuration model. This API is 'Step 2' in the following workflow  Step
        1Use 'POST
        /intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels' to
        start the provision of intended features. The response has a taskId which is the previewActivityId in
        all subsequent APIs. The task must be successfully complete before proceeding to the next step. It is
        not recommended to proceed when there is any task failure in this step. The API 'DELETE /intent/api/v1/w
        ired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivityId}'
        can be used at any step to discard/cancel the provision of intended features. Step 2Use 'POST /intent/ap
        i/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivity
        Id}/networkDevices/{networkDeviceId}/config' to generate device CLIs for preview. The response has a
        task ID. The task must be successfully complete before using the GET API to view CLIs. It is not
        recommended to proceed when there is any task failure(s) in this step. The API 'DELETE /intent/api/v1/wi
        red/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivityId}'
        can be used at any step to discard/cancel the provision of intended features. Step 3Use 'GET /intent/api
        /v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivityI
        d}/networkDevices/{networkDeviceId}/config' to view the CLIs that will be applied to the device. Step
        4Use 'POST /intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationMo
        dels/{previewActivityId}/deploy' to deploy the intent to the device.  Released for gathering feedbacks
        from early adopters. API design is not final and future updates of this API may implement changes to any
        aspects of the API design.

        Args:
            network_device_id(str): networkDeviceId path parameter. Network device ID of the wired device to
                provision. The API /intent/api/v1/network-device can be used to get the network device
                ID.
            preview_activity_id(str): previewActivityId path parameter. Activity id is taskId from Step 1POST
                /intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurat
                ionModels'.
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
            https://developer.cisco.com/docs/dna-center/#!generate-the-device-config-for-the-configuration-model
        """
        check_type(headers, dict)
        check_type(network_device_id, str, may_be_none=False)
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
            "networkDeviceId": network_device_id,
            "previewActivityId": preview_activity_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wired/networkDevices/{networkDeviceId"
            + "}/configFeatures/intended/configurationModels/{previewAc"
            + "tivityId}/config"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e174c2cf0ecb5b52806a95a08477ae4d_v3_2_3_0", json_data
        )

    def delete_the_configuration_model(
        self, network_device_id, preview_activity_id, headers=None, **request_parameters
    ):
        """Deletes the configuration model. The API can be used at any step to discard/cancel the provision of intended
        features.  Released for gathering feedbacks from early adopters. API design is not final and future
        updates of this API may implement changes to any aspects of the API design.

        Args:
            network_device_id(str): networkDeviceId path parameter. Network device ID of the wired device to
                provision. The API /intent/api/v1/network-device can be used to get the network device
                ID.
            preview_activity_id(str): previewActivityId path parameter. Activity id from POST
                /intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurat
                ionModels or /intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intend
                ed/configurationModels/{previewActivityId}/networkDevices/{networkDeviceId}/config.
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
            https://developer.cisco.com/docs/dna-center/#!delete-the-configuration-model
        """
        check_type(headers, dict)
        check_type(network_device_id, str, may_be_none=False)
        check_type(preview_activity_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
            "previewActivityId": preview_activity_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wired/networkDevices/{networkDeviceId"
            + "}/configFeatures/intended/configurationModels/{previewAc"
            + "tivityId}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fec9a36b80305b5593608e369fa05b64_v3_2_3_0", json_data
        )

    def deploy_the_intended_configuration_features(
        self, id, headers=None, **request_parameters
    ):
        """This API deploys intended configuration features on a switch. This can be used only if the provisioning settings
        do not require Preview or ITSM Approval before deploying configurations on network devices. The API
        /intent/api/v1/provisioningSettings can be used to get or update provisioning settings. The API
        /dna/campus/api/v1/switches/{id}/configs/intended/validate must be used to identiy the pre-deploy config
        feature validations.

        Args:
            id(str): id path parameter. Network device id of the switch to provision. The API
                /intent/api/v1/network-device can be used to get the network device ID.
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
            https://developer.cisco.com/docs/dna-center/#!deploy-the-intended-configuration-features
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

        e_url = (
            "/dna/campus/api/v1/provision/switches/{id}/configs/inten" + "ded/deploy"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d366656fa65a608e81c4f823689229_v3_2_3_0", json_data
        )

    def create_a_configuration_model_for_the_intended_configs_for_a_wired_device(
        self, network_device_id, headers=None, **request_parameters
    ):
        """Create a configuration model for the intended configs for a wired device. This is a pre-requisite to preview the
        generated device config for the provisioning intent. This is mandatory if the provisioning settings
        require Preview or ITSM Approval before deploying configurations on network devices. The API
        /intent/api/v1/provisioningSettings can be used to get or update provisioning settings. This API is
        'Step 1' in the following workflow Step 1Use 'POST
        /intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels' to
        start the provision of intended features. The response has a taskId which is the previewActivityId in
        all subsequent APIs. The task must be successfully complete before proceeding to the next step. It is
        not recommended to proceed when there is any task failure in this step. The API 'DELETE /intent/api/v1/w
        ired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivityId}'
        can be used at any step to discard/cancel the provision of intended features. Step 2Use 'POST /intent/ap
        i/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivity
        Id}/networkDevices/{networkDeviceId}/config' to generate device CLIs for preview. The response has a
        task ID. The task must be successfully complete before using the GET API to view CLIs. It is not
        recommended to proceed when there is any task failure(s) in this step. The API 'DELETE /intent/api/v1/wi
        red/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivityId}'
        can be used at any step to discard/cancel the provision of intended features. Step 3Use 'GET /intent/api
        /v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivityI
        d}/networkDevices/{networkDeviceId}/config' to view the CLIs that will be applied to the device. Step
        4Use 'POST /intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationMo
        dels/{previewActivityId}/deploy' to deploy the intent to the device.  Released for gathering feedbacks
        from early adopters. API design is not final and future updates of this API may implement changes to any
        aspects of the API design.

        Args:
            network_device_id(str): networkDeviceId path parameter. Network device ID of the wired device to
                provision. The API /intent/api/v1/network-device can be used to get the network device
                ID.
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
            https://developer.cisco.com/docs/dna-center/#!create-a-configuration-model-for-the-intended-configs-for-a-wired-device
        """
        check_type(headers, dict)
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
            "networkDeviceId": network_device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wired/networkDevices/{networkDeviceId"
            + "}/configFeatures/intended/configurationModels"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c74d2bae55f85924002ddb92fe064_v3_2_3_0", json_data
        )

    def get_number_of_configurations_for_a_deployed_layer2_feature_on_a_wired_device(
        self, feature, id, headers=None, **request_parameters
    ):
        """The API returns the number of configurations for a deployed layer 2 feature on a wired device.  Released for
        gathering feedbacks from early adopters. API design is not final and future updates of this API may
        implement changes to any aspects of the API design.

        Args:
            id(str): id path parameter. Network device ID of the wired device to retrieve configuration for.
            feature(str): feature path parameter. Name of the feature to retrieve configuration for. The API
                /dna/intent/api/v1/networkDevices/{id}/configFeatures/supported/layer2 can be used to
                get the list of features supported on a device.
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
            https://developer.cisco.com/docs/dna-center/#!get-number-of-configurations-for-a-deployed-layer2-feature-on-a-wired-device
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wired/networkDevices/{id}/configFeatu"
            + "res/deployed/layer2/{feature}/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e495979e25a6559394fbad6fcd4c495a_v3_2_3_0", json_data
        )

    def get_configurations_for_a_deployed_layer2_feature_on_a_wired_device(
        self, feature, id, headers=None, **request_parameters
    ):
        """The API returns configurations for a deployed layer 2 feature on a wired device.  Released for gathering
        feedbacks from early adopters. API design is not final and future updates of this API may implement
        changes to any aspects of the API design.

        Args:
            id(str): id path parameter. Network device ID of the wired device to retrieve configuration for.
            feature(str): feature path parameter. Name of the feature to retrieve Layer 2 configuration for. The API
                /dna/intent/api/v1/networkDevices/{id}/configFeatures/supported/layer2 can be used to
                get the list of features supported on a device.
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
            https://developer.cisco.com/docs/dna-center/#!get-configurations-for-a-deployed-layer2-feature-on-a-wired-device
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wired/networkDevices/{id}/configFeatu"
            + "res/deployed/layer2/{feature}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fcf9673050079b4abedf3ffc9777_v3_2_3_0", json_data
        )

    def get_deployed_port_feature_instance_count(
        self, feature, id, headers=None, **request_parameters
    ):
        """Returns the number of deployed configuration entries for the specified port feature on the switch. The device
        config learning must have enabled for the switch using the API
        /dna/campus/api/v1/switches/configs/deployed/enable and Error code NCCO15475 can be observed if not
        enabled.

        Args:
            id(str): id path parameter. Network device id of the switch. The Network device id can be identified
                from the GET network device API /dna/intent/api/v1/network-device response.
            feature(str): feature path parameter. Name of the feature to retrieve configuration for. The API
                /api/v1/switches/{id}/configs/supported/port can be used to get the list of features
                supported on a device.
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
            https://developer.cisco.com/docs/dna-center/#!get-deployed-port-feature-instance-count
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/campus/api/v1/switches/{id}/configs/deployed/port/{"
            + "feature}/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b8d1033aa31e5e1d8d6aa481418898e1_v3_2_3_0", json_data
        )

    def deploy_the_intended_configuration_features_on_a_wired_device(
        self, network_device_id, headers=None, **request_parameters
    ):
        """Deploy the intended configuration features on a wired device. This can be used only if the provisioning settings
        do not require Preview or ITSM Approval before deploying configurations on network devices. The API
        /intent/api/v1/provisioningSettings can be used to get or update provisioning settings.  Released for
        gathering feedbacks from early adopters. API design is not final and future updates of this API may
        implement changes to any aspects of the API design.

        Args:
            network_device_id(str): networkDeviceId path parameter. Network device ID of the wired device to
                provision. The API /intent/api/v1/network-device can be used to get the network device
                ID.
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
            https://developer.cisco.com/docs/dna-center/#!deploy-the-intended-configuration-features-on-a-wired-device
        """
        check_type(headers, dict)
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
            "networkDeviceId": network_device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wired/networkDevices/{networkDeviceId"
            + "}/configFeatures/intended/deploy"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a21cb2b7ea258e197f22082301cd1cc_v3_2_3_0", json_data
        )

    def disable_per_device_configuration_pdc_learning(
        self,
        deviceUuids=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Disables deployed configuration learning for the specified switches. This operation is synchronous and returns
        an HTTP 200 response when successful.

        Args:
            deviceUuids(list): Wired's One or more switch UUIDs. (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!disable-per-device-configuration-p-d-c-learning
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
            "deviceUuids": deviceUuids,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d91b7695ad79539e972a1a8fdbeff540_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/campus/api/v1/switches/configs/disable"
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
            "bpm_d91b7695ad79539e972a1a8fdbeff540_v3_2_3_0", json_data
        )

    def deploy_the_configuration_model_on_the_network_device(
        self, network_device_id, preview_activity_id, headers=None, **request_parameters
    ):
        """This API deploys the configuration model on the network device. This is the final step 'Step 4' of the following
        workflow. Step 1Use 'POST
        /intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels' to
        start the provision of intended features. The response has a taskId which is the previewActivityId in
        all subsequent APIs. The task must be successfully complete before proceeding to the next step. It is
        not recommended to proceed when there is any task failure in this step. The API 'DELETE /intent/api/v1/w
        ired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivityId}'
        can be used at any step to discard/cancel the provision of intended features. Step 2Use 'POST /intent/ap
        i/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivity
        Id}/networkDevices/{networkDeviceId}/config' to generate device CLIs for preview. The response has a
        task ID. The task must be successfully complete before using the GET API to view CLIs. It is not
        recommended to proceed when there is any task failure(s) in this step. The API 'DELETE /intent/api/v1/wi
        red/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivityId}'
        can be used at any step to discard/cancel the provision of intended features. Step 3Use 'GET /intent/api
        /v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivityI
        d}/networkDevices/{networkDeviceId}/config' to view the CLIs that will be applied to the device. Step
        4Use 'POST /intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationMo
        dels/{previewActivityId}/deploy' to push the intent to the device.  Released for gathering feedbacks
        from early adopters. API design is not final and future updates of this API may implement changes to any
        aspects of the API design.

        Args:
            network_device_id(str): networkDeviceId path parameter. Network device ID of the wired device to
                provision. The API /intent/api/v1/network-device can be used to get the network device
                ID.
            preview_activity_id(str): previewActivityId path parameter. Activity id from intent/api/v1/activity.
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
            https://developer.cisco.com/docs/dna-center/#!deploy-the-configuration-model-on-the-network-device
        """
        check_type(headers, dict)
        check_type(network_device_id, str, may_be_none=False)
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
            "networkDeviceId": network_device_id,
            "previewActivityId": preview_activity_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/intent/api/v1/wired/networkDevices/{n"
            + "etworkDeviceId}/configFeatures/intended/configurationMod"
            + "els/{previewActivityId}/deploy"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b6139c3f3ef15bcf9a42f5283a6aea64_v3_2_3_0", json_data
        )

    def get_supported_port_features(self, id, headers=None, **request_parameters):
        """Returns the list of supported port features for the specified switch.

        Args:
            id(str): id path parameter. Network device id of the switch. The Network device id can be identified
                from the GET network device API /dna/intent/api/v1/network-device response.
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
            https://developer.cisco.com/docs/dna-center/#!get-supported-port-features
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

        e_url = "/dna/campus/api/v1/switches/{id}/configs/supported/port"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e5947f60a1e566795feefce5becff4c_v3_2_3_0", json_data
        )

    def convert_intended_port_configurations(
        self,
        id,
        names=None,
        targetType=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API converts port configurations between Layer 2 and Layer 3 modes on a switch. The conversion is supported
        for the physical ports feature ethernetInterfaceConfig configurations. The device config learning must
        have enabled for the switch using the API /dna/campus/api/v1/switches/configs/deployed/enable and Error
        code NCCO15475 can be observed if not enabled.

        Args:
            names(list): Wired's List of port names to convert. (list of strings).
            targetType(string): Wired's Type of conversion to perform.. Available values are 'LAYER2' and 'LAYER3'.
            id(str): id path parameter. Network device id of the switch. The Network device id is identified from
                the GET network device API /dna/intent/api/v1/network-device response.
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
            https://developer.cisco.com/docs/dna-center/#!convert-intended-port-configurations
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
            "names": names,
            "targetType": targetType,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a630e120285a259cdb78af3c35649a_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/campus/api/v1/switches/{id}/configs/intended/port/c" + "onvert"
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
            "bpm_a630e120285a259cdb78af3c35649a_v3_2_3_0", json_data
        )

    def get_supported_security_features(self, id, headers=None, **request_parameters):
        """Returns the list of supported security features for the specified switch.

        Args:
            id(str): id path parameter. Network device id of the switch. The Network device id can be identified
                from the GET network device API /dna/intent/api/v1/network-device response.
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
            https://developer.cisco.com/docs/dna-center/#!get-supported-security-features
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

        e_url = "/dna/campus/api/v1/switches/{id}/configs/supported/secur" + "ity"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d4df6c41e9ec531f97f8d0580898dce7_v3_2_3_0", json_data
        )

    def update_configurations_for_intended_layer2_features_on_a_wired_device(
        self, id, headers=None, **request_parameters
    ):
        """This API updates the configurations for the intended features on a wired device. Only the feature configurations
        to be changed need to be added to the intended features. Updates to intended features can be done over
        several iterations. Once the updates are complete, the intended features can be deployed to a device
        using the API /dna/intent/api/v1/networkDevices/{id}/configFeatures/intended/deploy. When the intended
        features are deployed, they are applied on top of the existing configurations on the device. Any
        existing configurations on the device which are not included in the intended features, are retained on
        the device.

        Args:
            id(str): id path parameter. Network device ID of the wired device to configure.
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
            https://developer.cisco.com/docs/dna-center/#!update-configurations-for-intended-layer2-features-on-a-wired-device
        """
        check_type(headers, dict)
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

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wired/networkDevices/{id}/configFeatu"
            + "res/intended/layer2"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.put(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ecf0984975fb7af51796da58aca21_v3_2_3_0", json_data
        )

    def create_configurations_for_intended_layer2_features_on_a_wired_device(
        self, id, headers=None, **request_parameters
    ):
        """This API creates configurations for the intended features on a wired device, if none have been added earlier.
        Only the feature configurations to be changed need to be added to the intended features. When the
        intended features are deployed to a device using the API
        /intent/api/v1/networkDevices/{id}/configFeatures/intended/deploy, they are applied on top of the
        existing configurations on the device. Any existing configurations on the device which are not included
        in the intended features, are retained on the device.  Add configurations for intended layer 2 features
        on a wired device. This is needed the first time any intended features are added for a device.

        Args:
            id(str): id path parameter. Network device ID of the wired device to configure.
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
            https://developer.cisco.com/docs/dna-center/#!create-configurations-for-intended-layer2-features-on-a-wired-device
        """
        check_type(headers, dict)
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

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wired/networkDevices/{id}/configFeatu"
            + "res/intended/layer2"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a862379cc525a79a01fc845fdda7d68_v3_2_3_0", json_data
        )

    def get_configurations_for_intended_layer2_features_on_a_wired_device(
        self, feature, id, headers=None, **request_parameters
    ):
        """This API returns the configurations for the intended layer 2 features on a wired device. Even after the intended
        configurations are deployed using the API
        /intent/api/v1/networkDevices/{id}/configFeatures/intended/deploy, they continue to be a part of the
        intended features on the device.  Released for gathering feedbacks from early adopters. API design is
        not final and future updates of this API may implement changes to any aspects of the API design.

        Args:
            id(str): id path parameter. Network device ID of the wired device to configure.
            feature(str): feature query parameter. Name of the feature to configure. The API
                /data/intent/api/wired/networkDevices/{id}/configFeatures/supported/layer2 can be used
                to get the list of features supported on a device.
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
            https://developer.cisco.com/docs/dna-center/#!get-configurations-for-intended-layer2-features-on-a-wired-device
        """
        check_type(headers, dict)
        check_type(feature, str, may_be_none=False)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "feature": feature,
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

        e_url = (
            "/dna/intent/api/v1/wired/networkDevices/{id}/configFeatu"
            + "res/intended/layer2"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_abd659088f65d24ac291d8f1cadcd06_v3_2_3_0", json_data
        )

    def get_service_deployment_status(
        self, deploy_activity_id, network_device_id, headers=None, **request_parameters
    ):
        """Returns service deployment status based on filter criteria.  Released for gathering feedbacks from early
        adopters. API design is not final and future updates of this API may implement changes to any aspects of
        the API design.

        Args:
            network_device_id(str): networkDeviceId path parameter. Network device ID of the wired device to
                provision. The API /intent/api/v1/network-device can be used to get the network device
                ID.
            deploy_activity_id(str): deployActivityId path parameter. Activity Id from the
                /intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/deploy or
                /intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurat
                ionModels/{previewActivityId}/deploy task response.
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
            https://developer.cisco.com/docs/dna-center/#!get-service-deployment-status
        """
        check_type(headers, dict)
        check_type(network_device_id, str, may_be_none=False)
        check_type(deploy_activity_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
            "deployActivityId": deploy_activity_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wired/networkDevices/{networkDeviceId"
            + "}/configFeatures/intended/serviceDeployments"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c16b9caed6045399a6e7744914195fee_v3_2_3_0", json_data
        )

    def get_the_supported_layer2_features_on_a_wired_device(
        self, id, headers=None, **request_parameters
    ):
        """The API returns the supported layer 2 features on a wired device.  Released for gathering feedbacks from early
        adopters. API design is not final and future updates of this API may implement changes to any aspects of
        the API design.

        Args:
            id(str): id path parameter. Network device ID of the wired device.
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
            https://developer.cisco.com/docs/dna-center/#!get-the-supported-layer2-features-on-a-wired-device
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

        e_url = (
            "/dna/intent/api/v1/wired/networkDevices/{id}/configFeatu"
            + "res/supported/layer2"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c4684074beb50b1ae5e77141244ebbd_v3_2_3_0", json_data
        )

    def get_deployed_network_settings_config_count(
        self, feature, id, headers=None, **request_parameters
    ):
        """Returns the number of deployed configuration entries for the specified network settings feature on the switch.
        The device config learning must have enabled for the switch using the API
        /dna/campus/api/v1/switches/configs/deployed/enable and Error code NCCO15475 can be observed if not
        enabled.

        Args:
            id(str): id path parameter. Network device id of the switch to retrieve configuration. The Network
                device id is identified from the GET network device API /dna/intent/api/v1/network-
                device response. for.
            feature(str): feature path parameter. Name of the feature to retrieve configuration for. The API
                /api/v1/switches/{id}/configs/supported/networkSettings can be used to get the list of
                features supported on a device.
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
            https://developer.cisco.com/docs/dna-center/#!get-deployed-network-settings-config-count
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/campus/api/v1/switches/{id}/configs/deployed/networ"
            + "kSettings/{feature}/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e3ee13353b5cb0be7b2e82f0d54e09_v3_2_3_0", json_data
        )

    def get_deployed_layer2_config_count(
        self, feature, id, headers=None, **request_parameters
    ):
        """Returns the number of deployed configuration entries for the specified layer 2 feature on the switch. The device
        config learning must have enabled for the switch using the API
        /dna/campus/api/v1/switches/configs/deployed/enable.

        Args:
            id(str): id path parameter. Network device id of the switch. The Network device id can be identified
                from the GET network device API /dna/intent/api/v1/network-device response.
            feature(str): feature path parameter. Name of the feature to retrieve configuration for. The API
                /api/v1/switches/{id}/configs/supported/layer2 can be used to get the list of features
                supported on a device. The device config learning must have enabled for the switch using
                the API /dna/campus/api/v1/switches/configs/deployed/enable and Error code NCCO15475 can
                be observed if not enabled.
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
            https://developer.cisco.com/docs/dna-center/#!get-deployed-layer2-config-count
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/campus/api/v1/switches/{id}/configs/deployed/layer2"
            + "/{feature}/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_daa0c0905ad8bd3a2fbfd68448a4_v3_2_3_0", json_data
        )

    def get_deployed_layer3_configurations(
        self, feature, id, limit=None, offset=None, headers=None, **request_parameters
    ):
        """Returns deployed configuration entries for the specified layer 3 feature on the switch. The device config
        learning must have enabled for the switch using the API
        /dna/campus/api/v1/switches/configs/deployed/enable and Error code NCCO15475 can be observed if not
        enabled.

        Args:
            id(str): id path parameter. Network device id of the switch. The Network device id can be identified
                from the GET network device API /dna/intent/api/v1/network-device response.
            feature(str): feature path parameter. Name of the feature to retrieve Layer 3 configuration for. The API
                /api/v1/switches/{id}/configs/supported/layer3 can be used to get the list of features
                supported on a device.
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
            https://developer.cisco.com/docs/dna-center/#!get-deployed-layer3-configurations
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
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
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/campus/api/v1/switches/{id}/configs/deployed/layer3" + "/{feature}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f2343f549db494389fc73a8d48_v3_2_3_0", json_data
        )

    def get_intended_layer3_config_count(
        self, feature, id, headers=None, **request_parameters
    ):
        """Returns the number of intended configuration entries for the specified layer 3 feature on the switch. The
        feature entries configuration can be retrieved using
        /dna/campus/api/v1/switches/{id}/configs/intended/layer3/{feature}.

        Args:
            id(str): id path parameter. Network device id of the switch. The Network device id can be identified
                from the GET network device API /dna/intent/api/v1/network-device response.
            feature(str): feature path parameter. Name of the feature to configure. The API
                /api/v1/switches/{id}/configs/supported/layer3 can be used to get the list of features
                supported on a device.
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
            https://developer.cisco.com/docs/dna-center/#!get-intended-layer3-config-count
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/campus/api/v1/switches/{id}/configs/intended/layer3"
            + "/{feature}/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fa845293f2805099859bb684316d71fc_v3_2_3_0", json_data
        )

    def get_supported_layer3_features(self, id, headers=None, **request_parameters):
        """Returns the list of supported layer 3 features for the specified switch.The feature names are the supported to
        be used as feature in the all get deployed layer 3 endpoints.

        Args:
            id(str): id path parameter. Network device ID of the switch.
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
            https://developer.cisco.com/docs/dna-center/#!get-supported-layer3-features
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

        e_url = "/dna/campus/api/v1/switches/{id}/configs/supported/layer" + "3"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c600f5f874530b858d685efd8d4616_v3_2_3_0", json_data
        )

    def get_supported_layer2_features(self, id, headers=None, **request_parameters):
        """Returns the list of supported layer 2 features for the specified switch.

        Args:
            id(str): id path parameter. Network device id of the switch. The Network device id can be identified
                from the GET network device API /dna/intent/api/v1/network-device response.
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
            https://developer.cisco.com/docs/dna-center/#!get-supported-layer2-features
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

        e_url = "/dna/campus/api/v1/switches/{id}/configs/supported/layer" + "2"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e1acc92f0af531182536c3633f6d173_v3_2_3_0", json_data
        )

    def validate_intended_features(self, id, headers=None, **request_parameters):
        """This API validates the intended features for a switch and returns the list of any issues found with the intended
        features. The intended features should be deployed to a device only when there are no issues with the
        intended features.

        Args:
            id(str): id path parameter. Network device id of the switch to configure. The Network device id can be
                identified from the GET network device API /dna/intent/api/v1/network-device response.
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
            https://developer.cisco.com/docs/dna-center/#!validate-intended-features
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

        e_url = "/dna/campus/api/v1/switches/{id}/configs/intended/valida" + "te"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b93f1847c85ce9ad5480c4f8cc0e23_v3_2_3_0", json_data
        )

    def enable_per_device_configuration_pdc_learning(
        self,
        deviceUuids=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Enables deployed configuration learning for the specified switches. All supported features are discovered
        through the sync operation. This operation is asynchronous and returns a task identifier.

        Args:
            deviceUuids(list): Wired's One or more switch UUIDs. The Network device id can be identified from the
                GET network device API /dna/intent/api/v1/network-device response. (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!enable-per-device-configuration-p-d-c-learning
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
            "deviceUuids": deviceUuids,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d3c8d365418a51eaa103bf075f2634f3_v3_2_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/campus/api/v1/switches/configs/enable"
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
            "bpm_d3c8d365418a51eaa103bf075f2634f3_v3_2_3_0", json_data
        )

    def get_intended_layer2_config_count(
        self, feature, id, headers=None, **request_parameters
    ):
        """Returns the number of intended configuration entries for the specified layer 3 feature on the switch. The
        feature configuration entries can be retrieved using
        /dna/campus/api/v1/switches/{id}/configs/intended/layer2/{feature}.

        Args:
            id(str): id path parameter. Network device id of the switch. The Network device id can be identified
                from the GET network device API /dna/intent/api/v1/network-device response.
            feature(str): feature path parameter. Name of the feature to configure. The API
                /api/v1/switches/{id}/configs/supported/layer2 can be used to get the list of features
                supported on a device.
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
            https://developer.cisco.com/docs/dna-center/#!get-intended-layer2-config-count
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/campus/api/v1/switches/{id}/configs/intended/layer2"
            + "/{feature}/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c06558f426465eaabe216f8960eb0496_v3_2_3_0", json_data
        )

    def get_deployed_layer2_configurations(
        self, feature, id, limit=None, offset=None, headers=None, **request_parameters
    ):
        """Returns deployed configuration entries for the specified layer 2 feature on the switch. The device config
        learning must have enabled for the switch using the API
        /dna/campus/api/v1/switches/configs/deployed/enable and Error code NCCO15475 can be observed if not
        enabled.

        Args:
            id(str): id path parameter. Network device id of the switch. The Network device id can be identified
                from the GET network device API /dna/intent/api/v1/network-device response.
            feature(str): feature path parameter. Name of the feature to retrieve Layer 2 configuration for. The API
                /api/v1/switches/{id}/configs/supported/layer2 can be used to get the list of features
                supported on a device.
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
            https://developer.cisco.com/docs/dna-center/#!get-deployed-layer2-configurations
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
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
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/campus/api/v1/switches/{id}/configs/deployed/layer2" + "/{feature}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b5e8d2fbd8dc5094a82f37c49ebc4a9d_v3_2_3_0", json_data
        )

    def get_device_deployment_status_wired(
        self, deploy_activity_id, network_device_id, headers=None, **request_parameters
    ):
        """The API returns device deployment status based on filter criteria.  Released for gathering feedbacks from early
        adopters. API design is not final and future updates of this API may implement changes to any aspects of
        the API design.

        Args:
            network_device_id(str): networkDeviceId path parameter. Network device ID of the wired device to
                provision. The API /intent/api/v1/network-device can be used to get the network device
                ID.
            deploy_activity_id(str): deployActivityId path parameter.       Activity Id from the
                /intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/deploy or
                /intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurat
                ionModels/{previewActivityId}/deploy task response.
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
            https://developer.cisco.com/docs/dna-center/#!get-device-deployment-status-wired
        """
        check_type(headers, dict)
        check_type(network_device_id, str, may_be_none=False)
        check_type(deploy_activity_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
            "deployActivityId": deploy_activity_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wired/networkDevices/{networkDeviceId"
            + "}/configFeatures/intended/deviceDeployments"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_be5246ea895b5b958caa2c67d6e389_v3_2_3_0", json_data
        )
