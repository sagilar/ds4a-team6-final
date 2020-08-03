#Basics Requirements
import pathlib
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import base64


#Recall app
from app import app

from lib import demographic, geographic, gender, timeanalysis, crimeanalysis


tab1_content = html.Div(
    className = "container mt-3",
    children = [
        demographic.demographic_output
    ]
)

tab2_content = html.Div(
    className = "container mt-3",
    children = [
        geographic.geographic_histogram
    ]
)
tab3_content = html.Div(
    className = "container mt-3",
    children = [
        gender.gender_output
    ]
)
tab4_content = html.Div(
    className = "container mt-3",
    children = [
        timeanalysis.timeanalysis_output
    ]
)
tab5_content = html.Div(
    className = "container mt-3",
    children = [
        crimeanalysis.output_html
    ]
)

navigationTabs = dbc.Tabs(
    children = [
        dbc.Tab(tab1_content, label="Análisis Demográfico"),
        dbc.Tab(tab2_content, label="Análisis Geográfico"),
        dbc.Tab(tab3_content, label="Análisis Por Género"),
        dbc.Tab(tab4_content, label="Análisis de Tiempo"),
        dbc.Tab(tab5_content, label="Análisis de Crimen"),
    ]
)
