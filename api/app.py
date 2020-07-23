from flask import Flask, jsonify
from api.extensions import Api
from api.parse_http_data import ParseHTTPDataView
from api.temperature_conversion import TemperatureConversionView

# underlying server library that runs the flask library
from werkzeug.exceptions import HTTPException, default_exceptions

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')


    # default all errors to JSON errors (instead of html). Comment out for html
    # goes through all status codes, and register the json_error error handler
    for code in default_exceptions:
        app.register_error_handler(code, json_error)

    # all uncaught exceptions handled by json_error method
    app.register_error_handler(Exception, json_error)







    # Associate flask app with flask_restful api
    api = Api(app)

    # endpoints (resources)
    api.add_resource(ParseHTTPDataView, '/')
    api.add_resource(TemperatureConversionView, '/temperature')

    return app

def json_error(error):
    if isinstance(error, HTTPException):
        status_code = error.code
    else:
        status_code = 500 # Default to 'Internal Server Error'
    return jsonify ( {'error' : str(error) }), status_code