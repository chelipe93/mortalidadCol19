import pandas as pd
import plotly.express as px
from dash import html, dcc

def layout():
    # Leer los datos
    df_muertes = pd.read_excel("data/NoFetal2019.xlsx")
    df_divipola = pd.read_excel("data/Divipola.xlsx")

    # Filtrar homicidios
    df_homicidios = df_muertes[df_muertes['MANERA_MUERTE'] == 'Homicidio']

    # Crear clave concatenada en df_muertes
    df_homicidios['COD_CLAVE'] = df_homicidios['COD_DEPARTAMENTO'].astype(str).str.zfill(2) + df_homicidios['COD_MUNICIPIO'].astype(str).str.zfill(3)

    # Agrupar por la nueva clave
    homicidios_por_cod = df_homicidios.groupby('COD_CLAVE').size().reset_index(name='TotalHomicidios')

    # Crear clave concatenada en df_divipola
    df_divipola['COD_CLAVE'] = df_divipola['COD_DEPARTAMENTO'].astype(str).str.zfill(2) + df_divipola['COD_MUNICIPIO'].astype(str).str.zfill(3)

    # Asegurar que no hay duplicados y seleccionar municipios y clave
    df_divipola_unique = df_divipola[['COD_CLAVE', 'MUNICIPIO']].drop_duplicates()

    # Merge usando la clave concatenada
    df_merge = pd.merge(homicidios_por_cod, df_divipola_unique, on='COD_CLAVE', how='left')

    # Eliminar municipios sin nombre (nulos)
    df_merge = df_merge.dropna(subset=['MUNICIPIO'])

    # Tomar los top 5 homicidios
    top5 = df_merge.sort_values(by='TotalHomicidios', ascending=False).head(5)

    # Crear gráfico
    fig = px.bar(
        top5,
        x='TotalHomicidios',
        y='MUNICIPIO',
        orientation='h',
        title='5 Ciudades más Violentas de Colombia - 2019 (Homicidios)',
        labels={'TotalHomicidios': 'Total de Homicidios', 'MUNICIPIO': 'Ciudad'},
        color='TotalHomicidios',
        color_continuous_scale='Reds'
    )

    fig.update_layout(yaxis={'categoryorder':'total ascending'})

    return html.Div([
        html.H2("Top 5 ciudades más violentas (homicidios)", style={'textAlign': 'center'}),
        dcc.Graph(figure=fig)
    ])
