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

selected_coin = st.selectbox(
    "Velg kryptovaluta",
    df["Coin"]
)

st.dataframe(
    df.sort_values("24t %", ascending=False),
    width="stretch"
)

coin_info = df[df["Coin"] == selected_coin].iloc[0]

st.divider()

st.subheader(f"📈 {selected_coin}")

st.subheader("🎯 Mine prisområder")

kjop_nedre = st.number_input(
    "Kjøpsområde fra",
    min_value=0.0,
    value=0.0
)

kjop_ovre = st.number_input(
    "Kjøpsområde til",
    min_value=0.0,
    value=0.0
)

salg_nedre = st.number_input(
    "Salgsområde fra",
    min_value=0.0,
    value=0.0
)

salg_ovre = st.number_input(
    "Salgsområde til",
    min_value=0.0,
    value=0.0
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Pris (NOK)",
        f"{coin_info['Pris (NOK)']:,.2f}"
    )

with col2:
    st.metric(
        "24t Endring",
        f"{coin_info['24t %']}%"
    )

pris = coin_info["Pris (NOK)"]

if kjop_nedre <= pris <= kjop_ovre:
    st.success(
        "🟢 Kursen ligger innenfor kjøpsområdet ditt"
    )

elif salg_nedre <= pris <= salg_ovre:
    st.warning(
        "🔴 Kursen ligger innenfor salgsområdet ditt"
    )

else:
    st.info(
        "⚪ Kursen ligger utenfor områdene dine"
    )

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