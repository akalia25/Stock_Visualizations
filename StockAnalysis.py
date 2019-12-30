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


def stockForecastingMovingAverage(stocks_df):
    """
    This function calculates the stocks Simple Moving Average and Exponential
    Moving Average using the rolling function and the ewm function. It
    calculates for a window of 5,10, and 15 days. Returns a large DataFrame
    that has all moving averages for all stocks entered
    """
    uniqueStocks = stocks_df.StockName.unique()
    MovingAverageDF = stocks_df
    for stock in uniqueStocks:
        df1 = stocks_df.loc[stocks_df.StockName == stock]
        df1.reset_index(inplace=True)
        data = df1[['Date', 'Close']]
        for i in (5, 10, 15):
            simple_moving_average = data.set_index(
                    'Date').rolling(window=i).mean()
            df1.loc[:, 'SMA ' + str(stock) + ' ' + str(
                    i)] = simple_moving_average.values
        for i in (5, 10, 15):
            exponential_moving_average = data.set_index(
                    'Date').ewm(span=i, adjust=False).mean()
            df1.loc[:, 'EMA ' + str(stock) + ' ' + str(
                    i)] = exponential_moving_average.values
        df1 = df1.set_index('Date')
        smaPlotdf = df1.filter(regex='\ASMA')
        smaPlotdf.loc[:, 'Close'] = df1.Close
        ax1 = smaPlotdf.plot(legend=True, grid=True,
                   title='Simple Moving Average Plot of ' + stock)
        ax1.set_ylabel('Stock Price')
        ax1.set_xlabel('Date')
        emaPlotdf = df1.filter(regex='\AEMA')
        emaPlotdf.loc[:, 'Close'] = df1.Close
        ax2 = emaPlotdf.plot(legend=True, grid=True,
                   title='Exponential Moving Average Plot of ' + stock)
        ax2.set_ylabel('Stock Price')
        ax2.set_xlabel('Date')

        MovingAverageDF = pd.concat([df1, MovingAverageDF])
    return MovingAverageDF


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
        df.loc[:, 'Middle Bound'] = df['Close'].rolling(window=20).mean()
        df.loc[:, '20std'] = df['Close'].rolling(window=20).std()
        df.loc[:, 'Upper Bound'] = df['Middle Bound'] + (df['20std'] * 2)
        df.loc[:, 'Lower Bound'] = df['Middle Bound'] - (df['20std'] * 2)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        # https://stackoverflow.com/a/37219987 reference of the code
        majorFmt = matdates.DateFormatter('%Y-%m-%d %H:%M')
        Daylocator2 = matdates.DayLocator(interval=1)
        ax.xaxis.set_minor_locator(Daylocator2)
        ax.xaxis.set_major_formatter(majorFmt)
        plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)
        x_axis = df.index.get_level_values('Date')
        ax.fill_between(x_axis, df['Upper Bound'], df['Lower Bound'],
                        color='orange')
        ax.plot(x_axis, df['Close'], color='blue', lw=2)
        ax.plot(x_axis, df['Upper Bound'], color='Black', lw=1)
        ax.plot(x_axis, df['Lower Bound'], color='Black', lw=1)
        ax.plot(x_axis, df['Middle Bound'], color='Green', lw=1)
        ax.set_title('Bollinger Bands ' + stock)
        ax.set_xlabel('Date (Year/Month Hour/Minute)')
        ax.set_ylabel('Price')
        ax.legend()
        plt.show()


def CovarianceCorrelation(stocks_df):
    """
    Covariance measures how related the stocks are to each other, value
    of 0 meaning no relation, and a positive number indicating a positive
    relation in the same direction.
    Correlation measures a standarized value of the direction and strength
    between the stocks, it is measured between -1 to +1.
    """
    returns = stocks_df[['ROI', 'StockName']]
    returns = returns.pivot(columns='StockName', values='ROI')
    cov = returns.cov()
    print("The Covariance matrix is ")
    print(cov.rename_axis(None))
    corr = returns.corr()
    print("\n The Correlation matrix is ")
    print(corr.rename_axis(None))
    return cov, corr


def MarketComparison(stocks_df):
    """
    This function takes the users stocks and caculates the normalized returns,
    with the normalized returns, it maps it on the same plot as the noramlized
    returns on the market to provide a comparison on returns
    against the market.
    """
    norm = stocks_df.loc[:, ['StockName', 'Close']]
    norm = norm.pivot(index=norm.index, columns='StockName')
    norm = norm/norm.iloc[0]
    norm.columns = norm.columns.droplevel()
    marketVal = yf.Ticker('SPY')
    df1 = marketVal.history(period='1y')
    marketDF = df1.loc[:, ['Close']]
    marketDF = marketDF.rename(columns={'Close': 'SPY Market'})
    marketDF = marketDF/marketDF.iloc[0]
    norm['SPY Market'] = marketDF
    ax = norm.plot(legend=True, grid=True,
                   title='Stock Performance VS. Market(SPY)')
    ax.set_ylabel('Normalized Price')
    ax.set_xlabel('Date')
    plt.show()


def StandardDev(stocks_df):
    """
    This function takes input of the stocks dataframe and calculates the
    standard deviation of each stock for its 30 day closing price period
    using this standard deviation value the script creates a plot of the
    stock's closing price with an error bar equivalent to the standard
    deviation showing the closing price's possible voltaility.
    """
    for stock in stocks_df.StockName.unique():
        df = stocks_df['Close'][(stocks_df.StockName == stock)][-30:]
        std_Val = df.std()

        fig = plt.figure()
        ax = fig.add_subplot(111)
        majorFmt = matdates.DateFormatter('%Y-%m-%d')
        Daylocator2 = matdates.DayLocator(interval=1)
        ax.xaxis.set_minor_locator(Daylocator2)
        ax.xaxis.set_major_formatter(majorFmt)
        plt.setp(ax.xaxis.get_majorticklabels(), rotation=90)

        ax.set_xlabel('Date')
        ax.set_ylabel('Price')
        ax.set_title(stock + ' CLose Price With Error Bar  ')

        xaxis = df.index.get_level_values('Date')
        ax.errorbar(xaxis, df.values, yerr=std_Val, label=stock)
        ax.grid(color='lightgrey', linestyle='-')
        ax.set_facecolor('w')

        plt.show()


def StockAppraisal(stocks_df):
    """
    The function takes in the stocks dataframe and using
    analytical techniques calculates whether the stock should
    be bought or sold
    """
    stockAppraisal = {}
    for stock in stocks_df.StockName.unique():
        df = stocks_df['Close'][(stocks_df.StockName == stock)][-30:]
        zVal = zValue(df)
        stockAppraisal[stock] = zVal


def zValue(series):
    """
    This function takes a series as input and calculates the standard
    deviation, mean, and uses the series last stock price as the x value
    using these values it calculates the z value
    """
    meanVal = series.mean()
    stdVal = series.std()
    mu = series[-1]
    z1 = (mu - meanVal) / stdVal
    x = np.arange(-4, z1, 0.01)
    y = norm.pdf(x, 0, 1)
    # build the plot
    fig, ax = plt.subplots(figsize=(9, 6))
    plt.style.use('fivethirtyeight')

    ax.fill_between(x, y, -1, alpha=0.3, color='b')
    ax.set_xlim([-4, 4])
    ax.set_ylim(0)
    ax.set_xlabel('# of Standard Deviations Outside the Mean')
    ax.set_yticklabels([])
    ax.set_title('Normal Gaussian Curve')

    plt.savefig('normal_curve.png', dpi=72, bbox_inches='tight')
    plt.show()


def main():
    stocks = user_input().split(',')
    stocks = parseStocks(stocks)
    stocks_df = historicalData(stocks)
    stockForecastingMovingAverage(stocks_df)
    stockBollingerBands(stocks_df)
    CovarianceCorrelation(stocks_df)
    MarketComparison(stocks_df)
    StandardDev(stocks_df)


if __name__ == '__main__':
    main()
