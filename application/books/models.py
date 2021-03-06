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
    isbn = db.Column(db.String(13), nullable=False)

    book_notes = db.relationship("Note", backref='book', lazy=True)

    def __init__(self, title, author, description, isbn):
        self.title = title
        self.author = author
        self.description = description
        self.isbn = isbn


    @staticmethod
    def most_popular_books():
        stmt = text("SELECT Book.id, Book.title, Book.author, COUNT(read_books.book_id) FROM Book"
                    " LEFT JOIN read_books ON Book.id = read_books.book_id"
                    " GROUP BY Book.id"
                    " HAVING COUNT(read_books.book_id) > 0"
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

    @staticmethod
    def most_recent():
        stmt = text("SELECT Book.id, Book.title, Book.author, Book.date_created FROM Book"
                    " GROUP By Book.id"
                    " ORDER BY 4 DESC "
                    " LIMIT 5")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "title":row[1], "author":row[2]})

        return response


    @staticmethod
    def basic_search(search_term):
        stmt = text("SELECT Book.id, Book.title, Book.author FROM Book"
                    " WHERE lower(Book.title) LIKE lower(:search_term)"
                    " OR lower(Book.author) LIKE lower(:search_term)").params(search_term=search_term)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "title":row[1], "author":row[2]})

        return response

    @staticmethod
    def book_notes_data(book_id):
        stmt = text("SELECT Note.note, Note.account_id, Account.name FROM Note"
                    " LEFT JOIN Account ON Note.account_id = Account.id"
                    " WHERE Note.book_id = :book_id").params(book_id=book_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"note":row[0], "user_id":row[1], "user_name":row[2]})

        return response
