"""Functions for loading and validating insurance claims data."""

# Import pandas for working with tables and CSV files.
import pandas as pd

# Define the columns required in the insurance dataset.
REQUIRED_COLUMNS = ["age", "claim_amount"]


# Function 1: Validate insurance claims data.
def validate(df):
    """Validate an insurance claims dataset.

    Parameters
    ----------
    df : pandas.DataFrame
        Insurance data containing age in years
        and claim_amount in USD.

    Returns
    -------
    pandas.DataFrame
        The validated insurance claims dataset.

    Raises
    ------
    TypeError
        If the input is not a pandas DataFrame.
    ValueError
        If the data is empty or contains invalid values.
    """

    # Check whether the input is a pandas DataFrame.
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a DataFrame")

    # Check whether the dataset is empty.
    if df.empty:
        raise ValueError("The dataset is empty")

    # Check whether all required columns exist.
    for column in REQUIRED_COLUMNS:
        if column not in df.columns:
            raise ValueError(f"Missing column: {column}")

    # Check for missing values in the required columns.
    if df[REQUIRED_COLUMNS].isna().any().any():
        raise ValueError("Data contains missing values")

    # Check whether the required columns contain numeric data.
    for column in REQUIRED_COLUMNS:
        if not pd.api.types.is_numeric_dtype(df[column]):
            raise ValueError(f"{column} must be numeric")

    # Check whether all ages are between 0 and 120.
    if not df["age"].between(0, 120).all():
        raise ValueError("Age must be between 0 and 120")

    # Check whether any claim amount is negative.
    if (df["claim_amount"] < 0).any():
        raise ValueError("Claim amount cannot be negative")

    # Return the dataset if all checks are passed.
    return df


# Function 2: Load insurance claims data from a CSV file.
def load_data(path):
    """Load and validate an insurance claims CSV file.

    Parameters
    ----------
    path : str or pathlib.Path
        Path to a CSV file containing age in years
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
        If the CSV file is empty or contains invalid data.
    """

    # Try to read the CSV file.
    try:
        df = pd.read_csv(path)

    # Handle a completely empty CSV file.
    except pd.errors.EmptyDataError as error:
        raise ValueError("The CSV file is empty") from error

    # Validate the dataset and return it.
    return validate(df)
