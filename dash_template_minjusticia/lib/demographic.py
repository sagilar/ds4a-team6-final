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

#Recall app
from app import app

def tieneHijos(x):
    if x == 1:
        return "Si"
    else:
        return "No"

rKids = requests.get("http://ds4at6api.azurewebsites.net/api/PersonsByAttributes/api/PersonAttributes/HasKids")
dfKids =pd.read_json(rKids.text)
dfKids["hasKids"] = dfKids['hasKids'].apply(tieneHijos)

rMaritalStatus = requests.get("http://ds4at6api.azurewebsites.net/api/CrimesByMaritalStatus")
dfMaritalStatus =pd.read_json(rMaritalStatus.text)

rEducationLevel = requests.get("http://ds4at6api.azurewebsites.net/api/CrimesByScholarship")
dfEducationLevel =pd.read_json(rEducationLevel.text)

rSpecialCondition = requests.get("http://ds4at6api.azurewebsites.net/api/PersonsByAttributes/api/PersonAttributes/SpecialCondition")
dfSpecialCondition =pd.read_json(rSpecialCondition.text)

rAgeAndSex = requests.get("http://ds4at6api.azurewebsites.net/api/PersonsByAttributes/api/PersonAttributes/AgeAndSex")
dfAgeAndSex =pd.read_json(rAgeAndSex.text)

MS_hist = px.histogram(dfMaritalStatus,x="maritalStatus",y="events",nbins=50,hover_data=["maritalStatus","events"])
MS_hist.update_layout(title="Histograma de Estado Civil", xaxis_title = "Estado Civil", yaxis_title = "# Reincidentes")

MC_hist = px.histogram(dfKids,x="hasKids",y="events",nbins=50,hover_data=["hasKids","events"],color="hasKids")
MC_hist.update_layout(title="Histograma de Hijos Menores", xaxis_title = "Tiene Hijos", yaxis_title = "# Reincidentes", legend_title = "Tiene Hijos")

EL_hist = px.histogram(dfEducationLevel,x="scholarship",y="events",nbins=50,hover_data=["scholarship","events"])
EL_hist.update_layout(title="Histograma de Nivel de Educación", xaxis_title = "Escolaridad", yaxis_title = "# Reincidentes")

ET_hist = px.histogram(dfSpecialCondition,x="condition",y="events",nbins=50,hover_data=["condition","events"])
ET_hist.update_layout(title="Histograma de Etnia o Raza", xaxis_title = "Raza", yaxis_title = "# Reincidentes")

df_mj_men = dfAgeAndSex[dfAgeAndSex["gender"]=="MASCULINO"]

MA_hist = px.histogram(df_mj_men,x="age",y="events",nbins=50,hover_data=["age","events"])
MA_hist.update_layout(title="Histograma de reincidencia por edad en hombres", xaxis_title = "Edad", yaxis_title = "# Reincidentes")

df_mj_women = dfAgeAndSex[dfAgeAndSex["gender"]=="FEMENINO"]

WA_hist = px.histogram(df_mj_women,x="age",y="events",nbins=50,hover_data=["age","events"])
WA_hist.update_layout(title="Histograma de reincidencia por edad en mujeres", xaxis_title = "Edad", yaxis_title = "# Reincidentes")

#################################################################################
# Here the layout for the plots to use.
#################################################################################
demographic_output=html.Div([
	#Place the different graph components here.
	dbc.Row([
        dbc.Col(dcc.Graph(figure=MS_hist, id='MS_hist')),
	]),
	dbc.Row([
        dbc.Col(dcc.Graph(figure=MC_hist, id='MC_hist')),
	]),
	html.Hr(),
	dbc.Row([
        dbc.Col(dcc.Graph(figure=EL_hist, id='EL_hist')),
	]),
	dbc.Row([
        dbc.Col(dcc.Graph(figure=ET_hist, id='ET_hist')),
	]),
	html.Hr(),
	dbc.Row([
        dbc.Col(dcc.Graph(figure=MA_hist, id='MA_hist')),
	]),
	dbc.Row([
        dbc.Col(dcc.Graph(figure=WA_hist, id='WA_hist')),
	]),
	html.Hr(),
	],className="mj-body")
