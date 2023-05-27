import pytest
from src.conn import create_db_session
from src.get_csv import get_csv_files


@pytest.fixture
def db_objects():
    return create_db_session()


@pytest.fixture
def csv_files():
    dir_name = "import/"
    return get_csv_files(dir_name)


import pytest
from unittest.mock import patch, Mock


@pytest.fixture
def mock_env_vars(monkeypatch):
    """
    Fixture to mock environment variables.
    """
    monkeypatch.setenv("DB_USER", "user")
    monkeypatch.setenv("DB_PASS", "password")
    monkeypatch.setenv("DB_HOST", "localhost")
    monkeypatch.setenv("DB_NAME", "db")


@pytest.fixture
def mock_create_engine():
    """
    Fixture to mock SQLAlchemy's create_engine function.
    """
    with patch("sqlalchemy.create_engine") as mock:
        yield mock


@pytest.fixture
def mock_sessionmaker():
    """
    Fixture to mock SQLAlchemy's sessionmaker function.
    """
    with patch("sqlalchemy.orm.sessionmaker") as mock:
        mock.return_value = Mock()
        yield mock
