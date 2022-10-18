import pandas as pd
import pandas_datareader as pdr
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt

tickers = ['AAPL', 'TWTR', 'IBM', 'MSFT']
start = dt.datetime(2020, 1, 1)
data = pdr.get_data_yahoo(tickers, start)
data = data['Adj Close']
log_returns = np.log(data / data.shift())

# calculating correlation
log_returns.corr()

# adding SP500 index as reference
sp500 = pdr.get_data_yahoo("^GSPC", start)
log_returns['SP500'] = np.log(sp500['Adj Close'] / sp500['Adj Close'].shift())
log_returns.corr()


# finds and add any company, this will help us with finding company with negative correlation
def test_correlation(ticker):
    df = pdr.get_data_yahoo(ticker, start)
    lr = log_returns.copy()
    lr[ticker] = np.log(df['Adj Close'] / df['Adj Close'].shift())
    return lr.corr()


test_correlation("TLT")
print(log_returns.corr())


# visualisation of the AAPL and the TLT (negative correlation)
def visualize_correlation(ticker1, ticker2):
    df = pdr.get_data_yahoo([ticker1, ticker2], start)
    df = df['Adj Close']
    df = df/df.iloc[0]
    fig, ax = plt.subplots()
    df.plot(ax=ax)
    plt.show()


# correlation between AAPL and TLT
visualize_correlation('AAPL', 'TLT')

