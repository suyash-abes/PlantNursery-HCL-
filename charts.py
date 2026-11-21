import matplotlib.pyplot as plt
from plant_operations import load_data


def show_category_chart():
    """Bar chart showing the number of plants in each category."""
    plants = load_data()
    counts = plants["Category"].value_counts()

    plt.figure(figsize=(9, 5))
    counts.plot(kind="bar", edgecolor="black")
    plt.title("Number of Plants in Each Category")
    plt.xlabel("Plant Category")
    plt.ylabel("Number of Plant Records")
    plt.xticks(rotation=35, ha="right")
    plt.tight_layout()
    plt.show()


def show_category_pie_chart():
    """Pie chart showing each category's share of plant records."""
    plants = load_data()
    counts = plants["Category"].value_counts()

    plt.figure(figsize=(8, 8))
    plt.pie(counts, labels=counts.index, autopct="%1.1f%%", startangle=90)
    plt.title("Plant Category Distribution")
    plt.tight_layout()
    plt.show()


def show_price_chart():
    """Bar chart comparing the prices of the first 15 plants."""
    plants = load_data().dropna(subset=["Price"]).head(15)

    plt.figure(figsize=(11, 5))
    plt.bar(plants["Plant_Name"], plants["Price"], edgecolor="black")
    plt.title("Price Comparison of First 15 Plants")
    plt.xlabel("Plant Name")
    plt.ylabel("Price (Rs.)")
    plt.xticks(rotation=65, ha="right")
    plt.tight_layout()
    plt.show()
