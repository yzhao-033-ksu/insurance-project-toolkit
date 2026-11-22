# Insurance Claims Analysis Toolkit

## Scientific Question

How do insurance claim amounts vary across age groups, and which age group has the highest average claim amount?

## Track

Actuarial Mathematics

## Project Description

This Python toolkit analyzes insurance claim amounts across different age groups.

The toolkit can:
- Load insurance claims from a CSV file.
- Validate input data.
- Calculate overall claim statistics.
- Compare average claim amounts across age groups.
- Identify the age group with the highest average claim.

## Dataset

- Source: Synthetic data created for this project.
- License: CC0 1.0 for the original synthetic sample data.
- File: `data/sample/insurance_sample.csv`
- Number of records: 8
- Age unit: years
- Claim amount unit: USD

The dataset contains no real customer information.

## Project Structure

- `toolkit/io.py`: Data loading and validation.
- `toolkit/analysis.py`: Insurance claim analysis functions.
- `toolkit/__init__.py`: Package initialization.
- `tests/test_io.py`: Data loading and validation tests.
- `tests/test_analysis.py`: Statistical analysis tests.
- `data/sample/`: Sample dataset and chart.
- `data/raw/`: Reserved for raw datasets.
- `REPORT.md`: Final project report.

## Installation

Clone the repository using a GitHub account with access:

    git clone https://github.com/yzhao-033-ksu/insurance-project-toolkit.git
    cd insurance-project-toolkit

Install the required packages:

    python -m pip install -r requirements.txt

## Run Tests

Run all automated tests:

    python -m pytest tests/ -v

## Example Usage

Start Python from the project root directory:

    from toolkit.io import load_data
    from toolkit.analysis import summary_stats, analyze_by_age_group, highest_claim_group

    df = load_data("data/sample/insurance_sample.csv")

    stats = summary_stats(df)
    print(stats)

    results = analyze_by_age_group(df)
    print(results)

    highest = highest_claim_group(results)
    print(highest)

## Expected Results

- Number of claims: 8
- Overall average claim: $800
- Sample standard deviation: approximately $489.90
- Highest average claim group: ages 66-120
- Highest group average claim: $1,400

## Limitations

The dataset contains only eight synthetic observations.

The results do not represent real insurance populations.

The toolkit analyzes claim severity, not claim frequency per policy.

## AI Assistance

AI assistance was used to help draft and review code, tests, and documentation. The student is responsible for understanding and verifying the submitted work.

