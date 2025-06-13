# SaaS Revenue Retention & Expansion Model

This model forecasts Gross Revenue Retention (GRR), Net Revenue Retention (NRR), and MRR expansion over time, based on inputs like churn and upsell rates.

Built in Python and deployed with Streamlit, this tool allows users to simulate how customer revenue retention and expansion impact Monthly Recurring Revenue (MRR) over a 12+ month period.

---

## 🌐 Live App

Try the live version here:  
👉 [SaaS Revenue Retention App](https://saas-revenue-retention-app-bpepebtftewzxstyd5bt3u.streamlit.app/)

---

## 📊 What It Does

- Simulates monthly MRR retention and growth
- Calculates GRR and NRR for each month
- Visualizes MRR trajectory with a line chart
- Interactive inputs for:
  - Starting MRR
  - Monthly churn rate
  - Expansion rate
  - Forecast duration (1–36 months)

---

## 🧮 Key Formulas

- **Churned MRR** = `Starting MRR × Churn Rate`
- **Expansion MRR** = `(Starting MRR - Churned MRR) × Expansion Rate`
- **Ending MRR** = `Starting MRR - Churned MRR + Expansion MRR`
- **GRR** = `(Starting MRR - Churned MRR) ÷ Starting MRR`
- **NRR** = `(Ending MRR ÷ Starting MRR)`

---

## 🚀 Run It Locally

```bash
pip install streamlit pandas
streamlit run revenue_retention_model.py
