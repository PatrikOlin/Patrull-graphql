from flask import Flask, request, Response
from flask_restplus import Api, Resource, Namespace
import json
from datetime import datetime

app = Flask(__name__)

api = Namespace('reports', description='Error reports')


@api.route('/')
class Report(Resource):
    def post(self):
        timestamp = datetime.now()
        error = request.get_json()
        with open('incoming_reports.txt', 'a') as outfile:
            outfile.write(timestamp.isoformat() + ': ')
            json.dump(error, outfile)
            outfile.write(str('\n'))

        if error is None:
            response = Response("{'error': 'Report not received'",
                                status=400, mimetype='application/json')
            return response

        response = Response(json.dumps(error), status=201,
                            mimetype='application/json')
        return response


if __name__ == '__main__':
    api.run()
