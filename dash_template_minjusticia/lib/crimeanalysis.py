import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
import powerlaw as plw
import networkx as nx
import community as community_louvain
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import gensim
from gensim import corpora, models

from datetime import datetime as dt
import json
import numpy as np
import pandas as pd

#Recall app
from app import app

nodes_result = pd.read_csv('data/nodes_result.csv')
edges_result = pd.read_csv('data/edges_result.csv')

graph = nx.from_pandas_edgelist(edges_result, source = 'source', target = 'target', edge_attr = 'similarity')

pos_ = nx.spring_layout(graph)
edge_x = []
edge_y = []

for edge in graph.edges():
    
    if graph.edges()[edge]['similarity'] > 0:
        char_1 = edge[0]
        char_2 = edge[1]
        x0, y0 = pos_[char_1]
        x1, y1 = pos_[char_2]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)
        
edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')

node_x = []
node_y = []
community = []
crime_label = []
for node in graph.nodes():
    x, y = pos_[node]
    node_x.append(x)
    node_y.append(y)
    community.append(*nodes_result.loc[nodes_result.Id == node, 'community'].values)
    com = nodes_result.loc[nodes_result.Id == node, 'topic'].values[0]
    label = f'''{node}: {com}'''
    crime_label.append(label)

node_trace = go.Scatter(
    x= node_x, y= node_y,
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale = True,
        color=community,
        size=10,
        line_width=2),
    text = crime_label)

fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title='Relación entre crímenes <br>',
                titlefont_size=16,
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )

fig.update_layout(title="Análisis de Relación entre Crímenes")


#################################################################################
# Here the layout for the plots to use.
#################################################################################
output_html=html.Div([
	#Place the different graph components here.
	dcc.Graph(figure=fig,id="crime_graph"),
	],className="mj-body")
