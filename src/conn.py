import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError


def create_db_session():
    """
    Create a session for the PostgreSQL database.

    Retrieves the database parameters from environment variables and
    creates a session to interact with the database.

    Returns:
        session: a SQLAlchemy Session instance for the database.
        engine: a SQLAlchemy Engine instance for the database.

    Raises:
        SQLAlchemyError: An error occurred creating the engine or session.
    """
    # Ensure required environment variables are set
    try:
        db_user = os.getenv("DB_USER")
        db_pass = os.getenv("DB_PASS")
        db_host = os.getenv("DB_HOST")
        db_name = os.getenv("DB_NAME")

        if not all([db_user, db_pass, db_host, db_name]):
            raise ValueError("Missing required environment variable.")
    except ValueError as e:
        print(f"Error: {e}")
        return None, None

    try:
        # Create a database connection
        engine = create_engine(
            f"postgresql://{db_user}:{db_pass}@{db_host}:5432/{db_name}"
        )

        # Create a Session
        Session = sessionmaker(bind=engine)

    except SQLAlchemyError as e:
        print(f"Error occurred while creating engine: {e}")
        return None, None

    return Session, engine
