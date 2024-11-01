
# -*- coding: utf-8 -*-
"""Test suite for the community-developed Python SDK for the CatalystCenter APIs.

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

import catalystcentersdk
import requests
from tests.environment import (
    CATALYST_CENTER_USERNAME, CATALYST_CENTER_PASSWORD,
    CATALYST_CENTER_ENCODED_AUTH, CATALYST_CENTER_VERSION,
)

from catalystcentersdk.api.authentication import Authentication


from catalystcentersdk.catalystcentersdk.api.v2_3_7_6_1.ai_endpoint_analytics import \
    AIEndpointAnalytics as AIEndpointAnalytics_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.application_policy import \
    ApplicationPolicy as ApplicationPolicy_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.applications import \
    Applications as Applications_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.cisco_trusted_certificates import \
    CiscoTrustedCertificates as CiscoTrustedCertificates_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.clients import \
    Clients as Clients_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.command_runner import \
    CommandRunner as CommandRunner_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.compliance import \
    Compliance as Compliance_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.configuration_archive import \
    ConfigurationArchive as ConfigurationArchive_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.configuration_templates import \
    ConfigurationTemplates as ConfigurationTemplates_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.device_onboarding_pnp import \
    DeviceOnboardingPnp as DeviceOnboardingPnp_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.device_replacement import \
    DeviceReplacement as DeviceReplacement_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.devices import \
    Devices as Devices_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.disaster_recovery import \
    DisasterRecovery as DisasterRecovery_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.discovery import \
    Discovery as Discovery_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.eox import \
    EoX as EoX_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.event_management import \
    EventManagement as EventManagement_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.fabric_wireless import \
    FabricWireless as FabricWireless_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.file import \
    File as File_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.health_and_performance import \
    HealthAndPerformance as HealthAndPerformance_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.itsm import \
    Itsm as Itsm_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.itsm_integration import \
    ItsmIntegration as ItsmIntegration_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.issues import \
    Issues as Issues_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.lan_automation import \
    LanAutomation as LanAutomation_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.licenses import \
    Licenses as Licenses_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.network_settings import \
    NetworkSettings as NetworkSettings_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.path_trace import \
    PathTrace as PathTrace_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.platform import \
    Platform as Platform_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.reports import \
    Reports as Reports_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.sda import \
    Sda as Sda_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.security_advisories import \
    SecurityAdvisories as SecurityAdvisories_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.sensors import \
    Sensors as Sensors_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.site_design import \
    SiteDesign as SiteDesign_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.sites import \
    Sites as Sites_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.software_image_management_swim import \
    SoftwareImageManagementSwim as SoftwareImageManagementSwim_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.system_settings import \
    SystemSettings as SystemSettings_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.tag import \
    Tag as Tag_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.task import \
    Task as Task_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.topology import \
    Topology as Topology_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.user_and_roles import \
    UserandRoles as UserandRoles_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.users import \
    Users as Users_v2_3_7_6_1
from catalystcentersdk.api.v2_3_7_6_1.wireless import \
    Wireless as Wireless_v2_3_7_6_1
from catalystcentersdk.api.custom_caller import CustomCaller

from tests.config import (
    DEFAULT_VERIFY,
    DEFAULT_SINGLE_REQUEST_TIMEOUT,
    DEFAULT_WAIT_ON_RATE_LIMIT
)
import pytest


@pytest.mark.catalystcentersdk
class TestDNACenterSDK:
    """Test the package-level code."""

    def test_package_contents(self):
        """Ensure the package contains the correct top-level objects."""
        # CatalystCenter API Wrapper
        assert hasattr(catalystcentersdk, "CatalystCenterAPI")

        # Exceptions
        assert hasattr(catalystcentersdk, "AccessTokenError")
        assert hasattr(catalystcentersdk, "ApiError")
        assert hasattr(catalystcentersdk, "catalystcentersdkException")
        assert hasattr(catalystcentersdk, "DownloadFailure")
        assert hasattr(catalystcentersdk, "MalformedRequest")
        assert hasattr(catalystcentersdk, "RateLimitError")
        assert hasattr(catalystcentersdk, "RateLimitWarning")
        assert hasattr(catalystcentersdk, "VersionError")

        # Data Models
        assert hasattr(catalystcentersdk, "mydict_data_factory")

    @pytest.mark.catalystcentersdk
    def test_default_base_url(self, api, base_url):
        assert api.base_url == base_url

    @pytest.mark.catalystcentersdk
    def test_custom_base_url(self):
        custom_url = "https://custom.domain.com/v1/"
        with pytest.raises((catalystcentersdk.exceptions.ApiError, requests.exceptions.RequestException)):
            catalystcentersdk.CatalystCenterAPI(username=CATALYST_CENTER_USERNAME,
                                      password=CATALYST_CENTER_PASSWORD,
                                      encoded_auth=CATALYST_CENTER_ENCODED_AUTH,
                                      base_url=custom_url,
                                      verify=DEFAULT_VERIFY,
                                      version=CATALYST_CENTER_VERSION)

    @pytest.mark.catalystcentersdk
    def test_default_single_request_timeout(self, api):
        assert api.single_request_timeout == \
            DEFAULT_SINGLE_REQUEST_TIMEOUT

    @pytest.mark.catalystcentersdk
    def test_custom_single_request_timeout(self, base_url):
        custom_timeout = 10
        connection_object = catalystcentersdk.CatalystCenterAPI(username=CATALYST_CENTER_USERNAME,
                                                      password=CATALYST_CENTER_PASSWORD,
                                                      encoded_auth=CATALYST_CENTER_ENCODED_AUTH,
                                                      base_url=base_url,
                                                      single_request_timeout=custom_timeout,
                                                      verify=DEFAULT_VERIFY,
                                                      version=CATALYST_CENTER_VERSION)
        assert connection_object.single_request_timeout == custom_timeout

    @pytest.mark.catalystcentersdk
    def test_default_wait_on_rate_limit(self, api):
        assert api.wait_on_rate_limit == \
            DEFAULT_WAIT_ON_RATE_LIMIT

    @pytest.mark.catalystcentersdk
    def test_non_default_wait_on_rate_limit(self, base_url):
        connection_object = catalystcentersdk.CatalystCenterAPI(username=CATALYST_CENTER_USERNAME,
                                                      password=CATALYST_CENTER_PASSWORD,
                                                      encoded_auth=CATALYST_CENTER_ENCODED_AUTH,
                                                      base_url=base_url,
                                                      wait_on_rate_limit=not DEFAULT_WAIT_ON_RATE_LIMIT,
                                                      verify=DEFAULT_VERIFY,
                                                      version=CATALYST_CENTER_VERSION)
        assert connection_object.wait_on_rate_limit != \
            DEFAULT_WAIT_ON_RATE_LIMIT

    @pytest.mark.catalystcentersdk
    def test_api_object_creation(self, api):
        assert isinstance(api.authentication, Authentication)
        assert isinstance(api.custom_caller, CustomCaller)

        
        if api.version == '2.3.7.6':
            assert isinstance(api.ai_endpoint_analytics, AIEndpointAnalytics_v2_3_7_6_1)
            assert isinstance(api.application_policy, ApplicationPolicy_v2_3_7_6_1)
            assert isinstance(api.applications, Applications_v2_3_7_6_1)
            assert isinstance(api.cisco_trusted_certificates, CiscoTrustedCertificates_v2_3_7_6_1)
            assert isinstance(api.clients, Clients_v2_3_7_6_1)
            assert isinstance(api.command_runner, CommandRunner_v2_3_7_6_1)
            assert isinstance(api.compliance, Compliance_v2_3_7_6_1)
            assert isinstance(api.configuration_archive, ConfigurationArchive_v2_3_7_6_1)
            assert isinstance(api.configuration_templates, ConfigurationTemplates_v2_3_7_6_1)
            assert isinstance(api.device_onboarding_pnp, DeviceOnboardingPnp_v2_3_7_6_1)
            assert isinstance(api.device_replacement, DeviceReplacement_v2_3_7_6_1)
            assert isinstance(api.devices, Devices_v2_3_7_6_1)
            assert isinstance(api.disaster_recovery, DisasterRecovery_v2_3_7_6_1)
            assert isinstance(api.discovery, Discovery_v2_3_7_6_1)
            assert isinstance(api.eox, EoX_v2_3_7_6_1)
            assert isinstance(api.event_management, EventManagement_v2_3_7_6_1)
            assert isinstance(api.fabric_wireless, FabricWireless_v2_3_7_6_1)
            assert isinstance(api.file, File_v2_3_7_6_1)
            assert isinstance(api.health_and_performance, HealthAndPerformance_v2_3_7_6_1)
            assert isinstance(api.itsm, Itsm_v2_3_7_6_1)
            assert isinstance(api.itsm_integration, ItsmIntegration_v2_3_7_6_1)
            assert isinstance(api.issues, Issues_v2_3_7_6_1)
            assert isinstance(api.lan_automation, LanAutomation_v2_3_7_6_1)
            assert isinstance(api.licenses, Licenses_v2_3_7_6_1)
            assert isinstance(api.network_settings, NetworkSettings_v2_3_7_6_1)
            assert isinstance(api.path_trace, PathTrace_v2_3_7_6_1)
            assert isinstance(api.platform, Platform_v2_3_7_6_1)
            assert isinstance(api.reports, Reports_v2_3_7_6_1)
            assert isinstance(api.sda, Sda_v2_3_7_6_1)
            assert isinstance(api.security_advisories, SecurityAdvisories_v2_3_7_6_1)
            assert isinstance(api.sensors, Sensors_v2_3_7_6_1)
            assert isinstance(api.site_design, SiteDesign_v2_3_7_6_1)
            assert isinstance(api.sites, Sites_v2_3_7_6_1)
            assert isinstance(api.software_image_management_swim, SoftwareImageManagementSwim_v2_3_7_6_1)
            assert isinstance(api.system_settings, SystemSettings_v2_3_7_6_1)
            assert isinstance(api.tag, Tag_v2_3_7_6_1)
            assert isinstance(api.task, Task_v2_3_7_6_1)
            assert isinstance(api.topology, Topology_v2_3_7_6_1)
            assert isinstance(api.user_and_roles, UserandRoles_v2_3_7_6_1)
            assert isinstance(api.users, Users_v2_3_7_6_1)
            assert isinstance(api.wireless, Wireless_v2_3_7_6_1)
