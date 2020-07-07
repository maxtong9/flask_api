from flask import Flask
from api.extensions import Api
from api.parse_http_data import ParseHTTPDataView

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')

    # Associate flask app with flask_restful api
    api = Api(app)

    # endpoints (resources)
    api.add_resource(ParseHTTPDataView, '/')

    return app