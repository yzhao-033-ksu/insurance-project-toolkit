"""Analyze insurance claim amounts by age group."""

import numpy as np
import pandas as pd

from toolkit.io import validate


def summary_stats(df):
    """Calculate overall claim statistics.

    Parameters
    ----------
    df : pandas.DataFrame
        Insurance claims with age (years) and
        claim_amount (USD).

    Returns
    -------
    dict
        Number of claims, average claim (USD),
        and sample standard deviation (USD).

    Raises
    ------
    TypeError
        If the input is not a DataFrame.
    ValueError
        If data is invalid or contains fewer than two claims.
    """
    validate(df)

    if len(df) < 2:
        raise ValueError("At least two claims are required")

    amounts = df["claim_amount"]

    return {
        "number_of_claims": len(df),
        "average_claim": float(amounts.mean()),
        "std_claim": float(amounts.std(ddof=1))
    }


def analyze_by_age_group(df):
    """Calculate claim statistics by age group.

    Parameters
    ----------
    df : pandas.DataFrame
        Insurance claims with age (years) and
        claim_amount (USD).

    Returns
    -------
    pandas.DataFrame
        Age group, average claim (USD), and claim count.

    Raises
    ------
    TypeError
        If the input is not a DataFrame.
    ValueError
        If the data is invalid.
    """
    validate(df)

    bins = [-1, 25, 45, 65, 120]
    labels = ["0-25", "26-45", "46-65", "66-120"]

    data = df.copy()

    data["age_group"] = pd.cut(
        data["age"],
        bins=bins,
        labels=labels,
        right=True
    )

    results = data.groupby(
        "age_group",
        observed=True
    ).agg(
        average_claim=("claim_amount", "mean"),
        number_of_claims=("claim_amount", "count")
    ).reset_index()

    return results


def highest_claim_group(results):
    """Find the group with the highest average claim.

    Parameters
    ----------
    results : pandas.DataFrame
        Age group results with average_claim in USD.

    Returns
    -------
    dict
        Age group and highest average claim (USD).

    Raises
    ------
    TypeError
        If results is not a DataFrame.
    ValueError
        If results is empty or invalid.
    """
    if not isinstance(results, pd.DataFrame):
        raise TypeError("Results must be a DataFrame")

    if results.empty:
        raise ValueError("Results cannot be empty")

    required = ["age_group", "average_claim"]

    for column in required:
        if column not in results.columns:
            raise ValueError(f"Missing column: {column}")

    if results[required].isna().any().any():
        raise ValueError("Results contain missing values")

    if not pd.api.types.is_numeric_dtype(results["average_claim"]):
        raise ValueError("Average claim must be numeric")

    if not np.isfinite(results["average_claim"]).all():
        raise ValueError("Average claim must be finite")

    if (results["average_claim"] < 0).any():
        raise ValueError("Average claim cannot be negative")

    index = results["average_claim"].idxmax()
    highest = results.loc[index]

    return {
        "age_group": str(highest["age_group"]),
        "average_claim": float(highest["average_claim"])
    }
