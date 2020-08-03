#Basics Requirements
import pathlib
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html

#Recall app
from app import app



header = html.Header(
        id="pageHeader",
        className="header black-bg",
        children=[
            html.Div(
                className="sidebar-toggle-box",
                children=[
                    html.Div(
                        className="fa fa-bars tooltips"
                    )
                ]
            ),
            dcc.Link(
                href="/",
                className="logo",
                children=[
                    html.B(
                        "Minjusticia"
                    )
                ]
            )
        ]
    )
