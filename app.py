import streamlit as st
import joblib
import numpy as np

lin_reg_loaded = joblib.load('lin_reg_model.joblib')

st.title("Prediksi Gaji Berdasarkan Lama Bekerja")

years_experience = st.number_input("Masukan jumlah tahun bekerja:", min_value=0.0, max_value=20.0, step=0.1)

if st.button("Prediksi Gaji"):
	gaji = lin_reg_loaded.predict([[years_experience]])
	st.write(f"Gaji seseorang setelah bekerja selama {years_experience} tahun adalah Rp{gaji[0]:,.2f}")

