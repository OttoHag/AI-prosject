import requests

# CoinGecko API
url = "https://api.coingecko.com/api/v3/simple/price"

coins = [
    "bitcoin",
    "ethereum",
    "ripple",
    "solana",
    "cardano",
    "dogecoin",
    "polkadot",
    "chainlink",
    "litecoin"
]

params = {
    "ids": ",".join(coins),
    "vs_currencies": "nok",
    "include_24hr_change": "true"
}

response = requests.get(url, params=params)
data = response.json()


def vurder_coin(change):
    if change >= 5:
        return "🚀 Sterkt kjøpssignal"

    elif change >= 2:
        return "🟢 Positiv trend"

    elif change >= 0:
        return "✅ Svak oppgang"

    elif change >= -2:
        return "⚠️ Følg med"

    else:
        return "🔴 Negativ trend"


print("\n=== KryptoRadar AI ===\n")

for coin in coins:

    pris = data.get(coin, {}).get("nok")
    endring = data.get(coin, {}).get("nok_24h_change")

    print(f"{coin.upper()}")
    print(f"Pris: {pris:,.0f} NOK")
    print(f"24t endring: {endring:.2f}%")
    print(f"AI vurdering: {vurder_coin(endring)}")
    print("-" * 30)