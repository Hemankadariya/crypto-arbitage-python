import requests
import smtplib

# Set up email credentials
sender_email = "your_email_address@gmail.com"
sender_password = "your_email_password"
receiver_email = "recipient_email_address@gmail.com"

# Set up Binance API credentials
binance_api_key = "your_binance_api_key"
binance_secret_key = "your_binance_secret_key"

# Set up KuCoin API credentials
kucoin_api_key = "your_kucoin_api_key"
kucoin_secret_key = "your_kucoin_secret_key"
kucoin_passphrase = "your_kucoin_passphrase"

# Set up Hotbit API credentials
hotbit_api_key = "your_hotbit_api_key"
hotbit_secret_key = "your_hotbit_secret_key"

# Set up Coinspot API credentials
coinspot_api_key = "your_coinspot_api_key"
coinspot_secret_key = "your_coinspot_secret_key"

# Set up PancakeSwap URL
pancakeswap_url = "https://api.pancakeswap.com/api/v1/price?symbol=your_token_symbol"

# Get prices from all exchanges
binance_price = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol=your_token_symbolUSDT&apikey={binance_api_key}&secret={binance_secret_key}").json()["price"]
kucoin_price = requests.get(f"https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=your_token_symbol-USDT&apikey={kucoin_api_key}&secret={kucoin_secret_key}&passphrase={kucoin_passphrase}").json()["data"]["price"]
hotbit_price = requests.get(f"https://api.hotbit.io/api/v1/ticker?market=your_token_symbol/USDT&apikey={hotbit_api_key}&secret={hotbit_secret_key}").json()["result"]["last"]
coinspot_price = requests.get(f"https://www.coinspot.com.au/pubapi/v3/markets/data/ticker?c=your_token_symbol&a=USDT&apikey={coinspot_api_key}&secret={coinspot_secret_key}").json()["last"]
pancakeswap_price = requests.get(pancakeswap_url).json()["price"]

# Compare prices and send email if there's a 5% difference
if abs((binance_price - kucoin_price) / binance_price) >= 0.05 or abs((binance_price - hotbit_price) / binance_price) >= 0.05 or abs((binance_price - coinspot_price) / binance_price) >= 0.05 or abs((binance_price - pancakeswap_price) / binance_price) >= 0.05:
    message = f"Subject: Alert: Price difference detected for your_token_symbol!\n\nBinance: {binance_price}\nKuCoin: {kucoin_price}\nHotbit: {hotbit_price}\nCoinspot: {coinspot_price}\nPancakeSwap: {pancakeswap_price}"
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)
