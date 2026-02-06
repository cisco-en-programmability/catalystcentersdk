# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [3.1.3.0.1] - 2026-02-06
### Added
- GitHub issue templates for bug reports and feature requests
- Configuration file for GitHub issues (config.yml)

### Changed
- Updated .gitignore to exclude `.github/copilot-instructions.md`
- Renamed function `un_claim_device` to `unclaim_device` in Device Onboarding (PnP) module for versions 2.3.7.6.1, 2.3.7.9, and 3.1.3.0 (backward compatibility alias maintained)
- Renamed function `download_unmaskedraw_device_configuration_as_z_ip` to `download_unmaskedraw_device_configuration_as_zip` in Configuration Archive module for versions 2.3.7.9 and 3.1.3.0 (backward compatibility alias maintained)
- Renamed function `the_trend_analytics_data_for_thousand_eyes_test_results_in_the_specified_time_range` to `get_trend_analytics_data_for_thousand_eyes_test_results_in_the_specified_time_range` in Applications module for version 3.1.3.0 (backward compatibility alias maintained)
- Renamed multiple functions in Industrial Configuration module for versions 2.3.7.9 and 3.1.3.0 (backward compatibility aliases maintained):
  + `configure_are_p_ring_on_fabric_deployment` to `configure_rep_ring_on_fabric_deployment`
  + `configure_are_p_ring_on_non_fabric_deployment` to `configure_rep_ring_on_non_fabric_deployment`
  + `delete_are_p_ring_configured_in_the_fabric_deployment` to `delete_rep_ring_configured_in_the_fabric_deployment`
  + `delete_are_p_ring_configured_in_the_non_fabric_deployment` to `delete_rep_ring_configured_in_the_non_fabric_deployment`
  + `retrieves_the_list_of_are_p_rings` to `retrieves_the_list_of_rep_rings`
  + `retrieves_the_count_of_are_p_rings` to `retrieves_the_count_of_rep_rings`
  + `get_the_are_p_ring_based_on_the_ring_id` to `get_the_rep_ring_based_on_the_ring_id`

## [3.1.3.0.0] - 2025-06-19
### Added
- Add support of DNA Center versions ('3.1.3.0')
- Backup service.
- Industrial configuratiom service.
- Know your network service.
- Restore service.
- Wired service.
### Changed
- Update User-Agent header in RestSession
- Update requirements:
  + python = "^3.8"
  + requests = "^2.32.0"
  + readthedocs-sphinx-search = "^0.3.2"
- Renamed `get_auditlog_summary` to `get_audit_log_summary`
- Renamed `get_auditlog_parent_records` to `get_audit_log_parent_records`
- Renamed `get_eventartifacts` to `get_event_artifacts`
- Renamed `get_auditlog_records` to `get_audit_log_records`
- Renamed `gets_the_total_network_device_interface_counts_in_the_specified_time_range_when_there_is_no_start_and_end_time_specified_returns_the_latest_interfaces_total_count`to `gets_the_total_network_device_interface_counts`.
- Moved `get_port_channels` to LAN Automation service
### Removed
- The v1 alias functions were all removed. Example... if your using "application_v1" you must be able to change it
to "application".

## [2.3.7.9.5] - 2025-03-05
### Fix
- Error correction in the user_and_roles module

## [2.3.7.9.4] - 2025-02-28
### Added
- Add support of DNA Center versions ('2.3.7.7')

## [2.3.7.9.3] - 2025-02-24
### Fix
- Correction in the request validation structures. In the deploy_template functions in version 1 and 2. In 2.3.5.3, 2.3.7.6 and 2.3.7.9.

## [2.3.7.9.2] - 2025-02-17
### Fix
- Fix in create_webhook_destination, update_webhook_destination, get_webhook_destination functions. In versions 2.3.7.6 and 2.3.7.9.

### Added
- Cisco_IMC module added

### Changed
- Alias have been adjusted for backward compatibility
- Some functions were changed in versions 2.3.7.6 and 2.3.7.9 to handle files

## [2.3.7.9.1] - 2025-01-14
### Fix
- Removal of -v1 from reference urls in the documentation
- Modification of validators in 2.3.7.9 and 2.3.7.6
- Fixed a bug in site_design in the uploads_floor_image function in versions 2.3.7.6 and 2.3.7.9

## [2.3.7.9.0] - 2024-12-12
### Added
- Add support of Catalyst Center versions ('2.3.7.9')
- Adds modules for v2_3_7_9

## [2.3.7.6.2] - 2024-11-20
### Added
- Add authentication_management module

### Fix
- The get_templates_details function was added because it was named incorrectly. There was an "s" missing from the word templates

## [2.3.7.6.1] - 2024-11-05
### Added
- Documentation for alias functions has been added

### Changed
- Documentation has been corrected
- Modification of documentation references in functions
- The user_agent structure is modified

## [2.3.7.6.0] - 2024-10-30
### Added
- Add support of Catalyst Center versions ('2.3.7.6')
- Adds modules for v2_3_7_6_1


[2.3.7.6.0]: https://github.com/cisco-en-programmability/catalystcentersdk/releases/tag/v2.3.7.6.0
[2.3.7.6.1]: https://github.com/cisco-en-programmability/catalystcentersdk/compare/v2.3.7.6.0...v2.3.7.6.1
[2.3.7.6.2]: https://github.com/cisco-en-programmability/catalystcentersdk/compare/v2.3.7.6.1...v2.3.7.6.2
[2.3.7.9.0]: https://github.com/cisco-en-programmability/catalystcentersdk/compare/v2.3.7.6.2...v2.3.7.9.0
[2.3.7.9.1]: https://github.com/cisco-en-programmability/catalystcentersdk/compare/v2.3.7.9.0...v2.3.7.9.1
[2.3.7.9.2]: https://github.com/cisco-en-programmability/catalystcentersdk/compare/v2.3.7.9.1...v2.3.7.9.2
[2.3.7.9.3]: https://github.com/cisco-en-programmability/catalystcentersdk/compare/v2.3.7.9.2...v2.3.7.9.3
[2.3.7.9.4]: https://github.com/cisco-en-programmability/catalystcentersdk/compare/v2.3.7.9.3...v2.3.7.9.4
[2.3.7.9.5]: https://github.com/cisco-en-programmability/catalystcentersdk/compare/v2.3.7.9.4...v2.3.7.9.5
[3.1.3.0.0]: https://github.com/cisco-en-programmability/catalystcentersdk/compare/v2.3.7.9.5...v3.1.3.0.0
[3.1.3.0.1]: https://github.com/cisco-en-programmability/catalystcentersdk/compare/v3.1.3.0.0...v3.1.3.0.1
[Unreleased]: https://github.com/cisco-en-programmability/catalystcentersdk/compare/v3.1.3.0.1...develop