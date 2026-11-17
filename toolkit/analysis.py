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
