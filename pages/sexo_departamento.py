import pandas as pd
import plotly.express as px
from dash import html, dcc

def layout():
    df = pd.read_excel("data/NoFetal2019.xlsx")
    df_divipola = pd.read_excel("data/Divipola.xlsx")
    grupo = df.groupby(['COD_DEPARTAMENTO', 'SEXO']).size().reset_index(name='TotalMuertes')
    df_divipola_unique = df_divipola[['COD_DEPARTAMENTO', 'DEPARTAMENTO']].drop_duplicates()
    grupo = pd.merge(grupo, df_divipola_unique, on='COD_DEPARTAMENTO', how='left')

    fig = px.bar(grupo, x='DEPARTAMENTO', y='TotalMuertes', color='SEXO',
                 title='Muertes por Sexo y Departamento', barmode='stack')

    fig.update_layout(xaxis_tickangle=45)

    return html.Div([
        html.H2("Comparación por Sexo y Departamento", style={'textAlign': 'center'}),
        dcc.Graph(figure=fig)
    ])
