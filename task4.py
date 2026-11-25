import pandas as pd
import os

# Load dataset
df = pd.read_csv("employee_data.csv")

# Create report folder
os.makedirs("reports", exist_ok=True)

# Dataset information
total_rows = len(df)
total_columns = len(df.columns)
missing_values = df.isnull().sum().sum()
duplicates = df.duplicated().sum()

# Numeric analysis
numeric_df = df.select_dtypes(include="number")

# Generate report
report = f"""
EMPLOYEE DATA ANALYSIS REPORT

1. PROBLEM
The objective is to analyze employee data
and understand important patterns.

2. DATA
Total Rows: {total_rows}
Total Columns: {total_columns}
Missing Values: {missing_values}
Duplicate Rows: {duplicates}

3. THREE KEY INSIGHTS
"""

# Add numeric insights
for col in numeric_df.columns:
    report += f"\n- Average {col}: {numeric_df[col].mean():.2f}"
    
report += """

4. TWO RECOMMENDATIONS
- Improve data quality by handling missing values.
- Use data visualizations to support better decisions.

5. LIMITATIONS
- Results depend on the available dataset.
- Missing or incorrect values may affect analysis.
"""

# Save report
with open("reports/summary_report.txt", "w") as file:
    file.write(report)

print(report)
print("Report saved successfully!")