# -*- coding: utf-8 -*-
"""Cisco Catalyst Center Fabric Wireless API wrapper.

Copyright (c) 2024 Cisco Systems.

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



from builtins import *



from ...restsession import RestSession
from ...utils import (
    apply_path_params,
    check_type,
    dict_from_items_with_values,
    dict_of_str,
)


class FabricWireless(object):
    """Cisco Catalyst Center Fabric Wireless API (version: 2.3.7.6.1).

    Wraps the Catalyst Center Fabric Wireless
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new FabricWireless
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Catalyst Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(FabricWireless, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def add_ssid_to_ip_pool_mapping_v1(self,
                                       scalableGroupName=None,
                                       siteNameHierarchy=None,
                                       ssidNames=None,
                                       vlanName=None,
                                       headers=None,
                                       payload=None,
                                       active_validation=True,
                                       **request_parameters):
        """Add SSID to IP Pool Mapping .

        Args:
            scalableGroupName(string): Fabric Wireless's Scalable Group Name .
            siteNameHierarchy(string): Fabric Wireless's Site Name Hierarchy .
            ssidNames(list): Fabric Wireless's List of SSIDs  (list of strings).
            vlanName(string): Fabric Wireless's VLAN Name .
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
            https://developer.cisco.com/docs/dna-center/#!add-s-s-i-d-to-i-p-pool-mapping-v1
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = {
            'vlanName':
                vlanName,
            'scalableGroupName':
                scalableGroupName,
            'ssidNames':
                ssidNames,
            'siteNameHierarchy':
                siteNameHierarchy,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_ad96e712f4525a128368b1bfe3afc21c_v2_3_7_6_1')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/business/sda/hostonboarding/ssid-'
                 + 'ippool')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_ad96e712f4525a128368b1bfe3afc21c_v2_3_7_6_1', json_data)

    def update_ssid_to_ip_pool_mapping_v1(self,
                                          scalableGroupName=None,
                                          siteNameHierarchy=None,
                                          ssidNames=None,
                                          vlanName=None,
                                          headers=None,
                                          payload=None,
                                          active_validation=True,
                                          **request_parameters):
        """Update SSID to IP Pool Mapping .

        Args:
            scalableGroupName(string): Fabric Wireless's Scalable Group Name .
            siteNameHierarchy(string): Fabric Wireless's Site Name Hierarchy .
            ssidNames(list): Fabric Wireless's List of SSIDs  (list of strings).
            vlanName(string): Fabric Wireless's VLAN Name .
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
            https://developer.cisco.com/docs/dna-center/#!update-s-s-i-d-to-i-p-pool-mapping-v1
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = {
            'vlanName':
                vlanName,
            'scalableGroupName':
                scalableGroupName,
            'ssidNames':
                ssidNames,
            'siteNameHierarchy':
                siteNameHierarchy,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_f90ae8599c8a21c98b7a1ca804_v2_3_7_6_1')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/business/sda/hostonboarding/ssid-'
                 + 'ippool')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_f90ae8599c8a21c98b7a1ca804_v2_3_7_6_1', json_data)

    def get_ssid_to_ip_pool_mapping_v1(self,
                                       site_name_hierarchy,
                                       vlan_name,
                                       headers=None,
                                       **request_parameters):
        """Get SSID to IP Pool Mapping .

        Args:
            vlan_name(str): vlanName query parameter. VLAN Name .
            site_name_hierarchy(str): siteNameHierarchy query parameter. Site Name Heirarchy .
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
            https://developer.cisco.com/docs/dna-center/#!get-s-s-i-d-to-i-p-pool-mapping-v1
        """
        check_type(headers, dict)
        check_type(vlan_name, str,
                   may_be_none=False)
        check_type(site_name_hierarchy, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'vlanName':
                vlan_name,
            'siteNameHierarchy':
                site_name_hierarchy,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/business/sda/hostonboarding/ssid-'
                 + 'ippool')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b0f6a0410705c75a61cdc51cc96c53f_v2_3_7_6_1', json_data)

    def remove_w_l_c_from_fabric_domain_v1(self,
                                           device_ipaddress,
                                           headers=None,
                                           **request_parameters):
        """Remove WLC from Fabric Domain .

        Args:
            device_ipaddress(str): deviceIPAddress query parameter. Device Management IP Address .
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
            https://developer.cisco.com/docs/dna-center/#!remove-w-l-c-from-fabric-domain-v1
        """
        check_type(headers, dict)
        check_type(device_ipaddress, str,
                   may_be_none=False)
        if headers is not None:
            if '__persistbapioutput' in headers:
                check_type(headers.get('__persistbapioutput'),
                           str)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'deviceIPAddress':
                device_ipaddress,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/business/sda/wireless-controller')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bb706025a9cb183ce7a60e0b5df_v2_3_7_6_1', json_data)

    def add_w_l_c_to_fabric_domain_v1(self,
                                      deviceName=None,
                                      siteNameHierarchy=None,
                                      headers=None,
                                      payload=None,
                                      active_validation=True,
                                      **request_parameters):
        """Add WLC to Fabric Domain .

        Args:
            deviceName(string): Fabric Wireless's WLC Device Name .
            siteNameHierarchy(string): Fabric Wireless's Fabric Site Name Hierarchy .
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
            https://developer.cisco.com/docs/dna-center/#!add-w-l-c-to-fabric-domain-v1
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = {
            'deviceName':
                deviceName,
            'siteNameHierarchy':
                siteNameHierarchy,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_c4befbd77a452a9b7873ffc360a1f20_v2_3_7_6_1')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/business/sda/wireless-controller')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_c4befbd77a452a9b7873ffc360a1f20_v2_3_7_6_1', json_data)

    def returns_all_the_fabric_sites_that_have_vlan_to_ssid_mapping_v1(self,
                                                                       limit=None,
                                                                       offset=None,
                                                                       headers=None,
                                                                       **request_parameters):
        """It will return all vlan to SSID mapping across all the fabric site .

        Args:
            limit(int): limit query parameter. Return only this many IP Pool to SSID Mapping .
            offset(int): offset query parameter. Number of records to skip for pagination .
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
            https://developer.cisco.com/docs/dna-center/#!returns-all-the-fabric-sites-that-have-v-l-a-n-to-s-s-i-d-mapping-v1
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'limit':
                limit,
            'offset':
                offset,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/sda/fabrics/vlanToSsids')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fea6e17769f5b3eb5ee1696254d2973_v2_3_7_6_1', json_data)

    def return_the_count_of_all_the_fabric_site_which_has_ssid_to_ip_pool_mapping_v1(self,
                                                                                     headers=None,
                                                                                     **request_parameters):
        """Return the count of all the fabric site which has SSID to IP Pool mapping  .

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
            https://developer.cisco.com/docs/dna-center/#!return-the-count-of-all-the-fabric-site-which-has-s-s-i-d-to-i-p-pool-mapping-v1
        """
        check_type(headers, dict)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/sda/fabrics/vlanToSsids/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_be3f285e21b59701a1af044b28_v2_3_7_6_1', json_data)

    def add_update_or_remove_ssid_mapping_to_a_vlan_v1(self,
                                                       fabric_id,
                                                       headers=None,
                                                       payload=None,
                                                       active_validation=True,
                                                       **request_parameters):
        """Add, update, or remove SSID mappings to a VLAN. If the payload doesn't contain a 'vlanName' which has SSIDs
        mapping done earlier then all the mapped SSIDs of the 'vlanName' is cleared. The request must include
        all SSIDs currently mapped to a VLAN, as determined by the response from the GET operation for the same
        fabricId used in the request. If an already-mapped SSID is not included in the payload, its mapping will
        be removed by this API. Conversely, if a new SSID is provided, it will be added to the Mapping. Ensure
        that any new SSID added is a Fabric SSID. This API can also be used to add a VLAN and associate the
        relevant SSIDs with it. The 'vlanName' must be 'Fabric Wireless Enabled' and should be part of the
        Fabric Site representing 'Fabric ID' specified in the API request. .

        Args:
            fabric_id(str): fabricId path parameter. The 'fabricId' represents the Fabric ID of a particular
                Fabric Site .
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
            https://developer.cisco.com/docs/dna-center/#!add-update-or-remove-s-s-i-d-mapping-to-a-v-l-a-n-v1
        """
        check_type(headers, dict)
        check_type(payload, list)
        check_type(fabric_id, str,
                   may_be_none=False)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'fabricId': fabric_id,
        }
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_a3d2432ae8c55fe793c5180d8d5fce25_v2_3_7_6_1')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/sda/fabrics/{fabricId}/vlanToSsids')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_a3d2432ae8c55fe793c5180d8d5fce25_v2_3_7_6_1', json_data)

    def retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site_v1(self,
                                                                                fabric_id,
                                                                                limit=None,
                                                                                offset=None,
                                                                                headers=None,
                                                                                **request_parameters):
        """Retrieve the VLANs and SSIDs mapped to the VLAN, within a Fabric Site. The 'fabricId' represents the Fabric ID
        of a particular Fabric Site. .

        Args:
            fabric_id(str): fabricId path parameter. The 'fabricId' represents the Fabric ID of a particular
                Fabric Site .
            limit(int): limit query parameter. The number of records to show for this page. .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-the-v-l-a-ns-and-s-s-i-ds-mapped-to-the-v-l-a-n-within-a-fabric-site-v1
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        check_type(fabric_id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'limit':
                limit,
            'offset':
                offset,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'fabricId': fabric_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/sda/fabrics/{fabricId}/vlanToSsids')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a18f012c54a5d34aef05d651f2dea18_v2_3_7_6_1', json_data)

    def returns_the_count_of_vlans_mapped_to_ssids_in_a_fabric_site_v1(self,
                                                                       fabric_id,
                                                                       headers=None,
                                                                       **request_parameters):
        """Returns the count of VLANs mapped to SSIDs in a Fabric Site. The 'fabricId' represents the Fabric ID of a
        particular Fabric Site. .

        Args:
            fabric_id(str): fabricId path parameter. The 'fabricId' represents the Fabric ID of a particular
                Fabric Site .
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
            https://developer.cisco.com/docs/dna-center/#!returns-the-count-of-v-l-a-ns-mapped-to-s-s-i-ds-in-a-fabric-site-v1
        """
        check_type(headers, dict)
        check_type(fabric_id, str,
                   may_be_none=False)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'fabricId': fabric_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/sda/fabrics/{fabricId}/vlanToSsids/co'
                 + 'unt')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ed14be6211da53ab832acf9b5aea599c_v2_3_7_6_1', json_data)

                
    
    # Alias Function
    def remove_w_l_c_from_fabric_domain(self,
                                           device_ipaddress,
                                           headers=None,
                                           **request_parameters):  
        return self.remove_w_l_c_from_fabric_domain_v1(
                    device_ipaddress=device_ipaddress,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def returns_all_the_fabric_sites_that_have_vlan_to_ssid_mapping(self,
                                                                       limit=None,
                                                                       offset=None,
                                                                       headers=None,
                                                                       **request_parameters):  
        return self.returns_all_the_fabric_sites_that_have_vlan_to_ssid_mapping_v1(
                    limit=limit,
                    offset=offset,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def add_w_l_c_to_fabric_domain(self,
                                      deviceName=None,
                                      siteNameHierarchy=None,
                                      headers=None,
                                      payload=None,
                                      active_validation=True,
                                      **request_parameters):  
        return self.add_w_l_c_to_fabric_domain_v1(
                    deviceName=deviceName,
                    siteNameHierarchy=siteNameHierarchy,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def add_ssid_to_ip_pool_mapping(self,
                                       scalableGroupName=None,
                                       siteNameHierarchy=None,
                                       ssidNames=None,
                                       vlanName=None,
                                       headers=None,
                                       payload=None,
                                       active_validation=True,
                                       **request_parameters):  
        return self.add_ssid_to_ip_pool_mapping_v1(
                    scalableGroupName=scalableGroupName,
                    siteNameHierarchy=siteNameHierarchy,
                    ssidNames=ssidNames,
                    vlanName=vlanName,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def update_ssid_to_ip_pool_mapping(self,
                                          scalableGroupName=None,
                                          siteNameHierarchy=None,
                                          ssidNames=None,
                                          vlanName=None,
                                          headers=None,
                                          payload=None,
                                          active_validation=True,
                                          **request_parameters):  
        return self.update_ssid_to_ip_pool_mapping_v1(
                    scalableGroupName=scalableGroupName,
                    siteNameHierarchy=siteNameHierarchy,
                    ssidNames=ssidNames,
                    vlanName=vlanName,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def add_update_or_remove_ssid_mapping_to_a_vlan(self,
                                                       fabric_id,
                                                       headers=None,
                                                       payload=None,
                                                       active_validation=True,
                                                       **request_parameters):  
        return self.add_update_or_remove_ssid_mapping_to_a_vlan_v1(
                    fabric_id=fabric_id,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def returns_the_count_of_vlans_mapped_to_ssids_in_a_fabric_site(self,
                                                                       fabric_id,
                                                                       headers=None,
                                                                       **request_parameters):  
        return self.returns_the_count_of_vlans_mapped_to_ssids_in_a_fabric_site_v1(
                    fabric_id=fabric_id,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def return_the_count_of_all_the_fabric_site_which_has_ssid_to_ip_pool_mapping(self,
                                                                                     headers=None,
                                                                                     **request_parameters):
        return self.return_the_count_of_all_the_fabric_site_which_has_ssid_to_ip_pool_mapping_v1(
                                                                                     headers=headers,
                                                                                     **request_parameters
        )  
                
    
    # Alias Function
    def get_ssid_to_ip_pool_mapping(self,
                                       site_name_hierarchy,
                                       vlan_name,
                                       headers=None,
                                       **request_parameters):  
        return self.get_ssid_to_ip_pool_mapping_v1(
                    site_name_hierarchy=site_name_hierarchy,
                    vlan_name=vlan_name,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site(self,
                                                                                fabric_id,
                                                                                limit=None,
                                                                                offset=None,
                                                                                headers=None,
                                                                                **request_parameters):  
        return self.retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site_v1(
                    fabric_id=fabric_id,
                    limit=limit,
                    offset=offset,
                    headers=headers,
                    **request_parameters
        )

