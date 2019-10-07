from flask import Flask, request, Response
from flask_restplus import Api, Resource, Namespace, fields
import json
from datetime import datetime

app = Flask(__name__)

api = Namespace('reports', description='Error reports')

report = api.model('Report', {
    'id': fields.Integer(required=True, description='Report ID'),
    'publickey': fields.String(required=False, description='Public key used when error occurred'),
    'timestamp': fields.DateTime(required=True, description='Timestamp of when error report was received by Patrull'),
    'errorMsg': fields.String(required=True, description='Error message'),
    'severity': fields.String(required=True, description='Severity of the error'),
    'stackTrace': fields.String(required=False, description='Error stacktrace')
})


@api.route('/')
class Report(Resource):
    def post(self):
        timestamp = datetime.now()
        error = request.get_json()
        with open('incoming_reports.json', 'a', encoding='utf-8') as outfile:
            outfile.write('\n' + timestamp.isoformat() + ': ')
            json.dump(error, outfile, ensure_ascii=False, indent=4)

        if error is None:
            response = Response("{'error': 'Report not received'",
                                status=400, mimetype='application/json')
            return response

        response = Response(json.dumps(error), status=201,
                            mimetype='application/json')
        return response


if __name__ == '__main__':
    api.run()
