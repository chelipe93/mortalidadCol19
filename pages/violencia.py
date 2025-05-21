import pandas as pd
import plotly.express as px
from dash import html, dcc

def layout():
    # Leer los datos
    df_muertes = pd.read_excel("data/NoFetal2019.xlsx")
    df_divipola = pd.read_excel("data/Divipola.xlsx")

    # Filtrar homicidios: códigos que empiezan con 'X95'
    df_homicidios = df_muertes[df_muertes['COD_MUERTE'].astype(str).str.startswith('X95')]

    # Agrupar por COD_MUNICIPIO
    homicidios_por_cod = df_homicidios.groupby('COD_MUNICIPIO').size().reset_index(name='TotalHomicidios')

    # Asegurar que no hay duplicados en municipios
    df_divipola_unique = df_divipola[['COD_MUNICIPIO', 'MUNICIPIO']].drop_duplicates()

    # Unir nombres de municipios
    df_merge = pd.merge(homicidios_por_cod, df_divipola_unique, on='COD_MUNICIPIO', how='left')

    # Eliminar municipios sin nombre por si hay nulos
    df_merge = df_merge.dropna(subset=['MUNICIPIO'])

    # Tomar los 5 con mayor número de homicidios
    top5 = df_merge.sort_values(by='TotalHomicidios', ascending=False).head(5)

    # Crear gráfico de barras horizontal
    fig = px.bar(
        top5,
        x='TotalHomicidios',
        y='MUNICIPIO',
        orientation='h',
        title='5 Ciudades más Violentas de Colombia - 2019 (Homicidios - X95)',
        labels={'TotalHomicidios': 'Total de Homicidios', 'MUNICIPIO': 'Ciudad'},
        color='TotalHomicidios',
        color_continuous_scale='Reds'
    )

    fig.update_layout(yaxis={'categoryorder':'total ascending'})  # ordena de mayor a menor visualmente

    return html.Div([
        html.H2("Top 5 ciudades más violentas (homicidios)", style={'textAlign': 'center'}),
        dcc.Graph(figure=fig)
    ])
