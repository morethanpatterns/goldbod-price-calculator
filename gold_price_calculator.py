import streamlit as st
import pandas as pd
from datetime import datetime

st.title("Financial Ledger - Transaction Tracker")

# Initialize ledger in session state
if 'ledger' not in st.session_state:
    st.session_state.ledger = pd.DataFrame(columns=[
        "Date", "Description", "Beneficiary", "Debit (Outflow)", "Credit (Inflow)", "Balance"
    ])

# Input Fields
st.subheader("Enter New Transaction:")

date = st.date_input("Date:", datetime.today())
description = st.text_input("Description:")
beneficiary = st.text_input("Beneficiary:")

col1, col2 = st.columns(2)
with col1:
    debit = st.number_input("Debit (Outflow):", min_value=0.0, step=0.01, format="%.2f")
with col2:
    credit = st.number_input("Credit (Inflow):", min_value=0.0, step=0.01, format="%.2f")

# Add Transaction Button
if st.button("Add Transaction"):
    prev_balance = st.session_state.ledger["Balance"].iloc[-1] if len(st.session_state.ledger) > 0 else 0.0
    new_balance = prev_balance + credit - debit

    # Append new transaction with numeric default values
    new_entry = {
        "Date": date.strftime("%d-%m-%Y"),
        "Description": description,
        "Beneficiary": beneficiary,
        "Debit (Outflow)": debit if debit else 0.0,
        "Credit (Inflow)": credit if credit else 0.0,
        "Balance": new_balance
    }
    
    st.session_state.ledger = pd.concat([st.session_state.ledger, pd.DataFrame([new_entry])], ignore_index=True)

# Display the ledger clearly
st.subheader("Current Ledger:")
st.dataframe(st.session_state.ledger.style.format({
    "Debit (Outflow)": "{:,.2f}",
    "Credit (Inflow)": "{:,.2f}",
    "Balance": "{:,.2f}"
}), height=400)

# Summary Totals
st.subheader("Overall Summary:")
total_debit = st.session_state.ledger["Debit (Outflow)"].astype(float).sum()
total_credit = st.session_state.ledger["Credit (Inflow)"].astype(float).sum()
current_balance = st.session_state.ledger["Balance"].iloc[-1] if len(st.session_state.ledger) > 0 else 0.0

st.write(f"**Total Debit (Outflow):** {total_debit:,.2f}")
st.write(f"**Total Credit (Inflow):** {total_credit:,.2f}")
st.write(f"**Current Balance:** {current_balance:,.2f}")

# Beneficiary Subtotals
st.subheader("Subtotal by Beneficiary:")

if len(st.session_state.ledger) > 0:
    subtotal_df = st.session_state.ledger.copy()
    subtotals = subtotal_df.groupby("Beneficiary").agg({
        "Debit (Outflow)": "sum",
        "Credit (Inflow)": "sum"
    }).reset_index()

    subtotals["Net Amount"] = subtotals["Credit (Inflow)"] - subtotals["Debit (Outflow)"]
    st.dataframe(subtotals.style.format({
        "Debit (Outflow)": "{:,.2f}",
        "Credit (Inflow)": "{:,.2f}",
        "Net Amount": "{:,.2f}"
    }), height=300)
else:
    st.info("No transactions yet to show subtotals.")