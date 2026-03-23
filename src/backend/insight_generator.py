from groq import Groq
from dotenv import load_dotenv
import os
 
load_dotenv()
 
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
 
def generate_ai_insights(summary):
 
    prompt = f"""
You are a senior business data analyst.
 
Analyze the following sales summary and produce:
 
1. Business insights
2. Key trends
3. Strategic recommendations
 
Sales Summary:
--------------
Total Revenue: {summary['total_revenue']}
Top Product: {summary['top_product']}
Least Product: {summary['least_product']}
Top Region: {summary['top_region']}
Lowest Region: {summary['least_region']}
Average Order Value: {summary['average_order_value']}
 
Write the output professionally like a business report.
"""
 
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
 
    return response.choices[0].message.content