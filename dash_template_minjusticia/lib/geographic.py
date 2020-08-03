import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
#import geopandas


from datetime import datetime as dt
import json
import numpy as np
import pandas as pd
import requests

#Recall app
from app import app

# Call API to get Crimes By Region
r = requests.get("http://ds4at6api.azurewebsites.net/api/CrimesByRegion")
df_dept_count =pd.read_json(r.text)
df_dept_count = df_dept_count[["region", "events"]]

##############################################################
# RECIDIVISM BY DEPARTMENT HISTOGRAM
###############################################################

Rec_dep_fig = px.histogram(df_dept_count,x="region",y="events",nbins=50,hover_data=["region","events"],
                 width=900, height=600)
Rec_dep_fig.update_layout(title="Reincidencia por Departamento", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', xaxis_title = "Región", yaxis_title = "# Reincidentes")


add_data = {'region':["VAUPES","VICHADA","GUAVIARE","GUAINIA"],'events':[0,0,0,0]}
add_df = pd.DataFrame(data=add_data)


df_dept_count["region"][df_dept_count["region"]=="BOGOTA D.C."]="SANTAFE DE BOGOTA D.C"#]="BOGOTA D.C."
df_dept_count["region"][df_dept_count["region"]=="SAN ANDRES Y PROVIDENCIA"]="ARCHIPIELAGO DE SAN ANDRES PROVIDENCIA Y SANTA CATALINA"#]="SAN ANDRES Y PROVIDENCIA"
df_dept_count.columns = ["region","events"]
df_dept_count_comp = pd.concat([df_dept_count,add_df],ignore_index=True)
df_dept_count_comp.fillna(0,inplace=True)


#############################
# Load map data
#############################
with open('data/Colombia_mod.geo.json') as geo:
    geojson_file = json.loads(geo.read())
#Create the map:
Map_Fig=px.choropleth_mapbox(df_dept_count_comp,
        locations='region',
        color='events',
        geojson=geojson_file,
        zoom=3,
        mapbox_style="carto-positron",
        center={"lat": 4.12, "lon": -73.22},
        color_continuous_scale="Viridis",
        opacity=0.5,
        labels={"events":"Reincidencia por Departamento"}
        )

Map_Fig.update_layout(title='Mapa de Reincidencia in Colombia',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)')


#################################################################################
# Here the layout for the plots to use.
#################################################################################
geographic_output=html.Div([
	#Place the different graph components here.
    dcc.Graph(figure=Map_Fig, id='Colombia_map')
    ])

geographic_histogram=html.Div([
	#Place the different graph components here.
    dcc.Graph(figure=Rec_dep_fig, id='Histogram')
    ])

geographic_fulloutput=html.Div([
	#Place the different graph components here.
    dcc.Graph(figure=Rec_dep_fig,id="Recidivism_dept_hist"),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=Map_Fig, id='Colombia_map')),
        dbc.Col(),
	]),
    ],className="mj-body")