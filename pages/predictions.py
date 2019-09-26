import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy as np 
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from app import app

# Read in the dataframe
df = pd.read_csv('https://raw.githubusercontent.com/ocalzada/ds7-climate-change/master/Macintosh%20HD%E2%81%A9%5C%E2%81%A8Users%E2%81%A9%5Coscarcalzada%E2%81%A9%5CDocuments%5Cclimate-temp-anomalies.csv')

# Graph Time Series with RangeSlider
fig = go.Figure()
fig.add_trace(go.Scatter(x=df.ds, y=df['yhat'], name="Prediction",
                         line_color='deepskyblue'))

fig.add_trace(go.Scatter(x=df.ds, y=df['y'], name="Actual",
                         line_color='dimgray'))

fig.update_layout(title_text='Time Series with Rangeslider',
                  xaxis_rangeslider_visible=True)
fig.show()


column1 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1])