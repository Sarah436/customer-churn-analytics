import pandas as pd
import random

# Load current live data
file_path = "data/customer_churn_live.csv"
df = pd.read_csv(file_path)

print("Current rows:", len(df))

# Create new customer records
new_customers = []

for i in range(10):

    customer = df.sample(1).iloc[0].copy()

    customer["CustomerID"] = f"NEW{i+1:04d}"

    # Keep the new records slightly different
    customer["Tenure Months"] = random.randint(1, 72)
    customer["Monthly Charges"] = round(random.uniform(20, 110), 2)
    customer["Total Charges"] = round(
        customer["Tenure Months"] * customer["Monthly Charges"], 2
    )

    new_customers.append(customer)

new_data = pd.DataFrame(new_customers)

# Add new customers
df_updated = pd.concat(
    [df, new_data],
    ignore_index=True
)

# Save updated live data
df_updated.to_csv(file_path, index=False)

print("New customer records added!")
print("New rows:", len(df_updated))