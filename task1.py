import pandas as pd
import numpy as np

df = pd.read_csv("employee_data.csv")

print("Original Data:")
print(df)

print("\nBefore Cleaning")
print("Rows:", len(df))
print("Missing Values:", df.isnull().sum().sum())
print("Duplicates:", df.duplicated().sum())

df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")
df["Joining_Date"] = pd.to_datetime(
    df["Joining_Date"], errors="coerce"
)

# 4. Standardize text columns
for col in ["Name", "Department", "City"]:
    df[col] = df[col].str.strip().str.title()

# 5. Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].median())

df["City"] = df["City"].fillna(df["City"].mode()[0])

# 6. Remove duplicates
df = df.drop_duplicates()

# 7. Detect outliers using IQR
for col in ["Age", "Salary"]:

    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df[col + "_outlier"] = (
        (df[col] < lower) | (df[col] > upper)
    )

    print("\nOutliers in", col, ":",
          df[col + "_outlier"].sum())

# 8. After cleaning summary
print("\nAfter Cleaning")
print("Rows:", len(df))
print("Missing Values:", df.isnull().sum().sum())
print("Duplicates:", df.duplicated().sum())

# 9. Create summary table
summary = pd.DataFrame({
    "Metric": ["Rows", "Missing Values", "Duplicates"],
    "Before": [10, 2, 1],
    "After": [
        len(df),
        df.isnull().sum().sum(),
        df.duplicated().sum()
    ]
})

print("\nBefore and After Summary")
print(summary)

# 10. Save cleaned CSV
df.to_csv("clean_data.csv", index=False)

summary.to_csv("cleaning_summary.csv", index=False)

print("\nData Cleaning Completed Successfully!")
print("Saved: clean_data.csv")
print("Saved: cleaning_summary.csv")