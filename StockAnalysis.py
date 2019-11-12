#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 23:37:01 2019

@author: adityakalia
"""

import yfinance as yf

def user_Stocks():
    while True :
        try : 
            stocks =  input("Please enter the stocks you would like to analyze seperated by commas : ")
            if len(stocks) > 0 :
                break
        except :
            pass
        print("Incorrect input please enter your stocks")
    
    return stocks
<<<<<<< HEAD
 

stocks = user_Stocks().split(',')

stocks = [x.strip(' ') for x in stocks]
    
print(stocks)


#def parseStocks(stocks):
        
=======
>>>>>>> ac1540cfa537338700259b729e1b742591bce57c
