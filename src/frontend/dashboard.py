import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000/analyze"

st.set_page_config(page_title="AI Sales Intelligence Dashboard", layout="wide")
st.title("📊 AI Sales Intelligence Dashboard")

uploaded_file = st.file_uploader("Upload Sales Dataset", type=["csv"])

def parse_ai_report(report_text):
    """
    Attempt to split AI report into business insights and recommendations
    assuming the report contains numbered or bulleted sections.
    """
    insights, recommendations = [], []

    if not report_text:
        return insights, recommendations

    lines = report_text.splitlines()
    section = None

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if "business insights" in line.lower():
            section = "insights"
            continue
        elif "recommendations" in line.lower():
            section = "recommendations"
            continue

        if section == "insights":
            insights.append(line.lstrip("•0123456789. "))
        elif section == "recommendations":
            recommendations.append(line.lstrip("•0123456789. "))

    return insights, recommendations


if uploaded_file is not None:
    try:
        response = requests.post(
            API_URL,
            files={"file": uploaded_file.getvalue()}
        )

        if response.status_code != 200:
            st.error(f"API Error: {response.status_code}")
        else:
            data = response.json()

            summary = data.get("summary", {})
            ai_report = data.get("ai_report", "")

            st.success("Analysis Completed ✅")

            col1, col2, col3 = st.columns(3)
            col1.metric("Total Revenue", f"${float(summary.get('total_revenue', 0)):.2f}")
            col2.metric("Top Product", summary.get("top_product", "N/A"))
            col3.metric("Top Region", summary.get("top_region", "N/A"))

            insights, recommendations = parse_ai_report(ai_report)

            st.subheader("📈 Business Insights")
            if insights:
                for insight in insights:
                    st.write("•", insight)
            else:
                st.write("No business insights available.")

            st.subheader("💡 Recommendations")
            if recommendations:
                for rec in recommendations:
                    st.write("•", rec)
            else:
                st.write("No recommendations available.")

            charts = data.get("charts", {})
            st.subheader("📊 Sales Charts")
            product_chart = charts.get("product_chart")
            region_chart = charts.get("region_chart")

            if product_chart:
                st.image(product_chart, caption="Revenue by Product")
            if region_chart:
                st.image(region_chart, caption="Revenue by Region")

    except Exception as e:
        st.error(f"Unexpected error: {str(e)}")