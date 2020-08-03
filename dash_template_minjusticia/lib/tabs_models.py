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

from lib import survival, clusters, segmentacion


tab1_content = html.Div(
    className = "container mt-3",
    children = [
        survival.formLayout
    ]
)
tab2_content = html.Div(
    className = "container mt-3",
    children = [
        clusters.formLayout
    ]
)
tab3_content = html.Div(
    className = "container mt-3",
    children = [
        segmentacion.formLayout
    ]
)

navigationTabs = dbc.Tabs(
    children = [
        dbc.Tab(tab1_content, label="Modelo de Supervivencia"),
        dbc.Tab(tab2_content, label="Modelos de Clustering"),
        dbc.Tab(tab3_content, label="Modelo de Segmentación"),
    ]
)
