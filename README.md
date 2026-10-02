# E-commerce A/B Testing & Conversion Analytics Pipeline

An automated data analytics pipeline for analyzing advertising campaign performance using **Python, PostgreSQL, SQL, and Power BI**.

The project automates data cleaning, A/B testing, statistical analysis, database loading, SQL analysis, and dashboard reporting.

## Project Workflow

```text
CSV Dataset
     ↓
Python Data Cleaning & Analysis
     ↓
A/B Testing & Statistical Analysis
     ↓
PostgreSQL Database
     ↓
SQL Analysis
     ↓
Power BI Dashboard
     ↓
Scheduled Automation
```

## Project Objectives

- Analyze conversion performance between the `ad` and `psa` test groups
- Calculate conversion rates and uplift
- Perform statistical significance testing
- Calculate confidence intervals
- Store cleaned data and analysis results in PostgreSQL
- Use SQL for additional analysis
- Visualize results using Power BI
- Automate the Python pipeline using Windows Task Scheduler

## Dataset

The project uses the **Marketing A/B Testing** dataset from Kaggle.

The dataset contains user-level advertising campaign information, including:

- User ID
- Test group
- Conversion status
- Total ads shown
- Most ads day
- Most ads hour

The dataset contains approximately **588,000 user records**.

The original CSV is not included in the repository because of its large file size.

## Technologies Used

- **Python** — Data cleaning, analysis and automation
- **Pandas** — Data manipulation
- **Statsmodels** — Statistical testing
- **SQLAlchemy** — PostgreSQL connection
- **PostgreSQL** — Data storage
- **SQL** — Data analysis and querying
- **Power BI** — Dashboard and visualization
- **Windows Task Scheduler** — Pipeline automation
- **Git & GitHub** — Version control

## Python Analysis

The Python pipeline performs the following steps:

1. Loads the CSV dataset
2. Checks for duplicate records
3. Checks for missing values
4. Removes duplicates and missing values
5. Calculates user and conversion counts by test group
6. Calculates conversion rates
7. Calculates conversion uplift
8. Performs a two-proportion z-test
9. Calculates a 95% confidence interval
10. Loads the cleaned dataset into PostgreSQL
11. Stores A/B testing results in PostgreSQL

## A/B Testing Results

Results obtained from the dataset:

| Metric | Result |
|---|---:|
| Ad Conversion Rate | 2.5547% |
| PSA Conversion Rate | 1.7854% |
| Conversion Uplift | 43.09% |
| Z-statistic | 7.3701 |
| P-value | 1.705 × 10⁻¹³ |
| 95% CI for Difference | 0.5951 to 0.9434 percentage points |

The statistical results are specific to this dataset and test setup.

## PostgreSQL

The cleaned dataset is stored in PostgreSQL in the `ab_testing` database.

Main tables:

- `testing` — cleaned user-level dataset
- `ab_test_results` — A/B testing metrics and statistical results

## SQL Analysis

SQL queries are used to analyze:

- Users by test group
- Conversion rates
- Overall conversion rate
- Day-wise conversion performance
- Hour-wise conversion performance
- Test group and day performance
- Ad exposure levels
- Test group and exposure performance
- CTE-based analysis

SQL queries are available in:

```text
sql/ab_testing_queries.sql
```

## Power BI Dashboard

The Power BI dashboard provides an interactive view of the analysis.

Dashboard includes:

- Total Users
- Total Conversions
- Overall Conversion Rate
- Conversion Uplift
- Conversion Rate by Test Group
- Conversion Rate by Day
- Users by Test Group
- Test Group slicer

### Dashboard Preview

![Power BI Dashboard](dashboard/dashboard_preview.png)

## Automation

The Python pipeline is scheduled using **Windows Task Scheduler**.

The scheduled process:

1. Runs the Python pipeline
2. Loads and cleans the dataset
3. Performs the A/B testing analysis
4. Updates the PostgreSQL tables

Power BI Desktop can then be refreshed to retrieve the updated PostgreSQL data.

## Project Structure

```text
AB-Testing-Automated-Pipeline/
│
├── data/
│   └── README.md
│
├── sql/
│   └── ab_testing_queries.sql
│
├── output/
│   └── README.md
│
├── dashboard/
│   ├── dashboard_preview.png
│   └── README.md
│
├── ab_testing_pipeline.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository and install the required Python packages:

```bash
pip install -r requirements.txt
```

Required packages:

```text
pandas
sqlalchemy
psycopg2-binary
statsmodels
```

## Running the Pipeline

Place the dataset in:

```text
data/marketing_ab.csv
```

Then run:

```bash
python ab_testing_pipeline.py
```

The script will process the dataset, perform the A/B testing analysis, and load the results into PostgreSQL.

## Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis
