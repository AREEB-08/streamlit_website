import streamlit as st
import  pandas as pd
import numpy as np
import time

st.sidebar.title("STARTUP FUNDING ANALYSIS ")
df=pd.read_csv("streamlit_website/startup_funding.csv")
st.dataframe(df)
startup_name_list=df['Startup Name'].unique().tolist()


df['Investors Name']=df['Investors Name'].fillna("unknown")
investors_name_list=sorted(df['Investors Name'].unique().tolist())




option=st.sidebar.selectbox('SELECT THE OPTION',["Overall analysis","STARTUP","Investors",])

if option=="Overall analysis":
    st.title("Overall analysis")

elif option=="STARTUP":
    option_startup=st.sidebar.selectbox('SELECT STARTUP',startup_name_list)
    st.title("STARTUP ANALYSIS")

else:
    st.sidebar.selectbox("SELECT INVESTORS",investors_name_list)
    st.sidebar.title("INVESTOR")