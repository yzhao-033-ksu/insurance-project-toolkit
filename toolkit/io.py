"""Load and validate the project's data."""

from pathlib import Path
import pandas as pd

REQUIRED_COLUMNS = ["claim_id", "age", "claim_amount"]


def load_data(path):
    """Load a CSV file into a DataFrame."""
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {path}")

    return pd.read_csv(path)


def validate(df, required=REQUIRED_COLUMNS):
    """Check that the DataFrame has the required columns."""
    if df.empty:
        raise ValueError("The data table is empty")

    missing = [c for c in required if c not in df.columns]

    if missing:
        raise ValueError(f"Missing required column(s): {missing}")

    return df
