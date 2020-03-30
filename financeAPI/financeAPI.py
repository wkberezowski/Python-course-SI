import requests


def bitbay_data():
    response = requests.get("https://bitbay.net/API/Public/BTC/orderbook.json")
    return response.json()


def blockchain_data():
    response = requests.get("https://blockchain.info/ticker")
    return response.json()


financial_data_bitbay = bitbay_data()
financial_data_blockchain = blockchain_data()

print('Firs five bid offers for Bitcoin from Bitbay, first number is the exchange rate in USD, second is amount of Bitcoin:')
for arg in financial_data_bitbay['bids'][:5]:
    print(arg)

print("=" * 40)

print('First five ask offers from Bitbay:')
for arg in financial_data_bitbay['asks'][:5]:
    print(arg)

print("=" * 40)

print("Record of Bitcoin pricing from Blockchain, in USD: \n{}".format(financial_data_blockchain['USD']))

print("=" * 40)

if financial_data_bitbay['bids'][0][0] > financial_data_blockchain['USD']['buy']:
    print("It's better to buy Bitcoin from Bitbay at the moment.")
else:
    print("It's better to buy Bitcoin from Blockchain at the moment.")

if financial_data_bitbay['asks'][0][0] > financial_data_blockchain['USD']['sell']:
    print("It's better to sell Bitcoin at Bitbay at the moment.")
else:
    print("It's better to sell Bitcoin at Blockchain at the moment.")
