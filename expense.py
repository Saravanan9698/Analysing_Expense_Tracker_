import streamlit as st
from faker import Faker
import pandas as pd
import numpy as numpy
import random
from datetime import date
from getpass import getpass

faker = Faker()

categories = ["Groceries","stationary","Bills","Subscription","Investment","Transportation"]
payment_modes = ["UPI", "Cash", "Debit card"]
bills = ["water bill", "electricity bill", "wifi", "phone", "gas"]
subscription = ["audible", "prime","netflix","disney"]
description = [
    "Taxi fare for office",
    "monthly metro pass renewal",
    "Fuel refill at Gas Station Name",
    "Internet service provider bill",
    "Mobile recharge",
    "streaming service subscription renewal",
    "Accessories shopping",
]


def generate_monthly_data(year,month):
    data = []
    for _ in range(100):
        data.append({"Date": fake.date_this_month(),
            "Category": random.choice(categories),
            "payment mode": random.choice(payment_modes),
            "Description": fake.random.choice(description),
            "Amount": round(random.uniform(10,1000),2),

        })
    return pd.DataFrame(data)


# Generate data for all months
year = 2023
monthly_data = {}
for month in range(1,13):
    monthly_data[f"{year}_{month}"] = generate_monthly_data(year,month)
exp_data = generate_monthly_data(month,year)

# Save each month to a csv
for month, data in monthly_data.items():
    data.to_csv(f"{month}.csv, index = False")

