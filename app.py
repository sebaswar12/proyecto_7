import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.header("Análisis de anuncios de venta de coches")

car_data = pd.read_csv('vehicles_us.csv')  # asegúrate de subir luego este archivo

if st.button('Mostrar histograma'):
    st.write('Histograma de odómetro')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    st.plotly_chart(fig, use_container_width=True)
