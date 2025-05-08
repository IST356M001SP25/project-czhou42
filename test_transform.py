from transform import load_price_data

def test_load_price_data():
    df = load_price_data("cache/bitcoin_data.json")
    assert not df.empty
    assert "price" in df.columns
    assert "date" in df.columns
