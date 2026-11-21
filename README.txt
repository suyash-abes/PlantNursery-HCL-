PLANT NURSERY MANAGEMENT & DATA ANALYTICS SYSTEM
=================================================

HOW TO RUN
----------
1. Extract this folder.
2. Open the PlantNursery folder in VS Code.
3. Open Terminal > New Terminal.
4. Install all required packages:

   python -m pip install -r requirements.txt

5. Run the main program:

   python main.py

MENU
----
1. Add a new plant
2. Display all plants using Tabulate
3. Search for a plant
4. Update a plant
5. Delete a plant
6. Generate summary report
7. Run NumPy and Pandas analysis
8. Show Python data-structure examples
9. Show category report
10. Show category bar chart
11. Show category pie chart
12. Show plant price chart
0. Exit

FILES
-----
main.py                 Main menu
plant_operations.py    CRUD operations and CSV file handling
data_analysis.py       NumPy and Pandas analysis
reports.py             Python data structure examples and category report
table_display.py       Tabulate formatted inventory table
charts.py               Matplotlib charts
plants_dataset.csv     60 starter plant records
requirements.txt       Required Python packages

NOTES
-----
- Keep all files in the same folder.
- Run main.py from the PlantNursery folder.
- Add/update/delete operations change plants_dataset.csv.
- Make a backup of plants_dataset.csv before testing delete/update.
- The dataset is illustrative sample data, not actual business data.
- Revenue is calculated as Price multiplied by Sold.
- The chart window must be closed to return to the terminal menu.
