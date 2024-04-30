# -*- coding: utf-8 -*-
"""Yahoo Finance project

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VjwRaiyalkyJNIxpYzKeLPBmzt8ZtGfr
"""

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime
import seaborn as sns
from stocknews import StockNews

ticker = "AAPL"

start_date = '2022-02-28'
end_date = '2024-02-28'

data = yf.download(ticker, start=start_date, end=end_date)

data = pd.read_csv("stock_data.csv")

data.info()

# Check for missing values in the dataset
missing_values = [data.isnull().any(axis=1)]

data_new = data.dropna()
data_new

figsize = (12, 1.2 * len(data_new['Company'].unique()))
plt.figure(figsize=figsize)
sns.violinplot(data_new, x='Close', y='Company', inner='box', palette='Dark2')
sns.despine(top=True, right=True, bottom=True, left=True)

# @title Open

from matplotlib import pyplot as plt
data_new['Open'].plot(kind='hist', bins=20, title='Open')
plt.gca().spines[['top', 'right',]].set_visible(False)

opening_prices = data['Open']

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(opening_prices, color='blue')
plt.title(f"Opening Prices for {ticker}")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.grid(True)
plt.show()

# Download stock data for Apple
aapl = yf.download("AAPL", period="1d")

# Print the closing price
print(aapl["Close"][0])

df.head()

ticker = "AMZN"

start_date = '2022-02-28'
end_date = '2024-02-28'

data = yf.download(ticker, start=start_date, end=end_date)

# Define a list of ticker symbols
ticker_symbols = ['AAPL', 'AMZN', 'META', 'TSLA']

# Create an empty dictionary to store the data for each ticker symbol
stock_data = {}

# Loop through each ticker symbol
for symbol in ticker_symbols:
    # Fetch historical data for the current ticker symbol
    data = yf.download(symbol, start='2022-01-01', end='2022-12-31')

    # Store the data in the dictionary
    stock_data[symbol] = data

# Display the first few rows of data for each ticker symbol
for symbol, data in stock_data.items():
    print(f"\n{symbol} data:")
    print(data.head())

# Define a list of ticker symbols
ticker_symbols = ['AAPL', 'AMZN', 'META', 'TSLA']

# Create an empty dictionary to store the data for each ticker symbol
stock_data = {}

# Loop through each ticker symbol
for symbol in ticker_symbols:
    # Fetch historical data for the current ticker symbol
    data = yf.download(symbol, start='2022-01-01', end='2022-12-31')

    # Store the data in the dictionary
    stock_data[symbol] = data

# Plot the data for each ticker symbol
plt.figure(figsize=(12, 8))

for symbol, data in stock_data.items():
    plt.plot(data.index, data['Adj Close'], label=symbol)

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Adjusted Close Price')
plt.title('Comprehensive Chart of Yahoo Finance Data')
plt.legend()

# Display the plot
plt.grid(True)
plt.show()

from IPython.display import HTML

# Define a list of ticker symbols
ticker_symbols = ['AAPL', 'AMZN', 'META', 'TSLA']

# Generate HTML code for each ticker symbol
links_html = []
for symbol in ticker_symbols:
    link_html = f'<a href="https://finance.yahoo.com/quote/{symbol}">Link to Yahoo Finance for {symbol}</a>'
    links_html.append(link_html)

# Display the hyperlinks
HTML('<br>'.join(links_html))



"""# New Section"""

import plotly.graph_objs as go
from plotly.subplots import make_subplots


# Generate some sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a Plotly figure with subplots
fig = make_subplots(rows=1, cols=1)

# Add traces to the figure (lines)
fig.add_trace(go.Scatter(x=x, y=y1, mode='lines', name='sin(x)'), row=1, col=1)
fig.add_trace(go.Scatter(x=x, y=y2, mode='lines', name='cos(x)'), row=1, col=1)

# Update layout
fig.update_layout(title='Dynamic Chart', xaxis_title='X', yaxis_title='Y')

# Show the figure
fig.show()

import matplotlib.animation as animation
import datetime

# Function to generate new data points
def generate_data():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    return x, y

# Function to update the plot with new data
def update(frame):
    x, y = generate_data()
    line.set_data(x, y)
    ax.relim()
    ax.autoscale_view()
    return line,

# Create a figure and axis object
fig, ax = plt.subplots()

# Initialize the plot with empty data
line, = ax.plot([], [], lw=2)

# Set plot properties
ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)
ax.set_title('Moving Chart')
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Create an animation
ani = animation.FuncAnimation(fig, update, frames=10, interval=1000, blit=True)

# Show the plot
plt.show()

pip install alpha-vantage

import os
os.environ['ALPHAVANTAGE_API_KEY'] = '3GVHFFSHBKB0W6KN'

from alpha_vantage.timeseries import TimeSeries
API_key = '3GVHFFSHBKB0W6KN'
ts = TimeSeries(key = API_key, output_format='pandas')
data = ts.get_monthly_adjusted('AAPL')
data

from alpha_vantage.timeseries import TimeSeries
API_key = '3GVHFFSHBKB0W6KN'
ts = TimeSeries(key = API_key, output_format='pandas')
data = ts.get_intraday('AAPL',interval = '5min')
data[0]

#Analysing stock data
from alpha_vantage.fundamentaldata import FundamentalData
#annual income statement for a particular stock
key = '3GVHFFSHBKB0W6KN'
fd = FundamentalData(key,output_format = 'pandas')

data = fd.get_income_statement_annual('AAPL')
data[0].T#transposed format

#Analysing stock data
from alpha_vantage.fundamentaldata import FundamentalData
# analysing quartely cashflow statement
key = '3GVHFFSHBKB0W6KN'
fd = FundamentalData(key,output_format = 'pandas')

data = fd.get_cash_flow_quarterly('MSFT')
data[0].T

#Analysing stock data
from alpha_vantage.fundamentaldata import FundamentalData
# analysing annual balance sheet
key = '3GVHFFSHBKB0W6KN'
fd = FundamentalData(key,output_format = 'pandas')

data = fd.get_balance_sheet_annual('META')
data[0].T

# Time Series Analysis

from alpha_vantage.timeseries import TimeSeries

key = '3GVHFFSHBKB0W6KN'
outputsize = 'compact'
symbol = input('Ticker: ')
typ = input('Data type- "daily", "weekly", "monthly", "interval": ')

ts = TimeSeries(key,output_format='pandas')

if typ == 'daily':
  state = ts.get_daily_adjusted(symbol,outputsize=outputsize)[0]
elif typ== 'weekly':
  state = ts.get_weekly_adjusted(symbol)[0]
elif typ== 'monthly':
  state = ts.get_monthly_adjusted(symbol)[0]
elif typ== 'interval':
  interval =input('Interval-1min, 5min, 15min, 30min, 60min : ')
  state = ts.get_intraday(symbol, interval=interval, outputsize=outputsize)[0]
else:
  print('Wrong entry')
state

from alpha_vantage.fundamentaldata import FundamentalData

key = '3GVHFFSHBKB0W6KN'
symbol = input('Ticker: ')
period = input('Period - annual or quarterly: ')
statement = input('Statement - balance sheet, income statement, or cash flow: ')

fd = FundamentalData(key, output_format='pandas')

if period == 'annual':
    if statement == 'balance sheet':
        state = fd.get_balance_sheet_annual(symbol)[0].T[2:]
        state.columns = list(fd.get_balance_sheet_annual(symbol)[0].T.iloc[0])
    elif statement == 'income statement':
        state = fd.get_income_statement_annual(symbol)[0].T[2:]
        state.columns = list(fd.get_income_statement_annual(symbol)[0].T.iloc[0])
    elif statement == 'cash flow':
        state = fd.get_cash_flow_annual(symbol)[0].T[2:]
        state.columns = list(fd.get_cash_flow_annual(symbol)[0].T.iloc[0])
    else:
        print('Wrong Entry')
elif period == 'quarterly':
    if statement == 'balance sheet':
        state = fd.get_balance_sheet_quarterly(symbol)[0].T[2:]
        state.columns = list(fd.get_balance_sheet_quarterly(symbol)[0].T.iloc[0])
    elif statement == 'income statement':
        state = fd.get_income_statement_quarterly(symbol)[0].T[2:]
        state.columns = list(fd.get_income_statement_quarterly(symbol)[0].T.iloc[0])
    elif statement == 'cash flow':
        state = fd.get_cash_flow_quarterly(symbol)[0].T[2:]
        state.columns = list(fd.get_cash_flow_quarterly(symbol)[0].T.iloc[0])
    else:
        print('Wrong Entry')
else:
    print('Invalid period entry')

state

from alpha_vantage.cryptocurrencies import CryptoCurrencies

key = '3GVHFFSHBKB0W6KN'
curr = input('Crypto Currency: ')
period = input('Period - daily, weekly, monthly: ')

cc = CryptoCurrencies(key, output_format='pandas')

if period == 'daily':
    state = cc.get_digital_currency_daily(curr, 'CNY')[0]
elif period == 'weekly':
    state = cc.get_digital_currency_weekly(curr, 'CNY')[0]
elif period == 'monthly':
    state = cc.get_digital_currency_monthly(curr, 'CNY')[0]
else:
    print('Wrong Entry')

state

# from alpha_vantage.foreignexchange import ForeignExchange

# key = '3GVHFFSHBKB0W6KN'

# from_curr = input('From currency: ')
# to_curr = input('To currency: ')
# period = input('Period - daily, weekly, monthly, intraday: ')

# fe = ForeignExchange(key, output_format='pandas')

# # Retrieve the exchange rate based on the selected period
# if period == 'daily':
#     state, _ = fe.get_currency_exchange_daily(from_curr, to_curr)
# elif period == 'weekly':
#     state, _ = fe.get_currency_exchange_weekly(from_curr, to_curr)
# elif period == 'monthly':
#     state, _ = fe.get_currency_exchange_monthly(from_curr, to_curr)
# elif period == 'intraday':
#     interval = input('Interval - 1min, 5min, 15min, 30min, 60min: ')
#     state, _ = fe.get_currency_exchange_intraday(from_curr, to_curr, interval=interval)
# else:
#     print('Wrong Entry')

# # Display the retrieved data in a table format
# print(state)

from alpha_vantage.techindicators import TechIndicators

key = '3GVHFFSHBKB0W6KN'
symbol = input('Ticker : ')
outputsize = 'compact'
interval =input('Interval - 1min,5min,15min,30min,60min,daily,weekly,monthly : ')
time = input('TIME period : ')
tech_indi = input('Technical Indicator- : SMA,EMA,VWAP,MACD,Stochachastic oscillator,RSI,Bollinger bands,fibonacci retracements  : ')

ti =TechIndicators(key,output_formats='pandas')

# Retrieve the time series data based on the selected duration
if tech_indi == 'SMA':
   state = ti.get_sma(symbol, interval=interval, time_period=time, series_type='close')[0]
elif tech_indi == 'EMA':
   state = ti.get_ema(symbol, interval=interval, time_period=time, series_type='close')[0]
elif tech_indi == 'VWAP':
    state = ti.get_vwap(symbol, interval=interval, time_period=time, series_type='close')[0]
elif tech_indi == 'MACD':
    state = ti.get_macd(symbol, interval=interval, time_period=time, series_type='close')[0]
elif tech_indi == 'Stochastic oscillator':
  state = ti.get_stoch(symbol, interval=interval, time_period=time, series_type='close')[0]
elif tech_indi == 'RSI':
  state = ti.get_rsi(symbol, interval=interval, time_period=time, series_type='close')[0]
elif tech_indi == 'Bollinger bands':
  state = ti.get_bbands(symbol, interval=interval, time_period=time, series_type='close')[0]
elif tech_indi == 'fibonacci retracements':
  state = ti.get_fib(symbol, interval=interval, time_period=time, series_type='close')[0]
else:
    print('Wrong Entry')
    state


# # Example: Calculating SMA and EMA
# data['SMA'] = data['4. close'].rolling(window=20).mean()  # Simple Moving Average (SMA)
# data['EMA'] = data['4. close'].ewm(span=20, adjust=False).mean()  # Exponential Moving Average (EMA)

# # Plotting
# plt.figure(figsize=(10, 6))
# plt.plot(data.index, data['4. close'], label='Close Price', color='blue')
# plt.plot(data.index, data['SMA'], label='SMA (20)', color='red')
# plt.plot(data.index, data['EMA'], label='EMA (20)', color='green')
# plt.title(f'{symbol} - {duration.capitalize()} Technical Indicators')
# plt.xlabel('Date')
# plt.ylabel('Price')
# plt.legend()
# plt.grid(True)
# plt.show()

# Getting Stock News for i IN RANGE 10
!pip install stocknews

from stocknews import StockNews
sn =StockNews('BA',save_news=False)
df = sn.read_rss()
df