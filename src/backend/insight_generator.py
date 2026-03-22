def generate_insights(summary):

    insights = {
        "summary": {
            "total_revenue": "${:,.2f}".format(summary['total_revenue']),
            "best_product_category": summary['top_product'],
            "least_product_category": summary['least_product'],
            "top_region": summary['top_region'],
            "least_region": summary['least_region'],
            "average_order_value": "${:,.2f}".format(summary['average_order_value'])
        },

        "insights": [
            f"{summary['top_product']} is the best performing product category.",
            f"{summary['least_product']} is the least performing product category.",
            f"{summary['top_region']} generates the highest revenue.",
            f"{summary['least_region']} contributes the least revenue."
        ],

        "recommendation": (
            f"Increase marketing efforts for {summary['least_product']} "
            f"in the {summary['least_region']} region to improve sales performance."
        )
    }

    return insights