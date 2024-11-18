import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
@st.cache
def load_data(file_path):
    return pd.read_csv(file_path, parse_dates=["order_date"])

# Dashboard components
def show_dashboard(data):
    st.sidebar.title("Filters")
    date_range = st.sidebar.date_input(
        "Select Date Range",
        value=(data["order_date"].min(), data["order_date"].max())
    )
    filtered_data = data[
        (data["order_date"] >= pd.Timestamp(date_range[0])) &
        (data["order_date"] <= pd.Timestamp(date_range[1]))
    ]
    
    # Daily Profit/Loss
    filtered_data["profit"] = filtered_data["total_price"] - filtered_data["cost_price"]
    daily_profit = filtered_data.groupby("order_date")["profit"].sum().reset_index()
    st.subheader("Daily Profit/Loss")
    fig1 = px.line(daily_profit, x="order_date", y="profit", title="Daily Profit/Loss")
    st.plotly_chart(fig1)

    # Most Popular Products
    popular_products = filtered_data["product_name"].value_counts().head(10)
    st.subheader("Most Popular Products")
    fig2 = px.bar(
        x=popular_products.index, 
        y=popular_products.values, 
        labels={"x": "Product", "y": "Count"}, 
        title="Most Popular Products"
    )
    st.plotly_chart(fig2)

    # Filtered Table
    st.subheader("Filtered Data")
    st.write(filtered_data)

# Streamlit app
st.title("Ecommerce Dashboard")
csv_file = st.file_uploader("Upload a CSV file", type=["csv"])
if csv_file:
    data = load_data(csv_file)
    show_dashboard(data)
