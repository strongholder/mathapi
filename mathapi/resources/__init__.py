from flask_restful import Api
from prometheus_flask_exporter import RESTfulPrometheusMetrics

from mathapi.resources.exponent import Exponent
from mathapi.resources.factorial import Factorial

api_metrics = RESTfulPrometheusMetrics.for_app_factory()

api = Api(prefix="/api/v1")
api.add_resource(Exponent, "/exponent")
api.add_resource(Factorial, "/factorial")