from typing import List
import sys

from src.conn import create_db_session
from src.data import process_data
from src.get_csv import get_csv_files
from src.matches import matches


def main(csv_files: List[str], Session, engine):
    """
    Main function to process all CSV files, load data and match record counts.

    Parameters:
        csv_files (list): List of CSV filenames.
        Session (sqlalchemy.orm.sessionmaker): SQLAlchemy Session maker.
        engine (sqlalchemy.engine.Engine): SQLAlchemy Engine.
    """
    for filename in csv_files:
        try:
            df = process_data(dir_name, filename, engine)
            if df is None:
                print(f"Error processing file {filename}. Exiting.")
                exit()
            else:
                matches(Session, df, filename)
        except Exception as e:
            print(f"Error processing file {filename}: {e}")


if __name__ == "__main__":
    Session, engine = create_db_session()
    dir_name = "import/"

    csv_files = get_csv_files(dir_name)
    if csv_files is None:
        print("No valid CSV files found. Exiting.")
        sys.exit(1)

    main(csv_files, Session, engine)
