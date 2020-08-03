#Basics Requirements
import pathlib
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html

#Recall app
from app import app


card1 = html.Div(
    className = "col-md-4 col-sm-4 mb",
    children = [
        html.Div(
            className = "grey-panel pn donut-chart",
            children = [
                html.Div(
                    className = "grey-header",
                    children=[
                        html.H5(
                            "Tasa de Reincidencia"
                        )
                    ]
                ),
                html.Div(
                    className = "row",
                    children = [
                        html.Div(
                            className = "col-sm-6 col-xs-6 goleft",
                            children = [
                                html.P(
                                    children = [
                                        "Porcentaje",
                                        html.Br(),
                                       
                                    ]
                                )
                            ]
                        ),
                        html.Div(
                            className = "col-sm-6 col-xs-6 goleft",
                            children = [
                                html.H2("50%")
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)

card2 = html.Div(
    className = "col-md-4 col-sm-4 mb",
    children = [
        html.Div(
            className = "darkblue-panel pn",
            children = [
                html.Div(
                    className = "darkblue-header",
                    children=[
                        html.H5(
                            "Hijos Menores"
                        )
                    ]
                ),
                html.Div(
                    className = "row",
                    children = [
                        html.Div(
                            className = "col-sm-6 col-xs-6",
                            children = [
                                html.P(
                                    children = [
                                        "Tienen Hijos",
                                        html.Br(),
                                       
                                    ]
                                )
                            ]
                        ),
                        html.Div(
                            className = "col-sm-6 col-xs-6 goleft",
                            children = [
                                html.H2("79%")
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)

card3 = html.Div(
    className = "col-md-4 col-sm-4 mb",
    children = [
        html.Div(
            className = "green-panel pn",
            children = [
                html.Div(
                    className = "green-header",
                    children=[
                        html.H5(
                            "Información por Género"
                        )
                    ]
                ),
                html.Div(
                    className = "row",
                    children = [
                        html.Div(
                            className = "col-sm-6 col-xs-6",
                            children = [
                                html.P(
                                    children = [
                                        "Porcentaje",
                                        html.Br(),
                                        "Hombres: "
                                    ]
                                )
                            ]
                        ),
                        html.Div(
                            className = "col-sm-6 col-xs-6 goleft",
                            children = [
                                html.H2("90%")
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)
