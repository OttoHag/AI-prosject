import requests
import pandas as pd
import streamlit as st

st.set_page_config(page_title="KryptoRadar AI", layout="wide")

st.title("🚀 KryptoRadar AI")

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "nok",
    "order": "market_cap_desc",
    "per_page": 20,
    "page": 1,
    "sparkline": False
}

response = requests.get(url, params=params)
coins = response.json()

data = []

for coin in coins:
    data.append({
        "Coin": coin["name"],
        "Symbol": coin["symbol"].upper(),
        "Pris (NOK)": round(coin["current_price"], 2),
        "24t %": round(coin["price_change_percentage_24h"], 2)
    })

df = pd.DataFrame(data)

st.subheader("Top 20 kryptovalutaer")

st.dataframe(
    df.sort_values("24t %", ascending=False),
    use_container_width='stretch'
)

# SIDEPANEL

st.sidebar.title("📊 Markedsoversikt")

st.sidebar.subheader("🏆 Dagens vinnere")

vinnere = df.sort_values("24t %", ascending=False).head(3)

for _, row in vinnere.iterrows():
    st.sidebar.success(
        f"{row['Coin']} ({row['Symbol']}) : {row['24t %']}%"
    )



st.sidebar.subheader("💀 Dagens tapere")

tapere = df.sort_values("24t %", ascending=True).head(3)

for _, row in tapere.iterrows():
    st.sidebar.error(
        f"{row['Coin']} ({row['Symbol']}) : {row['24t %']}%"
    )



st.sidebar.subheader("⭐ Populære")

populære = df[df["Coin"].isin([
    "Bitcoin",
    "Ethereum",
    "Ripple"
])]

for _, row in populære.iterrows():
    st.sidebar.info(
        f"{row['Coin']} ({row['Symbol']}) : {row['24t %']}%"
    )