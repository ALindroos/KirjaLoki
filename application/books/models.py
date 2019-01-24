from application import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    title = db.Column(db.String(144), nullable=False)
    author = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(526), nullable=True)

    def __init__(self, title, author, description):
        self.title = title
        self.author = author
        self.description = description