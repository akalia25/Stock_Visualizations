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
            stocks =  input("Please enter the risk level from 1 (Low Risk) or 2 (Med Risk) or 3 (High Risk) you would like to take on from your portfolio : ")
            if int(risk) > 0 and int(risk) <=3 :
                break
        except :
            pass
        print("Incorrect input please enter risk level between 1-3")
    
    return stocks
