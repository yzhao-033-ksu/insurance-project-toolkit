import pandas as pd
import pytest

from toolkit.analysis import summary_stats


def test_known_answer():
    # Check the average claim amounts using known values
    df = pd.DataFrame({
        "age": [25, 28, 35, 40],
        "claim_amount": [1000, 2000, 3000, 5000]
    })

    result = analyze_by_age_group(df)

    young = result[result["age_group"] == "Young"].iloc[0]
    adult = result[result["age_group"] == "Adult"].iloc[0]

    assert young["average_claim"] == 1500
    assert young["number_of_claims"] == 2
    assert adult["average_claim"] == 4000
    assert adult["number_of_claims"] == 2


def test_tolerance():
    # Check a decimal average using a tolerance
    df = pd.DataFrame({
        "age": [25, 26],
        "claim_amount": [0.1, 0.2]
    })

    result = analyze_by_age_group(df)
    young = result[result["age_group"] == "Young"].iloc[0]

    assert young["average_claim"] == pytest.approx(0.15)


def test_invalid_input():
    # Negative claim amounts should raise an error
    df = pd.DataFrame({
        "age": [25, 35],
        "claim_amount": [1000, -500]
    })

    with pytest.raises(ValueError):
        analyze_by_age_group(df)


def test_highest_claim_group():
    # Check which age group has the highest average claim
    df = pd.DataFrame({
        "age": [25, 35, 65],
        "claim_amount": [1000, 3000, 5000]
    })

    result = analyze_by_age_group(df)
    highest = highest_claim_group(result)

    assert highest["age_group"] == "Senior"
    assert highest["average_claim"] == 5000
