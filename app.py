from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pages.home as home
import pages.lineas as lineas
import pages.mapa as mapa
import pages.violencia as violencia 
import pages.ciudades_menos_muertes as menos_muertes
import pages.top_causas as causas
import pages.edades as edades
import pages.sexo_departamento as sexo_dep

# Crear la aplicación Dash
app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server  # <- Esto es necesario para Gunicorn y Railway

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('🏠 Inicio | ', href='/'),
        dcc.Link('🗺️ Mapa por Departamento | ', href='/mapa'),
        dcc.Link('📈 Muertes por Mes', href='/lineas'),
        dcc.Link('🔫 5 Ciudades más Violentas', href='/violencia'),
        dcc.Link('🟢 10 Ciudades con Menor Mortalidad', href='/menos-muertes'),
        dcc.Link('📋 10 Principales Causas de Muerte', href='/causas'),
        dcc.Link('📊 Muertes por Grupo de Edad', href='/edades'),
        dcc.Link('🧑‍🤝‍🧑 Muertes por Sexo y Departamento', href='/sexo-departamento')
    ], style={'margin': '20px'}),
    html.Div(id='page-content')
])

@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/lineas':
        return lineas.layout
    elif pathname == '/mapa':
        return mapa.layout
    elif pathname == '/violencia':
        return violencia.layout    
    elif pathname == '/menos-muertes':
        return menos_muertes.layout
    elif pathname == '/causas':
        return causas.layout
    elif pathname == '/edades':
        return edades.layout
    elif pathname == '/sexo-departamento':
        return sexo_dep.layout
    else:
        return home.layout  # Asegura que devuelva la home por defecto

if __name__ == '__main__':
    app.run(debug=True)
