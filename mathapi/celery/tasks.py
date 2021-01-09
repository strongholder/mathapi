import flask_mail

from mathapi.app import celery, mail
from mathapi.models import Request
from mathapi.services.fibonacci import nth_fibonacci


@celery.task()
def compute_fibonacci(request_id):
    request = Request.query.filter_by(operation="fib", asynchronous=True).first()
    if not request:
        return

    msg = flask_mail.Message(
        subject=f"Fib({request.arg1}) result",
        body="Please find your result as a file attached to this messages.",
        recipients=[request.email],
    )
    msg.attach("result.txt", "text/plain", str(nth_fibonacci(request.arg1)))

    mail.send(msg)

    request.complete()
