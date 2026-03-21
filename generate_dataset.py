import pandas as pd
import random
from datetime import datetime, timedelta

products = ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"]
regions = ["North", "South", "East", "West"]

start_date = datetime(2023, 1, 1)

data = []

for i in range(1000):

    date = start_date + timedelta(days=random.randint(0, 365))

    product = random.choice(products)
    region = random.choice(regions)

    units = random.randint(1, 20)

    price = random.randint(100, 1500)

    revenue = units * price

    data.append([date, product, region, units, price, revenue])

df = pd.DataFrame(data, columns=[
    "Date",
    "Product",
    "Region",
    "Units",
    "Price",
    "Revenue"
])

df.to_csv("sales_data.csv", index=False)

print("Dataset generated successfully.")