# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2026-06-29

### Added
- **LWA (Login with Amazon) Authentication Support**: New v3.x credential versions for LWA-based authentication
  - `3.1` for NA (North America)
  - `3.2` for EU (Europe)
  - `3.3` for FE (Far East)
- New `VariationSummaryPrice` model for variation price data
- Python 3.13 classifier support

### Changed
- Updated `OAuth2Config` to support both Cognito (v2.x) and LWA (v3.x) endpoints
- Updated `OAuth2TokenManager` to handle LWA JSON body requests vs Cognito form-encoded requests
- Simplified all example scripts with cleaner code structure
- Improved README with installation instructions and LWA documentation

### Fixed
- Fixed merge conflict markers in README.md

## [1.0.0] - 2026-02-04

### Added
- Initial release of Amazon Creators API Python SDK
- Support for GetItems, SearchItems, GetBrowseNodes, GetVariations APIs
- Support for Feed and Report management (GetFeed, ListFeeds, GetReport, ListReports)
- OAuth2 authentication with Cognito (v2.x credential versions)
- Pydantic v2 models for all API request/response types
- Comprehensive example scripts for all API operations
- CI/CD workflows for testing and PyPI publishing
