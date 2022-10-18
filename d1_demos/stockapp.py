import yfinance as yf
import streamlit as st

tickerSymbol = 'GOOGL'
tickerSymbolMSFT = 'MSFT'

st.write(f"""
# Simple Stock Price App
Shown are the stock closing price and volume of {tickerSymbol} and {tickerSymbolMSFT}!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
tickerDataMSFT = yf.Ticker(tickerSymbolMSFT)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
tickerDfMSFT = tickerDataMSFT.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

tickerSymbol
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)


tickerSymbolMSFT
st.line_chart(tickerDfMSFT.Close)
st.line_chart(tickerDfMSFT.Volume)