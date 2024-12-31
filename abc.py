from faker import Faker
import pandas as pd
import random
from datetime import datetime

# Initialize Faker instance
fake = Faker()

# Data categories and options
categories = ["Groceries", "Stationary", "Bills", "Subscription", "Investment", "Transportation"]
payment_modes = ["UPI", "Cash", "Debit card"]
bills = ["water bill", "electricity bill", "wifi", "phone", "gas"]
subscription = ["audible", "prime", "netflix", "disney"]
description = [
    "Taxi fare for office",
    "monthly metro pass renewal",
    "Fuel refill at Gas Station Name",
    "Internet service provider bill",
    "Mobile recharge",
    "streaming service subscription renewal",
    "Accessories shopping",
]

# Generate monthly expenses data for each month
def generate_monthly_expenses(year, num_entries=100):
    all_data = []
    for month in range(1, 13):  # Loop through each month (1 to 12)
        data = []
        for _ in hrange(num_entries):
            # Randomly selecting categories, payment modes, and amounts
            payment_mode = random.choice(payment_modes)
            category = random.choice(categories)
            amount = round(random.uniform(10, 500), 2)
            
            # Generate a random date within the specified month and year
            start_date = datetime(year, month, 1)
            end_date = datetime(year, month, 31)  # Handling last day of the month
            expense_date = fake.date_between_dates(date_start=start_date, date_end=end_date)
            
            # Build the expense dictionary
            expense = {
                "Date": expense_date,
                "Category": category,
                "Payment Mode": payment_mode,
                "Description": fake.sentence(),
                "Amount": round(random.uniform(10, 1000), 2)
            }
            
            # Add the expense to the list
            data.append(expense)
        
        all_data.extend(data)  # Add the data of this month to the overall list

    # Return the combined data as a pandas DataFrame
    return pd.DataFrame(all_data)

# Example usage
year = 2023
exp_data = generate_monthly_expenses(year, num_entries=100)

# Save the data to a CSV file (optional)
exp_data.to_csv("fake_data_all_months.csv", index=False)

# Display the first few rows of the data
print(exp_data.head())