import streamlit as st
from faker import Faker
import pandas as pd
import numpy as numpy
import random
from datetime import datetime
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

def generate_monthly_data(year):
    data = []
    for _ in range(100):

        start_date = datetime(2024, 12, 1)
        end_date = datetime(2024, 12, 31)
        
        data.append({"Date": faker.date_between(start_date, end_date),
                     
            "Category": random.choice(categories),
            "payment mode": random.choice(payment_modes),
            "Description": faker.random.choice(description),
            "Amount": round(random.uniform(10,1000),2),
            "Cashback":round(random.uniform(0,20),2)

        })
    return pd.DataFrame(data)

# Generate data for all months
year = 2024

# monthly_data[f"{year}_{month}",] = generate_monthly_data(year,month)
exp_data = generate_monthly_data(year)
# print(monthly_data[f"{year}_{month}"])

print(exp_data)