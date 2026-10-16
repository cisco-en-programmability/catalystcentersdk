import json

import requests

from catalystcentersdk.exceptions import ApiError


def _response(body):
    response = requests.Response()
    response.status_code = 400
    response.reason = "Bad Request"
    response.headers["Content-Type"] = "application/json"
    response._content = json.dumps(body).encode("utf-8")
    return response


def test_api_error_handles_list_response_and_preserves_error_message():
    error = ApiError(
        _response(
            {
                "response": [],
                "errorMessage": "Field siteId is not valid.",
                "totalCount": 0,
                "version": "1.0",
            }
        )
    )

    assert error.status_code == 400
    assert error.details["response"] == []
    assert error.message == "Field siteId is not valid."
    assert str(error) == "[400] Bad Request - Field siteId is not valid."


def test_api_error_reads_nested_response_message():
    error = ApiError(_response({"response": {"message": "Nested failure."}}))

    assert error.message == "Nested failure."
