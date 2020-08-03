#Basics Requirements
import pathlib
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html

#Recall app
from app import app

sidebar = html.Aside(
        children=[
            html.Div(
                id="sidebar",
                className="nav-collapse",
                children=[
                    html.Ul(
                        className="sidebar-menu",
                        id="nav-accordion",
                        children=[
                            html.Li(
                                className="mt",
                                children=[
                                    dcc.Link(
                                        href="dashboard",
                                        children=[
                                            html.I(
                                                className="fa fa-dashboard"
                                                
                                            ),
                                            html.Span(
                                                "Dashboard"
                                            )

                                        ]
                                    )
                                ]
                            ),
                            html.Li(
                                className="mt",
                                children=[
                                    dcc.Link(
                                        href="dataexploration",
                                        children=[
                                            html.I(
                                                className="fa fa-book"
                                                
                                            ),
                                            html.Span(
                                                "Exploración de Datos"
                                            )

                                        ]
                                    )
                                ]
                            ),
                            html.Li(
                                className="mt",
                                children=[
                                    dcc.Link(
                                        href="models",
                                        children=[
                                            html.I(
                                                className="fa fa-tasks"
                                                
                                            ),
                                            html.Span(
                                                "Modelos"
                                            )

                                        ]
                                    )
                                ]
                            ),
                        ]
                    )
                ]
            )
        ]
    )
