import pytest
from pandas import DataFrame
from unittest.mock import patch

from src.data import process_data
from src.matches import matches
from main import main


@patch("src.data.process_data", return_value=DataFrame())
@patch("src.matches.matches")
def test_main(mock_matches, mock_process_data, db_objects, csv_files):
    Session, engine = db_objects

    if csv_files is not None:
        main(csv_files, Session, engine)

        mock_process_data.assert_called()
        mock_matches.assert_called()
    else:
        assert csv_files is None
