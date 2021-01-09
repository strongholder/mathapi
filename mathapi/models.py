from mathapi.app import db


class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    operation = db.Column(db.String(64), index=True, nullable=False)
    arg1 = db.Column(db.BigInteger(), index=True, nullable=False)
    arg2 = db.Column(db.BigInteger(), index=True, nullable=True)
    asynchronous = db.Column(db.Boolean(), index=True, nullable=True, default=False)
    email = db.Column(db.String(512), index=True, nullable=True)
    completed = db.Column(db.Boolean(), index=True, nullable=True)

    def __str__(self):
        return f"<Request {self.id}: {self.operation}({self.arg1}, {self.arg2}), async: {self.asynchronous}>"

    def complete(self):
        self.completed = True
        db.session.commit()
