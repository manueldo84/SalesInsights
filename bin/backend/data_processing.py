import pandas as pd

def process_sales_data(file):

    df = pd.read_csv(file)

    # Handle different column names
    if "Units_Sold" in df.columns:
        df.rename(columns={"Units_Sold": "Units"}, inplace=True)

    if "Unit_Price" in df.columns:
        df.rename(columns={"Unit_Price": "Price"}, inplace=True)

    df["Revenue"] = df["Units"] * df["Price"]

    total_revenue = df["Revenue"].sum()

    top_product = df.groupby("Product")["Revenue"].sum().idxmax()

    top_region = df.groupby("Region")["Revenue"].sum().idxmax()

    avg_order_value = df["Revenue"].mean()

    summary = {
        "total_revenue": float(total_revenue),
        "top_product": top_product,
        "top_region": top_region,
        "average_order_value": float(avg_order_value)
    }

    return summary