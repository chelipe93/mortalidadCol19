import pandas as pd
import plotly.express as px
from dash import html, dcc

# Leer datos
df = pd.read_excel("data/NoFetal2019.xlsx")

# Eliminar nulos en edad
df = df.dropna(subset=['GRUPO_EDAD1'])

# Agrupar por grupo quinquenal
edad_agrupada = df.groupby('GRUPO_EDAD1').size().reset_index(name='TotalMuertes')

# Ordenar por rango (si ya están en orden textual tipo '0-4', '5-9' etc.)
edad_agrupada = edad_agrupada.sort_values('GRUPO_EDAD1')

# Crear histograma
fig = px.bar(
    edad_agrupada,
    x='GRUPO_EDAD1',
    y='TotalMuertes',
    title='Distribución de Muertes por Grupo de Edad (2019)',
    labels={'GRUPO_EDAD1': 'Grupo de Edad', 'TotalMuertes': 'Muertes'},
    color='TotalMuertes',
    color_continuous_scale='Blues'
)

layout = html.Div([
    html.H2("Distribución de Muertes por Edad", style={'textAlign': 'center'}),
    dcc.Graph(figure=fig)
])
