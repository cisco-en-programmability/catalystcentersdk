"""CatalystCenterAPI system_settings API fixtures and tests.

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


def is_valid_delete_authentication_and_policy_server_access_configuration(
    json_schema_validate, obj
):
    json_schema_validate("jsd_3b5ce4c02a525aa98e49940d5aa006a7_v3_2_3_0").validate(obj)
    return True


def delete_authentication_and_policy_server_access_configuration(api):
    endpoint_result = api.system_settings.delete_authentication_and_policy_server_access_configuration(
        id="string"
    )
    return endpoint_result


@pytest.mark.system_settings
def test_delete_authentication_and_policy_server_access_configuration(api, validator):
    try:
        assert is_valid_delete_authentication_and_policy_server_access_configuration(
            validator, delete_authentication_and_policy_server_access_configuration(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_authentication_and_policy_server_access_configuration_default_val(api):
    endpoint_result = api.system_settings.delete_authentication_and_policy_server_access_configuration(
        id="string"
    )
    return endpoint_result


@pytest.mark.system_settings
def test_delete_authentication_and_policy_server_access_configuration_default_val(
    api, validator
):
    try:
        assert is_valid_delete_authentication_and_policy_server_access_configuration(
            validator,
            delete_authentication_and_policy_server_access_configuration_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_edit_authentication_and_policy_server_access_configuration(
    json_schema_validate, obj
):
    json_schema_validate("jsd_fbdd94fbecd256c08e1d9f6e1a7657ac_v3_2_3_0").validate(obj)
    return True


def edit_authentication_and_policy_server_access_configuration(api):
    endpoint_result = (
        api.system_settings.edit_authentication_and_policy_server_access_configuration(
            accountingPort=0,
            active_validation=True,
            authenticationPort=0,
            ciscoIseDtos=[
                {
                    "fqdn": "string",
                    "password": "string",
                    "sshkey": "string",
                    "userName": "string",
                }
            ],
            externalCiscoIseIpAddrDtos=[
                {
                    "externalCiscoIseIpAddresses": [{"externalIpAddress": "string"}],
                    "type": "string",
                }
            ],
            id="string",
            payload=None,
            port=0,
            protocol="string",
            pxgridEnabled=True,
            retries="string",
            timeoutSeconds="string",
            useDnacCertForPxgrid=True,
        )
    )
    return endpoint_result


@pytest.mark.system_settings
def test_edit_authentication_and_policy_server_access_configuration(api, validator):
    try:
        assert is_valid_edit_authentication_and_policy_server_access_configuration(
            validator, edit_authentication_and_policy_server_access_configuration(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def edit_authentication_and_policy_server_access_configuration_default_val(api):
    endpoint_result = (
        api.system_settings.edit_authentication_and_policy_server_access_configuration(
            accountingPort=None,
            active_validation=True,
            authenticationPort=None,
            ciscoIseDtos=None,
            externalCiscoIseIpAddrDtos=None,
            id="string",
            payload=None,
            port=None,
            protocol=None,
            pxgridEnabled=None,
            retries=None,
            timeoutSeconds=None,
            useDnacCertForPxgrid=None,
        )
    )
    return endpoint_result


@pytest.mark.system_settings
def test_edit_authentication_and_policy_server_access_configuration_default_val(
    api, validator
):
    try:
        assert is_valid_edit_authentication_and_policy_server_access_configuration(
            validator,
            edit_authentication_and_policy_server_access_configuration_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_cisco_spaces_accounts(json_schema_validate, obj):
    json_schema_validate("jsd_c68d6309e8af527280ec7ee6d5fb3e5d_v3_2_3_0").validate(obj)
    return True


def retrieves_cisco_spaces_accounts(api):
    endpoint_result = api.system_settings.retrieves_cisco_spaces_accounts(
        limit=0, offset=0, order="string", region_name="string"
    )
    return endpoint_result


@pytest.mark.system_settings
def test_retrieves_cisco_spaces_accounts(api, validator):
    try:
        assert is_valid_retrieves_cisco_spaces_accounts(
            validator, retrieves_cisco_spaces_accounts(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_cisco_spaces_accounts_default_val(api):
    endpoint_result = api.system_settings.retrieves_cisco_spaces_accounts(
        limit=None, offset=None, order=None, region_name=None
    )
    return endpoint_result


@pytest.mark.system_settings
def test_retrieves_cisco_spaces_accounts_default_val(api, validator):
    try:
        assert is_valid_retrieves_cisco_spaces_accounts(
            validator, retrieves_cisco_spaces_accounts_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_custom_prompt_support_get_api(json_schema_validate, obj):
    json_schema_validate("jsd_ada20dc4915d5901b50634628392e79f_v3_2_3_0").validate(obj)
    return True


def custom_prompt_support_get_api(api):
    endpoint_result = api.system_settings.custom_prompt_support_get_api()
    return endpoint_result


@pytest.mark.system_settings
def test_custom_prompt_support_get_api(api, validator):
    try:
        assert is_valid_custom_prompt_support_get_api(
            validator, custom_prompt_support_get_api(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def custom_prompt_support_get_api_default_val(api):
    endpoint_result = api.system_settings.custom_prompt_support_get_api()
    return endpoint_result


@pytest.mark.system_settings
def test_custom_prompt_support_get_api_default_val(api, validator):
    try:
        assert is_valid_custom_prompt_support_get_api(
            validator, custom_prompt_support_get_api_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_custom_prompt_post_api(json_schema_validate, obj):
    json_schema_validate("jsd_d2ea814bfae85da1b77872d095fc8221_v3_2_3_0").validate(obj)
    return True


def custom_prompt_post_api(api):
    endpoint_result = api.system_settings.custom_prompt_post_api(
        active_validation=True,
        passwordPrompt="string",
        payload=None,
        usernamePrompt="string",
    )
    return endpoint_result


@pytest.mark.system_settings
def test_custom_prompt_post_api(api, validator):
    try:
        assert is_valid_custom_prompt_post_api(validator, custom_prompt_post_api(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def custom_prompt_post_api_default_val(api):
    endpoint_result = api.system_settings.custom_prompt_post_api(
        active_validation=True, passwordPrompt=None, payload=None, usernamePrompt=None
    )
    return endpoint_result


@pytest.mark.system_settings
def test_custom_prompt_post_api_default_val(api, validator):
    try:
        assert is_valid_custom_prompt_post_api(
            validator, custom_prompt_post_api_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_activates_with_cisco_spaces_using_token_authentication(
    json_schema_validate, obj
):
    json_schema_validate("jsd_b1e014b05ac15c878c0ca4d93babebd6_v3_2_3_0").validate(obj)
    return True


def activates_with_cisco_spaces_using_token_authentication(api):
    endpoint_result = (
        api.system_settings.activates_with_cisco_spaces_using_token_authentication(
            active_validation=True, oneTimeUseToken="string", payload=None
        )
    )
    return endpoint_result


@pytest.mark.system_settings
def test_activates_with_cisco_spaces_using_token_authentication(api, validator):
    try:
        assert is_valid_activates_with_cisco_spaces_using_token_authentication(
            validator, activates_with_cisco_spaces_using_token_authentication(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def activates_with_cisco_spaces_using_token_authentication_default_val(api):
    endpoint_result = (
        api.system_settings.activates_with_cisco_spaces_using_token_authentication(
            active_validation=True, oneTimeUseToken=None, payload=None
        )
    )
    return endpoint_result


@pytest.mark.system_settings
def test_activates_with_cisco_spaces_using_token_authentication_default_val(
    api, validator
):
    try:
        assert is_valid_activates_with_cisco_spaces_using_token_authentication(
            validator,
            activates_with_cisco_spaces_using_token_authentication_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_a_cmx_server_setting(json_schema_validate, obj):
    json_schema_validate("jsd_3cf5275474cb5580ba73bd64ba6244f3_v3_2_3_0").validate(obj)
    return True


def delete_a_cmx_server_setting(api):
    endpoint_result = api.system_settings.delete_a_cmx_server_setting(id="string")
    return endpoint_result


@pytest.mark.system_settings
def test_delete_a_cmx_server_setting(api, validator):
    try:
        assert is_valid_delete_a_cmx_server_setting(
            validator, delete_a_cmx_server_setting(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_a_cmx_server_setting_default_val(api):
    endpoint_result = api.system_settings.delete_a_cmx_server_setting(id="string")
    return endpoint_result


@pytest.mark.system_settings
def test_delete_a_cmx_server_setting_default_val(api, validator):
    try:
        assert is_valid_delete_a_cmx_server_setting(
            validator, delete_a_cmx_server_setting_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_updates_a_cmx_server_setting(json_schema_validate, obj):
    json_schema_validate("jsd_031e0fa184df58678ccbef5a68ed9d42_v3_2_3_0").validate(obj)
    return True


def updates_a_cmx_server_setting(api):
    endpoint_result = api.system_settings.updates_a_cmx_server_setting(
        active_validation=True,
        connectionAddress={},
        id="string",
        password="string",
        payload=None,
        username="string",
    )
    return endpoint_result


@pytest.mark.system_settings
def test_updates_a_cmx_server_setting(api, validator):
    try:
        assert is_valid_updates_a_cmx_server_setting(
            validator, updates_a_cmx_server_setting(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def updates_a_cmx_server_setting_default_val(api):
    endpoint_result = api.system_settings.updates_a_cmx_server_setting(
        active_validation=True,
        connectionAddress=None,
        id="string",
        password=None,
        payload=None,
        username=None,
    )
    return endpoint_result


@pytest.mark.system_settings
def test_updates_a_cmx_server_setting_default_val(api, validator):
    try:
        assert is_valid_updates_a_cmx_server_setting(
            validator, updates_a_cmx_server_setting_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_gets_a_cmx_server_setting(json_schema_validate, obj):
    json_schema_validate("jsd_ce47319bdcff5f7c9eeac6524f865900_v3_2_3_0").validate(obj)
    return True


def gets_a_cmx_server_setting(api):
    endpoint_result = api.system_settings.gets_a_cmx_server_setting(id="string")
    return endpoint_result


@pytest.mark.system_settings
def test_gets_a_cmx_server_setting(api, validator):
    try:
        assert is_valid_gets_a_cmx_server_setting(
            validator, gets_a_cmx_server_setting(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def gets_a_cmx_server_setting_default_val(api):
    endpoint_result = api.system_settings.gets_a_cmx_server_setting(id="string")
    return endpoint_result


@pytest.mark.system_settings
def test_gets_a_cmx_server_setting_default_val(api, validator):
    try:
        assert is_valid_gets_a_cmx_server_setting(
            validator, gets_a_cmx_server_setting_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_authentication_and_policy_server_access_configuration(
    json_schema_validate, obj
):
    json_schema_validate("jsd_fa3975be5af25501abb40339d96917eb_v3_2_3_0").validate(obj)
    return True


def add_authentication_and_policy_server_access_configuration(api):
    endpoint_result = (
        api.system_settings.add_authentication_and_policy_server_access_configuration(
            accountingPort=0,
            active_validation=True,
            authenticationPort=0,
            ciscoIseDtos=[
                {
                    "description": "string",
                    "fqdn": "string",
                    "password": "string",
                    "sshkey": "string",
                    "ipAddress": "string",
                    "subscriberName": "string",
                    "userName": "string",
                }
            ],
            encryptionKey="string",
            encryptionScheme="string",
            externalCiscoIseIpAddrDtos=[
                {
                    "externalCiscoIseIpAddresses": [{"externalIpAddress": "string"}],
                    "type": "string",
                }
            ],
            ipAddress="string",
            isIseEnabled=True,
            messageKey="string",
            payload=None,
            port=0,
            protocol="string",
            pxgridEnabled=True,
            retries="string",
            role="string",
            sharedSecret="string",
            timeoutSeconds="string",
            useDnacCertForPxgrid=True,
        )
    )
    return endpoint_result


@pytest.mark.system_settings
def test_add_authentication_and_policy_server_access_configuration(api, validator):
    try:
        assert is_valid_add_authentication_and_policy_server_access_configuration(
            validator, add_authentication_and_policy_server_access_configuration(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def add_authentication_and_policy_server_access_configuration_default_val(api):
    endpoint_result = (
        api.system_settings.add_authentication_and_policy_server_access_configuration(
            accountingPort=None,
            active_validation=True,
            authenticationPort=None,
            ciscoIseDtos=None,
            encryptionKey=None,
            encryptionScheme=None,
            externalCiscoIseIpAddrDtos=None,
            ipAddress=None,
            isIseEnabled=None,
            messageKey=None,
            payload=None,
            port=None,
            protocol=None,
            pxgridEnabled=None,
            retries=None,
            role=None,
            sharedSecret=None,
            timeoutSeconds=None,
            useDnacCertForPxgrid=None,
        )
    )
    return endpoint_result


@pytest.mark.system_settings
def test_add_authentication_and_policy_server_access_configuration_default_val(
    api, validator
):
    try:
        assert is_valid_add_authentication_and_policy_server_access_configuration(
            validator,
            add_authentication_and_policy_server_access_configuration_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_authentication_and_policy_servers(json_schema_validate, obj):
    json_schema_validate("jsd_f7cc2592721f5b9b9f99795a26130147_v3_2_3_0").validate(obj)
    return True


def get_authentication_and_policy_servers(api):
    endpoint_result = api.system_settings.get_authentication_and_policy_servers(
        is_ise_enabled=True, role="string", state="string"
    )
    return endpoint_result


@pytest.mark.system_settings
def test_get_authentication_and_policy_servers(api, validator):
    try:
        assert is_valid_get_authentication_and_policy_servers(
            validator, get_authentication_and_policy_servers(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_authentication_and_policy_servers_default_val(api):
    endpoint_result = api.system_settings.get_authentication_and_policy_servers(
        is_ise_enabled=None, role=None, state=None
    )
    return endpoint_result


@pytest.mark.system_settings
def test_get_authentication_and_policy_servers_default_val(api, validator):
    try:
        assert is_valid_get_authentication_and_policy_servers(
            validator, get_authentication_and_policy_servers_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_provisioning_settings(json_schema_validate, obj):
    json_schema_validate("jsd_b2e5d0e7f80b555f865bb1f72c4d7bdd_v3_2_3_0").validate(obj)
    return True


def get_provisioning_settings(api):
    endpoint_result = api.system_settings.get_provisioning_settings()
    return endpoint_result


@pytest.mark.system_settings
def test_get_provisioning_settings(api, validator):
    try:
        assert is_valid_get_provisioning_settings(
            validator, get_provisioning_settings(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_provisioning_settings_default_val(api):
    endpoint_result = api.system_settings.get_provisioning_settings()
    return endpoint_result


@pytest.mark.system_settings
def test_get_provisioning_settings_default_val(api, validator):
    try:
        assert is_valid_get_provisioning_settings(
            validator, get_provisioning_settings_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_set_provisioning_settings(json_schema_validate, obj):
    json_schema_validate("jsd_b3ab480a3f485ecc9fef1bd2f8c9d109_v3_2_3_0").validate(obj)
    return True


def set_provisioning_settings(api):
    endpoint_result = api.system_settings.set_provisioning_settings(
        active_validation=True,
        payload=None,
        requireItsmApproval=True,
        requirePreview=True,
    )
    return endpoint_result


@pytest.mark.system_settings
def test_set_provisioning_settings(api, validator):
    try:
        assert is_valid_set_provisioning_settings(
            validator, set_provisioning_settings(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def set_provisioning_settings_default_val(api):
    endpoint_result = api.system_settings.set_provisioning_settings(
        active_validation=True,
        payload=None,
        requireItsmApproval=None,
        requirePreview=None,
    )
    return endpoint_result


@pytest.mark.system_settings
def test_set_provisioning_settings_default_val(api, validator):
    try:
        assert is_valid_set_provisioning_settings(
            validator, set_provisioning_settings_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_counts_cisco_spaces_accounts(json_schema_validate, obj):
    json_schema_validate("jsd_8aded9fcbdfb53a69ce3f93861851459_v3_2_3_0").validate(obj)
    return True


def counts_cisco_spaces_accounts(api):
    endpoint_result = api.system_settings.counts_cisco_spaces_accounts(
        region_name="string"
    )
    return endpoint_result


@pytest.mark.system_settings
def test_counts_cisco_spaces_accounts(api, validator):
    try:
        assert is_valid_counts_cisco_spaces_accounts(
            validator, counts_cisco_spaces_accounts(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def counts_cisco_spaces_accounts_default_val(api):
    endpoint_result = api.system_settings.counts_cisco_spaces_accounts(region_name=None)
    return endpoint_result


@pytest.mark.system_settings
def test_counts_cisco_spaces_accounts_default_val(api, validator):
    try:
        assert is_valid_counts_cisco_spaces_accounts(
            validator, counts_cisco_spaces_accounts_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_activates_existing_cisco_spaces_account_using_cisco_com_credentials(
    json_schema_validate, obj
):
    json_schema_validate("jsd_b41b600bf4ee50cea7277f3410ad5266_v3_2_3_0").validate(obj)
    return True


def activates_existing_cisco_spaces_account_using_cisco_com_credentials(api):
    endpoint_result = api.system_settings.activates_existing_cisco_spaces_account_using_cisco_com_credentials(
        accountName="string",
        active_validation=True,
        inviteAdminEmails=["string"],
        payload=None,
        region="string",
    )
    return endpoint_result


@pytest.mark.system_settings
def test_activates_existing_cisco_spaces_account_using_cisco_com_credentials(
    api, validator
):
    try:
        assert is_valid_activates_existing_cisco_spaces_account_using_cisco_com_credentials(
            validator,
            activates_existing_cisco_spaces_account_using_cisco_com_credentials(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def activates_existing_cisco_spaces_account_using_cisco_com_credentials_default_val(
    api,
):
    endpoint_result = api.system_settings.activates_existing_cisco_spaces_account_using_cisco_com_credentials(
        accountName=None,
        active_validation=True,
        inviteAdminEmails=None,
        payload=None,
        region=None,
    )
    return endpoint_result


@pytest.mark.system_settings
def test_activates_existing_cisco_spaces_account_using_cisco_com_credentials_default_val(
    api, validator
):
    try:
        assert is_valid_activates_existing_cisco_spaces_account_using_cisco_com_credentials(
            validator,
            activates_existing_cisco_spaces_account_using_cisco_com_credentials_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_cisco_ise_server_integration_status(json_schema_validate, obj):
    json_schema_validate("jsd_a1bc4f82533a5d909ed345b4703cff8a_v3_2_3_0").validate(obj)
    return True


def cisco_ise_server_integration_status(api):
    endpoint_result = api.system_settings.cisco_ise_server_integration_status()
    return endpoint_result


@pytest.mark.system_settings
def test_cisco_ise_server_integration_status(api, validator):
    try:
        assert is_valid_cisco_ise_server_integration_status(
            validator, cisco_ise_server_integration_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def cisco_ise_server_integration_status_default_val(api):
    endpoint_result = api.system_settings.cisco_ise_server_integration_status()
    return endpoint_result


@pytest.mark.system_settings
def test_cisco_ise_server_integration_status_default_val(api, validator):
    try:
        assert is_valid_cisco_ise_server_integration_status(
            validator, cisco_ise_server_integration_status_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_cmx_server_settings(json_schema_validate, obj):
    json_schema_validate("jsd_d451c0b1e0445fe3a458791df8e9d409_v3_2_3_0").validate(obj)
    return True


def retrieves_cmx_server_settings(api):
    endpoint_result = api.system_settings.retrieves_cmx_server_settings(
        connection_address="string", limit=0, offset=0, order="string"
    )
    return endpoint_result


@pytest.mark.system_settings
def test_retrieves_cmx_server_settings(api, validator):
    try:
        assert is_valid_retrieves_cmx_server_settings(
            validator, retrieves_cmx_server_settings(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_cmx_server_settings_default_val(api):
    endpoint_result = api.system_settings.retrieves_cmx_server_settings(
        connection_address=None, limit=None, offset=None, order=None
    )
    return endpoint_result


@pytest.mark.system_settings
def test_retrieves_cmx_server_settings_default_val(api, validator):
    try:
        assert is_valid_retrieves_cmx_server_settings(
            validator, retrieves_cmx_server_settings_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_creates_a_cmx_server_setting(json_schema_validate, obj):
    json_schema_validate("jsd_462fbefd8666583d81cba5dadd05b93f_v3_2_3_0").validate(obj)
    return True


def creates_a_cmx_server_setting(api):
    endpoint_result = api.system_settings.creates_a_cmx_server_setting(
        active_validation=True,
        connectionAddress={},
        id="string",
        password="string",
        payload=None,
        username="string",
    )
    return endpoint_result


@pytest.mark.system_settings
def test_creates_a_cmx_server_setting(api, validator):
    try:
        assert is_valid_creates_a_cmx_server_setting(
            validator, creates_a_cmx_server_setting(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def creates_a_cmx_server_setting_default_val(api):
    endpoint_result = api.system_settings.creates_a_cmx_server_setting(
        active_validation=True,
        connectionAddress=None,
        id=None,
        password=None,
        payload=None,
        username=None,
    )
    return endpoint_result


@pytest.mark.system_settings
def test_creates_a_cmx_server_setting_default_val(api, validator):
    try:
        assert is_valid_creates_a_cmx_server_setting(
            validator, creates_a_cmx_server_setting_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_counts_cmx_server_settings(json_schema_validate, obj):
    json_schema_validate("jsd_f015139af3c3555f8ecb15fec5c0cfc8_v3_2_3_0").validate(obj)
    return True


def counts_cmx_server_settings(api):
    endpoint_result = api.system_settings.counts_cmx_server_settings(
        connection_address="string", limit=0, offset=0, order="string"
    )
    return endpoint_result


@pytest.mark.system_settings
def test_counts_cmx_server_settings(api, validator):
    try:
        assert is_valid_counts_cmx_server_settings(
            validator, counts_cmx_server_settings(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def counts_cmx_server_settings_default_val(api):
    endpoint_result = api.system_settings.counts_cmx_server_settings(
        connection_address=None, limit=None, offset=None, order=None
    )
    return endpoint_result


@pytest.mark.system_settings
def test_counts_cmx_server_settings_default_val(api, validator):
    try:
        assert is_valid_counts_cmx_server_settings(
            validator, counts_cmx_server_settings_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_creates_configuration_details_of_the_external_ipam_server(
    json_schema_validate, obj
):
    json_schema_validate("jsd_9838825d6d7d5c8983c1d3c9815bfd35_v3_2_3_0").validate(obj)
    return True


def creates_configuration_details_of_the_external_ipam_server(api):
    endpoint_result = (
        api.system_settings.creates_configuration_details_of_the_external_ipam_server(
            active_validation=True,
            password="string",
            payload=None,
            provider={},
            serverName="string",
            serverUrl="string",
            state="string",
            syncView=True,
            userName="string",
            view="string",
        )
    )
    return endpoint_result


@pytest.mark.system_settings
def test_creates_configuration_details_of_the_external_ipam_server(api, validator):
    try:
        assert is_valid_creates_configuration_details_of_the_external_ipam_server(
            validator, creates_configuration_details_of_the_external_ipam_server(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def creates_configuration_details_of_the_external_ipam_server_default_val(api):
    endpoint_result = (
        api.system_settings.creates_configuration_details_of_the_external_ipam_server(
            active_validation=True,
            password=None,
            payload=None,
            provider=None,
            serverName=None,
            serverUrl=None,
            state=None,
            syncView=None,
            userName=None,
            view=None,
        )
    )
    return endpoint_result


@pytest.mark.system_settings
def test_creates_configuration_details_of_the_external_ipam_server_default_val(
    api, validator
):
    try:
        assert is_valid_creates_configuration_details_of_the_external_ipam_server(
            validator,
            creates_configuration_details_of_the_external_ipam_server_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_configuration_details_of_the_external_ipam_server(
    json_schema_validate, obj
):
    json_schema_validate("jsd_88f06b38c5915162acc31afbf33b843e_v3_2_3_0").validate(obj)
    return True


def retrieves_configuration_details_of_the_external_ipam_server(api):
    endpoint_result = (
        api.system_settings.retrieves_configuration_details_of_the_external_ipam_server()
    )
    return endpoint_result


@pytest.mark.system_settings
def test_retrieves_configuration_details_of_the_external_ipam_server(api, validator):
    try:
        assert is_valid_retrieves_configuration_details_of_the_external_ipam_server(
            validator, retrieves_configuration_details_of_the_external_ipam_server(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_configuration_details_of_the_external_ipam_server_default_val(api):
    endpoint_result = (
        api.system_settings.retrieves_configuration_details_of_the_external_ipam_server()
    )
    return endpoint_result


@pytest.mark.system_settings
def test_retrieves_configuration_details_of_the_external_ipam_server_default_val(
    api, validator
):
    try:
        assert is_valid_retrieves_configuration_details_of_the_external_ipam_server(
            validator,
            retrieves_configuration_details_of_the_external_ipam_server_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_updates_configuration_details_of_the_external_ipam_server(
    json_schema_validate, obj
):
    json_schema_validate("jsd_88ba98ed72975099b39dd2dc4cb65ed8_v3_2_3_0").validate(obj)
    return True


def updates_configuration_details_of_the_external_ipam_server(api):
    endpoint_result = (
        api.system_settings.updates_configuration_details_of_the_external_ipam_server(
            active_validation=True,
            password="string",
            payload=None,
            provider={},
            serverName="string",
            serverUrl="string",
            state="string",
            syncView=True,
            userName="string",
            view="string",
        )
    )
    return endpoint_result


@pytest.mark.system_settings
def test_updates_configuration_details_of_the_external_ipam_server(api, validator):
    try:
        assert is_valid_updates_configuration_details_of_the_external_ipam_server(
            validator, updates_configuration_details_of_the_external_ipam_server(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def updates_configuration_details_of_the_external_ipam_server_default_val(api):
    endpoint_result = (
        api.system_settings.updates_configuration_details_of_the_external_ipam_server(
            active_validation=True,
            password=None,
            payload=None,
            provider=None,
            serverName=None,
            serverUrl=None,
            state=None,
            syncView=None,
            userName=None,
            view=None,
        )
    )
    return endpoint_result


@pytest.mark.system_settings
def test_updates_configuration_details_of_the_external_ipam_server_default_val(
    api, validator
):
    try:
        assert is_valid_updates_configuration_details_of_the_external_ipam_server(
            validator,
            updates_configuration_details_of_the_external_ipam_server_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deletes_configuration_details_of_the_external_ipam_server(
    json_schema_validate, obj
):
    json_schema_validate("jsd_28f47e2181ce5957818a97f135a5eb9f_v3_2_3_0").validate(obj)
    return True


def deletes_configuration_details_of_the_external_ipam_server(api):
    endpoint_result = (
        api.system_settings.deletes_configuration_details_of_the_external_ipam_server()
    )
    return endpoint_result


@pytest.mark.system_settings
def test_deletes_configuration_details_of_the_external_ipam_server(api, validator):
    try:
        assert is_valid_deletes_configuration_details_of_the_external_ipam_server(
            validator, deletes_configuration_details_of_the_external_ipam_server(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deletes_configuration_details_of_the_external_ipam_server_default_val(api):
    endpoint_result = (
        api.system_settings.deletes_configuration_details_of_the_external_ipam_server()
    )
    return endpoint_result


@pytest.mark.system_settings
def test_deletes_configuration_details_of_the_external_ipam_server_default_val(
    api, validator
):
    try:
        assert is_valid_deletes_configuration_details_of_the_external_ipam_server(
            validator,
            deletes_configuration_details_of_the_external_ipam_server_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_creates_new_cisco_spaces_account_using_cisco_com_credentials(
    json_schema_validate, obj
):
    json_schema_validate("jsd_fa1905c13f0d5c54b5b854eaf94d8eda_v3_2_3_0").validate(obj)
    return True


def creates_new_cisco_spaces_account_using_cisco_com_credentials(api):
    endpoint_result = api.system_settings.creates_new_cisco_spaces_account_using_cisco_com_credentials(
        accountName="string",
        active_validation=True,
        inviteAdminEmails=["string"],
        payload=None,
        region="string",
    )
    return endpoint_result


@pytest.mark.system_settings
def test_creates_new_cisco_spaces_account_using_cisco_com_credentials(api, validator):
    try:
        assert is_valid_creates_new_cisco_spaces_account_using_cisco_com_credentials(
            validator, creates_new_cisco_spaces_account_using_cisco_com_credentials(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def creates_new_cisco_spaces_account_using_cisco_com_credentials_default_val(api):
    endpoint_result = api.system_settings.creates_new_cisco_spaces_account_using_cisco_com_credentials(
        accountName=None,
        active_validation=True,
        inviteAdminEmails=None,
        payload=None,
        region=None,
    )
    return endpoint_result


@pytest.mark.system_settings
def test_creates_new_cisco_spaces_account_using_cisco_com_credentials_default_val(
    api, validator
):
    try:
        assert is_valid_creates_new_cisco_spaces_account_using_cisco_com_credentials(
            validator,
            creates_new_cisco_spaces_account_using_cisco_com_credentials_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_cisco_spaces_regions(json_schema_validate, obj):
    json_schema_validate("jsd_c84c07b1411e51b1b26eb27ebff35a0f_v3_2_3_0").validate(obj)
    return True


def retrieves_cisco_spaces_regions(api):
    endpoint_result = api.system_settings.retrieves_cisco_spaces_regions(
        limit=0, offset=0, order="string"
    )
    return endpoint_result


@pytest.mark.system_settings
def test_retrieves_cisco_spaces_regions(api, validator):
    try:
        assert is_valid_retrieves_cisco_spaces_regions(
            validator, retrieves_cisco_spaces_regions(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_cisco_spaces_regions_default_val(api):
    endpoint_result = api.system_settings.retrieves_cisco_spaces_regions(
        limit=None, offset=None, order=None
    )
    return endpoint_result


@pytest.mark.system_settings
def test_retrieves_cisco_spaces_regions_default_val(api, validator):
    try:
        assert is_valid_retrieves_cisco_spaces_regions(
            validator, retrieves_cisco_spaces_regions_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_gets_a_cmx_server_ca_certificate(json_schema_validate, obj):
    json_schema_validate("jsd_492af7c1bebc571faa064106ebedb7f2_v3_2_3_0").validate(obj)
    return True


def gets_a_cmx_server_ca_certificate(api):
    endpoint_result = api.system_settings.gets_a_cmx_server_ca_certificate(
        connection_address="string"
    )
    return endpoint_result


@pytest.mark.system_settings
def test_gets_a_cmx_server_ca_certificate(api, validator):
    try:
        assert is_valid_gets_a_cmx_server_ca_certificate(
            validator, gets_a_cmx_server_ca_certificate(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def gets_a_cmx_server_ca_certificate_default_val(api):
    endpoint_result = api.system_settings.gets_a_cmx_server_ca_certificate(
        connection_address=None
    )
    return endpoint_result


@pytest.mark.system_settings
def test_gets_a_cmx_server_ca_certificate_default_val(api, validator):
    try:
        assert is_valid_gets_a_cmx_server_ca_certificate(
            validator, gets_a_cmx_server_ca_certificate_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_counts_cisco_spaces_regions(json_schema_validate, obj):
    json_schema_validate("jsd_90ca7a1f8c2154ffa55a7dd6e4cd1102_v3_2_3_0").validate(obj)
    return True


def counts_cisco_spaces_regions(api):
    endpoint_result = api.system_settings.counts_cisco_spaces_regions()
    return endpoint_result


@pytest.mark.system_settings
def test_counts_cisco_spaces_regions(api, validator):
    try:
        assert is_valid_counts_cisco_spaces_regions(
            validator, counts_cisco_spaces_regions(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def counts_cisco_spaces_regions_default_val(api):
    endpoint_result = api.system_settings.counts_cisco_spaces_regions()
    return endpoint_result


@pytest.mark.system_settings
def test_counts_cisco_spaces_regions_default_val(api, validator):
    try:
        assert is_valid_counts_cisco_spaces_regions(
            validator, counts_cisco_spaces_regions_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_cisco_spaces_settings(json_schema_validate, obj):
    json_schema_validate("jsd_4f96d291f9c05acab29b44ace7f870d0_v3_2_3_0").validate(obj)
    return True


def retrieves_cisco_spaces_settings(api):
    endpoint_result = api.system_settings.retrieves_cisco_spaces_settings()
    return endpoint_result


@pytest.mark.system_settings
def test_retrieves_cisco_spaces_settings(api, validator):
    try:
        assert is_valid_retrieves_cisco_spaces_settings(
            validator, retrieves_cisco_spaces_settings(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_cisco_spaces_settings_default_val(api):
    endpoint_result = api.system_settings.retrieves_cisco_spaces_settings()
    return endpoint_result


@pytest.mark.system_settings
def test_retrieves_cisco_spaces_settings_default_val(api, validator):
    try:
        assert is_valid_retrieves_cisco_spaces_settings(
            validator, retrieves_cisco_spaces_settings_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deletes_cisco_spaces_settings(json_schema_validate, obj):
    json_schema_validate("jsd_a0e604aa7ce3522db24cb3e5392f8cb0_v3_2_3_0").validate(obj)
    return True


def deletes_cisco_spaces_settings(api):
    endpoint_result = api.system_settings.deletes_cisco_spaces_settings()
    return endpoint_result


@pytest.mark.system_settings
def test_deletes_cisco_spaces_settings(api, validator):
    try:
        assert is_valid_deletes_cisco_spaces_settings(
            validator, deletes_cisco_spaces_settings(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deletes_cisco_spaces_settings_default_val(api):
    endpoint_result = api.system_settings.deletes_cisco_spaces_settings()
    return endpoint_result


@pytest.mark.system_settings
def test_deletes_cisco_spaces_settings_default_val(api, validator):
    try:
        assert is_valid_deletes_cisco_spaces_settings(
            validator, deletes_cisco_spaces_settings_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_accept_cisco_ise_server_certificate_for_cisco_ise_server_integration(
    json_schema_validate, obj
):
    json_schema_validate("jsd_4121e0ed6b9a530ea05d77a199ded4e3_v3_2_3_0").validate(obj)
    return True


def accept_cisco_ise_server_certificate_for_cisco_ise_server_integration(api):
    endpoint_result = api.system_settings.accept_cisco_ise_server_certificate_for_cisco_ise_server_integration(
        active_validation=True, id="string", isCertAcceptedByUser=True, payload=None
    )
    return endpoint_result


@pytest.mark.system_settings
def test_accept_cisco_ise_server_certificate_for_cisco_ise_server_integration(
    api, validator
):
    try:
        assert is_valid_accept_cisco_ise_server_certificate_for_cisco_ise_server_integration(
            validator,
            accept_cisco_ise_server_certificate_for_cisco_ise_server_integration(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def accept_cisco_ise_server_certificate_for_cisco_ise_server_integration_default_val(
    api,
):
    endpoint_result = api.system_settings.accept_cisco_ise_server_certificate_for_cisco_ise_server_integration(
        active_validation=True, id="string", isCertAcceptedByUser=None, payload=None
    )
    return endpoint_result


@pytest.mark.system_settings
def test_accept_cisco_ise_server_certificate_for_cisco_ise_server_integration_default_val(
    api, validator
):
    try:
        assert is_valid_accept_cisco_ise_server_certificate_for_cisco_ise_server_integration(
            validator,
            accept_cisco_ise_server_certificate_for_cisco_ise_server_integration_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
