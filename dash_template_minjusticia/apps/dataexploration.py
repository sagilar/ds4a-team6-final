#Basics Requirements
import pathlib
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html

#Recall app
from app import app
from lib import tabs

layout = html.Section(
    id="main-content",
    children = [
        html.Section(
            className = "wrapper",
            children = [
                html.Div(
                    className = "row",
                    children = [
                        html.Div(
                            className = "col-lg-12 main-chart",
                            children = [
                                html.Div(
                                    children = [
                                        html.Div(
                                            className = "border-head",
                                            children= [
                                                
                                                html.H2(
                                                    children = [
                                                        html.I(
                                                            className ="fa fa-book"
                                                        ),
                                                        "Exploración de Datos"
                                                    ]
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className = "row content-panel",
                                            children = [
                                                html.Div(
                                                    className = "col-md-12",
                                                    children = [
                                                        tabs.navigationTabs,
                                                    ]
                                                )

                                            ]
                                        )
                                        
                                                                             
                                        
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    ]
) 