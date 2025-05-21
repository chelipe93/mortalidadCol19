import pandas as pd
import plotly.express as px
from dash import html, dcc

# Leer datos
df = pd.read_excel("data/NoFetal2019.xlsx")
df_divipola = pd.read_excel("data/Divipola.xlsx")

# Agrupar por departamento y sexo
grupo = df.groupby(['COD_DEPARTAMENTO', 'SEXO']).size().reset_index(name='TotalMuertes')

# Unir para obtener nombre del departamento
df_divipola_unique = df_divipola[['COD_DEPARTAMENTO', 'DEPARTAMENTO']].drop_duplicates()
grupo = pd.merge(grupo, df_divipola_unique, on='COD_DEPARTAMENTO', how='left')

# Crear gráfico apilado
fig = px.bar(
    grupo,
    x='DEPARTAMENTO',
    y='TotalMuertes',
    color='SEXO',
    title='Muertes por Sexo y Departamento - Colombia 2019',
    labels={'DEPARTAMENTO': 'Departamento', 'TotalMuertes': 'Total de Muertes', 'SEXO': 'Sexo'},
)

fig.update_layout(barmode='stack', xaxis_tickangle=45)

layout = html.Div([
    html.H2("Comparación de Muertes por Sexo y Departamento", style={'textAlign': 'center'}),
    dcc.Graph(figure=fig)
])
