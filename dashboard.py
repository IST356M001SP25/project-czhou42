import streamlit as st
import pandas as pd
from transform import load_price_data

st.title("📈 Cryptocurrency Price Analyzer")

coin = st.selectbox("Choose a Coin", ["bitcoin", "ethereum"])
df = load_price_data(f"cache/{coin}_data.json")

st.line_chart(df.set_index("date")["price"])

st.write("### Raw Data")
st.dataframe(df.head(10))
