import streamlit as st
from datetime import datetime
import requests
from bs4 import BeautifulSoup

st.title('GoldBod Ghana Pound Price Calculator')

# Current date and time
now = datetime.now()
st.write(f"**Date & Time:** {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Function to fetch gold price from Kitco
def get_gold_price():
    try:
        url = 'https://www.kitco.com/charts/livegold.html'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        price_tag = soup.find('span', {'id': 'sp-bid'})
        price = float(price_tag.text.replace(',', '').strip())
        return price
    except:
        return None

# Function to fetch exchange rate from Bank of Ghana
def get_exchange_rate():
    try:
        url = 'https://www.bog.gov.gh/'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        rate_tag = soup.select_one('table tbody tr td:nth-child(3)')
        rate = float(rate_tag.text.strip())
        return rate
    except:
        return None

# Fetching real-time data
gold_price = get_gold_price()
exchange_rate = get_exchange_rate()

# Show fetched values clearly
st.subheader("Automatically fetched values:")
if gold_price:
    st.write(f"**LME Gold Price per Ounce (USD):** {gold_price:,.2f}")
else:
    st.warning("Could not fetch Gold price from Kitco.")

if exchange_rate:
    st.write(f"**Exchange Rate (GHS/USD):** {exchange_rate:.4f}")
else:
    st.warning("Could not fetch Exchange Rate from Bank of Ghana.")

# Allow manual override if fetch fails
manual_gold_price = st.number_input('Override Gold Price per Ounce (USD) manually (if needed):', value=gold_price, step=1.0)
manual_exchange_rate = st.number_input('Override Exchange Rate (GHS/USD) manually (if needed):', value=exchange_rate, step=0.01)

# User inputs for Adjustment Factor
adjustment_factor = st.number_input('Adjustment Factor (%):', value=95.86, step=0.01)

# Constants
grams_per_ounce = 31.1035
grams_per_ghana_pound = 7.75

# Calculations
if manual_gold_price and manual_exchange_rate:
    ghs_per_ounce = manual_gold_price * manual_exchange_rate
    adjusted_ghs_per_ounce = ghs_per_ounce * (adjustment_factor / 100)
    goldbod_ghana_pound_price = (adjusted_ghs_per_ounce / grams_per_ounce) * grams_per_ghana_pound

    # Display Results
    st.subheader('Calculated Results:')
    st.write(f'**GHS per Ounce:** {ghs_per_ounce:,.2f} GHS')
    st.write(f'**Adjusted GHS per Ounce:** {adjusted_ghs_per_ounce:,.2f} GHS')
    st.write(f'**GoldBod Ghana Pound Price:** {goldbod_ghana_pound_price:,.2f} GHS')
else:
    st.warning("Please ensure valid values for Gold Price and Exchange Rate.")
