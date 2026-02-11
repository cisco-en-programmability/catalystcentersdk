# -*- coding: utf-8 -*-
"""Cisco Catalyst Center API wrappers.

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


from catalystcentersdk.config import (
    DEFAULT_DEBUG,
    DEFAULT_VERSION,
    DEFAULT_BASE_URL,
    DEFAULT_SINGLE_REQUEST_TIMEOUT,
    DEFAULT_WAIT_ON_RATE_LIMIT,
    DEFAULT_VERIFY,
    DEFAULT_VERIFY_USER_AGENT,
)
import catalystcentersdk.environment as catalystcenter_environment
from catalystcentersdk.exceptions import AccessTokenError, VersionError
from catalystcentersdk.models.mydict import mydict_data_factory
from catalystcentersdk.models.schema_validator import SchemaValidator
from catalystcentersdk.restsession import RestSession
from catalystcentersdk.utils import check_type

from .authentication import Authentication
from .v2_3_7_6_1.ai_endpoint_analytics import (
    AIEndpointAnalytics as AIEndpointAnalytics_v2_3_7_6_1,
)
from .v2_3_7_6_1.authentication_management import (
    AuthenticationManagement as AuthenticationManagement_v2_3_7_6_1,
)
from .v2_3_7_6_1.application_policy import (
    ApplicationPolicy as ApplicationPolicy_v2_3_7_6_1,
)
from .v2_3_7_6_1.applications import Applications as Applications_v2_3_7_6_1
from .v2_3_7_6_1.cisco_trusted_certificates import (
    CiscoTrustedCertificates as CiscoTrustedCertificates_v2_3_7_6_1,
)
from .v2_3_7_6_1.clients import Clients as Clients_v2_3_7_6_1
from .v2_3_7_6_1.command_runner import (
    CommandRunner as CommandRunner_v2_3_7_6_1,
)
from .v2_3_7_6_1.compliance import Compliance as Compliance_v2_3_7_6_1
from .v2_3_7_6_1.configuration_archive import (
    ConfigurationArchive as ConfigurationArchive_v2_3_7_6_1,
)
from .v2_3_7_6_1.configuration_templates import (
    ConfigurationTemplates as ConfigurationTemplates_v2_3_7_6_1,
)
from .v2_3_7_6_1.device_onboarding_pnp import (
    DeviceOnboardingPnp as DeviceOnboardingPnp_v2_3_7_6_1,
)
from .v2_3_7_6_1.device_replacement import (
    DeviceReplacement as DeviceReplacement_v2_3_7_6_1,
)
from .v2_3_7_6_1.devices import Devices as Devices_v2_3_7_6_1
from .v2_3_7_6_1.disaster_recovery import (
    DisasterRecovery as DisasterRecovery_v2_3_7_6_1,
)
from .v2_3_7_6_1.discovery import Discovery as Discovery_v2_3_7_6_1
from .v2_3_7_6_1.eox import EoX as EoX_v2_3_7_6_1
from .v2_3_7_6_1.event_management import (
    EventManagement as EventManagement_v2_3_7_6_1,
)
from .v2_3_7_6_1.fabric_wireless import (
    FabricWireless as FabricWireless_v2_3_7_6_1,
)
from .v2_3_7_6_1.file import File as File_v2_3_7_6_1
from .v2_3_7_6_1.health_and_performance import (
    HealthAndPerformance as HealthAndPerformance_v2_3_7_6_1,
)
from .v2_3_7_6_1.itsm import Itsm as Itsm_v2_3_7_6_1
from .v2_3_7_6_1.itsm_integration import (
    ItsmIntegration as ItsmIntegration_v2_3_7_6_1,
)
from .v2_3_7_6_1.issues import Issues as Issues_v2_3_7_6_1
from .v2_3_7_6_1.lan_automation import (
    LanAutomation as LanAutomation_v2_3_7_6_1,
)
from .v2_3_7_6_1.licenses import Licenses as Licenses_v2_3_7_6_1
from .v2_3_7_6_1.network_settings import (
    NetworkSettings as NetworkSettings_v2_3_7_6_1,
)
from .v2_3_7_6_1.path_trace import PathTrace as PathTrace_v2_3_7_6_1
from .v2_3_7_6_1.platform import Platform as Platform_v2_3_7_6_1
from .v2_3_7_6_1.reports import Reports as Reports_v2_3_7_6_1
from .v2_3_7_6_1.sda import Sda as Sda_v2_3_7_6_1
from .v2_3_7_6_1.security_advisories import (
    SecurityAdvisories as SecurityAdvisories_v2_3_7_6_1,
)
from .v2_3_7_6_1.sensors import Sensors as Sensors_v2_3_7_6_1
from .v2_3_7_6_1.site_design import SiteDesign as SiteDesign_v2_3_7_6_1
from .v2_3_7_6_1.sites import Sites as Sites_v2_3_7_6_1
from .v2_3_7_6_1.software_image_management_swim import (
    SoftwareImageManagementSwim as SoftwareImageManagementSwim_v2_3_7_6_1,
)
from .v2_3_7_6_1.system_settings import (
    SystemSettings as SystemSettings_v2_3_7_6_1,
)
from .v2_3_7_6_1.tag import Tag as Tag_v2_3_7_6_1
from .v2_3_7_6_1.task import Task as Task_v2_3_7_6_1
from .v2_3_7_6_1.topology import Topology as Topology_v2_3_7_6_1
from .v2_3_7_6_1.user_and_roles import UserandRoles as UserandRoles_v2_3_7_6_1
from .v2_3_7_6_1.users import Users as Users_v2_3_7_6_1
from .v2_3_7_6_1.wireless import Wireless as Wireless_v2_3_7_6_1

from .v2_3_7_9.ai_endpoint_analytics import (
    AIEndpointAnalytics as AIEndpointAnalytics_v2_3_7_9,
)
from .v2_3_7_9.application_policy import (
    ApplicationPolicy as ApplicationPolicy_v2_3_7_9,
)
from .v2_3_7_9.applications import Applications as Applications_v2_3_7_9
from .v2_3_7_9.cisco_i_m_c import CiscoIMC as CiscoIMC_v2_3_7_9
from .v2_3_7_9.authentication_management import (
    AuthenticationManagement as AuthenticationManagement_v2_3_7_9,
)
from .v2_3_7_9.cisco_trusted_certificates import (
    CiscoTrustedCertificates as CiscoTrustedCertificates_v2_3_7_9,
)
from .v2_3_7_9.clients import Clients as Clients_v2_3_7_9
from .v2_3_7_9.command_runner import CommandRunner as CommandRunner_v2_3_7_9
from .v2_3_7_9.compliance import Compliance as Compliance_v2_3_7_9
from .v2_3_7_9.configuration_archive import (
    ConfigurationArchive as ConfigurationArchive_v2_3_7_9,
)
from .v2_3_7_9.configuration_templates import (
    ConfigurationTemplates as ConfigurationTemplates_v2_3_7_9,
)
from .v2_3_7_9.device_onboarding_pnp import (
    DeviceOnboardingPnp as DeviceOnboardingPnp_v2_3_7_9,
)
from .v2_3_7_9.device_replacement import (
    DeviceReplacement as DeviceReplacement_v2_3_7_9,
)
from .v2_3_7_9.devices import Devices as Devices_v2_3_7_9
from .v2_3_7_9.disaster_recovery import (
    DisasterRecovery as DisasterRecovery_v2_3_7_9,
)
from .v2_3_7_9.discovery import Discovery as Discovery_v2_3_7_9
from .v2_3_7_9.eox import Eox as Eox_v2_3_7_9
from .v2_3_7_9.event_management import (
    EventManagement as EventManagement_v2_3_7_9,
)
from .v2_3_7_9.fabric_wireless import FabricWireless as FabricWireless_v2_3_7_9
from .v2_3_7_9.file import File as File_v2_3_7_9
from .v2_3_7_9.health_and_performance import (
    HealthAndPerformance as HealthAndPerformance_v2_3_7_9,
)
from .v2_3_7_9.itsm import Itsm as Itsm_v2_3_7_9
from .v2_3_7_9.itsm_integration import (
    ItsmIntegration as ItsmIntegration_v2_3_7_9,
)
from .v2_3_7_9.issues import Issues as Issues_v2_3_7_9
from .v2_3_7_9.lan_automation import LanAutomation as LanAutomation_v2_3_7_9
from .v2_3_7_9.licenses import Licenses as Licenses_v2_3_7_9
from .v2_3_7_9.network_settings import (
    NetworkSettings as NetworkSettings_v2_3_7_9,
)
from .v2_3_7_9.path_trace import PathTrace as PathTrace_v2_3_7_9
from .v2_3_7_9.platform import Platform as Platform_v2_3_7_9
from .v2_3_7_9.reports import Reports as Reports_v2_3_7_9
from .v2_3_7_9.sda import Sda as Sda_v2_3_7_9
from .v2_3_7_9.security_advisories import (
    SecurityAdvisories as SecurityAdvisories_v2_3_7_9,
)
from .v2_3_7_9.sensors import Sensors as Sensors_v2_3_7_9
from .v2_3_7_9.site_design import SiteDesign as SiteDesign_v2_3_7_9
from .v2_3_7_9.sites import Sites as Sites_v2_3_7_9
from .v2_3_7_9.software_image_management_swim import (
    SoftwareImageManagementSwim as SoftwareImageManagementSwim_v2_3_7_9,
)
from .v2_3_7_9.system_settings import SystemSettings as SystemSettings_v2_3_7_9
from .v2_3_7_9.tag import Tag as Tag_v2_3_7_9
from .v2_3_7_9.task import Task as Task_v2_3_7_9
from .v2_3_7_9.topology import Topology as Topology_v2_3_7_9
from .v2_3_7_9.user_and_roles import UserandRoles as UserandRoles_v2_3_7_9
from .v2_3_7_9.users import Users as Users_v2_3_7_9
from .v2_3_7_9.wireless import Wireless as Wireless_v2_3_7_9

#  v3.1.3.0 APIs
from .v3_1_3_0.ai_endpoint_analytics import (
    AIEndpointAnalytics as AIEndpointAnalytics_v3_1_3_0,
)
from .v3_1_3_0.application_policy import (
    ApplicationPolicy as ApplicationPolicy_v3_1_3_0,
)
from .v3_1_3_0.applications import Applications as Applications_v3_1_3_0
from .v3_1_3_0.authentication_management import (
    AuthenticationManagement as AuthenticationManagement_v3_1_3_0,
)
from .v3_1_3_0.backup import Backup as Backup_v3_1_3_0
from .v3_1_3_0.cisco_i_m_c import CiscoIMC as CiscoIMC_v3_1_3_0
from .v3_1_3_0.cisco_trusted_certificates import (
    CiscoTrustedCertificates as CiscoTrustedCertificates_v3_1_3_0,
)
from .v3_1_3_0.clients import Clients as Clients_v3_1_3_0
from .v3_1_3_0.command_runner import CommandRunner as CommandRunner_v3_1_3_0
from .v3_1_3_0.compliance import Compliance as Compliance_v3_1_3_0
from .v3_1_3_0.configuration_archive import (
    ConfigurationArchive as ConfigurationArchive_v3_1_3_0,
)
from .v3_1_3_0.configuration_templates import (
    ConfigurationTemplates as ConfigurationTemplates_v3_1_3_0,
)
from .v3_1_3_0.device_onboarding_pnp import (
    DeviceOnboardingPnp as DeviceOnboardingPnp_v3_1_3_0,
)
from .v3_1_3_0.device_replacement import (
    DeviceReplacement as DeviceReplacement_v3_1_3_0,
)
from .v3_1_3_0.devices import Devices as Devices_v3_1_3_0
from .v3_1_3_0.disaster_recovery import (
    DisasterRecovery as DisasterRecovery_v3_1_3_0,
)
from .v3_1_3_0.discovery import Discovery as Discovery_v3_1_3_0
from .v3_1_3_0.eox import Eox as Eox_v3_1_3_0
from .v3_1_3_0.event_management import (
    EventManagement as EventManagement_v3_1_3_0,
)
from .v3_1_3_0.fabric_wireless import FabricWireless as FabricWireless_v3_1_3_0
from .v3_1_3_0.file import File as File_v3_1_3_0
from .v3_1_3_0.health_and_performance import (
    HealthAndPerformance as HealthAndPerformance_v3_1_3_0,
)
from .v3_1_3_0.itsm import Itsm as Itsm_v3_1_3_0
from .v3_1_3_0.itsm_integration import (
    ItsmIntegration as ItsmIntegration_v3_1_3_0,
)
from .v3_1_3_0.industrial_configuration import (
    IndustrialConfiguration as IndustrialConfiguration_v3_1_3_0,
)
from .v3_1_3_0.issues import Issues as Issues_v3_1_3_0
from .v3_1_3_0.know_your_network import (
    KnowYourNetwork as KnowYourNetwork_v3_1_3_0,
)
from .v3_1_3_0.lan_automation import LanAutomation as LanAutomation_v3_1_3_0
from .v3_1_3_0.licenses import Licenses as Licenses_v3_1_3_0
from .v3_1_3_0.network_settings import (
    NetworkSettings as NetworkSettings_v3_1_3_0,
)
from .v3_1_3_0.path_trace import PathTrace as PathTrace_v3_1_3_0
from .v3_1_3_0.platform import Platform as Platform_v3_1_3_0
from .v3_1_3_0.reports import Reports as Reports_v3_1_3_0
from .v3_1_3_0.restore import Restore as Restore_v3_1_3_0
from .v3_1_3_0.sda import Sda as Sda_v3_1_3_0
from .v3_1_3_0.security_advisories import (
    SecurityAdvisories as SecurityAdvisories_v3_1_3_0,
)
from .v3_1_3_0.sensors import Sensors as Sensors_v3_1_3_0
from .v3_1_3_0.site_design import SiteDesign as SiteDesign_v3_1_3_0
from .v3_1_3_0.sites import Sites as Sites_v3_1_3_0
from .v3_1_3_0.software_image_management_swim import (
    SoftwareImageManagementSwim as SoftwareImageManagementSwim_v3_1_3_0,
)
from .v3_1_3_0.system_settings import SystemSettings as SystemSettings_v3_1_3_0
from .v3_1_3_0.tag import Tag as Tag_v3_1_3_0
from .v3_1_3_0.task import Task as Task_v3_1_3_0
from .v3_1_3_0.topology import Topology as Topology_v3_1_3_0
from .v3_1_3_0.user_and_roles import UserandRoles as UserandRoles_v3_1_3_0
from .v3_1_3_0.users import Users as Users_v3_1_3_0
from .v3_1_3_0.wired import Wired as Wired_v3_1_3_0
from .v3_1_3_0.wireless import Wireless as Wireless_v3_1_3_0

# v3.1.6.0 APIs
from .v3_1_6_0.ai_endpoint_analytics import (
    AiEndpointAnalytics as AiEndpointAnalytics_v3_1_6_0,
)
from .v3_1_6_0.application_policy import ApplicationPolicy as ApplicationPolicy_v3_1_6_0
from .v3_1_6_0.applications import Applications as Applications_v3_1_6_0
from .v3_1_6_0.authentication_management import (
    AuthenticationManagement as AuthenticationManagement_v3_1_6_0,
)
from .v3_1_6_0.backup import Backup as Backup_v3_1_6_0
from .v3_1_6_0.cisco_imc import CiscoIMC as CiscoIMC_v3_1_6_0
from .v3_1_6_0.cisco_trusted_certificates import (
    CiscoTrustedCertificates as CiscoTrustedCertificates_v3_1_6_0,
)
from .v3_1_6_0.clients import Clients as Clients_v3_1_6_0
from .v3_1_6_0.command_runner import CommandRunner as CommandRunner_v3_1_6_0
from .v3_1_6_0.compliance import Compliance as Compliance_v3_1_6_0
from .v3_1_6_0.configuration_archive import (
    ConfigurationArchive as ConfigurationArchive_v3_1_6_0,
)
from .v3_1_6_0.configuration_templates import (
    ConfigurationTemplates as ConfigurationTemplates_v3_1_6_0,
)
from .v3_1_6_0.device_onboarding_pnp import (
    DeviceOnboardingPnp as DeviceOnboardingPnp_v3_1_6_0,
)
from .v3_1_6_0.device_replacement import DeviceReplacement as DeviceReplacement_v3_1_6_0
from .v3_1_6_0.devices import Devices as Devices_v3_1_6_0
from .v3_1_6_0.disaster_recovery import DisasterRecovery as DisasterRecovery_v3_1_6_0
from .v3_1_6_0.discovery import Discovery as Discovery_v3_1_6_0
from .v3_1_6_0.eox import Eox as Eox_v3_1_6_0
from .v3_1_6_0.event_management import EventManagement as EventManagement_v3_1_6_0
from .v3_1_6_0.fabric_wireless import FabricWireless as FabricWireless_v3_1_6_0
from .v3_1_6_0.file import File as File_v3_1_6_0
from .v3_1_6_0.health_and_performance import (
    HealthAndPerformance as HealthAndPerformance_v3_1_6_0,
)
from .v3_1_6_0.itsm import Itsm as Itsm_v3_1_6_0
from .v3_1_6_0.itsm_integration import ItsmIntegration as ItsmIntegration_v3_1_6_0
from .v3_1_6_0.industrial_configuration import (
    IndustrialConfiguration as IndustrialConfiguration_v3_1_6_0,
)
from .v3_1_6_0.issues import Issues as Issues_v3_1_6_0
from .v3_1_6_0.know_your_network import KnowYourNetwork as KnowYourNetwork_v3_1_6_0
from .v3_1_6_0.lan_automation import LanAutomation as LanAutomation_v3_1_6_0
from .v3_1_6_0.licenses import Licenses as Licenses_v3_1_6_0
from .v3_1_6_0.network_settings import NetworkSettings as NetworkSettings_v3_1_6_0
from .v3_1_6_0.path_trace import PathTrace as PathTrace_v3_1_6_0
from .v3_1_6_0.platform import Platform as Platform_v3_1_6_0
from .v3_1_6_0.reports import Reports as Reports_v3_1_6_0
from .v3_1_6_0.restore import Restore as Restore_v3_1_6_0
from .v3_1_6_0.sda import Sda as Sda_v3_1_6_0
from .v3_1_6_0.security_advisories import (
    SecurityAdvisories as SecurityAdvisories_v3_1_6_0,
)
from .v3_1_6_0.sensors import Sensors as Sensors_v3_1_6_0
from .v3_1_6_0.site_design import SiteDesign as SiteDesign_v3_1_6_0
from .v3_1_6_0.sites import Sites as Sites_v3_1_6_0
from .v3_1_6_0.software_image_management_swim import (
    SoftwareImageManagementSwim as SoftwareImageManagementSwim_v3_1_6_0,
)
from .v3_1_6_0.system_settings import SystemSettings as SystemSettings_v3_1_6_0
from .v3_1_6_0.system_software_upgrade import (
    SystemSoftwareUpgrade as SystemSoftwareUpgrade_v3_1_6_0,
)
from .v3_1_6_0.tag import Tag as Tag_v3_1_6_0
from .v3_1_6_0.task import Task as Task_v3_1_6_0
from .v3_1_6_0.topology import Topology as Topology_v3_1_6_0
from .v3_1_6_0.user_and_roles import UserandRoles as UserandRoles_v3_1_6_0
from .v3_1_6_0.users import Users as Users_v3_1_6_0
from .v3_1_6_0.wired import Wired as Wired_v3_1_6_0
from .v3_1_6_0.wireless import Wireless as Wireless_v3_1_6_0

# Custom Calller
from .custom_caller import CustomCaller


class CatalystCenterAPI(object):
    """Cisco Catalyst Center API wrapper.

    Creates a 'session' for all API calls through a created CatalystCenterAPI
    object.  The 'session' handles authentication, provides the needed headers,
    and checks all responses for error conditions.

    CatalystCenterAPI wraps all of the individual Catalyst Center APIs and represents
    them in a simple hierarchical structure.
    """

    def __init__(
        self,
        username=None,
        password=None,
        encoded_auth=None,
        base_url=None,
        single_request_timeout=None,
        wait_on_rate_limit=None,
        session=None,
        verify=None,
        version=None,
        debug=None,
        object_factory=mydict_data_factory,
        validator=SchemaValidator,
        user_agent=None,
    ):
        """Create a new CatalystCenterAPI object.
        An access token is required to interact with the Catalyst Center APIs.
        This package supports two methods for you to generate the
        authorization token:

          1. Provide a encoded_auth value (username:password encoded in
          base 64). *This has priority over the following method*

          2. Provide username and password values.

        This package supports two methods for you to set those values:

          1. Provide the parameter. That is the encoded_auth or
          username and password parameters.

          2. If an argument is not supplied, the package checks for
          its environment variable counterpart. That is the
          CATALYST_CENTER_ENCODED_AUTH, CATALYST_CENTER_USERNAME,
          CATALYST_CENTER_PASSWORD.

        When not given enough parameters an AccessTokenError is raised.

        Args:
            base_url(str): The base URL to be prefixed to the
                individual API endpoint suffixes.
                Defaults to the CATALYST_CENTER_BASE_URL environment variable or
                catalystcentersdk.config.DEFAULT_BASE_URL
                if the environment variable is not set.
            username(str): HTTP Basic Auth username.
            password(str): HTTP Basic Auth password.
            encoded_auth(str): HTTP Basic Auth base64 encoded string.
            single_request_timeout(int): Timeout (in seconds) for RESTful HTTP
                requests. Defaults to the CATALYST_CENTER_SINGLE_REQUEST_TIMEOUT
                environment variable or
                catalystcentersdk.config.DEFAULT_SINGLE_REQUEST_TIMEOUT
                if the environment variable is not set.
            wait_on_rate_limit(bool): Enables or disables automatic rate-limit
                handling. Defaults to the CATALYST_CENTER_WAIT_ON_RATE_LIMIT
                environment variable or
                catalystcentersdk.config.DEFAULT_WAIT_ON_RATE_LIMIT
                if the environment variable is not set.
            verify(bool,str): Controls whether we verify the server's
                TLS certificate, or a string, in which case it must be a path
                to a CA bundle to use. Defaults to the CATALYST_CENTER_VERIFY
                (or CATALYST_CENTER_VERIFY_STRING) environment variable or
                catalystcentersdk.config.DEFAULT_VERIFY if the environment
                variables are not set.
            version(str): Controls which version of CATALYST_CENTER to use.
                Defaults to the CATALYST_CENTER_VERSION environment variable or
                catalystcentersdk.config.DEFAULT_VERSION
                if the environment variable is not set.
            debug(bool,str): Controls whether to log information about
                Catalyst Center APIs' request and response process.
                Defaults to the CATALYST_CENTER_DEBUG environment variable or False
                if the environment variable is not set.
            object_factory(callable): The factory function to use to create
                Python objects from the returned Catalyst Center JSON data objects.
            validator(callable): The factory function to use to validate
                Python objects sent in the body of the request.
            user_string(str): It is part of the user agent and is used to specify a name. catalystcentersdk/v.x.x-user_string

        Returns:
            CatalystCenterAPI: A new CatalystCenterAPI object.

        Raises:
            TypeError: If the parameter types are incorrect.
            AccessTokenError: If an access token is not provided via the
                access_token argument or an environment variable.
            VersionError: If the version is not provided via the version
                argument or an environment variable, or it is not a
                Catalyst Center API supported version
                ['2.3.7.6', '2.3.7.9', '3.1.3.0' and '3.1.6.0'].

        """
        username = username or catalystcenter_environment.get_env_username()
        password = password or catalystcenter_environment.get_env_password()
        encoded_auth = encoded_auth or catalystcenter_environment.get_env_encoded_auth()
        base_url = (
            base_url
            or catalystcenter_environment.get_env_base_url()
            or DEFAULT_BASE_URL
        )
        user_agent = user_agent or catalystcenter_environment.get_env_user_agent()

        if single_request_timeout is None:
            single_request_timeout = (
                catalystcenter_environment.get_env_single_request_timeout()
                or DEFAULT_SINGLE_REQUEST_TIMEOUT
            )

        if wait_on_rate_limit is None:
            wait_on_rate_limit = (
                catalystcenter_environment.get_env_wait_on_rate_limit()
                or DEFAULT_WAIT_ON_RATE_LIMIT
            )

        if verify is None:
            verify = catalystcenter_environment.get_env_verify() or DEFAULT_VERIFY

        version = (
            version or catalystcenter_environment.get_env_version() or DEFAULT_VERSION
        )
        if version == "2.3.7.7":
            version = "2.3.7.6"

        if debug is None:
            debug = catalystcenter_environment.get_env_debug() or DEFAULT_DEBUG

        if user_agent is None:
            user_agent = (
                catalystcenter_environment.get_env_user_agent()
                or DEFAULT_VERIFY_USER_AGENT
            )

        check_type(base_url, str)
        check_type(single_request_timeout, int)
        check_type(wait_on_rate_limit, bool)
        check_type(debug, (bool, str), may_be_none=True)
        check_type(username, str, may_be_none=True)
        check_type(password, str, may_be_none=True)
        check_type(encoded_auth, str, may_be_none=True)
        check_type(verify, (bool, str), may_be_none=False)
        check_type(version, str, may_be_none=False)
        check_type(user_agent, str, may_be_none=False)

        if version not in ["2.3.7.6", "2.3.7.9", "3.1.3.0", "3.1.6.0"]:
            raise VersionError(
                "Unknown API version, "
                + "known versions are {}".format(
                    "2.3.7.6, 2.3.7.9, 3.1.3.0 and 3.1.6.0"
                )
            )

        if isinstance(debug, str):
            debug = "true" in debug.lower()

        # Init Authentication wrapper early to use for basicAuth requests
        self.authentication = Authentication(
            base_url,
            object_factory,
            single_request_timeout=single_request_timeout,
            verify=verify,
        )

        # Check if the user has provided the required basicAuth parameters
        if encoded_auth is None and (username is None or password is None):
            raise AccessTokenError(
                "You need an access token to interact with the Catalyst Center"
                " APIs. Catalyst Center uses HTTP Basic Auth to create an access"
                " token. You must provide the username and password or just"
                " the encoded_auth, either by setting each parameter or its"
                " environment variable counterpart ("
                "CATALYST_CENTER_USERNAME, CATALYST_CENTER_PASSWORD,"
                " CATALYST_CENTER_ENCODED_AUTH)."
            )

        def get_access_token():
            return self.authentication.authentication_api(
                username=username, password=password, encoded_auth=encoded_auth
            ).Token

        # Create the API session
        # All of the API calls associated with a CatalystCenterAPI object will
        # leverage a single RESTful 'session' connecting to the Catalyst Center
        # cloud.
        self._session = RestSession(
            get_access_token=get_access_token,
            access_token=get_access_token(),
            base_url=base_url,
            single_request_timeout=single_request_timeout,
            wait_on_rate_limit=wait_on_rate_limit,
            session=session,
            verify=verify,
            version=version,
            debug=debug,
            user_agent=user_agent,
        )

        _validator = validator(version).json_schema_validate

        # API wrappers
        if version == "2.3.7.6":
            self.ai_endpoint_analytics = AIEndpointAnalytics_v2_3_7_6_1(
                self._session, object_factory, _validator
            )
            self.authentication_management = AuthenticationManagement_v2_3_7_6_1(
                self._session, object_factory, _validator
            )
            self.application_policy = ApplicationPolicy_v2_3_7_6_1(
                self._session, object_factory, _validator
            )
            self.applications = Applications_v2_3_7_6_1(
                self._session, object_factory, _validator
            )
            self.cisco_trusted_certificates = CiscoTrustedCertificates_v2_3_7_6_1(
                self._session, object_factory, _validator
            )
            self.clients = Clients_v2_3_7_6_1(self._session, object_factory, _validator)
            self.command_runner = CommandRunner_v2_3_7_6_1(
                self._session, object_factory, _validator
            )
            self.compliance = Compliance_v2_3_7_6_1(
                self._session, object_factory, _validator
            )
            self.configuration_archive = ConfigurationArchive_v2_3_7_6_1(
                self._session, object_factory, _validator
            )
            self.configuration_templates = ConfigurationTemplates_v2_3_7_6_1(
                self._session, object_factory, _validator
            )
            self.device_onboarding_pnp = DeviceOnboardingPnp_v2_3_7_6_1(
                self._session, object_factory, _validator
            )
            self.device_replacement = DeviceReplacement_v2_3_7_6_1(
                self._session, object_factory, _validator
            )
            self.devices = Devices_v2_3_7_6_1(self._session, object_factory, _validator)
            self.disaster_recovery = DisasterRecovery_v2_3_7_6_1(
                self._session, object_factory, _validator
            )
            self.discovery = Discovery_v2_3_7_6_1(
                self._session, object_factory, _validator
            )
            self.eox = EoX_v2_3_7_6_1(self._session, object_factory, _validator)
            self.event_management = EventManagement_v2_3_7_6_1(
                self._session, object_factory, _validator
            )
            self.fabric_wireless = FabricWireless_v2_3_7_6_1(
                self._session, object_factory, _validator
            )
            self.file = File_v2_3_7_6_1(self._session, object_factory, _validator)
            self.health_and_performance = HealthAndPerformance_v2_3_7_6_1(
                self._session, object_factory, _validator
            )
            self.itsm = Itsm_v2_3_7_6_1(self._session, object_factory, _validator)
            self.itsm_integration = ItsmIntegration_v2_3_7_6_1(
                self._session, object_factory, _validator
            )
            self.issues = Issues_v2_3_7_6_1(self._session, object_factory, _validator)
            self.lan_automation = LanAutomation_v2_3_7_6_1(
                self._session, object_factory, _validator
            )
            self.licenses = Licenses_v2_3_7_6_1(
                self._session, object_factory, _validator
            )
            self.network_settings = NetworkSettings_v2_3_7_6_1(
                self._session, object_factory, _validator
            )
            self.path_trace = PathTrace_v2_3_7_6_1(
                self._session, object_factory, _validator
            )
            self.platform = Platform_v2_3_7_6_1(
                self._session, object_factory, _validator
            )
            self.reports = Reports_v2_3_7_6_1(self._session, object_factory, _validator)
            self.sda = Sda_v2_3_7_6_1(self._session, object_factory, _validator)
            self.security_advisories = SecurityAdvisories_v2_3_7_6_1(
                self._session, object_factory, _validator
            )
            self.sensors = Sensors_v2_3_7_6_1(self._session, object_factory, _validator)
            self.site_design = SiteDesign_v2_3_7_6_1(
                self._session, object_factory, _validator
            )
            self.sites = Sites_v2_3_7_6_1(self._session, object_factory, _validator)
            self.software_image_management_swim = (
                SoftwareImageManagementSwim_v2_3_7_6_1(
                    self._session, object_factory, _validator
                )
            )
            self.system_settings = SystemSettings_v2_3_7_6_1(
                self._session, object_factory, _validator
            )
            self.tag = Tag_v2_3_7_6_1(self._session, object_factory, _validator)
            self.task = Task_v2_3_7_6_1(self._session, object_factory, _validator)
            self.topology = Topology_v2_3_7_6_1(
                self._session, object_factory, _validator
            )
            self.user_and_roles = UserandRoles_v2_3_7_6_1(
                self._session, object_factory, _validator
            )
            self.users = Users_v2_3_7_6_1(self._session, object_factory, _validator)
            self.wireless = Wireless_v2_3_7_6_1(
                self._session, object_factory, _validator
            )

        if version == "2.3.7.9":
            self.a_i_endpoint_analytics = AIEndpointAnalytics_v2_3_7_9(
                self._session, object_factory, _validator
            )
            self.application_policy = ApplicationPolicy_v2_3_7_9(
                self._session, object_factory, _validator
            )
            self.applications = Applications_v2_3_7_9(
                self._session, object_factory, _validator
            )
            self.cisco_i_m_c = CiscoIMC_v2_3_7_9(
                self._session, object_factory, _validator
            )
            self.authentication_management = AuthenticationManagement_v2_3_7_9(
                self._session, object_factory, _validator
            )
            self.cisco_trusted_certificates = CiscoTrustedCertificates_v2_3_7_9(
                self._session, object_factory, _validator
            )
            self.clients = Clients_v2_3_7_9(self._session, object_factory, _validator)
            self.command_runner = CommandRunner_v2_3_7_9(
                self._session, object_factory, _validator
            )
            self.compliance = Compliance_v2_3_7_9(
                self._session, object_factory, _validator
            )
            self.configuration_archive = ConfigurationArchive_v2_3_7_9(
                self._session, object_factory, _validator
            )
            self.configuration_templates = ConfigurationTemplates_v2_3_7_9(
                self._session, object_factory, _validator
            )
            self.device_onboarding_pnp = DeviceOnboardingPnp_v2_3_7_9(
                self._session, object_factory, _validator
            )
            self.device_replacement = DeviceReplacement_v2_3_7_9(
                self._session, object_factory, _validator
            )
            self.devices = Devices_v2_3_7_9(self._session, object_factory, _validator)
            self.disaster_recovery = DisasterRecovery_v2_3_7_9(
                self._session, object_factory, _validator
            )
            self.discovery = Discovery_v2_3_7_9(
                self._session, object_factory, _validator
            )
            self.eox = Eox_v2_3_7_9(self._session, object_factory, _validator)
            self.event_management = EventManagement_v2_3_7_9(
                self._session, object_factory, _validator
            )
            self.fabric_wireless = FabricWireless_v2_3_7_9(
                self._session, object_factory, _validator
            )
            self.file = File_v2_3_7_9(self._session, object_factory, _validator)
            self.health_and_performance = HealthAndPerformance_v2_3_7_9(
                self._session, object_factory, _validator
            )
            self.itsm = Itsm_v2_3_7_9(self._session, object_factory, _validator)
            self.itsm_integration = ItsmIntegration_v2_3_7_9(
                self._session, object_factory, _validator
            )
            self.issues = Issues_v2_3_7_9(self._session, object_factory, _validator)
            self.lan_automation = LanAutomation_v2_3_7_9(
                self._session, object_factory, _validator
            )
            self.licenses = Licenses_v2_3_7_9(self._session, object_factory, _validator)
            self.network_settings = NetworkSettings_v2_3_7_9(
                self._session, object_factory, _validator
            )
            self.path_trace = PathTrace_v2_3_7_9(
                self._session, object_factory, _validator
            )
            self.platform = Platform_v2_3_7_9(self._session, object_factory, _validator)
            self.reports = Reports_v2_3_7_9(self._session, object_factory, _validator)
            self.sda = Sda_v2_3_7_9(self._session, object_factory, _validator)
            self.security_advisories = SecurityAdvisories_v2_3_7_9(
                self._session, object_factory, _validator
            )
            self.sensors = Sensors_v2_3_7_9(self._session, object_factory, _validator)
            self.site_design = SiteDesign_v2_3_7_9(
                self._session, object_factory, _validator
            )
            self.sites = Sites_v2_3_7_9(self._session, object_factory, _validator)
            self.software_image_management_swim = SoftwareImageManagementSwim_v2_3_7_9(
                self._session, object_factory, _validator
            )
            self.system_settings = SystemSettings_v2_3_7_9(
                self._session, object_factory, _validator
            )
            self.tag = Tag_v2_3_7_9(self._session, object_factory, _validator)
            self.task = Task_v2_3_7_9(self._session, object_factory, _validator)
            self.topology = Topology_v2_3_7_9(self._session, object_factory, _validator)
            self.user_and_roles = UserandRoles_v2_3_7_9(
                self._session, object_factory, _validator
            )
            self.users = Users_v2_3_7_9(self._session, object_factory, _validator)
            self.wireless = Wireless_v2_3_7_9(self._session, object_factory, _validator)

        if version == "3.1.3.0":
            self.ai_endpoint_analytics = AIEndpointAnalytics_v3_1_3_0(
                self._session, object_factory, _validator
            )
            self.application_policy = ApplicationPolicy_v3_1_3_0(
                self._session, object_factory, _validator
            )
            self.applications = Applications_v3_1_3_0(
                self._session, object_factory, _validator
            )
            self.authentication_management = AuthenticationManagement_v3_1_3_0(
                self._session, object_factory, _validator
            )
            self.backup = Backup_v3_1_3_0(self._session, object_factory, _validator)
            self.cisco_i_m_c = CiscoIMC_v3_1_3_0(
                self._session, object_factory, _validator
            )
            self.cisco_trusted_certificates = CiscoTrustedCertificates_v3_1_3_0(
                self._session, object_factory, _validator
            )
            self.clients = Clients_v3_1_3_0(self._session, object_factory, _validator)
            self.command_runner = CommandRunner_v3_1_3_0(
                self._session, object_factory, _validator
            )
            self.compliance = Compliance_v3_1_3_0(
                self._session, object_factory, _validator
            )
            self.configuration_archive = ConfigurationArchive_v3_1_3_0(
                self._session, object_factory, _validator
            )
            self.configuration_templates = ConfigurationTemplates_v3_1_3_0(
                self._session, object_factory, _validator
            )
            self.device_onboarding_pnp = DeviceOnboardingPnp_v3_1_3_0(
                self._session, object_factory, _validator
            )
            self.device_replacement = DeviceReplacement_v3_1_3_0(
                self._session, object_factory, _validator
            )
            self.devices = Devices_v3_1_3_0(self._session, object_factory, _validator)
            self.disaster_recovery = DisasterRecovery_v3_1_3_0(
                self._session, object_factory, _validator
            )
            self.discovery = Discovery_v3_1_3_0(
                self._session, object_factory, _validator
            )
            self.eox = Eox_v3_1_3_0(self._session, object_factory, _validator)
            self.event_management = EventManagement_v3_1_3_0(
                self._session, object_factory, _validator
            )
            self.fabric_wireless = FabricWireless_v3_1_3_0(
                self._session, object_factory, _validator
            )
            self.file = File_v3_1_3_0(self._session, object_factory, _validator)
            self.health_and_performance = HealthAndPerformance_v3_1_3_0(
                self._session, object_factory, _validator
            )
            self.itsm = Itsm_v3_1_3_0(self._session, object_factory, _validator)
            self.itsm_integration = ItsmIntegration_v3_1_3_0(
                self._session, object_factory, _validator
            )
            self.industrial_configuration = IndustrialConfiguration_v3_1_3_0(
                self._session, object_factory, _validator
            )
            self.issues = Issues_v3_1_3_0(self._session, object_factory, _validator)
            self.know_your_network = KnowYourNetwork_v3_1_3_0(
                self._session, object_factory, _validator
            )
            self.lan_automation = LanAutomation_v3_1_3_0(
                self._session, object_factory, _validator
            )
            self.licenses = Licenses_v3_1_3_0(self._session, object_factory, _validator)
            self.network_settings = NetworkSettings_v3_1_3_0(
                self._session, object_factory, _validator
            )
            self.path_trace = PathTrace_v3_1_3_0(
                self._session, object_factory, _validator
            )
            self.platform = Platform_v3_1_3_0(self._session, object_factory, _validator)
            self.reports = Reports_v3_1_3_0(self._session, object_factory, _validator)
            self.restore = Restore_v3_1_3_0(self._session, object_factory, _validator)
            self.sda = Sda_v3_1_3_0(self._session, object_factory, _validator)
            self.security_advisories = SecurityAdvisories_v3_1_3_0(
                self._session, object_factory, _validator
            )
            self.sensors = Sensors_v3_1_3_0(self._session, object_factory, _validator)
            self.site_design = SiteDesign_v3_1_3_0(
                self._session, object_factory, _validator
            )
            self.sites = Sites_v3_1_3_0(self._session, object_factory, _validator)
            self.software_image_management_swim = SoftwareImageManagementSwim_v3_1_3_0(
                self._session, object_factory, _validator
            )
            self.system_settings = SystemSettings_v3_1_3_0(
                self._session, object_factory, _validator
            )
            self.tag = Tag_v3_1_3_0(self._session, object_factory, _validator)
            self.task = Task_v3_1_3_0(self._session, object_factory, _validator)
            self.topology = Topology_v3_1_3_0(self._session, object_factory, _validator)
            self.user_and_roles = UserandRoles_v3_1_3_0(
                self._session, object_factory, _validator
            )
            self.users = Users_v3_1_3_0(self._session, object_factory, _validator)
            self.wired = Wired_v3_1_3_0(self._session, object_factory, _validator)
            self.wireless = Wireless_v3_1_3_0(self._session, object_factory, _validator)

        if version == "3.1.6.0":
            self.ai_endpoint_analytics = AiEndpointAnalytics_v3_1_6_0(
                self._session, object_factory, _validator
            )
            self.application_policy = ApplicationPolicy_v3_1_6_0(
                self._session, object_factory, _validator
            )
            self.applications = Applications_v3_1_6_0(
                self._session, object_factory, _validator
            )
            self.authentication_management = AuthenticationManagement_v3_1_6_0(
                self._session, object_factory, _validator
            )
            self.backup = Backup_v3_1_6_0(self._session, object_factory, _validator)
            self.cisco_i_m_c = CiscoIMC_v3_1_6_0(
                self._session, object_factory, _validator
            )
            self.cisco_trusted_certificates = CiscoTrustedCertificates_v3_1_6_0(
                self._session, object_factory, _validator
            )
            self.clients = Clients_v3_1_6_0(self._session, object_factory, _validator)
            self.command_runner = CommandRunner_v3_1_6_0(
                self._session, object_factory, _validator
            )
            self.compliance = Compliance_v3_1_6_0(
                self._session, object_factory, _validator
            )
            self.configuration_archive = ConfigurationArchive_v3_1_6_0(
                self._session, object_factory, _validator
            )
            self.configuration_templates = ConfigurationTemplates_v3_1_6_0(
                self._session, object_factory, _validator
            )
            self.device_onboarding_pnp = DeviceOnboardingPnp_v3_1_6_0(
                self._session, object_factory, _validator
            )
            self.device_replacement = DeviceReplacement_v3_1_6_0(
                self._session, object_factory, _validator
            )
            self.devices = Devices_v3_1_6_0(self._session, object_factory, _validator)
            self.disaster_recovery = DisasterRecovery_v3_1_6_0(
                self._session, object_factory, _validator
            )
            self.discovery = Discovery_v3_1_6_0(
                self._session, object_factory, _validator
            )
            self.eox = Eox_v3_1_6_0(self._session, object_factory, _validator)
            self.event_management = EventManagement_v3_1_6_0(
                self._session, object_factory, _validator
            )
            self.fabric_wireless = FabricWireless_v3_1_6_0(
                self._session, object_factory, _validator
            )
            self.file = File_v3_1_6_0(self._session, object_factory, _validator)
            self.health_and_performance = HealthAndPerformance_v3_1_6_0(
                self._session, object_factory, _validator
            )
            self.itsm = Itsm_v3_1_6_0(self._session, object_factory, _validator)
            self.itsm_integration = ItsmIntegration_v3_1_6_0(
                self._session, object_factory, _validator
            )
            self.industrial_configuration = IndustrialConfiguration_v3_1_6_0(
                self._session, object_factory, _validator
            )
            self.issues = Issues_v3_1_6_0(self._session, object_factory, _validator)
            self.know_your_network = KnowYourNetwork_v3_1_6_0(
                self._session, object_factory, _validator
            )
            self.lan_automation = LanAutomation_v3_1_6_0(
                self._session, object_factory, _validator
            )
            self.licenses = Licenses_v3_1_6_0(self._session, object_factory, _validator)
            self.network_settings = NetworkSettings_v3_1_6_0(
                self._session, object_factory, _validator
            )
            self.path_trace = PathTrace_v3_1_6_0(
                self._session, object_factory, _validator
            )
            self.platform = Platform_v3_1_6_0(self._session, object_factory, _validator)
            self.reports = Reports_v3_1_6_0(self._session, object_factory, _validator)
            self.restore = Restore_v3_1_6_0(self._session, object_factory, _validator)
            self.sda = Sda_v3_1_6_0(self._session, object_factory, _validator)
            self.security_advisories = SecurityAdvisories_v3_1_6_0(
                self._session, object_factory, _validator
            )
            self.sensors = Sensors_v3_1_6_0(self._session, object_factory, _validator)
            self.site_design = SiteDesign_v3_1_6_0(
                self._session, object_factory, _validator
            )
            self.sites = Sites_v3_1_6_0(self._session, object_factory, _validator)
            self.software_image_management_swim = SoftwareImageManagementSwim_v3_1_6_0(
                self._session, object_factory, _validator
            )
            self.system_settings = SystemSettings_v3_1_6_0(
                self._session, object_factory, _validator
            )
            self.system_software_upgrade = SystemSoftwareUpgrade_v3_1_6_0(
                self._session, object_factory, _validator
            )
            self.tag = Tag_v3_1_6_0(self._session, object_factory, _validator)
            self.task = Task_v3_1_6_0(self._session, object_factory, _validator)
            self.topology = Topology_v3_1_6_0(self._session, object_factory, _validator)
            self.user_and_roles = UserandRoles_v3_1_6_0(
                self._session, object_factory, _validator
            )
            self.users = Users_v3_1_6_0(self._session, object_factory, _validator)
            self.wired = Wired_v3_1_6_0(self._session, object_factory, _validator)
            self.wireless = Wireless_v3_1_6_0(self._session, object_factory, _validator)

        self.custom_caller = CustomCaller(self._session, object_factory)

    @property
    def session(self):
        """The Catalyst Center API session."""
        return self._session

    @property
    def access_token(self):
        """The access token used for API calls to the Catalyst Center service."""
        return self._session.access_token

    @property
    def base_url(self):
        """The base URL prefixed to the individual API endpoint suffixes."""
        return self._session.base_url

    @property
    def user_agent(self):
        """The API user agent."""
        return self._session.user_agent

    @property
    def user_string(self):
        """The API user string."""
        return self._session.user_string

    @user_string.setter
    def user_string(self, value):
        self._session.user_string = value

    @property
    def single_request_timeout(self):
        """Timeout (in seconds) for an single HTTP request."""
        return self._session.single_request_timeout

    @property
    def wait_on_rate_limit(self):
        """Automatic rate-limit handling enabled / disabled."""
        return self._session.wait_on_rate_limit

    @property
    def verify(self):
        """The verify (TLS Certificate) for the API endpoints."""
        return self._session._verify

    @property
    def version(self):
        """The API version of Catalyst Center."""
        return self._session._version

    @verify.setter
    def verify(self, value):
        """The verify (TLS Certificate) for the API endpoints."""
        self.authentication.verify = value
        self._session.verify = value

    @base_url.setter
    def base_url(self, value):
        """The base URL for the API endpoints."""
        self._session.base_url = value

    @single_request_timeout.setter
    def single_request_timeout(self, value):
        """The timeout (seconds) for a single HTTP REST API request."""
        self.authentication.single_request_timeout = value
        self._session.single_request_timeout = value

    @wait_on_rate_limit.setter
    def wait_on_rate_limit(self, value):
        """Enable or disable automatic rate-limit handling."""
        self._session.wait_on_rate_limit = value
