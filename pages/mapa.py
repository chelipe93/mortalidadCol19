import pandas as pd
import plotly.express as px
from dash import html, dcc
import json

def layout():
    df_muertes = pd.read_excel("data/NoFetal2019.xlsx")
    df_divipola = pd.read_excel("data/Divipola.xlsx")
    with open("data/Colombia.geo.json", encoding="utf-8") as f:
        geojson = json.load(f)

    muertes_por_depto = df_muertes.groupby('COD_DEPARTAMENTO').size().reset_index(name='TotalMuertes')
    df_merge = pd.merge(muertes_por_depto, df_divipola[['COD_DEPARTAMENTO', 'DEPARTAMENTO']], on='COD_DEPARTAMENTO', how='left')
    df_merge['COD_DEPARTAMENTO'] = df_merge['COD_DEPARTAMENTO'].astype(str).str.zfill(2)

    fig = px.choropleth(df_merge, geojson=geojson, locations='COD_DEPARTAMENTO',
                        featureidkey="properties.DPTO", color='TotalMuertes',
                        hover_name='DEPARTAMENTO', color_continuous_scale="Reds")
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":50,"l":0,"b":0})

    return html.Div([
        html.H2("Distribución geográfica de muertes", style={'textAlign': 'center'}),
        dcc.Graph(figure=fig)
    ])
