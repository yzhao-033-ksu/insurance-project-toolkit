"""Load and validate insurance claims data."""

import pandas as pd

REQUIRED_COLUMNS = ["age", "claim_amount"]


def validate(df):
    """Validate insurance claims data.

    Parameters
    ----------
    df : pandas.DataFrame
        Data containing age in years and claim_amount in USD.

    Returns
    -------
    pandas.DataFrame
        The validated insurance claims data.

    Raises
    ------
    TypeError
        If input is not a pandas DataFrame.
    ValueError
        If data is empty or contains invalid values.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a DataFrame")

    if df.empty:
        raise ValueError("The dataset is empty")

    for column in REQUIRED_COLUMNS:
        if column not in df.columns:
            raise ValueError(f"Missing column: {column}")

    if df[REQUIRED_COLUMNS].isna().any().any():
        raise ValueError("Data contains missing values")

    for column in REQUIRED_COLUMNS:
        if not pd.api.types.is_numeric_dtype(df[column]):
            raise ValueError(f"{column} must be numeric")

    if not df["age"].between(0, 120).all():
        raise ValueError("Age must be between 0 and 120")

    if (df["claim_amount"] < 0).any():
        raise ValueError("Claim amount cannot be negative")

    return df


def load_data(path):
    """Load and validate a CSV file.

    Parameters
    ----------
    path : str or pathlib.Path
        Location of a CSV file containing age in years
        and claim_amount in USD.

    Returns
    -------
    pandas.DataFrame
        Validated insurance claims data.

    Raises
    ------
    FileNotFoundError
        If the CSV file does not exist.
    ValueError
        If the file is empty or contains invalid data.
    """
    try:
        df = pd.read_csv(path)
    except pd.errors.EmptyDataError as error:
        raise ValueError("The CSV file is empty") from error

    return validate(df)
