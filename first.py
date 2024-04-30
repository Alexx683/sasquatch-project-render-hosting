import streamlit as st
import requests
import streamlit as st
import json
from streamlit_lottie import st_lottie


# Function to load Lottie animation from URL
#LOTTIE FILES
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def load_lottieurl(url: str):
     r = requests.get(url)
     if r.status_code != 200:
         return None
     return r.json()



# Set page configuration
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# Load Lottie animation

lottie_coding = load_lottiefile("lottiefiles/loading.json")
lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")


st.title = (" Include Lottie Files in Streamlit")
st_lottie(
     lottie_coding,
     speed=1,
     reverse=False,
     loop=True,
     quality="low", # medium ; high
     renderer="svg", # canvas
     height=None,
     width=None,
     key=None,
 )
st_lottie(lottie_hello, key="hello")

#  Display content
with st.container():
    st.subheader("Sasquatch")
    
    st.write("The Stock Market Data Monitoring, Analysis, and Visualizing Management System offers a comprehensive solution for users in the financial industry to effectively monitor, analyze, and visualize stock market data. With its advanced features and intuitive interface, the system empowers users to make informed decisions and stay ahead in the dynamic world of stock trading and investment.")
    st.write("[Learn More >](https://www.researchgate.net/publication/340385281_Stock_Market_Analysis_using_Data_Visualization)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Stock Market 📊")
        st.write("""
            - Data Visualization Tutorials: Creating and explaining how to use various data visualization tools and techniques, such as charts, graphs, and dashboards.
            - Case Studies: Presenting real-world examples of data analysis projects, including the challenges faced, the solutions implemented, and the outcomes achieved.
            - Software Demonstrations: Showcasing how to use data analysis software, such as Excel, Python libraries (e.g., pandas, matplotlib), or specialized data analysis tools.
            - Career Advice: Offering advice on career development, including tips for improving data analysis skills, preparing for job interviews, and navigating the job market.
        """)

    # with right_column:
    #     if lottie_coding:
    #         st_lottie(lottie_coding, height=400, key="coding")
    #     else:
    #         st.error("Failed to load Lottie animation.")




                    
