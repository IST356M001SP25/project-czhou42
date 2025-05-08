import json
import pandas as pd

def load_price_data(filepath):
    with open(filepath) as f:
        raw = json.load(f)

    prices = raw["prices"]
    df = pd.DataFrame(prices, columns=["timestamp", "price"])
    df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.drop("timestamp", axis=1, inplace=True)
    return df

if __name__ == "__main__":
    btc = load_price_data("cache/bitcoin_data.json")
    eth = load_price_data("cache/ethereum_data.json")
    btc.to_csv("cache/bitcoin_clean.csv", index=False)
    eth.to_csv("cache/ethereum_clean.csv", index=False)
