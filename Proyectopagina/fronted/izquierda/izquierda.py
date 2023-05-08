from dash import html, dcc
import dash_bootstrap_components as dbc

izquierda = dbc.Container(
    [
        

        html.Hr(),

        html.Div(
            [
                html.H2('Indice de plasticidad '),
                html.Label('Limite liquido '),
                dcc.Slider(
                    id='Limite_liquido',
                    min=0,
                    max=100,
                    value=55,
                    step=1,
                    marks={i: str(i) for i in range(0, 101, 10)}
                ),
                html.Label('Indice de plasticidad'),
                dcc.Slider(
                    id='Indice_plasticidad',
                    min=0,
                    max=60,
                    value=20,
                    step=1,
                    marks={i: str(i) for i in range(0, 61, 10)}
                ),

                # dcc.Input(id = 'Limite_liquido', value = 55 , type = 'number'),
                # dcc.Input(id = 'Indice_plasticidad', value = 5 , type = 'number'),
                html.Div(id='salidaCartaPlasticidad')
            ]
        ),




        

    ],
    style={'background-color':'white'}
)

relacionvolumen = dbc.Container(
    [
        html.H1('Relaciones volumetricas'),
        html.Hr(),

        html.Div(
            [
                html.Label('Porosidad'),
                html.Br(),
                html.H6('Volumen de vacios (m^3) / Volumen total (m^3) * 100'),
                dcc.Input(id = 'entradaVolumenVacios', value = 1 , type = 'number'),
                dcc.Input(id = 'entradaVolumenTotal', value = 1 , type = 'number'),
                html.Label(id = 'salidaPorosidad'),
            ]
        ),

        html.Div(
            [
                html.Label('Relacion de vacios'),
                html.Br(),
                html.H6('Volumen de vacios (m^3) / Volumen solidos (m^3)'),
                dcc.Input(id = 'entradaVolumenVacios', value = 1 , type = 'number'),
                dcc.Input(id = 'entradaVolumenSolidos', value = 1 , type = 'number'),
                html.Label(id = 'salidaVacios'),
            ]
        ),

        html.Div(
            [
                html.Label('Grado de saturacion'),
                html.Br(),
                html.H6('Volumen de agua (m^3) / Volumen de vacios (m^3) * 100'),
                dcc.Input(id = 'entradaVolumenAgua', value = 1 , type = 'number'),
                dcc.Input(id = 'entradaVolumenVacios', value = 1 , type = 'number'),
                html.Label(id = 'salidaSaturacion'),
            ]
        ),

        html.Hr(),

        
    ],
    style={'background-color':'white'}
)

relaciongravimetricas = dbc.Container(
    [
        html.H1('Relaciones gravimetricas'),
        html.Hr(),

        html.Div(
            [
                html.Label('Humedad'),
                html.Br(),
                html.H6('Peso del agua (gr) / Peso de solidos (gr) * 100'),
                dcc.Input(id = 'entradaPesoAgua', value = 1 , type = 'number'),
                dcc.Input(id = 'entradaPesoSolido', value = 1 , type = 'number'),
                html.Label(id = 'salidaHumedad'),
            ]
        ),

        html.Hr(),

        
    ],
    style={'background-color':'white'}
)


pesosunitarios = dbc.Container(
    [
        html.H1('Pesos unitarios'),
        html.Hr(),

        html.Div(
            [
                html.Label('Peso unitario muestra'),
                html.Br(),
                html.H6('Peso de la muestra (gr) / Volumen de la muestra (m^3)'),
                dcc.Input(id = 'entradaPesoMuestra', value = 1 , type = 'number'),
                dcc.Input(id = 'entradaVolumenMuestra', value = 1 , type = 'number'),
                html.Label(id = 'salidaPesoUnitarioMuestra'),
            ]
        ),
        
        
        html.Div(
            [
                html.Label('Peso unitario solidos'),
                html.Br(),
                html.H6('Peso de los solidos (gr) / Volumen de los solidos (m^3)'),
                dcc.Input(id = 'entradaPesoSolido', value = 1 , type = 'number'),
                dcc.Input(id = 'entradaVolumenSolido', value = 1 , type = 'number'),
                html.Label(id = 'salidaPesoUnitarioSolido'),
            ]
        ),
        
        
        html.Div(
            [
                html.Label('Peso unitario seco'),
                html.Br(),
                html.H6('Peso de los solidos (gr) / Volumen de la muestra (m^3)'),
                dcc.Input(id = 'entradaPesoSolido', value = 1 , type = 'number'),
                dcc.Input(id = 'entradaVolumenMuestra', value = 1 , type = 'number'),
                html.Label(id = 'salidaPesoUnitarioSeco'),
            ]
        ),

            

    ],
    style={'background-color':'white'}
)

graficas = dbc.Container(
    [
        

        html.Hr(),

        html.Div(
            [
                html.H2('Muestra grafica aproximada '),
                html.Label('Peso muestra '),
                dcc.Slider(
                    id='Peso_muestra',
                    min=0,
                    max=100,
                    value=55,
                    step=1,
                    marks={i: str(i) for i in range(0, 101, 10)}
                ),
                html.Label('Peso solidos'),
                dcc.Slider(
                    id='Peso_solidos',
                    min=0,
                    max=60,
                    value=20,
                    step=1,
                    marks={i: str(i) for i in range(0, 61, 10)}
                ),
                html.Label('Peso liquidos'),
                dcc.Slider(
                    id='Peso_liquidos',
                    min=0,
                    max=60,
                    value=20,
                    step=1,
                    marks={i: str(i) for i in range(0, 61, 10)}
                ),
                html.Label('Peso gases'),
                dcc.Slider(
                    id='Peso_gases',
                    min=0,
                    max=60,
                    value=20,
                    step=1,
                    marks={i: str(i) for i in range(0, 61, 10)}
                ),
                
                html.Hr(),
                
                html.Br(),
                html.Br(),
                html.Br(),
                
                html.Hr(),
                
                
                html.Label('Volumen muestra '),
                dcc.Slider(
                    id='Volumen_muestra',
                    min=0,
                    max=100,
                    value=55,
                    step=1,
                    marks={i: str(i) for i in range(0, 101, 10)}
                ),
                html.Label('Volumen solidos'),
                dcc.Slider(
                    id='Volumen_solidos',
                    min=0,
                    max=60,
                    value=20,
                    step=1,
                    marks={i: str(i) for i in range(0, 61, 10)}
                ),
                html.Label('Volumen liquidos'),
                dcc.Slider(
                    id='Volumen_liquidos',
                    min=0,
                    max=60,
                    value=20,
                    step=1,
                    marks={i: str(i) for i in range(0, 61, 10)}
                ),

                
            ]
        ),




        

    ],
    style={'background-color':'white'}
)