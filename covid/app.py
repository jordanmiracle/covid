import flask
from flask_caching import Cache
import dash
import dash_bootstrap_components as dbc

server = flask.Flask(__name__)
app = dash.Dash(
    __name__,
    server=server,
    external_stylesheets = [
        dbc.themes.SLATE, # Bootswatch theme
        "https://use.fontawesome.com/releases/v5.9.0/css/all.css", # for social media icons
    
    ],
    meta_tags = [
        {
            "name": "description",
            "content": "Coronavirus SARS-COV2 COVID19 US Dash Dashboard App",
        },
        {   "name": "viewport",
            "content": "width=device-width, initial-scale=1.0"
            },
    ],
)