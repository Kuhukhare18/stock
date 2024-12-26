import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as data
from keras.model import load_model
import streamlit as st

start = '2010-01-01'
end = '2019-12-31'

st.title('Stock trend prediction')

user_input=st.text_input('Enter Stock  Ticker', 'AAPL')

# Fetch historical stock data
df = yf.download(user_input, start=start, end=end)

#describing data
st.subheader('Data from 2010-2019')
st.write(df.describe())