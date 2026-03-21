def generate_insights(summary):

    text = f"""
Sales performance analysis:

Total revenue generated was ${summary['total_revenue']:.2f}.
The best performing product category was {summary['top_product']}.
The region contributing the most revenue was {summary['top_region']}.
The average order value was ${summary['average_order_value']:.2f}.

Recommendation:
Focus marketing efforts on the top-performing product and replicate
successful sales strategies used in the highest performing region.
"""

    return text