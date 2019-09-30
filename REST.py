from flask import Flask, request, Response
import json
from datetime import datetime

api = Flask(__name__)


@api.route('/isAlive', methods=['GET'])
def is_alive():
    alive = "And we're stayin' alive, stayin' alive \nAh, ha, ha, ha, stayin' alive, stayin' alive \nAh, ha, ha, ha, stayin' alive"
    return json.dumps(alive)


@api.route('/report', methods=['POST'])
def post_report():
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
