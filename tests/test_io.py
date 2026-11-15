import pandas as pd
import pytest

from toolkit.io import load_data, validate


@pytest.fixture
def tiny_table():
    return pd.DataFrame({
        "claim_id": ["C001", "C002", "C003"],
        "age": [25, 40, 65],
        "claim_amount": [1000, 3000, 5000]
    })


def test_load_data(tmp_path):
    file = tmp_path / "claims.csv"
    file.write_text(
        "claim_id,age,claim_amount\n"
        "C001,25,1000\n"
        "C002,40,3000\n"
    )

    df = load_data(file)

    assert len(df) == 2
    assert "claim_amount" in df.columns


def test_load_data_missing_file():
    with pytest.raises(FileNotFoundError):
        load_data("nonexistent.csv")


def test_validate_accepts_good_table(tiny_table):
    assert validate(tiny_table) is tiny_table


def test_validate_rejects_missing_columns():
    df = pd.DataFrame({
        "claim_id": ["C001"],
        "age": [25]
    })

    with pytest.raises(ValueError):
        validate(df)


def test_validate_rejects_empty_table():
    df = pd.DataFrame(columns=["claim_id", "age", "claim_amount"])

    with pytest.raises(ValueError):
        validate(df)
