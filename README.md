# Entro.py

Entro.py is a small script and function library for conducting different entropy analyses and randomness checks.

## Installation

To install run `pip3 install entro-py`.

## Library Functions Overview

The following functions are provided by the library:

* `compute_shannon` - calculates Shannon entropy value for a given byte array.
* `compute_monte_carlo_pi` - calculates Monte Carlo Pi approximation for a given byte array.
* `get_pi_deviation` - returns an absolute percentage of difference between the provided Pi value and canonic.
* `compute_chi_squared` - calculate Chi-Squared value for a given byte array.
* `compute_arithmetic_mean` - calculates arithmetic mean value for a given byte array. In a truly random data blob the result of arithmetic mean should lay around value of 127.5.
* `compute_entropy_graph` - calculates entropy graph values with different algorithms and configurable step.

## Reporting Class Overview

The `report` class provides functionality to print out file entropy statistics to standard output or a file.

* `process_directory_report` - creates an entropy report for a list of files in a directory and saves it to a CSV spreadsheet.
* `process_directory_graphs` - calculates entropy oscillations for every file in a passed directory and writes separate graph reports into CSV spreadsheets named <in_path>/<filename>.csv.
* `write_file_report` - creates an entropy report for a single file and saves it in a CSV spreadsheet.
* `write_file_graph` - calculates entropy oscillations for a file and writes it to CSV spreadsheet.
