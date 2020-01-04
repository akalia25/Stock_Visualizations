#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 02:20:38 2020

@author: adityakalia
"""

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as matdates
from scipy.stats import norm
import numpy as np


def user_input():
    """
    This function takes the user's input of what stocks they would like to
    anayze and stores .
    """
    while True:
        try:
            stocks = input("Please enter the stocks you would " +
                           "like to analyze seperated by commas : ")
            if len(stocks) > 0:
                break
        except ValueError:
            pass
        print("Incorrect input please enter your stocks")

    return stocks


def parseStocks(val):
    """
    This function parses the user's input and ensures there are no whitespaces.
    """
    val = [x.strip(' ') for x in val]
    return val


def historicalData(stocks):
    """
    This function uses the Yfinance API and collects the historical data
    of the user inputted and places the data in a dataframe (DF).
    """
    stocks_df = pd.DataFrame()
    for x in stocks:
        try:
            stock = yf.Ticker(x)
            tempdf = stock.history(period='3mo')
            tempdf.loc[:, 'StockName'] = x
            stocks_df = stocks_df.append(tempdf, sort='False')
            stocks_df.loc[:, 'ROI'] = stocks_df['Close'].pct_change()
        except ValueError:
            print("Incorrect stock entered " + x)
            pass
    return stocks_df


def main():
    stocks = user_input().split(',')
    stocks = parseStocks(stocks)
    stocks_df = historicalData(stocks)
    print(stocks_df)

if __name__ == '__main__':
    main()
