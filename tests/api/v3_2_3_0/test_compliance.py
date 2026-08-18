"""CatalystCenterAPI compliance API fixtures and tests.

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


def is_valid_get_count_of_security_advisories_affecting_the_network_devices(
    json_schema_validate, obj
):
    json_schema_validate("jsd_a0ee1bc9fe825b49aaf57eb14b4c90cf_v3_2_3_0").validate(obj)
    return True


def get_count_of_security_advisories_affecting_the_network_devices(api):
    endpoint_result = (
        api.compliance.get_count_of_security_advisories_affecting_the_network_devices(
            cvss_base_score="string",
            device_count=0,
            id="string",
            security_impact_rating="string",
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_security_advisories_affecting_the_network_devices(api, validator):
    try:
        assert is_valid_get_count_of_security_advisories_affecting_the_network_devices(
            validator,
            get_count_of_security_advisories_affecting_the_network_devices(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_security_advisories_affecting_the_network_devices_default_val(api):
    endpoint_result = (
        api.compliance.get_count_of_security_advisories_affecting_the_network_devices(
            cvss_base_score=None,
            device_count=None,
            id=None,
            security_impact_rating=None,
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_security_advisories_affecting_the_network_devices_default_val(
    api, validator
):
    try:
        assert is_valid_get_count_of_security_advisories_affecting_the_network_devices(
            validator,
            get_count_of_security_advisories_affecting_the_network_devices_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_a_specific_rule(json_schema_validate, obj):
    json_schema_validate("jsd_ae58a079ac705cba94b721c4f964871b_v3_2_3_0").validate(obj)
    return True


def delete_a_specific_rule(api):
    endpoint_result = api.compliance.delete_a_specific_rule(
        id="string", policy_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_delete_a_specific_rule(api, validator):
    try:
        assert is_valid_delete_a_specific_rule(validator, delete_a_specific_rule(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_a_specific_rule_default_val(api):
    endpoint_result = api.compliance.delete_a_specific_rule(
        id="string", policy_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_delete_a_specific_rule_default_val(api, validator):
    try:
        assert is_valid_delete_a_specific_rule(
            validator, delete_a_specific_rule_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_an_existing_rule(json_schema_validate, obj):
    json_schema_validate("jsd_8feb78fec3e454e1bd9dd531a6a29100_v3_2_3_0").validate(obj)
    return True


def update_an_existing_rule(api):
    endpoint_result = api.compliance.update_an_existing_rule(
        active_validation=True,
        conditionsCount=0,
        description="string",
        deviceTypes=[
            {
                "deviceFamily": "string",
                "deviceSeries": "string",
                "deviceModel": "string",
            }
        ],
        id="string",
        impact="string",
        name="string",
        payload=None,
        policyId="string",
        policy_id="string",
        softwareType="string",
        suggestedFix="string",
        variablesCount=0,
    )
    return endpoint_result


@pytest.mark.compliance
def test_update_an_existing_rule(api, validator):
    try:
        assert is_valid_update_an_existing_rule(validator, update_an_existing_rule(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_an_existing_rule_default_val(api):
    endpoint_result = api.compliance.update_an_existing_rule(
        active_validation=True,
        conditionsCount=None,
        description=None,
        deviceTypes=None,
        id="string",
        impact=None,
        name=None,
        payload=None,
        policyId=None,
        policy_id="string",
        softwareType=None,
        suggestedFix=None,
        variablesCount=None,
    )
    return endpoint_result


@pytest.mark.compliance
def test_update_an_existing_rule_default_val(api, validator):
    try:
        assert is_valid_update_an_existing_rule(
            validator, update_an_existing_rule_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_a_specific_rule(json_schema_validate, obj):
    json_schema_validate("jsd_e67ac393f9f55c93b7911cf4053be19d_v3_2_3_0").validate(obj)
    return True


def retrieve_a_specific_rule(api):
    endpoint_result = api.compliance.retrieve_a_specific_rule(
        id="string", policy_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_a_specific_rule(api, validator):
    try:
        assert is_valid_retrieve_a_specific_rule(
            validator, retrieve_a_specific_rule(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_a_specific_rule_default_val(api):
    endpoint_result = api.compliance.retrieve_a_specific_rule(
        id="string", policy_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_a_specific_rule_default_val(api, validator):
    try:
        assert is_valid_retrieve_a_specific_rule(
            validator, retrieve_a_specific_rule_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_a_new_variable(json_schema_validate, obj):
    json_schema_validate("jsd_b1ded5eaafa25e6b8814fa1cc0f9829a_v3_2_3_0").validate(obj)
    return True


def create_a_new_variable(api):
    endpoint_result = api.compliance.create_a_new_variable(
        active_validation=True,
        dataType="string",
        defaultValue="string",
        description="string",
        id="string",
        identifier="string",
        inputType="string",
        mandatory=True,
        maxLength=0,
        maxValue=0,
        minValue=0,
        name="string",
        payload=None,
        policy_id="string",
        rule_id="string",
        selectionList=[{"key": "string", "value": "string", "default": True}],
        sequenceNumber=0,
        usedByConditions=["string"],
        validationRegex="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_create_a_new_variable(api, validator):
    try:
        assert is_valid_create_a_new_variable(validator, create_a_new_variable(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_a_new_variable_default_val(api):
    endpoint_result = api.compliance.create_a_new_variable(
        active_validation=True,
        dataType=None,
        defaultValue=None,
        description=None,
        id=None,
        identifier=None,
        inputType=None,
        mandatory=None,
        maxLength=None,
        maxValue=None,
        minValue=None,
        name=None,
        payload=None,
        policy_id="string",
        rule_id="string",
        selectionList=None,
        sequenceNumber=None,
        usedByConditions=None,
        validationRegex=None,
    )
    return endpoint_result


@pytest.mark.compliance
def test_create_a_new_variable_default_val(api, validator):
    try:
        assert is_valid_create_a_new_variable(
            validator, create_a_new_variable_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_variables(json_schema_validate, obj):
    json_schema_validate("jsd_7f0883863a905d0b9e14aee6936c3586_v3_2_3_0").validate(obj)
    return True


def retrieve_the_variables(api):
    endpoint_result = api.compliance.retrieve_the_variables(
        limit=0, offset=0, policy_id="string", rule_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_variables(api, validator):
    try:
        assert is_valid_retrieve_the_variables(validator, retrieve_the_variables(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_variables_default_val(api):
    endpoint_result = api.compliance.retrieve_the_variables(
        limit=None, offset=None, policy_id="string", rule_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_variables_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_variables(
            validator, retrieve_the_variables_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_count_of_network_devices(json_schema_validate, obj):
    json_schema_validate("jsd_f34ef12e936754518d6d054c3cae6e1c_v3_2_3_0").validate(obj)
    return True


def retrieve_the_count_of_network_devices(api):
    endpoint_result = api.compliance.retrieve_the_count_of_network_devices(
        family="string",
        hostname="string",
        management_address="string",
        role="string",
        site_id="string",
        violation_id="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_count_of_network_devices(api, validator):
    try:
        assert is_valid_retrieve_the_count_of_network_devices(
            validator, retrieve_the_count_of_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_count_of_network_devices_default_val(api):
    endpoint_result = api.compliance.retrieve_the_count_of_network_devices(
        family=None,
        hostname=None,
        management_address=None,
        role=None,
        site_id="string",
        violation_id="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_count_of_network_devices_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_count_of_network_devices(
            validator, retrieve_the_count_of_network_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_a_new_policy(json_schema_validate, obj):
    json_schema_validate("jsd_5785878fdfba50738387ab89bede6252_v3_2_3_0").validate(obj)
    return True


def create_a_new_policy(api):
    endpoint_result = api.compliance.create_a_new_policy(
        active_validation=True,
        description="string",
        id="string",
        name="string",
        payload=None,
        rulesCount=0,
        sitesCount=0,
        source="string",
        status="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_create_a_new_policy(api, validator):
    try:
        assert is_valid_create_a_new_policy(validator, create_a_new_policy(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_a_new_policy_default_val(api):
    endpoint_result = api.compliance.create_a_new_policy(
        active_validation=True,
        description=None,
        id=None,
        name=None,
        payload=None,
        rulesCount=None,
        sitesCount=None,
        source=None,
        status=None,
    )
    return endpoint_result


@pytest.mark.compliance
def test_create_a_new_policy_default_val(api, validator):
    try:
        assert is_valid_create_a_new_policy(
            validator, create_a_new_policy_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_policies(json_schema_validate, obj):
    json_schema_validate("jsd_1e4d1fc1b50b5b7a976f7b918453aaf8_v3_2_3_0").validate(obj)
    return True


def retrieve_the_policies(api):
    endpoint_result = api.compliance.retrieve_the_policies(
        limit=0, name="string", offset=0, policy_id="value1,value2"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_policies(api, validator):
    try:
        assert is_valid_retrieve_the_policies(validator, retrieve_the_policies(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_policies_default_val(api):
    endpoint_result = api.compliance.retrieve_the_policies(
        limit=None, name=None, offset=None, policy_id=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_policies_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_policies(
            validator, retrieve_the_policies_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_a_specific_network_device(json_schema_validate, obj):
    json_schema_validate("jsd_21dbdcdf7d6b5af88c18f481d713f90c_v3_2_3_0").validate(obj)
    return True


def retrieve_a_specific_network_device(api):
    endpoint_result = api.compliance.retrieve_a_specific_network_device(
        network_device_id="string", policy_id="string", site_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_a_specific_network_device(api, validator):
    try:
        assert is_valid_retrieve_a_specific_network_device(
            validator, retrieve_a_specific_network_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_a_specific_network_device_default_val(api):
    endpoint_result = api.compliance.retrieve_a_specific_network_device(
        network_device_id="string", policy_id="string", site_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_a_specific_network_device_default_val(api, validator):
    try:
        assert is_valid_retrieve_a_specific_network_device(
            validator, retrieve_a_specific_network_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_creates_a_trial_for_field_notices_detection_on_network_devices(
    json_schema_validate, obj
):
    json_schema_validate("jsd_5820be66c0a0582fa234daaa2019b6b6_v3_2_3_0").validate(obj)
    return True


def creates_a_trial_for_field_notices_detection_on_network_devices(api):
    endpoint_result = (
        api.compliance.creates_a_trial_for_field_notices_detection_on_network_devices(
            active_validation=True, payload=None
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_creates_a_trial_for_field_notices_detection_on_network_devices(api, validator):
    try:
        assert is_valid_creates_a_trial_for_field_notices_detection_on_network_devices(
            validator,
            creates_a_trial_for_field_notices_detection_on_network_devices(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def creates_a_trial_for_field_notices_detection_on_network_devices_default_val(api):
    endpoint_result = (
        api.compliance.creates_a_trial_for_field_notices_detection_on_network_devices(
            active_validation=True, payload=None
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_creates_a_trial_for_field_notices_detection_on_network_devices_default_val(
    api, validator
):
    try:
        assert is_valid_creates_a_trial_for_field_notices_detection_on_network_devices(
            validator,
            creates_a_trial_for_field_notices_detection_on_network_devices_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_trial_details_for_field_notices_detection_on_network_devices(
    json_schema_validate, obj
):
    json_schema_validate("jsd_475203d3893f52738eaf50a6732d2159_v3_2_3_0").validate(obj)
    return True


def get_trial_details_for_field_notices_detection_on_network_devices(api):
    endpoint_result = (
        api.compliance.get_trial_details_for_field_notices_detection_on_network_devices()
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_trial_details_for_field_notices_detection_on_network_devices(
    api, validator
):
    try:
        assert (
            is_valid_get_trial_details_for_field_notices_detection_on_network_devices(
                validator,
                get_trial_details_for_field_notices_detection_on_network_devices(api),
            )
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_trial_details_for_field_notices_detection_on_network_devices_default_val(api):
    endpoint_result = (
        api.compliance.get_trial_details_for_field_notices_detection_on_network_devices()
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_trial_details_for_field_notices_detection_on_network_devices_default_val(
    api, validator
):
    try:
        assert is_valid_get_trial_details_for_field_notices_detection_on_network_devices(
            validator,
            get_trial_details_for_field_notices_detection_on_network_devices_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_bug_device_by_device_id(json_schema_validate, obj):
    json_schema_validate("jsd_e2f8ce2370c6532da9181a319daf0fec_v3_2_3_0").validate(obj)
    return True


def get_network_bug_device_by_device_id(api):
    endpoint_result = api.compliance.get_network_bug_device_by_device_id(
        network_device_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_network_bug_device_by_device_id(api, validator):
    try:
        assert is_valid_get_network_bug_device_by_device_id(
            validator, get_network_bug_device_by_device_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_bug_device_by_device_id_default_val(api):
    endpoint_result = api.compliance.get_network_bug_device_by_device_id(
        network_device_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_network_bug_device_by_device_id_default_val(api, validator):
    try:
        assert is_valid_get_network_bug_device_by_device_id(
            validator, get_network_bug_device_by_device_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_commit_device_configuration(json_schema_validate, obj):
    json_schema_validate("jsd_ba40975123ed50daa2f9f599cdf2d911_v3_2_3_0").validate(obj)
    return True


def commit_device_configuration(api):
    endpoint_result = api.compliance.commit_device_configuration(
        active_validation=True, deviceId=["string"], payload=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_commit_device_configuration(api, validator):
    try:
        assert is_valid_commit_device_configuration(
            validator, commit_device_configuration(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def commit_device_configuration_default_val(api):
    endpoint_result = api.compliance.commit_device_configuration(
        active_validation=True, deviceId=None, payload=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_commit_device_configuration_default_val(api, validator):
    try:
        assert is_valid_commit_device_configuration(
            validator, commit_device_configuration_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_field_notices_results_trend_over_time(json_schema_validate, obj):
    json_schema_validate("jsd_79872073a7065d7d9654a4015c6e961a_v3_2_3_0").validate(obj)
    return True


def get_field_notices_results_trend_over_time(api):
    endpoint_result = api.compliance.get_field_notices_results_trend_over_time(
        limit=0, offset=0, scan_time=0
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notices_results_trend_over_time(api, validator):
    try:
        assert is_valid_get_field_notices_results_trend_over_time(
            validator, get_field_notices_results_trend_over_time(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_field_notices_results_trend_over_time_default_val(api):
    endpoint_result = api.compliance.get_field_notices_results_trend_over_time(
        limit=None, offset=None, scan_time=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notices_results_trend_over_time_default_val(api, validator):
    try:
        assert is_valid_get_field_notices_results_trend_over_time(
            validator, get_field_notices_results_trend_over_time_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_a_specific_policy(json_schema_validate, obj):
    json_schema_validate("jsd_ca810854e3285927bd7fa0b36d0b2322_v3_2_3_0").validate(obj)
    return True


def retrieve_a_specific_policy(api):
    endpoint_result = api.compliance.retrieve_a_specific_policy(id="string")
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_a_specific_policy(api, validator):
    try:
        assert is_valid_retrieve_a_specific_policy(
            validator, retrieve_a_specific_policy(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_a_specific_policy_default_val(api):
    endpoint_result = api.compliance.retrieve_a_specific_policy(id="string")
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_a_specific_policy_default_val(api, validator):
    try:
        assert is_valid_retrieve_a_specific_policy(
            validator, retrieve_a_specific_policy_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_a_specific_policy(json_schema_validate, obj):
    json_schema_validate("jsd_ecbcd3aa7abb552d9123b8c8c6b194a0_v3_2_3_0").validate(obj)
    return True


def delete_a_specific_policy(api):
    endpoint_result = api.compliance.delete_a_specific_policy(id="string")
    return endpoint_result


@pytest.mark.compliance
def test_delete_a_specific_policy(api, validator):
    try:
        assert is_valid_delete_a_specific_policy(
            validator, delete_a_specific_policy(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_a_specific_policy_default_val(api):
    endpoint_result = api.compliance.delete_a_specific_policy(id="string")
    return endpoint_result


@pytest.mark.compliance
def test_delete_a_specific_policy_default_val(api, validator):
    try:
        assert is_valid_delete_a_specific_policy(
            validator, delete_a_specific_policy_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_an_existing_policy(json_schema_validate, obj):
    json_schema_validate("jsd_94f50ab34f58526bb0ed8aa910f47f24_v3_2_3_0").validate(obj)
    return True


def update_an_existing_policy(api):
    endpoint_result = api.compliance.update_an_existing_policy(
        active_validation=True,
        description="string",
        id="string",
        name="string",
        payload=None,
        rulesCount=0,
        sitesCount=0,
        source="string",
        status="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_update_an_existing_policy(api, validator):
    try:
        assert is_valid_update_an_existing_policy(
            validator, update_an_existing_policy(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_an_existing_policy_default_val(api):
    endpoint_result = api.compliance.update_an_existing_policy(
        active_validation=True,
        description=None,
        id="string",
        name=None,
        payload=None,
        rulesCount=None,
        sitesCount=None,
        source=None,
        status=None,
    )
    return endpoint_result


@pytest.mark.compliance
def test_update_an_existing_policy_default_val(api, validator):
    try:
        assert is_valid_update_an_existing_policy(
            validator, update_an_existing_policy_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_compliance_remediation(json_schema_validate, obj):
    json_schema_validate("jsd_a233477d86a459eab3c5e9352c1c9d3e_v3_2_3_0").validate(obj)
    return True


def compliance_remediation(api):
    endpoint_result = api.compliance.compliance_remediation(
        active_validation=True, id="string", payload=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_compliance_remediation(api, validator):
    try:
        assert is_valid_compliance_remediation(validator, compliance_remediation(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def compliance_remediation_default_val(api):
    endpoint_result = api.compliance.compliance_remediation(
        active_validation=True, id="string", payload=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_compliance_remediation_default_val(api, validator):
    try:
        assert is_valid_compliance_remediation(
            validator, compliance_remediation_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_a_specific_condition(json_schema_validate, obj):
    json_schema_validate("jsd_8c2eef5f8f6d5598866cd9da47a77842_v3_2_3_0").validate(obj)
    return True


def delete_a_specific_condition(api):
    endpoint_result = api.compliance.delete_a_specific_condition(
        id="string", policy_id="string", rule_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_delete_a_specific_condition(api, validator):
    try:
        assert is_valid_delete_a_specific_condition(
            validator, delete_a_specific_condition(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_a_specific_condition_default_val(api):
    endpoint_result = api.compliance.delete_a_specific_condition(
        id="string", policy_id="string", rule_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_delete_a_specific_condition_default_val(api, validator):
    try:
        assert is_valid_delete_a_specific_condition(
            validator, delete_a_specific_condition_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_an_existing_condition(json_schema_validate, obj):
    json_schema_validate("jsd_840c024bb00458248144753c93dd8215_v3_2_3_0").validate(obj)
    return True


def update_an_existing_condition(api):
    endpoint_result = api.compliance.update_an_existing_condition(
        action={
            "matchAction": "string",
            "matchViolationSeverity": {},
            "matchViolationMessageType": "string",
            "matchViolationMessage": "string",
            "doesNotMatchAction": "string",
            "doesNotMatchViolationSeverity": {},
            "doesNotMatchViolationMessageType": "string",
            "doesNotMatchViolationMessage": "string",
        },
        active_validation=True,
        blockEndExpression="string",
        blockStartExpression="string",
        blockViolationCriteria="string",
        deviceProperty="string",
        id="string",
        name="string",
        operator="string",
        parseAsBlocks=True,
        payload=None,
        policy_id="string",
        regexViolationCriteria="string",
        rule_id="string",
        scope="string",
        sequenceNumber=0,
        showCommand="string",
        value="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_update_an_existing_condition(api, validator):
    try:
        assert is_valid_update_an_existing_condition(
            validator, update_an_existing_condition(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_an_existing_condition_default_val(api):
    endpoint_result = api.compliance.update_an_existing_condition(
        action=None,
        active_validation=True,
        blockEndExpression=None,
        blockStartExpression=None,
        blockViolationCriteria=None,
        deviceProperty=None,
        id="string",
        name=None,
        operator=None,
        parseAsBlocks=None,
        payload=None,
        policy_id="string",
        regexViolationCriteria=None,
        rule_id="string",
        scope=None,
        sequenceNumber=None,
        showCommand=None,
        value=None,
    )
    return endpoint_result


@pytest.mark.compliance
def test_update_an_existing_condition_default_val(api, validator):
    try:
        assert is_valid_update_an_existing_condition(
            validator, update_an_existing_condition_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_a_specific_condition(json_schema_validate, obj):
    json_schema_validate("jsd_b254b9b8f2d059088f2bcad712ed4277_v3_2_3_0").validate(obj)
    return True


def retrieve_a_specific_condition(api):
    endpoint_result = api.compliance.retrieve_a_specific_condition(
        id="string", policy_id="string", rule_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_a_specific_condition(api, validator):
    try:
        assert is_valid_retrieve_a_specific_condition(
            validator, retrieve_a_specific_condition(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_a_specific_condition_default_val(api):
    endpoint_result = api.compliance.retrieve_a_specific_condition(
        id="string", policy_id="string", rule_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_a_specific_condition_default_val(api, validator):
    try:
        assert is_valid_retrieve_a_specific_condition(
            validator, retrieve_a_specific_condition_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_bugs_affecting_the_network_device(json_schema_validate, obj):
    json_schema_validate("jsd_a3e7c7a84b195cf989715f228c4c3337_v3_2_3_0").validate(obj)
    return True


def get_count_of_bugs_affecting_the_network_device(api):
    endpoint_result = api.compliance.get_count_of_bugs_affecting_the_network_device(
        id="string", network_device_id="string", severity="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_bugs_affecting_the_network_device(api, validator):
    try:
        assert is_valid_get_count_of_bugs_affecting_the_network_device(
            validator, get_count_of_bugs_affecting_the_network_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_bugs_affecting_the_network_device_default_val(api):
    endpoint_result = api.compliance.get_count_of_bugs_affecting_the_network_device(
        id=None, network_device_id="string", severity=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_bugs_affecting_the_network_device_default_val(api, validator):
    try:
        assert is_valid_get_count_of_bugs_affecting_the_network_device(
            validator, get_count_of_bugs_affecting_the_network_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_rules(json_schema_validate, obj):
    json_schema_validate("jsd_276010a17e315a6e8af213a81d5c97c1_v3_2_3_0").validate(obj)
    return True


def retrieve_the_rules(api):
    endpoint_result = api.compliance.retrieve_the_rules(
        limit=0, offset=0, policy_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_rules(api, validator):
    try:
        assert is_valid_retrieve_the_rules(validator, retrieve_the_rules(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_rules_default_val(api):
    endpoint_result = api.compliance.retrieve_the_rules(
        limit=None, offset=None, policy_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_rules_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_rules(
            validator, retrieve_the_rules_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_a_new_rule(json_schema_validate, obj):
    json_schema_validate("jsd_f7a0cdee493d597e816e012afbcc928d_v3_2_3_0").validate(obj)
    return True


def create_a_new_rule(api):
    endpoint_result = api.compliance.create_a_new_rule(
        active_validation=True,
        conditionsCount=0,
        description="string",
        deviceTypes=[
            {
                "deviceFamily": "string",
                "deviceSeries": "string",
                "deviceModel": "string",
            }
        ],
        id="string",
        impact="string",
        name="string",
        payload=None,
        policyId="string",
        policy_id="string",
        softwareType="string",
        suggestedFix="string",
        variablesCount=0,
    )
    return endpoint_result


@pytest.mark.compliance
def test_create_a_new_rule(api, validator):
    try:
        assert is_valid_create_a_new_rule(validator, create_a_new_rule(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_a_new_rule_default_val(api):
    endpoint_result = api.compliance.create_a_new_rule(
        active_validation=True,
        conditionsCount=None,
        description=None,
        deviceTypes=None,
        id=None,
        impact=None,
        name=None,
        payload=None,
        policyId=None,
        policy_id="string",
        softwareType=None,
        suggestedFix=None,
        variablesCount=None,
    )
    return endpoint_result


@pytest.mark.compliance
def test_create_a_new_rule_default_val(api, validator):
    try:
        assert is_valid_create_a_new_rule(validator, create_a_new_rule_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_network_device_count(json_schema_validate, obj):
    json_schema_validate("jsd_1ae32fd2639754d987d37b159006cb9d_v3_2_3_0").validate(obj)
    return True


def retrieve_the_network_device_count(api):
    endpoint_result = api.compliance.retrieve_the_network_device_count(
        compliance_types="value1,value2",
        severity="string",
        site_id="string",
        status="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_network_device_count(api, validator):
    try:
        assert is_valid_retrieve_the_network_device_count(
            validator, retrieve_the_network_device_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_network_device_count_default_val(api):
    endpoint_result = api.compliance.retrieve_the_network_device_count(
        compliance_types=None, severity=None, site_id="string", status=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_network_device_count_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_network_device_count(
            validator, retrieve_the_network_device_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_security_advisory_network_devices_for_the_security_advisory(
    json_schema_validate, obj
):
    json_schema_validate("jsd_3d5fcf338dd95610a4a65c77888b8ed4_v3_2_3_0").validate(obj)
    return True


def get_count_of_security_advisory_network_devices_for_the_security_advisory(api):
    endpoint_result = api.compliance.get_count_of_security_advisory_network_devices_for_the_security_advisory(
        id="string",
        network_device_id="string",
        scan_mode="string",
        scan_status="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_security_advisory_network_devices_for_the_security_advisory(
    api, validator
):
    try:
        assert is_valid_get_count_of_security_advisory_network_devices_for_the_security_advisory(
            validator,
            get_count_of_security_advisory_network_devices_for_the_security_advisory(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_security_advisory_network_devices_for_the_security_advisory_default_val(
    api,
):
    endpoint_result = api.compliance.get_count_of_security_advisory_network_devices_for_the_security_advisory(
        id="string", network_device_id=None, scan_mode=None, scan_status=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_security_advisory_network_devices_for_the_security_advisory_default_val(
    api, validator
):
    try:
        assert is_valid_get_count_of_security_advisory_network_devices_for_the_security_advisory(
            validator,
            get_count_of_security_advisory_network_devices_for_the_security_advisory_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_count_of_violations(json_schema_validate, obj):
    json_schema_validate("jsd_4f31700e7ac45659ba1587446bf1d066_v3_2_3_0").validate(obj)
    return True


def retrieve_the_count_of_violations(api):
    endpoint_result = api.compliance.retrieve_the_count_of_violations(
        acknowledgement_status="string",
        compliance_type="string",
        feature="string",
        operation="string",
        parameter="string",
        policy_name="string",
        rule_name="string",
        site_id="string",
        sub_types="value1,value2",
        template_name="string",
        violation_message="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_count_of_violations(api, validator):
    try:
        assert is_valid_retrieve_the_count_of_violations(
            validator, retrieve_the_count_of_violations(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_count_of_violations_default_val(api):
    endpoint_result = api.compliance.retrieve_the_count_of_violations(
        acknowledgement_status=None,
        compliance_type=None,
        feature=None,
        operation=None,
        parameter=None,
        policy_name=None,
        rule_name=None,
        site_id="string",
        sub_types=None,
        template_name=None,
        violation_message=None,
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_count_of_violations_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_count_of_violations(
            validator, retrieve_the_count_of_violations_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_count_of_violations_know_your_network(
    json_schema_validate, obj
):
    json_schema_validate("jsd_192bd9c5e8555048b3b6cd95c68b4eb4_v3_2_3_0").validate(obj)
    return True


def retrieve_the_count_of_violations_know_your_network(api):
    endpoint_result = api.compliance.retrieve_the_count_of_violations_know_your_network(
        hostname="string",
        management_address="string",
        policy_id="string",
        rule_id="string",
        rule_name="string",
        site_id="string",
        violation_message="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_count_of_violations_know_your_network(api, validator):
    try:
        assert is_valid_retrieve_the_count_of_violations_know_your_network(
            validator, retrieve_the_count_of_violations_know_your_network(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_count_of_violations_know_your_network_default_val(api):
    endpoint_result = api.compliance.retrieve_the_count_of_violations_know_your_network(
        hostname=None,
        management_address=None,
        policy_id="string",
        rule_id=None,
        rule_name=None,
        site_id="string",
        violation_message=None,
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_count_of_violations_know_your_network_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_count_of_violations_know_your_network(
            validator,
            retrieve_the_count_of_violations_know_your_network_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_triggers_a_security_advisories_scan_for_the_supported_network_devices(
    json_schema_validate, obj
):
    json_schema_validate("jsd_cce0f5e813955eabb3c736d3b5952341_v3_2_3_0").validate(obj)
    return True


def triggers_a_security_advisories_scan_for_the_supported_network_devices(api):
    endpoint_result = api.compliance.triggers_a_security_advisories_scan_for_the_supported_network_devices(
        active_validation=True, failed_devices_only=True, payload=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_triggers_a_security_advisories_scan_for_the_supported_network_devices(
    api, validator
):
    try:
        assert is_valid_triggers_a_security_advisories_scan_for_the_supported_network_devices(
            validator,
            triggers_a_security_advisories_scan_for_the_supported_network_devices(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def triggers_a_security_advisories_scan_for_the_supported_network_devices_default_val(
    api,
):
    endpoint_result = api.compliance.triggers_a_security_advisories_scan_for_the_supported_network_devices(
        active_validation=True, failed_devices_only=None, payload=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_triggers_a_security_advisories_scan_for_the_supported_network_devices_default_val(
    api, validator
):
    try:
        assert is_valid_triggers_a_security_advisories_scan_for_the_supported_network_devices(
            validator,
            triggers_a_security_advisories_scan_for_the_supported_network_devices_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_creates_a_trial_for_bugs_detection_on_network_devices(
    json_schema_validate, obj
):
    json_schema_validate("jsd_7c08d904cff256aca70a68901692a021_v3_2_3_0").validate(obj)
    return True


def creates_a_trial_for_bugs_detection_on_network_devices(api):
    endpoint_result = (
        api.compliance.creates_a_trial_for_bugs_detection_on_network_devices(
            active_validation=True, payload=None
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_creates_a_trial_for_bugs_detection_on_network_devices(api, validator):
    try:
        assert is_valid_creates_a_trial_for_bugs_detection_on_network_devices(
            validator, creates_a_trial_for_bugs_detection_on_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def creates_a_trial_for_bugs_detection_on_network_devices_default_val(api):
    endpoint_result = (
        api.compliance.creates_a_trial_for_bugs_detection_on_network_devices(
            active_validation=True, payload=None
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_creates_a_trial_for_bugs_detection_on_network_devices_default_val(
    api, validator
):
    try:
        assert is_valid_creates_a_trial_for_bugs_detection_on_network_devices(
            validator,
            creates_a_trial_for_bugs_detection_on_network_devices_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_trial_details_for_bugs_detection_on_network_devices(
    json_schema_validate, obj
):
    json_schema_validate("jsd_5a3479f3b91c5b73bdfed9f1cb6f7bb5_v3_2_3_0").validate(obj)
    return True


def get_trial_details_for_bugs_detection_on_network_devices(api):
    endpoint_result = (
        api.compliance.get_trial_details_for_bugs_detection_on_network_devices()
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_trial_details_for_bugs_detection_on_network_devices(api, validator):
    try:
        assert is_valid_get_trial_details_for_bugs_detection_on_network_devices(
            validator, get_trial_details_for_bugs_detection_on_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_trial_details_for_bugs_detection_on_network_devices_default_val(api):
    endpoint_result = (
        api.compliance.get_trial_details_for_bugs_detection_on_network_devices()
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_trial_details_for_bugs_detection_on_network_devices_default_val(
    api, validator
):
    try:
        assert is_valid_get_trial_details_for_bugs_detection_on_network_devices(
            validator,
            get_trial_details_for_bugs_detection_on_network_devices_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_field_notices(json_schema_validate, obj):
    json_schema_validate("jsd_15b172bd7cd55378bd25e4ae525a9179_v3_2_3_0").validate(obj)
    return True


def get_count_of_field_notices(api):
    endpoint_result = api.compliance.get_count_of_field_notices(
        device_count=0, id="string", type="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_field_notices(api, validator):
    try:
        assert is_valid_get_count_of_field_notices(
            validator, get_count_of_field_notices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_field_notices_default_val(api):
    endpoint_result = api.compliance.get_count_of_field_notices(
        device_count=None, id=None, type=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_field_notices_default_val(api, validator):
    try:
        assert is_valid_get_count_of_field_notices(
            validator, get_count_of_field_notices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_creates_a_trial_for_security_advisories_detection_on_network_devices(
    json_schema_validate, obj
):
    json_schema_validate("jsd_84b209c580ed5c0aaf4c978f4dfc00bd_v3_2_3_0").validate(obj)
    return True


def creates_a_trial_for_security_advisories_detection_on_network_devices(api):
    endpoint_result = api.compliance.creates_a_trial_for_security_advisories_detection_on_network_devices(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_creates_a_trial_for_security_advisories_detection_on_network_devices(
    api, validator
):
    try:
        assert is_valid_creates_a_trial_for_security_advisories_detection_on_network_devices(
            validator,
            creates_a_trial_for_security_advisories_detection_on_network_devices(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def creates_a_trial_for_security_advisories_detection_on_network_devices_default_val(
    api,
):
    endpoint_result = api.compliance.creates_a_trial_for_security_advisories_detection_on_network_devices(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_creates_a_trial_for_security_advisories_detection_on_network_devices_default_val(
    api, validator
):
    try:
        assert is_valid_creates_a_trial_for_security_advisories_detection_on_network_devices(
            validator,
            creates_a_trial_for_security_advisories_detection_on_network_devices_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_trial_details_for_security_advisories_detection_on_network_devices(
    json_schema_validate, obj
):
    json_schema_validate("jsd_fe4fd333ec815ec283443c490bde2741_v3_2_3_0").validate(obj)
    return True


def get_trial_details_for_security_advisories_detection_on_network_devices(api):
    endpoint_result = (
        api.compliance.get_trial_details_for_security_advisories_detection_on_network_devices()
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_trial_details_for_security_advisories_detection_on_network_devices(
    api, validator
):
    try:
        assert is_valid_get_trial_details_for_security_advisories_detection_on_network_devices(
            validator,
            get_trial_details_for_security_advisories_detection_on_network_devices(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_trial_details_for_security_advisories_detection_on_network_devices_default_val(
    api,
):
    endpoint_result = (
        api.compliance.get_trial_details_for_security_advisories_detection_on_network_devices()
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_trial_details_for_security_advisories_detection_on_network_devices_default_val(
    api, validator
):
    try:
        assert is_valid_get_trial_details_for_security_advisories_detection_on_network_devices(
            validator,
            get_trial_details_for_security_advisories_detection_on_network_devices_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_site_variables(json_schema_validate, obj):
    json_schema_validate("jsd_7ba0a122d6605486bc76945f27bd8fb7_v3_2_3_0").validate(obj)
    return True


def retrieve_site_variables(api):
    endpoint_result = api.compliance.retrieve_site_variables(
        inherited=True, policy_id="string", rule_id="string", site_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_site_variables(api, validator):
    try:
        assert is_valid_retrieve_site_variables(validator, retrieve_site_variables(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_site_variables_default_val(api):
    endpoint_result = api.compliance.retrieve_site_variables(
        inherited=None, policy_id="string", rule_id="string", site_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_site_variables_default_val(api, validator):
    try:
        assert is_valid_retrieve_site_variables(
            validator, retrieve_site_variables_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_set_site_variables(json_schema_validate, obj):
    json_schema_validate("jsd_d715bf675b1250118d4b201d1419065e_v3_2_3_0").validate(obj)
    return True


def set_site_variables(api):
    endpoint_result = api.compliance.set_site_variables(
        active_validation=True,
        inheritedSiteId="string",
        inheritedSiteName="string",
        payload=None,
        policy_id="string",
        rule_id="string",
        site_id="string",
        variableValues=[{"id": "string", "values": ["string"]}],
    )
    return endpoint_result


@pytest.mark.compliance
def test_set_site_variables(api, validator):
    try:
        assert is_valid_set_site_variables(validator, set_site_variables(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def set_site_variables_default_val(api):
    endpoint_result = api.compliance.set_site_variables(
        active_validation=True,
        inheritedSiteId=None,
        inheritedSiteName=None,
        payload=None,
        policy_id="string",
        rule_id="string",
        site_id="string",
        variableValues=None,
    )
    return endpoint_result


@pytest.mark.compliance
def test_set_site_variables_default_val(api, validator):
    try:
        assert is_valid_set_site_variables(
            validator, set_site_variables_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_count_of_policies(json_schema_validate, obj):
    json_schema_validate("jsd_f7125969fcf0572597a99c8b8ce071c8_v3_2_3_0").validate(obj)
    return True


def retrieve_the_count_of_policies(api):
    endpoint_result = api.compliance.retrieve_the_count_of_policies(
        name="string", policy_id="value1,value2", site_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_count_of_policies(api, validator):
    try:
        assert is_valid_retrieve_the_count_of_policies(
            validator, retrieve_the_count_of_policies(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_count_of_policies_default_val(api):
    endpoint_result = api.compliance.retrieve_the_count_of_policies(
        name=None, policy_id=None, site_id=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_count_of_policies_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_count_of_policies(
            validator, retrieve_the_count_of_policies_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_security_advisory_network_device_for_the_security_advisory_by_network_device_id(
    json_schema_validate, obj
):
    json_schema_validate("jsd_60544cb8be1c50ca9f2fe769cd27b2da_v3_2_3_0").validate(obj)
    return True


def get_security_advisory_network_device_for_the_security_advisory_by_network_device_id(
    api,
):
    endpoint_result = api.compliance.get_security_advisory_network_device_for_the_security_advisory_by_network_device_id(
        id="string", network_device_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisory_network_device_for_the_security_advisory_by_network_device_id(
    api, validator
):
    try:
        assert is_valid_get_security_advisory_network_device_for_the_security_advisory_by_network_device_id(
            validator,
            get_security_advisory_network_device_for_the_security_advisory_by_network_device_id(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_security_advisory_network_device_for_the_security_advisory_by_network_device_id_default_val(
    api,
):
    endpoint_result = api.compliance.get_security_advisory_network_device_for_the_security_advisory_by_network_device_id(
        id="string", network_device_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisory_network_device_for_the_security_advisory_by_network_device_id_default_val(
    api, validator
):
    try:
        assert is_valid_get_security_advisory_network_device_for_the_security_advisory_by_network_device_id(
            validator,
            get_security_advisory_network_device_for_the_security_advisory_by_network_device_id_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_conditions(json_schema_validate, obj):
    json_schema_validate("jsd_f73ad38bbbe15d65ba9526018bb4d03b_v3_2_3_0").validate(obj)
    return True


def retrieve_the_conditions(api):
    endpoint_result = api.compliance.retrieve_the_conditions(
        limit=0, offset=0, policy_id="string", rule_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_conditions(api, validator):
    try:
        assert is_valid_retrieve_the_conditions(validator, retrieve_the_conditions(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_conditions_default_val(api):
    endpoint_result = api.compliance.retrieve_the_conditions(
        limit=None, offset=None, policy_id="string", rule_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_conditions_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_conditions(
            validator, retrieve_the_conditions_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_a_new_condition(json_schema_validate, obj):
    json_schema_validate("jsd_ecb990ad7f24519397dd8d6c88de0067_v3_2_3_0").validate(obj)
    return True


def create_a_new_condition(api):
    endpoint_result = api.compliance.create_a_new_condition(
        action={
            "matchAction": "string",
            "matchViolationSeverity": {},
            "matchViolationMessageType": "string",
            "matchViolationMessage": "string",
            "doesNotMatchAction": "string",
            "doesNotMatchViolationSeverity": {},
            "doesNotMatchViolationMessageType": "string",
            "doesNotMatchViolationMessage": "string",
        },
        active_validation=True,
        blockEndExpression="string",
        blockStartExpression="string",
        blockViolationCriteria="string",
        deviceProperty="string",
        id="string",
        name="string",
        operator="string",
        parseAsBlocks=True,
        payload=None,
        policy_id="string",
        regexViolationCriteria="string",
        rule_id="string",
        scope="string",
        sequenceNumber=0,
        showCommand="string",
        value="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_create_a_new_condition(api, validator):
    try:
        assert is_valid_create_a_new_condition(validator, create_a_new_condition(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_a_new_condition_default_val(api):
    endpoint_result = api.compliance.create_a_new_condition(
        action=None,
        active_validation=True,
        blockEndExpression=None,
        blockStartExpression=None,
        blockViolationCriteria=None,
        deviceProperty=None,
        id=None,
        name=None,
        operator=None,
        parseAsBlocks=None,
        payload=None,
        policy_id="string",
        regexViolationCriteria=None,
        rule_id="string",
        scope=None,
        sequenceNumber=None,
        showCommand=None,
        value=None,
    )
    return endpoint_result


@pytest.mark.compliance
def test_create_a_new_condition_default_val(api, validator):
    try:
        assert is_valid_create_a_new_condition(
            validator, create_a_new_condition_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_compliance_violations(json_schema_validate, obj):
    json_schema_validate("jsd_1ca19be8bf8552f69e91eda2ab6862ae_v3_2_3_0").validate(obj)
    return True


def retrieve_the_compliance_violations(api):
    endpoint_result = api.compliance.retrieve_the_compliance_violations(
        acknowledgement_status="string",
        compliance_type="string",
        feature="string",
        limit=0,
        offset=0,
        operation="string",
        order="string",
        parameter="string",
        policy_name="string",
        rule_name="string",
        site_id="string",
        sort_by="string",
        sub_types="value1,value2",
        template_name="string",
        violation_message="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_compliance_violations(api, validator):
    try:
        assert is_valid_retrieve_the_compliance_violations(
            validator, retrieve_the_compliance_violations(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_compliance_violations_default_val(api):
    endpoint_result = api.compliance.retrieve_the_compliance_violations(
        acknowledgement_status=None,
        compliance_type=None,
        feature=None,
        limit=None,
        offset=None,
        operation=None,
        order=None,
        parameter=None,
        policy_name=None,
        rule_name=None,
        site_id="string",
        sort_by=None,
        sub_types=None,
        template_name=None,
        violation_message=None,
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_compliance_violations_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_compliance_violations(
            validator, retrieve_the_compliance_violations_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_security_advisories_affecting_the_network_device(
    json_schema_validate, obj
):
    json_schema_validate("jsd_74c12818ede552109f463d18c23a5a13_v3_2_3_0").validate(obj)
    return True


def get_security_advisories_affecting_the_network_device(api):
    endpoint_result = (
        api.compliance.get_security_advisories_affecting_the_network_device(
            cvss_base_score="string",
            id="string",
            limit=0,
            network_device_id="string",
            offset=0,
            order="string",
            security_impact_rating="string",
            sort_by="string",
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisories_affecting_the_network_device(api, validator):
    try:
        assert is_valid_get_security_advisories_affecting_the_network_device(
            validator, get_security_advisories_affecting_the_network_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_security_advisories_affecting_the_network_device_default_val(api):
    endpoint_result = (
        api.compliance.get_security_advisories_affecting_the_network_device(
            cvss_base_score=None,
            id=None,
            limit=None,
            network_device_id="string",
            offset=None,
            order=None,
            security_impact_rating=None,
            sort_by=None,
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisories_affecting_the_network_device_default_val(
    api, validator
):
    try:
        assert is_valid_get_security_advisories_affecting_the_network_device(
            validator,
            get_security_advisories_affecting_the_network_device_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_field_notice_network_devices(json_schema_validate, obj):
    json_schema_validate("jsd_50f4a44a87cc51ffb9be1cb2a6bdfa68_v3_2_3_0").validate(obj)
    return True


def get_count_of_field_notice_network_devices(api):
    endpoint_result = api.compliance.get_count_of_field_notice_network_devices(
        network_device_id="string", notice_count=0, scan_status="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_field_notice_network_devices(api, validator):
    try:
        assert is_valid_get_count_of_field_notice_network_devices(
            validator, get_count_of_field_notice_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_field_notice_network_devices_default_val(api):
    endpoint_result = api.compliance.get_count_of_field_notice_network_devices(
        network_device_id=None, notice_count=None, scan_status=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_field_notice_network_devices_default_val(api, validator):
    try:
        assert is_valid_get_count_of_field_notice_network_devices(
            validator, get_count_of_field_notice_network_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_a_specific_variable(json_schema_validate, obj):
    json_schema_validate("jsd_e6bad3aeee1356e89796eea887f1e03e_v3_2_3_0").validate(obj)
    return True


def retrieve_a_specific_variable(api):
    endpoint_result = api.compliance.retrieve_a_specific_variable(
        id="string", policy_id="string", rule_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_a_specific_variable(api, validator):
    try:
        assert is_valid_retrieve_a_specific_variable(
            validator, retrieve_a_specific_variable(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_a_specific_variable_default_val(api):
    endpoint_result = api.compliance.retrieve_a_specific_variable(
        id="string", policy_id="string", rule_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_a_specific_variable_default_val(api, validator):
    try:
        assert is_valid_retrieve_a_specific_variable(
            validator, retrieve_a_specific_variable_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_an_existing_variable(json_schema_validate, obj):
    json_schema_validate("jsd_4dfc7c061f9259ee891e60fd91235129_v3_2_3_0").validate(obj)
    return True


def update_an_existing_variable(api):
    endpoint_result = api.compliance.update_an_existing_variable(
        active_validation=True,
        dataType="string",
        defaultValue="string",
        description="string",
        id="string",
        inputType="string",
        mandatory=True,
        maxLength=0,
        maxValue=0,
        minValue=0,
        name="string",
        payload=None,
        policy_id="string",
        rule_id="string",
        selectionList=[{"key": "string", "value": "string", "default": True}],
        sequenceNumber=0,
        validationRegex="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_update_an_existing_variable(api, validator):
    try:
        assert is_valid_update_an_existing_variable(
            validator, update_an_existing_variable(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_an_existing_variable_default_val(api):
    endpoint_result = api.compliance.update_an_existing_variable(
        active_validation=True,
        dataType=None,
        defaultValue=None,
        description=None,
        id="string",
        inputType=None,
        mandatory=None,
        maxLength=None,
        maxValue=None,
        minValue=None,
        name=None,
        payload=None,
        policy_id="string",
        rule_id="string",
        selectionList=None,
        sequenceNumber=None,
        validationRegex=None,
    )
    return endpoint_result


@pytest.mark.compliance
def test_update_an_existing_variable_default_val(api, validator):
    try:
        assert is_valid_update_an_existing_variable(
            validator, update_an_existing_variable_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_a_specific_variable(json_schema_validate, obj):
    json_schema_validate("jsd_a1be1aa4cd8c58e3aeefef124501c19b_v3_2_3_0").validate(obj)
    return True


def delete_a_specific_variable(api):
    endpoint_result = api.compliance.delete_a_specific_variable(
        id="string", policy_id="string", rule_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_delete_a_specific_variable(api, validator):
    try:
        assert is_valid_delete_a_specific_variable(
            validator, delete_a_specific_variable(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_a_specific_variable_default_val(api):
    endpoint_result = api.compliance.delete_a_specific_variable(
        id="string", policy_id="string", rule_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_delete_a_specific_variable_default_val(api, validator):
    try:
        assert is_valid_delete_a_specific_variable(
            validator, delete_a_specific_variable_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_security_advisory_affecting_the_network_device_by_device_id_and_advisory_id(
    json_schema_validate, obj
):
    json_schema_validate("jsd_fc34a3eb64405e08b65fb830f2c1c05c_v3_2_3_0").validate(obj)
    return True


def get_security_advisory_affecting_the_network_device_by_device_id_and_advisory_id(
    api,
):
    endpoint_result = api.compliance.get_security_advisory_affecting_the_network_device_by_device_id_and_advisory_id(
        id="string", network_device_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisory_affecting_the_network_device_by_device_id_and_advisory_id(
    api, validator
):
    try:
        assert is_valid_get_security_advisory_affecting_the_network_device_by_device_id_and_advisory_id(
            validator,
            get_security_advisory_affecting_the_network_device_by_device_id_and_advisory_id(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_security_advisory_affecting_the_network_device_by_device_id_and_advisory_id_default_val(
    api,
):
    endpoint_result = api.compliance.get_security_advisory_affecting_the_network_device_by_device_id_and_advisory_id(
        id="string", network_device_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisory_affecting_the_network_device_by_device_id_and_advisory_id_default_val(
    api, validator
):
    try:
        assert is_valid_get_security_advisory_affecting_the_network_device_by_device_id_and_advisory_id(
            validator,
            get_security_advisory_affecting_the_network_device_by_device_id_and_advisory_id_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_a_specific_policy_know_your_network(json_schema_validate, obj):
    json_schema_validate("jsd_82cbcc3076565062acb03e727bb3e45a_v3_2_3_0").validate(obj)
    return True


def retrieve_a_specific_policy_know_your_network(api):
    endpoint_result = api.compliance.retrieve_a_specific_policy_know_your_network(
        policy_id="string", site_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_a_specific_policy_know_your_network(api, validator):
    try:
        assert is_valid_retrieve_a_specific_policy_know_your_network(
            validator, retrieve_a_specific_policy_know_your_network(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_a_specific_policy_know_your_network_default_val(api):
    endpoint_result = api.compliance.retrieve_a_specific_policy_know_your_network(
        policy_id="string", site_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_a_specific_policy_know_your_network_default_val(api, validator):
    try:
        assert is_valid_retrieve_a_specific_policy_know_your_network(
            validator, retrieve_a_specific_policy_know_your_network_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_acknowledge_or_unacknowledge_compliance_violations(
    json_schema_validate, obj
):
    json_schema_validate("jsd_c8c69357838e5263badfede9921c75da_v3_2_3_0").validate(obj)
    return True


def acknowledge_or_unacknowledge_compliance_violations(api):
    endpoint_result = api.compliance.acknowledge_or_unacknowledge_compliance_violations(
        acknowledgementStatus="string",
        active_validation=True,
        payload=None,
        site_id="string",
        violations=[{"violationId": "string", "networkDeviceIds": ["string"]}],
    )
    return endpoint_result


@pytest.mark.compliance
def test_acknowledge_or_unacknowledge_compliance_violations(api, validator):
    try:
        assert is_valid_acknowledge_or_unacknowledge_compliance_violations(
            validator, acknowledge_or_unacknowledge_compliance_violations(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def acknowledge_or_unacknowledge_compliance_violations_default_val(api):
    endpoint_result = api.compliance.acknowledge_or_unacknowledge_compliance_violations(
        acknowledgementStatus=None,
        active_validation=True,
        payload=None,
        site_id="string",
        violations=None,
    )
    return endpoint_result


@pytest.mark.compliance
def test_acknowledge_or_unacknowledge_compliance_violations_default_val(api, validator):
    try:
        assert is_valid_acknowledge_or_unacknowledge_compliance_violations(
            validator,
            acknowledge_or_unacknowledge_compliance_violations_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_field_notices_results_trend_over_time(
    json_schema_validate, obj
):
    json_schema_validate("jsd_20f89484e88e57b292756b0c7e54b553_v3_2_3_0").validate(obj)
    return True


def get_count_of_field_notices_results_trend_over_time(api):
    endpoint_result = api.compliance.get_count_of_field_notices_results_trend_over_time(
        scan_time=0
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_field_notices_results_trend_over_time(api, validator):
    try:
        assert is_valid_get_count_of_field_notices_results_trend_over_time(
            validator, get_count_of_field_notices_results_trend_over_time(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_field_notices_results_trend_over_time_default_val(api):
    endpoint_result = api.compliance.get_count_of_field_notices_results_trend_over_time(
        scan_time=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_field_notices_results_trend_over_time_default_val(api, validator):
    try:
        assert is_valid_get_count_of_field_notices_results_trend_over_time(
            validator,
            get_count_of_field_notices_results_trend_over_time_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_bugs_affecting_the_network_device(json_schema_validate, obj):
    json_schema_validate("jsd_aea65ed8cb2e55fb8d7c40abf2352504_v3_2_3_0").validate(obj)
    return True


def get_bugs_affecting_the_network_device(api):
    endpoint_result = api.compliance.get_bugs_affecting_the_network_device(
        id="string",
        limit=0,
        network_device_id="string",
        offset=0,
        order="string",
        severity="string",
        sort_by="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_bugs_affecting_the_network_device(api, validator):
    try:
        assert is_valid_get_bugs_affecting_the_network_device(
            validator, get_bugs_affecting_the_network_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_bugs_affecting_the_network_device_default_val(api):
    endpoint_result = api.compliance.get_bugs_affecting_the_network_device(
        id=None,
        limit=None,
        network_device_id="string",
        offset=None,
        order=None,
        severity=None,
        sort_by=None,
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_bugs_affecting_the_network_device_default_val(api, validator):
    try:
        assert is_valid_get_bugs_affecting_the_network_device(
            validator, get_bugs_affecting_the_network_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_field_notice_network_device_by_device_id(json_schema_validate, obj):
    json_schema_validate("jsd_f9138e17f05f57fda724a4767aa35ad4_v3_2_3_0").validate(obj)
    return True


def get_field_notice_network_device_by_device_id(api):
    endpoint_result = api.compliance.get_field_notice_network_device_by_device_id(
        network_device_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notice_network_device_by_device_id(api, validator):
    try:
        assert is_valid_get_field_notice_network_device_by_device_id(
            validator, get_field_notice_network_device_by_device_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_field_notice_network_device_by_device_id_default_val(api):
    endpoint_result = api.compliance.get_field_notice_network_device_by_device_id(
        network_device_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notice_network_device_by_device_id_default_val(api, validator):
    try:
        assert is_valid_get_field_notice_network_device_by_device_id(
            validator, get_field_notice_network_device_by_device_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_compliance_detail(json_schema_validate, obj):
    json_schema_validate("jsd_6395adeaeb8157da972efb7b91e1e2cb_v3_2_3_0").validate(obj)
    return True


def get_compliance_detail(api):
    endpoint_result = api.compliance.get_compliance_detail(
        compliance_status="string",
        compliance_type="string",
        device_uuid="string",
        limit=0,
        offset=0,
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_compliance_detail(api, validator):
    try:
        assert is_valid_get_compliance_detail(validator, get_compliance_detail(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_compliance_detail_default_val(api):
    endpoint_result = api.compliance.get_compliance_detail(
        compliance_status=None,
        compliance_type=None,
        device_uuid=None,
        limit=None,
        offset=None,
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_compliance_detail_default_val(api, validator):
    try:
        assert is_valid_get_compliance_detail(
            validator, get_compliance_detail_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_count_of_conditions(json_schema_validate, obj):
    json_schema_validate("jsd_36bff7821a975285a23ccae23d08ebd1_v3_2_3_0").validate(obj)
    return True


def retrieve_the_count_of_conditions(api):
    endpoint_result = api.compliance.retrieve_the_count_of_conditions(
        policy_id="string", rule_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_count_of_conditions(api, validator):
    try:
        assert is_valid_retrieve_the_count_of_conditions(
            validator, retrieve_the_count_of_conditions(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_count_of_conditions_default_val(api):
    endpoint_result = api.compliance.retrieve_the_count_of_conditions(
        policy_id="string", rule_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_count_of_conditions_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_count_of_conditions(
            validator, retrieve_the_count_of_conditions_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_compliance_summary(json_schema_validate, obj):
    json_schema_validate("jsd_a2a486537bc7509eba231ca3b4be9b25_v3_2_3_0").validate(obj)
    return True


def retrieve_the_compliance_summary(api):
    endpoint_result = api.compliance.retrieve_the_compliance_summary(
        compliance_types="value1,value2", site_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_compliance_summary(api, validator):
    try:
        assert is_valid_retrieve_the_compliance_summary(
            validator, retrieve_the_compliance_summary(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_compliance_summary_default_val(api):
    endpoint_result = api.compliance.retrieve_the_compliance_summary(
        compliance_types=None, site_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_compliance_summary_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_compliance_summary(
            validator, retrieve_the_compliance_summary_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_network_bug_devices_for_the_bug(json_schema_validate, obj):
    json_schema_validate("jsd_723c7afe7c0c5c2898eabb7cbbdc4ef4_v3_2_3_0").validate(obj)
    return True


def get_count_of_network_bug_devices_for_the_bug(api):
    endpoint_result = api.compliance.get_count_of_network_bug_devices_for_the_bug(
        id="string",
        network_device_id="string",
        scan_mode="string",
        scan_status="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_network_bug_devices_for_the_bug(api, validator):
    try:
        assert is_valid_get_count_of_network_bug_devices_for_the_bug(
            validator, get_count_of_network_bug_devices_for_the_bug(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_network_bug_devices_for_the_bug_default_val(api):
    endpoint_result = api.compliance.get_count_of_network_bug_devices_for_the_bug(
        id="string", network_device_id=None, scan_mode=None, scan_status=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_network_bug_devices_for_the_bug_default_val(api, validator):
    try:
        assert is_valid_get_count_of_network_bug_devices_for_the_bug(
            validator, get_count_of_network_bug_devices_for_the_bug_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_bugs(json_schema_validate, obj):
    json_schema_validate("jsd_a3217129c2295b27838cf486a35626f8_v3_2_3_0").validate(obj)
    return True


def get_network_bugs(api):
    endpoint_result = api.compliance.get_network_bugs(
        device_count=0,
        id="string",
        limit=0,
        offset=0,
        order="string",
        severity="string",
        sort_by="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_network_bugs(api, validator):
    try:
        assert is_valid_get_network_bugs(validator, get_network_bugs(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_bugs_default_val(api):
    endpoint_result = api.compliance.get_network_bugs(
        device_count=None,
        id=None,
        limit=None,
        offset=None,
        order=None,
        severity=None,
        sort_by=None,
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_network_bugs_default_val(api, validator):
    try:
        assert is_valid_get_network_bugs(validator, get_network_bugs_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_compliance_detail_count(json_schema_validate, obj):
    json_schema_validate("jsd_d3d38fed534f5aeaa80f5a8c63694708_v3_2_3_0").validate(obj)
    return True


def get_compliance_detail_count(api):
    endpoint_result = api.compliance.get_compliance_detail_count(
        compliance_status="string", compliance_type="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_compliance_detail_count(api, validator):
    try:
        assert is_valid_get_compliance_detail_count(
            validator, get_compliance_detail_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_compliance_detail_count_default_val(api):
    endpoint_result = api.compliance.get_compliance_detail_count(
        compliance_status=None, compliance_type=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_compliance_detail_count_default_val(api, validator):
    try:
        assert is_valid_get_compliance_detail_count(
            validator, get_compliance_detail_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_violating_policies(json_schema_validate, obj):
    json_schema_validate("jsd_9145689b12c05818915b94f985d903f8_v3_2_3_0").validate(obj)
    return True


def retrieve_the_violating_policies(api):
    endpoint_result = api.compliance.retrieve_the_violating_policies(
        limit=0, network_device_id="string", offset=0
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_violating_policies(api, validator):
    try:
        assert is_valid_retrieve_the_violating_policies(
            validator, retrieve_the_violating_policies(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_violating_policies_default_val(api):
    endpoint_result = api.compliance.retrieve_the_violating_policies(
        limit=None, network_device_id="string", offset=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_violating_policies_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_violating_policies(
            validator, retrieve_the_violating_policies_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_count_of_network_devices_know_your_network(
    json_schema_validate, obj
):
    json_schema_validate("jsd_29461c921a5c5465a9c9b8daa55bab93_v3_2_3_0").validate(obj)
    return True


def retrieve_the_count_of_network_devices_know_your_network(api):
    endpoint_result = (
        api.compliance.retrieve_the_count_of_network_devices_know_your_network(
            family="string",
            hostname="string",
            management_address="string",
            policy_id="string",
            role="string",
            site_id="string",
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_count_of_network_devices_know_your_network(api, validator):
    try:
        assert is_valid_retrieve_the_count_of_network_devices_know_your_network(
            validator, retrieve_the_count_of_network_devices_know_your_network(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_count_of_network_devices_know_your_network_default_val(api):
    endpoint_result = (
        api.compliance.retrieve_the_count_of_network_devices_know_your_network(
            family=None,
            hostname=None,
            management_address=None,
            policy_id="string",
            role=None,
            site_id="string",
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_count_of_network_devices_know_your_network_default_val(
    api, validator
):
    try:
        assert is_valid_retrieve_the_count_of_network_devices_know_your_network(
            validator,
            retrieve_the_count_of_network_devices_know_your_network_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_network_bugs(json_schema_validate, obj):
    json_schema_validate("jsd_5e1ec0f16d5e57cab08414ece382334d_v3_2_3_0").validate(obj)
    return True


def get_count_of_network_bugs(api):
    endpoint_result = api.compliance.get_count_of_network_bugs(
        device_count=0, id="string", severity="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_network_bugs(api, validator):
    try:
        assert is_valid_get_count_of_network_bugs(
            validator, get_count_of_network_bugs(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_network_bugs_default_val(api):
    endpoint_result = api.compliance.get_count_of_network_bugs(
        device_count=None, id=None, severity=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_network_bugs_default_val(api, validator):
    try:
        assert is_valid_get_count_of_network_bugs(
            validator, get_count_of_network_bugs_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_compliance_details_of_device(json_schema_validate, obj):
    json_schema_validate("jsd_90b70e1b6a2f51a59690669a4b2fd3f0_v3_2_3_0").validate(obj)
    return True


def compliance_details_of_device(api):
    endpoint_result = api.compliance.compliance_details_of_device(
        category="string",
        compliance_type="string",
        device_uuid="string",
        diff_list=True,
        remediation_supported=True,
        status="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_compliance_details_of_device(api, validator):
    try:
        assert is_valid_compliance_details_of_device(
            validator, compliance_details_of_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def compliance_details_of_device_default_val(api):
    endpoint_result = api.compliance.compliance_details_of_device(
        category=None,
        compliance_type=None,
        device_uuid="string",
        diff_list=None,
        remediation_supported=None,
        status=None,
    )
    return endpoint_result


@pytest.mark.compliance
def test_compliance_details_of_device_default_val(api, validator):
    try:
        assert is_valid_compliance_details_of_device(
            validator, compliance_details_of_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_count_of_policies_know_your_network(
    json_schema_validate, obj
):
    json_schema_validate("jsd_13b5b6246dda54a68b62d27f1f18a058_v3_2_3_0").validate(obj)
    return True


def retrieve_the_count_of_policies_know_your_network(api):
    endpoint_result = api.compliance.retrieve_the_count_of_policies_know_your_network(
        policy_name="string", site_id="string", status="value1,value2"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_count_of_policies_know_your_network(api, validator):
    try:
        assert is_valid_retrieve_the_count_of_policies_know_your_network(
            validator, retrieve_the_count_of_policies_know_your_network(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_count_of_policies_know_your_network_default_val(api):
    endpoint_result = api.compliance.retrieve_the_count_of_policies_know_your_network(
        policy_name=None, site_id="string", status=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_count_of_policies_know_your_network_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_count_of_policies_know_your_network(
            validator, retrieve_the_count_of_policies_know_your_network_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_field_notice_network_devices_for_the_notice(
    json_schema_validate, obj
):
    json_schema_validate("jsd_49cffe4d51a6508e8c18de0d45d78294_v3_2_3_0").validate(obj)
    return True


def get_count_of_field_notice_network_devices_for_the_notice(api):
    endpoint_result = (
        api.compliance.get_count_of_field_notice_network_devices_for_the_notice(
            id="string", network_device_id="string", scan_status="string"
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_field_notice_network_devices_for_the_notice(api, validator):
    try:
        assert is_valid_get_count_of_field_notice_network_devices_for_the_notice(
            validator, get_count_of_field_notice_network_devices_for_the_notice(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_field_notice_network_devices_for_the_notice_default_val(api):
    endpoint_result = (
        api.compliance.get_count_of_field_notice_network_devices_for_the_notice(
            id="string", network_device_id=None, scan_status=None
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_field_notice_network_devices_for_the_notice_default_val(
    api, validator
):
    try:
        assert is_valid_get_count_of_field_notice_network_devices_for_the_notice(
            validator,
            get_count_of_field_notice_network_devices_for_the_notice_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_a_specific_policy_violation(json_schema_validate, obj):
    json_schema_validate("jsd_1b728533d8e251998fb82f9e8c43c403_v3_2_3_0").validate(obj)
    return True


def retrieve_a_specific_policy_violation(api):
    endpoint_result = api.compliance.retrieve_a_specific_policy_violation(
        policy_id="string", site_id="string", violation_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_a_specific_policy_violation(api, validator):
    try:
        assert is_valid_retrieve_a_specific_policy_violation(
            validator, retrieve_a_specific_policy_violation(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_a_specific_policy_violation_default_val(api):
    endpoint_result = api.compliance.retrieve_a_specific_policy_violation(
        policy_id="string", site_id="string", violation_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_a_specific_policy_violation_default_val(api, validator):
    try:
        assert is_valid_retrieve_a_specific_policy_violation(
            validator, retrieve_a_specific_policy_violation_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_security_advisory_affecting_the_network_devices_by_id(
    json_schema_validate, obj
):
    json_schema_validate("jsd_37724dca392c51998fec3821dfb312de_v3_2_3_0").validate(obj)
    return True


def get_security_advisory_affecting_the_network_devices_by_id(api):
    endpoint_result = (
        api.compliance.get_security_advisory_affecting_the_network_devices_by_id(
            id="string"
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisory_affecting_the_network_devices_by_id(api, validator):
    try:
        assert is_valid_get_security_advisory_affecting_the_network_devices_by_id(
            validator, get_security_advisory_affecting_the_network_devices_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_security_advisory_affecting_the_network_devices_by_id_default_val(api):
    endpoint_result = (
        api.compliance.get_security_advisory_affecting_the_network_devices_by_id(
            id="string"
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisory_affecting_the_network_devices_by_id_default_val(
    api, validator
):
    try:
        assert is_valid_get_security_advisory_affecting_the_network_devices_by_id(
            validator,
            get_security_advisory_affecting_the_network_devices_by_id_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_triggers_a_bugs_scan_for_the_supported_network_devices(
    json_schema_validate, obj
):
    json_schema_validate("jsd_37b6c0f7132f5a1485b7b564818354d8_v3_2_3_0").validate(obj)
    return True


def triggers_a_bugs_scan_for_the_supported_network_devices(api):
    endpoint_result = (
        api.compliance.triggers_a_bugs_scan_for_the_supported_network_devices(
            active_validation=True, failed_devices_only=True, payload=None
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_triggers_a_bugs_scan_for_the_supported_network_devices(api, validator):
    try:
        assert is_valid_triggers_a_bugs_scan_for_the_supported_network_devices(
            validator, triggers_a_bugs_scan_for_the_supported_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def triggers_a_bugs_scan_for_the_supported_network_devices_default_val(api):
    endpoint_result = (
        api.compliance.triggers_a_bugs_scan_for_the_supported_network_devices(
            active_validation=True, failed_devices_only=None, payload=None
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_triggers_a_bugs_scan_for_the_supported_network_devices_default_val(
    api, validator
):
    try:
        assert is_valid_triggers_a_bugs_scan_for_the_supported_network_devices(
            validator,
            triggers_a_bugs_scan_for_the_supported_network_devices_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_field_notices_affecting_the_network_device(
    json_schema_validate, obj
):
    json_schema_validate("jsd_63af749446fd572cbad63745a6d55c5a_v3_2_3_0").validate(obj)
    return True


def get_count_of_field_notices_affecting_the_network_device(api):
    endpoint_result = (
        api.compliance.get_count_of_field_notices_affecting_the_network_device(
            id="string", network_device_id="string", type="string"
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_field_notices_affecting_the_network_device(api, validator):
    try:
        assert is_valid_get_count_of_field_notices_affecting_the_network_device(
            validator, get_count_of_field_notices_affecting_the_network_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_field_notices_affecting_the_network_device_default_val(api):
    endpoint_result = (
        api.compliance.get_count_of_field_notices_affecting_the_network_device(
            id=None, network_device_id="string", type=None
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_field_notices_affecting_the_network_device_default_val(
    api, validator
):
    try:
        assert is_valid_get_count_of_field_notices_affecting_the_network_device(
            validator,
            get_count_of_field_notices_affecting_the_network_device_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_site_assignments_for_policy(json_schema_validate, obj):
    json_schema_validate("jsd_ff2c6d88250757ad836564779835dc3d_v3_2_3_0").validate(obj)
    return True


def retrieve_site_assignments_for_policy(api):
    endpoint_result = api.compliance.retrieve_site_assignments_for_policy(
        policy_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_site_assignments_for_policy(api, validator):
    try:
        assert is_valid_retrieve_site_assignments_for_policy(
            validator, retrieve_site_assignments_for_policy(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_site_assignments_for_policy_default_val(api):
    endpoint_result = api.compliance.retrieve_site_assignments_for_policy(
        policy_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_site_assignments_for_policy_default_val(api, validator):
    try:
        assert is_valid_retrieve_site_assignments_for_policy(
            validator, retrieve_site_assignments_for_policy_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_set_site_assignments_for_policy(json_schema_validate, obj):
    json_schema_validate("jsd_07eec9550d3b5c9c9a10e65c3ef2fc2d_v3_2_3_0").validate(obj)
    return True


def set_site_assignments_for_policy(api):
    endpoint_result = api.compliance.set_site_assignments_for_policy(
        active_validation=True, payload=None, policy_id="string", siteIds=["string"]
    )
    return endpoint_result


@pytest.mark.compliance
def test_set_site_assignments_for_policy(api, validator):
    try:
        assert is_valid_set_site_assignments_for_policy(
            validator, set_site_assignments_for_policy(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def set_site_assignments_for_policy_default_val(api):
    endpoint_result = api.compliance.set_site_assignments_for_policy(
        active_validation=True, payload=None, policy_id="string", siteIds=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_set_site_assignments_for_policy_default_val(api, validator):
    try:
        assert is_valid_set_site_assignments_for_policy(
            validator, set_site_assignments_for_policy_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_network_devices_for_a_policy(json_schema_validate, obj):
    json_schema_validate("jsd_6abd6cdcccf4570d9e140e919250a498_v3_2_3_0").validate(obj)
    return True


def retrieve_the_network_devices_for_a_policy(api):
    endpoint_result = api.compliance.retrieve_the_network_devices_for_a_policy(
        family="string",
        hostname="string",
        limit=0,
        management_address="string",
        offset=0,
        order="string",
        policy_id="string",
        role="string",
        site_id="string",
        sort_by="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_network_devices_for_a_policy(api, validator):
    try:
        assert is_valid_retrieve_the_network_devices_for_a_policy(
            validator, retrieve_the_network_devices_for_a_policy(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_network_devices_for_a_policy_default_val(api):
    endpoint_result = api.compliance.retrieve_the_network_devices_for_a_policy(
        family=None,
        hostname=None,
        limit=None,
        management_address=None,
        offset=None,
        order=None,
        policy_id="string",
        role=None,
        site_id="string",
        sort_by=None,
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_network_devices_for_a_policy_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_network_devices_for_a_policy(
            validator, retrieve_the_network_devices_for_a_policy_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_bugs_results_trend_over_time(json_schema_validate, obj):
    json_schema_validate("jsd_4ad7e992ab6a526196819e35eb0418a4_v3_2_3_0").validate(obj)
    return True


def get_network_bugs_results_trend_over_time(api):
    endpoint_result = api.compliance.get_network_bugs_results_trend_over_time(
        limit=0, offset=0, scan_time=0
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_network_bugs_results_trend_over_time(api, validator):
    try:
        assert is_valid_get_network_bugs_results_trend_over_time(
            validator, get_network_bugs_results_trend_over_time(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_bugs_results_trend_over_time_default_val(api):
    endpoint_result = api.compliance.get_network_bugs_results_trend_over_time(
        limit=None, offset=None, scan_time=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_network_bugs_results_trend_over_time_default_val(api, validator):
    try:
        assert is_valid_get_network_bugs_results_trend_over_time(
            validator, get_network_bugs_results_trend_over_time_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_bug_device_for_the_bug_by_network_device_id(
    json_schema_validate, obj
):
    json_schema_validate("jsd_c369b19255b95cffb73b8061e01a1f7d_v3_2_3_0").validate(obj)
    return True


def get_network_bug_device_for_the_bug_by_network_device_id(api):
    endpoint_result = (
        api.compliance.get_network_bug_device_for_the_bug_by_network_device_id(
            id="string", network_device_id="string"
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_network_bug_device_for_the_bug_by_network_device_id(api, validator):
    try:
        assert is_valid_get_network_bug_device_for_the_bug_by_network_device_id(
            validator, get_network_bug_device_for_the_bug_by_network_device_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_bug_device_for_the_bug_by_network_device_id_default_val(api):
    endpoint_result = (
        api.compliance.get_network_bug_device_for_the_bug_by_network_device_id(
            id="string", network_device_id="string"
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_network_bug_device_for_the_bug_by_network_device_id_default_val(
    api, validator
):
    try:
        assert is_valid_get_network_bug_device_for_the_bug_by_network_device_id(
            validator,
            get_network_bug_device_for_the_bug_by_network_device_id_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_field_notice_by_id(json_schema_validate, obj):
    json_schema_validate("jsd_485fc5e9ea9a5acd9e461b88355330ee_v3_2_3_0").validate(obj)
    return True


def get_field_notice_by_id(api):
    endpoint_result = api.compliance.get_field_notice_by_id(id="string")
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notice_by_id(api, validator):
    try:
        assert is_valid_get_field_notice_by_id(validator, get_field_notice_by_id(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_field_notice_by_id_default_val(api):
    endpoint_result = api.compliance.get_field_notice_by_id(id="string")
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notice_by_id_default_val(api, validator):
    try:
        assert is_valid_get_field_notice_by_id(
            validator, get_field_notice_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_config_task_details(json_schema_validate, obj):
    json_schema_validate("jsd_5cb73c1c44665d1ebbe934dd380f4f5e_v3_2_3_0").validate(obj)
    return True


def get_config_task_details(api):
    endpoint_result = api.compliance.get_config_task_details(parent_task_id="string")
    return endpoint_result


@pytest.mark.compliance
def test_get_config_task_details(api, validator):
    try:
        assert is_valid_get_config_task_details(validator, get_config_task_details(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_config_task_details_default_val(api):
    endpoint_result = api.compliance.get_config_task_details(parent_task_id=None)
    return endpoint_result


@pytest.mark.compliance
def test_get_config_task_details_default_val(api, validator):
    try:
        assert is_valid_get_config_task_details(
            validator, get_config_task_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_field_notice_affecting_the_network_device_by_device_id_and_notice_id(
    json_schema_validate, obj
):
    json_schema_validate("jsd_f585d782d15b54b89e227ab1d01e6f57_v3_2_3_0").validate(obj)
    return True


def get_field_notice_affecting_the_network_device_by_device_id_and_notice_id(api):
    endpoint_result = api.compliance.get_field_notice_affecting_the_network_device_by_device_id_and_notice_id(
        id="string", network_device_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notice_affecting_the_network_device_by_device_id_and_notice_id(
    api, validator
):
    try:
        assert is_valid_get_field_notice_affecting_the_network_device_by_device_id_and_notice_id(
            validator,
            get_field_notice_affecting_the_network_device_by_device_id_and_notice_id(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_field_notice_affecting_the_network_device_by_device_id_and_notice_id_default_val(
    api,
):
    endpoint_result = api.compliance.get_field_notice_affecting_the_network_device_by_device_id_and_notice_id(
        id="string", network_device_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notice_affecting_the_network_device_by_device_id_and_notice_id_default_val(
    api, validator
):
    try:
        assert is_valid_get_field_notice_affecting_the_network_device_by_device_id_and_notice_id(
            validator,
            get_field_notice_affecting_the_network_device_by_device_id_and_notice_id_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_a_device_with_the_violation(json_schema_validate, obj):
    json_schema_validate("jsd_ce54955e5909595ca8e3e0cc02b916ad_v3_2_3_0").validate(obj)
    return True


def retrieve_a_device_with_the_violation(api):
    endpoint_result = api.compliance.retrieve_a_device_with_the_violation(
        network_device_id="string",
        site_id="string",
        views="value1,value2",
        violation_id="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_a_device_with_the_violation(api, validator):
    try:
        assert is_valid_retrieve_a_device_with_the_violation(
            validator, retrieve_a_device_with_the_violation(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_a_device_with_the_violation_default_val(api):
    endpoint_result = api.compliance.retrieve_a_device_with_the_violation(
        network_device_id="string", site_id="string", views=None, violation_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_a_device_with_the_violation_default_val(api, validator):
    try:
        assert is_valid_retrieve_a_device_with_the_violation(
            validator, retrieve_a_device_with_the_violation_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_acknowledge_or_unacknowledge_compliance_violation(
    json_schema_validate, obj
):
    json_schema_validate("jsd_2a92d2ee095455fab90a717502a8138f_v3_2_3_0").validate(obj)
    return True


def acknowledge_or_unacknowledge_compliance_violation(api):
    endpoint_result = api.compliance.acknowledge_or_unacknowledge_compliance_violation(
        acknowledgementStatus="string",
        active_validation=True,
        network_device_id="string",
        payload=None,
        site_id="string",
        violation_id="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_acknowledge_or_unacknowledge_compliance_violation(api, validator):
    try:
        assert is_valid_acknowledge_or_unacknowledge_compliance_violation(
            validator, acknowledge_or_unacknowledge_compliance_violation(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def acknowledge_or_unacknowledge_compliance_violation_default_val(api):
    endpoint_result = api.compliance.acknowledge_or_unacknowledge_compliance_violation(
        acknowledgementStatus=None,
        active_validation=True,
        network_device_id="string",
        payload=None,
        site_id="string",
        violation_id="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_acknowledge_or_unacknowledge_compliance_violation_default_val(api, validator):
    try:
        assert is_valid_acknowledge_or_unacknowledge_compliance_violation(
            validator,
            acknowledge_or_unacknowledge_compliance_violation_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_network_bugs_results_trend_over_time(
    json_schema_validate, obj
):
    json_schema_validate("jsd_a240f89766435001b3ed25c3d23f0ffc_v3_2_3_0").validate(obj)
    return True


def get_count_of_network_bugs_results_trend_over_time(api):
    endpoint_result = api.compliance.get_count_of_network_bugs_results_trend_over_time(
        scan_time=0
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_network_bugs_results_trend_over_time(api, validator):
    try:
        assert is_valid_get_count_of_network_bugs_results_trend_over_time(
            validator, get_count_of_network_bugs_results_trend_over_time(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_network_bugs_results_trend_over_time_default_val(api):
    endpoint_result = api.compliance.get_count_of_network_bugs_results_trend_over_time(
        scan_time=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_network_bugs_results_trend_over_time_default_val(api, validator):
    try:
        assert is_valid_get_count_of_network_bugs_results_trend_over_time(
            validator,
            get_count_of_network_bugs_results_trend_over_time_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_field_notices(json_schema_validate, obj):
    json_schema_validate("jsd_2aa335c92d485537bab1126533ac8ed7_v3_2_3_0").validate(obj)
    return True


def get_field_notices(api):
    endpoint_result = api.compliance.get_field_notices(
        device_count=0,
        id="string",
        limit=0,
        offset=0,
        order="string",
        sort_by="string",
        type="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notices(api, validator):
    try:
        assert is_valid_get_field_notices(validator, get_field_notices(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_field_notices_default_val(api):
    endpoint_result = api.compliance.get_field_notices(
        device_count=None,
        id=None,
        limit=None,
        offset=None,
        order=None,
        sort_by=None,
        type=None,
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notices_default_val(api, validator):
    try:
        assert is_valid_get_field_notices(validator, get_field_notices_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_device_compliance_status(json_schema_validate, obj):
    json_schema_validate("jsd_41da8e5cdd435db0b1da1684be8f15b8_v3_2_3_0").validate(obj)
    return True


def device_compliance_status(api):
    endpoint_result = api.compliance.device_compliance_status(device_uuid="string")
    return endpoint_result


@pytest.mark.compliance
def test_device_compliance_status(api, validator):
    try:
        assert is_valid_device_compliance_status(
            validator, device_compliance_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def device_compliance_status_default_val(api):
    endpoint_result = api.compliance.device_compliance_status(device_uuid="string")
    return endpoint_result


@pytest.mark.compliance
def test_device_compliance_status_default_val(api, validator):
    try:
        assert is_valid_device_compliance_status(
            validator, device_compliance_status_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_acknowledge_or_unacknowledge_compliance_violation_know_your_network(
    json_schema_validate, obj
):
    json_schema_validate("jsd_9abae371b6465670965fb82b8ba220f1_v3_2_3_0").validate(obj)
    return True


def acknowledge_or_unacknowledge_compliance_violation_know_your_network(api):
    endpoint_result = api.compliance.acknowledge_or_unacknowledge_compliance_violation_know_your_network(
        acknowledgementStatus="string",
        active_validation=True,
        payload=None,
        site_id="string",
        violation_id="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_acknowledge_or_unacknowledge_compliance_violation_know_your_network(
    api, validator
):
    try:
        assert is_valid_acknowledge_or_unacknowledge_compliance_violation_know_your_network(
            validator,
            acknowledge_or_unacknowledge_compliance_violation_know_your_network(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def acknowledge_or_unacknowledge_compliance_violation_know_your_network_default_val(
    api,
):
    endpoint_result = api.compliance.acknowledge_or_unacknowledge_compliance_violation_know_your_network(
        acknowledgementStatus=None,
        active_validation=True,
        payload=None,
        site_id="string",
        violation_id="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_acknowledge_or_unacknowledge_compliance_violation_know_your_network_default_val(
    api, validator
):
    try:
        assert is_valid_acknowledge_or_unacknowledge_compliance_violation_know_your_network(
            validator,
            acknowledge_or_unacknowledge_compliance_violation_know_your_network_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_a_specific_violation(json_schema_validate, obj):
    json_schema_validate("jsd_3c5f95f551f95e70a362c5358996228c_v3_2_3_0").validate(obj)
    return True


def retrieve_a_specific_violation(api):
    endpoint_result = api.compliance.retrieve_a_specific_violation(
        site_id="string", violation_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_a_specific_violation(api, validator):
    try:
        assert is_valid_retrieve_a_specific_violation(
            validator, retrieve_a_specific_violation(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_a_specific_violation_default_val(api):
    endpoint_result = api.compliance.retrieve_a_specific_violation(
        site_id="string", violation_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_a_specific_violation_default_val(api, validator):
    try:
        assert is_valid_retrieve_a_specific_violation(
            validator, retrieve_a_specific_violation_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_security_advisory_network_devices(json_schema_validate, obj):
    json_schema_validate("jsd_9eb1f5f93d0d549cbf99e032a73db16d_v3_2_3_0").validate(obj)
    return True


def get_count_of_security_advisory_network_devices(api):
    endpoint_result = api.compliance.get_count_of_security_advisory_network_devices(
        advisory_count=0,
        network_device_id="string",
        scan_mode="string",
        scan_status="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_security_advisory_network_devices(api, validator):
    try:
        assert is_valid_get_count_of_security_advisory_network_devices(
            validator, get_count_of_security_advisory_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_security_advisory_network_devices_default_val(api):
    endpoint_result = api.compliance.get_count_of_security_advisory_network_devices(
        advisory_count=None, network_device_id=None, scan_mode=None, scan_status=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_security_advisory_network_devices_default_val(api, validator):
    try:
        assert is_valid_get_count_of_security_advisory_network_devices(
            validator, get_count_of_security_advisory_network_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_security_advisory_network_device_by_network_device_id(
    json_schema_validate, obj
):
    json_schema_validate("jsd_e22988bedfbb5202b1bab7e811d56f53_v3_2_3_0").validate(obj)
    return True


def get_security_advisory_network_device_by_network_device_id(api):
    endpoint_result = (
        api.compliance.get_security_advisory_network_device_by_network_device_id(
            network_device_id="string"
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisory_network_device_by_network_device_id(api, validator):
    try:
        assert is_valid_get_security_advisory_network_device_by_network_device_id(
            validator, get_security_advisory_network_device_by_network_device_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_security_advisory_network_device_by_network_device_id_default_val(api):
    endpoint_result = (
        api.compliance.get_security_advisory_network_device_by_network_device_id(
            network_device_id="string"
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisory_network_device_by_network_device_id_default_val(
    api, validator
):
    try:
        assert is_valid_get_security_advisory_network_device_by_network_device_id(
            validator,
            get_security_advisory_network_device_by_network_device_id_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_security_advisories_results_trend_over_time(json_schema_validate, obj):
    json_schema_validate("jsd_0c60e785a6915253b715d9416e684132_v3_2_3_0").validate(obj)
    return True


def get_security_advisories_results_trend_over_time(api):
    endpoint_result = api.compliance.get_security_advisories_results_trend_over_time(
        limit=0, offset=0, scan_time=0
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisories_results_trend_over_time(api, validator):
    try:
        assert is_valid_get_security_advisories_results_trend_over_time(
            validator, get_security_advisories_results_trend_over_time(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_security_advisories_results_trend_over_time_default_val(api):
    endpoint_result = api.compliance.get_security_advisories_results_trend_over_time(
        limit=None, offset=None, scan_time=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisories_results_trend_over_time_default_val(api, validator):
    try:
        assert is_valid_get_security_advisories_results_trend_over_time(
            validator, get_security_advisories_results_trend_over_time_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_count_of_rules(json_schema_validate, obj):
    json_schema_validate("jsd_58d0cf3341d554ccb0dab6a6444ad747_v3_2_3_0").validate(obj)
    return True


def retrieve_the_count_of_rules(api):
    endpoint_result = api.compliance.retrieve_the_count_of_rules(policy_id="string")
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_count_of_rules(api, validator):
    try:
        assert is_valid_retrieve_the_count_of_rules(
            validator, retrieve_the_count_of_rules(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_count_of_rules_default_val(api):
    endpoint_result = api.compliance.retrieve_the_count_of_rules(policy_id="string")
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_count_of_rules_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_count_of_rules(
            validator, retrieve_the_count_of_rules_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_field_notice_network_devices(json_schema_validate, obj):
    json_schema_validate("jsd_bf89c9e9897659e496ff2c2c2cfb8d35_v3_2_3_0").validate(obj)
    return True


def get_field_notice_network_devices(api):
    endpoint_result = api.compliance.get_field_notice_network_devices(
        limit=0,
        network_device_id="string",
        notice_count=0,
        offset=0,
        order="string",
        scan_status="string",
        sort_by="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notice_network_devices(api, validator):
    try:
        assert is_valid_get_field_notice_network_devices(
            validator, get_field_notice_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_field_notice_network_devices_default_val(api):
    endpoint_result = api.compliance.get_field_notice_network_devices(
        limit=None,
        network_device_id=None,
        notice_count=None,
        offset=None,
        order=None,
        scan_status=None,
        sort_by=None,
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notice_network_devices_default_val(api, validator):
    try:
        assert is_valid_get_field_notice_network_devices(
            validator, get_field_notice_network_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_bug_by_id(json_schema_validate, obj):
    json_schema_validate("jsd_90a7663a127d59d9afc45d4daa0ba477_v3_2_3_0").validate(obj)
    return True


def get_network_bug_by_id(api):
    endpoint_result = api.compliance.get_network_bug_by_id(id="string")
    return endpoint_result


@pytest.mark.compliance
def test_get_network_bug_by_id(api, validator):
    try:
        assert is_valid_get_network_bug_by_id(validator, get_network_bug_by_id(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_bug_by_id_default_val(api):
    endpoint_result = api.compliance.get_network_bug_by_id(id="string")
    return endpoint_result


@pytest.mark.compliance
def test_get_network_bug_by_id_default_val(api, validator):
    try:
        assert is_valid_get_network_bug_by_id(
            validator, get_network_bug_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_policies_know_your_network(json_schema_validate, obj):
    json_schema_validate("jsd_31203fc1ac335ec88048f947a992b318_v3_2_3_0").validate(obj)
    return True


def retrieve_the_policies_know_your_network(api):
    endpoint_result = api.compliance.retrieve_the_policies_know_your_network(
        limit=0,
        offset=0,
        order="string",
        policy_name="string",
        site_id="string",
        sort_by="string",
        status="value1,value2",
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_policies_know_your_network(api, validator):
    try:
        assert is_valid_retrieve_the_policies_know_your_network(
            validator, retrieve_the_policies_know_your_network(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_policies_know_your_network_default_val(api):
    endpoint_result = api.compliance.retrieve_the_policies_know_your_network(
        limit=None,
        offset=None,
        order=None,
        policy_name=None,
        site_id="string",
        sort_by=None,
        status=None,
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_policies_know_your_network_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_policies_know_your_network(
            validator, retrieve_the_policies_know_your_network_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_run_compliance(json_schema_validate, obj):
    json_schema_validate("jsd_0802306a0a8d545698d1d59a9be90e51_v3_2_3_0").validate(obj)
    return True


def run_compliance(api):
    endpoint_result = api.compliance.run_compliance(
        active_validation=True,
        categories=["string"],
        deviceUuids=["string"],
        payload=None,
        triggerFull=True,
    )
    return endpoint_result


@pytest.mark.compliance
def test_run_compliance(api, validator):
    try:
        assert is_valid_run_compliance(validator, run_compliance(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def run_compliance_default_val(api):
    endpoint_result = api.compliance.run_compliance(
        active_validation=True,
        categories=None,
        deviceUuids=None,
        payload=None,
        triggerFull=None,
    )
    return endpoint_result


@pytest.mark.compliance
def test_run_compliance_default_val(api, validator):
    try:
        assert is_valid_run_compliance(validator, run_compliance_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_bug_devices_for_the_bug(json_schema_validate, obj):
    json_schema_validate("jsd_25d10f773fa5522384790bf1f198d861_v3_2_3_0").validate(obj)
    return True


def get_network_bug_devices_for_the_bug(api):
    endpoint_result = api.compliance.get_network_bug_devices_for_the_bug(
        id="string",
        limit=0,
        network_device_id="string",
        offset=0,
        order="string",
        scan_mode="string",
        scan_status="string",
        sort_by="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_network_bug_devices_for_the_bug(api, validator):
    try:
        assert is_valid_get_network_bug_devices_for_the_bug(
            validator, get_network_bug_devices_for_the_bug(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_bug_devices_for_the_bug_default_val(api):
    endpoint_result = api.compliance.get_network_bug_devices_for_the_bug(
        id="string",
        limit=None,
        network_device_id=None,
        offset=None,
        order=None,
        scan_mode=None,
        scan_status=None,
        sort_by=None,
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_network_bug_devices_for_the_bug_default_val(api, validator):
    try:
        assert is_valid_get_network_bug_devices_for_the_bug(
            validator, get_network_bug_devices_for_the_bug_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_security_advisories_results_trend_over_time(
    json_schema_validate, obj
):
    json_schema_validate("jsd_7259f083e6be591181051e43aebe7c7d_v3_2_3_0").validate(obj)
    return True


def get_count_of_security_advisories_results_trend_over_time(api):
    endpoint_result = (
        api.compliance.get_count_of_security_advisories_results_trend_over_time(
            scan_time=0
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_security_advisories_results_trend_over_time(api, validator):
    try:
        assert is_valid_get_count_of_security_advisories_results_trend_over_time(
            validator, get_count_of_security_advisories_results_trend_over_time(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_security_advisories_results_trend_over_time_default_val(api):
    endpoint_result = (
        api.compliance.get_count_of_security_advisories_results_trend_over_time(
            scan_time=None
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_security_advisories_results_trend_over_time_default_val(
    api, validator
):
    try:
        assert is_valid_get_count_of_security_advisories_results_trend_over_time(
            validator,
            get_count_of_security_advisories_results_trend_over_time_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_count_of_variables(json_schema_validate, obj):
    json_schema_validate("jsd_818a2a2ac82e53aeba856542a343a6d7_v3_2_3_0").validate(obj)
    return True


def retrieve_the_count_of_variables(api):
    endpoint_result = api.compliance.retrieve_the_count_of_variables(
        policy_id="string", rule_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_count_of_variables(api, validator):
    try:
        assert is_valid_retrieve_the_count_of_variables(
            validator, retrieve_the_count_of_variables(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_count_of_variables_default_val(api):
    endpoint_result = api.compliance.retrieve_the_count_of_variables(
        policy_id="string", rule_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_count_of_variables_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_count_of_variables(
            validator, retrieve_the_count_of_variables_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_security_advisory_network_devices(json_schema_validate, obj):
    json_schema_validate("jsd_60b210c3633d5cfe8127056abae805c7_v3_2_3_0").validate(obj)
    return True


def get_security_advisory_network_devices(api):
    endpoint_result = api.compliance.get_security_advisory_network_devices(
        advisory_count="string",
        limit=0,
        network_device_id="string",
        offset=0,
        order="string",
        scan_mode="string",
        scan_status="string",
        sort_by="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisory_network_devices(api, validator):
    try:
        assert is_valid_get_security_advisory_network_devices(
            validator, get_security_advisory_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_security_advisory_network_devices_default_val(api):
    endpoint_result = api.compliance.get_security_advisory_network_devices(
        advisory_count=None,
        limit=None,
        network_device_id=None,
        offset=None,
        order=None,
        scan_mode=None,
        scan_status=None,
        sort_by=None,
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisory_network_devices_default_val(api, validator):
    try:
        assert is_valid_get_security_advisory_network_devices(
            validator, get_security_advisory_network_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_policy_violations(json_schema_validate, obj):
    json_schema_validate("jsd_f77405fe5d3f59b2b05445d36358adaf_v3_2_3_0").validate(obj)
    return True


def retrieve_the_policy_violations(api):
    endpoint_result = api.compliance.retrieve_the_policy_violations(
        limit=0, network_device_id="string", offset=0, policy_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_policy_violations(api, validator):
    try:
        assert is_valid_retrieve_the_policy_violations(
            validator, retrieve_the_policy_violations(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_policy_violations_default_val(api):
    endpoint_result = api.compliance.retrieve_the_policy_violations(
        limit=None, network_device_id="string", offset=None, policy_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_policy_violations_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_policy_violations(
            validator, retrieve_the_policy_violations_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_violations_summary(json_schema_validate, obj):
    json_schema_validate("jsd_0803794da89a5e8193015a65b1494098_v3_2_3_0").validate(obj)
    return True


def retrieve_the_violations_summary(api):
    endpoint_result = api.compliance.retrieve_the_violations_summary(
        acknowledgement_status="string",
        compliance_types="value1,value2",
        site_id="string",
        sub_types="value1,value2",
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_violations_summary(api, validator):
    try:
        assert is_valid_retrieve_the_violations_summary(
            validator, retrieve_the_violations_summary(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_violations_summary_default_val(api):
    endpoint_result = api.compliance.retrieve_the_violations_summary(
        acknowledgement_status=None,
        compliance_types=None,
        site_id="string",
        sub_types=None,
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_violations_summary_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_violations_summary(
            validator, retrieve_the_violations_summary_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_violations_for_a_policy(json_schema_validate, obj):
    json_schema_validate("jsd_687a36e07ec15593902e55f5f0296772_v3_2_3_0").validate(obj)
    return True


def retrieve_the_violations_for_a_policy(api):
    endpoint_result = api.compliance.retrieve_the_violations_for_a_policy(
        hostname="string",
        limit=0,
        management_address="string",
        offset=0,
        order="string",
        policy_id="string",
        rule_id="string",
        rule_name="string",
        site_id="string",
        sort_by="string",
        violation_message="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_violations_for_a_policy(api, validator):
    try:
        assert is_valid_retrieve_the_violations_for_a_policy(
            validator, retrieve_the_violations_for_a_policy(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_violations_for_a_policy_default_val(api):
    endpoint_result = api.compliance.retrieve_the_violations_for_a_policy(
        hostname=None,
        limit=None,
        management_address=None,
        offset=None,
        order=None,
        policy_id="string",
        rule_id=None,
        rule_name=None,
        site_id="string",
        sort_by=None,
        violation_message=None,
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_violations_for_a_policy_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_violations_for_a_policy(
            validator, retrieve_the_violations_for_a_policy_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_compliance_details_of_network_devices(
    json_schema_validate, obj
):
    json_schema_validate("jsd_1e539a3b94ca52afbf6c7fd185c50b81_v3_2_3_0").validate(obj)
    return True


def retrieve_the_compliance_details_of_network_devices(api):
    endpoint_result = api.compliance.retrieve_the_compliance_details_of_network_devices(
        compliance_types="value1,value2",
        limit=0,
        network_device_id="string",
        offset=0,
        severity="string",
        site_id="string",
        status="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_compliance_details_of_network_devices(api, validator):
    try:
        assert is_valid_retrieve_the_compliance_details_of_network_devices(
            validator, retrieve_the_compliance_details_of_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_compliance_details_of_network_devices_default_val(api):
    endpoint_result = api.compliance.retrieve_the_compliance_details_of_network_devices(
        compliance_types=None,
        limit=None,
        network_device_id=None,
        offset=None,
        severity=None,
        site_id="string",
        status=None,
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_compliance_details_of_network_devices_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_compliance_details_of_network_devices(
            validator,
            retrieve_the_compliance_details_of_network_devices_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_triggers_a_field_notices_scan_for_the_supported_network_devices(
    json_schema_validate, obj
):
    json_schema_validate("jsd_8fd0f9b4adc5572da4ccc64802a275f5_v3_2_3_0").validate(obj)
    return True


def triggers_a_field_notices_scan_for_the_supported_network_devices(api):
    endpoint_result = (
        api.compliance.triggers_a_field_notices_scan_for_the_supported_network_devices(
            active_validation=True, failed_devices_only=True, payload=None
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_triggers_a_field_notices_scan_for_the_supported_network_devices(
    api, validator
):
    try:
        assert is_valid_triggers_a_field_notices_scan_for_the_supported_network_devices(
            validator,
            triggers_a_field_notices_scan_for_the_supported_network_devices(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def triggers_a_field_notices_scan_for_the_supported_network_devices_default_val(api):
    endpoint_result = (
        api.compliance.triggers_a_field_notices_scan_for_the_supported_network_devices(
            active_validation=True, failed_devices_only=None, payload=None
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_triggers_a_field_notices_scan_for_the_supported_network_devices_default_val(
    api, validator
):
    try:
        assert is_valid_triggers_a_field_notices_scan_for_the_supported_network_devices(
            validator,
            triggers_a_field_notices_scan_for_the_supported_network_devices_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_compliance_status_count(json_schema_validate, obj):
    json_schema_validate("jsd_079c37ce8136584f9e2ed471fc896ef9_v3_2_3_0").validate(obj)
    return True


def get_compliance_status_count(api):
    endpoint_result = api.compliance.get_compliance_status_count(
        compliance_status="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_compliance_status_count(api, validator):
    try:
        assert is_valid_get_compliance_status_count(
            validator, get_compliance_status_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_compliance_status_count_default_val(api):
    endpoint_result = api.compliance.get_compliance_status_count(compliance_status=None)
    return endpoint_result


@pytest.mark.compliance
def test_get_compliance_status_count_default_val(api, validator):
    try:
        assert is_valid_get_compliance_status_count(
            validator, get_compliance_status_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_compliance_status(json_schema_validate, obj):
    json_schema_validate("jsd_4a1de7ff46fa5da09c5051c06ad07f2c_v3_2_3_0").validate(obj)
    return True


def get_compliance_status(api):
    endpoint_result = api.compliance.get_compliance_status(
        compliance_status="string", device_uuid="string", limit=0, offset=0
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_compliance_status(api, validator):
    try:
        assert is_valid_get_compliance_status(validator, get_compliance_status(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_compliance_status_default_val(api):
    endpoint_result = api.compliance.get_compliance_status(
        compliance_status=None, device_uuid=None, limit=None, offset=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_compliance_status_default_val(api, validator):
    try:
        assert is_valid_get_compliance_status(
            validator, get_compliance_status_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_security_advisories_affecting_the_network_device(
    json_schema_validate, obj
):
    json_schema_validate("jsd_a12932efe27956de8c356e40e959d6c2_v3_2_3_0").validate(obj)
    return True


def get_count_of_security_advisories_affecting_the_network_device(api):
    endpoint_result = (
        api.compliance.get_count_of_security_advisories_affecting_the_network_device(
            cvss_base_score="string",
            id="string",
            network_device_id="string",
            security_impact_rating="string",
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_security_advisories_affecting_the_network_device(api, validator):
    try:
        assert is_valid_get_count_of_security_advisories_affecting_the_network_device(
            validator,
            get_count_of_security_advisories_affecting_the_network_device(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_security_advisories_affecting_the_network_device_default_val(api):
    endpoint_result = (
        api.compliance.get_count_of_security_advisories_affecting_the_network_device(
            cvss_base_score=None,
            id=None,
            network_device_id="string",
            security_impact_rating=None,
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_security_advisories_affecting_the_network_device_default_val(
    api, validator
):
    try:
        assert is_valid_get_count_of_security_advisories_affecting_the_network_device(
            validator,
            get_count_of_security_advisories_affecting_the_network_device_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_bug_affecting_the_network_device_by_device_id_and_bug_id(
    json_schema_validate, obj
):
    json_schema_validate("jsd_3beba27ea019536da45eef3cade3ab67_v3_2_3_0").validate(obj)
    return True


def get_bug_affecting_the_network_device_by_device_id_and_bug_id(api):
    endpoint_result = (
        api.compliance.get_bug_affecting_the_network_device_by_device_id_and_bug_id(
            id="string", network_device_id="string"
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_bug_affecting_the_network_device_by_device_id_and_bug_id(api, validator):
    try:
        assert is_valid_get_bug_affecting_the_network_device_by_device_id_and_bug_id(
            validator, get_bug_affecting_the_network_device_by_device_id_and_bug_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_bug_affecting_the_network_device_by_device_id_and_bug_id_default_val(api):
    endpoint_result = (
        api.compliance.get_bug_affecting_the_network_device_by_device_id_and_bug_id(
            id="string", network_device_id="string"
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_bug_affecting_the_network_device_by_device_id_and_bug_id_default_val(
    api, validator
):
    try:
        assert is_valid_get_bug_affecting_the_network_device_by_device_id_and_bug_id(
            validator,
            get_bug_affecting_the_network_device_by_device_id_and_bug_id_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_field_notice_network_device_for_the_notice_by_network_device_id(
    json_schema_validate, obj
):
    json_schema_validate("jsd_04e9343c828f586da856c48c8edee40b_v3_2_3_0").validate(obj)
    return True


def get_field_notice_network_device_for_the_notice_by_network_device_id(api):
    endpoint_result = api.compliance.get_field_notice_network_device_for_the_notice_by_network_device_id(
        id="string", network_device_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notice_network_device_for_the_notice_by_network_device_id(
    api, validator
):
    try:
        assert is_valid_get_field_notice_network_device_for_the_notice_by_network_device_id(
            validator,
            get_field_notice_network_device_for_the_notice_by_network_device_id(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_field_notice_network_device_for_the_notice_by_network_device_id_default_val(
    api,
):
    endpoint_result = api.compliance.get_field_notice_network_device_for_the_notice_by_network_device_id(
        id="string", network_device_id="string"
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notice_network_device_for_the_notice_by_network_device_id_default_val(
    api, validator
):
    try:
        assert is_valid_get_field_notice_network_device_for_the_notice_by_network_device_id(
            validator,
            get_field_notice_network_device_for_the_notice_by_network_device_id_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_devices_with_the_violation(json_schema_validate, obj):
    json_schema_validate("jsd_074754ea16365f6faf5651e268e45e06_v3_2_3_0").validate(obj)
    return True


def retrieve_the_devices_with_the_violation(api):
    endpoint_result = api.compliance.retrieve_the_devices_with_the_violation(
        family="string",
        hostname="string",
        limit=0,
        management_address="string",
        offset=0,
        order="string",
        role="string",
        site_id="string",
        sort_by="string",
        violation_id="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_devices_with_the_violation(api, validator):
    try:
        assert is_valid_retrieve_the_devices_with_the_violation(
            validator, retrieve_the_devices_with_the_violation(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_devices_with_the_violation_default_val(api):
    endpoint_result = api.compliance.retrieve_the_devices_with_the_violation(
        family=None,
        hostname=None,
        limit=None,
        management_address=None,
        offset=None,
        order=None,
        role=None,
        site_id="string",
        sort_by=None,
        violation_id="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_retrieve_the_devices_with_the_violation_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_devices_with_the_violation(
            validator, retrieve_the_devices_with_the_violation_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_field_notice_network_devices_for_the_notice(json_schema_validate, obj):
    json_schema_validate("jsd_6e015bf018f55499a59aae5c54264bf4_v3_2_3_0").validate(obj)
    return True


def get_field_notice_network_devices_for_the_notice(api):
    endpoint_result = api.compliance.get_field_notice_network_devices_for_the_notice(
        id="string",
        limit=0,
        network_device_id="string",
        offset=0,
        order="string",
        scan_status="string",
        sort_by="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notice_network_devices_for_the_notice(api, validator):
    try:
        assert is_valid_get_field_notice_network_devices_for_the_notice(
            validator, get_field_notice_network_devices_for_the_notice(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_field_notice_network_devices_for_the_notice_default_val(api):
    endpoint_result = api.compliance.get_field_notice_network_devices_for_the_notice(
        id="string",
        limit=None,
        network_device_id=None,
        offset=None,
        order=None,
        scan_status=None,
        sort_by=None,
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notice_network_devices_for_the_notice_default_val(api, validator):
    try:
        assert is_valid_get_field_notice_network_devices_for_the_notice(
            validator, get_field_notice_network_devices_for_the_notice_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_network_bug_devices(json_schema_validate, obj):
    json_schema_validate("jsd_9aab9fd032d15280ac99b00b34600781_v3_2_3_0").validate(obj)
    return True


def get_count_of_network_bug_devices(api):
    endpoint_result = api.compliance.get_count_of_network_bug_devices(
        bug_count=0,
        network_device_id="string",
        scan_mode="string",
        scan_status="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_network_bug_devices(api, validator):
    try:
        assert is_valid_get_count_of_network_bug_devices(
            validator, get_count_of_network_bug_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_network_bug_devices_default_val(api):
    endpoint_result = api.compliance.get_count_of_network_bug_devices(
        bug_count=None, network_device_id=None, scan_mode=None, scan_status=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_network_bug_devices_default_val(api, validator):
    try:
        assert is_valid_get_count_of_network_bug_devices(
            validator, get_count_of_network_bug_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_field_notices_affecting_the_network_device(json_schema_validate, obj):
    json_schema_validate("jsd_f44a1efb2d0f53209fdc441a3bbf073f_v3_2_3_0").validate(obj)
    return True


def get_field_notices_affecting_the_network_device(api):
    endpoint_result = api.compliance.get_field_notices_affecting_the_network_device(
        id="string",
        limit=0,
        network_device_id="string",
        offset=0,
        order="string",
        sort_by="string",
        type="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notices_affecting_the_network_device(api, validator):
    try:
        assert is_valid_get_field_notices_affecting_the_network_device(
            validator, get_field_notices_affecting_the_network_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_field_notices_affecting_the_network_device_default_val(api):
    endpoint_result = api.compliance.get_field_notices_affecting_the_network_device(
        id=None,
        limit=None,
        network_device_id="string",
        offset=None,
        order=None,
        sort_by=None,
        type=None,
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notices_affecting_the_network_device_default_val(api, validator):
    try:
        assert is_valid_get_field_notices_affecting_the_network_device(
            validator, get_field_notices_affecting_the_network_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_security_advisories_affecting_the_network_devices(
    json_schema_validate, obj
):
    json_schema_validate("jsd_aef04c74f2745a6ca3960d6c466856cf_v3_2_3_0").validate(obj)
    return True


def get_security_advisories_affecting_the_network_devices(api):
    endpoint_result = (
        api.compliance.get_security_advisories_affecting_the_network_devices(
            cvss_base_score="string",
            device_count=0,
            id="string",
            limit=0,
            offset=0,
            order="string",
            security_impact_rating="string",
            sort_by="string",
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisories_affecting_the_network_devices(api, validator):
    try:
        assert is_valid_get_security_advisories_affecting_the_network_devices(
            validator, get_security_advisories_affecting_the_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_security_advisories_affecting_the_network_devices_default_val(api):
    endpoint_result = (
        api.compliance.get_security_advisories_affecting_the_network_devices(
            cvss_base_score=None,
            device_count=None,
            id=None,
            limit=None,
            offset=None,
            order=None,
            security_impact_rating=None,
            sort_by=None,
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisories_affecting_the_network_devices_default_val(
    api, validator
):
    try:
        assert is_valid_get_security_advisories_affecting_the_network_devices(
            validator,
            get_security_advisories_affecting_the_network_devices_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_security_advisory_network_devices_for_the_security_advisory(
    json_schema_validate, obj
):
    json_schema_validate("jsd_d14f6e201c475f33a92d0222d76d40df_v3_2_3_0").validate(obj)
    return True


def get_security_advisory_network_devices_for_the_security_advisory(api):
    endpoint_result = (
        api.compliance.get_security_advisory_network_devices_for_the_security_advisory(
            id="string",
            limit=0,
            network_device_id="string",
            offset=0,
            order="string",
            scan_mode="string",
            scan_status="string",
            sort_by="string",
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisory_network_devices_for_the_security_advisory(
    api, validator
):
    try:
        assert is_valid_get_security_advisory_network_devices_for_the_security_advisory(
            validator,
            get_security_advisory_network_devices_for_the_security_advisory(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_security_advisory_network_devices_for_the_security_advisory_default_val(api):
    endpoint_result = (
        api.compliance.get_security_advisory_network_devices_for_the_security_advisory(
            id="string",
            limit=None,
            network_device_id=None,
            offset=None,
            order=None,
            scan_mode=None,
            scan_status=None,
            sort_by=None,
        )
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisory_network_devices_for_the_security_advisory_default_val(
    api, validator
):
    try:
        assert is_valid_get_security_advisory_network_devices_for_the_security_advisory(
            validator,
            get_security_advisory_network_devices_for_the_security_advisory_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_bug_devices(json_schema_validate, obj):
    json_schema_validate("jsd_2f6011b1d24c53d1aa7dda9e0d3ee29b_v3_2_3_0").validate(obj)
    return True


def get_network_bug_devices(api):
    endpoint_result = api.compliance.get_network_bug_devices(
        bug_count=0,
        limit=0,
        network_device_id="string",
        offset=0,
        order="string",
        scan_mode="string",
        scan_status="string",
        sort_by="string",
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_network_bug_devices(api, validator):
    try:
        assert is_valid_get_network_bug_devices(validator, get_network_bug_devices(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_bug_devices_default_val(api):
    endpoint_result = api.compliance.get_network_bug_devices(
        bug_count=None,
        limit=None,
        network_device_id=None,
        offset=None,
        order=None,
        scan_mode=None,
        scan_status=None,
        sort_by=None,
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_network_bug_devices_default_val(api, validator):
    try:
        assert is_valid_get_network_bug_devices(
            validator, get_network_bug_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
