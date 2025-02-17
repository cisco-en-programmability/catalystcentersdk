# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
- Update requirements:
  + python = "^3.8"
  + requests = "^2.32.0"
  + readthedocs-sphinx-search = "^0.3.2"


## [2.3.7.6.0] - 2024-10-30
### Added
- Add support of Catalyst Center versions ('2.3.7.6')
- Adds modules for v2_3_7_6_1

## [2.3.7.6.1] - 2024-11-05
### Added
- Documentation for alias functions has been added.
### Modifications
- Documentation has been corrected.
- Modification of documentation references in functions.
- The user_agent structure is modified.

## [2.3.7.6.2] - 2024-11-20
### Added
- Add authentication_management module.
### Bug fix
- The get_templates_details function was added because it was named incorrectly.There was an "s" missing from the word templates.

## [2.3.7.9] - 2024-12-12
### Added
- Add support of Catalyst Center versions ('2.3.7.9')
- Adds modules for v2_3_7_9

## [2.3.7.9.1] - 2025-01-14
### Bug fix
- removal of -v1 from reference urls in the documentation
- Modification of validators in 2.3.7.9 and 2.3.7.6
- Fixed a bug in site_design in the uploads_floor_image function in versions 2.3.7.6 and 2.3.7.9.

## [2.3.7.9.2] - 2025-02-17
### Bug fix
- Alias have been adjusted for backward compatibility.
- Some functions were changed in versions 2.3.7.6 and 2.3.7.9 to handle files.
- fix in create_webhook_destination, update_webhook_destination, get_webhook_destination functions. In versions 2.3.7.6 and 2.3.7.9.

### Added
- Cisco_IMC module added
