from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

# Importar las funciones layout() en lugar de layouts fijos
import pages.home as home
import pages.lineas as lineas
import pages.mapa as mapa
import pages.violencia as violencia 
import pages.ciudades_menos_muertes as menos_muertes
import pages.top_causas as causas
import pages.edades as edades
import pages.sexo_departamento as sexo_dep

# Crear aplicación Dash y servidor para gunicorn
app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server  # Necesario para que funcione en Railway con gunicorn

# Layout principal con menú de navegación
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('🏠 Inicio | ', href='/'),
        dcc.Link('🗺️ Mapa por Departamento | ', href='/mapa'),
        dcc.Link('📈 Muertes por Mes | ', href='/lineas'),
        dcc.Link('🔫 5 Ciudades más Violentas | ', href='/violencia'),
        dcc.Link('🟢 10 Ciudades con Menor Mortalidad | ', href='/menos-muertes'),
        dcc.Link('📋 10 Principales Causas de Muerte | ', href='/causas'),
        dcc.Link('📊 Muertes por Grupo de Edad | ', href='/edades'),
        dcc.Link('🧑‍🤝‍🧑 Muertes por Sexo y Departamento', href='/sexo-departamento')
    ], style={'margin': '20px'}),
    html.Div(id='page-content')
])

# Callback para mostrar la página correspondiente según la URL
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/lineas':
        return lineas.layout()
    elif pathname == '/mapa':
        return mapa.layout()
    elif pathname == '/violencia':
        return violencia.layout()    
    elif pathname == '/menos-muertes':
        return menos_muertes.layout()
    elif pathname == '/causas':
        return causas.layout()
    elif pathname == '/edades':
        return edades.layout()
    elif pathname == '/sexo-departamento':
        return sexo_dep.layout()
    else:
        return home.layout()

# Solo para ejecución local
if __name__ == '__main__':
    app.run(debug=True)
