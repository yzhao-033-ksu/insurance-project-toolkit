"""Analysis functions. Replace the starter function with your own."""
import pandas as pd


def analyze_by_age_group(df):
    """Calculate claim statistics for different age groups.

    Parameters
    ----------
    df : pandas.DataFrame
        Insurance claims data containing age and claim_amount.

    Returns
    -------
    pandas.DataFrame
        Average claim amount and number of claims for each age group.
    """
    if df.empty:
        raise ValueError("The data table is empty")

    required = ["age", "claim_amount"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required column(s): {missing}")

    if df[["age", "claim_amount"]].isna().any().any():
        raise ValueError("Age and claim amount cannot contain missing values")

    if (df["age"] < 18).any() or (df["claim_amount"] < 0).any():
        raise ValueError("Invalid age or claim amount")

    df = df.copy()

    bins = [0, 29, 44, 59, float("inf")]
    labels = ["Young", "Adult", "Middle-aged", "Senior"]

    df["age_group"] = pd.cut(
        df["age"],
        bins=bins,
        labels=labels,
        right=True
    )

    results = df.groupby("age_group", observed=False).agg(
        average_claim=("claim_amount", "mean"),
        number_of_claims=("claim_amount", "count")
    ).reset_index()

    return results


def highest_claim_group(results):
    """Find the age group with the highest average claim amount."""
    if results.empty or results["average_claim"].isna().all():
        raise ValueError("No valid age group results")

    highest = results.loc[results["average_claim"].idxmax()]

    return {
        "age_group": str(highest["age_group"]),
        "average_claim": float(highest["average_claim"])
    }


def calculate_claim_frequency(df):
    """Calculate claim frequency for each driver age group."""

    # Check that the data is not empty
    if df.empty:
        raise ValueError("The data table is empty")

    # Check that all required columns exist
    required = ["driver_age", "n_claims", "exposure_years"]

    for column in required:
        if column not in df.columns:
            raise ValueError(f"Missing required column: {column}")

    # Check for missing values
    if df[required].isna().any().any():
        raise ValueError("The data contains missing values")

    # Check for invalid values
    if ((df["driver_age"] < 18) |
        (df["n_claims"] < 0) |
        (df["exposure_years"] <= 0)).any():
        raise ValueError("Invalid insurance data")

    # Make a copy to protect the original data
    df = df.copy()

    # Divide drivers into four age groups
    bins = [0, 29, 44, 59, float("inf")]
    labels = ["Young", "Adult", "Middle-aged", "Senior"]

    df["age_group"] = pd.cut(
        df["driver_age"],
        bins=bins,
        labels=labels
    )

    # Calculate total claims and exposure for each group
    results = df.groupby("age_group", observed=False).agg(
        number_of_policies=("n_claims", "count"),
        total_claims=("n_claims", "sum"),
        total_exposure=("exposure_years", "sum")
    ).reset_index()

    # Calculate claim frequency
    results["claim_frequency"] = (
        results["total_claims"] / results["total_exposure"]
    )

    return results


def calculate_pure_premium(claim_frequency, average_claim_amount):
    """Calculate pure premium using frequency and severity."""
    if claim_frequency < 0 or average_claim_amount < 0:
        raise ValueError("Values cannot be negative")

    return claim_frequency * average_claim_amount
