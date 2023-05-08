from dash import html
import dash_bootstrap_components as dbc

#importar componentes del navegador
from .descripcion.visualizacion import visualizacion
from .descripcion.rayas import tituloprincipal
from .descripcion.usuario import usuario


navegador = dbc.Container(
    [
        html.H1('PROYECTO FINAL'),
        html.H6('Programacion ||'),
        dbc.Row(
            [
                dbc.Col(tituloprincipal, md=9 , style={'background-color':'gray'}),
                dbc.Col(usuario,md =3, style={'background-color':'yellow'}),
            ]
        )
    ]
)
