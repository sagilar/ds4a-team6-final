#Basics Requirements
import pathlib
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
from multiprocessing import Process, freeze_support

#Data
import math
import numpy as np
import datetime as dt
import pandas as pd
import json

# Flask
import flask

#Recall app
from app import app

# Apps
from apps import home, models, dataexploration



###########################################################
#
#           APP LAYOUT:
#
###########################################################

#LOAD THE DIFFERENT FILES
from lib import header, sidebar

#PLACE THE COMPONENTS IN THE LAYOUT
app.layout =html.Div(
    [
      dcc.Location(id='url', refresh=False),
      header.header,
      sidebar.sidebar,
      html.Div(id='page-content')
    ],
    id="container"
)



###############################################
#
#           APP INTERACTIVITY:
#
###############################################

###############################################################
#Callbacks for routing
#################################################################

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/models':
        return models.layout
    elif pathname == '/dataexploration':
        return dataexploration.layout
    else:
        return home.layout

###############################################################
#Load and modify the data that will be used in the app.
#################################################################




#############################################################
# LINE PLOT : Add sidebar interaction here
#############################################################



#############################################################
# PROFITS BY CATEGORY : Add sidebar interaction here
#############################################################



#############################################################
# TREEMAP PLOT : Add sidebar interaction here
#############################################################



#############################################################
# MAP : Add interactions here
#############################################################

#MAP date interaction



#MAP click interaction















if __name__ == "__main__":
    app.run_server(debug=True, port=9050)
    freeze_support()
