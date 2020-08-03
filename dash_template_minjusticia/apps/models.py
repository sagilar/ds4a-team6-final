#Basics Requirements
import pathlib
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html

#Recall app
from app import app
from lib import tabs_models

'''layout = html.Section(
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
                                                            className ="fa fa-users"
                                                        ),
                                                        #"Modelo de Supervivencia"
                                                        "Modelos"
                                                    ]
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className = "row content-panel",
                                            children = [
                                                tabs_models.navigationTabs,
                                                tabs_models.content

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
)'''
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
                                                        "Modelos"
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
                                                        tabs_models.navigationTabs,
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


'''html.Div(
    className = "container",
    children = [
        html.Div(
            className = "col-md-12",
            children = [
                survival.formLayout
            ]
        )
    ]
)'''
