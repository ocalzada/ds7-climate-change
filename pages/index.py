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
        
            ## How will average global temperatures change into the future?

            Specifically, by when will we reach the 1.5-2 degrees C threshold above which climate scientists agree
            will no longer sustain life as we know it?

            Using historical data (1880-2019) for monthly average global temperature anomalies
            in degrees Celsius, we developed a model to predict degrees C changes for the next 100 years.

            This app uses data collected by [NOAA.gov](https://www.ncdc.noaa.gov/cag/global/data-info). 
            Data includes combined global land and ocean temperature anomalies, which are calculated relative
            to the 20th century average. A positive anomaly indicates that the observed temperature was warmer
            than the baseline, while a negative anomaly indicates a cooler observation. NOAA uses weather stations
            and drifting ocean buoys to measure land and sea surface conditions, respectively.


            """
        ),
        dcc.Link(dbc.Button('Find Out !', color='primary'), href='/predictions')
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.Img(src='assets/climate-temperature-predictions.png', className='img-fluid'),
        dcc.Markdown('''
        **Temperature Anomaly Prediction for Next 100 Years**
        ''', style={'textAlign': 'center'}
        )
    ]
)


layout = dbc.Row([column1, column2])