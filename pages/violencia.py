import pandas as pd
import plotly.express as px
from dash import html, dcc

# Leer los datos
df_muertes = pd.read_excel("data/NoFetal2019.xlsx")
df_divipola = pd.read_excel("data/Divipola.xlsx")

# Filtrar homicidios (códigos que comienzan con 'X95')
df_homicidios = df_muertes[df_muertes['COD_MUERTE'].astype(str).str.startswith('X95')]

# Agrupar por código de municipio
homicidios_por_cod = df_homicidios.groupby('COD_MUNICIPIO').size().reset_index(name='TotalHomicidios')

# Asegurarnos de que cada municipio aparece una vez
df_divipola_unique = df_divipola[['COD_MUNICIPIO', 'MUNICIPIO']].drop_duplicates()

# Unir para obtener nombres de ciudades
df_merge = pd.merge(homicidios_por_cod, df_divipola_unique, on='COD_MUNICIPIO', how='left')

# Ordenar y tomar top 5
top5 = df_merge.sort_values(by='TotalHomicidios', ascending=False).head(5)

# Crear gráfico
fig = px.bar(
    top5,
    x='MUNICIPIO',
    y='TotalHomicidios',
    color='TotalHomicidios',
    title='5 Ciudades más Violentas de Colombia - 2019 (Homicidios - Códigos X95)',
    labels={'MUNICIPIO': 'Ciudad', 'TotalHomicidios': 'Total de Homicidios'},
    color_continuous_scale='OrRd'
)

layout = html.Div([
    html.H2("Top 5 ciudades más violentas (homicidios)", style={'textAlign': 'center'}),
    dcc.Graph(figure=fig)
])
