import pandas as pd
import matplotlib.pyplot as plt

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
    "total_revenue": float(total_revenue),

    "top_product": str(revenue_by_product.idxmax()),
    "least_product": str(revenue_by_product.idxmin()),

    "top_region": str(revenue_by_region.idxmax()),
    "least_region": str(revenue_by_region.idxmin()),

    "average_order_value": float(df["Revenue"].mean())
    }

    # Generate Visualizations

    revenue_by_product.plot(kind="bar", title="Revenue by Product")
    plt.xlabel("Product")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig("outputs/product_sales_chart.png")
    plt.clf()

    revenue_by_region.plot(kind="bar", title="Revenue by Region")
    plt.xlabel("Region")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig("outputs/region_sales_chart.png")
    plt.clf()

    return summary