def get_exchange_rate():
    url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_API_KEY}/latest/USD"
    response = requests.get(url)
    try:
        data = response.json()
        exchange_rate = data['conversion_rates']['GHS']
        return exchange_rate
    except Exception as e:
        st.error(f"API Error: {e}, Response: {response.text}")
        return None
