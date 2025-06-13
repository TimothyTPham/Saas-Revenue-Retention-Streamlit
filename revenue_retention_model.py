import streamlit as st
import pandas as pd

st.title("SaaS Revenue Retention & Expansion Model")

# --- User Inputs ---
starting_mrr = st.number_input("Starting MRR", value=100000, step=1000)
churn_rate = st.number_input("Monthly Churn Rate (%)", value=5.0, step=0.1) / 100
expansion_rate = st.number_input("Expansion Rate (%)", value=10.0, step=0.1) / 100
months = st.slider("Number of Months", min_value=1, max_value=36, value=12)

# --- Calculations ---
data = []
current_mrr = starting_mrr

for month in range(1, months + 1):
    churned_mrr = round(current_mrr * churn_rate)
    remaining_mrr = current_mrr - churned_mrr
    expansion_mrr = round(remaining_mrr * expansion_rate)
    ending_mrr = round(remaining_mrr + expansion_mrr)
    grr = (current_mrr - churned_mrr) / current_mrr
    nrr = (current_mrr - churned_mrr + expansion_mrr) / current_mrr

    data.append([
        f"Month {month}",
        f"${int(round(current_mrr)):,}",
        f"${churned_mrr:,}",
        f"${expansion_mrr:,}",
        f"${ending_mrr:,}",
        f"{grr:.1%}",
        f"{nrr:.1%}"
    ])

    current_mrr = ending_mrr

# --- Output Table ---
df = pd.DataFrame(data, columns=[
    "Month", "Starting MRR", "Churned MRR", "Expansion MRR",
    "Ending MRR", "GRR", "NRR"
])
st.subheader("Monthly Retention Table")
st.dataframe(df)

# --- Line Chart ---
chart_df = df[["Month", "Starting MRR", "Ending MRR"]].copy()
chart_df["Month"] = chart_df["Month"].str.extract(r'(\\d+)').astype(int)
chart_df["Starting MRR"] = chart_df["Starting MRR"].replace('[\\$,]', '', regex=True).astype(float)
chart_df["Ending MRR"] = chart_df["Ending MRR"].replace('[\\$,]', '', regex=True).astype(float)
chart_df.set_index("Month", inplace=True)

st.subheader("MRR Over Time")
st.line_chart(chart_df)

# --- Footer ---
st.markdown("---")
st.markdown("👨‍💻 Built by [Timothy T. Pham](https://github.com/TimothyTPham) — Part of the SaaS Financial Modeling Series")
