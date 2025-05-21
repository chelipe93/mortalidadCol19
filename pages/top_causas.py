import pandas as pd
from dash import html
from dash import dash_table

def layout():
    df = pd.read_excel("data/NoFetal2019.xlsx")
    top_causas = (df.groupby(['COD_MUERTE', 'MANERA_MUERTE'])
                    .size()
                    .reset_index(name='TotalCasos')
                    .sort_values(by='TotalCasos', ascending=False)
                    .head(10))

    return html.Div([
        html.H2("10 Principales Causas de Muerte", style={'textAlign': 'center'}),
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
