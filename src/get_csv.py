import os
from typing import List, Optional


def get_csv_files(dir_name: str) -> Optional[List[str]]:
    """
    Get the list of CSV files in the provided directory.

    If 'fake.csv' is the only CSV file, it is returned. If 'fake.csv' and
    another CSV file exist, the other file is returned. If no CSV files exist,
    return None.

    Parameters:
        dir_name (str): Directory path where CSV files are stored.

    Returns:
        list: List containing the relevant CSV file(s), or None if no valid CSV files found.

    Raises:
        FileNotFoundError: If the directory does not exist.
    """
    # Ensure directory exists
    if not os.path.isdir(dir_name):
        print(f"Error: Directory {dir_name} does not exist.")
        return None

    # Get list of all CSV files in the directory
    csv_files = [f for f in os.listdir(dir_name) if f.endswith(".csv")]

    # Decision logic based on the files found
    if "fake.csv" in csv_files and len(csv_files) == 2:
        csv_files.remove("fake.csv")
    elif "fake.csv" in csv_files and len(csv_files) == 1:
        csv_files = ["fake.csv"]
    else:
        print("Error: No valid CSV files found.")
        return None

    return csv_files
