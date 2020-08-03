import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px

from datetime import datetime as dt
import json
import numpy as np
import pandas as pd
import requests
import pickle ## to load models.
import joblib

from app import app




## Loading models
#seg_model = pickle.load(open("data/modelo_segmentacion.pkl", 'rb'))
seg_model = joblib.load("data/modelo_segmentacion.pkl")



education_levels = [
                {'label': 'ANALFABETA', 'value': '0'},
                {'label': 'CICLO I', 'value': '2'},
                {'label': 'CICLO II', 'value': '5'},
                {'label': 'CICLO III', 'value': '9'},
                {'label': 'CICLO IV', 'value': '11'},
                {'label': 'PROFESIONAL', 'value': '16'},
                {'label': 'TECNICO', 'value': '13'},
                {'label': 'TECNICO PROFESIONAL', 'value': '13.01'},
                {'label': 'TECNOLOGICO', 'value': '14'},
                {'label': 'ESPECIALIZACION', 'value': '18'},
                {'label': 'MAGISTER', 'value': '18.01'},
                {'label': 'POST GRADO', 'value': '18.02'}
            ]

education_level_map = {
            'ANALFABETA': 0,
            'CICLO I': 2,
            'CICLO II': 5,
            'CICLO III': 9,
            'CICLO IV': 11,
            'TECNICO': 13,
            'TECNOLOGICO': 14,
            'PROFESIONAL': 16,
            'MAGISTER': 18,
            'POST GRADO': 18
}

descripcion = {}
descripcion[0] = "Interno con alta probabilidad de reincidir varias veces."
descripcion[1] = "Interno con alta probabilidad de no estar en prisión domiciliaria y de estar sindicado de delitos contra la salud pública."
descripcion[2] = "Interno con baja probabilidad de estar sindicado de cometer delitos contra la libertad, integridad y formación sexual, con baja probabilidad de reincidir más de una vez, con alta probabilidad de no estar en prisión domiciliaria y con baja probabilidad de estar sindicado de delitos contra la salud pública."
descripcion[3] = "Interno con alta probabilidad de estar en prisión domiciliaria y con alto nivel educativo."
descripcion[4] = "Interno con alta probabilidad de estar sindicado de cometer delitos contra la libertad, integridad y formación sexual, pero baja probabilidad de estar sindicado de cometer delitos contra la seguridad pública y contra el patrimonio económico. Muy baja probabilidad de estar sindicado de cometer delitos contra los derechos de autor y contra los recursos naturales y el medio ambiente. Este interno es el perfil que, en promedio, pasa menos días libre, antes de reincidir de nuevo."
descripcion[5] = "Interno con alta probabilidad de estar en prisión domiciliaria y de estar sindicado de cometer delitos contra la salud pública pero baja probabilidad de estar sindicado de delitos contra el patrimonio económico. Este interno es el perfil que, en promedio, pasa más días libre, antes de reincidir de nuevo."
descripcion[6] = "Interno con alta probabilidad de estar en prisión domiciliaria y con bajo nivel educativo."



proporciondelitos_input = dbc.FormGroup(
    [
        dbc.Label("Proporción de delitos contra libertad, integridad y formación sexual:",
                    html_for="prop_delitos_slider"),
        dcc.Slider(
            id='prop_delitos_slider',
            min=0,
            max=1,
            step=0.05,
            value=0.5,
        )
    ]
)

proporciondelitossalud_input = dbc.FormGroup(
    [
        dbc.Label("Proporción de delitos contra la salud pública:",
                    html_for="prop_delitos_salud_slider"),
        dcc.Slider(
            id='prop_delitos_salud_slider',
            min=0,
            max=1,
            step=0.05,
            value=0.5,
        )
    ]
)

education_input = dbc.FormGroup(
    [
        dbc.Label("Nivel de Educación:", html_for="education_dropdown"),
        dcc.Dropdown(
            id='education_dropdown_segmentacion',
            options= education_levels,
            value='9'
        )
    ]
)

events_input = dbc.FormGroup(
    [
        dbc.Label("Reincidencias:", html_for="events_text_segmentacion"),
        dbc.Input(type="number", value="2", min=0, max=20, step=1, id="events_text_segmentacion")
    ]
)

age_input = dbc.FormGroup(
    [
        dbc.Label("Edad:", html_for="age_text_segmentacion"),
        html.Div(id='age_slider_segmentacion-container'),
        dbc.Input(type="number", min=18, max=100, value="21", step=1, id="age_text_segmentacion")

    ]
)

jail_switch = dbc.FormGroup(
    [
        dbc.Checklist(
            options=[
                {"label": "Carcel", "value": 1},
            ],
            value=[],
            id="jail_toogle_segmentacion",
            switch=True,
        ),
    ]
)

dias_captura_input = dbc.FormGroup(
    [
        dbc.Label("Días entre capturas:", html_for="dias_captura_slider-container"),
        html.Div(id='dias_captura_slider-container'),
        dbc.Input(type="number", min=0, max=10000, value="100", step=1, id="dias_captura_text")

    ]
)

dias_libre_input = dbc.FormGroup(
    [
        dbc.Label("Días libre:", html_for="dias_libre_slider-container"),
        html.Div(id='dias_libre_slider-container'),
        dbc.Input(type="number", min=0, max=10000, value="100", step=1, id="dias_libre_text")

    ]
)


card_segmentacion = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Segmentación", className="card-title"),
                html.P(
                    children=["init"],
                    className="card-text",
                    id="card_segmentacion",
                ),
            ]
        ),
    ],
    style={"width": "18rem"},

)


formLayout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    children = [
                        proporciondelitos_input,
                        proporciondelitossalud_input,
                        education_input,
                        events_input,
                        age_input,
                        jail_switch,
                        dias_captura_input,
                        dias_libre_input,
                    ],
                    md="4"
                ),
                dbc.Col(
                    children = [
                        #dcc.Graph(id='result_output')
                        dbc.Row(
                            [
                                card_segmentacion
                            ]
                        ),
                    ],
                    md="8"
                )
            ]
        )

    ]
)

@app.callback(
    Output("card_segmentacion", "children"),
    [Input('education_dropdown_segmentacion', 'value'),
    Input('prop_delitos_slider', 'value'),
    Input('prop_delitos_salud_slider', 'value'),
     Input('events_text_segmentacion', 'value'),
     Input('age_text_segmentacion', 'value'),
     Input('jail_toogle_segmentacion', 'value'),
     Input('dias_captura_text', 'value'),
     Input('dias_libre_text', 'value'),
     ]
)
def update_text_segmentacion(education,prop_delitos_1,prop_delitos_salud, events, age, jail, dias_captura, dias_libre):
    #1.1. Get info from local model

    interaccion = pd.DataFrame([float(prop_delitos_1), int(events), len(jail), float(prop_delitos_salud),
                                int(age), int(float(education)), int(dias_captura), int(dias_libre)]).T
    interaccion.columns = ['CONTRA LA LIBERTAD INTEGRIDAD Y FORMACION SEXUALES',
                 'NUMERO_REINCIDENCIAS', 'EN_CARCEL', 'CONTRA LA SALUD PUBLICA',
                 'EDAD', 'NIVEL_EDUCATIVO', 'DIAS_CAPTURA', 'DIAS_LIBRE']
    #print("-------------------------------------")
    #print(interaccion)
    #print(interaccion.shape)
    model_result = seg_model.predict(interaccion)
    #print(model_result)
    descrip_result = descripcion[model_result[0]]
    #print(descrip_result)
    #print("-------------------------------------")
    final_result = "Cluster " + str(model_result[0]) + ": " + descrip_result
    return final_result
