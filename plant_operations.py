import pandas as pd

DATA_FILE = "plants_dataset.csv"


def load_data():
    """Read the nursery dataset from the CSV file."""
    return pd.read_csv(DATA_FILE)


def save_data(df):
    """Save the current DataFrame to the CSV file."""
    df.to_csv(DATA_FILE, index=False)


def display_plants():
    """Display all plant records in a simple format."""
    df = load_data()
    print(df.fillna("Not specified").to_string(index=False))


def add_plant():
    df = load_data()
    try:
        plant_id = int(input("Enter new Plant ID: "))
        if plant_id in df["Plant_ID"].values:
            print("That Plant ID already exists.")
            return

        name = input("Plant name: ").strip()
        category = input("Category: ").strip().title()
        price = float(input("Price (Rs.): "))
        stock = int(input("Stock quantity: "))
        sold = int(input("Units sold: "))
        supplier = input("Supplier: ").strip()
        watering = input("Watering requirement: ").strip()
        sunlight = input("Sunlight requirement: ").strip()

        if not name or not category or min(price, stock, sold) < 0:
            print("Enter valid details. Price, stock and sold cannot be negative.")
            return

        record = {
            "Plant_ID": plant_id, "Plant_Name": name, "Category": category,
            "Price": price, "Stock": stock, "Sold": sold, "Supplier": supplier,
            "Watering_Requirement": watering, "Sunlight_Requirement": sunlight,
            "Revenue": price * sold
        }
        df = pd.concat([df, pd.DataFrame([record])], ignore_index=True)
        save_data(df)
        print("Plant added successfully.")
    except ValueError:
        print("Invalid number. Please try again.")


def search_plant():
    df = load_data()
    choice = input("Search by (1) Plant ID or (2) Plant Name? ").strip()

    if choice == "1":
        try:
            plant_id = int(input("Enter Plant ID: "))
            result = df[df["Plant_ID"] == plant_id]
        except ValueError:
            print("Plant ID must be a number.")
            return
    elif choice == "2":
        name = input("Enter plant name: ").strip()
        result = df[df["Plant_Name"].str.contains(name, case=False, na=False)]
    else:
        print("Invalid choice.")
        return

    if result.empty:
        print("No matching plant found.")
    else:
        print(result.fillna("Not specified").to_string(index=False))


def update_plant():
    df = load_data()
    try:
        plant_id = int(input("Enter Plant ID to update: "))
    except ValueError:
        print("Plant ID must be a number.")
        return

    matches = df.index[df["Plant_ID"] == plant_id].tolist()
    if not matches:
        print("Plant not found.")
        return

    index = matches[0]
    print("1. Update price")
    print("2. Update stock")
    choice = input("Choose what to update: ").strip()

    try:
        if choice == "1":
            value = float(input("Enter new price: "))
            if value < 0:
                print("Price cannot be negative.")
                return
            df.at[index, "Price"] = value
        elif choice == "2":
            value = int(input("Enter new stock: "))
            if value < 0:
                print("Stock cannot be negative.")
                return
            df.at[index, "Stock"] = value
        else:
            print("Invalid choice.")
            return

        df.at[index, "Revenue"] = df.at[index, "Price"] * df.at[index, "Sold"]
        save_data(df)
        print("Plant record updated successfully.")
    except ValueError:
        print("Invalid value. Record was not updated.")


def delete_plant():
    df = load_data()
    try:
        plant_id = int(input("Enter Plant ID to delete: "))
    except ValueError:
        print("Plant ID must be a number.")
        return

    updated = df[df["Plant_ID"] != plant_id]
    if len(updated) == len(df):
        print("Plant not found.")
    else:
        save_data(updated)
        print("Plant record deleted successfully.")
