"""Tests for insurance data loading and validation."""

import pandas as pd
import pytest

from toolkit.io import load_data, validate


@pytest.fixture
def sample_data():
    """Create a small dataset for testing."""
    return pd.DataFrame({
        "age": [20, 40, 60],
        "claim_amount": [100, 200, 300]
    })


def test_validate_valid_data(sample_data):
    result = validate(sample_data)
    assert len(result) == 3


def test_validate_empty_data():
    with pytest.raises(ValueError):
        validate(pd.DataFrame())


def test_validate_missing_column():
    df = pd.DataFrame({"age": [20, 30]})

    with pytest.raises(ValueError, match="Missing column"):
        validate(df)


def test_validate_negative_claim():
    df = pd.DataFrame({
        "age": [20],
        "claim_amount": [-100]
    })

    with pytest.raises(ValueError, match="negative"):
        validate(df)


def test_validate_invalid_age():
    df = pd.DataFrame({
        "age": [150],
        "claim_amount": [100]
    })

    with pytest.raises(ValueError, match="Age"):
        validate(df)


def test_validate_missing_value():
    df = pd.DataFrame({
        "age": [20, None],
        "claim_amount": [100, 200]
    })

    with pytest.raises(ValueError, match="missing"):
        validate(df)


def test_validate_non_numeric():
    df = pd.DataFrame({
        "age": [20, 30],
        "claim_amount": ["low", "high"]
    })

    with pytest.raises(ValueError, match="numeric"):
        validate(df)


def test_load_data(tmp_path):
    path = tmp_path / "claims.csv"

    df = pd.DataFrame({
        "age": [20, 40],
        "claim_amount": [100, 200]
    })

    df.to_csv(path, index=False)

    result = load_data(path)

    # Hand calculation: 100 + 200 = 300
    assert result["claim_amount"].sum() == 300


def test_load_missing_file(tmp_path):
    path = tmp_path / "missing.csv"

    with pytest.raises(FileNotFoundError):
        load_data(path)
