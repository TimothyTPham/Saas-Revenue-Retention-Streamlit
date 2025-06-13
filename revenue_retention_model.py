import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Revenue Retention Model", layout="centered")

st.title("SaaS Revenue Retention Model")

# Sample input table – replace with your actual logic or data loading
st.subheader("Revenue Retention Inputs")

initial_revenue = st.number_input("Initial Monthly Revenue ($)", min_value=0, value=10000, step=500)
retention_rate = st.slider("Monthly Gross Revenue Retention (%)", min_value=0, max_value=100, value=90)
expansion_rate = st.slider("Monthly Expansion (% of retained revenue)", min_value=0, max_value=100, value=5)
months = st.slider("Number of Months", min_value=1, max_value=24, value=12)

# Initialize DataFrame
data = []
revenue = initial_revenue

for month in range(1, months + 1):
    retained = revenue * (retention_rate / 100)
    expanded = retained * (expansion_rate / 100)
    total = retained + expanded
    data.append({
        "Month": f"Month {month}",
        "Starting Revenue": round(revenue),
        "Retained Revenue": round(retained),
        "Expansion Revenue": round(expanded),
        "Total Revenue": round(total)
    })
    revenue = total

chart_df = pd.DataFrame(data)

# --- SAFER FIX FOR MONTH EXTRACTION ---
chart_df["Month"] = chart_df["Month"].str.extract(r'(\d+)')[0]
chart_df = chart_df.dropna(subset=["Month"])
chart_df["Month"] = chart_df["Month"].astype(int)

# --- Show Table ---
st.subheader("Revenue Retention Table")
st.dataframe(chart_df.style.format({
    "Starting Revenue": "${:,.0f}",
    "Retained Revenue": "${:,.0f}",
    "Expansion Revenue": "${:,.0f}",
    "Total Revenue": "${:,.0f}"
}))

# --- Plot ---
st.subheader("Revenue Over Time")
fig, ax = plt.subplots()
ax.plot(chart_df["Month"], chart_df["Total Revenue"], marker='o')
ax.set_xlabel("Month")
ax.set_ylabel("Total Revenue ($)")
ax.set_title("Monthly Revenue Retention and Expansion")
ax.grid(True)
st.pyplot(fig)

# --- Footer ---
st.caption("Built by Tim Pham")
