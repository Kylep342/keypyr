# keypyr
A Python CLI for validating Unique Constraints for SQL DBs in source CSV files

This tool is useful for checking third party (or first party) csv files
that are loaded to an RDBMS for an ETL.

## Setup & Installation
Clone the repo

In the project's root directory, run the following:
```bash
python -m venv keypyr_venv
```
To activate the venv, run:
```bash
source keypyr_venv/bin/activate
```
To install the required dependencies, run:
```bash
pip install -r requirements.txt
```
Only Postgres and MySQL connector packages are included so far

If you need your own, feel free to pip it

## Usage
`python keypyr.py -h` or `python keypyr.py --help` should get you started

## Notes
Currently, use of this package assumes the following:
  - If the csvs have headers, they are the same names as the columns in the DB
  - CSV file names are identical to DB table names (but with a '.csv' extension)
  - The JSON flag '-j' is not currently implemented

To come:
  - Integration with AWS S3
  - Processing of zip files
