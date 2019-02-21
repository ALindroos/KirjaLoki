from application import db

from sqlalchemy import text

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    note = db.Column(db.String(512), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                            nullable=False)

    book_id = db.Column(db.Integer, db.ForeignKey('book.id'),
                        nullable=False)

    def __init__(self, note):
        self.note = note

    @staticmethod
    def communal_comments(user_id):
        stmt = text("SELECT Book.id, Book.title, Book.author, Account.id, Account.name,"
                    " Note.note, Note.date_created FROM Book, Account, Note"
                    " LEFT JOIN read_books ON read_books.account_id = :user_id"
                    " WHERE Note.book_id = Book.id"
                    " AND Book.id = read_books.book_id"
                    " AND Account.id != :user_id"
                    " AND Note.account_id = Account.id"
                    " ORDER BY 7 DESC").params(user_id=user_id)

        res = db.engine.execute(stmt)


        response = []
        for row in res:
            response.append({"book_id":row[0], "title":row[1], "author":row[2], "user_id":row[3],
                            "user_name":row[4], "note":row[5], "note_date":row[6]})

        return response