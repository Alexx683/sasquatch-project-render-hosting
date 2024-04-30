import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from streamlit_lottie import st_lottie
import requests
import yfinance as yf
import pandas as pd
import time
import json

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

#LOTTIE FILES
# def load_lottiefile(filepath: str):
#     with open(filepath, "r") as f:
#         return json.load(f)

def load_lottieurl(url: str):
     r = requests.get(url)
     if r.status_code != 200:
         return None
     return r.json()



# ---LOAD ASSETS---

# lottie_coding = load_lottiefile("lottiefiles/coding.json")
lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")

st.title = (" Include Lottie Files in Streamlit")
# st_lottie(
#     lottie_coding,
#     speed=1,
#     reverse=False,
#     loop=True,
#     quality="low",
#     renderer="svg",
#     height=None,
#     width=None,
#     key=None,
# )

# st_lottie(lottie_hello, key="hello")


# ------HEADER SECTION-----
with st.container():
    st.subheader("Sasquatch")





# # Create a search bar
search_query = st.text_input("Search:", "")

# Create a drop-down menu
option = st.selectbox("Select Option:", ["AAPL", "META", "AMZN", "TSLA"])

# Display the selected option
st.write("You selected:", option)


    # Your code herest.title("Stock Market Data Monitoring and Prediction System")
st.write("The Stock Market Data Monitoring, Analysis, and Visualizing Management System offers a comprehensive solution for users in the financial industry to effectively monitor, analyze, and visualize stock market data. With its advanced features and intuitive interface, the system empowers users to make informed decisions and stay ahead in the dynamic world of stock trading and investment.")
st.write("[Learn More >](https://www.researchgate.net/publication/340385281_Stock_Market_Analysis_using_Data_Visualization)")





#progress chart
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()
st.button("Re-run")


# Create a rounded progress bar
progress_value = st.sidebar.slider("Progress:", 0, 100, 50, step=1, format="%d%%")
progress_bar = st.sidebar.progress(progress_value)

# Create a drop-down menu


# Display the selected option
st.write("You selected:", option)






# Create two columns
left_column, right_column = st.columns([1, 4])

# Left column (dashboard)
with left_column:
    user_input = st.text_input("Enter something:")
    st.write("You entered:", user_input)

# Right column (charts)
with right_column:
    st.subheader("Histogram and Pie Chart")

    # Function to fetch real-time stock data
def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="1d")
    return data




# # Set page configuration
# st.set_page_config(layout="wide")


# Create progress bar and line chart
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
chart = st.line_chart(pd.DataFrame(columns=["Close"]))

# Simulate progress updates
for i in range(1, 101):
    # Fetch real-time data for a stock (e.g., AAPL)
    stock_data = get_stock_data("AAPL")
    stock_data = get_stock_data("AMZN")
    stock_data = get_stock_data("TSLA")
    stock_data = get_stock_data("META")
    
    # Update chart with new data
    chart_data = pd.DataFrame({"Close": stock_data["Close"]})
    chart.line_chart(chart_data)

    # Update progress bar and status text
    status_text.text("%i%% Complete" % i)
    progress_bar.progress(i)

    # Pause briefly to simulate real-time updates
    time.sleep(1)

# Clear progress bar
progress_bar.empty()

# Add button to rerun the script
#st.button("Re-run")


# with right_column:
#         if lottie_coding:
#             st_lottie(lottie_coding, height=400, key="coding")
#         else:
#             st.error("Failed to load Lottie animation.")

# Add custom layout using HTML and CSS
st.markdown("""
<style>
body {
    background-color: #f0f2f6;
    font-family: Arial, sans-serif;
}
.container {
    max-width: 800px;
    margin: auto;
    padding: 20px;
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}
</style>
""", unsafe_allow_html=True)

# # Add elements to the custom layout
# st.markdown('<div class="container">', unsafe_allow_html=True)
# st.title("Custom Layout Example")
# st.write("This is an example of using a custom layout in Streamlit.")
# st.markdown('</div>', unsafe_allow_html=True)

       

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Stock Market 📊")
        st.write("##")


 

# Insert a hyperlink to a Google Colab notebook
colab_link = "https://colab.research.google.com/drive/1VjwRaiyalkyJNIxpYzKeLPBmzt8ZtGfr#scrollTo=CcIZiYTSB2gB"
st.markdown(f"[Open in Google Colab]({colab_link})")
 

 
#  # Create progress bar, status text, and line chart
# progress_bar = st.sidebar.progress(0)
# status_text = st.sidebar.empty()
# last_rows = np.random.randn(1, 1)
# chart = st.line_chart(last_rows)

# # Simulate progress updates
# for i in range(1, 101):
#     new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
#     status_text.text("%i%% Complete" % i)
#     chart.add_rows(new_rows)
#     progress_bar.progress(i)
#     last_rows = new_rows
#     time.sleep(0.05)

# # Clear progress bar
# progress_bar.empty()

# # Add button to rerun the script
# st.button("Re-run")



# a progress bar code without the chart









