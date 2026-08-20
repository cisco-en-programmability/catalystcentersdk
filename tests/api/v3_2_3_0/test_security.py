"""CatalystCenterAPI security API fixtures and tests.

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


def is_valid_retrieve_the_count_of_traffic_steering_policies(json_schema_validate, obj):
    json_schema_validate("jsd_917a4a399bbf5999a8736ff4b6c6c82e_v3_2_3_0").validate(obj)
    return True


def retrieve_the_count_of_traffic_steering_policies(api):
    endpoint_result = api.security.retrieve_the_count_of_traffic_steering_policies(
        site_id="string"
    )
    return endpoint_result


@pytest.mark.security
def test_retrieve_the_count_of_traffic_steering_policies(api, validator):
    try:
        assert is_valid_retrieve_the_count_of_traffic_steering_policies(
            validator, retrieve_the_count_of_traffic_steering_policies(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_count_of_traffic_steering_policies_default_val(api):
    endpoint_result = api.security.retrieve_the_count_of_traffic_steering_policies(
        site_id=None
    )
    return endpoint_result


@pytest.mark.security
def test_retrieve_the_count_of_traffic_steering_policies_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_count_of_traffic_steering_policies(
            validator, retrieve_the_count_of_traffic_steering_policies_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_a_traffic_steering_contract(json_schema_validate, obj):
    json_schema_validate("jsd_6045561687145e63bf0ae35131894563_v3_2_3_0").validate(obj)
    return True


def delete_a_traffic_steering_contract(api):
    endpoint_result = api.security.delete_a_traffic_steering_contract(id="string")
    return endpoint_result


@pytest.mark.security
def test_delete_a_traffic_steering_contract(api, validator):
    try:
        assert is_valid_delete_a_traffic_steering_contract(
            validator, delete_a_traffic_steering_contract(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_a_traffic_steering_contract_default_val(api):
    endpoint_result = api.security.delete_a_traffic_steering_contract(id="string")
    return endpoint_result


@pytest.mark.security
def test_delete_a_traffic_steering_contract_default_val(api, validator):
    try:
        assert is_valid_delete_a_traffic_steering_contract(
            validator, delete_a_traffic_steering_contract_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_modify_a_traffic_steering_contract(json_schema_validate, obj):
    json_schema_validate("jsd_091d53bf319d5e4984e4fc65ab016726_v3_2_3_0").validate(obj)
    return True


def modify_a_traffic_steering_contract(api):
    endpoint_result = api.security.modify_a_traffic_steering_contract(
        active_validation=True,
        createdTime=0,
        description="string",
        id="string",
        lastUpdatedTime=0,
        name="string",
        payload=None,
        policyReferenceCount=0,
        ruleCount=0,
        rules=[
            {
                "applicationName": "string",
                "logging": True,
                "destinationNetworkIdentities": {},
                "sourceNetworkIdentities": {},
            }
        ],
        siteReferenceCount=0,
    )
    return endpoint_result


@pytest.mark.security
def test_modify_a_traffic_steering_contract(api, validator):
    try:
        assert is_valid_modify_a_traffic_steering_contract(
            validator, modify_a_traffic_steering_contract(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def modify_a_traffic_steering_contract_default_val(api):
    endpoint_result = api.security.modify_a_traffic_steering_contract(
        active_validation=True,
        createdTime=None,
        description=None,
        id="string",
        lastUpdatedTime=None,
        name=None,
        payload=None,
        policyReferenceCount=None,
        ruleCount=None,
        rules=None,
        siteReferenceCount=None,
    )
    return endpoint_result


@pytest.mark.security
def test_modify_a_traffic_steering_contract_default_val(api, validator):
    try:
        assert is_valid_modify_a_traffic_steering_contract(
            validator, modify_a_traffic_steering_contract_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_a_traffic_steering_contract_by_its_id(json_schema_validate, obj):
    json_schema_validate("jsd_37cbd1deda0a53669c2546c954403c59_v3_2_3_0").validate(obj)
    return True


def retrieve_a_traffic_steering_contract_by_its_id(api):
    endpoint_result = api.security.retrieve_a_traffic_steering_contract_by_its_id(
        id="string", views="string"
    )
    return endpoint_result


@pytest.mark.security
def test_retrieve_a_traffic_steering_contract_by_its_id(api, validator):
    try:
        assert is_valid_retrieve_a_traffic_steering_contract_by_its_id(
            validator, retrieve_a_traffic_steering_contract_by_its_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_a_traffic_steering_contract_by_its_id_default_val(api):
    endpoint_result = api.security.retrieve_a_traffic_steering_contract_by_its_id(
        id="string", views=None
    )
    return endpoint_result


@pytest.mark.security
def test_retrieve_a_traffic_steering_contract_by_its_id_default_val(api, validator):
    try:
        assert is_valid_retrieve_a_traffic_steering_contract_by_its_id(
            validator, retrieve_a_traffic_steering_contract_by_its_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_top_n_analytics_data_related_to_contracts(
    json_schema_validate, obj
):
    json_schema_validate("jsd_ecaa42b157d557e7bc770de8e04a5f7c_v3_2_3_0").validate(obj)
    return True


def retrieves_the_top_n_analytics_data_related_to_contracts(api):
    endpoint_result = (
        api.security.retrieves_the_top_n_analytics_data_related_to_contracts(
            limit=0, offset=0, order="string", sort_by="string"
        )
    )
    return endpoint_result


@pytest.mark.security
def test_retrieves_the_top_n_analytics_data_related_to_contracts(api, validator):
    try:
        assert is_valid_retrieves_the_top_n_analytics_data_related_to_contracts(
            validator, retrieves_the_top_n_analytics_data_related_to_contracts(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_top_n_analytics_data_related_to_contracts_default_val(api):
    endpoint_result = (
        api.security.retrieves_the_top_n_analytics_data_related_to_contracts(
            limit=None, offset=None, order=None, sort_by=None
        )
    )
    return endpoint_result


@pytest.mark.security
def test_retrieves_the_top_n_analytics_data_related_to_contracts_default_val(
    api, validator
):
    try:
        assert is_valid_retrieves_the_top_n_analytics_data_related_to_contracts(
            validator,
            retrieves_the_top_n_analytics_data_related_to_contracts_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_top_n_analytics_data_related_to_nodes(
    json_schema_validate, obj
):
    json_schema_validate("jsd_2ef26dc241f55b2b9d3e73aaafe20e46_v3_2_3_0").validate(obj)
    return True


def retrieves_the_top_n_analytics_data_related_to_nodes(api):
    endpoint_result = api.security.retrieves_the_top_n_analytics_data_related_to_nodes(
        limit=0, offset=0, order="string", sort_by="string"
    )
    return endpoint_result


@pytest.mark.security
def test_retrieves_the_top_n_analytics_data_related_to_nodes(api, validator):
    try:
        assert is_valid_retrieves_the_top_n_analytics_data_related_to_nodes(
            validator, retrieves_the_top_n_analytics_data_related_to_nodes(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_top_n_analytics_data_related_to_nodes_default_val(api):
    endpoint_result = api.security.retrieves_the_top_n_analytics_data_related_to_nodes(
        limit=None, offset=None, order=None, sort_by=None
    )
    return endpoint_result


@pytest.mark.security
def test_retrieves_the_top_n_analytics_data_related_to_nodes_default_val(
    api, validator
):
    try:
        assert is_valid_retrieves_the_top_n_analytics_data_related_to_nodes(
            validator,
            retrieves_the_top_n_analytics_data_related_to_nodes_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_traffic_steering_contracts(json_schema_validate, obj):
    json_schema_validate("jsd_c931889d86105c9998e82db6c2576e09_v3_2_3_0").validate(obj)
    return True


def retrieve_traffic_steering_contracts(api):
    endpoint_result = api.security.retrieve_traffic_steering_contracts(
        limit=0,
        name="string",
        offset=0,
        order="string",
        sort_by="string",
        views="string",
    )
    return endpoint_result


@pytest.mark.security
def test_retrieve_traffic_steering_contracts(api, validator):
    try:
        assert is_valid_retrieve_traffic_steering_contracts(
            validator, retrieve_traffic_steering_contracts(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_traffic_steering_contracts_default_val(api):
    endpoint_result = api.security.retrieve_traffic_steering_contracts(
        limit=None, name=None, offset=None, order=None, sort_by=None, views=None
    )
    return endpoint_result


@pytest.mark.security
def test_retrieve_traffic_steering_contracts_default_val(api, validator):
    try:
        assert is_valid_retrieve_traffic_steering_contracts(
            validator, retrieve_traffic_steering_contracts_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_creates_a_traffic_steering_contract(json_schema_validate, obj):
    json_schema_validate("jsd_34472953861f5414a7c5818844cb4d1a_v3_2_3_0").validate(obj)
    return True


def creates_a_traffic_steering_contract(api):
    endpoint_result = api.security.creates_a_traffic_steering_contract(
        active_validation=True,
        createdTime=0,
        description="string",
        id="string",
        lastUpdatedTime=0,
        name="string",
        payload=None,
        policyReferenceCount=0,
        ruleCount=0,
        rules=[
            {
                "applicationName": "string",
                "logging": True,
                "destinationNetworkIdentities": {},
                "sourceNetworkIdentities": {},
            }
        ],
        siteReferenceCount=0,
    )
    return endpoint_result


@pytest.mark.security
def test_creates_a_traffic_steering_contract(api, validator):
    try:
        assert is_valid_creates_a_traffic_steering_contract(
            validator, creates_a_traffic_steering_contract(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def creates_a_traffic_steering_contract_default_val(api):
    endpoint_result = api.security.creates_a_traffic_steering_contract(
        active_validation=True,
        createdTime=None,
        description=None,
        id=None,
        lastUpdatedTime=None,
        name=None,
        payload=None,
        policyReferenceCount=None,
        ruleCount=None,
        rules=None,
        siteReferenceCount=None,
    )
    return endpoint_result


@pytest.mark.security
def test_creates_a_traffic_steering_contract_default_val(api, validator):
    try:
        assert is_valid_creates_a_traffic_steering_contract(
            validator, creates_a_traffic_steering_contract_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_a_steering_policy(json_schema_validate, obj):
    json_schema_validate("jsd_86fedddf05435682aeb8606e13d00ecd_v3_2_3_0").validate(obj)
    return True


def update_a_steering_policy(api):
    endpoint_result = api.security.update_a_steering_policy(
        active_validation=True,
        contractId="string",
        contractName="string",
        createdTime=0,
        destinationId="string",
        destinationName="string",
        id="string",
        lastUpdatedTime=0,
        payload=None,
        siteId="string",
        sourceId="string",
        sourceName="string",
        virtualNetworkFirewall=[
            {
                "firewallIpAddress": "string",
                "subnetMask": 0,
                "firewallName": "string",
                "virtualNetworkName": "string",
                "virtualNetworkId": 0,
            }
        ],
        virtualNetworkFirewallCount=0,
    )
    return endpoint_result


@pytest.mark.security
def test_update_a_steering_policy(api, validator):
    try:
        assert is_valid_update_a_steering_policy(
            validator, update_a_steering_policy(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_a_steering_policy_default_val(api):
    endpoint_result = api.security.update_a_steering_policy(
        active_validation=True,
        contractId=None,
        contractName=None,
        createdTime=None,
        destinationId=None,
        destinationName=None,
        id="string",
        lastUpdatedTime=None,
        payload=None,
        siteId=None,
        sourceId=None,
        sourceName=None,
        virtualNetworkFirewall=None,
        virtualNetworkFirewallCount=None,
    )
    return endpoint_result


@pytest.mark.security
def test_update_a_steering_policy_default_val(api, validator):
    try:
        assert is_valid_update_a_steering_policy(
            validator, update_a_steering_policy_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_a_traffic_steering_policy(json_schema_validate, obj):
    json_schema_validate("jsd_a45d7e58f4175ebd9df1322f769150f7_v3_2_3_0").validate(obj)
    return True


def retrieve_a_traffic_steering_policy(api):
    endpoint_result = api.security.retrieve_a_traffic_steering_policy(
        id="string", views="string"
    )
    return endpoint_result


@pytest.mark.security
def test_retrieve_a_traffic_steering_policy(api, validator):
    try:
        assert is_valid_retrieve_a_traffic_steering_policy(
            validator, retrieve_a_traffic_steering_policy(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_a_traffic_steering_policy_default_val(api):
    endpoint_result = api.security.retrieve_a_traffic_steering_policy(
        id="string", views=None
    )
    return endpoint_result


@pytest.mark.security
def test_retrieve_a_traffic_steering_policy_default_val(api, validator):
    try:
        assert is_valid_retrieve_a_traffic_steering_policy(
            validator, retrieve_a_traffic_steering_policy_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_a_steering_policy(json_schema_validate, obj):
    json_schema_validate("jsd_9b86a66f5a355cbe8727b5026f3e2386_v3_2_3_0").validate(obj)
    return True


def delete_a_steering_policy(api):
    endpoint_result = api.security.delete_a_steering_policy(id="string")
    return endpoint_result


@pytest.mark.security
def test_delete_a_steering_policy(api, validator):
    try:
        assert is_valid_delete_a_steering_policy(
            validator, delete_a_steering_policy(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_a_steering_policy_default_val(api):
    endpoint_result = api.security.delete_a_steering_policy(id="string")
    return endpoint_result


@pytest.mark.security
def test_delete_a_steering_policy_default_val(api, validator):
    try:
        assert is_valid_delete_a_steering_policy(
            validator, delete_a_steering_policy_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_the_count_of_traffic_steering_contracts(
    json_schema_validate, obj
):
    json_schema_validate("jsd_5ab4f06dfba25e38993beb7dc6c40e17_v3_2_3_0").validate(obj)
    return True


def retrieve_the_count_of_traffic_steering_contracts(api):
    endpoint_result = api.security.retrieve_the_count_of_traffic_steering_contracts()
    return endpoint_result


@pytest.mark.security
def test_retrieve_the_count_of_traffic_steering_contracts(api, validator):
    try:
        assert is_valid_retrieve_the_count_of_traffic_steering_contracts(
            validator, retrieve_the_count_of_traffic_steering_contracts(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_the_count_of_traffic_steering_contracts_default_val(api):
    endpoint_result = api.security.retrieve_the_count_of_traffic_steering_contracts()
    return endpoint_result


@pytest.mark.security
def test_retrieve_the_count_of_traffic_steering_contracts_default_val(api, validator):
    try:
        assert is_valid_retrieve_the_count_of_traffic_steering_contracts(
            validator, retrieve_the_count_of_traffic_steering_contracts_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_creates_a_traffic_steering_policy(json_schema_validate, obj):
    json_schema_validate("jsd_d965a3ad0a645aa3951189baf7329480_v3_2_3_0").validate(obj)
    return True


def creates_a_traffic_steering_policy(api):
    endpoint_result = api.security.creates_a_traffic_steering_policy(
        active_validation=True,
        contractId="string",
        contractName="string",
        createdTime=0,
        destinationId="string",
        destinationName="string",
        id="string",
        lastUpdatedTime=0,
        payload=None,
        siteId="string",
        sourceId="string",
        sourceName="string",
        virtualNetworkFirewall=[
            {
                "firewallIpAddress": "string",
                "subnetMask": 0,
                "firewallName": "string",
                "virtualNetworkName": "string",
                "virtualNetworkId": 0,
            }
        ],
        virtualNetworkFirewallCount=0,
    )
    return endpoint_result


@pytest.mark.security
def test_creates_a_traffic_steering_policy(api, validator):
    try:
        assert is_valid_creates_a_traffic_steering_policy(
            validator, creates_a_traffic_steering_policy(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def creates_a_traffic_steering_policy_default_val(api):
    endpoint_result = api.security.creates_a_traffic_steering_policy(
        active_validation=True,
        contractId=None,
        contractName=None,
        createdTime=None,
        destinationId=None,
        destinationName=None,
        id=None,
        lastUpdatedTime=None,
        payload=None,
        siteId=None,
        sourceId=None,
        sourceName=None,
        virtualNetworkFirewall=None,
        virtualNetworkFirewallCount=None,
    )
    return endpoint_result


@pytest.mark.security
def test_creates_a_traffic_steering_policy_default_val(api, validator):
    try:
        assert is_valid_creates_a_traffic_steering_policy(
            validator, creates_a_traffic_steering_policy_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieve_traffic_steering_policies(json_schema_validate, obj):
    json_schema_validate("jsd_ef1b2329f56e51b69b02e8f913c87e6b_v3_2_3_0").validate(obj)
    return True


def retrieve_traffic_steering_policies(api):
    endpoint_result = api.security.retrieve_traffic_steering_policies(
        contract_name="string",
        destination_name="string",
        limit=0,
        offset=0,
        order="string",
        site_id="string",
        sort_by="string",
        source_name="string",
        views="string",
    )
    return endpoint_result


@pytest.mark.security
def test_retrieve_traffic_steering_policies(api, validator):
    try:
        assert is_valid_retrieve_traffic_steering_policies(
            validator, retrieve_traffic_steering_policies(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieve_traffic_steering_policies_default_val(api):
    endpoint_result = api.security.retrieve_traffic_steering_policies(
        contract_name=None,
        destination_name=None,
        limit=None,
        offset=None,
        order=None,
        site_id=None,
        sort_by=None,
        source_name=None,
        views=None,
    )
    return endpoint_result


@pytest.mark.security
def test_retrieve_traffic_steering_policies_default_val(api, validator):
    try:
        assert is_valid_retrieve_traffic_steering_policies(
            validator, retrieve_traffic_steering_policies_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_multiple_traffic_steering_policies_in_bulk(
    json_schema_validate, obj
):
    json_schema_validate("jsd_084ebc24be555d90b775c0070622ce24_v3_2_3_0").validate(obj)
    return True


def create_multiple_traffic_steering_policies_in_bulk(api):
    endpoint_result = api.security.create_multiple_traffic_steering_policies_in_bulk(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.security
def test_create_multiple_traffic_steering_policies_in_bulk(api, validator):
    try:
        assert is_valid_create_multiple_traffic_steering_policies_in_bulk(
            validator, create_multiple_traffic_steering_policies_in_bulk(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_multiple_traffic_steering_policies_in_bulk_default_val(api):
    endpoint_result = api.security.create_multiple_traffic_steering_policies_in_bulk(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.security
def test_create_multiple_traffic_steering_policies_in_bulk_default_val(api, validator):
    try:
        assert is_valid_create_multiple_traffic_steering_policies_in_bulk(
            validator,
            create_multiple_traffic_steering_policies_in_bulk_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_top_n_analytics_data_related_to_firewalls(
    json_schema_validate, obj
):
    json_schema_validate("jsd_14cb0938df3f5602ae040dd1e42920e2_v3_2_3_0").validate(obj)
    return True


def retrieves_the_top_n_analytics_data_related_to_firewalls(api):
    endpoint_result = (
        api.security.retrieves_the_top_n_analytics_data_related_to_firewalls(
            limit=0, offset=0, order="string", sort_by="string"
        )
    )
    return endpoint_result


@pytest.mark.security
def test_retrieves_the_top_n_analytics_data_related_to_firewalls(api, validator):
    try:
        assert is_valid_retrieves_the_top_n_analytics_data_related_to_firewalls(
            validator, retrieves_the_top_n_analytics_data_related_to_firewalls(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_top_n_analytics_data_related_to_firewalls_default_val(api):
    endpoint_result = (
        api.security.retrieves_the_top_n_analytics_data_related_to_firewalls(
            limit=None, offset=None, order=None, sort_by=None
        )
    )
    return endpoint_result


@pytest.mark.security
def test_retrieves_the_top_n_analytics_data_related_to_firewalls_default_val(
    api, validator
):
    try:
        assert is_valid_retrieves_the_top_n_analytics_data_related_to_firewalls(
            validator,
            retrieves_the_top_n_analytics_data_related_to_firewalls_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
