import dash
from dash import Dash, html, dcc, Input, Output, State, dash_table
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

# import dash_mantine_components as dmc

data = pd.read_csv("data/employee_data.csv")

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


def create_dt(data, columns):
    dt = dash_table.DataTable(
        data=data.to_dict("records"),
        columns=columns,
        style_table={
            "height": "300px",
            "overflowY": "auto",
            "overflowX": "auto",
        },
        style_header={"position": "sticky", "top": 0},
        sort_action="native",
        filter_action="native",
    )
    
    return dt


intro = html.Div(
    [
        html.H2("Introduction"),
        html.P("Predict employee retention using machine learning."),
    ]
)

exploratory_analysis = html.Div(
    [
        html.H2("Exploring The Data - Exploratory Analysis"),
        html.H3("The Data"),
        create_dt(data, [{"id": i, "name": i} for i in data.columns]),
    ]
)

feature_engineering = html.Div(
    [
        html.H2("Feature Engineering"),
    ]
)

app.layout = html.Div(
    [
        html.H1("Employee Retention"),
        html.Br(),
        intro,
        html.Br(),
        exploratory_analysis,
        html.Br(),
        feature_engineering,
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
