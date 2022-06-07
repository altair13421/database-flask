from email.policy import default
from manager import db
from datetime import datetime

class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True)
    age = db.Column(db.Integer, index = True)
    description = db.Column(db.String(128), index = True)
    date_added = db.Column(db.DateTime, index = True, default = datetime.utcnow())

    def __repr__(self):
        return f'<Data {self.id}>'