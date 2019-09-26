import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from fbprophet import Prophet
import numpy as np 
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from app import app

# Read in the dataframe
df = pd.read_csv('https://datahub.io/core/global-temp/r/monthly.csv')
df = df[df.Source == 'GCAG']
df = df[['Date', 'Mean']]
df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format=True)
df = df.rename(columns={'Date':'ds', 'Mean': 'y'})

m = Prophet(interval_width=0.95)
m.fit(df)

future = m.make_future_dataframe(freq='m', periods=100*12)
forecast = m.predict(future)


column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            #### Time Series Forecast Model
            -------------------------

            Select a date in the future to obtain the predicted global temperature anomaly for that date.
            """
        ),
    
    html.Br(),

    # Date dropdown selection
        dcc.Markdown('#### Date'),
        dcc.Dropdown(
            id='ds',
            options=[
                {'label': '2020-01-31', 'value': '2020-01-31'},
                {'label': '2030-01-31', 'value': '2030-01-31'},
                {'label': '2040-01-31', 'value': '2040-01-31'},
                {'label': '2050-01-31', 'value': '2050-01-31'},
                {'label': '2055-01-31', 'value': '2055-01-31'},
                {'label': '2060-01-31', 'value': '2060-01-31'},
                {'label': '2070-01-31', 'value': '2070-01-31'},
                {'label': '2080-01-31', 'value': '2080-01-31'},
                {'label': '2090-01-31', 'value': '2090-01-31'},
                {'label': '2100-01-31', 'value': '2100-01-31'},
                {'label': '2110-01-31', 'value': '2110-01-31'},
                {'label': '2116-01-31', 'value': '2116-01-31'},
            ],
            value='2020-01-31'
        )
    ],
    md=4,
)

column2 = dbc.Col(
    # [
    #     dcc.Graph(
    #         id='prediction-graph', 
    #         figure={
    #             'data': [
    #                 {
    #                     'x': forecast['ds'],
    #                     'y': forecast['yhat'],
    #                     'mode': 'bar',
                        
    #                 }
    #             ]
    #         },
    #         style={'width': '80%',
    #             'margin-left': 'auto',
    #             'margin-right': 'auto'
    #         }),
        
    # ]
)

layout = dbc.Row([column1, column2])

# @app.callback(
#     Output('prediction-graph', 'figure'),
#     [Input(component_id='ds', component_property='value')]
# )
# def graph(Date):

#     mask = (forecast['ds'] == Date)

#     layout= go.Layout(
#         yaxis={'title': 'Degree C Anomaly'},
#         barmode='group',
#         title=('Predicted Global Temperature Anomaly')
#     )

#     data=[
#         go.Bar(name='Predicted', x=forecast[mask]['ds'], y=forecast['yhat'])
#     ]

#     return {'data':data, 'layout':layout}