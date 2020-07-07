from flask import request
from flask_restful import Resource

# flask_restful resource
class ParseHTTPDataView(Resource):
    # GET REQUEST via http
    def get(self):
        print()
        print(' *** GET Request *** ')
        print('Request args: ', request.args)
        # get value of variable 'hello'
        print ('Request args "hello": ', request.args.get('hello'))
        print()
        print(' *** HEADERS *** ')
        print('Headers:\n', request.headers)
        print('User-Agent: ', request.headers.get('User-Agent'))

        # python dict with message 'get ok'
        return {'message' : 'GET ok' }, 200

    # POST REQUST via http
    def post(self):
        print()
        print(' *** POST Request *** ')
        # access vars from post request. (assuming json)
        json_data = request.get_json()
        print('POST Data (JSON): ', json_data)

        # Access 
        print('POST email: ', json_data.get('email'))

        return {'message':'POST ok' }, 200
