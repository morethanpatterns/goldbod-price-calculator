import streamlit as st

st.title('GoldBod Ghana Pound Price Calculator')

# Inputs from user
lme_price = st.number_input('LME Price per Ounce (USD)', value=3348.00)
exchange_rate = st.number_input('Exchange Rate (GHS/USD)', value=10.42)
adjustment_factor = st.number_input('Adjustment Factor (%)', value=95.92)

# Constants
grams_per_ounce = 31.1035
grams_per_ghana_pound = 7.75

# Calculations
ghs_per_ounce = lme_price * exchange_rate
adjusted_ghs_per_ounce = ghs_per_ounce * (adjustment_factor / 100)
goldbod_ghana_pound_price = adjusted_ghs_per_ounce / grams_per_ounce * grams_per_ghana_pound

# Display results
st.subheader('Calculated Results:')
st.write(f'GHS per Ounce: **{ghs_per_ounce:,.2f} GHS**')
st.write(f'Adjusted GHS per Ounce: **{adjusted_ghs_per_ounce:,.2f} GHS**')
st.write(f'GoldBod Ghana Pound Price: **{goldbod_ghana_pound_price:,.2f} GHS**')
