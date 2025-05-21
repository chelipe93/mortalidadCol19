from dash import html

def layout():
    link_style = {
        'display': 'inline-block',
        'padding': '15px 25px',
        'margin': '10px',
        'fontSize': '18px',
        'color': '#fff',
        'backgroundColor': '#007BFF',
        'borderRadius': '8px',
        'textDecoration': 'none',
        'textAlign': 'center',
        'boxShadow': '0 4px 6px rgba(0,0,0,0.1)',
        'transition': 'background-color 0.3s ease, transform 0.2s ease',
        'width': '250px',
        'userSelect': 'none',
    }
    link_hover_style = {
        'backgroundColor': '#0056b3',
        'transform': 'scale(1.05)',
        'cursor': 'pointer',
    }

    # Para el hover, Dash no soporta inline CSS para hover directamente,
    # pero si usas un CSS externo puedes agregarlo o usar dash-bootstrap-components.
    # Por simplicidad aquí solo damos el estilo base.

    container_style = {
        'maxWidth': '900px',
        'margin': '40px auto',
        'textAlign': 'center',
        'fontFamily': "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
    }

    grid_style = {
        'display': 'grid',
        'gridTemplateColumns': 'repeat(auto-fit, minmax(250px, 1fr))',
        'gap': '20px',
        'justifyItems': 'center',
    }

    return html.Div([
        html.H1("Análisis de Mortalidad en Colombia (2019)", style={'marginBottom': '50px', 'color': '#333'}),
        html.Div([
            html.A('🗺️ Mapa por Departamento', href='/mapa', style=link_style),
            html.A('📈 Muertes por Mes', href='/lineas', style=link_style),
            html.A('🔫 5 Ciudades más Violentas', href='/violencia', style=link_style),
            html.A('🟢 10 Ciudades con Menor Mortalidad', href='/menos-muertes', style=link_style),
            html.A('📋 10 Principales Causas de Muerte', href='/causas', style=link_style),
            html.A('📊 Muertes por Grupo de Edad', href='/edades', style=link_style),
            html.A('🧑‍🤝‍🧑 Muertes por Sexo y Departamento', href='/sexo-departamento', style=link_style),
        ], style=grid_style)
    ], style=container_style)
