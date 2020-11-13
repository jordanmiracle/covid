import reimport argparse
import flask
from flask import request
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc

app.layout = build_desktop_layout

@server.before_request
def before_request_func():
    """This check is the user agent is from mobile to determine which layout to serve 
    before user makes any requests."""
    agent = request.headers.get("User_Agent")
    mobile_string = "(?i)android|fennec|iemobile|iphone|opera (?:mini|mobi)|mobile"
    re_mobile = re.compile(mobile_string)
    is_mobile = len(re_mobile.findall(agent)) > 0


    if is_mobile:
        app.layout = build_mobile_layout
        flask.session['mobile'] = True
        flask.session['zoom'] = 1.9
    else:
        app.layout = build = build_desktop_layout
        flask.session['mobile'] = False
        flask.session['zoom'] = 2.8