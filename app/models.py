from app import db
import datetime

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200),nullable=False)
    completed = db.Column(db.Boolean,default=False)	
    created_at = db.Column(db.DateTime,default=datetime.datetime.utcnow)