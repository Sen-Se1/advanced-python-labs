import streamlit as st
import pandas as pd
import numpy as np

st.title("📈 Analytics Dashboard")

st.write("This is the dashboard page with data visualizations!")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Users", "1,234", "12%")
col2.metric("Revenue", "$56,789", "8%")
col3.metric("Conversion", "3.2%", "-2%")
col4.metric("Sessions", "45,678", "15%")

st.write("### Sample Analytics Chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Product A', 'Product B', 'Product C']
)
st.area_chart(chart_data)

st.write("### Sample Data")
data = pd.DataFrame({
    'Region': ['North', 'South', 'East', 'West'],
    'Sales': [1000, 1500, 800, 1200],
    'Growth': [0.1, 0.15, -0.05, 0.08]
})
st.dataframe(data)