import pandas as pd
import numpy as np

df = pd.read_csv("employee_data.csv")

print("ORIGINAL DATA")
print(df.head())

print("\nSUMMARY STATISTICS")
print(df.describe())

print("\nAVERAGE SALARY BY DEPARTMENT")
print(df.groupby("Department")["Salary"].agg(
    ["mean", "median", "min", "max", "std"]
))

print("\nEMPLOYEES BY CITY")
print(df.groupby("City")["Salary"].agg(
    ["mean", "count"]
))

print("\nCORRELATION")
numeric_df = df.select_dtypes(include=np.number)
corr = numeric_df.corr()
print(corr)

pairs = corr.unstack()
pairs = pairs[
    (pairs.index.get_level_values(0) <
     pairs.index.get_level_values(1))
]
print("\nTOP 3 CORRELATION RELATIONSHIPS")
print(pairs.abs().sort_values(ascending=False).head(3))

print("\nQ1: Total Employees:", len(df))

print("Q2: Average Salary:", df["Salary"].mean())

dept_salary = df.groupby("Department")["Salary"].mean()
print("Q3: Highest Salary Department:")
print(dept_salary.idxmax(), dept_salary.max())

print("\nQ4: Employees by City:")
print(df["City"].value_counts().head(1))

print("\nQ5: Maximum Salary:", df["Salary"].max())

budget = pd.DataFrame({
    "Department": df["Department"].dropna().unique(),
    "Budget": [0] * df["Department"].dropna().nunique()
})

merged = pd.merge(df, budget, on="Department", how="left")

print("\nMERGED DATA")
print(merged.head())

# 8. Bonus: Pivot Table
pivot = pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    columns="City",
    aggfunc="mean"
)

print("\nPIVOT TABLE")
print(pivot)

df.describe().to_csv("summary_statistics.csv")
corr.to_csv("correlation.csv")
merged.to_csv("merged_employee_data.csv", index=False)
pivot.to_csv("pivot_table.csv")

print("\nEDA COMPLETED SUCCESSFULLY!")
print("All output files saved.")