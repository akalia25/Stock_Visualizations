#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 23:37:01 2019

@author: adityakalia
"""

import yfinance as yf
import pandas as pd

def user_input():
    while True :
        try : 
            stocks =  input("Please enter the stocks you would like to analyze seperated by commas : ")
            if len(stocks) > 0 :
                break
        except :
            pass
        print("Incorrect input please enter your stocks")
    
    return stocks 

def parseStocks(val):
    val = [x.strip(' ') for x in val]
    return val    


def historicalData(stocks):
    df = pd.DataFrame()
    for x in stocks :
        stock = yf.Ticker(x)
        tempdf = stock.history()
        tempdf['StockName'] = x
        df = df.append(tempdf, sort = 'False')
    print(df)

def main():
    stocks = user_input().split(',')
    stocks = parseStocks(stocks)
    historicalData(stocks)
    

    
    
if __name__ == '__main__':
    main()

