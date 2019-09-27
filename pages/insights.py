import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Insights
            ----------------------------------------------------------------------
            This model was created to use historical data of global temperature anomalies by month 
            to predict temperature anomalies in the future.  
            
            To the right you can observe temperature anomaly predictions for the next 100 years. 
            The actual temperature anomalies are depicted in black and the predicted anomalies for a given date are in blue.  
            The faint blue corresponds to the 95% Confidence Interval (CI) of the predictive model, which,
            as expected, widens in range over time.   
            
            Forecast components and trend changepoints are described and visualized here.  

            First, the figure demonstrates an overall increase in the magnitude of temperature anomalies over time, 
            occurring exclusively in the positive direction. While seasonal variation in temperature anomalies is still 
            predicted to occur, they will center around an ever-increasing new baseline, which is representative of 
            overall global temperature rise. By these predictions, global temperatures will rise by 1.5-2 degrees 
            Celsius between the years of 2056 and 2089.  

            Additionally, the available historical temperature data utilized for this model demonstrated seasonal 
            variation in temperature anomalies. This seasonal variation is incorporated into the forecasting model 
            in order to best predict future temperature anomalies. The predicted seasonal variations in temperature 
            anomalies is shown to the right, where November 1 - January 1 have the most extreme anomalies.  
        
            The model also identified three trend changepoints in the historical record, which corresponds to changes 
            in global temperature trends, between 1902–1917, 1936–1945, and 1963–1976.
            
            Below is an evaluation of the model's performance after out-of-sample cross validation analysis. By manually 
            selecting cutoff points in the historical data, Prophet fits a model using data only up to that cutoff.
            It then compares forecasted values to the actual values to compute the model's error. Both the raw mean 
            absolute error (mae) values and a plot of the errors are below (mae average is shown by the blue line).

            """, style={'textAlign': 'left','font-size': '12px'}
        ),
    html.Br(),
        html.Div(html.Img(src='assets/model-performance-error.png', className='img-fluid')),
        html.Br(),
        html.Div(html.Img(src='assets/model-performance-error-plot.png', className='img-fluid'))
    ],
    md=6,
)


column2 = dbc.Col(
    [
        
        html.Div(html.Img(src='assets/climate-temperature-predictions.png', className='img-fluid')),
        html.Br(),
        html.Div(html.Img(src='assets/overall-and-yearly-climate-trend.png', className='img-fluid')),
        html.Br(),
        html.Div(html.Img(src='assets/trend-changepoints.png', className='img-fluid')),
    ]
)

layout = dbc.Row([column1, column2])