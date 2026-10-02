import pandas as pd
from sqlalchemy import create_engine
from statsmodels.stats.proportion import (
    proportions_ztest,
    confint_proportions_2indep
)
print("A/B Testing Automation Started")
df = pd.read_csv("D:\AB testing project\data\marketing_AB.csv")
print("Data loaded successfully")
print("Rows:", len(df))
print("Columns:", len(df.columns))

# Check for duplicates
duplicates = df.duplicated().sum()
print("Duplicate rows:", duplicates)

# Check for missing values
missing_values = df.isnull().sum().sum()
print("Missing values:", missing_values)

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing values
df = df.dropna()

print("Data cleaning completed")
print("Rows after cleaning:", len(df))

# Calculate A/B test summary
summary = df.groupby("test group").agg(
    total_users=("converted", "count"),
    conversions=("converted", "sum")
).reset_index()

print("\nA/B Test Summary:")
print(summary)

# Calculate conversion rate
summary["conversion_rate"] = (
    summary["conversions"] / summary["total_users"] * 100
)

print("\nConversion Rates:")
print(summary)

# Calculate conversion uplift
ad_rate = summary.loc[
    summary["test group"] == "ad", "conversion_rate"
].iloc[0]

psa_rate = summary.loc[
    summary["test group"] == "psa", "conversion_rate"
].iloc[0]

uplift = ((ad_rate - psa_rate) / psa_rate) * 100

print("\nConversion Uplift:", uplift, "%")

# Run A/B statistical test
conversions = summary["conversions"].tolist()
users = summary["total_users"].tolist()

z_stat, p_value = proportions_ztest(
    conversions,
    users
)

print("\nStatistical Test:")
print("Z-statistic:", z_stat)
print("P-value:", p_value)

# Calculate 95% confidence interval
ad_conversions = summary.loc[
    summary["test group"] == "ad", "conversions"
].iloc[0]

ad_users = summary.loc[
    summary["test group"] == "ad", "total_users"
].iloc[0]

psa_conversions = summary.loc[
    summary["test group"] == "psa", "conversions"
].iloc[0]

psa_users = summary.loc[
    summary["test group"] == "psa", "total_users"
].iloc[0]

ci_low, ci_high = confint_proportions_2indep(
    ad_conversions,
    ad_users,
    psa_conversions,
    psa_users,
    method="wald"
)

print("\n95% Confidence Interval:")
print("Lower:", ci_low)
print("Upper:", ci_high)
print("Percentage points:", ci_low * 100, "to", ci_high * 100)

# Create final A/B test results
results = pd.DataFrame({
    "metric": [
        "Ad Conversion Rate",
        "PSA Conversion Rate",
        "Conversion Uplift",
        "Z-statistic",
        "P-value",
        "CI Lower",
        "CI Upper"
    ],
    "value": [
        ad_rate,
        psa_rate,
        uplift,
        z_stat,
        p_value,
        ci_low * 100,
        ci_high * 100
    ]
})

print("\nFinal A/B Test Results:")
print(results)

# Connect to PostgreSQL
username = "postgres"
password = ""
host = "localhost"
port = "5432"
database = "ab_testing"

engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
)

print("\nConnected to PostgreSQL")

# Load cleaned data into PostgreSQL
df.to_sql(
    "testing",
    engine,
    if_exists="replace",
    index=False
)

print("Cleaned data loaded into PostgreSQL")

# Save A/B test results to PostgreSQL
results.to_sql(
    "ab_test_results",
    engine,
    if_exists="replace",
    index=False
)

print("A/B test results loaded into PostgreSQL")