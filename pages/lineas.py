import pandas as pd
import plotly.express as px
from dash import html, dcc

def layout():
    df = pd.read_excel("data/NoFetal2019.xlsx")
    df['FECHA'] = pd.to_datetime(df['AÑO'].astype(str) + '-' + df['MES'].astype(str).str.zfill(2) + '-01')
    muertes_por_mes = df.groupby('FECHA').size().reset_index(name='TotalMuertes')

    fig = px.line(muertes_por_mes, x='FECHA', y='TotalMuertes', markers=True,
                  title='Muertes por Mes', labels={'FECHA': 'Mes', 'TotalMuertes': 'Muertes'})

    return html.Div([
        html.H2("Variación mensual de muertes", style={'textAlign': 'center'}),
        dcc.Graph(figure=fig)
    ])
