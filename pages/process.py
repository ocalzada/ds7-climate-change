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
            ## Modeling Process
            ----------------------------------------------------------------------
            ### Mean Baselines

            ![](assets/mean-baseline.png)


            For this regression, the mean baseline is shown above.  
            When splitting the data into training and testing datasets (cutoff = 1980-01-01) and predicting
            the average climate temperature anomaly for the training set for every time point, the `Mean Absolute Error` to beat
            was `MAE: 0.149`.

            &emsp;

            ### Model Selection, Iteration, and Facebook's Prophet

            Due to a small dataset, a `k-fold cross validation with independent test set` approach was employed for model selection and performance evaluation. 
            The initial model was a `Ridge Regression` model that obtained a `MAE: 0.126`.
            After several iterations of this and other model types, including `Linear Regression`, `RandomForestEnsembles`, 
            hyperparameter optimization using `GridSearchCV` and `RandomizedSearchCV`, the best model or the model that obtained the lowest 
            MAE was the original `Ridge Regression` model prepped using a pipeline:
            

            ```
            pipeline = make_pipeline(
            SimpleImputer(strategy='mean'), 
            StandardScaler(),  
            Ridge(alpha=1.0)
            )
            k = 3
            scores = cross_val_score(pipeline, X_train, y_train, cv=k, 
                         scoring='neg_mean_absolute_error')
            ```
            
            However, when utilizing [Prophet](https://facebook.github.io/prophet/), an open source forecasting tool optimized to 
            model time series data, a model with a `MAE: 0.108` was obtained. Because Prophet uses an additive, univariate, linear model for its forecast,
            it works best for time series with high seasonal variation, such as seasonal weather averages.  
            
            """
        ),

    ],
)

layout = dbc.Row([column1])