Changelog
=========
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Changed
* Renamed `compute_entropy()` to `compute_shannon()`.
* Extended `compute_entropy_graph()` with parameters to select what functions to use.

### Removed
* Cleaned up `entrolib` module of unused draft functions.

## [0.4.0] - 2018.10.29
### Added
* `compute_entropy_graph()` now returns Chi-Squared graph as well as a second column. Reporting 
extended accordingly.


## [0.3.0] - 2018.09.24
### Added
* Batch directory entropy graph reporting.
* Single file report.

### Fixed
* Incorrect type for walk step CLI parameter.


## [0.2.0] - 2018.09.18
### Added
* Command line interface for directory report processing and single file entropy graph calculation.


## [0.1.0] - 2018.09.11
### Added
* Initial draft.
