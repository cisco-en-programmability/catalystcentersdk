"""CatalystCenterAPI industrial_configuration API fixtures and tests.

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


def is_valid_create_configuration_model_for_adding_prp_configuration(
    json_schema_validate, obj
):
    json_schema_validate("jsd_70b3075d19b55fd6a86994e01364c6dc_v3_2_3_0").validate(obj)
    return True


def create_configuration_model_for_adding_prp_configuration(api):
    endpoint_result = api.industrial_configuration.create_configuration_model_for_adding_prp_configuration(
        active_validation=True,
        activity_description="string",
        allowedVlans="string",
        channelNumber=0,
        description="string",
        interfaceNames=["string"],
        isPtpEnabled=True,
        isStpBpduFilter=True,
        isStpPortfastTrunk=True,
        lanBDeviceDetails={"networkDeviceId": "string", "interfaceName": "string"},
        networkDeviceId="string",
        payload=None,
        supervisionFrameOption={
            "vlanId": 0,
            "isVlanTagged": True,
            "isVlanAwareEnabled": True,
            "isVlanAwareRejectUntagged": True,
            "vlanAwareAllowedVlans": "string",
        },
        switchPortMode="string",
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_create_configuration_model_for_adding_prp_configuration(api, validator):
    try:
        assert is_valid_create_configuration_model_for_adding_prp_configuration(
            validator, create_configuration_model_for_adding_prp_configuration(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_configuration_model_for_adding_prp_configuration_default_val(api):
    endpoint_result = api.industrial_configuration.create_configuration_model_for_adding_prp_configuration(
        active_validation=True,
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
        payload=None,
        supervisionFrameOption=None,
        switchPortMode=None,
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_create_configuration_model_for_adding_prp_configuration_default_val(
    api, validator
):
    try:
        assert is_valid_create_configuration_model_for_adding_prp_configuration(
            validator,
            create_configuration_model_for_adding_prp_configuration_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_list_of_mrp_rings(json_schema_validate, obj):
    json_schema_validate("jsd_70ef907f6fb75c9187c6377b24549af5_v3_2_3_0").validate(obj)
    return True


def retrieves_the_list_of_mrp_rings(api):
    endpoint_result = api.industrial_configuration.retrieves_the_list_of_mrp_rings(
        id=0, limit=0, network_device_id="string", offset=0
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieves_the_list_of_mrp_rings(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_mrp_rings(
            validator, retrieves_the_list_of_mrp_rings(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_list_of_mrp_rings_default_val(api):
    endpoint_result = api.industrial_configuration.retrieves_the_list_of_mrp_rings(
        id=None, limit=None, network_device_id="string", offset=None
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieves_the_list_of_mrp_rings_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_mrp_rings(
            validator, retrieves_the_list_of_mrp_rings_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_configuration_model_for_deleting_prp_configuration(
    json_schema_validate, obj
):
    json_schema_validate("jsd_5cd1d97aed055c34a568c6d3e51f641a_v3_2_3_0").validate(obj)
    return True


def create_configuration_model_for_deleting_prp_configuration(api):
    endpoint_result = api.industrial_configuration.create_configuration_model_for_deleting_prp_configuration(
        active_validation=True,
        activity_description="string",
        interfaceName="string",
        networkDeviceId="string",
        payload=None,
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_create_configuration_model_for_deleting_prp_configuration(api, validator):
    try:
        assert is_valid_create_configuration_model_for_deleting_prp_configuration(
            validator, create_configuration_model_for_deleting_prp_configuration(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_configuration_model_for_deleting_prp_configuration_default_val(api):
    endpoint_result = api.industrial_configuration.create_configuration_model_for_deleting_prp_configuration(
        active_validation=True,
        activity_description=None,
        interfaceName=None,
        networkDeviceId=None,
        payload=None,
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_create_configuration_model_for_deleting_prp_configuration_default_val(
    api, validator
):
    try:
        assert is_valid_create_configuration_model_for_deleting_prp_configuration(
            validator,
            create_configuration_model_for_deleting_prp_configuration_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_configure_a_rep_ring_on_non_fabric_deployment(json_schema_validate, obj):
    json_schema_validate("jsd_bbc4dab8193c546ab116e19863dff621_v3_2_3_0").validate(obj)
    return True


def configure_a_rep_ring_on_non_fabric_deployment(api):
    endpoint_result = (
        api.industrial_configuration.configure_a_rep_ring_on_non_fabric_deployment(
            active_validation=True,
            deploymentMode="string",
            id="string",
            macsecConfig={
                "encryptionMode": "string",
                "accessControlMode": "string",
                "ciphersuite": "string",
                "keys": [
                    {
                        "id": 0,
                        "cryptoAlgo": "string",
                        "passPhrase": "string",
                        "startTime": "string",
                    }
                ],
            },
            networkDeviceId="string",
            payload=None,
            repSegmentId=0,
            repZtpMsg="string",
            ringMembers=[
                {
                    "networkDeviceId": "string",
                    "nodeName": "string",
                    "portName1": "string",
                    "portRepZtpStatus1": "string",
                    "portName2": "string",
                    "portRepZtpStatus2": "string",
                    "ringOrder": 0,
                }
            ],
            ringName="string",
            rootNeighbourNetworkDeviceIds=["string"],
            rootNetworkDeviceId="string",
            status="string",
        )
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_configure_a_rep_ring_on_non_fabric_deployment(api, validator):
    try:
        assert is_valid_configure_a_rep_ring_on_non_fabric_deployment(
            validator, configure_a_rep_ring_on_non_fabric_deployment(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def configure_a_rep_ring_on_non_fabric_deployment_default_val(api):
    endpoint_result = (
        api.industrial_configuration.configure_a_rep_ring_on_non_fabric_deployment(
            active_validation=True,
            deploymentMode=None,
            id=None,
            macsecConfig=None,
            networkDeviceId=None,
            payload=None,
            repSegmentId=None,
            repZtpMsg=None,
            ringMembers=None,
            ringName=None,
            rootNeighbourNetworkDeviceIds=None,
            rootNetworkDeviceId=None,
            status=None,
        )
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_configure_a_rep_ring_on_non_fabric_deployment_default_val(api, validator):
    try:
        assert is_valid_configure_a_rep_ring_on_non_fabric_deployment(
            validator, configure_a_rep_ring_on_non_fabric_deployment_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_a_configuration_model_for_performing_en_to_pen_upgrade(
    json_schema_validate, obj
):
    json_schema_validate("jsd_c69fd433ce0a5e3b86d1627f32ea3722_v3_2_3_0").validate(obj)
    return True


def create_a_configuration_model_for_performing_en_to_pen_upgrade(api):
    endpoint_result = api.industrial_configuration.create_a_configuration_model_for_performing_en_to_pen_upgrade(
        active_validation=True, networkDeviceId="string", payload=None
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_create_a_configuration_model_for_performing_en_to_pen_upgrade(api, validator):
    try:
        assert is_valid_create_a_configuration_model_for_performing_en_to_pen_upgrade(
            validator,
            create_a_configuration_model_for_performing_en_to_pen_upgrade(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_a_configuration_model_for_performing_en_to_pen_upgrade_default_val(api):
    endpoint_result = api.industrial_configuration.create_a_configuration_model_for_performing_en_to_pen_upgrade(
        active_validation=True, networkDeviceId=None, payload=None
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_create_a_configuration_model_for_performing_en_to_pen_upgrade_default_val(
    api, validator
):
    try:
        assert is_valid_create_a_configuration_model_for_performing_en_to_pen_upgrade(
            validator,
            create_a_configuration_model_for_performing_en_to_pen_upgrade_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_perform_en_to_pen_upgrade_without_generating_a_config_preview(
    json_schema_validate, obj
):
    json_schema_validate("jsd_1efd80bab13e5e1b927973e73b04300a_v3_2_3_0").validate(obj)
    return True


def perform_en_to_pen_upgrade_without_generating_a_config_preview(api):
    endpoint_result = api.industrial_configuration.perform_en_to_pen_upgrade_without_generating_a_config_preview(
        active_validation=True, networkDeviceId="string", payload=None
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_perform_en_to_pen_upgrade_without_generating_a_config_preview(api, validator):
    try:
        assert is_valid_perform_en_to_pen_upgrade_without_generating_a_config_preview(
            validator,
            perform_en_to_pen_upgrade_without_generating_a_config_preview(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def perform_en_to_pen_upgrade_without_generating_a_config_preview_default_val(api):
    endpoint_result = api.industrial_configuration.perform_en_to_pen_upgrade_without_generating_a_config_preview(
        active_validation=True, networkDeviceId=None, payload=None
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_perform_en_to_pen_upgrade_without_generating_a_config_preview_default_val(
    api, validator
):
    try:
        assert is_valid_perform_en_to_pen_upgrade_without_generating_a_config_preview(
            validator,
            perform_en_to_pen_upgrade_without_generating_a_config_preview_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_count_of_mrp_rings(json_schema_validate, obj):
    json_schema_validate("jsd_54f4d2ca417d50d7912fb8ea4a31662d_v3_2_3_0").validate(obj)
    return True


def retrieves_the_count_of_mrp_rings(api):
    endpoint_result = api.industrial_configuration.retrieves_the_count_of_mrp_rings(
        network_device_id="string"
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieves_the_count_of_mrp_rings(api, validator):
    try:
        assert is_valid_retrieves_the_count_of_mrp_rings(
            validator, retrieves_the_count_of_mrp_rings(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_count_of_mrp_rings_default_val(api):
    endpoint_result = api.industrial_configuration.retrieves_the_count_of_mrp_rings(
        network_device_id="string"
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieves_the_count_of_mrp_rings_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_count_of_mrp_rings(
            validator, retrieves_the_count_of_mrp_rings_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deploy_prp_configuration_without_generating_config_preview(
    json_schema_validate, obj
):
    json_schema_validate("jsd_f7bdc0b40fda5f378b9fef5b185fd92d_v3_2_3_0").validate(obj)
    return True


def deploy_prp_configuration_without_generating_config_preview(api):
    endpoint_result = api.industrial_configuration.deploy_prp_configuration_without_generating_config_preview(
        active_validation=True,
        activity_description="string",
        allowedVlans="string",
        channelNumber=0,
        description="string",
        interfaceNames=["string"],
        isPtpEnabled=True,
        isStpBpduFilter=True,
        isStpPortfastTrunk=True,
        lanBDeviceDetails={"networkDeviceId": "string", "interfaceName": "string"},
        networkDeviceId="string",
        payload=None,
        supervisionFrameOption={
            "vlanId": 0,
            "isVlanTagged": True,
            "isVlanAwareEnabled": True,
            "isVlanAwareRejectUntagged": True,
            "vlanAwareAllowedVlans": "string",
        },
        switchPortMode="string",
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_deploy_prp_configuration_without_generating_config_preview(api, validator):
    try:
        assert is_valid_deploy_prp_configuration_without_generating_config_preview(
            validator, deploy_prp_configuration_without_generating_config_preview(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deploy_prp_configuration_without_generating_config_preview_default_val(api):
    endpoint_result = api.industrial_configuration.deploy_prp_configuration_without_generating_config_preview(
        active_validation=True,
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
        payload=None,
        supervisionFrameOption=None,
        switchPortMode=None,
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_deploy_prp_configuration_without_generating_config_preview_default_val(
    api, validator
):
    try:
        assert is_valid_deploy_prp_configuration_without_generating_config_preview(
            validator,
            deploy_prp_configuration_without_generating_config_preview_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_prp_configuration_without_generating_config_preview(
    json_schema_validate, obj
):
    json_schema_validate("jsd_687853f44c345eaeb144e095610cc8e2_v3_2_3_0").validate(obj)
    return True


def update_prp_configuration_without_generating_config_preview(api):
    endpoint_result = api.industrial_configuration.update_prp_configuration_without_generating_config_preview(
        active_validation=True,
        activity_description="string",
        allowedVlans="string",
        networkDeviceId="string",
        payload=None,
        supervisionFrameOption={
            "vlanId": 0,
            "isVlanTagged": True,
            "isVlanAwareEnabled": True,
            "isVlanAwareRejectUntagged": True,
            "vlanAwareAllowedVlans": "string",
        },
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_update_prp_configuration_without_generating_config_preview(api, validator):
    try:
        assert is_valid_update_prp_configuration_without_generating_config_preview(
            validator, update_prp_configuration_without_generating_config_preview(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_prp_configuration_without_generating_config_preview_default_val(api):
    endpoint_result = api.industrial_configuration.update_prp_configuration_without_generating_config_preview(
        active_validation=True,
        activity_description=None,
        allowedVlans=None,
        networkDeviceId=None,
        payload=None,
        supervisionFrameOption=None,
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_update_prp_configuration_without_generating_config_preview_default_val(
    api, validator
):
    try:
        assert is_valid_update_prp_configuration_without_generating_config_preview(
            validator,
            update_prp_configuration_without_generating_config_preview_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_prp_configuration_without_generating_a_config_preview(
    json_schema_validate, obj
):
    json_schema_validate("jsd_ce4520dc1ca6557cba608f925ba58a08_v3_2_3_0").validate(obj)
    return True


def delete_prp_configuration_without_generating_a_config_preview(api):
    endpoint_result = api.industrial_configuration.delete_prp_configuration_without_generating_a_config_preview(
        activity_description="string",
        interface_name="string",
        network_device_id="string",
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_delete_prp_configuration_without_generating_a_config_preview(api, validator):
    try:
        assert is_valid_delete_prp_configuration_without_generating_a_config_preview(
            validator, delete_prp_configuration_without_generating_a_config_preview(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_prp_configuration_without_generating_a_config_preview_default_val(api):
    endpoint_result = api.industrial_configuration.delete_prp_configuration_without_generating_a_config_preview(
        activity_description=None, interface_name=None, network_device_id=None
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_delete_prp_configuration_without_generating_a_config_preview_default_val(
    api, validator
):
    try:
        assert is_valid_delete_prp_configuration_without_generating_a_config_preview(
            validator,
            delete_prp_configuration_without_generating_a_config_preview_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_generate_prp_configuration_for_the_given_network_device_and_prp_configuration_model(
    json_schema_validate, obj
):
    json_schema_validate("jsd_29ce4e7dde6c5f778337e1fd02f02e1a_v3_2_3_0").validate(obj)
    return True


def generate_prp_configuration_for_the_given_network_device_and_prp_configuration_model(
    api,
):
    endpoint_result = api.industrial_configuration.generate_prp_configuration_for_the_given_network_device_and_prp_configuration_model(
        active_validation=True,
        network_device_id="string",
        payload=None,
        preview_activity_id="string",
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_generate_prp_configuration_for_the_given_network_device_and_prp_configuration_model(
    api, validator
):
    try:
        assert is_valid_generate_prp_configuration_for_the_given_network_device_and_prp_configuration_model(
            validator,
            generate_prp_configuration_for_the_given_network_device_and_prp_configuration_model(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def generate_prp_configuration_for_the_given_network_device_and_prp_configuration_model_default_val(
    api,
):
    endpoint_result = api.industrial_configuration.generate_prp_configuration_for_the_given_network_device_and_prp_configuration_model(
        active_validation=True,
        network_device_id="string",
        payload=None,
        preview_activity_id="string",
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_generate_prp_configuration_for_the_given_network_device_and_prp_configuration_model_default_val(
    api, validator
):
    try:
        assert is_valid_generate_prp_configuration_for_the_given_network_device_and_prp_configuration_model(
            validator,
            generate_prp_configuration_for_the_given_network_device_and_prp_configuration_model_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_generated_prp_configuration_for_the_given_network_device_and_prp_configuration_model(
    json_schema_validate, obj
):
    json_schema_validate("jsd_ad98489d498a5c8e9a963a348df8634b_v3_2_3_0").validate(obj)
    return True


def retrieve_generated_prp_configuration_for_the_given_network_device_and_prp_configuration_model(
    api,
):
    endpoint_result = api.industrial_configuration.retrieve_generated_prp_configuration_for_the_given_network_device_and_prp_configuration_model(
        network_device_id="string", preview_activity_id="string"
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieve_generated_prp_configuration_for_the_given_network_device_and_prp_configuration_model(
    api, validator
):
    try:
        assert is_valid_retrieve_generated_prp_configuration_for_the_given_network_device_and_prp_configuration_model(
            validator,
            retrieve_generated_prp_configuration_for_the_given_network_device_and_prp_configuration_model(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_generated_prp_configuration_for_the_given_network_device_and_prp_configuration_model_default_val(
    api,
):
    endpoint_result = api.industrial_configuration.retrieve_generated_prp_configuration_for_the_given_network_device_and_prp_configuration_model(
        network_device_id="string", preview_activity_id="string"
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieve_generated_prp_configuration_for_the_given_network_device_and_prp_configuration_model_default_val(
    api, validator
):
    try:
        assert is_valid_retrieve_generated_prp_configuration_for_the_given_network_device_and_prp_configuration_model(
            validator,
            retrieve_generated_prp_configuration_for_the_given_network_device_and_prp_configuration_model_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_rep_ring_configured_in_the_non_fabric_deployment(
    json_schema_validate, obj
):
    json_schema_validate("jsd_4dcf9b8fecdd57f0bb7a33d358e6be37_v3_2_3_0").validate(obj)
    return True


def delete_rep_ring_configured_in_the_non_fabric_deployment(api):
    endpoint_result = api.industrial_configuration.delete_rep_ring_configured_in_the_non_fabric_deployment(
        force_delete=True, id="string"
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_delete_rep_ring_configured_in_the_non_fabric_deployment(api, validator):
    try:
        assert is_valid_delete_rep_ring_configured_in_the_non_fabric_deployment(
            validator, delete_rep_ring_configured_in_the_non_fabric_deployment(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_rep_ring_configured_in_the_non_fabric_deployment_default_val(api):
    endpoint_result = api.industrial_configuration.delete_rep_ring_configured_in_the_non_fabric_deployment(
        force_delete=None, id="string"
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_delete_rep_ring_configured_in_the_non_fabric_deployment_default_val(
    api, validator
):
    try:
        assert is_valid_delete_rep_ring_configured_in_the_non_fabric_deployment(
            validator,
            delete_rep_ring_configured_in_the_non_fabric_deployment_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_details_of_the_prp_topologies_configured(
    json_schema_validate, obj
):
    json_schema_validate("jsd_171a89ad22a95243a978ce374fd6b874_v3_2_3_0").validate(obj)
    return True


def retrieve_details_of_the_prp_topologies_configured(api):
    endpoint_result = (
        api.industrial_configuration.retrieve_details_of_the_prp_topologies_configured(
            limit=0, network_device_id="string", offset=0
        )
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieve_details_of_the_prp_topologies_configured(api, validator):
    try:
        assert is_valid_retrieve_details_of_the_prp_topologies_configured(
            validator, retrieve_details_of_the_prp_topologies_configured(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_details_of_the_prp_topologies_configured_default_val(api):
    endpoint_result = (
        api.industrial_configuration.retrieve_details_of_the_prp_topologies_configured(
            limit=None, network_device_id=None, offset=None
        )
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieve_details_of_the_prp_topologies_configured_default_val(api, validator):
    try:
        assert is_valid_retrieve_details_of_the_prp_topologies_configured(
            validator,
            retrieve_details_of_the_prp_topologies_configured_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_the_configuration_model_created_for_en_to_pen_upgrade(
    json_schema_validate, obj
):
    json_schema_validate("jsd_ff004631966055a2a9754de6ab56ef59_v3_2_3_0").validate(obj)
    return True


def delete_the_configuration_model_created_for_en_to_pen_upgrade(api):
    endpoint_result = api.industrial_configuration.delete_the_configuration_model_created_for_en_to_pen_upgrade(
        preview_activity_id="string"
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_delete_the_configuration_model_created_for_en_to_pen_upgrade(api, validator):
    try:
        assert is_valid_delete_the_configuration_model_created_for_en_to_pen_upgrade(
            validator, delete_the_configuration_model_created_for_en_to_pen_upgrade(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_the_configuration_model_created_for_en_to_pen_upgrade_default_val(api):
    endpoint_result = api.industrial_configuration.delete_the_configuration_model_created_for_en_to_pen_upgrade(
        preview_activity_id="string"
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_delete_the_configuration_model_created_for_en_to_pen_upgrade_default_val(
    api, validator
):
    try:
        assert is_valid_delete_the_configuration_model_created_for_en_to_pen_upgrade(
            validator,
            delete_the_configuration_model_created_for_en_to_pen_upgrade_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_the_rep_ring_based_on_the_ring_id(json_schema_validate, obj):
    json_schema_validate("jsd_98534ce1469c515d8a72455779e3a484_v3_2_3_0").validate(obj)
    return True


def get_the_rep_ring_based_on_the_ring_id(api):
    endpoint_result = (
        api.industrial_configuration.get_the_rep_ring_based_on_the_ring_id(id="string")
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_get_the_rep_ring_based_on_the_ring_id(api, validator):
    try:
        assert is_valid_get_the_rep_ring_based_on_the_ring_id(
            validator, get_the_rep_ring_based_on_the_ring_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_the_rep_ring_based_on_the_ring_id_default_val(api):
    endpoint_result = (
        api.industrial_configuration.get_the_rep_ring_based_on_the_ring_id(id="string")
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_get_the_rep_ring_based_on_the_ring_id_default_val(api, validator):
    try:
        assert is_valid_get_the_rep_ring_based_on_the_ring_id(
            validator, get_the_rep_ring_based_on_the_ring_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_total_count_of_prp_topologies(json_schema_validate, obj):
    json_schema_validate("jsd_b9d8e8fcb8f6533e9bbaf025b1d569b4_v3_2_3_0").validate(obj)
    return True


def retrieve_total_count_of_prp_topologies(api):
    endpoint_result = (
        api.industrial_configuration.retrieve_total_count_of_prp_topologies(
            network_device_id="string"
        )
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieve_total_count_of_prp_topologies(api, validator):
    try:
        assert is_valid_retrieve_total_count_of_prp_topologies(
            validator, retrieve_total_count_of_prp_topologies(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_total_count_of_prp_topologies_default_val(api):
    endpoint_result = (
        api.industrial_configuration.retrieve_total_count_of_prp_topologies(
            network_device_id=None
        )
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieve_total_count_of_prp_topologies_default_val(api, validator):
    try:
        assert is_valid_retrieve_total_count_of_prp_topologies(
            validator, retrieve_total_count_of_prp_topologies_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deploy_the_configuration_model_for_en_to_pen_upgrade_on_network_devices(
    json_schema_validate, obj
):
    json_schema_validate("jsd_0f8db82368e8549587fb1f9b5e96fdb2_v3_2_3_0").validate(obj)
    return True


def deploy_the_configuration_model_for_en_to_pen_upgrade_on_network_devices(api):
    endpoint_result = api.industrial_configuration.deploy_the_configuration_model_for_en_to_pen_upgrade_on_network_devices(
        active_validation=True, payload=None, preview_activity_id="string"
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_deploy_the_configuration_model_for_en_to_pen_upgrade_on_network_devices(
    api, validator
):
    try:
        assert is_valid_deploy_the_configuration_model_for_en_to_pen_upgrade_on_network_devices(
            validator,
            deploy_the_configuration_model_for_en_to_pen_upgrade_on_network_devices(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deploy_the_configuration_model_for_en_to_pen_upgrade_on_network_devices_default_val(
    api,
):
    endpoint_result = api.industrial_configuration.deploy_the_configuration_model_for_en_to_pen_upgrade_on_network_devices(
        active_validation=True, payload=None, preview_activity_id="string"
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_deploy_the_configuration_model_for_en_to_pen_upgrade_on_network_devices_default_val(
    api, validator
):
    try:
        assert is_valid_deploy_the_configuration_model_for_en_to_pen_upgrade_on_network_devices(
            validator,
            deploy_the_configuration_model_for_en_to_pen_upgrade_on_network_devices_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_config_of_network_device_for_en_to_pen_upgrade_configuration_model(
    json_schema_validate, obj
):
    json_schema_validate("jsd_4ef916e655545d8aac01b351ee8a7f0d_v3_2_3_0").validate(obj)
    return True


def retrieve_the_config_of_network_device_for_en_to_pen_upgrade_configuration_model(
    api,
):
    endpoint_result = api.industrial_configuration.retrieve_the_config_of_network_device_for_en_to_pen_upgrade_configuration_model(
        network_device_id="string", preview_activity_id="string"
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieve_the_config_of_network_device_for_en_to_pen_upgrade_configuration_model(
    api, validator
):
    try:
        assert is_valid_retrieve_the_config_of_network_device_for_en_to_pen_upgrade_configuration_model(
            validator,
            retrieve_the_config_of_network_device_for_en_to_pen_upgrade_configuration_model(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_config_of_network_device_for_en_to_pen_upgrade_configuration_model_default_val(
    api,
):
    endpoint_result = api.industrial_configuration.retrieve_the_config_of_network_device_for_en_to_pen_upgrade_configuration_model(
        network_device_id="string", preview_activity_id="string"
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieve_the_config_of_network_device_for_en_to_pen_upgrade_configuration_model_default_val(
    api, validator
):
    try:
        assert is_valid_retrieve_the_config_of_network_device_for_en_to_pen_upgrade_configuration_model(
            validator,
            retrieve_the_config_of_network_device_for_en_to_pen_upgrade_configuration_model_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_generate_the_config_of_network_device_for_en_to_pen_upgrade_configuration_model(
    json_schema_validate, obj
):
    json_schema_validate("jsd_f7c2678207695930a67fb326d09e13db_v3_2_3_0").validate(obj)
    return True


def generate_the_config_of_network_device_for_en_to_pen_upgrade_configuration_model(
    api,
):
    endpoint_result = api.industrial_configuration.generate_the_config_of_network_device_for_en_to_pen_upgrade_configuration_model(
        active_validation=True,
        network_device_id="string",
        payload=None,
        preview_activity_id="string",
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_generate_the_config_of_network_device_for_en_to_pen_upgrade_configuration_model(
    api, validator
):
    try:
        assert is_valid_generate_the_config_of_network_device_for_en_to_pen_upgrade_configuration_model(
            validator,
            generate_the_config_of_network_device_for_en_to_pen_upgrade_configuration_model(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def generate_the_config_of_network_device_for_en_to_pen_upgrade_configuration_model_default_val(
    api,
):
    endpoint_result = api.industrial_configuration.generate_the_config_of_network_device_for_en_to_pen_upgrade_configuration_model(
        active_validation=True,
        network_device_id="string",
        payload=None,
        preview_activity_id="string",
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_generate_the_config_of_network_device_for_en_to_pen_upgrade_configuration_model_default_val(
    api, validator
):
    try:
        assert is_valid_generate_the_config_of_network_device_for_en_to_pen_upgrade_configuration_model(
            validator,
            generate_the_config_of_network_device_for_en_to_pen_upgrade_configuration_model_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_aprp_configuration_model(json_schema_validate, obj):
    json_schema_validate("jsd_4a07eff6b9d8513f9313dca39c733d73_v3_2_3_0").validate(obj)
    return True


def delete_aprp_configuration_model(api):
    endpoint_result = api.industrial_configuration.delete_aprp_configuration_model(
        preview_activity_id="string"
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_delete_aprp_configuration_model(api, validator):
    try:
        assert is_valid_delete_aprp_configuration_model(
            validator, delete_aprp_configuration_model(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_aprp_configuration_model_default_val(api):
    endpoint_result = api.industrial_configuration.delete_aprp_configuration_model(
        preview_activity_id="string"
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_delete_aprp_configuration_model_default_val(api, validator):
    try:
        assert is_valid_delete_aprp_configuration_model(
            validator, delete_aprp_configuration_model_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_list_rep_rings(json_schema_validate, obj):
    json_schema_validate("jsd_5344fa2127b55124a3a00b2991b77db6_v3_2_3_0").validate(obj)
    return True


def retrieve_the_list_rep_rings(api):
    endpoint_result = api.industrial_configuration.retrieve_the_list_rep_rings(
        active_validation=True,
        deploymentMode="string",
        limit=0,
        networkDeviceId="string",
        offset=0,
        payload=None,
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieve_the_list_rep_rings(api, validator):
    try:
        assert is_valid_retrieve_the_list_rep_rings(
            validator, retrieve_the_list_rep_rings(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_list_rep_rings_default_val(api):
    endpoint_result = api.industrial_configuration.retrieve_the_list_rep_rings(
        active_validation=True,
        deploymentMode=None,
        limit=None,
        networkDeviceId=None,
        offset=None,
        payload=None,
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieve_the_list_rep_rings_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_list_rep_rings(
            validator, retrieve_the_list_rep_rings_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_configuration_model_generation_status_for_en_to_pen_upgrade(
    json_schema_validate, obj
):
    json_schema_validate("jsd_80af1303a4275fe4b3c028cb0933e813_v3_2_3_0").validate(obj)
    return True


def retrieve_configuration_model_generation_status_for_en_to_pen_upgrade(api):
    endpoint_result = api.industrial_configuration.retrieve_configuration_model_generation_status_for_en_to_pen_upgrade(
        preview_activity_id="string"
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieve_configuration_model_generation_status_for_en_to_pen_upgrade(
    api, validator
):
    try:
        assert is_valid_retrieve_configuration_model_generation_status_for_en_to_pen_upgrade(
            validator,
            retrieve_configuration_model_generation_status_for_en_to_pen_upgrade(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_configuration_model_generation_status_for_en_to_pen_upgrade_default_val(
    api,
):
    endpoint_result = api.industrial_configuration.retrieve_configuration_model_generation_status_for_en_to_pen_upgrade(
        preview_activity_id="string"
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieve_configuration_model_generation_status_for_en_to_pen_upgrade_default_val(
    api, validator
):
    try:
        assert is_valid_retrieve_configuration_model_generation_status_for_en_to_pen_upgrade(
            validator,
            retrieve_configuration_model_generation_status_for_en_to_pen_upgrade_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_configuration_model_for_updating_prp_configuration(
    json_schema_validate, obj
):
    json_schema_validate("jsd_b43efd6a99a55b27a83d6288f6ea0fb6_v3_2_3_0").validate(obj)
    return True


def create_configuration_model_for_updating_prp_configuration(api):
    endpoint_result = api.industrial_configuration.create_configuration_model_for_updating_prp_configuration(
        active_validation=True,
        activity_description="string",
        allowedVlans="string",
        networkDeviceId="string",
        payload=None,
        supervisionFrameOption={
            "vlanId": 0,
            "isVlanTagged": True,
            "isVlanAwareEnabled": True,
            "isVlanAwareRejectUntagged": True,
            "vlanAwareAllowedVlans": "string",
        },
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_create_configuration_model_for_updating_prp_configuration(api, validator):
    try:
        assert is_valid_create_configuration_model_for_updating_prp_configuration(
            validator, create_configuration_model_for_updating_prp_configuration(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_configuration_model_for_updating_prp_configuration_default_val(api):
    endpoint_result = api.industrial_configuration.create_configuration_model_for_updating_prp_configuration(
        active_validation=True,
        activity_description=None,
        allowedVlans=None,
        networkDeviceId=None,
        payload=None,
        supervisionFrameOption=None,
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_create_configuration_model_for_updating_prp_configuration_default_val(
    api, validator
):
    try:
        assert is_valid_create_configuration_model_for_updating_prp_configuration(
            validator,
            create_configuration_model_for_updating_prp_configuration_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_count_of_mrp_ring_members(json_schema_validate, obj):
    json_schema_validate("jsd_35bc1b3345f259e9859ac21a1ec694fe_v3_2_3_0").validate(obj)
    return True


def retrieves_the_count_of_mrp_ring_members(api):
    endpoint_result = (
        api.industrial_configuration.retrieves_the_count_of_mrp_ring_members(
            id=0, network_device_id="string"
        )
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieves_the_count_of_mrp_ring_members(api, validator):
    try:
        assert is_valid_retrieves_the_count_of_mrp_ring_members(
            validator, retrieves_the_count_of_mrp_ring_members(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_count_of_mrp_ring_members_default_val(api):
    endpoint_result = (
        api.industrial_configuration.retrieves_the_count_of_mrp_ring_members(
            id=0, network_device_id="string"
        )
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieves_the_count_of_mrp_ring_members_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_count_of_mrp_ring_members(
            validator, retrieves_the_count_of_mrp_ring_members_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_list_of_network_devices_part_of_mrp_ring(
    json_schema_validate, obj
):
    json_schema_validate("jsd_bf87f6cb9efb5451b84253593e548f98_v3_2_3_0").validate(obj)
    return True


def retrieves_the_list_of_network_devices_part_of_mrp_ring(api):
    endpoint_result = api.industrial_configuration.retrieves_the_list_of_network_devices_part_of_mrp_ring(
        id=0, limit=0, network_device_id="string", offset=0
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieves_the_list_of_network_devices_part_of_mrp_ring(api, validator):
    try:
        assert is_valid_retrieves_the_list_of_network_devices_part_of_mrp_ring(
            validator, retrieves_the_list_of_network_devices_part_of_mrp_ring(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_list_of_network_devices_part_of_mrp_ring_default_val(api):
    endpoint_result = api.industrial_configuration.retrieves_the_list_of_network_devices_part_of_mrp_ring(
        id=0, limit=None, network_device_id="string", offset=None
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieves_the_list_of_network_devices_part_of_mrp_ring_default_val(
    api, validator
):
    try:
        assert is_valid_retrieves_the_list_of_network_devices_part_of_mrp_ring(
            validator,
            retrieves_the_list_of_network_devices_part_of_mrp_ring_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_configure_a_rep_ring_on_fabric_deployment(json_schema_validate, obj):
    json_schema_validate("jsd_f200dc9a10d25beab1243a5b29f99c7d_v3_2_3_0").validate(obj)
    return True


def configure_a_rep_ring_on_fabric_deployment(api):
    endpoint_result = (
        api.industrial_configuration.configure_a_rep_ring_on_fabric_deployment(
            active_validation=True,
            deploymentMode="string",
            id="string",
            macsecConfig={
                "encryptionMode": "string",
                "accessControlMode": "string",
                "ciphersuite": "string",
                "keys": [
                    {
                        "id": 0,
                        "cryptoAlgo": "string",
                        "passPhrase": "string",
                        "startTime": "string",
                    }
                ],
            },
            networkDeviceId="string",
            payload=None,
            repSegmentId=0,
            repZtpMsg="string",
            ringMembers=[
                {
                    "networkDeviceId": "string",
                    "nodeName": "string",
                    "portName1": "string",
                    "portRepZtpStatus1": "string",
                    "portName2": "string",
                    "portRepZtpStatus2": "string",
                    "ringOrder": 0,
                }
            ],
            ringName="string",
            rootNeighbourNetworkDeviceIds=["string"],
            rootNetworkDeviceId="string",
            status="string",
        )
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_configure_a_rep_ring_on_fabric_deployment(api, validator):
    try:
        assert is_valid_configure_a_rep_ring_on_fabric_deployment(
            validator, configure_a_rep_ring_on_fabric_deployment(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def configure_a_rep_ring_on_fabric_deployment_default_val(api):
    endpoint_result = (
        api.industrial_configuration.configure_a_rep_ring_on_fabric_deployment(
            active_validation=True,
            deploymentMode=None,
            id=None,
            macsecConfig=None,
            networkDeviceId=None,
            payload=None,
            repSegmentId=None,
            repZtpMsg=None,
            ringMembers=None,
            ringName=None,
            rootNeighbourNetworkDeviceIds=None,
            rootNetworkDeviceId=None,
            status=None,
        )
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_configure_a_rep_ring_on_fabric_deployment_default_val(api, validator):
    try:
        assert is_valid_configure_a_rep_ring_on_fabric_deployment(
            validator, configure_a_rep_ring_on_fabric_deployment_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_configuration_model_generation_status_for_prp(
    json_schema_validate, obj
):
    json_schema_validate("jsd_45d1950132e25b1881cfabdd34719ee5_v3_2_3_0").validate(obj)
    return True


def retrieve_configuration_model_generation_status_for_prp(api):
    endpoint_result = api.industrial_configuration.retrieve_configuration_model_generation_status_for_prp(
        preview_activity_id="string"
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieve_configuration_model_generation_status_for_prp(api, validator):
    try:
        assert is_valid_retrieve_configuration_model_generation_status_for_prp(
            validator, retrieve_configuration_model_generation_status_for_prp(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_configuration_model_generation_status_for_prp_default_val(api):
    endpoint_result = api.industrial_configuration.retrieve_configuration_model_generation_status_for_prp(
        preview_activity_id="string"
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieve_configuration_model_generation_status_for_prp_default_val(
    api, validator
):
    try:
        assert is_valid_retrieve_configuration_model_generation_status_for_prp(
            validator,
            retrieve_configuration_model_generation_status_for_prp_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_count_of_rep_rings(json_schema_validate, obj):
    json_schema_validate("jsd_2d9f276a532e5eeb86bb591f8537fcc7_v3_2_3_0").validate(obj)
    return True


def retrieves_the_count_of_rep_rings(api):
    endpoint_result = api.industrial_configuration.retrieves_the_count_of_rep_rings(
        active_validation=True,
        deploymentMode="string",
        networkDeviceId="string",
        payload=None,
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieves_the_count_of_rep_rings(api, validator):
    try:
        assert is_valid_retrieves_the_count_of_rep_rings(
            validator, retrieves_the_count_of_rep_rings(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_count_of_rep_rings_default_val(api):
    endpoint_result = api.industrial_configuration.retrieves_the_count_of_rep_rings(
        active_validation=True, deploymentMode=None, networkDeviceId=None, payload=None
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_retrieves_the_count_of_rep_rings_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_count_of_rep_rings(
            validator, retrieves_the_count_of_rep_rings_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_rep_ring_configured_in_the_fabric_deployment(
    json_schema_validate, obj
):
    json_schema_validate("jsd_743aca1b387f556ca0c87d563b3df8f2_v3_2_3_0").validate(obj)
    return True


def delete_rep_ring_configured_in_the_fabric_deployment(api):
    endpoint_result = api.industrial_configuration.delete_rep_ring_configured_in_the_fabric_deployment(
        force_delete=True, id="string"
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_delete_rep_ring_configured_in_the_fabric_deployment(api, validator):
    try:
        assert is_valid_delete_rep_ring_configured_in_the_fabric_deployment(
            validator, delete_rep_ring_configured_in_the_fabric_deployment(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_rep_ring_configured_in_the_fabric_deployment_default_val(api):
    endpoint_result = api.industrial_configuration.delete_rep_ring_configured_in_the_fabric_deployment(
        force_delete=None, id="string"
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_delete_rep_ring_configured_in_the_fabric_deployment_default_val(
    api, validator
):
    try:
        assert is_valid_delete_rep_ring_configured_in_the_fabric_deployment(
            validator,
            delete_rep_ring_configured_in_the_fabric_deployment_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deploy_the_configuration_model_for_prp_on_network_devices(
    json_schema_validate, obj
):
    json_schema_validate("jsd_815dbfa788ae5dfe849b7b4784aa8297_v3_2_3_0").validate(obj)
    return True


def deploy_the_configuration_model_for_prp_on_network_devices(api):
    endpoint_result = api.industrial_configuration.deploy_the_configuration_model_for_prp_on_network_devices(
        active_validation=True, payload=None, preview_activity_id="string"
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_deploy_the_configuration_model_for_prp_on_network_devices(api, validator):
    try:
        assert is_valid_deploy_the_configuration_model_for_prp_on_network_devices(
            validator, deploy_the_configuration_model_for_prp_on_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deploy_the_configuration_model_for_prp_on_network_devices_default_val(api):
    endpoint_result = api.industrial_configuration.deploy_the_configuration_model_for_prp_on_network_devices(
        active_validation=True, payload=None, preview_activity_id="string"
    )
    return endpoint_result


@pytest.mark.industrial_configuration
def test_deploy_the_configuration_model_for_prp_on_network_devices_default_val(
    api, validator
):
    try:
        assert is_valid_deploy_the_configuration_model_for_prp_on_network_devices(
            validator,
            deploy_the_configuration_model_for_prp_on_network_devices_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
