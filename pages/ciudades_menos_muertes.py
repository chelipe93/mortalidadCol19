import pandas as pd
import plotly.express as px
from dash import html, dcc

def layout():
    df_muertes = pd.read_excel("data/NoFetal2019.xlsx")
    df_divipola = pd.read_excel("data/Divipola.xlsx")
    muertes_por_mpio = df_muertes.groupby('COD_MUNICIPIO').size().reset_index(name='TotalMuertes')
    df_divipola_unique = df_divipola[['COD_MUNICIPIO', 'MUNICIPIO']].drop_duplicates()
    df_merge = pd.merge(muertes_por_mpio, df_divipola_unique, on='COD_MUNICIPIO', how='left')
    bottom10 = df_merge.sort_values(by='TotalMuertes').head(10)

    fig = px.pie(bottom10, names='MUNICIPIO', values='TotalMuertes',
                 title='10 Ciudades con Menor Mortalidad', hole=0.3)

    return html.Div([
        html.H2("Ciudades con menor mortalidad", style={'textAlign': 'center'}),
        dcc.Graph(figure=fig)
    ])
