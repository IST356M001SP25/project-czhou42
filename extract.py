import requests
import json
import os
from datetime import datetime

def fetch_price_data(coin_id, days="30"):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {
        "vs_currency": "usd",
        "days": days,
        "interval": "daily"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    os.makedirs("cache", exist_ok=True)
    with open(f"cache/{coin_id}_data.json", "w") as f:
        json.dump(data, f, indent=2)

    return data

if __name__ == "__main__":
    fetch_price_data("bitcoin", "60")
    fetch_price_data("ethereum", "60")
