import pandas as pd
import plotly.express as px
from dash import html, dcc

# Cargar datos
df = pd.read_excel("data/NoFetal2019.xlsx")

# Crear columna de fecha artificial con día fijo (01 de cada mes)
df['FECHA'] = pd.to_datetime(df['AÑO'].astype(str) + '-' + df['MES'].astype(str).str.zfill(2) + '-01')

# Agrupar por mes
muertes_por_mes = df.groupby('FECHA').size().reset_index(name='TotalMuertes')

# Crear gráfico de líneas
fig = px.line(
    muertes_por_mes,
    x='FECHA',
    y='TotalMuertes',
    markers=True,
    title='Muertes Totales por Mes en Colombia - 2019',
    labels={'FECHA': 'Mes', 'TotalMuertes': 'Número de Muertes'}
)

layout = html.Div([
    html.H2("Variación mensual de muertes en Colombia (2019)", style={'textAlign': 'center'}),
    dcc.Graph(figure=fig)
])
