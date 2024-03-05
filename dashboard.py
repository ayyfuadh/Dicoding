import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

with st.sidebar:
    st.header('Dashboard')

st.title("Data From E-Commerce Analysis Results")

image = Image.open("commerce.JPG")

st.image(image, caption='', width=450, use_column_width=False)

st.write("The project is an interactive dashboard built using Streamlit. This dashboard utilizes the Brazilian E-Commerce Public Dataset by Olist as its data source. The dataset contains information about e-commerce transactions in Brazil and provides insights into trends and patterns of online purchases in the country In this dashboard, we present informative data visualizations to aid understanding of various aspects of e-commerce sales in Brazil. This visualization includes information about the cities with the largest number of sellers, the most popular product categories, and purchasing trends over a specific time period. By using attractive graphs and charts, users can easily analyze and understand relevant sales patterns. This dashboard provides valuable insights for e-commerce business owners and other stakeholders in making decisions based on sales data presented in a way that is insightful and easy to understand. The aim of this project is to analyze e-commerce sales in Brazil through an interactive dashboard. This project aims to achieve the following: Gain insight into the distribution of sellers in different cities in Brazil, Identify the most popular product categories, Analyzing purchasing trends over a period of time, Helps make decisions based on data presented visually, Using this dashboard, users can easily understand and analyze e-commerce sales in Brazil, and make data-backed decisions.")

