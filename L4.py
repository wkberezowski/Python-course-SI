import requests
import time


def comparison():

    wallet = 8000
    print("I will change the names of stocks markets to numbers for sake of clarity:\n"
          "0. - Bitbay"
          "\n1. - Blockchain"
          "\n2. - Bitstamp"
          "\n3. - CoinBase")
    print(40*"=")

    while True:
        bitbay_ticker = requests.get("https://bitbay.net/API/Public/BTC/ticker.json")
        blockchain_ticker = requests.get("https://blockchain.info/ticker")
        bitstamp_ticker = requests.get("https://www.bitstamp.net/api/ticker/")
        coinbase_buy = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/buy")
        coinbase_sell = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/sell")

        bitbay_taker_fee = 0.0027
        blockchain_taker_fee = 0.0024
        bitstamp_taker_fee = 0.0025
        coinbase_taker_fee = 0.0030

        list_of_bids = [bitbay_ticker.json()["bid"], blockchain_ticker.json()["USD"]["buy"], float(bitstamp_ticker.json()['bid']), float(coinbase_buy.json()['data']['amount'])]
        list_of_asks = [bitbay_ticker.json()["ask"], blockchain_ticker.json()["USD"]["sell"], float(bitstamp_ticker.json()['ask']), float(coinbase_sell.json()['data']['amount'])]

        print("Current wallet {} USD".format(wallet))

        for i in range(len(list_of_asks)):
            count = 0
            if i == 0:
                list_of_asks[i] += (list_of_asks[i] * bitbay_taker_fee)
            elif i == 1:
                list_of_asks[i] += (list_of_asks[i] * blockchain_taker_fee)
            elif i == 2:
                list_of_asks[i] += (list_of_asks[i] * bitstamp_taker_fee)
            elif i == 3:
                list_of_asks[i] += (list_of_asks[i] * coinbase_taker_fee)
            if count != 3:
                for j in range(len(list_of_bids)):
                    if i != j:
                        if list_of_asks[i] < list_of_bids[j]:
                            print("You can buy for less in {} and sell in {}, and you will earn {} USD".format(i, j, round(list_of_bids[j] - list_of_asks[i], 2)))
                            if j == 0:
                                earned_bitbay = (list_of_bids[j] - list_of_asks[i]) - ((list_of_bids[j] - list_of_asks[i]) * bitbay_taker_fee)
                                print("After taker fee you will have {} USD".format(round(earned_bitbay, 2)))
                                wallet += earned_bitbay
                            elif j == 1:
                                earned_blockchain = (list_of_bids[j] - list_of_asks[i]) - ((list_of_bids[j] - list_of_asks[i]) * blockchain_taker_fee)
                                print("After taker fee you will have {} USD".format(round(earned_blockchain, 2)))
                                wallet += earned_blockchain
                            elif j == 2:
                                earned_bitstamp = (list_of_bids[j] - list_of_asks[i]) - ((list_of_bids[j] - list_of_asks[i]) * bitstamp_taker_fee)
                                print("After taker fee you will have {} USD".format(round(earned_bitstamp, 2)))
                                wallet += earned_bitstamp
                            elif j == 3:
                                earned_coinbase = (list_of_bids[j] - list_of_asks[i]) - ((list_of_bids[j] - list_of_asks[i]) * coinbase_taker_fee)
                                print("After taker fee you will have {} USD".format(round(earned_coinbase, 2)))
                                wallet += earned_coinbase
                            print(40*"=")
                        else:
                            print("You wouldn't earn any money buying in {} and selling in {}".format(i, j))
                            print(40*"=")
                        count += 1
        print()
        time.sleep(2.5)


comparison()
