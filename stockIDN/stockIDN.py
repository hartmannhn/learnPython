#=======================================================================
# stockIDN
#=======================================================================
#
#       script to pull specific stock price data from chosen source. 
#       currently for Indonesian Stock only.
#
#       author : @hartmannhn
#
#=======================================================================

#=======================================================================
# Library Used
#=======================================================================

import math
import pandas_datareader as pdr
import pandas as pd
#import matplotlib.pyplot as plt

#========initial setting for source and date range==========
source = 'yahoo'
startDate = '2015-01-01'
endDate = '2021-01-01'
name = 'Adj Close'
#===========================================================

print('Please input your Indonesian stock ticker code: ',end='')
ticker = input()
ticker = ticker + '.JK'

closePrice = pdr.DataReader(ticker,data_source=source,start=startDate,end=endDate)[name]

year = list(range(int(startDate[:4]),(int(endDate[:4]))))

#========function to calculate parameters================
def totalReturn(price):
    return (price[-1]/price[0])-1

def byYear(year,price):
    priceByYear = {}
    for item in year:
        priceByYear[item] = price[(str(item)+'-01-01'):(str(item)+'-12-31')]
    return priceByYear

closePricePerYear = byYear(year,closePrice)
tickerDailyChange = (closePrice/closePrice.shift(1))-1
tickerDailyChangePerYear = byYear(year,tickerDailyChange)

dailyPriceVolatility = {}
annualPriceVolatility = {}
annualReturnPerYear = {}
for item in year:
    dailyPriceVolatility[item] = tickerDailyChangePerYear[item].std()
    annualPriceVolatility[item] = (dailyPriceVolatility[item])*(math.sqrt(len(tickerDailyChangePerYear[item])))
    annualReturnPerYear[item] = totalReturn(closePricePerYear[item])
tickerTotalReturn = totalReturn(closePrice)

#========function to display basic pull data================    
def showInfo(price):
    global year
    global dailyPriceVolatility
    global annualPriceVolatility
    global annualReturnPerYear
    global tickerTotalReturn
    print('total of stock price data record found: %s' %len(price))
    print('total return: %.2f%% \n' %(tickerTotalReturn*100))
    print('per year basis:')
    print('year\trecord\treturn\tdaily volat\tannual volatility')
    for item in year:
        print('%d\t%d\t%.2f%%\t%.2f%%\t\t%.2f%%' %(item, len(closePricePerYear[item]), annualReturnPerYear[item]*100, dailyPriceVolatility[item]*100, annualPriceVolatility[item]*100))
    print('\n')
#===========================================================

showInfo(closePrice)
