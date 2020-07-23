from flask import request
from flask_restful import Resource
import sys

class TemperatureConversionView(Resource):
    def post(self):
        data = request.get_json()

        try:
            temperature = float(data.get('temperature'))
            unit = data['unit'] # another way of accessing json data
            result = {}

            if unit == 'f':
                result['temperature'] = (temperature - 32) / 9 * 5
                result['unit'] = 'c'
            else:
                result['temperature'] = temperature * 9 / 5 + 32
                result['unit'] = 'f'
            return result, 200 # dictionary automatically gets converted to json
        except:
            for e in sys.exc_info():
                print(e)
            message = str(sys.exc_info()[0])
            return {'error': True, 'message': message}, 400 # ERROR HTTP Status code 400. Bad Request