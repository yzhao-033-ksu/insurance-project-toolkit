# Insurance Claims Analysis Toolkit
## Final Project Report

### 1. Scientific Question

How do insurance claim amounts vary across age groups, and which age group has the highest average claim amount?

This project focuses on insurance claim severity, a topic related to actuarial mathematics.

### 2. Dataset

The project uses eight synthetic insurance claims created for educational purposes.

The dataset contains two variables:

- `age`: Policyholder age in years.
- `claim_amount`: Insurance claim amount in USD.

No real customer information is used.

### 3. Methods

The toolkit contains five public functions in two Python modules.

The `io.py` module loads CSV files and validates insurance data.

The `analysis.py` module calculates overall claim statistics, compares claim amounts across four age groups, and identifies the group with the highest average claim amount.

Pandas is used for data analysis, NumPy is used for numerical validation, and pytest is used for automated testing.

### 4. Results

The dataset contains eight claims with a total claim amount of $6,400.

The overall average claim amount is $800.

The sample standard deviation is approximately $489.90.

| Age Group | Average Claim (USD) | Number of Claims |
|---|---:|---:|
| 0-25 | 200 | 2 |
| 26-45 | 600 | 2 |
| 46-65 | 1000 | 2 |
| 66-120 | 1400 | 2 |

The 66-120 age group has the highest average claim amount at $1,400.

### 5. Testing

The project includes 18 automated pytest tests.

The tests cover valid data, invalid inputs, known-answer calculations, floating-point comparisons, and age-group boundaries.

The final test results will be confirmed before submission.

### 6. Limitations

The dataset is small and synthetic.

The results cannot be generalized to real insurance populations.

The project analyzes claim severity but does not estimate claim frequency because policy exposure data are unavailable.

### 7. Future Improvements

Future improvements could include larger insurance datasets, claim frequency calculations, and additional statistical models.

### 8. Contributions

Yanming Zhao: Project implementation, data validation, statistical analysis, automated testing, documentation, and demonstration, subject to actual completed work and instructor approval for an individual project.

AI assistance was used to help draft and review project materials.
