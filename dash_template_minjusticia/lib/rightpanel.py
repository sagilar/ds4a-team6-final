#Basics Requirements
import pathlib
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html

#Recall app
from app import app

highlight1 = html.Div(
    className = "desc",
    children = [
        html.Div(
            className = "thumb",
            children = [
                html.Span(
                    className = "badge bg-theme",
                    children = [
                        html.I(
                            className = "fa fa-clock-o"
                        )
                    ]
                )
            ]
        ),
        html.Div(
            className = "details",
            children = [
                html.P(
                    "La mayoría de los casos se concentran en Bogotá, Antioquia, Valle del Cauca, Santander y Meta"
                )
            ]
        )
    ]
)
highlight2 = html.Div(
    className = "desc",
    children = [
        html.Div(
            className = "thumb",
            children = [
                html.Span(
                    className = "badge bg-theme",
                    children = [
                        html.I(
                            className = "fa fa-child"
                        )
                    ]
                )
            ]
        ),
        html.Div(
            className = "details",
            children = [
                html.P(
                    "Las personas que realizan estudios en el centro de reclusión tienen menos probabilidad de reincidir que los que no lo hacen."
                )
            ]
        )
    ]
)
highlight3 = html.Div(
    className = "desc",
    children = [
        html.Div(
            className = "thumb",
            children = [
                html.Span(
                    className = "badge bg-theme",
                    children = [
                        html.I(
                            className = "fa fa-tasks"
                        )
                    ]
                )
            ]
        ),
        html.Div(
            className = "details",
            children = [
                html.P(
                    "El crimen más cometido por los hombres es robo."
                )
            ]
        )
    ]
)
highlight4 = html.Div(
    className = "desc",
    children = [
        html.Div(
            className = "thumb",
            children = [
                html.Span(
                    className = "badge bg-theme",
                    children = [
                        html.I(
                            className = "fa fa-binoculars"
                        )
                    ]
                )
            ]
        ),
        html.Div(
            className = "details",
            children = [
                html.P(
                    "El crimen más cometido por las mujeres es tráfico de drogas."
                )
            ]
        )
    ]
)

rightpanel= html.Div(
    className = "col-lg-3 ds",
    children = [
        html.Div(
            children= [
                html.H4(
                    "Highlights",
                    className = "centered mt"
                ),
                highlight1,
                highlight2,
                highlight3,
                highlight4,
            ]
        )
    ]
)