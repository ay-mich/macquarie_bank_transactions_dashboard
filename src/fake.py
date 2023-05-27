"""
This script generates a CSV file with fake transactions data using Faker library.
Each transaction contains a date, details, account, category, subcategory, notes,
debit, credit, balance, and an original description.
"""

import random
import pandas as pd
from faker import Faker

# Create a fake data generator
fake = Faker()

# Constants
NUM_ROWS = 2000  # number of rows
OUTPUT_FILE_PATH = "../import/fake.csv"

# Categories and subcategories mapping
categories = {
    "Education": ["Stationery"],
    "Financial": ["Cash Withdrawals", "Direct Debits", "Transfers"],
    "Food & Drink": [
        "Alcohol & Bars",
        "Fast Food",
        "Groceries",
        "Other Food Expenses",
        "Restaurants",
    ],
    "Gifts & Donations": ["Gifts"],
    "Health & Medical": ["Eyes", "Other Health Expenses", "Pharmacies"],
    "Home": ["Furnishings"],
    "Income": ["Salary"],
    "Insurance": ["Financial Insurance"],
    "Leisure": ["Dance", "Fun", "Games", "Movies", "Music"],
    "Personal": ["Clothing", "Other Personal Expenses"],
    "Services": ["Government", "Marketing"],
    "Technology": ["Hardware", "Online Services", "Software"],
    "Transportation": ["Fuel", "Parking & Tolls", "Public Transit", "Taxis"],
    "Travel": ["Accommodation", "Flights", "Tours & Cruises", "Travel Entertainment"],
    "Utilities": ["Electricity, Gas & Water", "Pay TV", "Phone"],
}


def generate_data():
    """Generates a list of dictionaries where each dictionary represents a fake transaction."""
    data = []

    for _ in range(NUM_ROWS):
        category = random.choice(list(categories.keys()))
        subcategory = random.choice(
            categories[category]
        )  # Pick a random subcategory related to the category

        # If category is "Income", amount is in the Credit column. For all other categories, it's in the Debit column.
        if category == "Income":
            credit = round(random.uniform(500, 1000), 2)
            debit = ""
        else:
            debit = round(random.uniform(1, 800), 2)
            credit = ""

        data.append(
            {
                "Transaction Date": fake.date_between(
                    start_date="-1y", end_date="today"
                ).strftime("%d-%m-%Y"),
                "Details": fake.company(),
                "Account": "Transaction Account",
                "Category": category,
                "Subcategory": subcategory,
                "Notes": fake.sentence(),
                "Debit": debit,
                "Credit": credit,
                "Balance": round(random.uniform(10000, 50000), 2),
                "Original Description": fake.sentence(),
            }
        )

    df = pd.DataFrame(data)
    return df


def main():
    """Main function that generates the data and writes it to a CSV file."""
    try:
        data = generate_data()
        df = pd.DataFrame(data)
        df.to_csv(OUTPUT_FILE_PATH, index=False)
        print(f"Data successfully written to {OUTPUT_FILE_PATH}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
