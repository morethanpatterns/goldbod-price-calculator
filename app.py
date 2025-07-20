import streamlit as st
from datetime import datetime

st.title("GoldBod Ghana Pound Price Calculator")

# Display current date and time
now = datetime.now()
st.write(f"**Date & Time:** {now.strftime('%Y-%m-%d %H:%M:%S')}")

# User Inputs (empty fields for user input)
lme_price_usd = st.number_input("LME Price per Ounce (USD):", value=None, step=1)
exchange_rate = st.number_input("Exchange Rate (GHS/USD):", value=None, step=0.01)
adjustment_factor = st.number_input("Adjustment Factor (%):", value=95.86, step=0.01)

# Constants
grams_in_ounce = 31.1035
grams_in_ghana_pound = 7.75

# Calculations
if lme_price_usd and exchange_rate:
    ghs_per_ounce = lme_price_usd * exchange_rate
    adjusted_ghs_per_ounce = ghs_per_ounce * (adjustment_factor / 100)
    goldbod_ghana_pound_price = (adjusted_ghs_per_ounce / grams_in_ounce) * grams_in_ghana_pound

    # Display Results
    st.subheader("Calculated Results")
    st.write(f"**GHS per Ounce:** {ghs_per_ounce:,.2f}")
    st.write(f"**Adjusted GHS per Ounce:** {adjusted_ghs_per_ounce:,.2f}")
    st.write(f"**GoldBod Ghana Pound Price (GHS):** {goldbod_ghana_pound_price:,.2f}")
else:
    st.warning("Please enter both LME Price and Exchange Rate to calculate results.")
