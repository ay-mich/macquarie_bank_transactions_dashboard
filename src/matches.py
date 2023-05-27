import pandas as pd
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from typing import Tuple, Optional


def matches(Session, df: pd.DataFrame, filename: str) -> Optional[Tuple[int, int]]:
    """
    Compare the number of records in the DataFrame and the database.

    Parameters:
        Session (sqlalchemy.orm.sessionmaker): SQLAlchemy Session maker.
        df (pd.DataFrame): DataFrame to compare.
        filename (str): Name of the CSV file.

    Returns:
        Tuple[int, int]: Number of records in DataFrame and in DB, or None if there was an error.

    Raises:
        SQLAlchemyError: If there's an error executing the query.
    """
    if df is None:
        exit()
    else:    
        try:
            with Session() as session:
                count_query = text("SELECT COUNT(*) FROM raw_transactions")
                count_db = session.execute(count_query).scalar()
                count_csv = df.shape[0]

                if count_db != count_csv:
                    print(
                        f"Discrepancy in number of records for {filename}. CSV: {count_csv}, DB: {count_db}"
                    )
                else:
                    print(
                        f"Import of {filename} was successful. {count_csv} records were imported."
                    )
                return count_csv, count_db
        except SQLAlchemyError as e:
            print(f"Error counting records: {e}")
            return None
