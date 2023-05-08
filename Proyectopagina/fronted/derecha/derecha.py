from dash import html
import dash_bootstrap_components as dbc

derecha = dbc.Container(
    [
        # html.H2('Datos del proyecto'),
        # html.Hr(),
        # html.Label('Nombre:'),
        # dbc.Input(value="Nombre"),
        # html.Label('Localización:'),
        # dbc.Input(value="Localización"),
        # html.Label('Fecha Inicio:'),
        # dbc.Input(value="Fecha", type="date"),
        # html.Label('Fecha Fin:'),
        # dbc.Input(value="Fecha", type="date"),
        
        html.H3('Suelo CH'),
        html.Hr(),
        html.H6('Este suelo tiene propiedades por qeu blablabla'),
        html.H3('Suelo MH'),
        html.Hr(),
        html.H6('Este suelo tiene propiedades por qeu blablabla'),
        html.H3('Suelo CL'),
        html.Hr(),
        html.H6('Este suelo tiene propiedades por qeu blablabla'),
        html.H3('Suelo ML'),
        html.Hr(),
        html.H6('Este suelo tiene propiedades por qeu blablabla'),
        html.H3('Suelo CL-ML'),
        html.Hr(),
        html.H6('Este suelo tiene propiedades por qeu blablabla'),
    ]
)


