import os
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd
from pandas.errors import ParserError


def load_csv(dir_name: str, filename: str) -> pd.DataFrame | None:
    """
    Load a CSV file as a pandas DataFrame.

    Parameters:
        dir_name (str): Directory path to the CSV file.
        filename (str): Name of the CSV file.

    Returns:
        df (pd.DataFrame): Loaded DataFrame.

    Raises:
        FileNotFoundError: If the CSV file does not exist.
        ParserError: If there is an error in parsing the CSV file.
    """
    # Construct full file path
    file_path = os.path.join(dir_name, filename)

    # Load CSV file
    try:
        df = pd.read_csv(file_path, dayfirst=True)
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return None
    except ParserError:
        print(f"Error: Could not parse the CSV file {filename}.")
        return None

    return df


def columns_exist(df: pd.DataFrame, filename: str) -> bool:
    """
    Check if required columns exist in the DataFrame.

    Parameters:
        df (pd.DataFrame): DataFrame to check.
        filename (str): Name of the CSV file.

    Returns:
        bool: True if all required columns exist, False otherwise.
    """
    # Check if required columns exist
    required_columns = [
        "Transaction Date",
        "Details",
        "Account",
        "Category",
        "Subcategory",
        "Notes",
        "Debit",
        "Credit",
        "Balance",
        "Original Description",
    ]
    if not all(c in df.columns for c in required_columns):
        print(
            f"Error: CSV file {filename} does not contain all required columns. Skipping this file."
        )
        return False
    else:
        return True


def write_data(df: pd.DataFrame, engine) -> bool:
    """
    Write DataFrame to a PostgreSQL table.

    Parameters:
        df (pd.DataFrame): DataFrame to write.
        engine (sqlalchemy.Engine): SQLAlchemy Engine instance.

    Returns:
        bool: True if write was successful, False otherwise.

    Raises:
        SQLAlchemyError: If there is an error in writing to the database.
    """
    # Write data to PostgreSQL
    try:
        df.to_sql("raw_transactions", engine, if_exists="replace", index=False)
    except SQLAlchemyError as e:
        print(f"Error: Failed to write to PostgreSQL: {e}")
        return False

    return True


def process_data(dir_name, filename, engine):
    """
    Process the data from CSV file and load into PostgreSQL.

    Parameters:
        dir_name (str): Directory path to the CSV file.
        filename (str): Name of the CSV file.
        engine (sqlalchemy.Engine): SQLAlchemy Engine instance.

    Returns:
        df (pd.DataFrame): Processed DataFrame, or None if there were errors.
    """
    df = load_csv(dir_name, filename)
    if df is None:
        return None

    if not columns_exist(df, filename):
        return None

    if not write_data(df, engine):
        return None

    return df
