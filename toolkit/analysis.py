"""Functions for analyzing insurance claim amounts."""

# Import NumPy for numerical operations.
import numpy as np

# Import pandas for data analysis.
import pandas as pd

# Import the validation function from io.py.
from toolkit.io import validate


# Function 3: Calculate overall claim statistics.
def summary_stats(df):
    """Calculate overall insurance claim statistics.

    Parameters
    ----------
    df : pandas.DataFrame
        Insurance data containing age in years
        and claim_amount in USD.

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
        If the dataset is invalid or has fewer than two claims.
    """

    # Validate the input dataset.
    validate(df)

    # Require at least two claims for sample standard deviation.
    if len(df) < 2:
        raise ValueError("At least two claims are required")

    # Select the claim amount column.
    amounts = df["claim_amount"]

    # Calculate and return overall statistics.
    return {
        "number_of_claims": len(df),
        "average_claim": float(amounts.mean()),
        "std_claim": float(amounts.std(ddof=1))
    }


# Function 4: Analyze insurance claims by age group.
def analyze_by_age_group(df):
    """Calculate average claim amounts by age group.

    Parameters
    ----------
    df : pandas.DataFrame
        Insurance data containing age in years
        and claim_amount in USD.

    Returns
    -------
    pandas.DataFrame
        Age group, average claim (USD), and number of claims.

    Raises
    ------
    TypeError
        If the input is not a DataFrame.
    ValueError
        If the dataset contains invalid values.
    """

    # Validate the input dataset.
    validate(df)

    # Define the boundaries of the age groups.
    bins = [-1, 25, 45, 65, 120]

    # Define the labels for the age groups.
    labels = ["0-25", "26-45", "46-65", "66-120"]

    # Create a copy to avoid modifying the original dataset.
    data = df.copy()

    # Assign each age to an age group.
    data["age_group"] = pd.cut(
        data["age"],
        bins=bins,
        labels=labels,
        right=True
    )

    # Group claims by age group and calculate statistics.
    results = data.groupby(
        "age_group",
        observed=True
    ).agg(
        average_claim=("claim_amount", "mean"),
        number_of_claims=("claim_amount", "count")
    ).reset_index()

    # Return the grouped results.
    return results


# Function 5: Find the age group with the highest average claim.
def highest_claim_group(results):
    """Find the age group with the highest average claim.

    Parameters
    ----------
    results : pandas.DataFrame
        Grouped results containing average_claim in USD.

    Returns
    -------
    dict
        Age group and highest average claim amount (USD).

    Raises
    ------
    TypeError
        If the input is not a DataFrame.
    ValueError
        If the results are empty or invalid.
    """

    # Check whether the input is a DataFrame.
    if not isinstance(results, pd.DataFrame):
        raise TypeError("Results must be a DataFrame")

    # Check whether the results are empty.
    if results.empty:
        raise ValueError("Results cannot be empty")

    # Define the required columns.
    required = ["age_group", "average_claim"]

    # Check whether the required columns exist.
    for column in required:
        if column not in results.columns:
            raise ValueError(f"Missing column: {column}")

    # Check for missing values.
    if results[required].isna().any().any():
        raise ValueError("Results contain missing values")

    # Check whether average claim amounts are numeric.
    if not pd.api.types.is_numeric_dtype(results["average_claim"]):
        raise ValueError("Average claim must be numeric")

    # Check whether all average claim amounts are finite.
    if not np.isfinite(results["average_claim"]).all():
        raise ValueError("Average claim must be finite")

    # Check for negative average claim amounts.
    if (results["average_claim"] < 0).any():
        raise ValueError("Average claim cannot be negative")

    # Find the row index with the highest average claim.
    index = results["average_claim"].idxmax()

    # Select the row with the highest average claim.
    highest = results.loc[index]

    # Return the highest age group and average claim.
    return {
        "age_group": str(highest["age_group"]),
        "average_claim": float(highest["average_claim"])
    }

