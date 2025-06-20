# -*- coding: utf-8 -*-
"""Package exceptions.

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


import logging
from builtins import *

import requests

from .response_codes import RESPONSE_CODES

logger = logging.getLogger(__name__)


class catalystcentersdkException(Exception):
    """Base class for all catalystcentersdk package exceptions."""

    pass


class AccessTokenError(catalystcentersdkException):
    """Raised when an incorrect CatalystCenter Access Token has been provided."""

    pass


class VersionError(catalystcentersdkException):
    """Raised when an incorrect CatalystCenter version has been provided."""

    pass


class DownloadFailure(catalystcentersdkException):
    """Errors returned in response to requests sent to the CatalystCenter APIs
    with stream=True.

    Several data attributes are available for inspection.
    """

    def __init__(self, response, exception):
        assert isinstance(response, requests.Response)
        assert isinstance(exception, Exception)

        # Extended exception attributes
        self.response = response
        """The :class:`requests.Response` object returned from the API call."""

        self.request = self.response.request
        """The :class:`requests.PreparedRequest` of the API call."""

        self.status_code = self.response.status_code
        """The HTTP status code from the API response."""

        self.status = self.response.reason
        """The HTTP status from the API response."""

        self.original_error = exception
        """The original exception"""

        self.raw = self.response.raw
        """The raw value of the API response"""

        self.message = "Check raw property to retrieve raw response."

        super(DownloadFailure, self).__init__(
            "[{status_code}]{status} - {message} : {original_error}".format(
                status_code=self.status_code,
                status=" " + self.status if self.status else "",
                message=self.message,
                original_error=self.original_error,
            )
        )

    def __repr__(self):
        return "<{exception_name} [{status_code}]>".format(
            exception_name=self.__class__.__name__,
            status_code=self.status_code,
        )


class ApiError(catalystcentersdkException):
    """Errors returned in response to requests sent to the CatalystCenter APIs.

    Several data attributes are available for inspection.
    """

    def __init__(self, response):
        assert isinstance(response, requests.Response)

        # Extended exception attributes
        self.response = response
        """The :class:`requests.Response` object returned from the API call."""

        self.request = self.response.request
        """The :class:`requests.PreparedRequest` of the API call."""

        self.status_code = self.response.status_code
        """The HTTP status code from the API response."""

        self.status = self.response.reason
        """The HTTP status from the API response."""

        self.details = None
        """The parsed JSON details from the API response."""
        if "application/json" in self.response.headers.get("Content-Type", "").lower():
            try:
                self.details = self.response.json()
            except ValueError:
                logger.warning("Error parsing JSON response body")

        self.message = (
            self.details.get("message")
            or self.details.get("response", {}).get("message")
            or self.details.get("description")
            if self.details and isinstance(self.details, dict)
            else None
        )
        """The error message from the parsed API response."""

        self.description = RESPONSE_CODES.get(self.status_code)
        """A description of the HTTP Response Code from the API docs."""

        super(ApiError, self).__init__(
            "[{status_code}]{status} - {message}".format(
                status_code=self.status_code,
                status=" " + self.status if self.status else "",
                message=self.message or self.description or "Unknown Error",
            )
        )

    def __repr__(self):
        return "<{exception_name} [{status_code}]>".format(
            exception_name=self.__class__.__name__,
            status_code=self.status_code,
        )


class RateLimitError(ApiError):
    """Cisco CatalystCenter Rate-Limit exceeded Error.

    Raised when a rate-limit exceeded message is received and the request
    **will not** be retried.
    """

    def __init__(self, response):
        assert isinstance(response, requests.Response)

        # Extended exception attributes
        self.retry_after = max(1, int(response.headers.get("Retry-After", 15)))
        """The `Retry-After` time period (in seconds) provided by CatalystCenter.

        Defaults to 15 seconds if the response `Retry-After` header isn't
        present in the response headers, and defaults to a minimum wait time of
        1 second if CatalystCenter returns a `Retry-After` header of 0 seconds.
        """

        super(RateLimitError, self).__init__(response)


class RateLimitWarning(UserWarning):
    """Cisco CatalystCenter rate-limit exceeded warning.

    Raised when a rate-limit exceeded message is received and the request will
    be retried.
    """

    def __init__(self, response):
        assert isinstance(response, requests.Response)

        # Extended warning attributes
        self.retry_after = max(1, int(response.headers.get("Retry-After", 15)))
        """The `Retry-After` time period (in seconds) provided by CatalystCenter.

        Defaults to 15 seconds if the response `Retry-After` header isn't
        present in the response headers, and defaults to a minimum wait time of
        1 second if CatalystCenter returns a `Retry-After` header of 0 seconds.
        """

        super(RateLimitWarning, self).__init__()


class MalformedRequest(catalystcentersdkException):
    """Raised when a malformed request is received from CatalystCenter user."""

    pass
