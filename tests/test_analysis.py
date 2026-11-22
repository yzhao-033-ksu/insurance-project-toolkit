"""Tests for insurance claim analysis functions."""

# Import pytest for testing and approximate comparisons.
import pytest

# Import pandas to create test datasets.
import pandas as pd

# Import the analysis functions.
from toolkit.analysis import (
    summary_stats,
    analyze_by_age_group,
    highest_claim_group
)


# Test 1: Check overall statistics using known answers.
def test_summary_stats_known_values():

    # Create a dataset with easy-to-calculate values.
    df = pd.DataFrame({
        "age": [20, 30, 40],
        "claim_amount": [100, 200, 300]
    })

    # Calculate summary statistics.
    result = summary_stats(df)

    # Check the number of claims.
    assert result["number_of_claims"] == 3

    # Check the average claim amount.
    assert result["average_claim"] == pytest.approx(200)

    # Check the sample standard deviation.
    assert result["std_claim"] == pytest.approx(100)


# Test 2: Check floating-point calculations.
def test_summary_stats_floating_point():

    # Create a dataset with decimal claim amounts.
    df = pd.DataFrame({
        "age": [25, 35, 45],
        "claim_amount": [0.1, 0.2, 0.3]
    })

    # Calculate summary statistics.
    result = summary_stats(df)

    # Check the average using approximate comparison.
    assert result["average_claim"] == pytest.approx(0.2)

    # Check the sample standard deviation.
    assert result["std_claim"] == pytest.approx(0.1)


# Test 3: Check whether one claim is rejected.
def test_summary_stats_one_claim():

    # Create a dataset with only one claim.
    df = pd.DataFrame({
        "age": [30],
        "claim_amount": [500]
    })

    # Expect a ValueError because sample SD needs two values.
    with pytest.raises(ValueError, match="At least two"):

        # Try to calculate summary statistics.
        summary_stats(df)


# Test 4: Check whether empty data is rejected.
def test_summary_stats_empty_data():

    # Create an empty DataFrame.
    df = pd.DataFrame(columns=["age", "claim_amount"])

    # Expect a ValueError for empty data.
    with pytest.raises(ValueError, match="empty"):

        # Try to calculate summary statistics.
        summary_stats(df)


# Test 5: Check age-group analysis using known values.
def test_analyze_by_age_group_known_values():

    # Create a dataset with two claims in each age group.
    df = pd.DataFrame({
        "age": [20, 22, 30, 42, 50, 60, 70, 80],
        "claim_amount": [
            100, 300, 500, 700,
            900, 1100, 1300, 1500
        ]
    })

    # Calculate claim statistics by age group.
    result = analyze_by_age_group(df)

    # Define the expected average claim amounts.
    expected_averages = [200, 600, 1000, 1400]

    # Define the expected number of claims.
    expected_counts = [2, 2, 2, 2]

    # Compare actual averages with expected averages.
    assert result["average_claim"].tolist() == pytest.approx(
        expected_averages
    )

    # Compare actual claim counts with expected counts.
    assert result["number_of_claims"].tolist() == expected_counts


# Test 6: Check age-group boundary values.
def test_analyze_by_age_group_boundaries():

    # Create a dataset using the age-group boundaries.
    df = pd.DataFrame({
        "age": [0, 25, 26, 45, 46, 65, 66, 120],
        "claim_amount": [100] * 8
    })

    # Analyze the dataset.
    result = analyze_by_age_group(df)

    # Check that each group contains exactly two claims.
    assert result["number_of_claims"].tolist() == [2, 2, 2, 2]


# Test 7: Check whether the original data remains unchanged.
def test_analyze_by_age_group_no_modification():

    # Create a small insurance dataset.
    df = pd.DataFrame({
        "age": [20, 40],
        "claim_amount": [100, 500]
    })

    # Create a copy of the original data.
    original = df.copy()

    # Run the age-group analysis.
    analyze_by_age_group(df)

    # Check that the original DataFrame was not changed.
    pd.testing.assert_frame_equal(df, original)


# Test 8: Check the highest average claim group.
def test_highest_claim_group_known_values():

    # Create a DataFrame containing age-group results.
    results = pd.DataFrame({
        "age_group": ["0-25", "26-45", "46-65"],
        "average_claim": [200, 600, 1000]
    })

    # Find the group with the highest average claim.
    highest = highest_claim_group(results)

    # Check the correct age group.
    assert highest["age_group"] == "46-65"

    # Check the correct average claim amount.
    assert highest["average_claim"] == pytest.approx(1000)


# Test 9: Check whether empty results are rejected.
def test_highest_claim_group_empty():

    # Create an empty DataFrame.
    results = pd.DataFrame(
        columns=["age_group", "average_claim"]
    )

    # Expect a ValueError for empty results.
    with pytest.raises(ValueError, match="empty"):

        # Try to find the highest claim group.
        highest_claim_group(results)


# Test 10: Check whether missing columns are rejected.
def test_highest_claim_group_missing_column():

    # Create a DataFrame without average_claim.
    results = pd.DataFrame({
        "age_group": ["0-25", "26-45"]
    })

    # Expect a ValueError for the missing column.
    with pytest.raises(ValueError, match="Missing column"):

        # Try to find the highest claim group.
        highest_claim_group(results)

