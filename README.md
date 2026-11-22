# Insurance Claims Analysis Toolkit

## Scientific Question

How do insurance claim amounts vary across age groups, and which age group has the highest average claim amount?

## Track

Actuarial Mathematics

## Project Description

This Python toolkit loads, validates, and analyzes insurance claims data.

It calculates overall claim statistics, compares average claim amounts across age groups, and identifies the group with the highest average claim amount.

## Dataset

- Source: Synthetic data created for this project.
- License: CC0 1.0 (synthetic sample data).
- File: data/sample/insurance_sample.csv
- Age unit: years.
- Claim amount unit: USD.
- Number of records: 8.

The dataset contains no real customer information.

## Project Structure

- toolkit/io.py: Data loading and validation.
- toolkit/analysis.py: Insurance claim analysis.
- tests/test_io.py: Loading and validation tests.
- tests/test_analysis.py: Analysis tests.
- data/sample/: Small dataset for testing and demonstration.
- data/raw/: Reserved for raw data, excluded from Git.
- REPORT.md: Final project report.

## Installation

Clone the private repository using an account with access:

    git clone https://github.com/yzhao-033-ksu/insurance-project-toolkit.git
    cd insurance-project-toolkit
    python -m pip install -r requirements.txt

## Run Tests

    python -m pytest -v

## Run Analysis

Start Python in the project directory and run:

    from toolkit.io import load_data
    from toolkit.analysis import summary_stats, analyze_by_age_group, highest_claim_group

    df = load_data("data/sample/insurance_sample.csv")

    print(summary_stats(df))

    results = analyze_by_age_group(df)
    print(results)

    print(highest_claim_group(results))

## Functions

1. load_data(path): Load CSV data and validate it.
2. validate(df): Check insurance data for invalid values.
3. summary_stats(df): Calculate claim count, mean, and sample standard deviation.
4. analyze_by_age_group(df): Calculate claim statistics by age group.
5. highest_claim_group(results): Identify the group with the highest average claim.

## Expected Results

- Number of claims: 8
- Overall average claim: $800
- Sample standard deviation: approximately $489.90
- Highest average claim group: ages 66-120
- Highest group average: $1,400

## Limitations

The sample contains only eight synthetic observations.

The results cannot be generalized to real insurance populations.

The toolkit analyzes claim severity, not claim frequency per policy. Frequency analysis would require policy counts or exposure data.

## AI Assistance

AI assistance was used to draft and review project code, documentation, and tests. The student is responsible for reviewing, understanding, and testing the submitted work.
