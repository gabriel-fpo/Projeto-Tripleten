import pandas as pd
import plotly.express as px
import streamlit as st

# Cabeçalho
st.header('Dashboard de Vendas de Veículos')

car_data = pd.read_csv('vehicles.csv') # lendo os dados

# Checkbox para histograma
hist_checkbox = st.checkbox('Criar histograma')

if hist_checkbox: # se o checkbox estiver marcado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    
    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# Checkbox para gráfico de dispersão
scatter_checkbox = st.checkbox('Criar gráfico de dispersão')

if scatter_checkbox: # se o checkbox estiver marcado
    # escrever uma mensagem
    st.write('Criando um gráfico de dispersão para odometer vs price')
    
    # criar um gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)