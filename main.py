import requests
import datetime
import time
import statistics
import pandas as pd
import matplotlib.pyplot as plt


def get_data(crypto):
    now = time.time()
    date = "2020-05-01"
    date_timestamp = time.mktime(datetime.datetime.strptime(date, "%Y-%m-%d").timetuple())
    crypto = requests.get(
        "https://poloniex.com/public?command=returnChartData&currencyPair=BTC_{}&start={}&end={}&period=14400".format(
            crypto, date_timestamp, now))
    return crypto.json()


def model(crypto):
    volumes = []
    for item in crypto:
        volumes.append(item['volume'])

    window_size = 3
    numbers_series = pd.Series(volumes)
    windows = numbers_series.rolling(window_size)
    moving_averages = windows.mean()

    plt.figure(figsize=(15, 5))
    plt.plot(volumes, '-m', label='crypto')
    plt.plot(moving_averages, '-b', label='simulation')
    plt.xlabel("Number of days")
    plt.legend()
    plt.show()


def stats(crypto):
    volumes = []
    list_of_growths = []
    list_of_declines = []

    for item in crypto:
        volumes.append(item['volume'])

    for i in range(len(volumes) - 1):
        if volumes[i] > volumes[i + 1]:
            list_of_declines.append(volumes[i])
        elif volumes[i] < volumes[i + 1]:
            list_of_growths.append(volumes[i])

    growth_mean = statistics.mean(list_of_growths)
    decline_mean = statistics.mean(list_of_declines)

    growth_median = statistics.median(list_of_growths)
    decline_median = statistics.median(list_of_declines)

    st_dev_growth = statistics.stdev(list_of_growths)
    st_dev_decline = statistics.stdev(list_of_declines)

    print("Statistics for inclines and declines respectively:\n"
          "Means: {}, {}\n"
          "Medians: {}, {}\n"
          "Standard deviation: {}, {}".format(round(growth_mean, 2), round(decline_mean, 2),
                                              round(growth_median, 2), round(decline_median, 2),
                                              round(st_dev_growth, 2), round(st_dev_decline, 2)))


name = input("Choose your crypto (ETC, DASH, XMR): ").upper()

crypto = get_data(name)
model(crypto)
stats(crypto)
