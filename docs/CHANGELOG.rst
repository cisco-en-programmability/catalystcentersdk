Changelog
=========

All notable changes to this project will be documented in this file.

The format is based on `Keep a
Changelog <https://keepachangelog.com/en/1.0.0/>`__, and this project
adheres to `Semantic
Versioning <https://semver.org/spec/v2.0.0.html>`__.

`Unreleased <https://github.com/cisco-en-programmability/catalystcentersdk/compare/v3.1.3.0.0...develop>`__
-----------------------------------------------------------------------------------------------------------

`3.1.3.0.0 <https://github.com/cisco-en-programmability/catalystcentersdk/compare/v2.3.7.9.5...v3.1.3.0.0>`__ - 2025-06-17
--------------------------------------------------------------------------------------------------------------------------

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

.. _section-1:

`2.3.7.9.5 <https://github.com/cisco-en-programmability/catalystcentersdk/compare/v2.3.7.9.4...v2.3.7.9.5>`__ - 2025-03-05
--------------------------------------------------------------------------------------------------------------------------

Fix
~~~

- Error correction in the user_and_roles module

.. _section-2:

`2.3.7.9.4 <https://github.com/cisco-en-programmability/catalystcentersdk/compare/v2.3.7.9.3...v2.3.7.9.4>`__ - 2025-02-28
--------------------------------------------------------------------------------------------------------------------------

.. _added-1:

Added
~~~~~

- Add support of DNA Center versions (‘2.3.7.7’)

.. _section-3:

`2.3.7.9.3 <https://github.com/cisco-en-programmability/catalystcentersdk/compare/v2.3.7.9.2...v2.3.7.9.3>`__ - 2025-02-24
--------------------------------------------------------------------------------------------------------------------------

.. _fix-1:

Fix
~~~

- Correction in the request validation structures. In the
  deploy_template functions in version 1 and 2. In 2.3.5.3, 2.3.7.6 and
  2.3.7.9.

.. _section-4:

`2.3.7.9.2 <https://github.com/cisco-en-programmability/catalystcentersdk/compare/v2.3.7.9.1...v2.3.7.9.2>`__ - 2025-02-17
--------------------------------------------------------------------------------------------------------------------------

.. _fix-2:

Fix
~~~

- Fix in create_webhook_destination, update_webhook_destination,
  get_webhook_destination functions. In versions 2.3.7.6 and 2.3.7.9.

.. _added-2:

Added
~~~~~

- Cisco_IMC module added

Changed
~~~~~~~

- Alias have been adjusted for backward compatibility
- Some functions were changed in versions 2.3.7.6 and 2.3.7.9 to handle
  files

.. _section-5:

`2.3.7.9.1 <https://github.com/cisco-en-programmability/catalystcentersdk/compare/v2.3.7.9...v2.3.7.9.1>`__ - 2025-01-14
------------------------------------------------------------------------------------------------------------------------

.. _fix-3:

Fix
~~~

- Removal of -v1 from reference urls in the documentation
- Modification of validators in 2.3.7.9 and 2.3.7.6
- Fixed a bug in site_design in the uploads_floor_image function in
  versions 2.3.7.6 and 2.3.7.9

.. _section-6:

`2.3.7.9 <https://github.com/cisco-en-programmability/catalystcentersdk/compare/v2.3.7.6.2...v2.3.7.9>`__ - 2024-12-12
----------------------------------------------------------------------------------------------------------------------

.. _added-3:

Added
~~~~~

- Add support of Catalyst Center versions (‘2.3.7.9’)
- Adds modules for v2_3_7_9

.. _section-7:

`2.3.7.6.2 <https://github.com/cisco-en-programmability/catalystcentersdk/compare/v2.3.7.6.1...v2.3.7.6.2>`__ - 2024-11-20
--------------------------------------------------------------------------------------------------------------------------

.. _added-4:

Added
~~~~~

- Add authentication_management module

.. _fix-4:

Fix
~~~

- The get_templates_details function was added because it was named
  incorrectly. There was an “s” missing from the word templates

.. _section-8:

`2.3.7.6.1 <https://github.com/cisco-en-programmability/catalystcentersdk/compare/v2.3.7.6.0...v2.3.7.6.1>`__ - 2024-11-05
--------------------------------------------------------------------------------------------------------------------------

.. _added-5:

Added
~~~~~

- Documentation for alias functions has been added

.. _changed-1:

Changed
~~~~~~~

- Documentation has been corrected
- Modification of documentation references in functions
- The user_agent structure is modified

.. _section-9:

`2.3.7.6.0 <https://github.com/cisco-en-programmability/catalystcentersdk/releases/tag/v2.3.7.6.0>`__ - 2024-10-30
------------------------------------------------------------------------------------------------------------------

.. _added-6:

Added
~~~~~

- Add support of Catalyst Center versions (‘2.3.7.6’)
- Adds modules for v2_3_7_6_1
