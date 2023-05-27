from src.conn import create_db_session
from sqlalchemy.exc import SQLAlchemyError

def test_create_db_session_missing_env(mock_env_vars, monkeypatch):
    """
    Test that function returns None, None when an environment variable is missing.
    """
    monkeypatch.delenv('DB_USER')
    session, engine = create_db_session()
    assert session is None
    assert engine is None

def test_create_db_session_sqlalchemy_error(mock_env_vars, mock_create_engine):
    """
    Test that function returns None, None when SQLAlchemy raises an error.
    """
    mock_create_engine.side_effect = SQLAlchemyError("Engine creation error")
    session, engine = create_db_session()
    assert session is not None
    assert engine is not None

def test_create_db_session_success(mock_env_vars, mock_create_engine, mock_sessionmaker):
    """
    Test that function returns Session, Engine on success.
    """
    session, engine = create_db_session()
    assert session is not None
    assert engine is not None
