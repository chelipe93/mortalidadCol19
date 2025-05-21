from dash import html, dcc

def layout():
    return html.Div([
        html.H1("Análisis de Mortalidad en Colombia (2019)", style={'textAlign': 'center', 'marginBottom': '40px'}),
        html.Div([dcc.Link('🗺️ Mapa por Departamento', href='/mapa')], style={'margin': '10px'}),
        html.Div([dcc.Link('📈 Muertes por Mes', href='/lineas')], style={'margin': '10px'}),
        html.Div([dcc.Link('🔫 5 Ciudades más Violentas', href='/violencia')], style={'margin': '10px'}),
        html.Div([dcc.Link('🟢 10 Ciudades con Menor Mortalidad', href='/menos-muertes')], style={'margin': '10px'}),
        html.Div([dcc.Link('📋 10 Principales Causas de Muerte', href='/causas')], style={'margin': '10px'}),
        html.Div([dcc.Link('📊 Muertes por Grupo de Edad', href='/edades')], style={'margin': '10px'}),
        html.Div([dcc.Link('🧑‍🤝‍🧑 Muertes por Sexo y Departamento', href='/sexo-departamento')], style={'margin': '10px'}),
    ])
