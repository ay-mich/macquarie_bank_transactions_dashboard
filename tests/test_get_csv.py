import os
import pytest
from src.get_csv import get_csv_files


def test_get_csv_files_no_dir():
    # Pass a non-existent directory, expect None in return
    csv_files = get_csv_files("nonexistent_dir")
    assert csv_files is None


def test_get_csv_files_empty_dir(tmp_path):
    # Create an empty directory, expect None in return
    d = tmp_path / "empty"
    d.mkdir()
    csv_files = get_csv_files(str(d))
    assert csv_files is None


def test_get_csv_files_fake_csv_only(tmp_path):
    # Create a directory with only 'fake.csv', expect ['fake.csv'] in return
    d = tmp_path / "fake_only"
    d.mkdir()
    (d / "fake.csv").touch()
    csv_files = get_csv_files(str(d))
    assert csv_files == ["fake.csv"]


def test_get_csv_files_fake_csv_and_other(tmp_path):
    # Create a directory with 'fake.csv' and 'other.csv', expect ['other.csv'] in return
    d = tmp_path / "fake_and_other"
    d.mkdir()
    (d / "fake.csv").touch()
    (d / "other.csv").touch()
    csv_files = get_csv_files(str(d))
    assert csv_files == ["other.csv"]

