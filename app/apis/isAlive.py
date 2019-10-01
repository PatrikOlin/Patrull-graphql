from flask_restplus import Namespace, Resource
import json

api = Namespace('isAlive', description='Basic isAlive-endpoint')


@api.route('/')
class IsAlive(Resource):
    def get(self):
        alive = "And we're stayin' alive, stayin' alive \nAh, ha, ha, ha, stayin' alive, stayin' alive \nAh, ha, ha, ha, stayin' alive"
        return json.dumps(alive)
