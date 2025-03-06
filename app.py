import streamlit as st
import requests

# Title of the app
st.title("Stock Price Prediction App")

# Input fields for historical prices
st.header("Enter Historical Stock Prices")
prices = st.text_input("Enter historical prices (comma-separated):", "100, 101, 102, 103, 104")

# Input field for future days
st.header("Enter Number of Days to Predict")
future_days = st.number_input("Enter number of days to predict:", min_value=1, value=5)

# Button to trigger prediction
if st.button("Predict"):
    # Prepare the input data
    prices_list = [float(price.strip()) for price in prices.split(",")]
    data = {
        "data": prices_list  # Use "data" instead of "prices"
    }

    # Send a POST request to the FastAPI backend
    try:
        response = requests.post("https://c939-34-81-138-181.ngrok-free.app/predict", json=data)
        if response.status_code == 200:
            predictions = response.json()["prediction"]  # Use "prediction" instead of "predicted_prices"
            st.success("Prediction successful!")
            st.write("Predicted Price:", predictions)
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"An error occurred: {e}")