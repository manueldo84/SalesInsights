import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000/analyze"

st.set_page_config(page_title="AI Sales Intelligence Dashboard", layout="wide")

st.title("📊 AI Sales Intelligence Dashboard")

uploaded_file = st.file_uploader("Upload Sales Dataset", type=["csv"])

if uploaded_file is not None:

    response = requests.post(
        API_URL,
        files={"file": uploaded_file.getvalue()}
    )

    if response.status_code == 200:

        data = response.json()

        st.success("Analysis Completed")

        summary = data["insights"]["summary"]

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Revenue", f"${summary['total_revenue']:.2f}")
        col2.metric("Top Product", summary["top_product"])
        col3.metric("Top Region", summary["top_region"])

        st.subheader("📈 Business Insights")

        for insight in data["insights"]["business_insights"]:
            st.write("•", insight)

        st.subheader("💡 Recommendations")

        for rec in data["insights"]["recommendations"]:
            st.write("•", rec)

        st.subheader("📊 Sales Charts")

        st.image(data["charts"]["product_chart"])
        st.image(data["charts"]["region_chart"])

    else:
        st.error("API Error")