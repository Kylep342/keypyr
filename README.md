# keypyr
A Python CLI for validating Unique Constraints for SQL DBs in source CSV files

# Setup & Installation
Clone the repo
In the project's root directory, run the following:
```python
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

# Notes
Currently, use of this package assumes the following:
  - If the csvs have headers, they are the same names as the columns in the DB
  - CSV file names are identical to DB table names (but with a '.csv' extension)

To come:
  - Integration with AWS S3
  - Processing of zip files
