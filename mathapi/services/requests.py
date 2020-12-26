def save(operation, arg1, arg2=None):
    from mathapi.app import db
    from mathapi.models import Request

    request = Request(operation=operation, arg1=arg1, arg2=arg2)
    db.session.add(request)
    db.session.commit()
