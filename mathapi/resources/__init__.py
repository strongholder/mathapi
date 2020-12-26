from flask_restful import Api
from prometheus_flask_exporter import RESTfulPrometheusMetrics

from mathapi.resources.exponent import Exponent
from mathapi.resources.factorial import Factorial
from mathapi.resources.fibonacci import Fibonacci
from mathapi.services.auth import login_required

api_metrics = RESTfulPrometheusMetrics.for_app_factory(metrics_decorator=login_required)

api = Api(prefix="/api/v1")
api.add_resource(Exponent, "/exponent")
api.add_resource(Factorial, "/factorial")
api.add_resource(Fibonacci, "/fibonacci")
