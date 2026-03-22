import pandas as pd

REQUIRED_COLUMNS = ["Date", "Product", "Region", "Units", "Price"]

def process_sales_data(file):

    df = pd.read_csv(file)

    df.columns = [col.strip() for col in df.columns]

    rename_map = {
        "Units_Sold": "Units",
        "Unit_Price": "Price"
    }

    df.rename(columns=rename_map, inplace=True)

    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]

    if missing:
        raise ValueError(f"Dataset missing required columns: {missing}")
    
    df["Revenue"] = df["Units"] * df["Price"]

    total_revenue = df["Revenue"].sum()

    revenue_by_product = df.groupby("Product")["Revenue"].sum()
    revenue_by_region = df.groupby("Region")["Revenue"].sum()

    summary = {
        "total_revenue": total_revenue,

        "top_product": revenue_by_product.idxmax(),
        "least_product": revenue_by_product.idxmin(),

        "top_region": revenue_by_region.idxmax(),
        "least_region": revenue_by_region.idxmin(),

        "average_order_value": df["Revenue"].mean()
    }

    return summary