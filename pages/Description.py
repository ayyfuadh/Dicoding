import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

with st.sidebar:
    st.header('Description')

st.title("E-Commerce Dashboard")

image = Image.open("E-Commerce.JPG")

st.image(image, caption='E-Commerce Image', width=500, use_column_width=False)

st.write("The E-Commerce Public Dataset comprises data from e-commerce transactions in Brazil over a certain period. It consists of several related files, providing comprehensive insights into the e-commerce industry in Brazil. Some main files in this dataset include: Orders (Information about orders, such as order ID, order status, purchase time, approval time, and order delivery), Order Items (Detailed information about each item purchased in orders, such as product ID, price, quantity, and shipping cost) Products (Product information, including ID, category, and product name), Sellers (Seller information, including ID, name, and location), Customers (Customer information, including ID, name, and location). This dataset enables extensive analysis of various aspects of e-commerce in Brazil. It allows us to analyze sales trends over time, the most popular product categories, customer purchasing preferences across different regions, as well as seller characteristics and locations. By leveraging this dataset in visualization analysis projects, we can gain deeper insights into the e-commerce market in Brazil, acquire understanding of purchasing behaviors, and identify opportunities or challenges in the industry..")

