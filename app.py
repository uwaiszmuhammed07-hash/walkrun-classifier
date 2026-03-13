import streamlit as st
import joblib
import numpy as np
import pandas as pd

model = joblib.load('walkrun_best_model.pkl')

st.set_page_config(page_title='Walk or Run Classifier', page_icon='🏃', layout='centered')
st.title('🏃 Walk or Run Classifier')
st.write('**PRCP-1013** — Wrist sensor activity detection | Best Model: LightGBM (99.27% accuracy)')
st.divider()

col1, col2 = st.columns(2)
with col1:
    st.subheader('📡 Accelerometer')
    acc_x = st.number_input('Acceleration X', value=0.30)
    acc_y = st.number_input('Acceleration Y', value=-0.78)
    acc_z = st.number_input('Acceleration Z', value=-0.03)
with col2:
    st.subheader('🔄 Gyroscope')
    gyro_x = st.number_input('Gyro X', value=0.04)
    gyro_y = st.number_input('Gyro Y', value=-0.04)
    gyro_z = st.number_input('Gyro Z', value=-2.94)

wrist = st.selectbox('Wrist', [0, 1], format_func=lambda x: '0 — Left' if x == 0 else '1 — Right')
st.divider()

if st.button('🔍 Predict Activity', use_container_width=True):
    EPS = 1e-6
    acc_mag  = np.sqrt(acc_x**2 + acc_y**2 + acc_z**2)
    gyro_mag = np.sqrt(gyro_x**2 + gyro_y**2 + gyro_z**2)
    features = pd.DataFrame([[
        wrist, acc_x, acc_y, acc_z, gyro_x, gyro_y, gyro_z,
        acc_mag, gyro_mag,
        acc_x / (abs(acc_y) + EPS),
        gyro_x / (abs(gyro_y) + EPS),
        acc_mag * gyro_mag,
        acc_x**2 + acc_y**2 + acc_z**2,
        gyro_x**2 + gyro_y**2 + gyro_z**2,
        abs(acc_x - acc_y) + abs(acc_y - acc_z)
    ]], columns=[
        'wrist','acceleration_x','acceleration_y','acceleration_z',
        'gyro_x','gyro_y','gyro_z',
        'acc_magnitude','gyro_magnitude','acc_xy_ratio','gyro_xy_ratio',
        'jerk_proxy','acc_energy','gyro_energy','acc_std_proxy'
    ])
    prediction = model.predict(features)[0]
    proba = model.predict_proba(features)[0]
    if prediction == 1:
        st.success(f'## 🏃 Running!  ({proba[1]*100:.1f}% confidence)')
    else:
        st.info(f'## 🚶 Walking!  ({proba[0]*100:.1f}% confidence)')
