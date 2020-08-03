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

from app import app
# Call Webservice to get Crimes List:
r = requests.get("http://ds4at6api.azurewebsites.net/api/Crimes")
df_crimes =pd.read_json(r.text)
df_crimes = df_crimes.rename(columns={'name': 'label', 'crimeId': 'value'})
#print(df_crimes)
df_dropdown_crimes = df_crimes[['label', 'value']]
#df_crimes = df_crimes.drop(['crimeId'], axis = 1)
# Convert to a dictionary to let dropdown use it
crimes = json.loads(df_dropdown_crimes.to_json(orient="records"))

## Loading models
cluster_model_1 = pickle.load(open("data/nb_model_no_education.pickle", 'rb'))
cluster_model_2 = pickle.load(open("data/nb_model_education.pickle", 'rb'))

cluster1_map = {
	0:"Grupo medianamente poblado, nivel variado de educación, crímenes de reincidencia medianamente altos, cumplimiento de pena fuera de la cárcel, donde la mayoría no realiza actividades de trabajo ni actividades de estudio. En su mayoría son hombres.",
	1:"Grupo altamente poblado, nivel variado de educación, crímenes de reincidencia generalmente altos, cumplimiento de pena dentro de la cárcel, donde la mayoría realiza actividades de trabajo y estudio. En su mayoría son hombres.",
	2:"Grupo medianamente poblado, nivel variado de educación, crímenes de reincidencia medianamente altos, cumplimiento de pena dentro de la cárcel, donde la mayoría realiza actividades de trabajo pero no actividades de estudio. En su mayoría son hombres.",
	3:"Grupo altamente poblado, nivel variado de educación, crímenes de reincidencia generalmente altos, cumplimiento de pena fuera de la cárcel, donde la mayoría realiza actividades de trabajo y actividades de estudio. En su mayoría son hombres.",
	4:"Grupo altamente poblado, nivel variado-bajo de educación, crímenes de reincidencia medianamente altos, cumplimiento de pena dentro de la cárcel, donde la mayoría no realiza actividades de trabajo pero sí actividades de estudio. En su mayoría son hombres.",
	5:"Grupo medianamente poblado, nivel variado de educación, crímenes de reincidencia generalmente altos, cumplimiento de pena fuera de la cárcel, donde la mayoría no realiza actividades de trabajo pero sí actividades de estudio. En su mayoría son hombres.",
	6:"Grupo bajamente poblado, nivel variado de educación, crímenes de reincidencia bajos, cumplimiento de pena dentro y fuera de la cárcel, donde se realiza o no actividades de trabajo y estudio en partes similares. En su mayoría son hombres.",
	7:"Grupo bajamente poblado, nivel variado de educación, crímenes de reincidencia medianamente altos, cumplimiento de pena dentro de la cárcel en partes similares, donde la mayoría no realiza actividades de trabajo ni actividades de estudio. En su mayoría son hombres.",
}
cluster2_map = {
	0:"Grupo medianamente poblado, nivel bajo de educación, crímenes de reincidencia generalmente altos, cumplimiento de pena fuera de la cárcel, donde la mayoría realiza actividades de trabajo y estudio. En su mayoría son hombres.",
	1:"Grupo medianamente poblado, nivel alto de educación, crímenes de reincidencia generalmente altos, cumplimiento de pena fuera de la cárcel, donde se realiza o no actividades de trabajo en partes similares y la mayoría realiza actividades de estudio. En su mayoría son hombres.",
	2:"Grupo medianamente poblado, nivel bajo de educación, crímenes de reincidencia medianamente altos, cumplimiento de pena dentro de la cárcel, donde la mayoría realiza actividades de trabajo pero no actividades de estudio. En su mayoría son hombres.",
	3:"Grupo altamente poblado, nivel bajo de educación, crímenes de reincidencia generalmente altos, cumplimiento de pena dentro de la cárcel mayormente, donde la mayoría realiza actividades de trabajo y actividades de estudio. En su mayoría son hombres.",
	4:"Grupo altamente poblado, nivel bajo de educación, crímenes de reincidencia generalmente altos, cumplimiento de pena dentro de la cárcel, donde no se realizan actividades de trabajo pero la mayoría realiza actividades de estudio. En su mayoría son hombres.",
	5:"Grupo medianamente poblado, nivel variado de educación, crímenes de reincidencia generalmente altos, cumplimiento de pena dentro y fuera de la cárcel, donde se realiza o no actividades de trabajo y estudio en partes similares. En su mayoría son mujeres.",
	6:"Grupo bajamente poblado, nivel alto de educación, crímenes de reincidencia generalmente altos, cumplimiento de pena fuera de la cárcel mayormente, donde la mayoría no realiza actividades de trabajo ni actividades de estudio. En su mayoría son hombres.",
	7:"Grupo medianamente poblado, nivel medio-alto de educación, crímenes de reincidencia generalmente altos, cumplimiento de pena dentro de la cárcel, donde la mayoría no realiza actividades de trabajo pero sí actividades de estudio. En su mayoría son hombres.",
	8:"Grupo altamente poblado, nivel medio-alto de educación, crímenes de reincidencia generalmente altos, cumplimiento de pena dentro de la cárcel, donde la mayoría realiza actividades de trabajo y las actividades de estudio se realizan o no en partes similares. En su mayoría son hombres.",
	9:"Grupo medianamente poblado, nivel bajo de educación, crímenes de reincidencia generalmente altos, cumplimiento de pena fuera de la cárcel, donde la mayoría no realiza actividades de trabajo y las actividades de estudio se realizan o no en partes similares. En su mayoría son hombres.",
}


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


education_input = dbc.FormGroup(
    [
        dbc.Label("Nivel de Educación:", html_for="education_dropdown"),
        dcc.Dropdown(
            id='education_dropdown_cluster',
            options= education_levels,
            value='9'
        )
    ]
)

studies_input = dbc.FormGroup(
    [
        dbc.Checklist(
            options=[
                {"label": "Realiza estudios en el centro de reclusión", "value": 1},
            ],
            value=[],
            id="studies_toogle_cluster",
            switch=True,
        ),
    ]
)
working_input = dbc.FormGroup(
    [
        dbc.Checklist(
            options=[
                {"label": "Realiza actividades de trabajo", "value": 1},
            ],
            value=[],
            id="working_toogle",
            switch=True,
        ),
    ]
)
crime_input = dbc.FormGroup(
    [
        dbc.Label("Crimen:", html_for="crime_dropdown_cluster"),
        dcc.Dropdown(
            id='crime_dropdown_cluster',
            options= crimes,
            value="260"
        )
    ]
)

jail_switch = dbc.FormGroup(
    [
        dbc.Checklist(
            options=[
                {"label": "Carcel", "value": 1},
            ],
            value=[],
            id="jail_toogle",
            switch=True,
        ),
    ]
)
gender_switch = dbc.FormGroup(
    [
        dbc.Checklist(
            options=[
                {"label": "Mujer-Hombre", "value": 1},
            ],
            value=[],
            id="gender_toogle",
            switch=True,
        ),
    ]
)

card_cluster1 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Cluster 1", className="card-title"),
                html.P(
                    children=["init"],
                    className="card-text",
                    id="card_cluster1_text",
                ),
            ]
        ),
    ],
    style={"width": "18rem"},

)

card_cluster2 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Cluster 2", className="card-title"),
                html.P(
                    children=["init2"],
                    className="card-text",
                    id="card_cluster2_text",
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
                        education_input,
                        studies_input,
                        working_input,
                        crime_input,
                        jail_switch,
                        gender_switch

                    ],
                    md="4"
                ),
                dbc.Col(
                    children = [
                        #dcc.Graph(id='result_output')
                        dbc.Row(
                            [
                                card_cluster1
                            ]
                        ),
                        dbc.Row(
                            [
                                card_cluster2
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
    [Output("card_cluster1_text", "children"),
    Output("card_cluster2_text", "children")],
    [Input('education_dropdown_cluster', 'value'),
     Input('crime_dropdown_cluster', 'value'),
     Input('studies_toogle_cluster', 'value'),
     Input('working_toogle', 'value'),
     Input('jail_toogle', 'value'),
     Input('gender_toogle', 'value'),
     ]
)
def update_text_cluster(education, crime, studies, working, jail, gender):
    # Load crime weight:
    if len(df_crimes[df_crimes.value == int(crime)]) > 0:
        weight = int(df_crimes[df_crimes.value == int(crime)].weight)
    else:
        weight = 5
    #1.1. Get info from local model
    ##inputs: covariates = ['NIVEL_EDUCATIVO','logDelito','EN_CARCEL',
    #'ACTIVIDADES_TRABAJO_SI','ACTIVIDADES_ESTUDIO_SI','GENERO_MASCULINO']
    input_1 = pd.DataFrame([float(int(float(education))*1.8), weight*2.5, len(jail), len(working),
                                len(studies), len(gender)*1]).T
    input_2 = pd.DataFrame([float(int(float(education))*3.5), weight*2, len(jail), len(working),
                                len(studies), len(gender)*2]).T
    input_1.columns = ['NIVEL_EDUCATIVO','logDelito','EN_CARCEL',
                        'ACTIVIDADES_TRABAJO_SI','ACTIVIDADES_ESTUDIO_SI','GENERO_MASCULINO']
    input_2.columns = ['NIVEL_EDUCATIVO','logDelito','EN_CARCEL',
                        'ACTIVIDADES_TRABAJO_SI','ACTIVIDADES_ESTUDIO_SI','GENERO_MASCULINO']
    cluster1_result = cluster_model_1.predict(input_1)[0]
    cluster2_result = cluster_model_2.predict(input_2)[0]

    final_cluster1_result = "Cluster " + str(cluster1_result) + ": " + cluster1_map[cluster1_result]
    final_cluster2_result = "Cluster " + str(cluster2_result) + ": " + cluster2_map[cluster2_result]
    return final_cluster1_result,final_cluster2_result
