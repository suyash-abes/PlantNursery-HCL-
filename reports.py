import pandas as pd

DATA_FILE = "plants_dataset.csv"
PLANT_CATEGORIES = ("Indoor", "Flowering", "Medicinal", "Succulent", "Outdoor")


def show_data_structure_examples():
    """Demonstrate list, tuple, set, dictionary and their methods."""
    df = pd.read_csv(DATA_FILE)

    plant_names = df["Plant_Name"].tolist()
    plant_names.append("Demo Plant")
    plant_names.remove("Demo Plant")
    plant_names.sort()

    unique_categories = set(df["Category"].dropna())
    first_plant = df.iloc[0].to_dict()

    print("\\n--- PYTHON DATA STRUCTURES ---")
    print("List: first five sorted plant names:", plant_names[:5])
    print("Tuple: fixed categories:", PLANT_CATEGORIES)
    print("Set: unique categories:", unique_categories)
    print("Dictionary: first plant:", first_plant)
    print("Dictionary get('Price'):", first_plant.get("Price"))
    first_plant.update({"Display_Note": "Example update"})
    print("Dictionary after update:", first_plant)


def show_category_report():
    df = pd.read_csv(DATA_FILE)
    report = df.groupby("Category").agg(
        Plant_Count=("Plant_ID", "count"),
        Average_Price=("Price", "mean"),
        Total_Units_Sold=("Sold", "sum")
    )
    print("\\n--- CATEGORY REPORT ---")
    print(report.round(2).to_string())
