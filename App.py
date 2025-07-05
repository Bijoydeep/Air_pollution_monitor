import streamlit as st
import pandas as pd
from utils.data_loader import load_openaq_data
from utils.ai_explainer import explain_trend
from ml.model import predict_pollution
st.set_page_config(page_title="Air Pollution Monitor", layout="wide")
st.title("🛰️ Air Pollution Monitor")
st.markdown("Using Satellite, Ground, Reanalysis Data + AI/ML")
location = st.sidebar.text_input("Enter location (e.g. Delhi)", "Delhi")
pollutant = st.sidebar.selectbox("Select Pollutant", ["pm25", "no2", "o3"])
data = load_openaq_data(location, pollutant)
if data is not None:
    st.line_chart(data["value"])
    st.dataframe(data.tail())
    if st.button("🔮 Forecast Next 7 Days"):
        forecast = predict_pollution(data)
        st.subheader("7-Day Forecast")
        st.line_chart(forecast)
    if st.button("🧠 GPT Explanation"):
        explanation = explain_trend(data)
        st.success(explanation)
else:
    st.error("Failed to load data. Try a different location.")
