from application import db

from sqlalchemy.sql import text

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    title = db.Column(db.String(144), nullable=False)
    author = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(526), nullable=True)

    bookNotes = db.relationship("Note", backref='book', lazy=True)

    def __init__(self, title, author, description):
        self.title = title
        self.author = author
        self.description = description


    @staticmethod
    def most_popular_books():
        stmt = text("SELECT Book.id, Book.title, Book.author, COUNT(readBooks.book_id) FROM Book"
                    " LEFT JOIN readBooks ON readBooks.book_id = Book.id"
                    " GROUP BY Book.id"
                    " HAVING COUNT(readBooks.book_id) > 0"
                    " ORDER BY 4 DESC"
                    " LIMIT 10")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "title":row[1], "author":row[2], "reads":row[3]})

        return response

    @staticmethod
    def most_notes():
        stmt = text("SELECT Book.id, Book.title, Book.author, COUNT(Note.book_id) FROM Book"
                    " LEFT JOIN Note ON Note.book_id = Book.id"
                    " GROUP BY Book.id"
                    " HAVING COUNT(Note.book_id) > 0"
                    " ORDER BY 4 DESC"
                    " LIMIT 10")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "title":row[1], "author":row[2], "notes":row[3]})

        return response