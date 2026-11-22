"""Tests for loading and validating insurance claims data."""

# Import pytest for automated testing.
import pytest

# Import pandas to create test datasets.
import pandas as pd

# Import the functions we want to test.
from toolkit.io import load_data, validate


# Test 1: Check whether valid data passes validation.
def test_validate_valid_data():

    # Create a valid insurance dataset.
    df = pd.DataFrame({
        "age": [20, 40, 60],
        "claim_amount": [100, 500, 900]
    })

    # Validate the dataset.
    result = validate(df)

    # Check that the returned data matches the input.
    pd.testing.assert_frame_equal(result, df)


# Test 2: Check whether empty data is rejected.
def test_validate_empty_data():

    # Create an empty DataFrame with required columns.
    df = pd.DataFrame(columns=["age", "claim_amount"])

    # Expect a ValueError when validating empty data.
    with pytest.raises(ValueError, match="empty"):

        # Call the validation function.
        validate(df)


# Test 3: Check whether a missing column is rejected.
def test_validate_missing_column():

    # Create a dataset without claim_amount.
    df = pd.DataFrame({
        "age": [20, 40, 60]
    })

    # Expect a ValueError for the missing column.
    with pytest.raises(ValueError, match="Missing column"):

        # Validate the incomplete dataset.
        validate(df)


# Test 4: Check whether missing values are rejected.
def test_validate_missing_values():

    # Create a dataset containing a missing claim amount.
    df = pd.DataFrame({
        "age": [20, 40],
        "claim_amount": [100, None]
    })

    # Expect a ValueError for missing data.
    with pytest.raises(ValueError, match="missing values"):

        # Validate the dataset.
        validate(df)


# Test 5: Check whether negative claims are rejected.
def test_validate_negative_claim():

    # Create a dataset with a negative claim amount.
    df = pd.DataFrame({
        "age": [20, 40],
        "claim_amount": [100, -500]
    })

    # Expect a ValueError for the negative claim.
    with pytest.raises(ValueError, match="negative"):

        # Validate the dataset.
        validate(df)


# Test 6: Check whether invalid ages are rejected.
def test_validate_invalid_age():

    # Create a dataset with an age above 120.
    df = pd.DataFrame({
        "age": [20, 150],
        "claim_amount": [100, 500]
    })

    # Expect a ValueError for the invalid age.
    with pytest.raises(ValueError, match="Age"):

        # Validate the dataset.
        validate(df)


# Test 7: Check whether a CSV file loads correctly.
def test_load_data_valid_file(tmp_path):

    # Create a small insurance dataset.
    df = pd.DataFrame({
        "age": [25, 45],
        "claim_amount": [200, 600]
    })

    # Create a temporary CSV file path.
    file_path = tmp_path / "test_claims.csv"

    # Save the dataset to the temporary CSV file.
    df.to_csv(file_path, index=False)

    # Load the CSV file using our function.
    result = load_data(file_path)

    # Check that the loaded data matches the original data.
    pd.testing.assert_frame_equal(result, df)


# Test 8: Check whether a missing file raises an error.
def test_load_data_missing_file(tmp_path):

    # Define a path to a file that does not exist.
    file_path = tmp_path / "missing.csv"

    # Expect FileNotFoundError when loading the file.
    with pytest.raises(FileNotFoundError):

        # Try to load the nonexistent file.
        load_data(file_path)
