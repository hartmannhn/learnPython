stockIDN.py  
by @hartmannhn
- used to pull Indonesia's listed company stock price data from specified date range and perform simple calculations
- made with Python 3.7.4 (x64)
- learning using dataframe with pandas, and pandas_datareader to pull data from internet

input required
- stock ticker code (e.g. "BBCA" / "BBRI" )

output
- total return from start date to end date (in %)
- compounded return (in %)
- annual return (per year in %)
- daily price volatility (in %)
- annual price volatility (in %)

future-update-plan  
- adding IHSG and LQ45 to enable direct comparison
- adding beta parameter to show stock price volatility in relation to market
- adding more input to enable stock to stock comparison
- adding plot to show the comparison against IHSG, LQ45, or other stock visually

v1.0  (2021/04/19)
- uses pandas_datareader to pull data from Yahoo!
- now display total return, yearly return, compounded return, and daily/annual price volatility
