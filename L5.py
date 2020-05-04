import requests
import time
import sys


def max_profit(amount):
    while True:
        list_of_diffs = []
        all_profit = 0

        ETH = requests.get("https://bitbay.net/API/Public/ETH/ticker.json")
        BTC = requests.get("https://bitbay.net/API/Public/BTC/ticker.json")
        XRP = requests.get("https://bitbay.net/API/Public/XRP/ticker.json")
        LTC = requests.get("https://bitbay.net/API/Public/LTC/ticker.json")
        BCC = requests.get("https://bitbay.net/API/Public/BCC/ticker.json")

        list_of_names_json = [ETH.json(), BTC.json(), XRP.json(), LTC.json(), BCC.json()]
        list_of_strings = ["ETH", "BTC", "XRP", "LTC", "BCC"]

        print("Your budget is now {}".format(amount))

        for element in list_of_names_json:
            if element['volume'] != 0:
                formula = round(((element['max'] - element['min']) / element['min']) * 100, 2)
                list_of_diffs.append(formula)
                name_index = list_of_names_json.index(element)
                name = list_of_strings[name_index]
                if amount > 0:
                    if element['volume'] * element['min'] < amount:
                        amount -= element['volume'] * element['min']
                        profit = (element['max'] - element['min']) * element['volume']
                        all_profit += profit
                        print("{} of {} can be bought".format(element['volume'] * element['min'], name))
                        print("Your profit is now {}".format(all_profit))
                        print("You now have {} USD".format(amount))
                    else:
                        profit = (element['max'] - element['min']) * (amount/element['min'])
                        print("{} of {} can be bought".format(amount / (element['volume'] * element['min']), name))
                        all_profit += profit
                        print("Your profit is now {}".format(all_profit))
                        print("You now have {} USD".format(amount))
                        amount = 0
                else:
                    print("You don't have any money")
                    sys.exit()
            else:
                print("This resource is not available right now")

        for k in range(len(list_of_diffs)):
            if list_of_diffs[k] > 0:
                print("{} +{}%".format(list_of_strings[k], list_of_diffs[k]))
            elif list_of_diffs[k] < 0:
                print("{} -{}%".format(list_of_strings[k], list_of_diffs[k]))
            else:
                print("{} {}%".format(list_of_strings[k], list_of_diffs[k]))

        print(40*"=")
        time.sleep(300)


max_profit(200000)
