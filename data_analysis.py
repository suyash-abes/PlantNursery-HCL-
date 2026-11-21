import numpy as np
import pandas as pd

DATA_FILE = "plants_dataset.csv"


def run_numpy_analysis(df):
    """Demonstrate NumPy arrays, indexing, slicing and statistics."""
    prices = df["Price"].fillna(0).to_numpy()
    stock_sold = df[["Stock", "Sold"]].fillna(0).to_numpy()

    print("\\n--- NUMPY ANALYSIS ---")
    print("1D price array (first 10):", prices[:10])
    print("2D Stock/Sold array (first 5 rows):\\n", stock_sold[:5])
    print("First price (indexing):", prices[0])
    print("Price slice (positions 1 to 5):", prices[1:6])
    print("Sum:", np.sum(prices))
    print("Mean:", round(np.mean(prices), 2))
    print("Maximum:", np.max(prices))
    print("Minimum:", np.min(prices))
    print("Standard deviation:", round(np.std(prices), 2))


def run_pandas_analysis(df):
    """Demonstrate required Pandas operations."""
    print("\\n--- PANDAS ANALYSIS ---")
    print("\\nFirst five rows:")
    print(df.head().to_string(index=False))

    print("\\nSelected columns:")
    print(df[["Plant_Name", "Category", "Price", "Stock"]].head(10).to_string(index=False))

    print("\\nPlants with stock below 15:")
    low_stock = df[df["Stock"] < 15]
    print(low_stock[["Plant_Name", "Stock"]].to_string(index=False))

    print("\\nFive most expensive plants:")
    print(df.sort_values("Price", ascending=False)[["Plant_Name", "Price"]].head().to_string(index=False))

    print("\\nUnits sold by category:")
    print(df.groupby("Category")["Sold"].sum().sort_values(ascending=False))

    print("\\nMissing values before handling:")
    print(df.isnull().sum())

    cleaned = df.copy()
    for column in ["Supplier", "Watering_Requirement", "Sunlight_Requirement"]:
        cleaned[column] = cleaned[column].fillna("Not specified")
    print("\\nMissing values after handling:")
    print(cleaned.isnull().sum())

    print("\\nStatistical analysis:")
    print(df[["Price", "Stock", "Sold", "Revenue"]].describe().round(2).to_string())


def analyse_dataset():
    df = pd.read_csv(DATA_FILE)
    run_numpy_analysis(df)
    run_pandas_analysis(df)


def generate_summary_report():
    df = pd.read_csv(DATA_FILE)
    print("\\n========== NURSERY SUMMARY REPORT ==========")
    print("Total plant records :", len(df))
    print("Total categories    :", df["Category"].nunique())
    print("Total stock units   :", int(df["Stock"].sum()))
    print("Total units sold    :", int(df["Sold"].sum()))
    print("Total revenue       : Rs.", round(df["Revenue"].sum(), 2))
    print("Best-selling plant  :", df.loc[df["Sold"].idxmax(), "Plant_Name"])
    print("Lowest-stock plant  :", df.loc[df["Stock"].idxmin(), "Plant_Name"])
    print("Average plant price :", round(df["Price"].mean(), 2))
    print("============================================")
