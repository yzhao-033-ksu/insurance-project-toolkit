"""Tests for insurance claims analysis."""

import pandas as pd
import pytest

from toolkit.analysis import (
    summary_stats,
    analyze_by_age_group,
    highest_claim_group
)


@pytest.fixture
def sample_data():
    """Create a small insurance claims table by hand."""
    return pd.DataFrame({
        "age": [20, 22, 30, 42, 50, 60, 70, 80],
        "claim_amount": [100, 300, 500, 700, 900, 1100, 1300, 1500]
    })


def test_summary_count(sample_data):
    result = summary_stats(sample_data)

    # Known answer: there are 8 claims
    assert result["number_of_claims"] == 8


def test_summary_mean(sample_data):
    result = summary_stats(sample_data)

    # Known answer: 6400 / 8 = 800
    assert result["average_claim"] == 800


def test_summary_std(sample_data):
    result = summary_stats(sample_data)

    # Sum of squared deviations = 1,680,000
    # Sample variance = 1,680,000 / 7 = 240,000
    # Sample SD = sqrt(240000) = 489.89794856
    assert result["std_claim"] == pytest.approx(
        489.89794856, rel=1e-8
    )


def test_age_group_mean(sample_data):
    result = analyze_by_age_group(sample_data)

    # Known answer: (100 + 300) / 2 = 200
    assert result["average_claim"].iloc[0] == 200


def test_age_group_tolerance():
    df = pd.DataFrame({
        "age": [20, 22, 30, 42],
        "claim_amount": [0.1, 0.2, 0.2, 0.4]
    })

    result = analyze_by_age_group(df)

    # Known answer: (0.2 + 0.4) / 2 = 0.3
    assert result["average_claim"].iloc[1] == pytest.approx(
        0.3, abs=1e-12
    )


def test_highest_group(sample_data):
    results = analyze_by_age_group(sample_data)
    highest = highest_claim_group(results)

    # Known answer: (1300 + 1500) / 2 = 1400
    assert highest["age_group"] == "66-120"
    assert highest["average_claim"] == 1400


def test_summary_one_claim():
    df = pd.DataFrame({
        "age": [20],
        "claim_amount": [100]
    })

    with pytest.raises(ValueError):
        summary_stats(df)


def test_highest_empty():
    with pytest.raises(ValueError):
        highest_claim_group(pd.DataFrame())


def test_highest_missing_column():
    df = pd.DataFrame({
        "age_group": ["0-25"]
    })

    with pytest.raises(ValueError):
        highest_claim_group(df)
