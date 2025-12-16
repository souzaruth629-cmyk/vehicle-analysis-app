import pandas as pd
import plotly.express as px
import streamlit as st

# Carregar os dados
car_data = pd.read_csv('vehicles_us.csv')

# Cabeçalho
st.header('Dashboard de Análise de Veículos')

# Slider de faixa de preço
price_range = st.slider(
    'Selecione a faixa de preço:',
    min_value=int(car_data['price'].min()),
    max_value=int(car_data['price'].max()),
    value=(int(car_data['price'].min()), int(car_data['price'].max()))
)

# Filtrar dados com base no slider
filtered_data = car_data[
    (car_data['price'] >= price_range[0]) &
    (car_data['price'] <= price_range[1])
]

# Gráfico de dispersão
st.subheader('Relação entre Preço e Ano do Veículo')
fig_scatter = px.scatter(
    filtered_data,
    x='model_year',
    y='price',
    title='Preço vs Ano do Carro'
)
st.plotly_chart(fig_scatter)

# Histograma com botão
if st.button('Mostrar Histograma de Preços'):
    fig_price_hist = px.histogram(
        filtered_data,
        x='price',
        title='Distribuição de Preços dos Carros',
        labels={'price': 'Preço (USD)', 'count': 'Quantidade de Carros'},
        nbins=50
    )
    st.plotly_chart(fig_price_hist)
