#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 23:37:01 2019

@author: adityakalia
"""

import yfinance as yf
import pandas as pd


def user_input():
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
    val = [x.strip(' ') for x in val]
    return val


def historicalData(stocks):
    df = pd.DataFrame()
    for x in stocks:
        stock = yf.Ticker(x)
        tempdf = stock.history()
        tempdf['StockName'] = x
        df = df.append(tempdf, sort='False')
        df['ROI'] = df['Close'].pct_change()
    return df


def stockForecastingMovingAverage(stocks_df):
    uniqueStocks = stocks_df.StockName.unique()
    for stock in uniqueStocks:
        df1 = stocks_df.loc[stocks_df.StockName == stock]
        df1.reset_index(inplace=True)
        data = df1[['Date','Close']]
        for i in (5, 10, 15):
            simple_moving_average = data.set_index('Date').rolling(window=i).mean()
            df1['SMA ' + str(stock) + ' ' + str(i)] = simple_moving_average.values
        for i in (5, 10, 15):
            exponential_moving_average = data.set_index('Date').ewm(span=i, adjust=False).mean()
            df1['EMA ' + str(stock) + ' ' + str(i)] = exponential_moving_average.values
        print(df1)

def main():
    stocks = user_input().split(',')
    stocks = parseStocks(stocks)
    stocks_df = historicalData(stocks)
    stockForecastingMovingAverage(stocks_df)

if __name__ == '__main__':
    main()