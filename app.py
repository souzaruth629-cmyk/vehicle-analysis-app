import pandas as pd
import plotly.express as px
import streamlit as st

# Primeiro: carregar os dados
car_data = pd.read_csv('vehicles_us.csv')

# Segundo: criar o cabeçalho
st.header('Dashboard de Análise de Veículos')
 #Criar slider para filtrar por faixa de preço
price_range = st.slider(
    'Selecione a faixa de preço:',
    min_value=int(car_data['price'].min()),
    max_value=int(car_data['price'].max()),
    value=(int(car_data['price'].min()), int(car_data['price'].max()))
  # Filtrar dados baseado no slider
filtered_data = car_data[(car_data['price'] >= price_range[0]) & 
                        (car_data['price'] <= price_range[1])]
)# Criar gráfico de dispersão
st.subheader('Relação entre Preço e Ano do Veículo')
fig_scatter = px.scatter(dados_do_carro, x='model_year', y='price', 
                        title='Preço vs Ano do Carro')
st.plotly_chart(fig_scatter)



# Criar histograma da distribuição de preços
fig_price_dist = px.histogram(car_data, 
                             x='price', 
                             title='Distribuição de Preços dos Carros',
                             labels={'price': 'Preço (USD)', 'count': 'Quantidade de Carros'},
                             nbins=30)  # número de barras no histograma

st.plotly_chart(fig_price_dist)
