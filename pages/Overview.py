import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

with st.sidebar:
    st.header('Overview')
    
st.title('Information')

st.write("Order Data Every Year")

image = Image.open("data1.png")

st.image(image, caption='', width=450, use_column_width=False)

st.write("The Most and Least Sold Products in 2016")

image = Image.open("data2.png")

st.image(image, caption='', width=450, use_column_width=False)
