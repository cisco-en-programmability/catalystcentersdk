"""CatalystCenterAPI path_trace API fixtures and tests.

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


def is_valid_retrieves_previous_path_trace_result(json_schema_validate, obj):
    json_schema_validate("jsd_83d7cc6ea2f45cd9b213b244de5c59bf_v3_2_3_0").validate(obj)
    return True


def retrieves_previous_path_trace_result(api):
    endpoint_result = api.path_trace.retrieves_previous_path_trace_result(
        id="string", view="value1,value2"
    )
    return endpoint_result


@pytest.mark.path_trace
def test_retrieves_previous_path_trace_result(api, validator):
    try:
        assert is_valid_retrieves_previous_path_trace_result(
            validator, retrieves_previous_path_trace_result(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_previous_path_trace_result_default_val(api):
    endpoint_result = api.path_trace.retrieves_previous_path_trace_result(
        id="string", view=None
    )
    return endpoint_result


@pytest.mark.path_trace
def test_retrieves_previous_path_trace_result_default_val(api, validator):
    try:
        assert is_valid_retrieves_previous_path_trace_result(
            validator, retrieves_previous_path_trace_result_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_count_of_path_traces_matching_filter_criteria(
    json_schema_validate, obj
):
    json_schema_validate("jsd_544c1ab1b11f541090f55245ecd327fb_v3_2_3_0").validate(obj)
    return True


def retrieves_the_count_of_path_traces_matching_filter_criteria(api):
    endpoint_result = (
        api.path_trace.retrieves_the_count_of_path_traces_matching_filter_criteria(
            destination_ip_address="string",
            destination_mac_address="string",
            destination_port=0,
            greater_than_create_time=0,
            last_update_time=0,
            less_than_create_time=0,
            periodic_refresh=True,
            protocol="string",
            source_ip_address="string",
            source_mac_address="string",
            source_port=0,
            status="string",
        )
    )
    return endpoint_result


@pytest.mark.path_trace
def test_retrieves_the_count_of_path_traces_matching_filter_criteria(api, validator):
    try:
        assert is_valid_retrieves_the_count_of_path_traces_matching_filter_criteria(
            validator, retrieves_the_count_of_path_traces_matching_filter_criteria(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_count_of_path_traces_matching_filter_criteria_default_val(api):
    endpoint_result = (
        api.path_trace.retrieves_the_count_of_path_traces_matching_filter_criteria(
            destination_ip_address=None,
            destination_mac_address=None,
            destination_port=None,
            greater_than_create_time=None,
            last_update_time=None,
            less_than_create_time=None,
            periodic_refresh=None,
            protocol=None,
            source_ip_address=None,
            source_mac_address=None,
            source_port=None,
            status=None,
        )
    )
    return endpoint_result


@pytest.mark.path_trace
def test_retrieves_the_count_of_path_traces_matching_filter_criteria_default_val(
    api, validator
):
    try:
        assert is_valid_retrieves_the_count_of_path_traces_matching_filter_criteria(
            validator,
            retrieves_the_count_of_path_traces_matching_filter_criteria_default_val(
                api
            ),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deletes_path_trace_by_id(json_schema_validate, obj):
    json_schema_validate("jsd_626a202e493b5d7899cc77bbdab1c409_v3_2_3_0").validate(obj)
    return True


def deletes_path_trace_by_id(api):
    endpoint_result = api.path_trace.deletes_path_trace_by_id(id="string")
    return endpoint_result


@pytest.mark.path_trace
def test_deletes_path_trace_by_id(api, validator):
    try:
        assert is_valid_deletes_path_trace_by_id(
            validator, deletes_path_trace_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deletes_path_trace_by_id_default_val(api):
    endpoint_result = api.path_trace.deletes_path_trace_by_id(id="string")
    return endpoint_result


@pytest.mark.path_trace
def test_deletes_path_trace_by_id_default_val(api, validator):
    try:
        assert is_valid_deletes_path_trace_by_id(
            validator, deletes_path_trace_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_summary_of_a_specific_path_trace(json_schema_validate, obj):
    json_schema_validate("jsd_26a249ce703a589dae0b88ce5fb9ac9a_v3_2_3_0").validate(obj)
    return True


def retrieves_the_summary_of_a_specific_path_trace(api):
    endpoint_result = api.path_trace.retrieves_the_summary_of_a_specific_path_trace(
        id="string"
    )
    return endpoint_result


@pytest.mark.path_trace
def test_retrieves_the_summary_of_a_specific_path_trace(api, validator):
    try:
        assert is_valid_retrieves_the_summary_of_a_specific_path_trace(
            validator, retrieves_the_summary_of_a_specific_path_trace(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_summary_of_a_specific_path_trace_default_val(api):
    endpoint_result = api.path_trace.retrieves_the_summary_of_a_specific_path_trace(
        id="string"
    )
    return endpoint_result


@pytest.mark.path_trace
def test_retrieves_the_summary_of_a_specific_path_trace_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_summary_of_a_specific_path_trace(
            validator, retrieves_the_summary_of_a_specific_path_trace_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_initiate_a_new_pathtrace(json_schema_validate, obj):
    json_schema_validate("jsd_a54fce1a0c305bdabfe91a8a6161e539_v3_2_3_0").validate(obj)
    return True


def initiate_a_new_pathtrace(api):
    endpoint_result = api.path_trace.initiate_a_new_pathtrace(
        active_validation=True,
        controlPath=True,
        destIP="string",
        destPort="string",
        inclusions=["string"],
        payload=None,
        periodicRefresh=True,
        protocol="string",
        sourceIP="string",
        sourcePort="string",
    )
    return endpoint_result


@pytest.mark.path_trace
def test_initiate_a_new_pathtrace(api, validator):
    try:
        assert is_valid_initiate_a_new_pathtrace(
            validator, initiate_a_new_pathtrace(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def initiate_a_new_pathtrace_default_val(api):
    endpoint_result = api.path_trace.initiate_a_new_pathtrace(
        active_validation=True,
        controlPath=None,
        destIP=None,
        destPort=None,
        inclusions=None,
        payload=None,
        periodicRefresh=None,
        protocol=None,
        sourceIP=None,
        sourcePort=None,
    )
    return endpoint_result


@pytest.mark.path_trace
def test_initiate_a_new_pathtrace_default_val(api, validator):
    try:
        assert is_valid_initiate_a_new_pathtrace(
            validator, initiate_a_new_pathtrace_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_all_previous_pathtraces_summary(json_schema_validate, obj):
    json_schema_validate("jsd_a75e4b27171c5c6782e84f902da9e5be_v3_2_3_0").validate(obj)
    return True


def retrieves_all_previous_pathtraces_summary(api):
    endpoint_result = api.path_trace.retrieves_all_previous_pathtraces_summary(
        dest_ip="string",
        dest_port=0,
        gt_create_time=0,
        last_update_time=0,
        limit=0,
        lt_create_time=0,
        offset=0,
        order="string",
        periodic_refresh=True,
        protocol="string",
        sort_by="string",
        source_ip="string",
        source_port=0,
        status="string",
        task_id="string",
    )
    return endpoint_result


@pytest.mark.path_trace
def test_retrieves_all_previous_pathtraces_summary(api, validator):
    try:
        assert is_valid_retrieves_all_previous_pathtraces_summary(
            validator, retrieves_all_previous_pathtraces_summary(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_all_previous_pathtraces_summary_default_val(api):
    endpoint_result = api.path_trace.retrieves_all_previous_pathtraces_summary(
        dest_ip=None,
        dest_port=None,
        gt_create_time=None,
        last_update_time=None,
        limit=None,
        lt_create_time=None,
        offset=None,
        order=None,
        periodic_refresh=None,
        protocol=None,
        sort_by=None,
        source_ip=None,
        source_port=None,
        status=None,
        task_id=None,
    )
    return endpoint_result


@pytest.mark.path_trace
def test_retrieves_all_previous_pathtraces_summary_default_val(api, validator):
    try:
        assert is_valid_retrieves_all_previous_pathtraces_summary(
            validator, retrieves_all_previous_pathtraces_summary_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_the_summary_of_all_previous_path_traces(
    json_schema_validate, obj
):
    json_schema_validate("jsd_9c53cecf7e5b54cb8d23310ecd049e15_v3_2_3_0").validate(obj)
    return True


def retrieves_the_summary_of_all_previous_path_traces(api):
    endpoint_result = api.path_trace.retrieves_the_summary_of_all_previous_path_traces(
        destination_ip_address="string",
        destination_mac_address="string",
        destination_port=0,
        greater_than_create_time=0,
        last_update_time=0,
        less_than_create_time=0,
        limit=0,
        offset=0,
        order="string",
        periodic_refresh=True,
        protocol="string",
        sort_by="string",
        source_ip_address="string",
        source_mac_address="string",
        source_port=0,
        status="string",
    )
    return endpoint_result


@pytest.mark.path_trace
def test_retrieves_the_summary_of_all_previous_path_traces(api, validator):
    try:
        assert is_valid_retrieves_the_summary_of_all_previous_path_traces(
            validator, retrieves_the_summary_of_all_previous_path_traces(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_the_summary_of_all_previous_path_traces_default_val(api):
    endpoint_result = api.path_trace.retrieves_the_summary_of_all_previous_path_traces(
        destination_ip_address=None,
        destination_mac_address=None,
        destination_port=None,
        greater_than_create_time=None,
        last_update_time=None,
        less_than_create_time=None,
        limit=None,
        offset=None,
        order=None,
        periodic_refresh=None,
        protocol=None,
        sort_by=None,
        source_ip_address=None,
        source_mac_address=None,
        source_port=None,
        status=None,
    )
    return endpoint_result


@pytest.mark.path_trace
def test_retrieves_the_summary_of_all_previous_path_traces_default_val(api, validator):
    try:
        assert is_valid_retrieves_the_summary_of_all_previous_path_traces(
            validator,
            retrieves_the_summary_of_all_previous_path_traces_default_val(api),
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_initiate_a_new_path_trace(json_schema_validate, obj):
    json_schema_validate("jsd_aface7a4f75552cc9e167e2126979261_v3_2_3_0").validate(obj)
    return True


def initiate_a_new_path_trace(api):
    endpoint_result = api.path_trace.initiate_a_new_path_trace(
        active_validation=True,
        controlPath=True,
        destinationIpAddress="string",
        destinationMacAddress="string",
        destinationPort="string",
        inclusions=["string"],
        payload=None,
        periodicRefresh=True,
        protocol="string",
        sourceIpAddress="string",
        sourceMacAddress="string",
        sourcePort="string",
    )
    return endpoint_result


@pytest.mark.path_trace
def test_initiate_a_new_path_trace(api, validator):
    try:
        assert is_valid_initiate_a_new_path_trace(
            validator, initiate_a_new_path_trace(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def initiate_a_new_path_trace_default_val(api):
    endpoint_result = api.path_trace.initiate_a_new_path_trace(
        active_validation=True,
        controlPath=None,
        destinationIpAddress=None,
        destinationMacAddress=None,
        destinationPort=None,
        inclusions=None,
        payload=None,
        periodicRefresh=None,
        protocol=None,
        sourceIpAddress=None,
        sourceMacAddress=None,
        sourcePort=None,
    )
    return endpoint_result


@pytest.mark.path_trace
def test_initiate_a_new_path_trace_default_val(api, validator):
    try:
        assert is_valid_initiate_a_new_path_trace(
            validator, initiate_a_new_path_trace_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_previous_pathtrace(json_schema_validate, obj):
    json_schema_validate("jsd_ed5cbafc332a5efa97547736ba8b6044_v3_2_3_0").validate(obj)
    return True


def retrieves_previous_pathtrace(api):
    endpoint_result = api.path_trace.retrieves_previous_pathtrace(
        flow_analysis_id="string"
    )
    return endpoint_result


@pytest.mark.path_trace
def test_retrieves_previous_pathtrace(api, validator):
    try:
        assert is_valid_retrieves_previous_pathtrace(
            validator, retrieves_previous_pathtrace(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def retrieves_previous_pathtrace_default_val(api):
    endpoint_result = api.path_trace.retrieves_previous_pathtrace(
        flow_analysis_id="string"
    )
    return endpoint_result


@pytest.mark.path_trace
def test_retrieves_previous_pathtrace_default_val(api, validator):
    try:
        assert is_valid_retrieves_previous_pathtrace(
            validator, retrieves_previous_pathtrace_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deletes_pathtrace_by_id(json_schema_validate, obj):
    json_schema_validate("jsd_8a7ae984f943507ba621abe155e6e744_v3_2_3_0").validate(obj)
    return True


def deletes_pathtrace_by_id(api):
    endpoint_result = api.path_trace.deletes_pathtrace_by_id(flow_analysis_id="string")
    return endpoint_result


@pytest.mark.path_trace
def test_deletes_pathtrace_by_id(api, validator):
    try:
        assert is_valid_deletes_pathtrace_by_id(validator, deletes_pathtrace_by_id(api))
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deletes_pathtrace_by_id_default_val(api):
    endpoint_result = api.path_trace.deletes_pathtrace_by_id(flow_analysis_id="string")
    return endpoint_result


@pytest.mark.path_trace
def test_deletes_pathtrace_by_id_default_val(api, validator):
    try:
        assert is_valid_deletes_pathtrace_by_id(
            validator, deletes_pathtrace_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
