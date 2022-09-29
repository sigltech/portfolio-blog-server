from ..database.db import db
from datetime import date

class Post(db.Model):
    id = db.Column(db.String(80), primary_key=True)
    content = db.Column(db.String(120), unique=True, nullable=False)
    title = db.Column(db.String(80), nullable=False)
    date_posted = db.Column(db.String(100), nullable=False, default=date.today())
    description = db.Column(db.String(120), nullable=False)


    def __init__(self, id, description, title, content, date_posted):
        self.id = id
        self.description = description
        self.title = title
        self.content = content
        self.date_posted = date_posted
