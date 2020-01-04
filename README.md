# Stock_Visualizations

### Abstract:
The purpose of this script is to provide in-depth visualizations on stocks that utilize statistical/Forecasting methods, and can assist the user in making stock related decisons(Buy, Sell, Hold). The script runs by asking the user for the list of stocks they would like analyzed and generates various powerful visualizations for the user.

### Running this Script:
To run this script simply download and execute the python file, and ensure that you have required modules installed (For yfinance installation use (pip install yfinance))

### The Stock analysis done by the script are discussed below with outputs from the program:

#### Simple Moving Average + Exponential Moving Average
For all the stocks entered, the script plots the Simple Moving Average(SMA) of 5,10,15 days on the same plot as the stock's close price to show how close the moving averages are to the actual stock price (used to determine stock volatility). 

![alt text](https://github.com/akalia25/Stock_Analysis/blob/master/Screenshots/SMA_Plot.png)

For all the stocks entered, the program plots the Exponential Moving Average(EMA) of 5,10,15 days on the same plot as the stock's close price.

![alt text](https://github.com/akalia25/Stock_Analysis/blob/master/Screenshots/EMA_Plot.png)

**The difference between the Simple Moving Average(SMA) and Exponential Moving Average(EMA), is that EMA places higher weighting towards recent stock prices, whereas the SMA applies equal weighting for all stock prices.

#### Bollinger Bands Visualization
The script conducts techcnial analysis by calculating the upper, lower, and middle bands on each stock.

The **lower and upper band** is calculated by taking 2 standard deviations from a 20-day Simple Moving Average of the stock's close price.

The **middle band** is the stock's Simple Moving Average of a 20-day period

Combining the upper, lower, and middle bands the Bollinger Bands visualization is created. 

![alt text](https://github.com/akalia25/Stock_Analysis/blob/master/Screenshots/bollinger_band.png)

#### Covariance + Correlation between Stocks
For the stocks entered by the user, the scripts calculates the **covariance**(how related the stocks are to each other, value of 0 meaning no relation, and a postive number indicating a postive relation in the same direction)

**correlation**(a standardized value of the direction and strength between the stocks, its is measured between [-1, +1] ) between the stocks.

![alt text](https://github.com/akalia25/Stock_Analysis/blob/master/Screenshots/Covariance%26Correlation.png)

#### Comparision Against Market Analysis 
The script calculates the **normalized closing prices**(Xn / Xn-1) for the stocks entered and compares it against the market (SPY), this information is then plotted on the same axis

![alt text](https://github.com/akalia25/Stock_Analysis/blob/master/Screenshots/Stock%20Comparison%20to%20Market.png)

#### Error Bar Plot with Standard Deviation
Using the last 30-days of data for each stock, the stock's closing price is used to calculate standard deviation. This standard deviation value becomes the error value for the error bar plot. The stock's closing price as well as the error-bar is plotted to measure potential volatility with the stock's closing price 

![alt text](https://github.com/akalia25/Stock_Analysis/blob/master/Screenshots/Error_Bar_Plot.png)
