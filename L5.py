import requests
import time


def max_profit(amount):
    while True:
        list_of_diffs = []
        ETH = requests.get("https://bitbay.net/API/Public/ETH/ticker.json")
        BTC = requests.get("https://bitbay.net/API/Public/BTC/ticker.json")
        GAME = requests.get("https://bitbay.net/API/Public/GAME/ticker.json")
        LTC = requests.get("https://bitbay.net/API/Public/LTC/ticker.json")
        BCC = requests.get("https://bitbay.net/API/Public/BCC/ticker.json")

        list_of_names = [ETH, BTC, GAME, LTC, BCC]
        list_of_names_json = [ETH.json(), BTC.json(), GAME.json(), LTC.json(), BCC.json()]
        list_of_strings = ["ETH", "BTC", "GAME", "LTC", "BCC"]

        for i in list_of_names:
            formula = round(((i.json()['max'] - i.json()['min']) / i.json()['min']) * 100, 2)
            list_of_diffs.append(formula)

        for k in range(len(list_of_diffs)):
            if list_of_diffs[k] > 0:
                print("{} +{}%".format(list_of_strings[k], list_of_diffs[k]))
            elif list_of_diffs[k] < 0:
                print("{} -{}%".format(list_of_strings[k], list_of_diffs[k]))
            else:
                print("{} {}%".format(list_of_strings[k], list_of_diffs[k]))

        for element in list_of_names_json:
            if amount > 0:
                if element['volume'] * element['min'] < amount:
                    amount -= element['volume'] * element['min']
                    name_index = list_of_names_json.index(element)
                    name = list_of_strings[name_index]
                    print("{} of {} can be bought".format(element['volume'] * element['min'], name))
                    print("You now have {} USD".format(amount))
            elif amount == 0:
                print("You don't have any money left")

        print(40*"=")
        time.sleep(300)


max_profit(10000)
