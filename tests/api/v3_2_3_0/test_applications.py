"""CatalystCenterAPI applications API fixtures and tests.

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


def is_valid_retrieves_the_list_of_network_applications_along_with_experience_and_health_metrics(
    json_schema_validate, obj
):
    json_schema_validate("jsd_fb02436a6c935d5d8a536b86de8b2846_v3_2_3_0").validate(obj)
    return True


def retrieves_the_list_of_network_applications_along_with_experience_and_health_metrics(
    api,
):
    endpoint_result = api.applications.retrieves_the_list_of_network_applications_along_with_experience_and_health_metrics(
        application_name="string",
        attribute="string",
        business_relevance="string",
        end_time=0,
        exporter_network_device_id="string",
        health_score=0,
        limit=0,
        offset=0,
        order="string",
        site_id="string",
        sort_by="string",
        ssid="string",
        start_time=0,
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_the_list_of_network_applications_along_with_experience_and_health_metrics(
    api, validator
):
    try:
        assert is_valid_retrieves_the_list_of_network_applications_along_with_experience_and_health_metrics(
            validator,
            retrieves_the_list_of_network_applications_along_with_experience_and_health_metrics(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_list_of_network_applications_along_with_experience_and_health_metrics_default_val(
    api,
):
    endpoint_result = api.applications.retrieves_the_list_of_network_applications_along_with_experience_and_health_metrics(
        application_name=None,
        attribute=None,
        business_relevance=None,
        end_time=None,
        exporter_network_device_id=None,
        health_score=None,
        limit=None,
        offset=None,
        order=None,
        site_id=None,
        sort_by=None,
        ssid=None,
        start_time=None,
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_the_list_of_network_applications_along_with_experience_and_health_metrics_default_val(
    api, validator
):
    try:
        assert is_valid_retrieves_the_list_of_network_applications_along_with_experience_and_health_metrics(
            validator,
            retrieves_the_list_of_network_applications_along_with_experience_and_health_metrics_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_the_trend_analytics_data_for_thousand_eyes_test_results_in_the_specified_time_range(
    json_schema_validate, obj
):
    json_schema_validate("jsd_42af0e7bab8659f19c619fae31772d15_v3_2_3_0").validate(obj)
    return True


def the_trend_analytics_data_for_thousand_eyes_test_results_in_the_specified_time_range(
    api,
):
    endpoint_result = api.applications.the_trend_analytics_data_for_thousand_eyes_test_results_in_the_specified_time_range(
        agent_id="string",
        attribute="string",
        end_time=0,
        limit=0,
        network_device_name="string",
        offset=0,
        order="string",
        site_id="string",
        start_time=0,
        test_id="string",
        test_name="string",
        test_type="string",
        trend_interval="string",
    )
    return endpoint_result


@pytest.mark.applications
def test_the_trend_analytics_data_for_thousand_eyes_test_results_in_the_specified_time_range(
    api, validator
):
    try:
        assert is_valid_the_trend_analytics_data_for_thousand_eyes_test_results_in_the_specified_time_range(
            validator,
            the_trend_analytics_data_for_thousand_eyes_test_results_in_the_specified_time_range(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def the_trend_analytics_data_for_thousand_eyes_test_results_in_the_specified_time_range_default_val(
    api,
):
    endpoint_result = api.applications.the_trend_analytics_data_for_thousand_eyes_test_results_in_the_specified_time_range(
        agent_id=None,
        attribute=None,
        end_time=None,
        limit=None,
        network_device_name=None,
        offset=None,
        order=None,
        site_id=None,
        start_time=None,
        test_id=None,
        test_name=None,
        test_type=None,
        trend_interval=None,
    )
    return endpoint_result


@pytest.mark.applications
def test_the_trend_analytics_data_for_thousand_eyes_test_results_in_the_specified_time_range_default_val(
    api, validator
):
    try:
        assert is_valid_the_trend_analytics_data_for_thousand_eyes_test_results_in_the_specified_time_range(
            validator,
            the_trend_analytics_data_for_thousand_eyes_test_results_in_the_specified_time_range_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_list_of_thousand_eyes_test_results_along_with_related_metrics(
    json_schema_validate, obj
):
    json_schema_validate("jsd_a499ab977fea5c139c9344227c7769a5_v3_2_3_0").validate(obj)
    return True


def retrieves_the_list_of_thousand_eyes_test_results_along_with_related_metrics(api):
    endpoint_result = api.applications.retrieves_the_list_of_thousand_eyes_test_results_along_with_related_metrics(
        agent_id="string",
        attribute="string",
        end_time=0,
        limit=0,
        network_device_name="string",
        offset=0,
        order="string",
        site_id="string",
        sort_by="string",
        start_time=0,
        test_id="string",
        test_name="string",
        test_type="string",
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_the_list_of_thousand_eyes_test_results_along_with_related_metrics(
    api, validator
):
    try:
        assert is_valid_retrieves_the_list_of_thousand_eyes_test_results_along_with_related_metrics(
            validator,
            retrieves_the_list_of_thousand_eyes_test_results_along_with_related_metrics(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_list_of_thousand_eyes_test_results_along_with_related_metrics_default_val(
    api,
):
    endpoint_result = api.applications.retrieves_the_list_of_thousand_eyes_test_results_along_with_related_metrics(
        agent_id=None,
        attribute=None,
        end_time=None,
        limit=None,
        network_device_name=None,
        offset=None,
        order=None,
        site_id=None,
        sort_by=None,
        start_time=None,
        test_id=None,
        test_name=None,
        test_type=None,
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_the_list_of_thousand_eyes_test_results_along_with_related_metrics_default_val(
    api, validator
):
    try:
        assert is_valid_retrieves_the_list_of_thousand_eyes_test_results_along_with_related_metrics(
            validator,
            retrieves_the_list_of_thousand_eyes_test_results_along_with_related_metrics_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_total_count_of_thousand_eyes_test_results(
    json_schema_validate, obj
):
    json_schema_validate("jsd_ef366ca484355d15937dd851a67c88e3_v3_2_3_0").validate(obj)
    return True


def retrieves_the_total_count_of_thousand_eyes_test_results(api):
    endpoint_result = (
        api.applications.retrieves_the_total_count_of_thousand_eyes_test_results(
            agent_id="string",
            end_time=0,
            network_device_name="string",
            site_id="string",
            start_time=0,
            test_id="string",
            test_name="string",
            test_type="string",
        )
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_the_total_count_of_thousand_eyes_test_results(api, validator):
    try:
        assert is_valid_retrieves_the_total_count_of_thousand_eyes_test_results(
            validator, retrieves_the_total_count_of_thousand_eyes_test_results(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_total_count_of_thousand_eyes_test_results_default_val(api):
    endpoint_result = (
        api.applications.retrieves_the_total_count_of_thousand_eyes_test_results(
            agent_id=None,
            end_time=None,
            network_device_name=None,
            site_id=None,
            start_time=None,
            test_id=None,
            test_name=None,
            test_type=None,
        )
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_the_total_count_of_thousand_eyes_test_results_default_val(
    api, validator
):
    try:
        assert is_valid_retrieves_the_total_count_of_thousand_eyes_test_results(
            validator,
            retrieves_the_total_count_of_thousand_eyes_test_results_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_total_count_of_network_applications_by_applying_basic_filtering(
    json_schema_validate, obj
):
    json_schema_validate("jsd_43c50def6b3a58e5acab3ae592a57da8_v3_2_3_0").validate(obj)
    return True


def retrieves_the_total_count_of_network_applications_by_applying_basic_filtering(api):
    endpoint_result = api.applications.retrieves_the_total_count_of_network_applications_by_applying_basic_filtering(
        application_name="string",
        business_relevance="string",
        end_time=0,
        exporter_network_device_id="string",
        health_score=0,
        site_id="string",
        ssid="string",
        start_time=0,
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_the_total_count_of_network_applications_by_applying_basic_filtering(
    api, validator
):
    try:
        assert is_valid_retrieves_the_total_count_of_network_applications_by_applying_basic_filtering(
            validator,
            retrieves_the_total_count_of_network_applications_by_applying_basic_filtering(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_total_count_of_network_applications_by_applying_basic_filtering_default_val(
    api,
):
    endpoint_result = api.applications.retrieves_the_total_count_of_network_applications_by_applying_basic_filtering(
        application_name=None,
        business_relevance=None,
        end_time=None,
        exporter_network_device_id=None,
        health_score=None,
        site_id=None,
        ssid=None,
        start_time=None,
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_the_total_count_of_network_applications_by_applying_basic_filtering_default_val(
    api, validator
):
    try:
        assert is_valid_retrieves_the_total_count_of_network_applications_by_applying_basic_filtering(
            validator,
            retrieves_the_total_count_of_network_applications_by_applying_basic_filtering_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_summary_analytics_data_related_to_network_applications_along_with_health_metrics(
    json_schema_validate, obj
):
    json_schema_validate("jsd_ded95db0af275081801b54e0ce105c71_v3_2_3_0").validate(obj)
    return True


def retrieves_summary_analytics_data_related_to_network_applications_along_with_health_metrics(
    api,
):
    endpoint_result = api.applications.retrieves_summary_analytics_data_related_to_network_applications_along_with_health_metrics(
        active_validation=True,
        aggregateAttributes=[{"name": "string", "function": "string"}],
        attributes=["string"],
        endTime=0,
        filters=[{"key": "string", "operator": "string", "value": 0}],
        page={
            "limit": 0,
            "offset": 0,
            "cursor": "string",
            "sortBy": [{"name": "string", "function": "string", "order": "string"}],
        },
        payload=None,
        siteIds=["string"],
        startTime=0,
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_summary_analytics_data_related_to_network_applications_along_with_health_metrics(
    api, validator
):
    try:
        assert is_valid_retrieves_summary_analytics_data_related_to_network_applications_along_with_health_metrics(
            validator,
            retrieves_summary_analytics_data_related_to_network_applications_along_with_health_metrics(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_summary_analytics_data_related_to_network_applications_along_with_health_metrics_default_val(
    api,
):
    endpoint_result = api.applications.retrieves_summary_analytics_data_related_to_network_applications_along_with_health_metrics(
        active_validation=True,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        page=None,
        payload=None,
        siteIds=None,
        startTime=None,
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_summary_analytics_data_related_to_network_applications_along_with_health_metrics_default_val(
    api, validator
):
    try:
        assert is_valid_retrieves_summary_analytics_data_related_to_network_applications_along_with_health_metrics(
            validator,
            retrieves_summary_analytics_data_related_to_network_applications_along_with_health_metrics_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_trend_analytics_data_related_to_network_applications(
    json_schema_validate, obj
):
    json_schema_validate("jsd_154870476ce35f19bc4c1d058aa01536_v3_2_3_0").validate(obj)
    return True


def retrieves_the_trend_analytics_data_related_to_network_applications(api):
    endpoint_result = api.applications.retrieves_the_trend_analytics_data_related_to_network_applications(
        active_validation=True,
        aggregateAttributes=[{"name": "string", "function": "string"}],
        attributes=["string"],
        endTime=0,
        filters=[{"key": "string", "operator": "string", "value": 0}],
        groupBy=["string"],
        page={"limit": 0, "cursor": "string", "timeSortOrder": "string"},
        payload=None,
        siteIds=["string"],
        startTime=0,
        trendInterval="string",
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_the_trend_analytics_data_related_to_network_applications(
    api, validator
):
    try:
        assert (
            is_valid_retrieves_the_trend_analytics_data_related_to_network_applications(
                validator,
                retrieves_the_trend_analytics_data_related_to_network_applications(api),
            )
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_trend_analytics_data_related_to_network_applications_default_val(api):
    endpoint_result = api.applications.retrieves_the_trend_analytics_data_related_to_network_applications(
        active_validation=True,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        page=None,
        payload=None,
        siteIds=None,
        startTime=None,
        trendInterval=None,
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_the_trend_analytics_data_related_to_network_applications_default_val(
    api, validator
):
    try:
        assert is_valid_retrieves_the_trend_analytics_data_related_to_network_applications(
            validator,
            retrieves_the_trend_analytics_data_related_to_network_applications_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_list_of_clients_metrics_for_the_given_application(
    json_schema_validate, obj
):
    json_schema_validate("jsd_6a8102ea97535f25b4919d714a3af5d3_v3_2_3_0").validate(obj)
    return True


def retrieves_the_list_of_clients_metrics_for_the_given_application(api):
    endpoint_result = api.applications.retrieves_the_list_of_clients_metrics_for_the_given_application(
        attribute="string",
        end_time=0,
        exporter_network_device_id="string",
        id="string",
        limit=0,
        offset=0,
        order="string",
        site_id="string",
        sort_by="string",
        start_time=0,
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_the_list_of_clients_metrics_for_the_given_application(
    api, validator
):
    try:
        assert is_valid_retrieves_the_list_of_clients_metrics_for_the_given_application(
            validator,
            retrieves_the_list_of_clients_metrics_for_the_given_application(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_list_of_clients_metrics_for_the_given_application_default_val(api):
    endpoint_result = api.applications.retrieves_the_list_of_clients_metrics_for_the_given_application(
        attribute=None,
        end_time=None,
        exporter_network_device_id=None,
        id="string",
        limit=None,
        offset=None,
        order=None,
        site_id=None,
        sort_by=None,
        start_time=None,
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_the_list_of_clients_metrics_for_the_given_application_default_val(
    api, validator
):
    try:
        assert is_valid_retrieves_the_list_of_clients_metrics_for_the_given_application(
            validator,
            retrieves_the_list_of_clients_metrics_for_the_given_application_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_bulk_update_application_health_score_definitions(
    json_schema_validate, obj
):
    json_schema_validate("jsd_6cfff77e00e75fc6a3970bf71bf9e0b8_v3_2_3_0").validate(obj)
    return True


def bulk_update_application_health_score_definitions(api):
    endpoint_result = api.applications.bulk_update_application_health_score_definitions(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.applications
def test_bulk_update_application_health_score_definitions(api, validator):
    try:
        assert is_valid_bulk_update_application_health_score_definitions(
            validator, bulk_update_application_health_score_definitions(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def bulk_update_application_health_score_definitions_default_val(api):
    endpoint_result = api.applications.bulk_update_application_health_score_definitions(
        active_validation=True, payload=None
    )
    return endpoint_result


@pytest.mark.applications
def test_bulk_update_application_health_score_definitions_default_val(api, validator):
    try:
        assert is_valid_bulk_update_application_health_score_definitions(
            validator, bulk_update_application_health_score_definitions_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_application_health_score_definition_for_the_given_id(
    json_schema_validate, obj
):
    json_schema_validate("jsd_119a776c50bb5fb397e47d3e5f63a371_v3_2_3_0").validate(obj)
    return True


def update_application_health_score_definition_for_the_given_id(api):
    endpoint_result = (
        api.applications.update_application_health_score_definition_for_the_given_id(
            active_validation=True,
            badDefaultValue=0,
            badMaxValue=0,
            badMinValue=0,
            badValue=0,
            definitionType="string",
            goodDefaultValue=0,
            goodMaxValue=0,
            goodMinValue=0,
            goodValue=0,
            greatDefaultValue=0,
            greatMaxValue=0,
            greatMinValue=0,
            greatValue=0,
            id="string",
            includeForHealthScore=True,
            includeForHealthScoreDefault=True,
            kpiName="string",
            lastModified=0,
            payload=None,
            poorDefaultValue=0,
            poorMaxValue=0,
            poorMinValue=0,
            poorValue=0,
            trafficClass="string",
            unit="string",
            weightDefaultValue=0,
            weightValue=0,
        )
    )
    return endpoint_result


@pytest.mark.applications
def test_update_application_health_score_definition_for_the_given_id(api, validator):
    try:
        assert is_valid_update_application_health_score_definition_for_the_given_id(
            validator, update_application_health_score_definition_for_the_given_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_application_health_score_definition_for_the_given_id_default_val(api):
    endpoint_result = (
        api.applications.update_application_health_score_definition_for_the_given_id(
            active_validation=True,
            badDefaultValue=None,
            badMaxValue=None,
            badMinValue=None,
            badValue=None,
            definitionType=None,
            goodDefaultValue=None,
            goodMaxValue=None,
            goodMinValue=None,
            goodValue=None,
            greatDefaultValue=None,
            greatMaxValue=None,
            greatMinValue=None,
            greatValue=None,
            id="string",
            includeForHealthScore=None,
            includeForHealthScoreDefault=None,
            kpiName=None,
            lastModified=None,
            payload=None,
            poorDefaultValue=None,
            poorMaxValue=None,
            poorMinValue=None,
            poorValue=None,
            trafficClass=None,
            unit=None,
            weightDefaultValue=None,
            weightValue=None,
        )
    )
    return endpoint_result


@pytest.mark.applications
def test_update_application_health_score_definition_for_the_given_id_default_val(
    api, validator
):
    try:
        assert is_valid_update_application_health_score_definition_for_the_given_id(
            validator,
            update_application_health_score_definition_for_the_given_id_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_application_health_score_definition_for_the_given_id(
    json_schema_validate, obj
):
    json_schema_validate("jsd_b01c993595cb5d8e9cfc55b92f4dd7e7_v3_2_3_0").validate(obj)
    return True


def get_application_health_score_definition_for_the_given_id(api):
    endpoint_result = (
        api.applications.get_application_health_score_definition_for_the_given_id(
            attribute="string", id="string"
        )
    )
    return endpoint_result


@pytest.mark.applications
def test_get_application_health_score_definition_for_the_given_id(api, validator):
    try:
        assert is_valid_get_application_health_score_definition_for_the_given_id(
            validator, get_application_health_score_definition_for_the_given_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_application_health_score_definition_for_the_given_id_default_val(api):
    endpoint_result = (
        api.applications.get_application_health_score_definition_for_the_given_id(
            attribute=None, id="string"
        )
    )
    return endpoint_result


@pytest.mark.applications
def test_get_application_health_score_definition_for_the_given_id_default_val(
    api, validator
):
    try:
        assert is_valid_get_application_health_score_definition_for_the_given_id(
            validator,
            get_application_health_score_definition_for_the_given_id_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_counts_the_number_of_path_traces_for_the_given_thousand_eyes_test_result(
    json_schema_validate, obj
):
    json_schema_validate("jsd_821b73ac9ff65584bb0971d3e7d4d656_v3_2_3_0").validate(obj)
    return True


def counts_the_number_of_path_traces_for_the_given_thousand_eyes_test_result(api):
    endpoint_result = api.applications.counts_the_number_of_path_traces_for_the_given_thousand_eyes_test_result(
        client_mac_address="string", id="string"
    )
    return endpoint_result


@pytest.mark.applications
def test_counts_the_number_of_path_traces_for_the_given_thousand_eyes_test_result(
    api, validator
):
    try:
        assert is_valid_counts_the_number_of_path_traces_for_the_given_thousand_eyes_test_result(
            validator,
            counts_the_number_of_path_traces_for_the_given_thousand_eyes_test_result(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def counts_the_number_of_path_traces_for_the_given_thousand_eyes_test_result_default_val(
    api,
):
    endpoint_result = api.applications.counts_the_number_of_path_traces_for_the_given_thousand_eyes_test_result(
        client_mac_address=None, id="string"
    )
    return endpoint_result


@pytest.mark.applications
def test_counts_the_number_of_path_traces_for_the_given_thousand_eyes_test_result_default_val(
    api, validator
):
    try:
        assert is_valid_counts_the_number_of_path_traces_for_the_given_thousand_eyes_test_result(
            validator,
            counts_the_number_of_path_traces_for_the_given_thousand_eyes_test_result_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_all_application_health_score_definitions(json_schema_validate, obj):
    json_schema_validate("jsd_09775ac6832a5e6790991958bedebcd4_v3_2_3_0").validate(obj)
    return True


def get_all_application_health_score_definitions(api):
    endpoint_result = api.applications.get_all_application_health_score_definitions(
        attribute="string",
        include_for_health_score=True,
        limit=0,
        offset=0,
        traffic_class="string",
    )
    return endpoint_result


@pytest.mark.applications
def test_get_all_application_health_score_definitions(api, validator):
    try:
        assert is_valid_get_all_application_health_score_definitions(
            validator, get_all_application_health_score_definitions(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_application_health_score_definitions_default_val(api):
    endpoint_result = api.applications.get_all_application_health_score_definitions(
        attribute=None,
        include_for_health_score=None,
        limit=None,
        offset=None,
        traffic_class=None,
    )
    return endpoint_result


@pytest.mark.applications
def test_get_all_application_health_score_definitions_default_val(api, validator):
    try:
        assert is_valid_get_all_application_health_score_definitions(
            validator, get_all_application_health_score_definitions_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_the_count_of_application_health_score_definitions(
    json_schema_validate, obj
):
    json_schema_validate("jsd_f35518c9315f5a94872a8e062f717011_v3_2_3_0").validate(obj)
    return True


def get_the_count_of_application_health_score_definitions(api):
    endpoint_result = (
        api.applications.get_the_count_of_application_health_score_definitions(
            include_for_health_score=True, traffic_class="string"
        )
    )
    return endpoint_result


@pytest.mark.applications
def test_get_the_count_of_application_health_score_definitions(api, validator):
    try:
        assert is_valid_get_the_count_of_application_health_score_definitions(
            validator, get_the_count_of_application_health_score_definitions(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_the_count_of_application_health_score_definitions_default_val(api):
    endpoint_result = (
        api.applications.get_the_count_of_application_health_score_definitions(
            include_for_health_score=None, traffic_class=None
        )
    )
    return endpoint_result


@pytest.mark.applications
def test_get_the_count_of_application_health_score_definitions_default_val(
    api, validator
):
    try:
        assert is_valid_get_the_count_of_application_health_score_definitions(
            validator,
            get_the_count_of_application_health_score_definitions_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_trend_analytics_related_to_specific_network_application(
    json_schema_validate, obj
):
    json_schema_validate("jsd_755b33956f3e56c6b8d234e7ed6a20e6_v3_2_3_0").validate(obj)
    return True


def retrieves_the_trend_analytics_related_to_specific_network_application(api):
    endpoint_result = api.applications.retrieves_the_trend_analytics_related_to_specific_network_application(
        active_validation=True,
        aggregateAttributes=[{"name": "string", "function": "string"}],
        attributes=["string"],
        endTime=0,
        filters=[{"key": "string", "operator": "string", "value": "string"}],
        id="string",
        page={"limit": 0, "cursor": "string", "timeSortOrder": "string"},
        payload=None,
        siteIds=["string"],
        startTime=0,
        trendInterval="string",
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_the_trend_analytics_related_to_specific_network_application(
    api, validator
):
    try:
        assert is_valid_retrieves_the_trend_analytics_related_to_specific_network_application(
            validator,
            retrieves_the_trend_analytics_related_to_specific_network_application(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_trend_analytics_related_to_specific_network_application_default_val(
    api,
):
    endpoint_result = api.applications.retrieves_the_trend_analytics_related_to_specific_network_application(
        active_validation=True,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        id="string",
        page=None,
        payload=None,
        siteIds=None,
        startTime=None,
        trendInterval=None,
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_the_trend_analytics_related_to_specific_network_application_default_val(
    api, validator
):
    try:
        assert is_valid_retrieves_the_trend_analytics_related_to_specific_network_application(
            validator,
            retrieves_the_trend_analytics_related_to_specific_network_application_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_list_of_path_traces_for_the_given_thousand_eyes_test_result(
    json_schema_validate, obj
):
    json_schema_validate("jsd_6c616c07cbda559194d82311fb2ec7cc_v3_2_3_0").validate(obj)
    return True


def retrieves_the_list_of_path_traces_for_the_given_thousand_eyes_test_result(api):
    endpoint_result = api.applications.retrieves_the_list_of_path_traces_for_the_given_thousand_eyes_test_result(
        client_mac_address="string", id="string"
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_the_list_of_path_traces_for_the_given_thousand_eyes_test_result(
    api, validator
):
    try:
        assert is_valid_retrieves_the_list_of_path_traces_for_the_given_thousand_eyes_test_result(
            validator,
            retrieves_the_list_of_path_traces_for_the_given_thousand_eyes_test_result(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_list_of_path_traces_for_the_given_thousand_eyes_test_result_default_val(
    api,
):
    endpoint_result = api.applications.retrieves_the_list_of_path_traces_for_the_given_thousand_eyes_test_result(
        client_mac_address=None, id="string"
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_the_list_of_path_traces_for_the_given_thousand_eyes_test_result_default_val(
    api, validator
):
    try:
        assert is_valid_retrieves_the_list_of_path_traces_for_the_given_thousand_eyes_test_result(
            validator,
            retrieves_the_list_of_path_traces_for_the_given_thousand_eyes_test_result_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_client_count_for_the_given_application(
    json_schema_validate, obj
):
    json_schema_validate("jsd_7b36ae8285d45e3da3c22e1d77eb2bb2_v3_2_3_0").validate(obj)
    return True


def retrieves_the_client_count_for_the_given_application(api):
    endpoint_result = (
        api.applications.retrieves_the_client_count_for_the_given_application(
            end_time=0,
            exporter_network_device_id="string",
            id="string",
            site_id="string",
            start_time=0,
        )
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_the_client_count_for_the_given_application(api, validator):
    try:
        assert is_valid_retrieves_the_client_count_for_the_given_application(
            validator, retrieves_the_client_count_for_the_given_application(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_client_count_for_the_given_application_default_val(api):
    endpoint_result = (
        api.applications.retrieves_the_client_count_for_the_given_application(
            end_time=None,
            exporter_network_device_id=None,
            id="string",
            site_id=None,
            start_time=None,
        )
    )
    return endpoint_result


@pytest.mark.applications
def test_retrieves_the_client_count_for_the_given_application_default_val(
    api, validator
):
    try:
        assert is_valid_retrieves_the_client_count_for_the_given_application(
            validator,
            retrieves_the_client_count_for_the_given_application_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_applications(json_schema_validate, obj):
    json_schema_validate("jsd_1b85e4ce533d5ff49ddd3b2f9657cfa5_v3_2_3_0").validate(obj)
    return True


def applications(api):
    endpoint_result = api.applications.applications(
        application_health="string",
        application_name="string",
        device_id="string",
        end_time=0,
        limit=0,
        mac_address="string",
        offset=0,
        site_id="string",
        start_time=0,
    )
    return endpoint_result


@pytest.mark.applications
def test_applications(api, validator):
    try:
        assert is_valid_applications(validator, applications(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def applications_default_val(api):
    endpoint_result = api.applications.applications(
        application_health=None,
        application_name=None,
        device_id=None,
        end_time=None,
        limit=None,
        mac_address=None,
        offset=None,
        site_id=None,
        start_time=None,
    )
    return endpoint_result


@pytest.mark.applications
def test_applications_default_val(api, validator):
    try:
        assert is_valid_applications(validator, applications_default_val(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
