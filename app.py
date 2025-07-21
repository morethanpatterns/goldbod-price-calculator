import streamlit as st
from datetime import datetime
import requests

st.title('GoldBod Ghana Pound Price Calculator')

# Current date and time
now = datetime.now()
st.write(f"**Date & Time:** {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Replace with your actual API keys from the websites
METALS_API_KEY = 'YOUR_METALS_API_KEY'
EXCHANGE_API_KEY = 'YOUR_EXCHANGE_API_KEY'

# Function to fetch gold price from Metals-API
def get_gold_price():
    url = f"https://metals-api.com/api/latest?access_key={METALS_API_KEY}&base=USD&symbols=XAU"
    response = requests.get(url).json()
    try:
        gold_price = 1 / response['rates']['XAU']
        return gold_price
    except:
        return None

# Function to fetch USD to GHS rate from ExchangeRate-API
def get_exchange_rate():
    url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_API_KEY}/latest/USD"
    response = requests.get(url).json()
    try:
        exchange_rate = response['conversion_rates']['GHS']
        return exchange_rate
    except:
        return None

# Fetch real-time data
gold_price = get_gold_price()
exchange_rate = get_exchange_rate()

# Display fetched values
st.subheader("Automatically fetched values:")
if gold_price:
    st.write(f"**LME Gold Price per Ounce (USD):** {gold_price:,.2f}")
else:
    st.warning("Could not fetch Gold price from API.")

if exchange_rate:
    st.write(f"**Exchange Rate (GHS/USD):** {exchange_rate:.4f}")
else:
    st.warning("Could not fetch Exchange Rate from API.")

# Manual override if fetch fails
manual_gold_price = st.number_input('Override Gold Price per Ounce (USD):', value=gold_price, step=1.0)
manual_exchange_rate = st.number_input('Override Exchange Rate (GHS/USD):', value=exchange_rate, step=0.01)

# Adjustment Factor Input
adjustment_factor = st.number_input('Adjustment Factor (%):', value=95.86, step=0.01)

# Constants
grams_per_ounce = 31.1035
grams_per_ghana_pound = 7.75

# Calculations
if manual_gold_price and manual_exchange_rate:
    ghs_per_ounce = manual_gold_price * manual_exchange_rate
    adjusted_ghs_per_ounce = ghs_per_ounce * (adjustment_factor / 100)
    goldbod_ghana_pound_price = (adjusted_ghs_per_ounce / grams_per_ounce) * grams_per_ghana_pound

    # Display results
    st.subheader('Calculated Results:')
    st.write(f'**GHS per Ounce:** {ghs_per_ounce:,.2f} GHS')
    st.write(f'**Adjusted GHS per Ounce:** {adjusted_ghs_per_ounce:,.2f} GHS')
    st.write(f'**GoldBod Ghana Pound Price:** {goldbod_ghana_pound_price:,.2f} GHS')
else:
    st.warning("Please ensure valid values for Gold Price and Exchange Rate.")
