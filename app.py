import joblib
import streamlit as st
import pandas as pd
import numpy as np
model = joblib.load("model.pkl")
st.title('Pushpin Task Volume Prediction App')
st.write('Enter the necessary details here:')
st_date = st.date_input('Select Date:')
st_time = st.time_input('Select Time:')
datetime_value = pd.to_datetime(f'{st_date} {st_time}')
year = datetime_value.year
month = datetime_value.month
Day= datetime_value.day
day = datetime_value.day_name()
hour = datetime_value.hour

lag1 = st.number_input(
    'Previous Hour Orders',
    min_value=0.0
)
lag24 = st.number_input(
    'Previous Day Same Hour Orders',
    min_value=0.0
)
assigned_shift = st.selectbox(
    'Shift',
    ['A','B','C','D','E','F']
)
st.subheader('Extracted Features')

st.write(f'Year: {year}')
st.write(f'Month: {month}')
st.write(f'Day: {Day}')
st.write(f'Hour: {hour}')
st.write(f'Day Name: {day}')
if st.button('Predict Orders'):

    input_df = pd.DataFrame({

        'hour': [hour],
        'lag1': [lag1],
        'lag24': [lag24],
        'Year': [year],
        'Month': [month],
        'Day': [Day],
        'day': [day],
        'assigned_shift': [assigned_shift]

    })

    prediction = model.predict(input_df)

    st.success(
        f'Predicted Orders: {prediction[0]:.2f}\nApprox CWs required :{prediction/3}'
    )
