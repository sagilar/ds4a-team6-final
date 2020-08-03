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

#Recall app
from app import app

df_mj = pd.read_csv('data/reincidencia11junio2020_clean.csv', parse_dates=['FECHA_INGRESO','FECHA_SALIDA','FECHA_CAPTURA'])

df_genero = pd.DataFrame(df_mj.groupby(["GENERO","TITULO_DELITO"])["INTERNOEN"].agg('count'))
df_genero.reset_index(inplace=True)
df_geo_gen = pd.DataFrame(df_mj.groupby(["GENERO","DEPTO_ESTABLECIMIENTO"])["INTERNOEN"].agg('count'))
df_geo_gen.reset_index(inplace=True)
df_crimen = pd.DataFrame(df_mj.groupby(["TITULO_DELITO"])["INTERNOEN"].agg('count'))
df_crimen.reset_index(inplace=True)
df_edu_gen = pd.DataFrame(df_mj.groupby(["GENERO","NIVEL_EDUCATIVO"])["INTERNOEN"].agg('count'))
df_edu_gen.reset_index(inplace=True)
economic_crime = df_mj[(df_mj["TITULO_DELITO"]=="CONTRA EL PATRIMONIO ECONOMICO")].groupby(["GENERO", "DELITO"])["DELITO"].agg("count")
economic_crime = pd.DataFrame(economic_crime)
economic_crime.rename(columns={"DELITO": "COUNT"},inplace=True)
economic_crime.reset_index(inplace=True)
female_crime = df_mj[(df_mj["TITULO_DELITO"]=="CONTRA LA SALUD PUBLICA")].groupby(["GENERO", "DELITO"])["DELITO"].agg("count")
female_crime = pd.DataFrame(female_crime)
female_crime.rename(columns={"DELITO": "COUNT"},inplace=True)
female_crime.reset_index(inplace=True)


fig_edu_gen = px.bar(df_edu_gen, x='NIVEL_EDUCATIVO', y='INTERNOEN',
             hover_data=['GENERO','NIVEL_EDUCATIVO'], color='GENERO',
             labels={'INTERNOEN':'Amount of recidivist crimes'}, width=800, height=400, barmode='group', text="INTERNOEN")
fig_edu_gen.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig_edu_gen.update_layout(uniformtext_minsize=6, uniformtext_mode='hide',
                  title="Crímenes más cometidos por nivel de educación", xaxis_title = "Nivel Educativo", yaxis_title = "# Casos"
                 )

fig_gen_men = px.bar(df_genero[df_genero["GENERO"]=="MASCULINO"], x='TITULO_DELITO', y='INTERNOEN',
             hover_data=['TITULO_DELITO'],
             labels={'INTERNOEN':'Amount of recidivist crimes'}, height=400, barmode='stack', text="INTERNOEN")
fig_gen_men.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig_gen_men.update_layout(uniformtext_minsize=6, uniformtext_mode='hide', xaxis_tickangle=-45, showlegend=False, autosize=False,
                 width=800, height=700, margin=dict(l=50, r=50, b=100, t=100, pad=4 ),
                  title="Crímenes más cometidos por hombres", xaxis_title = "Crimen", yaxis_title = "# Casos"
                 )
fig_gen_men.update_xaxes( tickfont=dict(family='Rockwell', color='black', size=8)) #tickangle=45,


fig_gen_women = px.bar(df_genero[df_genero["GENERO"]=="FEMENINO"], x='TITULO_DELITO', y='INTERNOEN',
             hover_data=['TITULO_DELITO'],
             labels={'INTERNOEN':'Amount of recidivist crimes'}, height=400, barmode='stack', text="INTERNOEN")
fig_gen_women.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig_gen_women.update_layout(uniformtext_minsize=6, uniformtext_mode='hide', xaxis_tickangle=-45, showlegend=False, autosize=False,
                 width=800, height=700, margin=dict(l=50, r=50, b=100, t=100, pad=4 ),
                  title="Crímenes más cometidos por mujeres", xaxis_title = "Crimen", yaxis_title = "# Casos"
                 )
fig_gen_women.update_xaxes( tickfont=dict(family='Rockwell', color='black', size=8)) #tickangle=45,

fig_del_gen = px.bar(df_genero, x='TITULO_DELITO', y='INTERNOEN',
             hover_data=["GENERO",'TITULO_DELITO'], color='GENERO',
             labels={'INTERNOEN':'Amount of recidivist crimes'}, height=400, barmode='relative', text="INTERNOEN")
fig_del_gen.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig_del_gen.update_layout(uniformtext_minsize=7, uniformtext_mode='hide', xaxis_tickangle=-45, showlegend=True, autosize=False,
                 width=800, height=700, margin=dict(l=50, r=50, b=100, t=100, pad=4 ),
                  title="Crímienes más cometidos por género", xaxis_title = "Crimen", yaxis_title = "# Casos"
                 )
fig_del_gen.update_xaxes( tickfont=dict(family='Rockwell', color='black', size=8)) #tickangle=45,

fig_geo_gen = px.bar(df_geo_gen, x='DEPTO_ESTABLECIMIENTO', y='INTERNOEN',
             hover_data=["GENERO",'DEPTO_ESTABLECIMIENTO'], color='GENERO',
             labels={'INTERNOEN':'Amount of recidivist crimes'}, barmode='relative', text="INTERNOEN")
fig_geo_gen.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig_geo_gen.update_layout(uniformtext_minsize=6, uniformtext_mode='hide', xaxis_tickangle=-45, showlegend=True, autosize=False,
                 width=900, height=700, margin=dict(l=50, r=50, b=100, t=100, pad=4 ),
                  title="Distribución geográfica por género", xaxis_title = "", yaxis_title = "# Casos"
                 )
fig_geo_gen.update_xaxes( tickfont=dict(family='Rockwell', color='black', size=8)) #tickangle=45,

fig_econo_crime = px.bar(economic_crime, x='DELITO', y='COUNT',
             hover_data=["GENERO",'DELITO'], color='GENERO',
             labels={'COUNT':'Amount of recidivist economic crimes'}, barmode='relative', text="COUNT")
fig_econo_crime.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig_econo_crime.update_layout(uniformtext_minsize=6, uniformtext_mode='hide', xaxis_tickangle=-45, showlegend=True, autosize=False,
                 width=900, height=700, margin=dict(l=50, r=50, b=100, t=100, pad=4 ),
                  title="Crímenes más cometidos contra el patrimonio económico por género", xaxis_title = "Crimen", yaxis_title = "# Casos"
                 )
fig_econo_crime.update_xaxes( tickfont=dict(family='Rockwell', color='black', size=8)) #tickangle=45,

fig_fem_crime = px.bar(female_crime, x='DELITO', y='COUNT',
             hover_data=["GENERO",'DELITO'], color='GENERO',
             labels={'COUNT':'Número de reincidencias en crímenes contra la salud pública'}, barmode='relative', text="COUNT")
fig_fem_crime.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig_fem_crime.update_layout(uniformtext_minsize=6, uniformtext_mode='hide', xaxis_tickangle=-45, showlegend=True, autosize=False,
                 width=900, height=700, margin=dict(l=50, r=50, b=100, t=100, pad=4 ),
                  title="Crímenes más cometidos contra la salud pública por género", xaxis_title = "Crimen", yaxis_title = "# Casos"
                 )
fig_fem_crime.update_xaxes( tickfont=dict(family='Rockwell', color='black', size=8)) #tickangle=45,

#################################################################################
# Here the layout for the plots to use.
#################################################################################
gender_output=html.Div([
	#Place the different graph components here.
	dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_edu_gen, id='fig_edu_gen'), md=12),
	]),
        dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_gen_men, id='fig_gen_men'), md=12),
	]),
	dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_gen_women, id='fig_gen_women'), md=12),
	]),
        dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_del_gen, id='fig_del_gen'), md=12),
	]),
	dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_geo_gen, id='fig_geo_gen'), md=12),
	]),
	dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_econo_crime, id='fig_econo_crime'), md=12),
	]),

	dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_fem_crime, id='fig_fem_crime'), md=12),
	]),
	],className="mj-body")
