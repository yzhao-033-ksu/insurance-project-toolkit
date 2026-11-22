# Insurance Claims Analysis Toolkit
## Final Project Report

### 1. Scientific Question

How do insurance claim amounts vary across age groups, and which age group has the highest average claim amount?

This project focuses on insurance claim severity, which is related to actuarial mathematics.

### 2. Data

The dataset contains eight synthetic insurance claims.

Each record has two variables:
- age: Policyholder age in years.
- claim_amount: Insurance claim amount in USD.

The data were created for educational purposes and contain no real customer information.

### 3. Methods

The toolkit contains five public functions in two Python modules.

The io.py module loads CSV files and validates input data.

The analysis.py module calculates overall claim statistics, compares claims across four age groups, and identifies the group with the highest average claim amount.

The project uses pandas for data analysis and pytest for automated testing.

### 4. Results

The dataset contains eight claims with a total claim amount of $6,400.

The overall average claim amount is $800.

The sample standard deviation is approximately $489.90.

Average claims by age group:

| Age Group | Average Claim (USD) | Claim Count |
|---|---:|---:|
| 0-25 | 200 | 2 |
| 26-45 | 600 | 2 |
| 46-65 | 1000 | 2 |
| 66-120 | 1400 | 2 |

The 66-120 age group has the highest average claim amount at $1,400.

### 5. Testing and Functionality

The project contains 18 pytest tests covering all five public functions.

The tests include known-answer calculations, floating-point tolerance tests, invalid-input tests, and small manually created datasets.

The toolkit can load CSV files, reject invalid data, calculate statistics, and compare age groups.

The final test results must be verified before submission.

### 6. Limitations

The dataset is small and synthetic.

The results cannot be used to estimate real insurance risk.

The project analyzes claim severity but cannot estimate claim frequency per policy because policy exposure data are unavailable.

The age groups were selected for demonstration purposes.

### 7. Future Improvements

Future improvements could include a larger public insurance dataset, policy exposure information, claim frequency calculations, and severity distribution fitting.

### 8. Individual Contributions

| Contributor | Work |
|---|---|
| Yanming Zhao | Project implementation, validation, analysis, testing, documentation, and demonstration, subject to actual completed work |

This is an individual project, subject to instructor approval.

AI assistance was used for drafting and code review. All submitted work must be reviewed and understood by the student.
