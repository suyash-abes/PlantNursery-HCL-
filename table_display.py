from tabulate import tabulate
from plant_operations import load_data


def show_plant_table():
    """Display all plant records in a formatted table."""
    plants = load_data()
    if plants.empty:
        print("\\nNo plant records available.")
        return

    print("\\n========== PLANT NURSERY INVENTORY ==========\\n")
    print(tabulate(
        plants.fillna("Not specified"),
        headers="keys",
        tablefmt="grid",
        showindex=False
    ))
    print(f"\\nTotal plants: {len(plants)}")
