import requests
import datetime
import time
import numpy as np
import matplotlib.pyplot as plt
import statistics


def get_data(crypto):
    now = time.time()
    date = input("Enter date (YYYY-MM-DD): ")
    date_timestamp = time.mktime(datetime.datetime.strptime(date, "%Y-%m-%d").timetuple())
    crypto = requests.get(
        "https://poloniex.com/public?command=returnChartData&currencyPair=BTC_{}&start={}&end={}&period=14400".format(
            crypto, date_timestamp, now))
    return crypto.json()


def model(crypto):
    times = []
    volumes = []
    for item in crypto:
        times.append(datetime.datetime.fromtimestamp(int(item["date"])).strftime("%Y-%m-%d %H:%M:%S"))
        volumes.append(item['volume'])

    model_time = times.copy()
    model_time.append('00:00')

    exp_smoothing = np.zeros(len(volumes) + 1)
    exp_smoothing[0] = volumes[0]
    exp_smoothing[1] = volumes[1]

    alpha = float(input("Enter the alpha value [0, 1]. The higher the better: "))

    for i in range(2, len(model_time)):
        exp_smoothing[i] = alpha * volumes[i - 1] + (1 - alpha) * exp_smoothing[i - 1]

    plt.figure(figsize=(15, 5))
    plt.plot(times, volumes, '-ro', label='Crypto')
    plt.plot(model_time, exp_smoothing, '-go', label="Prediction")
    plt.xticks(times, rotation='vertical')
    plt.ylabel("Volume")
    plt.legend()
    plt.title("Volume prediction")
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
