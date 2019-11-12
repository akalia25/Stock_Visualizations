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
 

    