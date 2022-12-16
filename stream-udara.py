import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('udara_model.sav', 'rb'))

# Judul
st.title("PREDIKSI KUALITAS STANDAR PENCEMARAN UDARA")
st.header("Tugas UAS Business intelligence")
st.subheader("NENDA PUTRI SUCIATY")
st.subheader("191351065")

pm10 = st.text_input('Partikel debu dalam emisi gas buang (PM10)')
so2 = st.text_input('Sulfida (SO2)')
co = st.text_input('Carbon Monoksida (CO)')
o3 = st.text_input('Ozon (03)')
no2 = st.text_input('Nitrogen Dioksida (NO2)')
max = st.text_input(
    'Nilai ukur paling tinggi dari seluruh parameter yang diukur dalam waktu yang sama (MAX)')


udara_diagnosis = ''

if st.button('STATUS PENCEMARAN UDARA'):
    udara_prediction = model.predict([[pm10, so2, co, o3, no2, max]])

    if (udara_prediction[0] == 0):
        udara_diagnosis = 'STATUS UDARA TIDAK SEHAT'
    elif (udara_prediction[0] == 1):
        udara_diagnosis = 'STATUS UDARA SEDANG'
    else:
        udara_diagnosis = 'STATUS UDARA BAIK'

st.success(udara_diagnosis)
