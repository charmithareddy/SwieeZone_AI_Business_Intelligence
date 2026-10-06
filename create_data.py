import pandas as pd
import numpy as np

# Make the results reproducible
np.random.seed(42)

# Number of orders
num_orders = 1000

# Product information
products = [
    "T-Shirt",
    "Jeans",
    "Sneakers",
    "Hoodie",
    "Dress",
    "Jacket",
    "Watch",
    "Backpack",
    "Sunglasses",
    "Perfume"
]

categories = {
    "T-Shirt": "Clothing",
    "Jeans": "Clothing",
    "Sneakers": "Footwear",
    "Hoodie": "Clothing",
    "Dress": "Clothing",
    "Jacket": "Clothing",
    "Watch": "Accessories",
    "Backpack": "Accessories",
    "Sunglasses": "Accessories",
    "Perfume": "Beauty"
}

regions = [
    "North",
    "South",
    "East",
    "West"
]

payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Cash on Delivery"
]

# Generate data
data = []

# Generate dates across one year
dates = pd.date_range(
    start="2025-01-01",
    end="2025-12-31",
    periods=num_orders
)

for order_id in range(1, num_orders + 1):

    product = np.random.choice(products)

    quantity = np.random.randint(1, 5)

    price = np.random.randint(300, 5000)

    discount = np.random.randint(0, 31)

    revenue = quantity * price * (1 - discount / 100)

    region = np.random.choice(regions)

    payment_method = np.random.choice(payment_methods)

    order_date = dates[order_id - 1]

    data.append([
        order_id,
        order_date,
        product,
        categories[product],
        quantity,
        price,
        discount,
        round(revenue, 2),
        region,
        payment_method
    ])

# Create DataFrame
df = pd.DataFrame(
    data,
    columns=[
        "Order_ID",
        "Order_Date",
        "Product",
        "Category",
        "Quantity",
        "Price",
        "Discount",
        "Revenue",
        "Region",
        "Payment_Method"
    ]
)

# Save dataset
df.to_csv("data/swieeZone_sales.csv", index=False)

print("SwieeZone dataset created successfully!")
print(f"Total orders: {len(df)}")
print(f"Total revenue: ₹{df['Revenue'].sum():,.2f}")
print(f"Date range: {df['Order_Date'].min().date()} to {df['Order_Date'].max().date()}")