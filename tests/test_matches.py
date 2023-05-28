import pandas as pd
import pytest
from sqlalchemy import text
from unittest.mock import Mock, patch
from src.matches import matches


class MockSession:
    """Mock SQLAlchemy Session"""

    def __init__(self):
        self.execute = Mock()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def test_matches():
    # Create a Mock Session
    mock_session = MockSession()
    mock_session.execute.return_value.scalar.return_value = 100

    # Mock SQLAlchemy text function
    with patch(
        "src.matches.text", return_value="SELECT COUNT(*) FROM raw_transactions"
    ) as mock_text:
        # Create a DataFrame of length 100
        df = pd.DataFrame(range(100), columns=["value"])

        # Mock sessionmaker to return a callable that returns our mock session
        with patch(
            "sqlalchemy.orm.sessionmaker", return_value=lambda: mock_session
        ) as MockedSession:
            # Call matches function
            count_csv, count_db = matches(MockedSession, df, "test.csv")

            # Assert that the execute method was called once with the right query
            mock_text.assert_called_once_with("SELECT COUNT(*) FROM raw_transactions")
            mock_session.execute.assert_called_once_with(mock_text.return_value)

            # Assert that the scalar() method was called once
            mock_session.execute.return_value.scalar.assert_called_once()

            # Assert the counts returned
            assert count_csv == 100
            assert count_db == 100
