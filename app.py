import requests

# CoinGecko API
url = "https://api.coingecko.com/api/v3/simple/price"

params = {
"ids": "bitcoin,ethereum,solana,ripple,dogecoin,cardano,polkadot,chainlink,litecoin",
"vs_currencies": "nok",
"include_24hr_change": "true"
}

response = requests.get(url, params=params)

# Gjør om svaret til Python-data
data = response.json()

# Hent priser
bitcoin_price = data.get("bitcoin", {}).get("nok")
ethereum_price = data.get("ethereum", {}).get("nok")
solana_price = data.get("solana", {}).get("nok")
ripple_price = data.get("ripple", {}).get("nok")
dogecoin_price = data.get("dogecoin", {}).get("nok")
cardano_price = data.get("cardano", {}).get("nok")
polkadot_price = data.get("polkadot", {}).get("nok")
chainlink_price = data.get("chainlink", {}).get("nok")
litecoin_price = data.get("litecoin", {}).get("nok")


# Hent endring siste 24 timer
bitcoin_change = data.get("bitcoin", {}).get("nok_24h_change")
ethereum_change = data.get("ethereum", {}).get("nok_24h_change")
solana_change = data.get("solana", {}).get("nok_24h_change")
ripple_change = data.get("ripple", {}).get("nok_24h_change")
dogecoin_change = data.get("dogecoin", {}).get("nok_24h_change")
cardano_change = data.get("cardano", {}).get("nok_24h_change")
polkadot_change = data.get("polkadot", {}).get("nok_24h_change")
chainlink_change = data.get("chainlink", {}).get("nok_24h_change")
litecoin_change = data.get("litecoin", {}).get("nok_24h_change")

# Funksjon som gir en enkel vurdering
def vurder_coin(change):
    if change is None:
        return "❓ Ingen data"

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

print(f"Bitcoin")
print(f"Pris: {bitcoin_price:,.0f} NOK")
print(f"24t endring: {bitcoin_change:.2f}%")
print(f"AI vurdering: {vurder_coin(bitcoin_change)}")

print()

print(f"Ethereum")
print(f"Pris: {ethereum_price:,.0f} NOK")
print(f"24t endring: {ethereum_change:.2f}%")
print(f"AI vurdering: {vurder_coin(ethereum_change)}")

print()

print(f"Solana")
print(f"Pris: {solana_price:,.0f} NOK")
print(f"24t endring: {solana_change:.2f}%")
print(f"AI vurdering: {vurder_coin(solana_change)}")

print()

print(f"Ripple")
print(f"Pris: {ripple_price:,.0f} NOK")
print(f"24t endring: {ripple_change:.2f}%")
print(f"AI vurdering: {vurder_coin(ripple_change)}")

print()

print(f"Dogecoin")
print(f"Pris: {dogecoin_price:,.0f} NOK")
print(f"24t endring: {dogecoin_change:.2f}%")
print(f"AI vurdering: {vurder_coin(dogecoin_change)}")

print()

print(f"Cardano")
print(f"Pris: {cardano_price:,.0f} NOK")
print(f"24t endring: {cardano_change:.2f}%")
print(f"AI vurdering: {vurder_coin(cardano_change)}")

print()

print(f"Polkadot")
print(f"Pris: {polkadot_price:,.0f} NOK")
print(f"24t endring: {polkadot_change:.2f}%")
print(f"AI vurdering: {vurder_coin(polkadot_change)}")

print()

print(f"Chainlink")
print(f"Pris: {chainlink_price:,.0f} NOK")
print(f"24t endring: {chainlink_change:.2f}%")
print(f"AI vurdering: {vurder_coin(chainlink_change)}")

print()

print(f"Litecoin")
print(f"Pris: {litecoin_price:,.0f} NOK")
print(f"24t endring: {litecoin_change:.2f}%")
print(f"AI vurdering: {vurder_coin(litecoin_change)}")