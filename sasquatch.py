import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px
import numpy as np





# Dashboard and Side Bar
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")
st.title("Sasquatch Admin 📈 📉")

st.markdown("---")

# ------HEADER SECTION-----
with st.container():
    st.subheader("Stock Dashboard ")

    # Your code herest.title("Stock Market Data Monitoring and Prediction System")
st.write("The Stock Market Data Monitoring, Analysis, and Visualizing Management System offers a comprehensive solution for users in the financial industry to effectively monitor, analyze, and visualize stock market data. With its advanced features and intuitive interface, the system empowers users to make informed decisions and stay ahead in the dynamic world of stock trading and investment.")
st.write("[Learn More >](https://www.researchgate.net/publication/340385281_Stock_Market_Analysis_using_Data_Visualization)")




# Define the Google Colab link
colab_link = "https://colab.research.google.com/drive/1VjwRaiyalkyJNIxpYzKeLPBmzt8ZtGfr#scrollTo=CcIZiYTSB2gB"

st.markdown(f"""
    My Google Colab link contains a collaborative notebook hosted on Google's platform, enabling users to execute Python code, visualize data, and share insights in real-time. It serves as an interactive environment for experimenting with machine learning algorithms, conducting data analysis, and prototyping solutions. Integrating this link into my Streamlit code allows users to seamlessly access and interact with the notebook's contents directly within my web application, enhancing the overall user experience and facilitating collaboration.
""")

st.write(f"To access the Google Colab notebook, click [here]({colab_link})")

st.markdown("---")



# Input widgets for user interaction
ticker = st.sidebar.text_input('Enter Ticker Symbol', value='META', max_chars=10).upper()
start_date = st.sidebar.date_input('Start Date', pd.to_datetime('2015-01-01'))
end_date = st.sidebar.date_input('End Date', pd.to_datetime('today'))

data = yf.download(ticker,start=start_date,end=end_date)
fig = px.line(data, x=data.index, y=data['Adj Close'], title=ticker)


st.plotly_chart(fig)

pricing_data, fundamental_data, news = st.tabs(["Pricing Data", "Fundamental Data", "Top 10 News"])

with pricing_data:
     st.header('Price Movements')
     data2 = data
     data2['% Change'] = data['Adj Close'] / data['Adj Close'].shift(1)-1
     data2.dropna(inplace = True)
     st.write(data2)

#252 excluding the weekends(only market days)

     annual_return = data2['% Change'].mean()*252*100
     st.write('Annual Return : = ',annual_return,'%') # Annual Return
     stdev = np.std(data2['% Change'])*np.sqrt(252)
     st.write('Standard Deviation : = ',stdev*100,'%') # Standard Deviation
     st.write('Risk Adj. Return : = ',annual_return/(stdev*100)) # Risk Adjustment

 
import streamlit as st
import time

# Create progress bar and status text
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()

# Simulate progress updates
for i in range(1, 101):
    status_text.text("%i%% Complete" % i)
    progress_bar.progress(i)
    time.sleep(0.05)

# Clear progress bar
progress_bar.empty()

# Add button to rerun the script
st.button("Re-run")




# Analysing stock data
from alpha_vantage.fundamentaldata import FundamentalData
with fundamental_data:
      key = 'KMCJKFXVJ2KCB9PQ'
      fd = FundamentalData(key,output_format = 'pandas')

# balance_sheet = balance_sheet.T[2:]
      st.subheader('Fundamental Data')
      balance_sheet = fd.get_balance_sheet_annual(ticker)[0].T[2:]
      balance_sheet.columns = list(balance_sheet.iloc[0])
      st.write('Balance Sheet:', balance_sheet)

# income_statement = income_statement.T[2:]
      income_statement = fd.get_income_statement_annual(ticker)[0].T[2:] 
      income_statement.columns = list(income_statement.iloc[0])
      st.write('Income Statement:', income_statement)

# cf = cash_flow.T[2:]
      cash_flow = fd.get_cash_flow_annual(ticker)[0].T[2:]
      cash_flow.columns = list(cash_flow.iloc[0])
      st.write('Cash Flow Statement:', cash_flow)





     
# Fundamental Data
from stocknews import StockNews
with news:
    st.header(f'News of {ticker}')
    sn = StockNews(ticker , save_news=False)
    df_news = sn.read_rss()
    for i in range(10):
         st.subheader(f'News {i+1}')
         st.write(df_news['published'][i])
         st.write(df_news['title'][i])
         st.write(df_news['summary'][i])
         title_sentiment = df_news['sentiment_title'][i]
         st.write(f'Title sentiment {title_sentiment}')
         news_sentiment = df_news['sentiment_summary'][i]
         st.write(f'News sentiment {news_sentiment}')

