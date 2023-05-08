import dash
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import math
import matplotlib
import time

#import fronted
from fronted.main import layout

#import backend
from backend.cartaplasticidad import cartaPlasticidad

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = layout





#Calculamos porosidad de la muestra
@app.callback(
    Output('salidaPorosidad', 'children'),
    Input('entradaVolumenVacios', 'value'),
    Input('entradaVolumenTotal', 'value'),
)


def porosidad(entradaVolumenVacios,entradaVolumenTotal):
    porosidad = 100*entradaVolumenVacios/entradaVolumenTotal
    return 'La porosidad de la muestra es: ' + str(porosidad)+'%'


#Calculamos relacion de vacios
@app.callback(
    Output('salidaVacios', 'children'),
    Input('entradaVolumenVacios', 'value'),
    Input('entradaVolumenSolidos', 'value'),
)

def relacionvacios(entradaVolumenVacios,entradaVolumenSolidos):
    relacionvacios = entradaVolumenVacios/entradaVolumenSolidos
    return 'La relacion de vacios es de: ' + str(relacionvacios)

#Calculamos grado de saturacion
@app.callback(
    Output('salidaSaturacion', 'children'),
    Input('entradaVolumenAgua', 'value'),
    Input('entradaVolumenVacios', 'value')
)

def gradosaturacion(entradaVolumenAgua,entradaVolumenVacios):
    gradosaturacion = 100*entradaVolumenAgua/entradaVolumenVacios
    return 'El grado de saturacion es de : ' + str(gradosaturacion)+ '%'


#Calculamos Humedad o contenido de agua
@app.callback(
    Output('salidaHumedad', 'children'),
    Input('entradaPesoAgua', 'value'),
    Input('entradaPesoSolido', 'value')
)

def humedad(entradaPesoAgua,entradaPesoSolido):
    humedad = 100*entradaPesoAgua/entradaPesoSolido
    return 'La humedad de la muestra es: ' + str(humedad)+ '%'

#Calculamos Pesos unitarios de la muestra
@app.callback(
    Output('salidaPesoUnitarioMuestra', 'children'),
    Input('entradaPesoMuestra', 'value'),
    Input('entradaVolumenMuestra', 'value')
)

def pesounitariomuestra(entradaPesoMuestra,entradaVolumenMuestra):
    pesounitariomuestra = entradaPesoMuestra/entradaVolumenMuestra
    return 'El peso unitario de la muestra es: ' + str(pesounitariomuestra)+ ' gr/m3'


#Calculamos Peso unitarios de los solidos
@app.callback(
    Output('salidaPesoUnitarioSolido', 'children'),
    Input('entradaPesoSolido', 'value'),
    Input('entradaVolumenSolido', 'value')
)

def pesounitariosolido(entradaPesoSolido,entradaVolumenSolido):
    pesounitariosolido = entradaPesoSolido/entradaVolumenSolido
    return 'El peso unitario de los solidos es: ' + str(pesounitariosolido)+ ' gr/m3'


#Calculamos Peso unitarios de la muestra seca
@app.callback(
    Output('salidaPesoUnitarioSeco', 'children'),
    Input('entradaPesoSolido', 'value'),
    Input('entradaVolumenMuestra', 'value')
)

def pesounitarioseco(entradaPesoSolido,entradaVolumenMuestra):
    pesounitarioseco = entradaPesoSolido/entradaVolumenMuestra
    return 'El peso unitario seco de la muestra es: ' + str(pesounitarioseco)+ ' gr/m3'


#calculamos la carta de plasticidad
@app.callback(
    Output('salidaCartaPlasticidad', 'children'),
    Input('Limite_liquido', 'value'),
    Input('Indice_plasticidad', 'value')
)

def cartaPlasticidadDash(Limite_liquido, Indice_plasticidad):
    #retrasar la página un segundo
    # time.sleep(1)
    encoded_image, messages = cartaPlasticidad(Limite_liquido, Indice_plasticidad)

    image_element = html.Img(src="data:image/png;base64,{}".format(encoded_image))
    messages_element = html.Label(messages)

    return html.Div([image_element, messages_element])






if __name__ == '__main__':
    app.run_server(debug=True)