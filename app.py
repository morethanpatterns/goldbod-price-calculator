import streamlit as st

st.title("GoldBod Ghana Pound Price Calculator")

# User Inputs
lme_price_usd = st.number_input("LME Price per Ounce (USD):", value=3348.00, step=0.01)
exchange_rate = st.number_input("Exchange Rate (GHS/USD):", value=10.42, step=0.01)
adjustment_factor = st.number_input("Adjustment Factor (%):", value=95.92, step=0.01)

# Constants
grams_in_ounce = 31.1035
grams_in_ghana_pound = 7.75

# Calculations
ghs_per_ounce = lme_price_usd * exchange_rate
adjusted_ghs_per_ounce = ghs_per_ounce * (adjustment_factor / 100)
goldbod_ghana_pound_price = (adjusted_ghs_per_ounce / grams_in_ounce) * grams_in_ghana_pound

# Display Results
st.subheader("Calculated Results")
st.write(f"**GHS per Ounce:** {ghs_per_ounce:,.2f}")
st.write(f"**Adjusted GHS per Ounce:** {adjusted_ghs_per_ounce:,.2f}")
st.write(f"**GoldBod Ghana Pound Price (GHS):** {goldbod_ghana_pound_price:,.2f}")
