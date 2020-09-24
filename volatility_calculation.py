import load_data_test
import config
import requests
import pandas as pd
import numpy as np


def volatility_calculation_(stock_name_lst):
    # TODO: added a full function of volatility calulation rather than
    # TODO: having parts of code all around the places
    string_for_alpaca = ""

    for value in load_data_test.stock_name_list:
        string_for_alpaca = string_for_alpaca + value + ','

    print(string_for_alpaca[:-1])
    sym = string_for_alpaca[:-1]
    print(f'sym: {sym}')
    n = 100

    minute_bars_url = f'{config.BARS_URL}/minute?symbols={sym}&limit={n}'
    five_minutes_url = f'{config.BARS_URL}/5Min?symbols={sym}&limit={n}'
    # fifteen_minute_url = f'{config.BARS_URL}/15Min?symbols={sym}&limit={n}'  # Get 15 minutes candle stick data

    # day_bars_url = '{}/day?symbols={}&limit=5'.format(config.BARS_URL, sym)  # Get daily candle stick data

    # r = requests.get(day_bars_url, headers=config.HEADERS)  # day candle sticks data
    r1 = requests.get(minute_bars_url, headers=config.HEADERS)
    r5 = requests.get(five_minutes_url, headers=config.HEADERS)
    # r15 = requests.get(fifteen_minute_url, headers=config.HEADERS)  # 15 minutes candle stick data

    # data0 = r.json()
    data1 = r1.json()
    data2 = r5.json()
    # data3 = r15.json()

    def volatility_calculation(stock_name):  # This function calculates the volatility of each stock the volatility is
        # used in the fib code to decide if the trade is worth taking or not

        df = pd.DataFrame.from_dict(data1[stock_name])
        z = df["c"]
        q = 0
        b = np.zeros(len(z) - 1)
        while q < len(z) - 1:
            a = (z[q + 1] / z[q]) - 1
            b[q] = a
            q = q + 1

        volatility = b.std() * 100

        load_data_test.Dict_one[stock_name]["volatility"] = volatility
        print(f'Dict_one[stock_name]["volatility"]: {load_data_test.Dict_one[stock_name]["volatility"]}')

        df = pd.DataFrame.from_dict(data2[stock_name])
        z = df["c"]
        q = 0
        b = np.zeros(len(z) - 1)
        while q < len(z) - 1:
            a = (z[q + 1] / z[q]) - 1
            b[q] = a
            q = q + 1

        volatility = b.std() * 100

        # print(f'volatility of {stock_name}: {volatility}')

        load_data_test.Dict_five[stock_name]["volatility"] = volatility
        print(f'Dict_five[stock_name]["volatility"]: of {stock_name} - '
              f'{load_data_test.Dict_five[stock_name]["volatility"]}')

    def volatality_calculation_function(stock_names):
        # print("Heya")  # print statement for debugging purposes
        for stock in stock_names:
            volatility_calculation(stock)
            print(f'Dict_five: {load_data_test.Dict_five}')
            print(f'Dict_one: {load_data_test.Dict_one}')

    volatality_calculation_function(stock_name_lst)


# volatility_calculation_(load_data_test.stock_name_list)
# print(f'load_data_test.Dict_five: {load_data_test.Dict_five}')
