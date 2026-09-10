"""CatalystCenterAPI streamed-download tests.

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

import importlib

import pytest

# Endpoints that answer with a ZIP, a packet capture or raw text. Their bodies
# must reach RestSession.download() instead of extract_and_parse_json(), which is
# what `stream=True` selects. See issue #63.
DOWNLOADS = [
    (
        "configuration_archive",
        "ConfigurationArchive",
        "download_masked_device_configuration",
        {"id": "abc"},
        "/dna/intent/api/v1/networkDeviceConfigFiles/abc/downloadMasked",
    ),
    (
        "configuration_archive",
        "ConfigurationArchive",
        "download_unmaskedraw_device_configuration_as_zip",
        {"id": "abc", "active_validation": False},
        "/dna/intent/api/v1/networkDeviceConfigFiles/abc/downloadUnmasked",
    ),
    (
        "configuration_archive",
        "ConfigurationArchive",
        "download_unmaskedraw_device_configuration_as_z_ip",
        {"id": "abc", "active_validation": False},
        "/dna/intent/api/v1/networkDeviceConfigFiles/abc/downloadUnmasked",
    ),
    (
        "reports",
        "Reports",
        "download_flexible_report",
        {"report_id": "rep", "execution_id": "exec"},
        "/dna/data/api/v1/flexible-report/report/content/rep/exec",
    ),
    (
        "reports",
        "Reports",
        "download_report_content",
        {"report_id": "rep", "execution_id": "exec"},
        "/dna/intent/api/v1/data/reports/rep/executions/exec",
    ),
    (
        "sensors",
        "Sensors",
        "downloads_a_specific_icap_packet_capture_file",
        {"id": "abc"},
        "/dna/data/api/v1/icap/captureFiles/abc/download",
    ),
    (
        "file",
        "File",
        "download_a_file_by_fileid",
        {"file_id": "abc"},
        "/dna/intent/api/v1/file/abc",
    ),
]


class RecordingSession:
    """Captures the kwargs an API method hands to the session."""

    headers = {}

    def __init__(self):
        self.calls = []

    def _record(self, url, **kwargs):
        self.calls.append((url, kwargs))
        return object()

    get = _record
    post = _record


def build(module, cls_name):
    cls = getattr(
        importlib.import_module(f"catalystcentersdk.api.v3_2_3_0.{module}"), cls_name
    )
    # Built without __init__ so no live RestSession is needed.
    api = cls.__new__(cls)
    api._session = RecordingSession()
    api._object_factory = lambda key, data: data
    api._request_validator = None
    return api


@pytest.mark.parametrize("module,cls,method,kwargs,url", DOWNLOADS)
def test_download_streams_the_response(module, cls, method, kwargs, url):
    api = build(module, cls)
    getattr(api, method)(
        dirpath="/tmp/downloads",
        save_file=True,
        filename="payload.bin",
        **kwargs,
    )
    called_url, sent = api._session.calls[0]
    assert called_url == url
    assert sent["stream"] is True
    assert sent["dirpath"] == "/tmp/downloads"
    assert sent["save_file"] is True
    assert sent["filename"] == "payload.bin"


def test_software_image_download_is_not_a_streamed_download():
    """`POST /images/{id}/download` starts a server-side pull and returns a task,
    so it must keep parsing its JSON body."""
    api = build("software_image_management_swim", "SoftwareImageManagementSwim")
    api.download_the_software_image(id="abc")
    _, sent = api._session.calls[0]
    assert "stream" not in sent
