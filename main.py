from plant_operations import (
    add_plant, display_plants, search_plant, update_plant, delete_plant
)
from data_analysis import analyse_dataset, generate_summary_report
from reports import show_data_structure_examples, show_category_report
from table_display import show_plant_table
from charts import (
    show_category_chart, show_category_pie_chart, show_price_chart
)


def main():
    """Display the menu and run the selected operation."""
    while True:
        print("\\n" + "=" * 52)
        print("          GREEN LEAF NURSERY MANAGEMENT")
        print("=" * 52)
        print("1. Add a new plant")
        print("2. Display all plants (Tabulate table)")
        print("3. Search for a plant")
        print("4. Update a plant")
        print("5. Delete a plant")
        print("6. Generate summary report")
        print("7. Run NumPy and Pandas analysis")
        print("8. Show Python data-structure examples")
        print("9. Show category report")
        print("10. Show category bar chart")
        print("11. Show category pie chart")
        print("12. Show plant price chart")
        print("0. Exit")
        print("=" * 52)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_plant()
        elif choice == "2":
            show_plant_table()
        elif choice == "3":
            search_plant()
        elif choice == "4":
            update_plant()
        elif choice == "5":
            delete_plant()
        elif choice == "6":
            generate_summary_report()
        elif choice == "7":
            analyse_dataset()
        elif choice == "8":
            show_data_structure_examples()
        elif choice == "9":
            show_category_report()
        elif choice == "10":
            show_category_chart()
        elif choice == "11":
            show_category_pie_chart()
        elif choice == "12":
            show_price_chart()
        elif choice == "0":
            print("Thank you for using Green Leaf Nursery Management!")
            break
        else:
            print("Invalid choice. Please enter a number from 0 to 12.")


if __name__ == "__main__":
    main()
