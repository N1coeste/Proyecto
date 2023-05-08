from dash import html
import dash_bootstrap_components as dbc

logo = dbc.Container(
    [
        html.Img(src="https://www.udistrital.edu.co/themes/custom/versh/logo.png"),
    ]
)

links = dbc.Container(
    [
        html.Link(href="https://www.udistrital.edu.co/inicio"),
    ]
)