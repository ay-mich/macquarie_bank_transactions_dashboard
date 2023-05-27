import os
import pandas as pd
import pytest
from sqlalchemy import create_engine
from unittest.mock import patch, MagicMock
from sqlalchemy.exc import SQLAlchemyError
from pandas.errors import ParserError
from src.data import load_csv, columns_exist, write_data, process_data

@pytest.fixture
def mock_df():
    return pd.DataFrame({
        "Transaction Date": ["2021-01-01"],
        "Details": ["Test"],
        "Account": ["Account1"],
        "Category": ["Category1"],
        "Subcategory": ["Subcategory1"],
        "Notes": ["Notes"],
        "Debit": [100],
        "Credit": [0],
        "Balance": [100],
        "Original Description": ["Test"],
    })

@pytest.fixture
def mock_engine():
    return create_engine('sqlite://')

def test_load_csv_file_not_found():
    with patch('os.path.join', return_value='nonexistent.csv'), \
            patch('pandas.read_csv') as mock_read_csv:
        mock_read_csv.side_effect = FileNotFoundError
        df = load_csv('dir', 'nonexistent.csv')
        assert df is None

def test_load_csv_parser_error():
    with patch('os.path.join', return_value='bad.csv'), \
            patch('pandas.read_csv') as mock_read_csv:
        mock_read_csv.side_effect = ParserError
        df = load_csv('dir', 'bad.csv')
        assert df is None

def test_columns_exist(mock_df):
    assert columns_exist(mock_df, 'test.csv') is True

def test_columns_exist_missing_column(mock_df):
    mock_df.drop(columns=["Original Description"], inplace=True)
    assert columns_exist(mock_df, 'test.csv') is False

def test_write_data_sqlalchemy_error(mock_df, mock_engine):
    with patch.object(mock_df, 'to_sql', side_effect=SQLAlchemyError):
        success = write_data(mock_df, mock_engine)
        assert success is False

def test_process_data_load_csv_error():
    with patch('src.data.load_csv', return_value=None):
        df = process_data('dir', 'bad.csv', 'engine')
        assert df is None

def test_process_data_columns_exist_error(mock_df, mock_engine):
    with patch('src.data.load_csv', return_value=mock_df), \
            patch('src.data.columns_exist', return_value=False):
        df = process_data('dir', 'bad.csv', mock_engine)
        assert df is None

def test_process_data_write_data_error(mock_df, mock_engine):
    with patch('src.data.load_csv', return_value=mock_df), \
            patch('src.data.columns_exist', return_value=True), \
            patch('src.data.write_data', return_value=False):
        df = process_data('dir', 'bad.csv', mock_engine)
        assert df is None
