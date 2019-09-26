import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has 
twelve columns.

There are three main layout components in dash-bootstrap-components: Container, 
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column 
should take up a third of the width. Since we don't specify behaviour on 
smaller size screens Bootstrap will allow the rows to wrap so as not to squash 
the content.
"""

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ### How will global temperatures change into the future?

            Specifically, when will we reach the 1.5-2 degrees C threshold above which climate scientists agree will no longer sustain life as we know it?

            Using historical data (1880-2019) for monthly average global temperature anomalies in degrees Celsius, we developed a model to predict temperature 
            anomalies into the future, which represents global temperature rise.

            This app uses data collected by [NOAA.gov](https://www.ncdc.noaa.gov/cag/global/data-info), which was obtained using weather stations and drifting 
            ocean buoys to measure land and sea surface conditions. These observations were converted into temperature anomalies, calculated relative to the 20th 
            century average temperature for that location. A positive anomaly indicates that the observed temperature was warmer than the average, while a negative 
            anomaly indicates a cooler observation. 


            """,style={'textAlign': 'left','font-size': '20px'}
        ),
        dcc.Link(dbc.Button('Find Out !', color='primary'), href='/predictions')
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.Img(src='assets/climate-temperature-predictions.png', className='img-fluid'),
        dcc.Markdown('''
        **Temperature Anomaly Predictions for the Next 100 Years**
        ''', style={'textAlign': 'center'}
        )
    ]
)


layout = dbc.Row([column1, column2])