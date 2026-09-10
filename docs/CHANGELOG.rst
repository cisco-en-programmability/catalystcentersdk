Changelog
=========

All notable changes to this project will be documented in this file.

The format is based on `Keep a
Changelog <https://keepachangelog.com/en/1.0.0/>`__, and this project
adheres to `Semantic
Versioning <https://semver.org/spec/v2.0.0.html>`__.

`Unreleased <https://github.com/cisco-en-programmability/catalystcentersdk/compare/v3.2.3.0.1...develop>`__
-----------------------------------------------------------------------------------------------------------

`3.2.3.0.1 <https://github.com/cisco-en-programmability/catalystcentersdk/compare/v3.2.3.0.0...v3.2.3.0.1>`__ - 2026-09-07
--------------------------------------------------------------------------------------------------------------------------

Fixed
~~~~~

- **Names dropped in 3.2.3.0.0 (issues #57, #58, #60, #62, #64, #65)**:
  collapsed acronyms (``_r_r_m_``, ``_l_s_c_``, ``_n_f_s_``,
  ``_i_m_c_``, ``_d_h_c_p_`` and the rest), the move to ``get_all_*`` /
  ``get_count_of_*``, and alias blocks that were not carried over left
  53 names raising ``AttributeError`` on upgrade. All are back, plus the
  ``UserandRoles`` class name. Four ``Wireless`` aliases reach a method
  whose parameters moved upstream, ``CalendarProfileSetting`` to
  ``calendarProfile`` among them, so pass arguments as keywords.
- **Plain names repointed to ``/v2/`` (issues #59, #61)**:
  ``ApplicationPolicy.get_application_sets``, ``get_applications``,
  ``delete_application_set``, ``delete_application``, ``Sites.get_site``
  and ``get_site_count`` mean the v1 operation again with their
  3.1.6.0.7 signatures, raising neither ``TypeError`` nor unfiltered
  results; the v2 operations keep their ``_v2`` names.
- **File downloads (issue #63)**: the two ``ConfigurationArchive``
  configuration downloads stream again instead of raising
  ``JSONDecodeError``, and ``Reports.download_flexible_report`` and
  ``Sensors.downloads_a_specific_icap_packet_capture_file`` now stream
  as well, returning ``DownloadResponse`` instead of ``MyDict``.

Removed
~~~~~~~

- The README’s “Method naming and v1/v2 aliases” section.

.. _section-1:

`3.2.3.0.0 <https://github.com/cisco-en-programmability/catalystcentersdk/compare/v3.1.6.0.7...v3.2.3.0.0>`__ - 2026-08-20
--------------------------------------------------------------------------------------------------------------------------

Added
~~~~~

- Add support of Cisco Catalyst Center version (‘3.2.3.0’)
- Adds modules for v3_2_3_0
- New service for Cisco Catalyst Center 3.2.3.0’s API:

  - ``security``

Changed
~~~~~~~

- Cisco Catalyst Center 3.2.3.0’s API drops the
  ``ai_endpoint_analytics`` and ``disaster_recovery`` tags present in
  3.1.6.0; these services are not available under version 3.2.3.0.
- Standardized class name capitalization for ``AIEndpointAnalytics``,
  ``EoX``, ``CiscoIMC``, and ``UserAndRoles`` across all API versions;
  the previous spellings (``AiEndpointAnalytics``, ``Eox``,
  ``CiscoImc``, ``UserandRoles``) remain available as class aliases.
- Renamed module ``cisco_i_m_c.py`` to ``cisco_imc.py`` for versions
  2.3.7.9 and 3.1.3.0 (already correct in 3.1.6.0 and 3.2.3.0); the old
  filename is kept as a backward-compatible shim re-exporting
  ``CiscoIMC``.
- Established a consistent v1/v2 method naming convention, documented in
  the README under “Method naming and v1/v2 aliases”: the v2 operation
  is the canonical method name and also gets a ``_v2`` alias, while the
  v1 operation keeps its ``_v1`` suffix and additionally gets a
  bare-name alias whenever its own operationId differs from the v2
  side’s.

.. _fixed-1:

Fixed
~~~~~

- **Duplicate keyword argument crash on parameters shared by path and
  body (e.g. ``id``)**: The generator’s parameter sorter could resolve a
  name collision between a required path parameter and an optional body
  property of the same name in favor of the optional one, silently
  turning a required path segment into an omittable ``id=None``, or
  otherwise raise ``SyntaxError: keyword argument repeated`` in
  generated code. Fixed the generator to always prefer the required
  occurrence and resynced the affected methods
  (e.g. ``update_application_health_score_definition_for_the_given_id``
  in 3.2.3.0).
- **``get_template_versions`` /
  ``gets_all_the_versions_of_a_given_template`` naming collision**: A
  stale ``rename_endpoints`` shortcut collapsed two distinct
  Configuration Templates operations onto the same method name, silently
  shadowing one of them across all API versions. Removed the stale
  shortcut so both operations are reachable under their own names.
- **``lan_automation_start_v2`` alias missing (3.2.3.0)**: The generator
  template only supported one alias per endpoint, so this genuine
  ``_v2`` alias was being silently shadowed by an unrelated short alias
  (``start``). Fixed the template to support multiple aliases per
  endpoint, restoring ``lan_automation_start_v2``.
- **``Sda.get_site_v2`` incorrectly pointed to a v1-only endpoint
  (3.2.3.0)**: A ``rename_endpoints`` shortcut for SDA’s
  ``GetSiteFromSDAFabric`` collided by name with an unrelated
  ``Sites``-tag alias, producing a bogus ``get_site_v2`` method that
  actually called the v1 SDA endpoint. Removed the incorrect alias.
- **Missing v1/v2 divergent-name aliases (3.2.3.0)**: Cisco does not
  always name both sides of a v1/v2 pair the same way (for example the
  v1 side of “create an application set” is ``CreateApplicationSetV1``,
  singular, while the v2 side is ``CreateApplicationSets``, plural).
  Added bare-name aliases so the v1 method is also reachable under its
  own identity: ``ApplicationPolicy.create_application_set``,
  ``get_application_sets_count``, ``edit_application``,
  ``create_application``, ``get_applications_count``;
  ``ConfigurationTemplates.gets_the_templates_available``;
  ``UserAndRoles.get_roles_api``.
- **Missing aliases required by the ``cisco.catalystcenter`` Ansible
  collection (3.2.3.0)**: Added ``Discovery.get_global_credentials`` and
  ``Licenses.retrieves_c_s_s_m_connection_mode`` /
  ``update_c_s_s_m_connection_mode`` aliases so the collection’s
  existing calls resolve correctly under 3.2.3.0.
- **Legacy ``dnacentersdk`` rebranding leftovers in the 3.1.6.0 test
  suite**: Fixed lingering ``dnacentersdk`` imports across 1353
  validator files and 49 API test files, stray ``DNA_CENTER_VERSION`` /
  ``DNA_CENTER_USERNAME`` / ``DNA_CENTER_PASSWORD`` environment variable
  references across the test suite, a ``cisco_i_m_c`` import path
  mismatch in ``test_catalystcentersdk.py``, and a
  ``catalystcentersdkersdk`` typo in ``test_restsession.py``. None of
  these affected the published package; they only blocked running the
  test suite from source.
- Registered the 3.2.3.0 mock server and added its missing pytest
  markers (``security``, ``ai_endpoint_analytics``, ``backup``,
  ``cisco_imc``, ``cisco_trusted_certificates``,
  ``industrial_configuration``, ``know_your_network``, ``restore``,
  ``system_software_upgrade``, ``wired``) to ``conftest.py``, so the
  test suite collects and runs cleanly for 3.2.3.0.

.. _section-2:

`3.1.6.0.7 <https://github.com/cisco-en-programmability/catalystcentersdk/compare/v3.1.6.0.6...v3.1.6.0.7>`__ - 2026-07-28
--------------------------------------------------------------------------------------------------------------------------

.. _fixed-2:

Fixed
~~~~~

- **Missing backward-compatibility aliases in v2.3.7.6.1 (Issues #44,
  #45, #46)**: Three v2.3.7.6.1 API classes exposed ``_v2`` methods
  without the historical compatibility alias present in v3.1.6.0,
  raising ``AttributeError`` for Catalyst Center 2.3.7.6 users and
  breaking the ``cisco.catalystcenter`` Ansible collection’s
  ``device_templates``, ``site_hierarchy``, ``device_credentials``, and
  ``device_discovery`` workflows. Added the missing aliases:
  ``ConfigurationTemplates.get_templates_details`` to
  ``get_templates_details_v2``, ``SiteDesign.deletes_a_floor`` to
  ``deletes_a_floor_v2``, and ``Discovery.get_all_global_credentials``
  to ``get_all_global_credentials_v2``.
- **Additional missing v2.3.7.6.1 aliases found by audit**: After fixing
  Issues #44-#46, audited every v2.3.7.6.1 module against its v3.1.6.0
  counterpart for the same class of missing compatibility alias. Found
  and fixed 22 more across 8 modules: ``ApplicationPolicy``
  (``create_application_sets``, ``get_application_set_count``,
  ``create_applications``, ``edit_applications``,
  ``get_application_count``), ``ConfigurationTemplates``
  (``get_projects_details``), ``Devices``
  (``get_device_interface_stats_info``), ``Discovery``
  (``create_global_credentials``, ``delete_global_credential``),
  ``EventManagement`` (``get_eventartifacts``), ``File``
  (``download_a_file_by_fileid``), ``Sda``
  (``get_port_channels_connectivity``), ``SiteDesign`` (7 more
  building/floor methods), and ``UserandRoles`` (``get_users``,
  ``add_user``, ``update_user``). Each alias was verified to resolve to
  a method hitting the same REST endpoint in both versions before being
  added.

.. _section-3:

`3.1.6.0.6 <https://github.com/cisco-en-programmability/catalystcentersdk/compare/v3.1.6.0.5...v3.1.6.0.6>`__ - 2026-07-09
--------------------------------------------------------------------------------------------------------------------------

.. _fixed-3:

Fixed
~~~~~

- **Missing backward-compatibility aliases for renamed Site Design
  ``_v2`` methods (Issue #39)**: The v3.1.6.0 API classes renamed
  several Site Design operations with a ``_v2`` suffix and re-exposed
  the historical names as aliases, but seven access point position
  methods on ``SiteDesign`` were left without one. Calling them by their
  historical name raised ``AttributeError`` when the SDK ran against API
  version 3.1.6.0, breaking downstream consumers such as the
  ``cisco.catalystcenter`` Ansible collection. Added the missing aliases
  so the following names resolve again: ``get_access_points_positions``,
  ``edit_the_access_points_positions``,
  ``assign_planned_access_points_to_operations_ones``,
  ``add_planned_access_points_positions``,
  ``edit_planned_access_points_positions``,
  ``get_planned_access_points_positions_count``, and
  ``delete_planned_access_points_position``.

.. _section-4:

`3.1.6.0.5 <https://github.com/cisco-en-programmability/catalystcentersdk/compare/v3.1.6.0.4...v3.1.6.0.5>`__ - 2026-06-05
--------------------------------------------------------------------------------------------------------------------------

.. _fixed-4:

Fixed
~~~~~

- **Missing ``licenseLevel``, ``topOfStackSerialNumber``, and
  ``cablingScheme`` in ``claim_a_device_to_a_site`` (Issue #23)**: Added
  the three missing parameters to the method signature, ``_payload``
  assembly, and request validator JSON schema across all SDK API
  versions (2.3.7.6.1, 2.3.7.9, 3.1.3.0, 3.1.6.0). Previously, passing
  these fields with ``active_validation=True`` caused a
  ``MalformedRequest`` error, and with ``active_validation=False`` they
  were silently dropped from the request body, making it impossible to
  claim stacked Catalyst switches with a license level or cabling scheme
  via the SDK.

.. _section-5:

`3.1.6.0.4 <https://github.com/cisco-en-programmability/catalystcentersdk/compare/v3.1.6.0.3...v3.1.6.0.4>`__ - 2026-05-07
--------------------------------------------------------------------------------------------------------------------------

.. _fixed-5:

Fixed
~~~~~

- **Authorization retries not applying to auth requests (PR #248
  equivalent)**: The ``Authentication`` class was issuing token requests
  via bare ``requests.post()`` calls, bypassing any ``urllib3.Retry``
  adapter configured on the session. This meant user-configured retry
  logic — intended to handle intermittent network issues — was silently
  ignored during authentication. ``Authentication`` now accepts an
  optional ``requests.Session`` and uses it for token requests, so retry
  adapters apply uniformly across all SDK calls.

.. _section-6:

`3.1.6.0.3 <https://github.com/cisco-en-programmability/catalystcentersdk/compare/v3.1.6.0.2...v3.1.6.0.3>`__ - 2026-05-05
--------------------------------------------------------------------------------------------------------------------------

.. _fixed-6:

Fixed
~~~~~

- **Content-Type None TypeError (Issue #18)**: Fixed
  ``pprint_response_info()`` in ``utils.py`` crashing with
  ``TypeError: argument of type 'NoneType' is not iterable`` when an API
  response lacks a ``Content-Type`` header. Changed
  ``response.headers.get("Content-Type")`` to
  ``response.headers.get("Content-Type", "")`` so the ``in`` check
  safely handles ``None``.
- **Webhook destination headers collision (Issue #20)**: Fixed
  ``TypeError`` in ``create_webhook_destination()`` and
  ``update_webhook_destination()`` across all API versions (2.3.7.6.1,
  2.3.7.9, 3.1.3.0, 3.1.6.0) in the Event Management module. The
  ``headers`` parameter was incorrectly overloaded for both webhook
  custom headers (list) and HTTP request headers (dict). Renamed the
  webhook payload field parameter to ``webhook_headers`` to eliminate
  the collision. Users must now pass custom webhook headers via
  ``webhook_headers=[...]``; the ``headers`` parameter continues to
  accept a dict for HTTP transport.
- **Missing ``udldGlobalConfig`` support (Issue #17 equivalent / Issue
  #246)**: Added ``udldGlobalConfig`` parameter to
  ``create_configurations_for_an_intended_layer2_feature_on_a_wired_device()``
  and
  ``update_configurations_for_an_intended_layer2_feature_on_a_wired_device()``
  across all API versions (2.3.7.9, 3.1.3.0, 3.1.6.0) in the Wired
  module. UDLD global configuration can now be created and updated
  through the SDK.
- **Port Channel Configuration key casing (portchannelConfig)**: Fixed
  payload key mismatch in
  ``create_configurations_for_an_intended_layer2_feature_on_a_wired_device()``
  and
  ``update_configurations_for_an_intended_layer2_feature_on_a_wired_device()``
  for API versions 2.3.7.9 and 3.1.3.0. The payload key
  ``"portChannelConfig"`` (uppercase C) was renamed to
  ``"portchannelConfig"`` (lowercase c) to match the API’s expected
  format, consistent with v3.1.6.0 and the dnacentersdk. Updated request
  validator schemas for v3.1.3.0 and v3.1.6.0
  (``jsd_d7b57050bdb98e9340d0bc4dba``,
  ``jsd_ee7664344f50cb8f2c94beaa01629d``) to use the same corrected key.
- **``udldGlobalConfig`` validator relaxed**: Replaced the strict
  ``udldGlobalConfig`` JSON schema (which constrained ``configType`` to
  an enum, ``isUdldEnabled``/``udldAggressive`` to booleans, and
  ``messageTime`` to integer) with an open schema (``{}``) across all
  API versions (2.3.7.9, 3.1.3.0, 3.1.6.0). The field is not present in
  the official Cisco Catalyst Center OpenAPI specification, so a
  permissive schema prevents false validation failures as the API
  evolves.

.. _section-7:

`3.1.6.0.2 <https://github.com/cisco-en-programmability/catalystcentersdk/compare/v3.1.6.0.1...v3.1.6.0.2>`__ - 2026-03-30
--------------------------------------------------------------------------------------------------------------------------

.. _fixed-7:

Fixed
~~~~~

- Added missing ``dirpath``, ``save_file``, ``filename`` parameters and
  ``stream=True`` to ``download_masked_device_configuration`` and
  ``download_unmaskedraw_device_configuration_as_zip`` methods in
  Configuration Archive module for versions 2.3.7.9, 3.1.3.0 and
  3.1.6.0. These parameters are required for file download functionality
  to work correctly.

.. _changed-1:

Changed
~~~~~~~

- Updated ``requests`` dependency minimum version from 2.32.0 to 2.33.0
  across pyproject.toml, Pipfile, and setup.py.
- Regenerated Pipfile.lock, poetry.lock, requirements.txt, and
  requirements-dev.txt with updated dependencies.

.. _section-8:

`3.1.6.0.1 <https://github.com/cisco-en-programmability/catalystcentersdk/compare/v3.1.6.0.0...v3.1.6.0.1>`__ - 2026-02-27
--------------------------------------------------------------------------------------------------------------------------

.. _fixed-8:

Fixed
~~~~~

- Corrected ``offset`` and ``limit`` parameter types from ``str`` to
  ``int`` in pagination-related API methods across versions 2.3.7.6.1,
  2.3.7.9, and 3.1.3.0. Affected modules: Sites, Devices, Application
  Policy, LAN Automation, SDA, and Wireless.
- Corrected parameter type annotations in v3.1.6.0 for Configuration
  Templates (``templates``, ``resourceParams``), Devices
  (``attributes``, ``aggregateAttributes``, ``groupBy``), and Reports
  (``schedule``, ``deliveries``).
- Updated request validation schemas across versions 2.3.7.6.1, 2.3.7.9,
  3.1.3.0, and 3.1.6.0.

.. _changed-2:

Changed
~~~~~~~

- Added explicit ``python_version = "3.12"`` requirement to Pipfile.
- Updated ``certifi`` dependency.

.. _section-9:

`3.1.6.0.0 <https://github.com/cisco-en-programmability/catalystcentersdk/compare/v3.1.3.0.1...v3.1.6.0.0>`__ - 2026-02-11
--------------------------------------------------------------------------------------------------------------------------

.. _added-1:

Added
~~~~~

- Add support of Cisco Catalyst Center version (‘3.1.6.0’)
- Adds modules for v3_1_6_0
- New service for Cisco Catalyst Center 3.1.6.0’s API:

  - ``system_software_upgrade``

.. _section-10:

`3.1.3.0.1 <https://github.com/cisco-en-programmability/catalystcentersdk/compare/v3.1.3.0.0...v3.1.3.0.1>`__ - 2026-02-06
--------------------------------------------------------------------------------------------------------------------------

.. _added-2:

Added
~~~~~

- GitHub issue templates for bug reports and feature requests
- Configuration file for GitHub issues (config.yml)

.. _changed-3:

Changed
~~~~~~~

- Updated .gitignore to exclude ``.github/copilot-instructions.md``
- Renamed function ``un_claim_device`` to ``unclaim_device`` in Device
  Onboarding (PnP) module for versions 2.3.7.6.1, 2.3.7.9, and 3.1.3.0
  (backward compatibility alias maintained)
- Renamed function ``download_unmaskedraw_device_configuration_as_z_ip``
  to ``download_unmaskedraw_device_configuration_as_zip`` in
  Configuration Archive module for versions 2.3.7.9 and 3.1.3.0
  (backward compatibility alias maintained)
- Renamed function
  ``the_trend_analytics_data_for_thousand_eyes_test_results_in_the_specified_time_range``
  to
  ``get_trend_analytics_data_for_thousand_eyes_test_results_in_the_specified_time_range``
  in Applications module for version 3.1.3.0 (backward compatibility
  alias maintained)
- Renamed multiple functions in Industrial Configuration module for
  versions 2.3.7.9 and 3.1.3.0 (backward compatibility aliases
  maintained):

  - ``configure_are_p_ring_on_fabric_deployment`` to
    ``configure_rep_ring_on_fabric_deployment``
  - ``configure_are_p_ring_on_non_fabric_deployment`` to
    ``configure_rep_ring_on_non_fabric_deployment``
  - ``delete_are_p_ring_configured_in_the_fabric_deployment`` to
    ``delete_rep_ring_configured_in_the_fabric_deployment``
  - ``delete_are_p_ring_configured_in_the_non_fabric_deployment`` to
    ``delete_rep_ring_configured_in_the_non_fabric_deployment``
  - ``retrieves_the_list_of_are_p_rings`` to
    ``retrieves_the_list_of_rep_rings``
  - ``retrieves_the_count_of_are_p_rings`` to
    ``retrieves_the_count_of_rep_rings``
  - ``get_the_are_p_ring_based_on_the_ring_id`` to
    ``get_the_rep_ring_based_on_the_ring_id``

.. _section-11:

`3.1.3.0.0 <https://github.com/cisco-en-programmability/catalystcentersdk/compare/v2.3.7.9.5...v3.1.3.0.0>`__ - 2025-06-19
--------------------------------------------------------------------------------------------------------------------------

.. _added-3:

Added
~~~~~

- Add support of DNA Center versions (‘3.1.3.0’)
- Backup service.
- Industrial configuratiom service.
- Know your network service.
- Restore service.
- Wired service. ### Changed
- Update User-Agent header in RestSession
- Update requirements:

  - python = “^3.8”
  - requests = “^2.32.0”
  - readthedocs-sphinx-search = “^0.3.2”

- Renamed ``get_auditlog_summary`` to ``get_audit_log_summary``
- Renamed ``get_auditlog_parent_records`` to
  ``get_audit_log_parent_records``
- Renamed ``get_eventartifacts`` to ``get_event_artifacts``
- Renamed ``get_auditlog_records`` to ``get_audit_log_records``
- Renamed
  ``gets_the_total_network_device_interface_counts_in_the_specified_time_range_when_there_is_no_start_and_end_time_specified_returns_the_latest_interfaces_total_count``\ to
  ``gets_the_total_network_device_interface_counts``.
- Moved ``get_port_channels`` to LAN Automation service ### Removed
- The v1 alias functions were all removed. Example… if your using
  “application_v1” you must be able to change it to “application”.

.. _section-12:

`2.3.7.9.5 <https://github.com/cisco-en-programmability/catalystcentersdk/compare/v2.3.7.9.4...v2.3.7.9.5>`__ - 2025-03-05
--------------------------------------------------------------------------------------------------------------------------

Fix
~~~

- Error correction in the user_and_roles module

.. _section-13:

`2.3.7.9.4 <https://github.com/cisco-en-programmability/catalystcentersdk/compare/v2.3.7.9.3...v2.3.7.9.4>`__ - 2025-02-28
--------------------------------------------------------------------------------------------------------------------------

.. _added-4:

Added
~~~~~

- Add support of DNA Center versions (‘2.3.7.7’)

.. _section-14:

`2.3.7.9.3 <https://github.com/cisco-en-programmability/catalystcentersdk/compare/v2.3.7.9.2...v2.3.7.9.3>`__ - 2025-02-24
--------------------------------------------------------------------------------------------------------------------------

.. _fix-1:

Fix
~~~

- Correction in the request validation structures. In the
  deploy_template functions in version 1 and 2. In 2.3.5.3, 2.3.7.6 and
  2.3.7.9.

.. _section-15:

`2.3.7.9.2 <https://github.com/cisco-en-programmability/catalystcentersdk/compare/v2.3.7.9.1...v2.3.7.9.2>`__ - 2025-02-17
--------------------------------------------------------------------------------------------------------------------------

.. _fix-2:

Fix
~~~

- Fix in create_webhook_destination, update_webhook_destination,
  get_webhook_destination functions. In versions 2.3.7.6 and 2.3.7.9.

.. _added-5:

Added
~~~~~

- Cisco_IMC module added

.. _changed-4:

Changed
~~~~~~~

- Alias have been adjusted for backward compatibility
- Some functions were changed in versions 2.3.7.6 and 2.3.7.9 to handle
  files

.. _section-16:

`2.3.7.9.1 <https://github.com/cisco-en-programmability/catalystcentersdk/compare/v2.3.7.9.0...v2.3.7.9.1>`__ - 2025-01-14
--------------------------------------------------------------------------------------------------------------------------

.. _fix-3:

Fix
~~~

- Removal of -v1 from reference urls in the documentation
- Modification of validators in 2.3.7.9 and 2.3.7.6
- Fixed a bug in site_design in the uploads_floor_image function in
  versions 2.3.7.6 and 2.3.7.9

.. _section-17:

`2.3.7.9.0 <https://github.com/cisco-en-programmability/catalystcentersdk/compare/v2.3.7.6.2...v2.3.7.9.0>`__ - 2024-12-12
--------------------------------------------------------------------------------------------------------------------------

.. _added-6:

Added
~~~~~

- Add support of Catalyst Center versions (‘2.3.7.9’)
- Adds modules for v2_3_7_9

.. _section-18:

`2.3.7.6.2 <https://github.com/cisco-en-programmability/catalystcentersdk/compare/v2.3.7.6.1...v2.3.7.6.2>`__ - 2024-11-20
--------------------------------------------------------------------------------------------------------------------------

.. _added-7:

Added
~~~~~

- Add authentication_management module

.. _fix-4:

Fix
~~~

- The get_templates_details function was added because it was named
  incorrectly. There was an “s” missing from the word templates

.. _section-19:

`2.3.7.6.1 <https://github.com/cisco-en-programmability/catalystcentersdk/compare/v2.3.7.6.0...v2.3.7.6.1>`__ - 2024-11-05
--------------------------------------------------------------------------------------------------------------------------

.. _added-8:

Added
~~~~~

- Documentation for alias functions has been added

.. _changed-5:

Changed
~~~~~~~

- Documentation has been corrected
- Modification of documentation references in functions
- The user_agent structure is modified

.. _section-20:

`2.3.7.6.0 <https://github.com/cisco-en-programmability/catalystcentersdk/releases/tag/v2.3.7.6.0>`__ - 2024-10-30
------------------------------------------------------------------------------------------------------------------

.. _added-9:

Added
~~~~~

- Add support of Catalyst Center versions (‘2.3.7.6’)
- Adds modules for v2_3_7_6_1
