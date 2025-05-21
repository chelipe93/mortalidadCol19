import pandas as pd
import plotly.express as px
from dash import html, dcc

def layout():
    df = pd.read_excel("data/NoFetal2019.xlsx")
    df = df.dropna(subset=['GRUPO_EDAD1'])
    edad_agrupada = df.groupby('GRUPO_EDAD1').size().reset_index(name='TotalMuertes')
    edad_agrupada = edad_agrupada.sort_values('GRUPO_EDAD1')

    fig = px.bar(edad_agrupada, x='GRUPO_EDAD1', y='TotalMuertes',
                 title='Distribución de Muertes por Edad',
                 color='TotalMuertes', color_continuous_scale='Blues')

    return html.Div([
        html.H2("Distribución de Muertes por Grupo de Edad", style={'textAlign': 'center'}),
        dcc.Graph(figure=fig)
    ])
