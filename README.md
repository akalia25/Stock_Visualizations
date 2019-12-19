# Stock_Analysis
Abstract: The purpose of this script is to conduct statistical/Visualization/Forecasting analysis on stocks. The script runs by asking the user for the list of stocks they would like analyzed.

Running this Script: To run this script simply download and execute the python file, and ensure that you have required modules installed (For yfinance installation use (pip install yfinance)) 

The Stock analysis done by the program are discussed below with outputs from the program:


This script provides the user with the stocks Simple Moving Average (SMA), Exponential Moving Average (EMA), and cacluclates the bollinger bands (see image referenced below). 

![alt text](https://github.com/akalia25/Stock_Analysis/blob/master/Screenshots/bollinger_band.png)


For the stocks entered by the user, the program calculates the covariance(how related the stocks are to each other, value of 0 meaning no relation, and a postive number indicating a postive relation in the same direction) and correlation(a standardized value of the direction and strength between the stocks, its is measured between [-1, +1] ) between the stocks.

![alt text](https://github.com/akalia25/Stock_Analysis/blob/master/Screenshots/Covariance%26Correlation.png)


The program calculates the normalized closing prices for the stocks entered and compares it against the market (SPY), this information is then plotted on the same axis

![alt text](https://github.com/akalia25/Stock_Analysis/blob/master/Screenshots/Stock%20Comparison%20to%20Market.png)


For all the stocks entered, the program plots the Simple Moving Average of 5,10,15 days on the same plot as the stock's close price to show how close the moving averages are to the actual stock price (used to determine stock volatility). 

![alt text](https://github.com/akalia25/Stock_Analysis/blob/master/Screenshots/SMA_Plot.png)

For all the stocks entered, the program plots the Exponential Moving Average of 5,10,15 days on the same plot as the stock's close price.

![alt text](https://github.com/akalia25/Stock_Analysis/blob/master/Screenshots/EMA_Plot.png)

**The difference between the Simple Moving Average(SMA) and Exponential Moving Average(EMA), is that EMA places higher weighting towards recent stock prices, whereas the SMA applies equal weighting for all stock prices.
