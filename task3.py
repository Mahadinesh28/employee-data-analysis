import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv("employee_data.csv")

print(df.head())

os.makedirs("reports/figures", exist_ok=True)

numeric = df.select_dtypes(include="number").columns
categorical = df.select_dtypes(include="object").columns

sns.set_style("whitegrid")

if len(categorical) > 0:
    plt.figure(figsize=(8, 5))
    df[categorical[0]].value_counts().head(10).plot(
        kind="bar", color="skyblue"
    )
    plt.title("Bar Chart")
    plt.xlabel(categorical[0])
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("reports/figures/bar_chart.png")
    plt.show()

if len(numeric) > 0:
    plt.figure(figsize=(8, 5))
    plt.hist(df[numeric[0]].dropna(), bins=10,
             color="orange", edgecolor="black")
    plt.title("Histogram")
    plt.xlabel(numeric[0])
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("reports/figures/histogram.png")
    plt.show()

if len(numeric) >= 2:
    plt.figure(figsize=(8, 5))
    plt.scatter(df[numeric[0]], df[numeric[1]],
                color="green", label="Employees")
    plt.title("Scatter Plot")
    plt.xlabel(numeric[0])
    plt.ylabel(numeric[1])
    plt.legend()
    plt.tight_layout()
    plt.savefig("reports/figures/scatter_plot.png")
    plt.show()

if len(numeric) > 0:
    plt.figure(figsize=(8, 5))
    values = df[numeric[0]].dropna().sort_values().reset_index(drop=True)
    plt.plot(values, color="red", label=numeric[0])
    plt.title("Line Chart")
    plt.xlabel("Index")
    plt.ylabel(numeric[0])
    plt.legend()
    plt.tight_layout()
    plt.savefig("reports/figures/line_chart.png")
    plt.show()
    
if len(numeric) >= 2:
    plt.figure(figsize=(8, 5))
    sns.heatmap(df[numeric].corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("reports/figures/heatmap.png")
    plt.show()

print("All 5 visualizations completed!")
print("Charts saved in reports/figures/")