def generate_insights(summary):

    insights = {
        "report_title": "Sales Performance Report",

        "summary": {
            "total_revenue": f"${summary['total_revenue']:.2f}",
            "top_product": summary['top_product'],
            "least_product": summary['least_product'],
            "top_region": summary['top_region'],
            "least_region": summary['least_region'],
            "average_order_value": f"${summary['average_order_value']:.2f}"
        },

        "business_insights": [
            f"The strongest demand was observed for {summary['top_product']}.",
            f"The weakest product category is {summary['least_product']}, which may require marketing or pricing adjustments.",
            f"The region contributing the most revenue is {summary['top_region']}.",
            f"The lowest performing region is {summary['least_region']}."
        ],

        "recommendations": [
            f"Increase inventory and promotions for {summary['top_product']}.",
            f"Investigate low sales in {summary['least_region']}.",
            f"Consider targeted marketing campaigns for underperforming products."
        ]
    }

    return insights