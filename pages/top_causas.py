import pandas as pd
from dash import html, dcc
from dash import dash_table

# Cargar datos
df = pd.read_excel("data/NoFetal2019.xlsx")

# Agrupar por código y nombre de causa
top_causas = (
    df.groupby(['COD_MUERTE', 'MANERA_MUERTE'])
    .size()
    .reset_index(name='TotalCasos')
    .sort_values(by='TotalCasos', ascending=False)
    .head(10)
)

layout = html.Div([
    html.H2("10 Principales Causas de Muerte - Colombia 2019", style={'textAlign': 'center'}),
    dash_table.DataTable(
        columns=[
            {"name": "Código", "id": "COD_MUERTE"},
            {"name": "Causa de Muerte", "id": "MANERA_MUERTE"},
            {"name": "Total de Casos", "id": "TotalCasos"}
        ],
        data=top_causas.to_dict('records'),
        style_table={'margin': '30px auto', 'width': '80%'},
        style_cell={'textAlign': 'left'},
        style_header={'fontWeight': 'bold'},
    )
])
