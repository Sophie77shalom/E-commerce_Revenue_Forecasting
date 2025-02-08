import streamlit as st
import requests
import pandas as pd
import datetime

# Streamlit UI
st.title("📈 E-commerce Revenue Forecast")

# User input for prediction
start_date = st.date_input("Select Start Date", datetime.date(2025, 3, 1))
steps = st.number_input("Days to Predict", min_value=1, max_value=90, value=30)

if st.button("Predict"):
    url = "http://127.0.0.1:5000/predict"
    data = {"start_date": str(start_date), "steps": steps}
    
    try:
        response = requests.post(url, json=data)
        forecast = response.json()
        
        df = pd.DataFrame(forecast)
        df["date"] = pd.to_datetime(df["date"])
        
        # Display the results
        st.subheader("📊 Forecasted Revenue")
        st.line_chart(df.set_index("date")["predicted_revenue"])
        
        st.write(df)
    
    except Exception as e:
        st.error(f"Error: {e}")
