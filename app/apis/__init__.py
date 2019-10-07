from flask_restplus import Api
from .isAlive import api as ns0
from .reports import api as ns1

api = Api(
    title='Patrull API',
    version='0.1',
    doc='/docs'
)

api.add_namespace(ns0)
api.add_namespace(ns1)
