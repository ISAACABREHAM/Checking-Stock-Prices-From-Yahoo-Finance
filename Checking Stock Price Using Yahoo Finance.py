

import yfinance as yf

stock = input("Enter share name : ")
share = yf.Ticker(stock).info
market_price = share['regularMarketPrice']
print(market_price)
