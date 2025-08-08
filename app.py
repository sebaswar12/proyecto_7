import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.header("Analisis de anuncios de venta de coches")

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Boton  histogramas
if st.button("Mostrar histogramas"):
    # H.Odometer
    st.subheader("Histograma: odometer")
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title='Distribución del odometro', xaxis_title='Odometro', yaxis_title='Frecuencia')
    st.plotly_chart(fig, use_container_width=True)

    # H.Price
    st.subheader("Histograma: price")
    fig = go.Figure(data=[go.Histogram(x=car_data['price'])])
    fig.update_layout(title='Distribucion del precio', xaxis_title='Precio', yaxis_title='Frecuencia')
    st.plotly_chart(fig, use_container_width=True)

    # H.Model_year
    st.subheader("Histograma: model_year")
    fig = go.Figure(data=[go.Histogram(x=car_data['model_year'].dropna())])
    fig.update_layout(title='Distribucion del año del modelo', xaxis_title='Año del modelo', yaxis_title='Frecuencia')
    st.plotly_chart(fig, use_container_width=True)

if st.button("Mostrar gráfico de dispersión"):
    fig = go.Figure([go.Scatter(
        x=car_data['model_year'],
        y=car_data['price'],
        mode='markers'
    )])
    st.plotly_chart(fig, use_container_width=True)
