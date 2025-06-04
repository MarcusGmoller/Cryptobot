import os
import time
import hmac
import hashlib
import base64
from flask import Flask, jsonify
import requests

app = Flask(__name__)
#tester 
# Erstat med dine egne API-oplysninger 
#Lav et getenv miljø 
API_KEY = os.getenv('COINBASE_API_KEY')
API_SECRET = os.getenv('COINBASE_API_SECRET')
API_PASSPHRASE = os.getenv('COINBASE_API_PASSPHRASE')

COINBASE_API_URL = "https://api.pro.coinbase.com"

COINS = ["BTC-USD", "ETH-USD", "LTC-USD", "BCH-USD", "XRP-USD", "EOS-USD", "XTZ-USD", "LINK-USD", "XLM-USD", "ADA-USD"]

def create_auth_headers(timestamp, method, request_path, body=''):
    message = str(timestamp) + method + request_path + (body if body else '')
    hmac_key = base64.b64decode(API_SECRET)
    signature = hmac.new(hmac_key, message.encode(), hashlib.sha256)
    signature_b64 = base64.b64encode(signature.digest()).decode()

    return {
        'CB-ACCESS-SIGN': signature_b64,
        'CB-ACCESS-TIMESTAMP': str(timestamp),
        'CB-ACCESS-KEY': API_KEY,
        'CB-ACCESS-PASSPHRASE': API_PASSPHRASE,
        'Content-Type': 'application/json'
    }

@app.route('/coin-data')
def get_coin_data():
    coin_data = []
    for coin in COINS:
        timestamp = time.time()
        request_path = f"/products/{coin}/ticker"
        headers = create_auth_headers(timestamp, 'GET', request_path)
        response = requests.get(COINBASE_API_URL + request_path, headers=headers)
        if response.status_code == 200:
            coin_data.append(response.json())
        else:
            coin_data.append({"error": f"Failed to fetch data for {coin}"})
    return jsonify(coin_data)

if __name__ == '__main__':
    app.run(debug=True)
