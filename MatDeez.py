import streamlit as st
import pickle
import pandas as pd
import numpy as np



with open('random_forest_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title('Electricity Consumption Predictor')
st.sidebar.header('Input Features')

temperature = st.sidebar.number_input('Suhu (°C)', min_value=0.0, max_value=50.0, value=25.0)
humidity = st.sidebar.number_input('Kelembapan (%)', min_value=0.0, max_value=100.0, value=50.0)
square_footage = st.sidebar.number_input('Ukuran Bangunan (ft²)', min_value=0.0, max_value=10000.0, value=1000.0)
occupancy = st.sidebar.number_input('Penghuni', min_value=0, max_value=9, value=5)


hvac_usage = st.sidebar.selectbox('Penggunaan AC Heater', ['Off', 'On'])
hvac_usage_numeric = 1 if hvac_usage == 'On' else 0

lighting_usage = st.sidebar.selectbox('Penggunaan Lampu', ['Off', 'On'])
lighting_usage_numeric = 1 if lighting_usage == 'On' else 0

holiday = st.sidebar.selectbox('Apakah Hari Libur?', ['Tidak', 'Ya'])
holiday_numeric = 1 if holiday == 'Yes' else 0

day_of_week = st.sidebar.selectbox('Hari Apa?', ['Hari Kerja', 'Akhir Pekan'])
day_of_week_numeric = 1 if day_of_week == 'Weekend' else 0


input_data = pd.DataFrame({
    'Temperature': [temperature],
    'Humidity': [humidity],
    'SquareFootage': [square_footage],
    'Occupancy': [occupancy],
    'HVACUsage': [hvac_usage_numeric],
    'LightingUsage': [lighting_usage_numeric],
    'DayOfWeek': [day_of_week_numeric],
    'Holiday': [holiday_numeric]
})

# # model_prediction = model.predict(input_data)

if st.sidebar.button('Predict Energy Consumption'):
    prediction = model.predict(input_data)
            
            # Display prediction
    st.header('Prediction Results')
    st.metric(label='Predicted Energy Consumption', value=f'{prediction} kWh')
            
#             # Optional: Provide some insights
#     st.write('### Insights:')
#     if prediction < 500:
#         st.success('Low energy consumption predicted.')
#     elif 500 <= prediction < 1000:
#         st.warning('Moderate energy consumption predicted.')
#     else:
#         st.error('High energy consumption predicted.')
        
