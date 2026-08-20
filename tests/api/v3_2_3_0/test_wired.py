"""CatalystCenterAPI wired API fixtures and tests.

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

import pytest
from fastjsonschema.exceptions import JsonSchemaException
from catalystcentersdk.exceptions import MalformedRequest
from tests.environment import CATALYST_CENTER_VERSION

pytestmark = pytest.mark.skipif(
    CATALYST_CENTER_VERSION != "3.2.3.0", reason="version does not match"
)


def is_valid_get_deployed_security_config_count(json_schema_validate, obj):
    json_schema_validate("jsd_beb58a142cab5335907622914f56fca4_v3_2_3_0").validate(obj)
    return True


def get_deployed_security_config_count(api):
    endpoint_result = api.wired.get_deployed_security_config_count(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_get_deployed_security_config_count(api, validator):
    try:
        assert is_valid_get_deployed_security_config_count(
            validator, get_deployed_security_config_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_deployed_security_config_count_default_val(api):
    endpoint_result = api.wired.get_deployed_security_config_count(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_get_deployed_security_config_count_default_val(api, validator):
    try:
        assert is_valid_get_deployed_security_config_count(
            validator, get_deployed_security_config_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_intended_security_configurations(json_schema_validate, obj):
    json_schema_validate("jsd_462ca61c56055259bd48e61f6bbeac29_v3_2_3_0").validate(obj)
    return True


def get_intended_security_configurations(api):
    endpoint_result = api.wired.get_intended_security_configurations(
        feature="string", id="string", limit=0, offset=0
    )
    return endpoint_result


@pytest.mark.wired
def test_get_intended_security_configurations(api, validator):
    try:
        assert is_valid_get_intended_security_configurations(
            validator, get_intended_security_configurations(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_intended_security_configurations_default_val(api):
    endpoint_result = api.wired.get_intended_security_configurations(
        feature="string", id="string", limit=None, offset=None
    )
    return endpoint_result


@pytest.mark.wired
def test_get_intended_security_configurations_default_val(api, validator):
    try:
        assert is_valid_get_intended_security_configurations(
            validator, get_intended_security_configurations_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_intended_security_configurations(json_schema_validate, obj):
    json_schema_validate("jsd_e43e520b26ad52b8b99dd1a9a97f2eff_v3_2_3_0").validate(obj)
    return True


def update_intended_security_configurations(api):
    endpoint_result = api.wired.update_intended_security_configurations(
        active_validation=True,
        arpInspectionConfig={"items": [{"configType": "string", "vlanId": 0}]},
        ctsConfig={
            "items": [
                {
                    "authorizationList": "string",
                    "configType": "string",
                    "roleBasedPermissions": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "sourceSgtRange": 0,
                                "destinationSgtRanges": {
                                    "configType": "string",
                                    "items": [
                                        {
                                            "configType": "string",
                                            "destinationSgt": 0,
                                            "ipv4RoleBasedAclName": "string",
                                            "ipv6RoleBasedAclName": "string",
                                        }
                                    ],
                                },
                            }
                        ],
                    },
                    "ctsSgt": 0,
                    "sxpIpV4Peers": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "minimumHoldTime": 0,
                                "ipV4Address": "string",
                                "maximumHoldTime": 0,
                                "mode": "string",
                                "localDeviceMode": "string",
                                "passwordType": "string",
                                "sourceIpv4Address": "string",
                            }
                        ],
                    },
                    "isRoleBasedEnforcementEnabled": True,
                    "enforcementVlans": "string",
                    "defaultSxpPassword": "string",
                    "ipSgtMappings": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "hostOrSubnetIpAddress": "string",
                                "sgt": 0,
                            }
                        ],
                    },
                    "ipVrfSgtMappings": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "ipAddress": "string",
                                "vrfName": "string",
                                "sgt": 0,
                            }
                        ],
                    },
                    "isSxpEnabled": True,
                }
            ]
        },
        deviceTrackingConfig={
            "items": [
                {
                    "fallbackSourceIpv4Address": "string",
                    "fallbackSourceIpv4Mask": "string",
                    "isFallbackSourceOverrideEnabled": True,
                    "configType": "string",
                    "deviceTrackingPolicy": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "policyName": "string",
                                "deviceRole": "string",
                                "isPrefixGleanEnabled": True,
                                "isTrustedPortEnabled": True,
                                "isDestinationGleanLogOnly": True,
                                "isProtocolArpEnabled": True,
                                "isProtocolDhcp4Enabled": True,
                                "isProtocolDhcp6Enabled": True,
                                "isProtocolNdpEnabled": True,
                                "isTrackingEnabled": True,
                                "addressCountLimit": 0,
                                "isSecurityLevelGleanEnabled": True,
                            }
                        ],
                    },
                    "isLoggingTheftEnabled": True,
                    "maxBindingEntries": 0,
                    "isTrackingEnabled": True,
                    "isAutoSourceEnabled": True,
                }
            ]
        },
        deviceTrackingVlanConfig={
            "items": [
                {
                    "configType": "string",
                    "deviceTrackingPolicy": "string",
                    "vlanId": "string",
                    "isDeviceTrackingEnabled": True,
                }
            ]
        },
        dhcpSnoopingConfig={
            "items": [
                {
                    "configType": "string",
                    "isSnoopingInfoOptionEnabled": True,
                    "writeDelay": 0,
                    "dhcpSnoopingVlans": {
                        "configType": "string",
                        "items": [{"configType": "string", "vlanId": 0}],
                    },
                    "isGleanEnabled": True,
                    "databaseTimeout": 0,
                    "databaseUrl": "string",
                    "isSnoopingOptionAllowUntrustedEnabled": True,
                    "isDhcpSnoopingEnabled": True,
                }
            ]
        },
        dot1xConfig={
            "items": [
                {
                    "configType": "string",
                    "isDot1xEnabled": True,
                    "isLoggingVerboseEnabled": True,
                    "dot1xCredentials": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "profileName": "string",
                                "password": "string",
                                "passwordType": "string",
                                "username": "string",
                            }
                        ],
                    },
                }
            ]
        },
        feature="string",
        id="string",
        ipV4ExtendedAccessListConfig={
            "items": [
                {
                    "configType": "string",
                    "aclName": "string",
                    "accessListSequenceRules": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "sourceIpV4Subnet": "string",
                                "isSourceAnyEnabled": True,
                                "destinationWildcard": "string",
                                "sourceIpV4Address": "string",
                                "isLoggingEnabled": True,
                                "destinationIpV4Subnet": "string",
                                "matchDscp": "string",
                                "sourceWildcard": "string",
                                "sequence": 0,
                                "protocol": "string",
                                "action": "string",
                                "isDestinationAnyEnabled": True,
                                "destinationIpV4Address": "string",
                                "sourceType": "string",
                                "sourceStartRange": "string",
                                "sourceEndRange": "string",
                                "destinationType": "string",
                                "destinationStartRange": "string",
                                "destinationEndRange": "string",
                                "sourceValue": "string",
                                "destinationValue": "string",
                            }
                        ],
                    },
                }
            ]
        },
        ipV4RoleBasedAccessListConfig={
            "items": [
                {
                    "configType": "string",
                    "aclName": "string",
                    "accessListSequenceRules": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "action": "string",
                                "protocol": "string",
                                "sequence": 0,
                                "isLoggingEnabled": True,
                            }
                        ],
                    },
                }
            ]
        },
        ipV4StandardAccessListConfig={
            "items": [
                {
                    "configType": "string",
                    "accessListSequenceRules": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "isDenyLogEnabled": True,
                                "isPermitLogEnabled": True,
                                "subnetWildcard": "string",
                                "sequence": 0,
                                "sourceWildcard": "string",
                                "isPermitAnyEnabled": True,
                                "sourceIpV4Address": "string",
                                "subnetIpV4Address": "string",
                                "isDenyAnyEnabled": True,
                                "subnetHostIpV4Address": "string",
                                "sourceHostIpV4Address": "string",
                            }
                        ],
                    },
                    "aclName": "string",
                }
            ]
        },
        ipV6AccessListConfig={
            "items": [
                {
                    "configType": "string",
                    "accessListSequenceRules": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "isEstablishedEnabled": True,
                                "matchDscp": "string",
                                "isLoggingEnabled": True,
                                "sequence": 0,
                                "destinationPrefix": "string",
                                "isDestinationAnyEnabled": True,
                                "protocol": "string",
                                "sourceIpV6Address": "string",
                                "action": "string",
                                "isSourceAnyEnabled": True,
                                "sourcePrefix": "string",
                                "destinationIpV6Address": "string",
                                "sourceType": "string",
                                "sourceStartRange": "string",
                                "sourceEndRange": "string",
                                "destinationType": "string",
                                "destinationStartRange": "string",
                                "destinationEndRange": "string",
                                "sourceValue": "string",
                                "destinationValue": "string",
                                "sourceNetworkAddress": "string",
                                "sourceNetworkWildcard": "string",
                                "destinationNetworkAddress": "string",
                                "destinationNetworkWildcard": "string",
                            }
                        ],
                    },
                    "aclName": "string",
                }
            ]
        },
        ipV6RoleBasedAccessListConfig={
            "items": [
                {
                    "configType": "string",
                    "accessListSequenceRules": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "action": "string",
                                "sequence": 0,
                                "isLogEnabled": True,
                                "protocolType": "string",
                                "protocolValue": "string",
                            }
                        ],
                    },
                    "aclName": "string",
                }
            ]
        },
        macExtendedAccessListConfig={
            "items": [
                {
                    "accessListExtendedEntries": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "values": "string",
                                "action": "string",
                            }
                        ],
                    },
                    "configType": "string",
                    "aclName": "string",
                }
            ]
        },
        payload=None,
    )
    return endpoint_result


@pytest.mark.wired
def test_update_intended_security_configurations(api, validator):
    try:
        assert is_valid_update_intended_security_configurations(
            validator, update_intended_security_configurations(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_intended_security_configurations_default_val(api):
    endpoint_result = api.wired.update_intended_security_configurations(
        active_validation=True,
        arpInspectionConfig=None,
        ctsConfig=None,
        deviceTrackingConfig=None,
        deviceTrackingVlanConfig=None,
        dhcpSnoopingConfig=None,
        dot1xConfig=None,
        feature="string",
        id="string",
        ipV4ExtendedAccessListConfig=None,
        ipV4RoleBasedAccessListConfig=None,
        ipV4StandardAccessListConfig=None,
        ipV6AccessListConfig=None,
        ipV6RoleBasedAccessListConfig=None,
        macExtendedAccessListConfig=None,
        payload=None,
    )
    return endpoint_result


@pytest.mark.wired
def test_update_intended_security_configurations_default_val(api, validator):
    try:
        assert is_valid_update_intended_security_configurations(
            validator, update_intended_security_configurations_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_intended_security_configurations(json_schema_validate, obj):
    json_schema_validate("jsd_fd1548d678db5fc89ff81116d3eb64de_v3_2_3_0").validate(obj)
    return True


def add_intended_security_configurations(api):
    endpoint_result = api.wired.add_intended_security_configurations(
        active_validation=True,
        arpInspectionConfig={"items": [{"configType": "string", "vlanId": 0}]},
        ctsConfig={
            "items": [
                {
                    "authorizationList": "string",
                    "configType": "string",
                    "roleBasedPermissions": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "sourceSgtRange": 0,
                                "destinationSgtRanges": {
                                    "configType": "string",
                                    "items": [
                                        {
                                            "configType": "string",
                                            "destinationSgt": 0,
                                            "ipv4RoleBasedAclName": "string",
                                            "ipv6RoleBasedAclName": "string",
                                        }
                                    ],
                                },
                            }
                        ],
                    },
                    "ctsSgt": 0,
                    "sxpIpV4Peers": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "minimumHoldTime": 0,
                                "ipV4Address": "string",
                                "maximumHoldTime": 0,
                                "mode": "string",
                                "localDeviceMode": "string",
                                "passwordType": "string",
                                "sourceIpv4Address": "string",
                            }
                        ],
                    },
                    "isRoleBasedEnforcementEnabled": True,
                    "enforcementVlans": "string",
                    "defaultSxpPassword": "string",
                    "ipSgtMappings": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "hostOrSubnetIpAddress": "string",
                                "sgt": 0,
                            }
                        ],
                    },
                    "ipVrfSgtMappings": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "ipAddress": "string",
                                "vrfName": "string",
                                "sgt": 0,
                            }
                        ],
                    },
                    "isSxpEnabled": True,
                }
            ]
        },
        deviceTrackingConfig={
            "items": [
                {
                    "fallbackSourceIpv4Address": "string",
                    "fallbackSourceIpv4Mask": "string",
                    "isFallbackSourceOverrideEnabled": True,
                    "configType": "string",
                    "deviceTrackingPolicy": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "policyName": "string",
                                "deviceRole": "string",
                                "isPrefixGleanEnabled": True,
                                "isTrustedPortEnabled": True,
                                "isDestinationGleanLogOnly": True,
                                "isProtocolArpEnabled": True,
                                "isProtocolDhcp4Enabled": True,
                                "isProtocolDhcp6Enabled": True,
                                "isProtocolNdpEnabled": True,
                                "isTrackingEnabled": True,
                                "addressCountLimit": 0,
                                "isSecurityLevelGleanEnabled": True,
                            }
                        ],
                    },
                    "isLoggingTheftEnabled": True,
                    "maxBindingEntries": 0,
                    "isTrackingEnabled": True,
                    "isAutoSourceEnabled": True,
                }
            ]
        },
        deviceTrackingVlanConfig={
            "items": [
                {
                    "configType": "string",
                    "deviceTrackingPolicy": "string",
                    "vlanId": "string",
                    "isDeviceTrackingEnabled": True,
                }
            ]
        },
        dhcpSnoopingConfig={
            "items": [
                {
                    "configType": "string",
                    "isSnoopingInfoOptionEnabled": True,
                    "writeDelay": 0,
                    "dhcpSnoopingVlans": {
                        "configType": "string",
                        "items": [{"configType": "string", "vlanId": 0}],
                    },
                    "isGleanEnabled": True,
                    "databaseTimeout": 0,
                    "databaseUrl": "string",
                    "isSnoopingOptionAllowUntrustedEnabled": True,
                    "isDhcpSnoopingEnabled": True,
                }
            ]
        },
        dot1xConfig={
            "items": [
                {
                    "configType": "string",
                    "isDot1xEnabled": True,
                    "isLoggingVerboseEnabled": True,
                    "dot1xCredentials": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "profileName": "string",
                                "password": "string",
                                "passwordType": "string",
                                "username": "string",
                            }
                        ],
                    },
                }
            ]
        },
        feature="string",
        id="string",
        ipV4ExtendedAccessListConfig={
            "items": [
                {
                    "configType": "string",
                    "aclName": "string",
                    "accessListSequenceRules": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "sourceIpV4Subnet": "string",
                                "isSourceAnyEnabled": True,
                                "destinationWildcard": "string",
                                "sourceIpV4Address": "string",
                                "isLoggingEnabled": True,
                                "destinationIpV4Subnet": "string",
                                "matchDscp": "string",
                                "sourceWildcard": "string",
                                "sequence": 0,
                                "protocol": "string",
                                "action": "string",
                                "isDestinationAnyEnabled": True,
                                "destinationIpV4Address": "string",
                                "sourceType": "string",
                                "sourceStartRange": "string",
                                "sourceEndRange": "string",
                                "destinationType": "string",
                                "destinationStartRange": "string",
                                "destinationEndRange": "string",
                                "sourceValue": "string",
                                "destinationValue": "string",
                            }
                        ],
                    },
                }
            ]
        },
        ipV4RoleBasedAccessListConfig={
            "items": [
                {
                    "configType": "string",
                    "aclName": "string",
                    "accessListSequenceRules": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "action": "string",
                                "protocol": "string",
                                "sequence": 0,
                                "isLoggingEnabled": True,
                            }
                        ],
                    },
                }
            ]
        },
        ipV4StandardAccessListConfig={
            "items": [
                {
                    "configType": "string",
                    "accessListSequenceRules": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "isDenyLogEnabled": True,
                                "isPermitLogEnabled": True,
                                "subnetWildcard": "string",
                                "sequence": 0,
                                "sourceWildcard": "string",
                                "isPermitAnyEnabled": True,
                                "sourceIpV4Address": "string",
                                "subnetIpV4Address": "string",
                                "isDenyAnyEnabled": True,
                                "subnetHostIpV4Address": "string",
                                "sourceHostIpV4Address": "string",
                            }
                        ],
                    },
                    "aclName": "string",
                }
            ]
        },
        ipV6AccessListConfig={
            "items": [
                {
                    "configType": "string",
                    "accessListSequenceRules": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "isEstablishedEnabled": True,
                                "matchDscp": "string",
                                "isLoggingEnabled": True,
                                "sequence": 0,
                                "destinationPrefix": "string",
                                "isDestinationAnyEnabled": True,
                                "protocol": "string",
                                "sourceIpV6Address": "string",
                                "action": "string",
                                "isSourceAnyEnabled": True,
                                "sourcePrefix": "string",
                                "destinationIpV6Address": "string",
                                "sourceType": "string",
                                "sourceStartRange": "string",
                                "sourceEndRange": "string",
                                "destinationType": "string",
                                "destinationStartRange": "string",
                                "destinationEndRange": "string",
                                "sourceValue": "string",
                                "destinationValue": "string",
                                "sourceNetworkAddress": "string",
                                "sourceNetworkWildcard": "string",
                                "destinationNetworkAddress": "string",
                                "destinationNetworkWildcard": "string",
                            }
                        ],
                    },
                    "aclName": "string",
                }
            ]
        },
        ipV6RoleBasedAccessListConfig={
            "items": [
                {
                    "configType": "string",
                    "accessListSequenceRules": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "action": "string",
                                "sequence": 0,
                                "isLogEnabled": True,
                                "protocolType": "string",
                                "protocolValue": "string",
                            }
                        ],
                    },
                    "aclName": "string",
                }
            ]
        },
        macExtendedAccessListConfig={
            "items": [
                {
                    "accessListExtendedEntries": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "values": "string",
                                "action": "string",
                            }
                        ],
                    },
                    "configType": "string",
                    "aclName": "string",
                }
            ]
        },
        payload=None,
    )
    return endpoint_result


@pytest.mark.wired
def test_add_intended_security_configurations(api, validator):
    try:
        assert is_valid_add_intended_security_configurations(
            validator, add_intended_security_configurations(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_intended_security_configurations_default_val(api):
    endpoint_result = api.wired.add_intended_security_configurations(
        active_validation=True,
        arpInspectionConfig=None,
        ctsConfig=None,
        deviceTrackingConfig=None,
        deviceTrackingVlanConfig=None,
        dhcpSnoopingConfig=None,
        dot1xConfig=None,
        feature="string",
        id="string",
        ipV4ExtendedAccessListConfig=None,
        ipV4RoleBasedAccessListConfig=None,
        ipV4StandardAccessListConfig=None,
        ipV6AccessListConfig=None,
        ipV6RoleBasedAccessListConfig=None,
        macExtendedAccessListConfig=None,
        payload=None,
    )
    return endpoint_result


@pytest.mark.wired
def test_add_intended_security_configurations_default_val(api, validator):
    try:
        assert is_valid_add_intended_security_configurations(
            validator, add_intended_security_configurations_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_intended_security_configurations(json_schema_validate, obj):
    json_schema_validate("jsd_d75e159daf8153d8943ddc640fd2b1eb_v3_2_3_0").validate(obj)
    return True


def delete_intended_security_configurations(api):
    endpoint_result = api.wired.delete_intended_security_configurations(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_delete_intended_security_configurations(api, validator):
    try:
        assert is_valid_delete_intended_security_configurations(
            validator, delete_intended_security_configurations(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_intended_security_configurations_default_val(api):
    endpoint_result = api.wired.delete_intended_security_configurations(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_delete_intended_security_configurations_default_val(api, validator):
    try:
        assert is_valid_delete_intended_security_configurations(
            validator, delete_intended_security_configurations_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_deployed_security_configurations(json_schema_validate, obj):
    json_schema_validate("jsd_2ed4975052bc522dba1deb2622d9f32f_v3_2_3_0").validate(obj)
    return True


def get_deployed_security_configurations(api):
    endpoint_result = api.wired.get_deployed_security_configurations(
        feature="string", id="string", limit=0, offset=0
    )
    return endpoint_result


@pytest.mark.wired
def test_get_deployed_security_configurations(api, validator):
    try:
        assert is_valid_get_deployed_security_configurations(
            validator, get_deployed_security_configurations(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_deployed_security_configurations_default_val(api):
    endpoint_result = api.wired.get_deployed_security_configurations(
        feature="string", id="string", limit=None, offset=None
    )
    return endpoint_result


@pytest.mark.wired
def test_get_deployed_security_configurations_default_val(api, validator):
    try:
        assert is_valid_get_deployed_security_configurations(
            validator, get_deployed_security_configurations_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_intended_layer2_configurations(json_schema_validate, obj):
    json_schema_validate("jsd_2302d1d6fcb35d1dab928a35dac6dbb1_v3_2_3_0").validate(obj)
    return True


def get_intended_layer2_configurations(api):
    endpoint_result = api.wired.get_intended_layer2_configurations(
        feature="string", id="string", limit=0, offset=0
    )
    return endpoint_result


@pytest.mark.wired
def test_get_intended_layer2_configurations(api, validator):
    try:
        assert is_valid_get_intended_layer2_configurations(
            validator, get_intended_layer2_configurations(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_intended_layer2_configurations_default_val(api):
    endpoint_result = api.wired.get_intended_layer2_configurations(
        feature="string", id="string", limit=None, offset=None
    )
    return endpoint_result


@pytest.mark.wired
def test_get_intended_layer2_configurations_default_val(api, validator):
    try:
        assert is_valid_get_intended_layer2_configurations(
            validator, get_intended_layer2_configurations_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_intended_layer2_configurations(json_schema_validate, obj):
    json_schema_validate("jsd_5d58ffeab64f5677a135fd95bf37c554_v3_2_3_0").validate(obj)
    return True


def delete_intended_layer2_configurations(api):
    endpoint_result = api.wired.delete_intended_layer2_configurations(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_delete_intended_layer2_configurations(api, validator):
    try:
        assert is_valid_delete_intended_layer2_configurations(
            validator, delete_intended_layer2_configurations(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_intended_layer2_configurations_default_val(api):
    endpoint_result = api.wired.delete_intended_layer2_configurations(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_delete_intended_layer2_configurations_default_val(api, validator):
    try:
        assert is_valid_delete_intended_layer2_configurations(
            validator, delete_intended_layer2_configurations_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_intended_layer2_configurations(json_schema_validate, obj):
    json_schema_validate("jsd_c576d6792fd3532cb34cb6e1e2abb125_v3_2_3_0").validate(obj)
    return True


def update_intended_layer2_configurations(api):
    endpoint_result = api.wired.update_intended_layer2_configurations(
        active_validation=True,
        cdpConfig={
            "items": [
                {
                    "holdtime": 0,
                    "isCdpEnabled": True,
                    "timer": 0,
                    "configType": "string",
                    "isAdvertiseV2Enabled": True,
                }
            ]
        },
        etherchannelConfig={
            "items": [
                {
                    "configType": "string",
                    "isAutoEnabled": True,
                    "loadBalancingMethod": "string",
                    "lacpSystemPriority": 0,
                }
            ]
        },
        feature="string",
        id="string",
        igmpSnoopingConfig={
            "items": [
                {
                    "configType": "string",
                    "igmpSnoopingQuerierEntry": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "querierAddress": "string",
                                "querierVersion": 0,
                                "queryInterval": 0,
                            }
                        ],
                    },
                    "igmpSnoopingVlans": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "isImmediateLeaveEnabled": True,
                                "isQuerierEnabled": True,
                                "mrouterInterface": "string",
                                "querierAddress": "string",
                                "querierVersion": 0,
                                "queryInterval": 0,
                                "vlanId": 0,
                            }
                        ],
                    },
                    "lastMemberQueryInterval": 0,
                    "isQuerierEnabled": True,
                    "isIgmpSnoopingEnabled": True,
                }
            ]
        },
        lldpConfig={
            "items": [
                {
                    "configType": "string",
                    "holdtime": 0,
                    "reinitializationDelay": 0,
                    "isLldpEnabled": True,
                    "timer": 0,
                }
            ]
        },
        macAddressTableConfig={
            "items": [
                {
                    "configType": "string",
                    "agingTime": 0,
                    "notificationChangeHistorySize": 0,
                    "notificationChangeInterval": 0,
                    "isChangeNotificationEnabled": True,
                    "isMacMoveEnabled": True,
                    "isNotificationThresholdEnabled": True,
                    "notificationThresholdInterval": 0,
                    "notificationThresholdLimit": 0,
                    "macAddressTableStatic": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "destinationInterface": "string",
                                "isDropEnabled": True,
                                "macAddress": "string",
                                "vlanId": 0,
                            }
                        ],
                    },
                    "macAddressTableVlanAgingTime": {
                        "configType": "string",
                        "items": [
                            {"configType": "string", "agingTime": 0, "vlanId": 0}
                        ],
                    },
                }
            ]
        },
        mldSnoopingConfig={
            "items": [
                {
                    "configType": "string",
                    "isQuerierEnabled": True,
                    "isListenerMessageSuppressionEnabled": True,
                    "mldSnoopingQuerierEntry": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "querierAddress": "string",
                                "querierVersion": 0,
                                "queryInterval": 0,
                            }
                        ],
                    },
                    "mldSnoopingVlans": {
                        "configType": "string",
                        "items": [
                            {
                                "mrouterInterface": "string",
                                "isImmediateLeaveEnabled": True,
                                "querierAddress": "string",
                                "queryInterval": 0,
                                "isQuerierEnabled": True,
                                "querierVersion": 0,
                                "vlanId": 0,
                                "configType": "string",
                            }
                        ],
                    },
                    "lastListenerQueryInterval": 0,
                    "isMldSnoopingEnabled": True,
                }
            ]
        },
        payload=None,
        stpConfig={
            "items": [
                {
                    "configType": "string",
                    "isEtherChannelGuardEnabled": True,
                    "isBpduFilterEnabled": True,
                    "isBpduGuardEnabled": True,
                    "portFastMode": "string",
                    "isBackboneFastEnabled": True,
                    "isLoggingEnabled": True,
                    "isLoopGuardEnabled": True,
                    "isExtendedSystemIdEnabled": True,
                    "isUplinkFastEnabled": True,
                    "vlanConfig": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "forwardDelay": 0,
                                "helloInterval": 0,
                                "vlan": 0,
                                "maxAge": 0,
                                "priority": 0,
                            }
                        ],
                    },
                    "stpMode": "string",
                    "transmitHoldCount": 0,
                    "uplinkFastMaxUpdateRate": 0,
                }
            ]
        },
        udldConfig={
            "items": [
                {
                    "configType": "string",
                    "isAggressiveEnabled": True,
                    "isUdldEnabled": True,
                    "messageTime": 0,
                    "isRecoveryEnabled": True,
                    "recoveryInterval": 0,
                }
            ]
        },
        vlanConfig={
            "items": [
                {
                    "configType": "string",
                    "vlanId": 0,
                    "name": "string",
                    "state": "string",
                    "isRemoteSpanEnabled": True,
                }
            ]
        },
        vtpConfig={
            "items": [
                {
                    "configType": "string",
                    "isPruningEnabled": True,
                    "isServerPrimary": True,
                    "mode": "string",
                    "domainName": "string",
                    "configurationFileName": "string",
                    "interfaceName": "string",
                    "version": 0,
                }
            ]
        },
    )
    return endpoint_result


@pytest.mark.wired
def test_update_intended_layer2_configurations(api, validator):
    try:
        assert is_valid_update_intended_layer2_configurations(
            validator, update_intended_layer2_configurations(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_intended_layer2_configurations_default_val(api):
    endpoint_result = api.wired.update_intended_layer2_configurations(
        active_validation=True,
        cdpConfig=None,
        etherchannelConfig=None,
        feature="string",
        id="string",
        igmpSnoopingConfig=None,
        lldpConfig=None,
        macAddressTableConfig=None,
        mldSnoopingConfig=None,
        payload=None,
        stpConfig=None,
        udldConfig=None,
        vlanConfig=None,
        vtpConfig=None,
    )
    return endpoint_result


@pytest.mark.wired
def test_update_intended_layer2_configurations_default_val(api, validator):
    try:
        assert is_valid_update_intended_layer2_configurations(
            validator, update_intended_layer2_configurations_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_intended_layer2_configurations(json_schema_validate, obj):
    json_schema_validate("jsd_538416a251b25925b0c317ae1bf2bacd_v3_2_3_0").validate(obj)
    return True


def add_intended_layer2_configurations(api):
    endpoint_result = api.wired.add_intended_layer2_configurations(
        active_validation=True,
        cdpConfig={
            "items": [
                {
                    "holdtime": 0,
                    "isCdpEnabled": True,
                    "timer": 0,
                    "configType": "string",
                    "isAdvertiseV2Enabled": True,
                }
            ]
        },
        etherchannelConfig={
            "items": [
                {
                    "configType": "string",
                    "isAutoEnabled": True,
                    "loadBalancingMethod": "string",
                    "lacpSystemPriority": 0,
                }
            ]
        },
        feature="string",
        id="string",
        igmpSnoopingConfig={
            "items": [
                {
                    "configType": "string",
                    "igmpSnoopingQuerierEntry": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "querierAddress": "string",
                                "querierVersion": 0,
                                "queryInterval": 0,
                            }
                        ],
                    },
                    "igmpSnoopingVlans": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "isImmediateLeaveEnabled": True,
                                "isQuerierEnabled": True,
                                "mrouterInterface": "string",
                                "querierAddress": "string",
                                "querierVersion": 0,
                                "queryInterval": 0,
                                "vlanId": 0,
                            }
                        ],
                    },
                    "lastMemberQueryInterval": 0,
                    "isQuerierEnabled": True,
                    "isIgmpSnoopingEnabled": True,
                }
            ]
        },
        lldpConfig={
            "items": [
                {
                    "configType": "string",
                    "holdtime": 0,
                    "reinitializationDelay": 0,
                    "isLldpEnabled": True,
                    "timer": 0,
                }
            ]
        },
        macAddressTableConfig={
            "items": [
                {
                    "configType": "string",
                    "agingTime": 0,
                    "notificationChangeHistorySize": 0,
                    "notificationChangeInterval": 0,
                    "isChangeNotificationEnabled": True,
                    "isMacMoveEnabled": True,
                    "isNotificationThresholdEnabled": True,
                    "notificationThresholdInterval": 0,
                    "notificationThresholdLimit": 0,
                    "macAddressTableStatic": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "destinationInterface": "string",
                                "isDropEnabled": True,
                                "macAddress": "string",
                                "vlanId": 0,
                            }
                        ],
                    },
                    "macAddressTableVlanAgingTime": {
                        "configType": "string",
                        "items": [
                            {"configType": "string", "agingTime": 0, "vlanId": 0}
                        ],
                    },
                }
            ]
        },
        mldSnoopingConfig={
            "items": [
                {
                    "configType": "string",
                    "isQuerierEnabled": True,
                    "isListenerMessageSuppressionEnabled": True,
                    "mldSnoopingQuerierEntry": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "querierAddress": "string",
                                "querierVersion": 0,
                                "queryInterval": 0,
                            }
                        ],
                    },
                    "mldSnoopingVlans": {
                        "configType": "string",
                        "items": [
                            {
                                "mrouterInterface": "string",
                                "isImmediateLeaveEnabled": True,
                                "querierAddress": "string",
                                "queryInterval": 0,
                                "isQuerierEnabled": True,
                                "querierVersion": 0,
                                "vlanId": 0,
                                "configType": "string",
                            }
                        ],
                    },
                    "lastListenerQueryInterval": 0,
                    "isMldSnoopingEnabled": True,
                }
            ]
        },
        payload=None,
        stpConfig={
            "items": [
                {
                    "configType": "string",
                    "isEtherChannelGuardEnabled": True,
                    "isBpduFilterEnabled": True,
                    "isBpduGuardEnabled": True,
                    "portFastMode": "string",
                    "isBackboneFastEnabled": True,
                    "isLoggingEnabled": True,
                    "isLoopGuardEnabled": True,
                    "isExtendedSystemIdEnabled": True,
                    "isUplinkFastEnabled": True,
                    "vlanConfig": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "forwardDelay": 0,
                                "helloInterval": 0,
                                "vlan": 0,
                                "maxAge": 0,
                                "priority": 0,
                            }
                        ],
                    },
                    "stpMode": "string",
                    "transmitHoldCount": 0,
                    "uplinkFastMaxUpdateRate": 0,
                }
            ]
        },
        udldConfig={
            "items": [
                {
                    "configType": "string",
                    "isAggressiveEnabled": True,
                    "isUdldEnabled": True,
                    "messageTime": 0,
                    "isRecoveryEnabled": True,
                    "recoveryInterval": 0,
                }
            ]
        },
        vlanConfig={
            "items": [
                {
                    "configType": "string",
                    "vlanId": 0,
                    "name": "string",
                    "state": "string",
                    "isRemoteSpanEnabled": True,
                }
            ]
        },
        vtpConfig={
            "items": [
                {
                    "configType": "string",
                    "isPruningEnabled": True,
                    "isServerPrimary": True,
                    "mode": "string",
                    "domainName": "string",
                    "configurationFileName": "string",
                    "interfaceName": "string",
                    "version": 0,
                }
            ]
        },
    )
    return endpoint_result


@pytest.mark.wired
def test_add_intended_layer2_configurations(api, validator):
    try:
        assert is_valid_add_intended_layer2_configurations(
            validator, add_intended_layer2_configurations(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_intended_layer2_configurations_default_val(api):
    endpoint_result = api.wired.add_intended_layer2_configurations(
        active_validation=True,
        cdpConfig=None,
        etherchannelConfig=None,
        feature="string",
        id="string",
        igmpSnoopingConfig=None,
        lldpConfig=None,
        macAddressTableConfig=None,
        mldSnoopingConfig=None,
        payload=None,
        stpConfig=None,
        udldConfig=None,
        vlanConfig=None,
        vtpConfig=None,
    )
    return endpoint_result


@pytest.mark.wired
def test_add_intended_layer2_configurations_default_val(api, validator):
    try:
        assert is_valid_add_intended_layer2_configurations(
            validator, add_intended_layer2_configurations_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_deployment_status_connectivity(json_schema_validate, obj):
    json_schema_validate("jsd_f0b54311312e5a699a0828417088c9a4_v3_2_3_0").validate(obj)
    return True


def get_device_deployment_status_connectivity(api):
    endpoint_result = api.wired.get_device_deployment_status_connectivity(
        deploy_activity_id="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_get_device_deployment_status_connectivity(api, validator):
    try:
        assert is_valid_get_device_deployment_status_connectivity(
            validator, get_device_deployment_status_connectivity(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_deployment_status_connectivity_default_val(api):
    endpoint_result = api.wired.get_device_deployment_status_connectivity(
        deploy_activity_id=None, id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_get_device_deployment_status_connectivity_default_val(api, validator):
    try:
        assert is_valid_get_device_deployment_status_connectivity(
            validator, get_device_deployment_status_connectivity_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_intended_port_configurations(json_schema_validate, obj):
    json_schema_validate("jsd_c502bd27faaa506ea2ab28177996f094_v3_2_3_0").validate(obj)
    return True


def update_intended_port_configurations(api):
    endpoint_result = api.wired.update_intended_port_configurations(
        active_validation=True,
        ethernetInterfaceConfig={
            "items": [
                {
                    "interfaceName": "string",
                    "accessSessionControlDirection": "string",
                    "accessSessionHostModeEnum": "string",
                    "accessSessionPortControl": "string",
                    "authControlDirection": "string",
                    "authHostMode": "string",
                    "accessSessionHostModeCfg": "string",
                    "authInactivityTimer": 0,
                    "authPortControl": "string",
                    "bfdTemplate": "string",
                    "channelGroupMode": "string",
                    "channelGroupNumber": 0,
                    "configType": "string",
                    "deviceTrackingPolicy": {
                        "configType": "string",
                        "items": [
                            {"configType": "string", "deviceTrackingPolicy": "string"}
                        ],
                    },
                    "isDeviceTrackingEnabled": True,
                    "channelProtocol": "string",
                    "clientPdPreName": "string",
                    "ipDhcpHostname": "string",
                    "ipV4InboundAclName": "string",
                    "ipV4OutboundAclName": "string",
                    "primaryIpAddress": "string",
                    "primaryIpMask": "string",
                    "isIpV6Enabled": True,
                    "ipV6DhcpRelayDestinationGlobal": {
                        "configType": "string",
                        "items": [{"configType": "string", "ipV6Address": "string"}],
                    },
                    "lacpPortPriority": 0,
                    "lacpRate": "string",
                    "mode": "string",
                    "description": "string",
                    "isShutdown": True,
                    "stpCost": 0,
                    "stpPortPriority": 0,
                    "stpBpdufilterStatus": "string",
                    "trunkAllowedVlansMode": "string",
                    "trunkAllowedVlanIds": "string",
                    "nativeVlanId": 0,
                    "udldMode": "string",
                    "stpGuardMode": "string",
                    "voiceVlanId": 0,
                    "ipV6DhcpRelayDestination": {
                        "configType": "string",
                        "items": [{"configType": "string", "ipV6Address": "string"}],
                    },
                    "helperAddresses": {
                        "configType": "string",
                        "items": [{"configType": "string", "ipAddress": "string"}],
                    },
                    "secondaryAddress": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "ipAddress": "string",
                                "mask": "string",
                            }
                        ],
                    },
                    "ipV6LinkLocalAddress": "string",
                    "dhcpSnoopingLimitRate": 0,
                    "ipV4VrfName": "string",
                    "vrfName": "string",
                    "portSecurityAgingType": "string",
                    "bfdMinTxInterval": 0,
                    "bfdIntervalMultiplier": 0,
                    "isAccessSessionClosed": True,
                    "isAuthInactivityTimerFromServerEnabled": True,
                    "isAuthOpenEnabled": True,
                    "isBfdEnabled": True,
                    "isDot1xMabOrderEnabled": True,
                    "isDot1xMabPriorityEnabled": True,
                    "isCdpEnabled": True,
                    "isCdpTlvAppEnabled": True,
                    "isIpV6AutoconfigEnabled": True,
                    "lldpAdminStatus": "string",
                    "stpBpduGuard": "string",
                    "stpPortfastMode": "string",
                    "isSwitchportNonegotiate": True,
                    "portSecurityViolation": "string",
                    "isStormControlShutdownEnabled": True,
                    "isStormControlTrapEnabled": True,
                    "isArpInspectionTrustEnabled": True,
                    "isDhcpSnoopingTrustEnabled": True,
                    "isPortSecurityEnabled": True,
                    "portSecurityAgingTime": 0,
                    "ipV6PrefixList": {
                        "configType": "string",
                        "items": [{"configType": "string", "ipV6Address": "string"}],
                    },
                    "ipV6TrafficFilter": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "accessList": "string",
                                "direction": "string",
                            }
                        ],
                    },
                    "isMabEapEnabled": True,
                    "isMabEnabled": True,
                    "isMabWebauthPriority": True,
                    "isPeriodicAuthEnabled": True,
                    "isReauthTimerFromServerEnabled": True,
                    "bfdMinRxInterval": 0,
                    "reauthTimer": 0,
                    "staticSgt": 0,
                    "isStaticTrustedEnabled": True,
                    "accessVlanId": 0,
                    "accessList": "string",
                    "direction": "string",
                    "isSwitchportEnabled": True,
                    "trunkVlans": "string",
                    "txPeriod": 0,
                    "isBfdIntervalEnabled": {},
                    "isDhcpEnabled": True,
                    "isIpV6DhcpEnabled": True,
                }
            ]
        },
        feature="string",
        id="string",
        payload=None,
        portChannelInterfaceConfig={
            "items": [
                {
                    "portchannelNumber": 0,
                    "macAddress": "string",
                    "ipV4VrfName": "string",
                    "ipV4InboundAclName": "string",
                    "ipV4OutboundAclName": "string",
                    "stpPortPriority": 0,
                    "bfdTemplate": "string",
                    "configType": "string",
                    "description": "string",
                    "secondaryAddress": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "ipAddress": "string",
                                "mask": "string",
                            }
                        ],
                    },
                    "helperAddress": {
                        "configType": "string",
                        "items": [{"ipAddress": "string", "configType": "string"}],
                    },
                    "vrfName": "string",
                    "bfdMinTxInterval": 0,
                    "bfdIntervalMultiplier": 0,
                    "primaryAddress": "string",
                    "isBfdEnabled": True,
                    "isIpV6Enabled": True,
                    "isIpV6RedirectsEnabled": True,
                    "isIpV4DhcpEnabled": True,
                    "isIpV6DhcpEnabled": True,
                    "isIpV6AutoconfigEnabled": True,
                    "isIpv6RedirectsEnabled": True,
                    "isLacpFastSwitchoverEnabled": True,
                    "isShutdown": True,
                    "stpBpdufilterStatus": "string",
                    "trunkAllowedVlansMode": "string",
                    "trunkAllowedVlanIds": "string",
                    "isSwitchportNonegotiate": True,
                    "isProxyArpEnabled": True,
                    "isRapidCommitEnabled": True,
                    "isIpV4RedirectsEnabled": True,
                    "stpBpduGuard": "string",
                    "isSwitchportEnabled": True,
                    "mode": "string",
                    "isIpV4UnreachablesEnabled": True,
                    "accessVlanId": 0,
                    "minLinks": 0,
                    "bfdMinRxInterval": 0,
                    "ipV6DhcpRelayDestinationGlobal": {
                        "configType": "string",
                        "items": [{"configType": "string", "ipV6Address": "string"}],
                    },
                    "ipV4Mask": "string",
                    "ipV6TrafficFilter": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "actionList": "string",
                                "direction": "string",
                            }
                        ],
                    },
                    "lacpMaxBundle": 0,
                    "stpGuardMode": "string",
                    "stpPortfastMode": "string",
                    "ipV6PrefixList": {
                        "configType": "string",
                        "items": [{"configType": "string", "ipV6Prefix": "string"}],
                    },
                    "ipV6DhcpRelayDestination": {
                        "configType": "string",
                        "items": [{"configType": "string", "ipV6Address": "string"}],
                    },
                    "ipV6LinkLocalAddress": "string",
                    "stpCost": 0,
                    "nativeVlanId": 0,
                    "voiceVlanId": 0,
                    "isBfdIntervalEnabled": True,
                }
            ]
        },
    )
    return endpoint_result


@pytest.mark.wired
def test_update_intended_port_configurations(api, validator):
    try:
        assert is_valid_update_intended_port_configurations(
            validator, update_intended_port_configurations(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_intended_port_configurations_default_val(api):
    endpoint_result = api.wired.update_intended_port_configurations(
        active_validation=True,
        ethernetInterfaceConfig=None,
        feature="string",
        id="string",
        payload=None,
        portChannelInterfaceConfig=None,
    )
    return endpoint_result


@pytest.mark.wired
def test_update_intended_port_configurations_default_val(api, validator):
    try:
        assert is_valid_update_intended_port_configurations(
            validator, update_intended_port_configurations_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_intended_port_configurations(json_schema_validate, obj):
    json_schema_validate("jsd_54728ccaa0b85d619300dca40cf09973_v3_2_3_0").validate(obj)
    return True


def delete_intended_port_configurations(api):
    endpoint_result = api.wired.delete_intended_port_configurations(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_delete_intended_port_configurations(api, validator):
    try:
        assert is_valid_delete_intended_port_configurations(
            validator, delete_intended_port_configurations(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_intended_port_configurations_default_val(api):
    endpoint_result = api.wired.delete_intended_port_configurations(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_delete_intended_port_configurations_default_val(api, validator):
    try:
        assert is_valid_delete_intended_port_configurations(
            validator, delete_intended_port_configurations_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_intended_port_configurations(json_schema_validate, obj):
    json_schema_validate("jsd_bac13e35d2b556488b0485ea174e11d2_v3_2_3_0").validate(obj)
    return True


def add_intended_port_configurations(api):
    endpoint_result = api.wired.add_intended_port_configurations(
        active_validation=True,
        ethernetInterfaceConfig={
            "items": [
                {
                    "interfaceName": "string",
                    "accessSessionControlDirection": "string",
                    "accessSessionHostModeEnum": "string",
                    "accessSessionPortControl": "string",
                    "authControlDirection": "string",
                    "authHostMode": "string",
                    "accessSessionHostModeCfg": "string",
                    "authInactivityTimer": 0,
                    "authPortControl": "string",
                    "bfdTemplate": "string",
                    "channelGroupMode": "string",
                    "channelGroupNumber": 0,
                    "configType": "string",
                    "deviceTrackingPolicy": {
                        "configType": "string",
                        "items": [
                            {"configType": "string", "deviceTrackingPolicy": "string"}
                        ],
                    },
                    "isDeviceTrackingEnabled": True,
                    "channelProtocol": "string",
                    "clientPdPreName": "string",
                    "ipDhcpHostname": "string",
                    "ipV4InboundAclName": "string",
                    "ipV4OutboundAclName": "string",
                    "primaryIpAddress": "string",
                    "primaryIpMask": "string",
                    "isIpV6Enabled": True,
                    "ipV6DhcpRelayDestinationGlobal": {
                        "configType": "string",
                        "items": [{"configType": "string", "ipV6Address": "string"}],
                    },
                    "lacpPortPriority": 0,
                    "lacpRate": "string",
                    "mode": "string",
                    "description": "string",
                    "isShutdown": True,
                    "stpCost": 0,
                    "stpPortPriority": 0,
                    "stpBpdufilterStatus": "string",
                    "trunkAllowedVlansMode": "string",
                    "trunkAllowedVlanIds": "string",
                    "nativeVlanId": 0,
                    "udldMode": "string",
                    "stpGuardMode": "string",
                    "voiceVlanId": 0,
                    "ipV6DhcpRelayDestination": {
                        "configType": "string",
                        "items": [{"configType": "string", "ipV6Address": "string"}],
                    },
                    "helperAddresses": {
                        "configType": "string",
                        "items": [{"configType": "string", "ipAddress": "string"}],
                    },
                    "secondaryAddress": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "ipAddress": "string",
                                "mask": "string",
                            }
                        ],
                    },
                    "ipV6LinkLocalAddress": "string",
                    "dhcpSnoopingLimitRate": 0,
                    "ipV4VrfName": "string",
                    "vrfName": "string",
                    "portSecurityAgingType": "string",
                    "bfdMinTxInterval": 0,
                    "bfdIntervalMultiplier": 0,
                    "isAccessSessionClosed": True,
                    "isAuthInactivityTimerFromServerEnabled": True,
                    "isAuthOpenEnabled": True,
                    "isBfdEnabled": True,
                    "isDot1xMabOrderEnabled": True,
                    "isDot1xMabPriorityEnabled": True,
                    "isCdpEnabled": True,
                    "isCdpTlvAppEnabled": True,
                    "isIpV6AutoconfigEnabled": True,
                    "lldpAdminStatus": "string",
                    "stpBpduGuard": "string",
                    "stpPortfastMode": "string",
                    "isSwitchportNonegotiate": True,
                    "portSecurityViolation": "string",
                    "isStormControlShutdownEnabled": True,
                    "isStormControlTrapEnabled": True,
                    "isArpInspectionTrustEnabled": True,
                    "isDhcpSnoopingTrustEnabled": True,
                    "isPortSecurityEnabled": True,
                    "portSecurityAgingTime": 0,
                    "ipV6PrefixList": {
                        "configType": "string",
                        "items": [{"configType": "string", "ipV6Address": "string"}],
                    },
                    "ipV6TrafficFilter": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "accessList": "string",
                                "direction": "string",
                            }
                        ],
                    },
                    "isMabEapEnabled": True,
                    "isMabEnabled": True,
                    "isMabWebauthPriority": True,
                    "isPeriodicAuthEnabled": True,
                    "isReauthTimerFromServerEnabled": True,
                    "bfdMinRxInterval": 0,
                    "reauthTimer": 0,
                    "staticSgt": 0,
                    "isStaticTrustedEnabled": True,
                    "accessVlanId": 0,
                    "accessList": "string",
                    "direction": "string",
                    "isSwitchportEnabled": True,
                    "trunkVlans": "string",
                    "txPeriod": 0,
                    "isBfdIntervalEnabled": {},
                    "isDhcpEnabled": True,
                    "isIpV6DhcpEnabled": True,
                }
            ]
        },
        feature="string",
        id="string",
        payload=None,
        portChannelInterfaceConfig={
            "items": [
                {
                    "portchannelNumber": 0,
                    "macAddress": "string",
                    "ipV4VrfName": "string",
                    "ipV4InboundAclName": "string",
                    "ipV4OutboundAclName": "string",
                    "stpPortPriority": 0,
                    "bfdTemplate": "string",
                    "configType": "string",
                    "description": "string",
                    "secondaryAddress": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "ipAddress": "string",
                                "mask": "string",
                            }
                        ],
                    },
                    "helperAddress": {
                        "configType": "string",
                        "items": [{"ipAddress": "string", "configType": "string"}],
                    },
                    "vrfName": "string",
                    "bfdMinTxInterval": 0,
                    "bfdIntervalMultiplier": 0,
                    "primaryAddress": "string",
                    "isBfdEnabled": True,
                    "isIpV6Enabled": True,
                    "isIpV6RedirectsEnabled": True,
                    "isIpV4DhcpEnabled": True,
                    "isIpV6DhcpEnabled": True,
                    "isIpV6AutoconfigEnabled": True,
                    "isIpv6RedirectsEnabled": True,
                    "isLacpFastSwitchoverEnabled": True,
                    "isShutdown": True,
                    "stpBpdufilterStatus": "string",
                    "trunkAllowedVlansMode": "string",
                    "trunkAllowedVlanIds": "string",
                    "isSwitchportNonegotiate": True,
                    "isProxyArpEnabled": True,
                    "isRapidCommitEnabled": True,
                    "isIpV4RedirectsEnabled": True,
                    "stpBpduGuard": "string",
                    "isSwitchportEnabled": True,
                    "mode": "string",
                    "isIpV4UnreachablesEnabled": True,
                    "accessVlanId": 0,
                    "minLinks": 0,
                    "bfdMinRxInterval": 0,
                    "ipV6DhcpRelayDestinationGlobal": {
                        "configType": "string",
                        "items": [{"configType": "string", "ipV6Address": "string"}],
                    },
                    "ipV4Mask": "string",
                    "ipV6TrafficFilter": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "actionList": "string",
                                "direction": "string",
                            }
                        ],
                    },
                    "lacpMaxBundle": 0,
                    "stpGuardMode": "string",
                    "stpPortfastMode": "string",
                    "ipV6PrefixList": {
                        "configType": "string",
                        "items": [{"configType": "string", "ipV6Prefix": "string"}],
                    },
                    "ipV6DhcpRelayDestination": {
                        "configType": "string",
                        "items": [{"configType": "string", "ipV6Address": "string"}],
                    },
                    "ipV6LinkLocalAddress": "string",
                    "stpCost": 0,
                    "nativeVlanId": 0,
                    "voiceVlanId": 0,
                    "isBfdIntervalEnabled": True,
                }
            ]
        },
    )
    return endpoint_result


@pytest.mark.wired
def test_add_intended_port_configurations(api, validator):
    try:
        assert is_valid_add_intended_port_configurations(
            validator, add_intended_port_configurations(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_intended_port_configurations_default_val(api):
    endpoint_result = api.wired.add_intended_port_configurations(
        active_validation=True,
        ethernetInterfaceConfig=None,
        feature="string",
        id="string",
        payload=None,
        portChannelInterfaceConfig=None,
    )
    return endpoint_result


@pytest.mark.wired
def test_add_intended_port_configurations_default_val(api, validator):
    try:
        assert is_valid_add_intended_port_configurations(
            validator, add_intended_port_configurations_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_intended_port_configurations(json_schema_validate, obj):
    json_schema_validate("jsd_36d1f7bd92b654ee8a8549f868b7225f_v3_2_3_0").validate(obj)
    return True


def get_intended_port_configurations(api):
    endpoint_result = api.wired.get_intended_port_configurations(
        feature="string", id="string", limit=0, offset=0
    )
    return endpoint_result


@pytest.mark.wired
def test_get_intended_port_configurations(api, validator):
    try:
        assert is_valid_get_intended_port_configurations(
            validator, get_intended_port_configurations(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_intended_port_configurations_default_val(api):
    endpoint_result = api.wired.get_intended_port_configurations(
        feature="string", id="string", limit=None, offset=None
    )
    return endpoint_result


@pytest.mark.wired
def test_get_intended_port_configurations_default_val(api, validator):
    try:
        assert is_valid_get_intended_port_configurations(
            validator, get_intended_port_configurations_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_deployed_layer3_config_count(json_schema_validate, obj):
    json_schema_validate("jsd_d058f2e619f65a379fc9027ccb76bd09_v3_2_3_0").validate(obj)
    return True


def get_deployed_layer3_config_count(api):
    endpoint_result = api.wired.get_deployed_layer3_config_count(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_get_deployed_layer3_config_count(api, validator):
    try:
        assert is_valid_get_deployed_layer3_config_count(
            validator, get_deployed_layer3_config_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_deployed_layer3_config_count_default_val(api):
    endpoint_result = api.wired.get_deployed_layer3_config_count(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_get_deployed_layer3_config_count_default_val(api, validator):
    try:
        assert is_valid_get_deployed_layer3_config_count(
            validator, get_deployed_layer3_config_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_deployed_port_feature_configurations(json_schema_validate, obj):
    json_schema_validate("jsd_a97e7b02905657d8ac61790110b0f057_v3_2_3_0").validate(obj)
    return True


def get_deployed_port_feature_configurations(api):
    endpoint_result = api.wired.get_deployed_port_feature_configurations(
        feature="string", id="string", limit=0, offset=0
    )
    return endpoint_result


@pytest.mark.wired
def test_get_deployed_port_feature_configurations(api, validator):
    try:
        assert is_valid_get_deployed_port_feature_configurations(
            validator, get_deployed_port_feature_configurations(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_deployed_port_feature_configurations_default_val(api):
    endpoint_result = api.wired.get_deployed_port_feature_configurations(
        feature="string", id="string", limit=None, offset=None
    )
    return endpoint_result


@pytest.mark.wired
def test_get_deployed_port_feature_configurations_default_val(api, validator):
    try:
        assert is_valid_get_deployed_port_feature_configurations(
            validator, get_deployed_port_feature_configurations_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_intended_port_config_count(json_schema_validate, obj):
    json_schema_validate("jsd_5c51594e9b965f27a6e579c66d9f6c5d_v3_2_3_0").validate(obj)
    return True


def get_intended_port_config_count(api):
    endpoint_result = api.wired.get_intended_port_config_count(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_get_intended_port_config_count(api, validator):
    try:
        assert is_valid_get_intended_port_config_count(
            validator, get_intended_port_config_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_intended_port_config_count_default_val(api):
    endpoint_result = api.wired.get_intended_port_config_count(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_get_intended_port_config_count_default_val(api, validator):
    try:
        assert is_valid_get_intended_port_config_count(
            validator, get_intended_port_config_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_configurations_for_an_intended_layer2_feature_on_a_wired_device(
    json_schema_validate, obj
):
    json_schema_validate("jsd_d1b2d399192a5da39b4ae3fe0f5288d4_v3_2_3_0").validate(obj)
    return True


def get_configurations_for_an_intended_layer2_feature_on_a_wired_device(api):
    endpoint_result = (
        api.wired.get_configurations_for_an_intended_layer2_feature_on_a_wired_device(
            feature="string", id="string"
        )
    )
    return endpoint_result


@pytest.mark.wired
def test_get_configurations_for_an_intended_layer2_feature_on_a_wired_device(
    api, validator
):
    try:
        assert is_valid_get_configurations_for_an_intended_layer2_feature_on_a_wired_device(
            validator,
            get_configurations_for_an_intended_layer2_feature_on_a_wired_device(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_configurations_for_an_intended_layer2_feature_on_a_wired_device_default_val(
    api,
):
    endpoint_result = (
        api.wired.get_configurations_for_an_intended_layer2_feature_on_a_wired_device(
            feature="string", id="string"
        )
    )
    return endpoint_result


@pytest.mark.wired
def test_get_configurations_for_an_intended_layer2_feature_on_a_wired_device_default_val(
    api, validator
):
    try:
        assert is_valid_get_configurations_for_an_intended_layer2_feature_on_a_wired_device(
            validator,
            get_configurations_for_an_intended_layer2_feature_on_a_wired_device_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_configurations_for_an_intended_layer2_feature_on_a_wired_device(
    json_schema_validate, obj
):
    json_schema_validate("jsd_50d4649fef20535193fd86c95925bcf8_v3_2_3_0").validate(obj)
    return True


def delete_configurations_for_an_intended_layer2_feature_on_a_wired_device(api):
    endpoint_result = api.wired.delete_configurations_for_an_intended_layer2_feature_on_a_wired_device(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_delete_configurations_for_an_intended_layer2_feature_on_a_wired_device(
    api, validator
):
    try:
        assert is_valid_delete_configurations_for_an_intended_layer2_feature_on_a_wired_device(
            validator,
            delete_configurations_for_an_intended_layer2_feature_on_a_wired_device(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_configurations_for_an_intended_layer2_feature_on_a_wired_device_default_val(
    api,
):
    endpoint_result = api.wired.delete_configurations_for_an_intended_layer2_feature_on_a_wired_device(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_delete_configurations_for_an_intended_layer2_feature_on_a_wired_device_default_val(
    api, validator
):
    try:
        assert is_valid_delete_configurations_for_an_intended_layer2_feature_on_a_wired_device(
            validator,
            delete_configurations_for_an_intended_layer2_feature_on_a_wired_device_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_configurations_for_an_intended_layer2_feature_on_a_wired_device(
    json_schema_validate, obj
):
    json_schema_validate("jsd_12ee7664344f50cb8f2c94beaa01629d_v3_2_3_0").validate(obj)
    return True


def update_configurations_for_an_intended_layer2_feature_on_a_wired_device(api):
    endpoint_result = api.wired.update_configurations_for_an_intended_layer2_feature_on_a_wired_device(
        active_validation=True,
        cdpGlobalConfig={
            "items": [
                {
                    "configType": "string",
                    "timer": 0,
                    "isCdpEnabled": True,
                    "isLogDuplexMismatchEnabled": True,
                    "isAdvertiseV2Enabled": True,
                    "holdTime": 0,
                }
            ]
        },
        cdpInterfaceConfig={
            "items": [
                {
                    "configType": "string",
                    "interfaceName": "string",
                    "isCdpEnabled": True,
                    "isLogDuplexMismatchEnabled": True,
                }
            ]
        },
        dhcpSnoopingGlobalConfig={
            "items": [
                {
                    "configType": "string",
                    "isDhcpSnoopingEnabled": True,
                    "databaseAgent": {
                        "configType": "string",
                        "agentUrl": "string",
                        "timeout": 0,
                        "writeDelay": 0,
                    },
                    "isGleaningEnabled": True,
                    "proxyBridgeVlans": "string",
                    "dhcpSnoopingVlans": "string",
                }
            ]
        },
        dhcpSnoopingInterfaceConfig={
            "items": [
                {
                    "configType": "string",
                    "interfaceName": "string",
                    "isTrustedInterface": True,
                    "messageRateLimit": 0,
                }
            ]
        },
        dot1xGlobalConfig={
            "items": [
                {
                    "configType": "string",
                    "authenticationConfigMode": "string",
                    "isDot1xEnabled": True,
                }
            ]
        },
        dot1xInterfaceConfig={
            "items": [
                {
                    "configType": "string",
                    "interfaceName": "string",
                    "authenticationOrder": {
                        "configType": "string",
                        "items": ["string"],
                    },
                }
            ]
        },
        feature="string",
        id="string",
        igmpSnoopingGlobalConfig={
            "items": [
                {
                    "configType": "string",
                    "isIgmpSnoopingEnabled": True,
                    "isQuerierEnabled": True,
                    "querierAddress": "string",
                    "querierQueryInterval": 0,
                    "querierVersion": "string",
                    "igmpSnoopingVlanSettings": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "vlanId": 0,
                                "isIgmpSnoopingEnabled": True,
                                "isImmediateLeaveEnabled": True,
                                "isQuerierEnabled": True,
                                "querierAddress": "string",
                                "querierQueryInterval": 0,
                                "querierVersion": "string",
                                "igmpSnoopingVlanMrouters": {
                                    "configType": "string",
                                    "items": [
                                        {
                                            "configType": "string",
                                            "interfaceName": "string",
                                        }
                                    ],
                                },
                            }
                        ],
                    },
                }
            ]
        },
        lldpGlobalConfig={
            "items": [
                {
                    "configType": "string",
                    "timer": 0,
                    "isLldpEnabled": True,
                    "reinitializationDelay": 0,
                    "holdTime": 0,
                }
            ]
        },
        lldpInterfaceConfig={
            "items": [
                {
                    "configType": "string",
                    "interfaceName": "string",
                    "adminStatus": "string",
                }
            ]
        },
        mabInterfaceConfig={
            "items": [
                {
                    "configType": "string",
                    "interfaceName": "string",
                    "isMabEnabled": True,
                }
            ]
        },
        mldSnoopingGlobalConfig={
            "items": [
                {
                    "configType": "string",
                    "isMldSnoopingEnabled": True,
                    "isSuppressListenerMessagesEnabled": True,
                    "isQuerierEnabled": True,
                    "querierAddress": "string",
                    "querierQueryInterval": 0,
                    "querierVersion": "string",
                    "mldSnoopingVlanSettings": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "vlanId": 0,
                                "isMldSnoopingEnabled": True,
                                "isImmediateLeaveEnabled": True,
                                "isQuerierEnabled": True,
                                "querierAddress": "string",
                                "querierQueryInterval": 0,
                                "querierVersion": "string",
                                "mldSnoopingVlanMrouters": {
                                    "configType": "string",
                                    "items": [
                                        {
                                            "configType": "string",
                                            "interfaceName": "string",
                                        }
                                    ],
                                },
                            }
                        ],
                    },
                }
            ]
        },
        payload=None,
        portChannelConfig={
            "items": [
                {
                    "configType": "string",
                    "isAutoEnabled": True,
                    "loadBalancingMethod": "string",
                    "lacpSystemPriority": 0,
                    "portchannels": {
                        "configType": "string",
                        "items": [
                            {
                                "AnyOf": {
                                    "EtherchannelConfig": {
                                        "configType": "string",
                                        "name": "string",
                                        "minLinks": 0,
                                        "memberPorts": {
                                            "configType": "string",
                                            "items": [
                                                {
                                                    "configType": "string",
                                                    "interfaceName": "string",
                                                    "mode": "string",
                                                }
                                            ],
                                        },
                                    },
                                    "LacpPortchannelConfig": {
                                        "configType": "string",
                                        "name": "string",
                                        "minLinks": 0,
                                        "memberPorts": {
                                            "configType": "string",
                                            "items": [
                                                {
                                                    "configType": "string",
                                                    "interfaceName": "string",
                                                    "mode": "string",
                                                    "portPriority": 0,
                                                    "rate": 0,
                                                }
                                            ],
                                        },
                                    },
                                    "PagpPortchannelConfig": {
                                        "configType": "string",
                                        "name": "string",
                                        "minLinks": 0,
                                        "memberPorts": {
                                            "configType": "string",
                                            "items": [
                                                {
                                                    "configType": "string",
                                                    "interfaceName": "string",
                                                    "mode": "string",
                                                    "portPriority": 0,
                                                    "learnMethod": "string",
                                                }
                                            ],
                                        },
                                    },
                                }
                            }
                        ],
                    },
                }
            ]
        },
        stpGlobalConfig={
            "items": [
                {
                    "configType": "string",
                    "stpMode": "string",
                    "isBackboneFastEnabled": True,
                    "isEtherChannelGuardEnabled": True,
                    "isExtendedSystemIdEnabled": True,
                    "isLoggingEnabled": True,
                    "isLoopGuardEnabled": True,
                    "portFastMode": "string",
                    "isBpduFilterEnabled": True,
                    "isBpduGuardEnabled": True,
                    "isUplinkFastEnabled": True,
                    "transmitHoldCount": 0,
                    "uplinkFastMaxUpdateRate": 0,
                    "stpInstances": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "vlanId": 0,
                                "priority": 0,
                                "timers": {
                                    "configType": "string",
                                    "forwardDelay": 0,
                                    "helloInterval": 0,
                                    "maxAge": 0,
                                    "isStpEnabled": True,
                                },
                            }
                        ],
                    },
                }
            ]
        },
        stpInterfaceConfig={
            "items": {
                "configType": "string",
                "interfaceName": "string",
                "guardMode": "string",
                "bpduFilter": "string",
                "bpduGuard": "string",
                "pathCost": 0,
                "portFastMode": "string",
                "priority": 0,
                "portVlanCostSettings": {
                    "configType": "string",
                    "items": [{"configType": "string", "cost": 0, "vlans": "string"}],
                },
                "portVlanPrioritySettings": {
                    "configType": "string",
                    "items": [
                        {"configType": "string", "priority": 0, "vlans": "string"}
                    ],
                },
            }
        },
        switchportInterfaceConfig={
            "items": [
                {
                    "configType": "string",
                    "interfaceName": "string",
                    "description": "string",
                    "mode": "string",
                    "accessVlan": 0,
                    "voiceVlan": 0,
                    "adminStatus": "string",
                    "trunkAllowedVlans": "string",
                    "nativeVlan": 0,
                }
            ]
        },
        trunkInterfaceConfig={
            "items": [
                {
                    "configType": "string",
                    "interfaceName": "string",
                    "isProtected": True,
                    "isDtpNegotiationEnabled": True,
                    "pruneEligibleVlans": "string",
                }
            ]
        },
        vlanConfig={
            "items": [
                {
                    "configType": "string",
                    "vlanId": 0,
                    "name": "string",
                    "isVlanEnabled": True,
                }
            ]
        },
        vtpGlobalConfig={
            "items": [
                {
                    "configType": "string",
                    "mode": "string",
                    "version": "string",
                    "domainName": "string",
                    "isPruningEnabled": True,
                    "configurationFileName": "string",
                    "sourceInterface": "string",
                }
            ]
        },
        vtpInterfaceConfig={
            "items": [
                {
                    "configType": "string",
                    "interfaceName": "string",
                    "isVtpEnabled": True,
                }
            ]
        },
    )
    return endpoint_result


@pytest.mark.wired
def test_update_configurations_for_an_intended_layer2_feature_on_a_wired_device(
    api, validator
):
    try:
        assert is_valid_update_configurations_for_an_intended_layer2_feature_on_a_wired_device(
            validator,
            update_configurations_for_an_intended_layer2_feature_on_a_wired_device(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_configurations_for_an_intended_layer2_feature_on_a_wired_device_default_val(
    api,
):
    endpoint_result = api.wired.update_configurations_for_an_intended_layer2_feature_on_a_wired_device(
        active_validation=True,
        cdpGlobalConfig=None,
        cdpInterfaceConfig=None,
        dhcpSnoopingGlobalConfig=None,
        dhcpSnoopingInterfaceConfig=None,
        dot1xGlobalConfig=None,
        dot1xInterfaceConfig=None,
        feature="string",
        id="string",
        igmpSnoopingGlobalConfig=None,
        lldpGlobalConfig=None,
        lldpInterfaceConfig=None,
        mabInterfaceConfig=None,
        mldSnoopingGlobalConfig=None,
        payload=None,
        portChannelConfig=None,
        stpGlobalConfig=None,
        stpInterfaceConfig=None,
        switchportInterfaceConfig=None,
        trunkInterfaceConfig=None,
        vlanConfig=None,
        vtpGlobalConfig=None,
        vtpInterfaceConfig=None,
    )
    return endpoint_result


@pytest.mark.wired
def test_update_configurations_for_an_intended_layer2_feature_on_a_wired_device_default_val(
    api, validator
):
    try:
        assert is_valid_update_configurations_for_an_intended_layer2_feature_on_a_wired_device(
            validator,
            update_configurations_for_an_intended_layer2_feature_on_a_wired_device_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_configurations_for_an_intended_layer2_feature_on_a_wired_device(
    json_schema_validate, obj
):
    json_schema_validate("jsd_162286d7b57050bdb98e9340d0bc4dba_v3_2_3_0").validate(obj)
    return True


def create_configurations_for_an_intended_layer2_feature_on_a_wired_device(api):
    endpoint_result = api.wired.create_configurations_for_an_intended_layer2_feature_on_a_wired_device(
        active_validation=True,
        cdpGlobalConfig={
            "items": [
                {
                    "configType": "string",
                    "timer": 0,
                    "isCdpEnabled": True,
                    "isLogDuplexMismatchEnabled": True,
                    "isAdvertiseV2Enabled": True,
                    "holdTime": 0,
                }
            ]
        },
        cdpInterfaceConfig={
            "items": [
                {
                    "configType": "string",
                    "interfaceName": "string",
                    "isCdpEnabled": True,
                    "isLogDuplexMismatchEnabled": True,
                }
            ]
        },
        dhcpSnoopingGlobalConfig={
            "items": [
                {
                    "configType": "string",
                    "isDhcpSnoopingEnabled": True,
                    "databaseAgent": {
                        "configType": "string",
                        "agentUrl": "string",
                        "timeout": 0,
                        "writeDelay": 0,
                    },
                    "isGleaningEnabled": True,
                    "proxyBridgeVlans": "string",
                    "dhcpSnoopingVlans": "string",
                }
            ]
        },
        dhcpSnoopingInterfaceConfig={
            "items": [
                {
                    "configType": "string",
                    "interfaceName": "string",
                    "isTrustedInterface": True,
                    "messageRateLimit": 0,
                }
            ]
        },
        dot1xGlobalConfig={
            "items": [
                {
                    "configType": "string",
                    "authenticationConfigMode": "string",
                    "isDot1xEnabled": True,
                }
            ]
        },
        dot1xInterfaceConfig={
            "items": [
                {
                    "configType": "string",
                    "interfaceName": "string",
                    "authenticationOrder": {
                        "configType": "string",
                        "items": ["string"],
                    },
                }
            ]
        },
        feature="string",
        id="string",
        igmpSnoopingGlobalConfig={
            "items": [
                {
                    "configType": "string",
                    "isIgmpSnoopingEnabled": True,
                    "isQuerierEnabled": True,
                    "querierAddress": "string",
                    "querierQueryInterval": 0,
                    "querierVersion": "string",
                    "igmpSnoopingVlanSettings": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "vlanId": 0,
                                "isIgmpSnoopingEnabled": True,
                                "isImmediateLeaveEnabled": True,
                                "isQuerierEnabled": True,
                                "querierAddress": "string",
                                "querierQueryInterval": 0,
                                "querierVersion": "string",
                                "igmpSnoopingVlanMrouters": {
                                    "configType": "string",
                                    "items": [
                                        {
                                            "configType": "string",
                                            "interfaceName": "string",
                                        }
                                    ],
                                },
                            }
                        ],
                    },
                }
            ]
        },
        lldpGlobalConfig={
            "items": [
                {
                    "configType": "string",
                    "timer": 0,
                    "isLldpEnabled": True,
                    "reinitializationDelay": 0,
                    "holdTime": 0,
                }
            ]
        },
        lldpInterfaceConfig={
            "items": [
                {
                    "configType": "string",
                    "interfaceName": "string",
                    "adminStatus": "string",
                }
            ]
        },
        mabInterfaceConfig={
            "items": [
                {
                    "configType": "string",
                    "interfaceName": "string",
                    "isMabEnabled": True,
                }
            ]
        },
        mldSnoopingGlobalConfig={
            "items": [
                {
                    "configType": "string",
                    "isMldSnoopingEnabled": True,
                    "isSuppressListenerMessagesEnabled": True,
                    "isQuerierEnabled": True,
                    "querierAddress": "string",
                    "querierQueryInterval": 0,
                    "querierVersion": "string",
                    "mldSnoopingVlanSettings": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "vlanId": 0,
                                "isMldSnoopingEnabled": True,
                                "isImmediateLeaveEnabled": True,
                                "isQuerierEnabled": True,
                                "querierAddress": "string",
                                "querierQueryInterval": 0,
                                "querierVersion": "string",
                                "mldSnoopingVlanMrouters": {
                                    "configType": "string",
                                    "items": [
                                        {
                                            "configType": "string",
                                            "interfaceName": "string",
                                        }
                                    ],
                                },
                            }
                        ],
                    },
                }
            ]
        },
        payload=None,
        portChannelConfig={
            "items": [
                {
                    "configType": "string",
                    "isAutoEnabled": True,
                    "loadBalancingMethod": "string",
                    "lacpSystemPriority": 0,
                    "portchannels": {
                        "configType": "string",
                        "items": [
                            {
                                "AnyOf": {
                                    "EtherchannelConfig": {
                                        "configType": "string",
                                        "name": "string",
                                        "minLinks": 0,
                                        "memberPorts": {
                                            "configType": "string",
                                            "items": [
                                                {
                                                    "configType": "string",
                                                    "interfaceName": "string",
                                                    "mode": "string",
                                                }
                                            ],
                                        },
                                    },
                                    "LacpPortchannelConfig": {
                                        "configType": "string",
                                        "name": "string",
                                        "minLinks": 0,
                                        "memberPorts": {
                                            "configType": "string",
                                            "items": [
                                                {
                                                    "configType": "string",
                                                    "interfaceName": "string",
                                                    "mode": "string",
                                                    "portPriority": 0,
                                                    "rate": 0,
                                                }
                                            ],
                                        },
                                    },
                                    "PagpPortchannelConfig": {
                                        "configType": "string",
                                        "name": "string",
                                        "minLinks": 0,
                                        "memberPorts": {
                                            "configType": "string",
                                            "items": [
                                                {
                                                    "configType": "string",
                                                    "interfaceName": "string",
                                                    "mode": "string",
                                                    "portPriority": 0,
                                                    "learnMethod": "string",
                                                }
                                            ],
                                        },
                                    },
                                }
                            }
                        ],
                    },
                }
            ]
        },
        stpGlobalConfig={
            "items": [
                {
                    "configType": "string",
                    "stpMode": "string",
                    "isBackboneFastEnabled": True,
                    "isEtherChannelGuardEnabled": True,
                    "isExtendedSystemIdEnabled": True,
                    "isLoggingEnabled": True,
                    "isLoopGuardEnabled": True,
                    "portFastMode": "string",
                    "isBpduFilterEnabled": True,
                    "isBpduGuardEnabled": True,
                    "isUplinkFastEnabled": True,
                    "transmitHoldCount": 0,
                    "uplinkFastMaxUpdateRate": 0,
                    "stpInstances": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "vlanId": 0,
                                "priority": 0,
                                "timers": {
                                    "configType": "string",
                                    "forwardDelay": 0,
                                    "helloInterval": 0,
                                    "maxAge": 0,
                                    "isStpEnabled": True,
                                },
                            }
                        ],
                    },
                }
            ]
        },
        stpInterfaceConfig={
            "items": {
                "configType": "string",
                "interfaceName": "string",
                "guardMode": "string",
                "bpduFilter": "string",
                "bpduGuard": "string",
                "pathCost": 0,
                "portFastMode": "string",
                "priority": 0,
                "portVlanCostSettings": {
                    "configType": "string",
                    "items": [{"configType": "string", "cost": 0, "vlans": "string"}],
                },
                "portVlanPrioritySettings": {
                    "configType": "string",
                    "items": [
                        {"configType": "string", "priority": 0, "vlans": "string"}
                    ],
                },
            }
        },
        switchportInterfaceConfig={
            "items": [
                {
                    "configType": "string",
                    "interfaceName": "string",
                    "description": "string",
                    "mode": "string",
                    "accessVlan": 0,
                    "voiceVlan": 0,
                    "adminStatus": "string",
                    "trunkAllowedVlans": "string",
                    "nativeVlan": 0,
                }
            ]
        },
        trunkInterfaceConfig={
            "items": [
                {
                    "configType": "string",
                    "interfaceName": "string",
                    "isProtected": True,
                    "isDtpNegotiationEnabled": True,
                    "pruneEligibleVlans": "string",
                }
            ]
        },
        vlanConfig={
            "items": [
                {
                    "configType": "string",
                    "vlanId": 0,
                    "name": "string",
                    "isVlanEnabled": True,
                }
            ]
        },
        vtpGlobalConfig={
            "items": [
                {
                    "configType": "string",
                    "mode": "string",
                    "version": "string",
                    "domainName": "string",
                    "isPruningEnabled": True,
                    "configurationFileName": "string",
                    "sourceInterface": "string",
                }
            ]
        },
        vtpInterfaceConfig={
            "items": [
                {
                    "configType": "string",
                    "interfaceName": "string",
                    "isVtpEnabled": True,
                }
            ]
        },
    )
    return endpoint_result


@pytest.mark.wired
def test_create_configurations_for_an_intended_layer2_feature_on_a_wired_device(
    api, validator
):
    try:
        assert is_valid_create_configurations_for_an_intended_layer2_feature_on_a_wired_device(
            validator,
            create_configurations_for_an_intended_layer2_feature_on_a_wired_device(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_configurations_for_an_intended_layer2_feature_on_a_wired_device_default_val(
    api,
):
    endpoint_result = api.wired.create_configurations_for_an_intended_layer2_feature_on_a_wired_device(
        active_validation=True,
        cdpGlobalConfig=None,
        cdpInterfaceConfig=None,
        dhcpSnoopingGlobalConfig=None,
        dhcpSnoopingInterfaceConfig=None,
        dot1xGlobalConfig=None,
        dot1xInterfaceConfig=None,
        feature="string",
        id="string",
        igmpSnoopingGlobalConfig=None,
        lldpGlobalConfig=None,
        lldpInterfaceConfig=None,
        mabInterfaceConfig=None,
        mldSnoopingGlobalConfig=None,
        payload=None,
        portChannelConfig=None,
        stpGlobalConfig=None,
        stpInterfaceConfig=None,
        switchportInterfaceConfig=None,
        trunkInterfaceConfig=None,
        vlanConfig=None,
        vtpGlobalConfig=None,
        vtpInterfaceConfig=None,
    )
    return endpoint_result


@pytest.mark.wired
def test_create_configurations_for_an_intended_layer2_feature_on_a_wired_device_default_val(
    api, validator
):
    try:
        assert is_valid_create_configurations_for_an_intended_layer2_feature_on_a_wired_device(
            validator,
            create_configurations_for_an_intended_layer2_feature_on_a_wired_device_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_intended_network_settings_configurations(json_schema_validate, obj):
    json_schema_validate("jsd_f527ec1c3b08547e9a1d1138ff1c3f25_v3_2_3_0").validate(obj)
    return True


def add_intended_network_settings_configurations(api):
    endpoint_result = api.wired.add_intended_network_settings_configurations(
        active_validation=True,
        dhcpExcludedAddressConfig={
            "items": [
                {
                    "configType": "string",
                    "ipDhcpExcludedLowHighAddressConfig": {
                        "items": [
                            {
                                "configType": "string",
                                "excludedAddressLow": "string",
                                "excludedAddressHigh": "string",
                            }
                        ]
                    },
                    "ipDhcpExcludedLowAddressConfig": {
                        "items": [
                            {"configType": "string", "excludedAddressLow": "string"}
                        ]
                    },
                }
            ]
        },
        dhcpGeneralConfig={
            "items": [{"configType": "string", "isBootpIgnoreEnabled": True}]
        },
        domainConfig={
            "items": [
                {
                    "configType": "string",
                    "domainName": "string",
                    "ipDomainList": {
                        "configType": "string",
                        "items": [{"configType": "string", "domainNameList": "string"}],
                    },
                    "ipDomainName": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "domainWithVrf": {
                                    "configType": "string",
                                    "items": [
                                        {
                                            "configType": "string",
                                            "domainName": "string",
                                            "vrfName": "string",
                                        }
                                    ],
                                },
                            }
                        ],
                    },
                    "sourceLoopbackInterface": 0,
                    "isLookupEnabled": True,
                    "timeout": 0,
                }
            ]
        },
        feature="string",
        id="string",
        ipV4DhcpPoolConfig={
            "items": [
                {
                    "configType": "string",
                    "poolName": "string",
                    "primaryNetworkMask": "string",
                    "primaryNetworkNumber": "string",
                    "vrfName": "string",
                    "defaultRouterList": "string",
                    "dnsServerList": "string",
                    "leaseDays": 0,
                    "leaseHours": 0,
                    "leaseMinutes": 0,
                    "optionCode": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "asciiString": "string",
                                "ipAddresses": "string",
                                "optionCode": 0,
                                "hexadecimalString": "string",
                                "ipAddressString": "string",
                            }
                        ],
                    },
                    "domainName": "string",
                }
            ]
        },
        ipV6DhcpPoolConfig={
            "items": [
                {
                    "configType": "string",
                    "dnsServer": "string",
                    "domainNames": "string",
                    "poolName": "string",
                    "prefix": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "ipV6Prefix": "string",
                                "poolName": "string",
                                "preferredLifetime": 0,
                                "validLifetime": 0,
                            }
                        ],
                    },
                }
            ]
        },
        nameServerConfig={
            "items": [
                {
                    "configType": "string",
                    "nameServers": "string",
                    "nameServerWithVrf": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "vrfName": "string",
                                "nameServers": "string",
                            }
                        ],
                    },
                }
            ]
        },
        ntpAuthenticationKeyConfig={
            "items": [
                {
                    "configType": "string",
                    "encryptionType": 0,
                    "md5": "string",
                    "md5Config": "string",
                    "keyNumber": 0,
                }
            ]
        },
        ntpGeneralConfig={
            "items": [
                {
                    "configType": "string",
                    "isAuthenticateEnabled": True,
                    "isLoggingEnabled": True,
                    "sourceLoopbackInterface": 0,
                    "stratum": 0,
                }
            ]
        },
        ntpPerVrfServerConfig={
            "items": [
                {
                    "configType": "string",
                    "ntpVrfServerList": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "ipAddress": "string",
                                "peerAuthenticationKey": 0,
                                "isPreferred": True,
                            }
                        ],
                    },
                    "vrfName": "string",
                }
            ]
        },
        ntpServerConfig={
            "items": [
                {
                    "configType": "string",
                    "ipAddress": "string",
                    "peerAuthenticationKey": 0,
                    "isPreferred": True,
                    "sourceInterface": "string",
                }
            ]
        },
        ntpTrustedKeyConfig={"items": [{"configType": "string", "trustedKey": 0}]},
        payload=None,
    )
    return endpoint_result


@pytest.mark.wired
def test_add_intended_network_settings_configurations(api, validator):
    try:
        assert is_valid_add_intended_network_settings_configurations(
            validator, add_intended_network_settings_configurations(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_intended_network_settings_configurations_default_val(api):
    endpoint_result = api.wired.add_intended_network_settings_configurations(
        active_validation=True,
        dhcpExcludedAddressConfig=None,
        dhcpGeneralConfig=None,
        domainConfig=None,
        feature="string",
        id="string",
        ipV4DhcpPoolConfig=None,
        ipV6DhcpPoolConfig=None,
        nameServerConfig=None,
        ntpAuthenticationKeyConfig=None,
        ntpGeneralConfig=None,
        ntpPerVrfServerConfig=None,
        ntpServerConfig=None,
        ntpTrustedKeyConfig=None,
        payload=None,
    )
    return endpoint_result


@pytest.mark.wired
def test_add_intended_network_settings_configurations_default_val(api, validator):
    try:
        assert is_valid_add_intended_network_settings_configurations(
            validator, add_intended_network_settings_configurations_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_intended_network_settings_configurations(json_schema_validate, obj):
    json_schema_validate("jsd_b851dc7a9bc352a680e8ca37fb8b4fcc_v3_2_3_0").validate(obj)
    return True


def get_intended_network_settings_configurations(api):
    endpoint_result = api.wired.get_intended_network_settings_configurations(
        feature="string", id="string", limit=0, offset=0
    )
    return endpoint_result


@pytest.mark.wired
def test_get_intended_network_settings_configurations(api, validator):
    try:
        assert is_valid_get_intended_network_settings_configurations(
            validator, get_intended_network_settings_configurations(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_intended_network_settings_configurations_default_val(api):
    endpoint_result = api.wired.get_intended_network_settings_configurations(
        feature="string", id="string", limit=None, offset=None
    )
    return endpoint_result


@pytest.mark.wired
def test_get_intended_network_settings_configurations_default_val(api, validator):
    try:
        assert is_valid_get_intended_network_settings_configurations(
            validator, get_intended_network_settings_configurations_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_intended_network_settings_configurations(json_schema_validate, obj):
    json_schema_validate("jsd_c7cb6993eea05af1b710666f8e257a8e_v3_2_3_0").validate(obj)
    return True


def delete_intended_network_settings_configurations(api):
    endpoint_result = api.wired.delete_intended_network_settings_configurations(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_delete_intended_network_settings_configurations(api, validator):
    try:
        assert is_valid_delete_intended_network_settings_configurations(
            validator, delete_intended_network_settings_configurations(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_intended_network_settings_configurations_default_val(api):
    endpoint_result = api.wired.delete_intended_network_settings_configurations(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_delete_intended_network_settings_configurations_default_val(api, validator):
    try:
        assert is_valid_delete_intended_network_settings_configurations(
            validator, delete_intended_network_settings_configurations_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_intended_network_settings_configurations(json_schema_validate, obj):
    json_schema_validate("jsd_a43a9f24a3705db1a74241b01ebc991d_v3_2_3_0").validate(obj)
    return True


def update_intended_network_settings_configurations(api):
    endpoint_result = api.wired.update_intended_network_settings_configurations(
        active_validation=True,
        dhcpExcludedAddressConfig={
            "items": [
                {
                    "configType": "string",
                    "ipDhcpExcludedLowHighAddressConfig": {
                        "items": [
                            {
                                "configType": "string",
                                "excludedAddressLow": "string",
                                "excludedAddressHigh": "string",
                            }
                        ]
                    },
                    "ipDhcpExcludedLowAddressConfig": {
                        "items": [
                            {"configType": "string", "excludedAddressLow": "string"}
                        ]
                    },
                }
            ]
        },
        dhcpGeneralConfig={
            "items": [{"configType": "string", "isBootpIgnoreEnabled": True}]
        },
        domainConfig={
            "items": [
                {
                    "configType": "string",
                    "domainName": "string",
                    "ipDomainList": {
                        "configType": "string",
                        "items": [{"configType": "string", "domainNameList": "string"}],
                    },
                    "ipDomainName": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "domainWithVrf": {
                                    "configType": "string",
                                    "items": [
                                        {
                                            "configType": "string",
                                            "domainName": "string",
                                            "vrfName": "string",
                                        }
                                    ],
                                },
                            }
                        ],
                    },
                    "sourceLoopbackInterface": 0,
                    "isLookupEnabled": True,
                    "timeout": 0,
                }
            ]
        },
        feature="string",
        id="string",
        ipV4DhcpPoolConfig={
            "items": [
                {
                    "configType": "string",
                    "poolName": "string",
                    "primaryNetworkMask": "string",
                    "primaryNetworkNumber": "string",
                    "vrfName": "string",
                    "defaultRouterList": "string",
                    "dnsServerList": "string",
                    "leaseDays": 0,
                    "leaseHours": 0,
                    "leaseMinutes": 0,
                    "optionCode": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "asciiString": "string",
                                "ipAddresses": "string",
                                "optionCode": 0,
                                "hexadecimalString": "string",
                                "ipAddressString": "string",
                            }
                        ],
                    },
                    "domainName": "string",
                }
            ]
        },
        ipV6DhcpPoolConfig={
            "items": [
                {
                    "configType": "string",
                    "dnsServer": "string",
                    "domainNames": "string",
                    "poolName": "string",
                    "prefix": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "ipV6Prefix": "string",
                                "poolName": "string",
                                "preferredLifetime": 0,
                                "validLifetime": 0,
                            }
                        ],
                    },
                }
            ]
        },
        nameServerConfig={
            "items": [
                {
                    "configType": "string",
                    "nameServers": "string",
                    "nameServerWithVrf": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "vrfName": "string",
                                "nameServers": "string",
                            }
                        ],
                    },
                }
            ]
        },
        ntpAuthenticationKeyConfig={
            "items": [
                {
                    "configType": "string",
                    "encryptionType": 0,
                    "md5": "string",
                    "md5Config": "string",
                    "keyNumber": 0,
                }
            ]
        },
        ntpGeneralConfig={
            "items": [
                {
                    "configType": "string",
                    "isAuthenticateEnabled": True,
                    "isLoggingEnabled": True,
                    "sourceLoopbackInterface": 0,
                    "stratum": 0,
                }
            ]
        },
        ntpPerVrfServerConfig={
            "items": [
                {
                    "configType": "string",
                    "ntpVrfServerList": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "ipAddress": "string",
                                "peerAuthenticationKey": 0,
                                "isPreferred": True,
                            }
                        ],
                    },
                    "vrfName": "string",
                }
            ]
        },
        ntpServerConfig={
            "items": [
                {
                    "configType": "string",
                    "ipAddress": "string",
                    "peerAuthenticationKey": 0,
                    "isPreferred": True,
                    "sourceInterface": "string",
                }
            ]
        },
        ntpTrustedKeyConfig={"items": [{"configType": "string", "trustedKey": 0}]},
        payload=None,
    )
    return endpoint_result


@pytest.mark.wired
def test_update_intended_network_settings_configurations(api, validator):
    try:
        assert is_valid_update_intended_network_settings_configurations(
            validator, update_intended_network_settings_configurations(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_intended_network_settings_configurations_default_val(api):
    endpoint_result = api.wired.update_intended_network_settings_configurations(
        active_validation=True,
        dhcpExcludedAddressConfig=None,
        dhcpGeneralConfig=None,
        domainConfig=None,
        feature="string",
        id="string",
        ipV4DhcpPoolConfig=None,
        ipV6DhcpPoolConfig=None,
        nameServerConfig=None,
        ntpAuthenticationKeyConfig=None,
        ntpGeneralConfig=None,
        ntpPerVrfServerConfig=None,
        ntpServerConfig=None,
        ntpTrustedKeyConfig=None,
        payload=None,
    )
    return endpoint_result


@pytest.mark.wired
def test_update_intended_network_settings_configurations_default_val(api, validator):
    try:
        assert is_valid_update_intended_network_settings_configurations(
            validator, update_intended_network_settings_configurations_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_deployed_configuration_learning_status(json_schema_validate, obj):
    json_schema_validate("jsd_ead369243e89557580bd605ba8e110b6_v3_2_3_0").validate(obj)
    return True


def get_deployed_configuration_learning_status(api):
    endpoint_result = api.wired.get_deployed_configuration_learning_status(
        active_validation=True, deviceUuids=["string"], payload=None
    )
    return endpoint_result


@pytest.mark.wired
def test_get_deployed_configuration_learning_status(api, validator):
    try:
        assert is_valid_get_deployed_configuration_learning_status(
            validator, get_deployed_configuration_learning_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_deployed_configuration_learning_status_default_val(api):
    endpoint_result = api.wired.get_deployed_configuration_learning_status(
        active_validation=True, deviceUuids=None, payload=None
    )
    return endpoint_result


@pytest.mark.wired
def test_get_deployed_configuration_learning_status_default_val(api, validator):
    try:
        assert is_valid_get_deployed_configuration_learning_status(
            validator, get_deployed_configuration_learning_status_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_supported_network_settings_features(json_schema_validate, obj):
    json_schema_validate("jsd_2d399a5429f0536ab4250374a75d1973_v3_2_3_0").validate(obj)
    return True


def get_supported_network_settings_features(api):
    endpoint_result = api.wired.get_supported_network_settings_features(id="string")
    return endpoint_result


@pytest.mark.wired
def test_get_supported_network_settings_features(api, validator):
    try:
        assert is_valid_get_supported_network_settings_features(
            validator, get_supported_network_settings_features(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_supported_network_settings_features_default_val(api):
    endpoint_result = api.wired.get_supported_network_settings_features(id="string")
    return endpoint_result


@pytest.mark.wired
def test_get_supported_network_settings_features_default_val(api, validator):
    try:
        assert is_valid_get_supported_network_settings_features(
            validator, get_supported_network_settings_features_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_deployed_network_settings_configurations(json_schema_validate, obj):
    json_schema_validate("jsd_58c6400c350f5b06bc0719c938a10e7b_v3_2_3_0").validate(obj)
    return True


def get_deployed_network_settings_configurations(api):
    endpoint_result = api.wired.get_deployed_network_settings_configurations(
        feature="string", id="string", limit=0, offset=0
    )
    return endpoint_result


@pytest.mark.wired
def test_get_deployed_network_settings_configurations(api, validator):
    try:
        assert is_valid_get_deployed_network_settings_configurations(
            validator, get_deployed_network_settings_configurations(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_deployed_network_settings_configurations_default_val(api):
    endpoint_result = api.wired.get_deployed_network_settings_configurations(
        feature="string", id="string", limit=None, offset=None
    )
    return endpoint_result


@pytest.mark.wired
def test_get_deployed_network_settings_configurations_default_val(api, validator):
    try:
        assert is_valid_get_deployed_network_settings_configurations(
            validator, get_deployed_network_settings_configurations_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_number_of_configurations_for_an_intended_layer2_feature_on_a_wired_device(
    json_schema_validate, obj
):
    json_schema_validate("jsd_1614364d2cca58398312cb0129d39d8c_v3_2_3_0").validate(obj)
    return True


def get_number_of_configurations_for_an_intended_layer2_feature_on_a_wired_device(api):
    endpoint_result = api.wired.get_number_of_configurations_for_an_intended_layer2_feature_on_a_wired_device(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_get_number_of_configurations_for_an_intended_layer2_feature_on_a_wired_device(
    api, validator
):
    try:
        assert is_valid_get_number_of_configurations_for_an_intended_layer2_feature_on_a_wired_device(
            validator,
            get_number_of_configurations_for_an_intended_layer2_feature_on_a_wired_device(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_number_of_configurations_for_an_intended_layer2_feature_on_a_wired_device_default_val(
    api,
):
    endpoint_result = api.wired.get_number_of_configurations_for_an_intended_layer2_feature_on_a_wired_device(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_get_number_of_configurations_for_an_intended_layer2_feature_on_a_wired_device_default_val(
    api, validator
):
    try:
        assert is_valid_get_number_of_configurations_for_an_intended_layer2_feature_on_a_wired_device(
            validator,
            get_number_of_configurations_for_an_intended_layer2_feature_on_a_wired_device_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_intended_security_config_count(json_schema_validate, obj):
    json_schema_validate("jsd_547f8e5737305424add787cbd20fe2bc_v3_2_3_0").validate(obj)
    return True


def get_intended_security_config_count(api):
    endpoint_result = api.wired.get_intended_security_config_count(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_get_intended_security_config_count(api, validator):
    try:
        assert is_valid_get_intended_security_config_count(
            validator, get_intended_security_config_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_intended_security_config_count_default_val(api):
    endpoint_result = api.wired.get_intended_security_config_count(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_get_intended_security_config_count_default_val(api, validator):
    try:
        assert is_valid_get_intended_security_config_count(
            validator, get_intended_security_config_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_intended_layer3_configurations(json_schema_validate, obj):
    json_schema_validate("jsd_71c0d437df555638b0fcac4cb8e04750_v3_2_3_0").validate(obj)
    return True


def delete_intended_layer3_configurations(api):
    endpoint_result = api.wired.delete_intended_layer3_configurations(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_delete_intended_layer3_configurations(api, validator):
    try:
        assert is_valid_delete_intended_layer3_configurations(
            validator, delete_intended_layer3_configurations(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_intended_layer3_configurations_default_val(api):
    endpoint_result = api.wired.delete_intended_layer3_configurations(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_delete_intended_layer3_configurations_default_val(api, validator):
    try:
        assert is_valid_delete_intended_layer3_configurations(
            validator, delete_intended_layer3_configurations_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_intended_layer3_configurations(json_schema_validate, obj):
    json_schema_validate("jsd_6fb6660c599b5b12832f5e82b1e5b56a_v3_2_3_0").validate(obj)
    return True


def update_intended_layer3_configurations(api):
    endpoint_result = api.wired.update_intended_layer3_configurations(
        active_validation=True,
        bfdConfig={
            "items": [
                {"configType": "string", "ipV6L3Cos": 0, "isMoreSnmpTrapsEnabled": True}
            ]
        },
        bfdTemplateSingleHopConfig={
            "items": [
                {
                    "name": "string",
                    "configType": "string",
                    "isEchoEnabled": True,
                    "intervalMultiplier": 0,
                    "minRxInterval": 0,
                    "minTxInterval": 0,
                    "sha1AuthenticationKeychain": "string",
                }
            ]
        },
        dhcpRelayConfig={
            "items": [
                {
                    "configType": "string",
                    "isTrustAllEnabled": True,
                    "isVpnOptionEnabled": True,
                    "isDefaultOptionEnabled": True,
                }
            ]
        },
        feature="string",
        id="string",
        ipv4RoutesConfig={
            "items": [
                {
                    "configType": "string",
                    "forwardingList": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "nextHopFwd": "string",
                                "metric": 0,
                            }
                        ],
                    },
                    "mask": "string",
                    "prefix": "string",
                }
            ]
        },
        ipv4RoutingConfig={
            "items": [{"configType": "string", "isRoutingEnabled": True}]
        },
        ipv4VrfConfig={
            "items": [
                {
                    "configType": "string",
                    "name": "string",
                    "routeDistinguisher": "string",
                    "routeTarget": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "direction": "string",
                                "target": "string",
                            }
                        ],
                    },
                }
            ]
        },
        ipv4VrfRoutesConfig={
            "items": [
                {
                    "configType": "string",
                    "forwardingList": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "forwardingList": {
                                    "configType": "string",
                                    "items": [
                                        {
                                            "configType": "string",
                                            "interfaceNextHop": {
                                                "configType": "string",
                                                "items": [
                                                    {
                                                        "configType": "string",
                                                        "ipAddress": "string",
                                                    }
                                                ],
                                            },
                                            "nextHopFwd": "string",
                                        }
                                    ],
                                },
                                "mask": "string",
                                "prefix": "string",
                            }
                        ],
                    },
                    "vrfName": "string",
                }
            ]
        },
        ipv6RoutesConfig={
            "items": [
                {
                    "configType": "string",
                    "forwardingList": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "interfaceNextHop": {
                                    "configType": "string",
                                    "items": [
                                        {"configType": "string", "ipAddress": "string"}
                                    ],
                                },
                                "nextHopFwd": "string",
                            }
                        ],
                    },
                    "prefix": "string",
                }
            ]
        },
        ipv6RoutingConfig={
            "items": [{"configType": "string", "isUnicastRoutingEnabled": True}]
        },
        ipv6VrfRoutesConfig={
            "items": [
                {
                    "configType": "string",
                    "forwardingList": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "prefix": "string",
                                "forwardingList": {
                                    "configType": "string",
                                    "items": [
                                        {
                                            "configType": "string",
                                            "interfaceNextHop": {
                                                "configType": "string",
                                                "items": [
                                                    {
                                                        "configType": "string",
                                                        "ipAddress": "string",
                                                    }
                                                ],
                                            },
                                            "nextHopFwd": "string",
                                        }
                                    ],
                                },
                            }
                        ],
                    },
                    "vrfName": "string",
                }
            ]
        },
        loopbackConfig={
            "items": [
                {
                    "bfdTemplate": "string",
                    "configType": "string",
                    "bfdMinTxInterval": 0,
                    "bfdMinRxInterval": 0,
                    "bfdIntervalMultiplier": 0,
                    "isBfdEnabled": True,
                    "isDhcpRelayInfoTrusted": True,
                    "isProxyArpEnabled": True,
                    "isIpV6Enabled": True,
                    "isShutdownEnabled": True,
                    "isRedirectsEnabled": True,
                    "isIpV4UnreachablesEnabled": True,
                    "description": "string",
                    "loopbackNumber": 0,
                    "primaryMask": "string",
                    "primaryIpAddress": "string",
                    "vrfName": "string",
                    "ipVrfName": "string",
                    "isDhcpEnabled": True,
                    "isIpV6AutoconfigEnabled": True,
                    "secondaryAddresses": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "ipAddress": "string",
                                "mask": "string",
                            }
                        ],
                    },
                    "ipV6DhcpServerAddress": {
                        "configType": "string",
                        "items": [{"configType": "string", "dhcpServerPool": "string"}],
                    },
                    "ipV6LinkLocalAddress": "string",
                    "ipV6DhcpRelayDestination": {
                        "configType": "string",
                        "items": [{"configType": "string", "ipV6Address": "string"}],
                    },
                    "ipV6PrefixList": {
                        "configType": "string",
                        "items": [{"configType": "string", "ipV6Prefix": "string"}],
                    },
                    "isBfdIntervalEnabled": True,
                }
            ]
        },
        payload=None,
        sviConfig={
            "items": [
                {
                    "bfdTemplate": "string",
                    "configType": "string",
                    "dhcpRelaySourceInterface": "string",
                    "vrfName": "string",
                    "vlanId": 0,
                    "macAddress": "string",
                    "secondaryAddresses": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "ipAddress": "string",
                                "mask": "string",
                            }
                        ],
                    },
                    "dhcpClientId": "string",
                    "ipVrfName": "string",
                    "isIpV4UnreachablesEnabled": True,
                    "helperAddress": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "ipAddress": "string",
                                "vrfName": "string",
                            }
                        ],
                    },
                    "igmpVersion": 0,
                    "bfdMinTxInterval": 0,
                    "bfdMinRxInterval": 0,
                    "bfdIntervalMultiplier": 0,
                    "ipV6AddressPrefixList": {
                        "configType": "string",
                        "items": [{"configType": "string", "ipV6Prefix": "string"}],
                    },
                    "isBfdEnabled": True,
                    "isDhcpRelayInfoOptionVpnIdEnabled": True,
                    "isIpV6DhcpRelayOptionVpnEnabled": True,
                    "isIpV6RedirectsEnabled": True,
                    "isIpv6DhcpRelayTrustEnabled": True,
                    "isIpV6DhcpClientReqVendorEnabled": True,
                    "isRedirectsEnabled": True,
                    "isAutostateEnabled": True,
                    "isDhcpEnabled": True,
                    "isIpV6AutoconfigEnabled": True,
                    "isIpV6DhcpEnabled": True,
                    "isIpV6Enabled": True,
                    "isProxyArpEnabled": True,
                    "isShutdownEnabled": True,
                    "ipV6LinkLocalAddress": "string",
                    "ipV6DhcpRelayLoopbackSrcInterface": 0,
                    "primaryAddress": "string",
                    "primaryMask": "string",
                    "description": "string",
                    "ipV4OutboundAclName": "string",
                    "ipV4InboundAclName": "string",
                    "ipV4Unnumbered": "string",
                    "ipV6DhcpRelayDestinationAddress": {
                        "configType": "string",
                        "items": [{"configType": "string", "ipV6Address": "string"}],
                    },
                    "ipV6DhcpRelayDestinationGlobal": {
                        "configType": "string",
                        "items": [{"configType": "string", "ipV6Address": "string"}],
                    },
                    "ipV6DhcpServer": {
                        "configType": "string",
                        "items": [{"configType": "string", "dhcpServerPool": "string"}],
                    },
                    "ipV6UnnumberedInterface": "string",
                    "trafficFilter": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "direction": "string",
                                "accessListName": "string",
                            }
                        ],
                    },
                    "isBfdIntervalEnabled": True,
                }
            ]
        },
        vrfConfig={
            "items": [
                {
                    "configType": "string",
                    "name": "string",
                    "description": "string",
                    "routeDistinguisher": "string",
                    "isIpV4AddressFamilyEnabled": True,
                    "isIpV6Enabled": True,
                    "routeTargetImport": {
                        "configType": "string",
                        "items": [{"configType": "string", "asnIp": "string"}],
                    },
                    "routeTargetExport": {
                        "configType": "string",
                        "items": [{"configType": "string", "asnIp": "string"}],
                    },
                    "ipV4ExportRouteTargetWithoutStitching": {
                        "configType": "string",
                        "items": [{"configType": "string", "asnIp": "string"}],
                    },
                    "ipV6ImportRouteTargetWithoutStitching": {
                        "configType": "string",
                        "items": [{"configType": "string", "asnIp": "string"}],
                    },
                    "ipV6ExportRouteTargetWithoutStitching": {
                        "configType": "string",
                        "items": [{"configType": "string", "asnIp": "string"}],
                    },
                    "ipV4ImportRouteTargetWithoutStitching": {
                        "configType": "string",
                        "items": [{"configType": "string", "asnIp": "string"}],
                    },
                }
            ]
        },
    )
    return endpoint_result


@pytest.mark.wired
def test_update_intended_layer3_configurations(api, validator):
    try:
        assert is_valid_update_intended_layer3_configurations(
            validator, update_intended_layer3_configurations(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_intended_layer3_configurations_default_val(api):
    endpoint_result = api.wired.update_intended_layer3_configurations(
        active_validation=True,
        bfdConfig=None,
        bfdTemplateSingleHopConfig=None,
        dhcpRelayConfig=None,
        feature="string",
        id="string",
        ipv4RoutesConfig=None,
        ipv4RoutingConfig=None,
        ipv4VrfConfig=None,
        ipv4VrfRoutesConfig=None,
        ipv6RoutesConfig=None,
        ipv6RoutingConfig=None,
        ipv6VrfRoutesConfig=None,
        loopbackConfig=None,
        payload=None,
        sviConfig=None,
        vrfConfig=None,
    )
    return endpoint_result


@pytest.mark.wired
def test_update_intended_layer3_configurations_default_val(api, validator):
    try:
        assert is_valid_update_intended_layer3_configurations(
            validator, update_intended_layer3_configurations_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_intended_layer3_configurations(json_schema_validate, obj):
    json_schema_validate("jsd_7117285bf8dd5f23a9a13ab8fde04c16_v3_2_3_0").validate(obj)
    return True


def get_intended_layer3_configurations(api):
    endpoint_result = api.wired.get_intended_layer3_configurations(
        feature="string", id="string", limit=0, offset=0
    )
    return endpoint_result


@pytest.mark.wired
def test_get_intended_layer3_configurations(api, validator):
    try:
        assert is_valid_get_intended_layer3_configurations(
            validator, get_intended_layer3_configurations(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_intended_layer3_configurations_default_val(api):
    endpoint_result = api.wired.get_intended_layer3_configurations(
        feature="string", id="string", limit=None, offset=None
    )
    return endpoint_result


@pytest.mark.wired
def test_get_intended_layer3_configurations_default_val(api, validator):
    try:
        assert is_valid_get_intended_layer3_configurations(
            validator, get_intended_layer3_configurations_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_intended_layer3_configurations(json_schema_validate, obj):
    json_schema_validate("jsd_eccb282c36ab52739f4bd3ea3a8217d9_v3_2_3_0").validate(obj)
    return True


def add_intended_layer3_configurations(api):
    endpoint_result = api.wired.add_intended_layer3_configurations(
        active_validation=True,
        bfdConfig={
            "items": [
                {"configType": "string", "ipV6L3Cos": 0, "isMoreSnmpTrapsEnabled": True}
            ]
        },
        bfdTemplateSingleHopConfig={
            "items": [
                {
                    "name": "string",
                    "configType": "string",
                    "isEchoEnabled": True,
                    "intervalMultiplier": 0,
                    "minRxInterval": 0,
                    "minTxInterval": 0,
                    "sha1AuthenticationKeychain": "string",
                }
            ]
        },
        dhcpRelayConfig={
            "items": [
                {
                    "configType": "string",
                    "isTrustAllEnabled": True,
                    "isVpnOptionEnabled": True,
                    "isDefaultOptionEnabled": True,
                }
            ]
        },
        feature="string",
        id="string",
        ipv4RoutesConfig={
            "items": [
                {
                    "configType": "string",
                    "forwardingList": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "nextHopFwd": "string",
                                "metric": 0,
                            }
                        ],
                    },
                    "mask": "string",
                    "prefix": "string",
                }
            ]
        },
        ipv4RoutingConfig={
            "items": [{"configType": "string", "isRoutingEnabled": True}]
        },
        ipv4VrfConfig={
            "items": [
                {
                    "configType": "string",
                    "name": "string",
                    "routeDistinguisher": "string",
                    "routeTarget": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "direction": "string",
                                "target": "string",
                            }
                        ],
                    },
                }
            ]
        },
        ipv4VrfRoutesConfig={
            "items": [
                {
                    "configType": "string",
                    "forwardingList": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "forwardingList": {
                                    "configType": "string",
                                    "items": [
                                        {
                                            "configType": "string",
                                            "interfaceNextHop": {
                                                "configType": "string",
                                                "items": [
                                                    {
                                                        "configType": "string",
                                                        "ipAddress": "string",
                                                    }
                                                ],
                                            },
                                            "nextHopFwd": "string",
                                        }
                                    ],
                                },
                                "mask": "string",
                                "prefix": "string",
                            }
                        ],
                    },
                    "vrfName": "string",
                }
            ]
        },
        ipv6RoutesConfig={
            "items": [
                {
                    "configType": "string",
                    "forwardingList": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "interfaceNextHop": {
                                    "configType": "string",
                                    "items": [
                                        {"configType": "string", "ipAddress": "string"}
                                    ],
                                },
                                "nextHopFwd": "string",
                            }
                        ],
                    },
                    "prefix": "string",
                }
            ]
        },
        ipv6RoutingConfig={
            "items": [{"configType": "string", "isUnicastRoutingEnabled": True}]
        },
        ipv6VrfRoutesConfig={
            "items": [
                {
                    "configType": "string",
                    "forwardingList": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "prefix": "string",
                                "forwardingList": {
                                    "configType": "string",
                                    "items": [
                                        {
                                            "configType": "string",
                                            "interfaceNextHop": {
                                                "configType": "string",
                                                "items": [
                                                    {
                                                        "configType": "string",
                                                        "ipAddress": "string",
                                                    }
                                                ],
                                            },
                                            "nextHopFwd": "string",
                                        }
                                    ],
                                },
                            }
                        ],
                    },
                    "vrfName": "string",
                }
            ]
        },
        loopbackConfig={
            "items": [
                {
                    "bfdTemplate": "string",
                    "configType": "string",
                    "bfdMinTxInterval": 0,
                    "bfdMinRxInterval": 0,
                    "bfdIntervalMultiplier": 0,
                    "isBfdEnabled": True,
                    "isDhcpRelayInfoTrusted": True,
                    "isProxyArpEnabled": True,
                    "isIpV6Enabled": True,
                    "isShutdownEnabled": True,
                    "isRedirectsEnabled": True,
                    "isIpV4UnreachablesEnabled": True,
                    "description": "string",
                    "loopbackNumber": 0,
                    "primaryMask": "string",
                    "primaryIpAddress": "string",
                    "vrfName": "string",
                    "ipVrfName": "string",
                    "isDhcpEnabled": True,
                    "isIpV6AutoconfigEnabled": True,
                    "secondaryAddresses": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "ipAddress": "string",
                                "mask": "string",
                            }
                        ],
                    },
                    "ipV6DhcpServerAddress": {
                        "configType": "string",
                        "items": [{"configType": "string", "dhcpServerPool": "string"}],
                    },
                    "ipV6LinkLocalAddress": "string",
                    "ipV6DhcpRelayDestination": {
                        "configType": "string",
                        "items": [{"configType": "string", "ipV6Address": "string"}],
                    },
                    "ipV6PrefixList": {
                        "configType": "string",
                        "items": [{"configType": "string", "ipV6Prefix": "string"}],
                    },
                    "isBfdIntervalEnabled": True,
                }
            ]
        },
        payload=None,
        sviConfig={
            "items": [
                {
                    "bfdTemplate": "string",
                    "configType": "string",
                    "dhcpRelaySourceInterface": "string",
                    "vrfName": "string",
                    "vlanId": 0,
                    "macAddress": "string",
                    "secondaryAddresses": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "ipAddress": "string",
                                "mask": "string",
                            }
                        ],
                    },
                    "dhcpClientId": "string",
                    "ipVrfName": "string",
                    "isIpV4UnreachablesEnabled": True,
                    "helperAddress": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "ipAddress": "string",
                                "vrfName": "string",
                            }
                        ],
                    },
                    "igmpVersion": 0,
                    "bfdMinTxInterval": 0,
                    "bfdMinRxInterval": 0,
                    "bfdIntervalMultiplier": 0,
                    "ipV6AddressPrefixList": {
                        "configType": "string",
                        "items": [{"configType": "string", "ipV6Prefix": "string"}],
                    },
                    "isBfdEnabled": True,
                    "isDhcpRelayInfoOptionVpnIdEnabled": True,
                    "isIpV6DhcpRelayOptionVpnEnabled": True,
                    "isIpV6RedirectsEnabled": True,
                    "isIpv6DhcpRelayTrustEnabled": True,
                    "isIpV6DhcpClientReqVendorEnabled": True,
                    "isRedirectsEnabled": True,
                    "isAutostateEnabled": True,
                    "isDhcpEnabled": True,
                    "isIpV6AutoconfigEnabled": True,
                    "isIpV6DhcpEnabled": True,
                    "isIpV6Enabled": True,
                    "isProxyArpEnabled": True,
                    "isShutdownEnabled": True,
                    "ipV6LinkLocalAddress": "string",
                    "ipV6DhcpRelayLoopbackSrcInterface": 0,
                    "primaryAddress": "string",
                    "primaryMask": "string",
                    "description": "string",
                    "ipV4OutboundAclName": "string",
                    "ipV4InboundAclName": "string",
                    "ipV4Unnumbered": "string",
                    "ipV6DhcpRelayDestinationAddress": {
                        "configType": "string",
                        "items": [{"configType": "string", "ipV6Address": "string"}],
                    },
                    "ipV6DhcpRelayDestinationGlobal": {
                        "configType": "string",
                        "items": [{"configType": "string", "ipV6Address": "string"}],
                    },
                    "ipV6DhcpServer": {
                        "configType": "string",
                        "items": [{"configType": "string", "dhcpServerPool": "string"}],
                    },
                    "ipV6UnnumberedInterface": "string",
                    "trafficFilter": {
                        "configType": "string",
                        "items": [
                            {
                                "configType": "string",
                                "direction": "string",
                                "accessListName": "string",
                            }
                        ],
                    },
                    "isBfdIntervalEnabled": True,
                }
            ]
        },
        vrfConfig={
            "items": [
                {
                    "configType": "string",
                    "name": "string",
                    "description": "string",
                    "routeDistinguisher": "string",
                    "isIpV4AddressFamilyEnabled": True,
                    "isIpV6Enabled": True,
                    "routeTargetImport": {
                        "configType": "string",
                        "items": [{"configType": "string", "asnIp": "string"}],
                    },
                    "routeTargetExport": {
                        "configType": "string",
                        "items": [{"configType": "string", "asnIp": "string"}],
                    },
                    "ipV4ExportRouteTargetWithoutStitching": {
                        "configType": "string",
                        "items": [{"configType": "string", "asnIp": "string"}],
                    },
                    "ipV6ImportRouteTargetWithoutStitching": {
                        "configType": "string",
                        "items": [{"configType": "string", "asnIp": "string"}],
                    },
                    "ipV6ExportRouteTargetWithoutStitching": {
                        "configType": "string",
                        "items": [{"configType": "string", "asnIp": "string"}],
                    },
                    "ipV4ImportRouteTargetWithoutStitching": {
                        "configType": "string",
                        "items": [{"configType": "string", "asnIp": "string"}],
                    },
                }
            ]
        },
    )
    return endpoint_result


@pytest.mark.wired
def test_add_intended_layer3_configurations(api, validator):
    try:
        assert is_valid_add_intended_layer3_configurations(
            validator, add_intended_layer3_configurations(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_intended_layer3_configurations_default_val(api):
    endpoint_result = api.wired.add_intended_layer3_configurations(
        active_validation=True,
        bfdConfig=None,
        bfdTemplateSingleHopConfig=None,
        dhcpRelayConfig=None,
        feature="string",
        id="string",
        ipv4RoutesConfig=None,
        ipv4RoutingConfig=None,
        ipv4VrfConfig=None,
        ipv4VrfRoutesConfig=None,
        ipv6RoutesConfig=None,
        ipv6RoutingConfig=None,
        ipv6VrfRoutesConfig=None,
        loopbackConfig=None,
        payload=None,
        sviConfig=None,
        vrfConfig=None,
    )
    return endpoint_result


@pytest.mark.wired
def test_add_intended_layer3_configurations_default_val(api, validator):
    try:
        assert is_valid_add_intended_layer3_configurations(
            validator, add_intended_layer3_configurations_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_intended_network_settings_config_count(json_schema_validate, obj):
    json_schema_validate("jsd_3aa604b7528954c0b504a4404fd7779f_v3_2_3_0").validate(obj)
    return True


def get_intended_network_settings_config_count(api):
    endpoint_result = api.wired.get_intended_network_settings_config_count(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_get_intended_network_settings_config_count(api, validator):
    try:
        assert is_valid_get_intended_network_settings_config_count(
            validator, get_intended_network_settings_config_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_intended_network_settings_config_count_default_val(api):
    endpoint_result = api.wired.get_intended_network_settings_config_count(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_get_intended_network_settings_config_count_default_val(api, validator):
    try:
        assert is_valid_get_intended_network_settings_config_count(
            validator, get_intended_network_settings_config_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_gets_the_device_config_for_the_configuration_model(
    json_schema_validate, obj
):
    json_schema_validate("jsd_9f7fdcd6e2dd5f4eaf7ceed5e5856ba2_v3_2_3_0").validate(obj)
    return True


def gets_the_device_config_for_the_configuration_model(api):
    endpoint_result = api.wired.gets_the_device_config_for_the_configuration_model(
        network_device_id="string", preview_activity_id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_gets_the_device_config_for_the_configuration_model(api, validator):
    try:
        assert is_valid_gets_the_device_config_for_the_configuration_model(
            validator, gets_the_device_config_for_the_configuration_model(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def gets_the_device_config_for_the_configuration_model_default_val(api):
    endpoint_result = api.wired.gets_the_device_config_for_the_configuration_model(
        network_device_id="string", preview_activity_id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_gets_the_device_config_for_the_configuration_model_default_val(api, validator):
    try:
        assert is_valid_gets_the_device_config_for_the_configuration_model(
            validator,
            gets_the_device_config_for_the_configuration_model_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_generate_the_device_config_for_the_configuration_model(
    json_schema_validate, obj
):
    json_schema_validate("jsd_e174c2cf0ecb5b52806a95a08477ae4d_v3_2_3_0").validate(obj)
    return True


def generate_the_device_config_for_the_configuration_model(api):
    endpoint_result = api.wired.generate_the_device_config_for_the_configuration_model(
        active_validation=True,
        network_device_id="string",
        payload=None,
        preview_activity_id="string",
    )
    return endpoint_result


@pytest.mark.wired
def test_generate_the_device_config_for_the_configuration_model(api, validator):
    try:
        assert is_valid_generate_the_device_config_for_the_configuration_model(
            validator, generate_the_device_config_for_the_configuration_model(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def generate_the_device_config_for_the_configuration_model_default_val(api):
    endpoint_result = api.wired.generate_the_device_config_for_the_configuration_model(
        active_validation=True,
        network_device_id="string",
        payload=None,
        preview_activity_id="string",
    )
    return endpoint_result


@pytest.mark.wired
def test_generate_the_device_config_for_the_configuration_model_default_val(
    api, validator
):
    try:
        assert is_valid_generate_the_device_config_for_the_configuration_model(
            validator,
            generate_the_device_config_for_the_configuration_model_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_the_configuration_model(json_schema_validate, obj):
    json_schema_validate("jsd_fec9a36b80305b5593608e369fa05b64_v3_2_3_0").validate(obj)
    return True


def delete_the_configuration_model(api):
    endpoint_result = api.wired.delete_the_configuration_model(
        network_device_id="string", preview_activity_id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_delete_the_configuration_model(api, validator):
    try:
        assert is_valid_delete_the_configuration_model(
            validator, delete_the_configuration_model(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_the_configuration_model_default_val(api):
    endpoint_result = api.wired.delete_the_configuration_model(
        network_device_id="string", preview_activity_id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_delete_the_configuration_model_default_val(api, validator):
    try:
        assert is_valid_delete_the_configuration_model(
            validator, delete_the_configuration_model_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deploy_the_intended_configuration_features(json_schema_validate, obj):
    json_schema_validate("jsd_25d366656fa65a608e81c4f823689229_v3_2_3_0").validate(obj)
    return True


def deploy_the_intended_configuration_features(api):
    endpoint_result = api.wired.deploy_the_intended_configuration_features(
        active_validation=True, id="string", payload=None
    )
    return endpoint_result


@pytest.mark.wired
def test_deploy_the_intended_configuration_features(api, validator):
    try:
        assert is_valid_deploy_the_intended_configuration_features(
            validator, deploy_the_intended_configuration_features(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deploy_the_intended_configuration_features_default_val(api):
    endpoint_result = api.wired.deploy_the_intended_configuration_features(
        active_validation=True, id="string", payload=None
    )
    return endpoint_result


@pytest.mark.wired
def test_deploy_the_intended_configuration_features_default_val(api, validator):
    try:
        assert is_valid_deploy_the_intended_configuration_features(
            validator, deploy_the_intended_configuration_features_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_a_configuration_model_for_the_intended_configs_for_a_wired_device(
    json_schema_validate, obj
):
    json_schema_validate("jsd_594c74d2bae55f85924002ddb92fe064_v3_2_3_0").validate(obj)
    return True


def create_a_configuration_model_for_the_intended_configs_for_a_wired_device(api):
    endpoint_result = api.wired.create_a_configuration_model_for_the_intended_configs_for_a_wired_device(
        active_validation=True, network_device_id="string", payload=None
    )
    return endpoint_result


@pytest.mark.wired
def test_create_a_configuration_model_for_the_intended_configs_for_a_wired_device(
    api, validator
):
    try:
        assert is_valid_create_a_configuration_model_for_the_intended_configs_for_a_wired_device(
            validator,
            create_a_configuration_model_for_the_intended_configs_for_a_wired_device(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_a_configuration_model_for_the_intended_configs_for_a_wired_device_default_val(
    api,
):
    endpoint_result = api.wired.create_a_configuration_model_for_the_intended_configs_for_a_wired_device(
        active_validation=True, network_device_id="string", payload=None
    )
    return endpoint_result


@pytest.mark.wired
def test_create_a_configuration_model_for_the_intended_configs_for_a_wired_device_default_val(
    api, validator
):
    try:
        assert is_valid_create_a_configuration_model_for_the_intended_configs_for_a_wired_device(
            validator,
            create_a_configuration_model_for_the_intended_configs_for_a_wired_device_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_number_of_configurations_for_a_deployed_layer2_feature_on_a_wired_device(
    json_schema_validate, obj
):
    json_schema_validate("jsd_e495979e25a6559394fbad6fcd4c495a_v3_2_3_0").validate(obj)
    return True


def get_number_of_configurations_for_a_deployed_layer2_feature_on_a_wired_device(api):
    endpoint_result = api.wired.get_number_of_configurations_for_a_deployed_layer2_feature_on_a_wired_device(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_get_number_of_configurations_for_a_deployed_layer2_feature_on_a_wired_device(
    api, validator
):
    try:
        assert is_valid_get_number_of_configurations_for_a_deployed_layer2_feature_on_a_wired_device(
            validator,
            get_number_of_configurations_for_a_deployed_layer2_feature_on_a_wired_device(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_number_of_configurations_for_a_deployed_layer2_feature_on_a_wired_device_default_val(
    api,
):
    endpoint_result = api.wired.get_number_of_configurations_for_a_deployed_layer2_feature_on_a_wired_device(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_get_number_of_configurations_for_a_deployed_layer2_feature_on_a_wired_device_default_val(
    api, validator
):
    try:
        assert is_valid_get_number_of_configurations_for_a_deployed_layer2_feature_on_a_wired_device(
            validator,
            get_number_of_configurations_for_a_deployed_layer2_feature_on_a_wired_device_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_configurations_for_a_deployed_layer2_feature_on_a_wired_device(
    json_schema_validate, obj
):
    json_schema_validate("jsd_8747fcf9673050079b4abedf3ffc9777_v3_2_3_0").validate(obj)
    return True


def get_configurations_for_a_deployed_layer2_feature_on_a_wired_device(api):
    endpoint_result = (
        api.wired.get_configurations_for_a_deployed_layer2_feature_on_a_wired_device(
            feature="string", id="string"
        )
    )
    return endpoint_result


@pytest.mark.wired
def test_get_configurations_for_a_deployed_layer2_feature_on_a_wired_device(
    api, validator
):
    try:
        assert (
            is_valid_get_configurations_for_a_deployed_layer2_feature_on_a_wired_device(
                validator,
                get_configurations_for_a_deployed_layer2_feature_on_a_wired_device(api),
            )
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_configurations_for_a_deployed_layer2_feature_on_a_wired_device_default_val(api):
    endpoint_result = (
        api.wired.get_configurations_for_a_deployed_layer2_feature_on_a_wired_device(
            feature="string", id="string"
        )
    )
    return endpoint_result


@pytest.mark.wired
def test_get_configurations_for_a_deployed_layer2_feature_on_a_wired_device_default_val(
    api, validator
):
    try:
        assert is_valid_get_configurations_for_a_deployed_layer2_feature_on_a_wired_device(
            validator,
            get_configurations_for_a_deployed_layer2_feature_on_a_wired_device_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_deployed_port_feature_instance_count(json_schema_validate, obj):
    json_schema_validate("jsd_b8d1033aa31e5e1d8d6aa481418898e1_v3_2_3_0").validate(obj)
    return True


def get_deployed_port_feature_instance_count(api):
    endpoint_result = api.wired.get_deployed_port_feature_instance_count(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_get_deployed_port_feature_instance_count(api, validator):
    try:
        assert is_valid_get_deployed_port_feature_instance_count(
            validator, get_deployed_port_feature_instance_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_deployed_port_feature_instance_count_default_val(api):
    endpoint_result = api.wired.get_deployed_port_feature_instance_count(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_get_deployed_port_feature_instance_count_default_val(api, validator):
    try:
        assert is_valid_get_deployed_port_feature_instance_count(
            validator, get_deployed_port_feature_instance_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deploy_the_intended_configuration_features_on_a_wired_device(
    json_schema_validate, obj
):
    json_schema_validate("jsd_1a21cb2b7ea258e197f22082301cd1cc_v3_2_3_0").validate(obj)
    return True


def deploy_the_intended_configuration_features_on_a_wired_device(api):
    endpoint_result = (
        api.wired.deploy_the_intended_configuration_features_on_a_wired_device(
            active_validation=True, network_device_id="string", payload=None
        )
    )
    return endpoint_result


@pytest.mark.wired
def test_deploy_the_intended_configuration_features_on_a_wired_device(api, validator):
    try:
        assert is_valid_deploy_the_intended_configuration_features_on_a_wired_device(
            validator, deploy_the_intended_configuration_features_on_a_wired_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deploy_the_intended_configuration_features_on_a_wired_device_default_val(api):
    endpoint_result = (
        api.wired.deploy_the_intended_configuration_features_on_a_wired_device(
            active_validation=True, network_device_id="string", payload=None
        )
    )
    return endpoint_result


@pytest.mark.wired
def test_deploy_the_intended_configuration_features_on_a_wired_device_default_val(
    api, validator
):
    try:
        assert is_valid_deploy_the_intended_configuration_features_on_a_wired_device(
            validator,
            deploy_the_intended_configuration_features_on_a_wired_device_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_disable_per_device_configuration_pdc_learning(json_schema_validate, obj):
    json_schema_validate("jsd_d91b7695ad79539e972a1a8fdbeff540_v3_2_3_0").validate(obj)
    return True


def disable_per_device_configuration_pdc_learning(api):
    endpoint_result = api.wired.disable_per_device_configuration_pdc_learning(
        active_validation=True, deviceUuids=["string"], payload=None
    )
    return endpoint_result


@pytest.mark.wired
def test_disable_per_device_configuration_pdc_learning(api, validator):
    try:
        assert is_valid_disable_per_device_configuration_pdc_learning(
            validator, disable_per_device_configuration_pdc_learning(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def disable_per_device_configuration_pdc_learning_default_val(api):
    endpoint_result = api.wired.disable_per_device_configuration_pdc_learning(
        active_validation=True, deviceUuids=None, payload=None
    )
    return endpoint_result


@pytest.mark.wired
def test_disable_per_device_configuration_pdc_learning_default_val(api, validator):
    try:
        assert is_valid_disable_per_device_configuration_pdc_learning(
            validator, disable_per_device_configuration_pdc_learning_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deploy_the_configuration_model_on_the_network_device(
    json_schema_validate, obj
):
    json_schema_validate("jsd_b6139c3f3ef15bcf9a42f5283a6aea64_v3_2_3_0").validate(obj)
    return True


def deploy_the_configuration_model_on_the_network_device(api):
    endpoint_result = api.wired.deploy_the_configuration_model_on_the_network_device(
        active_validation=True,
        network_device_id="string",
        payload=None,
        preview_activity_id="string",
    )
    return endpoint_result


@pytest.mark.wired
def test_deploy_the_configuration_model_on_the_network_device(api, validator):
    try:
        assert is_valid_deploy_the_configuration_model_on_the_network_device(
            validator, deploy_the_configuration_model_on_the_network_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deploy_the_configuration_model_on_the_network_device_default_val(api):
    endpoint_result = api.wired.deploy_the_configuration_model_on_the_network_device(
        active_validation=True,
        network_device_id="string",
        payload=None,
        preview_activity_id="string",
    )
    return endpoint_result


@pytest.mark.wired
def test_deploy_the_configuration_model_on_the_network_device_default_val(
    api, validator
):
    try:
        assert is_valid_deploy_the_configuration_model_on_the_network_device(
            validator,
            deploy_the_configuration_model_on_the_network_device_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_supported_port_features(json_schema_validate, obj):
    json_schema_validate("jsd_4e5947f60a1e566795feefce5becff4c_v3_2_3_0").validate(obj)
    return True


def get_supported_port_features(api):
    endpoint_result = api.wired.get_supported_port_features(id="string")
    return endpoint_result


@pytest.mark.wired
def test_get_supported_port_features(api, validator):
    try:
        assert is_valid_get_supported_port_features(
            validator, get_supported_port_features(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_supported_port_features_default_val(api):
    endpoint_result = api.wired.get_supported_port_features(id="string")
    return endpoint_result


@pytest.mark.wired
def test_get_supported_port_features_default_val(api, validator):
    try:
        assert is_valid_get_supported_port_features(
            validator, get_supported_port_features_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_convert_intended_port_configurations(json_schema_validate, obj):
    json_schema_validate("jsd_85a630e120285a259cdb78af3c35649a_v3_2_3_0").validate(obj)
    return True


def convert_intended_port_configurations(api):
    endpoint_result = api.wired.convert_intended_port_configurations(
        active_validation=True,
        id="string",
        names=["string"],
        payload=None,
        targetType="string",
    )
    return endpoint_result


@pytest.mark.wired
def test_convert_intended_port_configurations(api, validator):
    try:
        assert is_valid_convert_intended_port_configurations(
            validator, convert_intended_port_configurations(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def convert_intended_port_configurations_default_val(api):
    endpoint_result = api.wired.convert_intended_port_configurations(
        active_validation=True, id="string", names=None, payload=None, targetType=None
    )
    return endpoint_result


@pytest.mark.wired
def test_convert_intended_port_configurations_default_val(api, validator):
    try:
        assert is_valid_convert_intended_port_configurations(
            validator, convert_intended_port_configurations_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_supported_security_features(json_schema_validate, obj):
    json_schema_validate("jsd_d4df6c41e9ec531f97f8d0580898dce7_v3_2_3_0").validate(obj)
    return True


def get_supported_security_features(api):
    endpoint_result = api.wired.get_supported_security_features(id="string")
    return endpoint_result


@pytest.mark.wired
def test_get_supported_security_features(api, validator):
    try:
        assert is_valid_get_supported_security_features(
            validator, get_supported_security_features(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_supported_security_features_default_val(api):
    endpoint_result = api.wired.get_supported_security_features(id="string")
    return endpoint_result


@pytest.mark.wired
def test_get_supported_security_features_default_val(api, validator):
    try:
        assert is_valid_get_supported_security_features(
            validator, get_supported_security_features_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_configurations_for_intended_layer2_features_on_a_wired_device(
    json_schema_validate, obj
):
    json_schema_validate("jsd_350ecf0984975fb7af51796da58aca21_v3_2_3_0").validate(obj)
    return True


def update_configurations_for_intended_layer2_features_on_a_wired_device(api):
    endpoint_result = (
        api.wired.update_configurations_for_intended_layer2_features_on_a_wired_device(
            active_validation=True, id="string", payload=None
        )
    )
    return endpoint_result


@pytest.mark.wired
def test_update_configurations_for_intended_layer2_features_on_a_wired_device(
    api, validator
):
    try:
        assert is_valid_update_configurations_for_intended_layer2_features_on_a_wired_device(
            validator,
            update_configurations_for_intended_layer2_features_on_a_wired_device(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_configurations_for_intended_layer2_features_on_a_wired_device_default_val(
    api,
):
    endpoint_result = (
        api.wired.update_configurations_for_intended_layer2_features_on_a_wired_device(
            active_validation=True, id="string", payload=None
        )
    )
    return endpoint_result


@pytest.mark.wired
def test_update_configurations_for_intended_layer2_features_on_a_wired_device_default_val(
    api, validator
):
    try:
        assert is_valid_update_configurations_for_intended_layer2_features_on_a_wired_device(
            validator,
            update_configurations_for_intended_layer2_features_on_a_wired_device_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_configurations_for_intended_layer2_features_on_a_wired_device(
    json_schema_validate, obj
):
    json_schema_validate("jsd_0a862379cc525a79a01fc845fdda7d68_v3_2_3_0").validate(obj)
    return True


def create_configurations_for_intended_layer2_features_on_a_wired_device(api):
    endpoint_result = (
        api.wired.create_configurations_for_intended_layer2_features_on_a_wired_device(
            active_validation=True, id="string", payload=None
        )
    )
    return endpoint_result


@pytest.mark.wired
def test_create_configurations_for_intended_layer2_features_on_a_wired_device(
    api, validator
):
    try:
        assert is_valid_create_configurations_for_intended_layer2_features_on_a_wired_device(
            validator,
            create_configurations_for_intended_layer2_features_on_a_wired_device(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_configurations_for_intended_layer2_features_on_a_wired_device_default_val(
    api,
):
    endpoint_result = (
        api.wired.create_configurations_for_intended_layer2_features_on_a_wired_device(
            active_validation=True, id="string", payload=None
        )
    )
    return endpoint_result


@pytest.mark.wired
def test_create_configurations_for_intended_layer2_features_on_a_wired_device_default_val(
    api, validator
):
    try:
        assert is_valid_create_configurations_for_intended_layer2_features_on_a_wired_device(
            validator,
            create_configurations_for_intended_layer2_features_on_a_wired_device_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_configurations_for_intended_layer2_features_on_a_wired_device(
    json_schema_validate, obj
):
    json_schema_validate("jsd_5abd659088f65d24ac291d8f1cadcd06_v3_2_3_0").validate(obj)
    return True


def get_configurations_for_intended_layer2_features_on_a_wired_device(api):
    endpoint_result = (
        api.wired.get_configurations_for_intended_layer2_features_on_a_wired_device(
            feature="string", id="string"
        )
    )
    return endpoint_result


@pytest.mark.wired
def test_get_configurations_for_intended_layer2_features_on_a_wired_device(
    api, validator
):
    try:
        assert (
            is_valid_get_configurations_for_intended_layer2_features_on_a_wired_device(
                validator,
                get_configurations_for_intended_layer2_features_on_a_wired_device(api),
            )
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_configurations_for_intended_layer2_features_on_a_wired_device_default_val(api):
    endpoint_result = (
        api.wired.get_configurations_for_intended_layer2_features_on_a_wired_device(
            feature=None, id="string"
        )
    )
    return endpoint_result


@pytest.mark.wired
def test_get_configurations_for_intended_layer2_features_on_a_wired_device_default_val(
    api, validator
):
    try:
        assert is_valid_get_configurations_for_intended_layer2_features_on_a_wired_device(
            validator,
            get_configurations_for_intended_layer2_features_on_a_wired_device_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_service_deployment_status(json_schema_validate, obj):
    json_schema_validate("jsd_c16b9caed6045399a6e7744914195fee_v3_2_3_0").validate(obj)
    return True


def get_service_deployment_status(api):
    endpoint_result = api.wired.get_service_deployment_status(
        deploy_activity_id="string", network_device_id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_get_service_deployment_status(api, validator):
    try:
        assert is_valid_get_service_deployment_status(
            validator, get_service_deployment_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_service_deployment_status_default_val(api):
    endpoint_result = api.wired.get_service_deployment_status(
        deploy_activity_id="string", network_device_id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_get_service_deployment_status_default_val(api, validator):
    try:
        assert is_valid_get_service_deployment_status(
            validator, get_service_deployment_status_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_the_supported_layer2_features_on_a_wired_device(
    json_schema_validate, obj
):
    json_schema_validate("jsd_3c4684074beb50b1ae5e77141244ebbd_v3_2_3_0").validate(obj)
    return True


def get_the_supported_layer2_features_on_a_wired_device(api):
    endpoint_result = api.wired.get_the_supported_layer2_features_on_a_wired_device(
        id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_get_the_supported_layer2_features_on_a_wired_device(api, validator):
    try:
        assert is_valid_get_the_supported_layer2_features_on_a_wired_device(
            validator, get_the_supported_layer2_features_on_a_wired_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_the_supported_layer2_features_on_a_wired_device_default_val(api):
    endpoint_result = api.wired.get_the_supported_layer2_features_on_a_wired_device(
        id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_get_the_supported_layer2_features_on_a_wired_device_default_val(
    api, validator
):
    try:
        assert is_valid_get_the_supported_layer2_features_on_a_wired_device(
            validator,
            get_the_supported_layer2_features_on_a_wired_device_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_deployed_network_settings_config_count(json_schema_validate, obj):
    json_schema_validate("jsd_65e3ee13353b5cb0be7b2e82f0d54e09_v3_2_3_0").validate(obj)
    return True


def get_deployed_network_settings_config_count(api):
    endpoint_result = api.wired.get_deployed_network_settings_config_count(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_get_deployed_network_settings_config_count(api, validator):
    try:
        assert is_valid_get_deployed_network_settings_config_count(
            validator, get_deployed_network_settings_config_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_deployed_network_settings_config_count_default_val(api):
    endpoint_result = api.wired.get_deployed_network_settings_config_count(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_get_deployed_network_settings_config_count_default_val(api, validator):
    try:
        assert is_valid_get_deployed_network_settings_config_count(
            validator, get_deployed_network_settings_config_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_deployed_layer2_config_count(json_schema_validate, obj):
    json_schema_validate("jsd_1846daa0c0905ad8bd3a2fbfd68448a4_v3_2_3_0").validate(obj)
    return True


def get_deployed_layer2_config_count(api):
    endpoint_result = api.wired.get_deployed_layer2_config_count(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_get_deployed_layer2_config_count(api, validator):
    try:
        assert is_valid_get_deployed_layer2_config_count(
            validator, get_deployed_layer2_config_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_deployed_layer2_config_count_default_val(api):
    endpoint_result = api.wired.get_deployed_layer2_config_count(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_get_deployed_layer2_config_count_default_val(api, validator):
    try:
        assert is_valid_get_deployed_layer2_config_count(
            validator, get_deployed_layer2_config_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_deployed_layer3_configurations(json_schema_validate, obj):
    json_schema_validate("jsd_737745f2343f549db494389fc73a8d48_v3_2_3_0").validate(obj)
    return True


def get_deployed_layer3_configurations(api):
    endpoint_result = api.wired.get_deployed_layer3_configurations(
        feature="string", id="string", limit=0, offset=0
    )
    return endpoint_result


@pytest.mark.wired
def test_get_deployed_layer3_configurations(api, validator):
    try:
        assert is_valid_get_deployed_layer3_configurations(
            validator, get_deployed_layer3_configurations(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_deployed_layer3_configurations_default_val(api):
    endpoint_result = api.wired.get_deployed_layer3_configurations(
        feature="string", id="string", limit=None, offset=None
    )
    return endpoint_result


@pytest.mark.wired
def test_get_deployed_layer3_configurations_default_val(api, validator):
    try:
        assert is_valid_get_deployed_layer3_configurations(
            validator, get_deployed_layer3_configurations_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_intended_layer3_config_count(json_schema_validate, obj):
    json_schema_validate("jsd_fa845293f2805099859bb684316d71fc_v3_2_3_0").validate(obj)
    return True


def get_intended_layer3_config_count(api):
    endpoint_result = api.wired.get_intended_layer3_config_count(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_get_intended_layer3_config_count(api, validator):
    try:
        assert is_valid_get_intended_layer3_config_count(
            validator, get_intended_layer3_config_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_intended_layer3_config_count_default_val(api):
    endpoint_result = api.wired.get_intended_layer3_config_count(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_get_intended_layer3_config_count_default_val(api, validator):
    try:
        assert is_valid_get_intended_layer3_config_count(
            validator, get_intended_layer3_config_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_supported_layer3_features(json_schema_validate, obj):
    json_schema_validate("jsd_66c600f5f874530b858d685efd8d4616_v3_2_3_0").validate(obj)
    return True


def get_supported_layer3_features(api):
    endpoint_result = api.wired.get_supported_layer3_features(id="string")
    return endpoint_result


@pytest.mark.wired
def test_get_supported_layer3_features(api, validator):
    try:
        assert is_valid_get_supported_layer3_features(
            validator, get_supported_layer3_features(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_supported_layer3_features_default_val(api):
    endpoint_result = api.wired.get_supported_layer3_features(id="string")
    return endpoint_result


@pytest.mark.wired
def test_get_supported_layer3_features_default_val(api, validator):
    try:
        assert is_valid_get_supported_layer3_features(
            validator, get_supported_layer3_features_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_supported_layer2_features(json_schema_validate, obj):
    json_schema_validate("jsd_7e1acc92f0af531182536c3633f6d173_v3_2_3_0").validate(obj)
    return True


def get_supported_layer2_features(api):
    endpoint_result = api.wired.get_supported_layer2_features(id="string")
    return endpoint_result


@pytest.mark.wired
def test_get_supported_layer2_features(api, validator):
    try:
        assert is_valid_get_supported_layer2_features(
            validator, get_supported_layer2_features(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_supported_layer2_features_default_val(api):
    endpoint_result = api.wired.get_supported_layer2_features(id="string")
    return endpoint_result


@pytest.mark.wired
def test_get_supported_layer2_features_default_val(api, validator):
    try:
        assert is_valid_get_supported_layer2_features(
            validator, get_supported_layer2_features_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_validate_intended_features(json_schema_validate, obj):
    json_schema_validate("jsd_12b93f1847c85ce9ad5480c4f8cc0e23_v3_2_3_0").validate(obj)
    return True


def validate_intended_features(api):
    endpoint_result = api.wired.validate_intended_features(
        active_validation=True, id="string", payload=None
    )
    return endpoint_result


@pytest.mark.wired
def test_validate_intended_features(api, validator):
    try:
        assert is_valid_validate_intended_features(
            validator, validate_intended_features(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def validate_intended_features_default_val(api):
    endpoint_result = api.wired.validate_intended_features(
        active_validation=True, id="string", payload=None
    )
    return endpoint_result


@pytest.mark.wired
def test_validate_intended_features_default_val(api, validator):
    try:
        assert is_valid_validate_intended_features(
            validator, validate_intended_features_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_enable_per_device_configuration_pdc_learning(json_schema_validate, obj):
    json_schema_validate("jsd_d3c8d365418a51eaa103bf075f2634f3_v3_2_3_0").validate(obj)
    return True


def enable_per_device_configuration_pdc_learning(api):
    endpoint_result = api.wired.enable_per_device_configuration_pdc_learning(
        active_validation=True, deviceUuids=["string"], payload=None
    )
    return endpoint_result


@pytest.mark.wired
def test_enable_per_device_configuration_pdc_learning(api, validator):
    try:
        assert is_valid_enable_per_device_configuration_pdc_learning(
            validator, enable_per_device_configuration_pdc_learning(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def enable_per_device_configuration_pdc_learning_default_val(api):
    endpoint_result = api.wired.enable_per_device_configuration_pdc_learning(
        active_validation=True, deviceUuids=None, payload=None
    )
    return endpoint_result


@pytest.mark.wired
def test_enable_per_device_configuration_pdc_learning_default_val(api, validator):
    try:
        assert is_valid_enable_per_device_configuration_pdc_learning(
            validator, enable_per_device_configuration_pdc_learning_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_intended_layer2_config_count(json_schema_validate, obj):
    json_schema_validate("jsd_c06558f426465eaabe216f8960eb0496_v3_2_3_0").validate(obj)
    return True


def get_intended_layer2_config_count(api):
    endpoint_result = api.wired.get_intended_layer2_config_count(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_get_intended_layer2_config_count(api, validator):
    try:
        assert is_valid_get_intended_layer2_config_count(
            validator, get_intended_layer2_config_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_intended_layer2_config_count_default_val(api):
    endpoint_result = api.wired.get_intended_layer2_config_count(
        feature="string", id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_get_intended_layer2_config_count_default_val(api, validator):
    try:
        assert is_valid_get_intended_layer2_config_count(
            validator, get_intended_layer2_config_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_deployed_layer2_configurations(json_schema_validate, obj):
    json_schema_validate("jsd_b5e8d2fbd8dc5094a82f37c49ebc4a9d_v3_2_3_0").validate(obj)
    return True


def get_deployed_layer2_configurations(api):
    endpoint_result = api.wired.get_deployed_layer2_configurations(
        feature="string", id="string", limit=0, offset=0
    )
    return endpoint_result


@pytest.mark.wired
def test_get_deployed_layer2_configurations(api, validator):
    try:
        assert is_valid_get_deployed_layer2_configurations(
            validator, get_deployed_layer2_configurations(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_deployed_layer2_configurations_default_val(api):
    endpoint_result = api.wired.get_deployed_layer2_configurations(
        feature="string", id="string", limit=None, offset=None
    )
    return endpoint_result


@pytest.mark.wired
def test_get_deployed_layer2_configurations_default_val(api, validator):
    try:
        assert is_valid_get_deployed_layer2_configurations(
            validator, get_deployed_layer2_configurations_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_deployment_status_wired(json_schema_validate, obj):
    json_schema_validate("jsd_44be5246ea895b5b958caa2c67d6e389_v3_2_3_0").validate(obj)
    return True


def get_device_deployment_status_wired(api):
    endpoint_result = api.wired.get_device_deployment_status_wired(
        deploy_activity_id="string", network_device_id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_get_device_deployment_status_wired(api, validator):
    try:
        assert is_valid_get_device_deployment_status_wired(
            validator, get_device_deployment_status_wired(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_deployment_status_wired_default_val(api):
    endpoint_result = api.wired.get_device_deployment_status_wired(
        deploy_activity_id="string", network_device_id="string"
    )
    return endpoint_result


@pytest.mark.wired
def test_get_device_deployment_status_wired_default_val(api, validator):
    try:
        assert is_valid_get_device_deployment_status_wired(
            validator, get_device_deployment_status_wired_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
