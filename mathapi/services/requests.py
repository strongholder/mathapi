def save(operation, arg1, arg2=None, email=None):
    from mathapi.app import db
    from mathapi.models import Request

    request = Request(operation=operation, arg1=arg1, arg2=arg2)
    if email is not None:
        request.asynchronous = True
        request.email = email

    db.session.add(request)
    db.session.commit()

    return request.id
