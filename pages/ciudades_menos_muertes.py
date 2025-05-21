import pandas as pd
import plotly.express as px
from dash import html, dcc

# Leer los datos
df_muertes = pd.read_excel("data/NoFetal2019.xlsx")
df_divipola = pd.read_excel("data/Divipola.xlsx")

# Agrupar muertes por municipio
muertes_por_mpio = df_muertes.groupby('COD_MUNICIPIO').size().reset_index(name='TotalMuertes')

# Eliminar duplicados en Divipola por si hay múltiples filas por municipio
df_divipola_unique = df_divipola[['COD_MUNICIPIO', 'MUNICIPIO']].drop_duplicates()

# Unir para obtener nombres
df_merge = pd.merge(muertes_por_mpio, df_divipola_unique, on='COD_MUNICIPIO', how='left')

# Tomar las 10 ciudades con menor mortalidad
bottom10 = df_merge.sort_values(by='TotalMuertes', ascending=True).head(10)

# Crear gráfico circular
fig = px.pie(
    bottom10,
    names='MUNICIPIO',
    values='TotalMuertes',
    title='10 Ciudades con Menor Mortalidad en Colombia - 2019',
    hole=0.3  # si prefieres que sea tipo "dona"
)

layout = html.Div([
    html.H2("Ciudades con menor índice de mortalidad", style={'textAlign': 'center'}),
    dcc.Graph(figure=fig)
])
