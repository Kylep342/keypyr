# keypyr
A Python CLI for validating Unique Constraints for SQL DBs in source CSV files


Currently, use of this package assumes the following:
  - If the csvs have headers, they are the same names as the columns in the DB
  - CSV file names are identical to DB table names (but with a '.csv' extension)

To come:
  - Integration with AWS S3
  - Processing of zip files
