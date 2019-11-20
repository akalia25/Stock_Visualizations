#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 23:37:01 2019

@author: adityakalia
"""

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as matdates
import matplotlib as mpl


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
    df = pd.DataFrame()
    for x in stocks:
        stock = yf.Ticker(x)
        tempdf = stock.history(period='3mo')
        tempdf['StockName'] = x
        df = df.append(tempdf, sort='False')
        df['ROI'] = df['Close'].pct_change()
    return df


def stockForecastingMovingAverage(stocks_df):
    """
    This function calculates the stocks Simple Moving Average and Exponential
    Moving Average using the rolling function and the ewm function. It
    calculates for a window of 5,10, and 15 days.
    """
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


def stockBollingerBands(stocks_df):
    """
    This function calculates the upper/middle/lower bound for the bollinger
    bands using a window of 20 days to calculate the STD
    (multiplying by 2 after). Ater calculating the bounds, it plots the data
    using matplotlib.
    """
    uniqueStocks = stocks_df.StockName.unique()
    for stock in uniqueStocks:
        df = stocks_df.loc[stocks_df.StockName == stock]
        df['Middle Bound'] = df['Close'].rolling(window=20).mean()
        df['20std'] = df['Close'].rolling(window=20).std()
        df['Upper Bound'] = df['Middle Bound'] + (df['20std'] * 2)
        df['Lower Bound'] = df['Middle Bound'] - (df['20std'] * 2)
        fig = plt.figure() #
        ax = fig.add_subplot(111)
        #https://stackoverflow.com/a/37219987 reference of the code
        majorFmt = matdates.DateFormatter('%Y-%m-%d %H:%M')
        Daylocator2 =matdates.DayLocator(interval =1)
        ax.xaxis.set_minor_locator(Daylocator2)
        ax.xaxis.set_major_formatter(majorFmt)
        plt.setp(ax.xaxis.get_majorticklabels(),rotation = 45)
        x_axis=df.index.get_level_values('Date')

        ax.fill_between(x_axis, df['Upper Bound'], df['Lower Bound'],\ color='orange')
        ax.plot(x_axis, df['Close'], color='blue', lw=2)
        ax.plot(x_axis, df['Upper Bound'], color='Black', lw=1)
        ax.plot(x_axis, df['Lower Bound'], color='Black', lw=1)
        ax.plot(x_axis, df['Middle Bound'], color='Green', lw=1)

        ax.set_title('Bollinger Bands ' + stock)
        ax.set_xlabel('Date (Year/Month Hour/Minute)')
        ax.set_ylabel('Price')
        ax.legend()
        plt.show();


def main():
    stocks = user_input().split(',')
    stocks = parseStocks(stocks)
    stocks_df = historicalData(stocks)
    stockForecastingMovingAverage(stocks_df)
    stockBollingerBands(stocks_df)

if __name__ == '__main__':
    main()