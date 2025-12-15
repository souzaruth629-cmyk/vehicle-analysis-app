import pandas as pd
import plotly.express as px
import streamlit as st

# Primeiro: carregar os dados
car_data = pd.read_csv('vehicles_us.csv')

# Segundo: criar o cabeçalho
st.header('Dashboard de Análise de Veículos')
