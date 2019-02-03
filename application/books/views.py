from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.books.models import Book
from application.books.forms import BookForm
from application.auth.models import readBooks
from application.auth.models import User

#Basic view, shows all books
@app.route("/books", methods=["GET"])
def books_index():
    return render_template("books/list.html", books = Book.query.all())

#Show new book form
@app.route("/books/new/")
@login_required
def books_form():
    return render_template("books/new.html", form = BookForm())

#Edit book
@app.route("/books/edit/<book_id>", methods=["GET"])
@login_required
def books_edit(book_id):
    form = BookForm(request.form)
    form.description.data = Book.query.get(book_id).description
    return render_template("books/edit.html", book = Book.query.get(book_id), form = form)

#Update book data
@app.route("/books/upd/<book_id>", methods=["POST"])
@login_required
def books_update(book_id):
    form = BookForm(request.form)

    if not form.validate():
        return render_template("books/edit.html", book = Book.query.get(book_id), form = form)

    b = Book.query.get(book_id)
    b.title = form.title.data
    b.author = form.author.data
    b.description = form.description.data
    db.session().commit()

    return redirect(url_for('book_show', book_id=book_id))

#Show individual book
@app.route("/books/<book_id>", methods=["GET"])
def book_show(book_id):
    return render_template("books/book.html", book = Book.query.get(book_id))

#Create new book
@app.route("/books/", methods=["POST"])
@login_required
def books_create():
    form = BookForm(request.form)

    if not form.validate():
        return render_template("books/new.html", form = form)

    b = Book(form.title.data, form.author.data, form.description.data)

    db.session().add(b)
    db.session().commit()

    return redirect(url_for("books_index"))

#Search books, matches author&title
@app.route("/books/seach/")
def books_search():
    return render_template("books/search.html")

#Show search results
@app.route("/books/results/", methods=["POST"])
def books_results():
    st = request.form.get("seachTerm")
    print(st)
    res = Book.query \
    .filter(Book.title.contains(st) | Book.author.contains(st)) \
    .all()
    
    return render_template("books/results.html", books = res)

#Mark a book read
@app.route("/books/add/<book_id>", methods=["POST"])
@login_required
def book_markRead(book_id):

    current_user.readBooks.append(Book.query.get(book_id))
    db.session().commit()

    return redirect(url_for("user_page", user_id=current_user.id))

#remove from booklist
@app.route("/book/rem/<book_id>", methods=["POST"])
@login_required
def book_removeRead(book_id):

    current_user.readBooks.remove(Book.query.get(book_id))
    db.session().commit()

    return redirect(url_for("user_page", user_id=current_user.id))


#delete book
@app.route("/books/del/<book_id>", methods=["POST"])
@login_required
def book_delete(book_id):

    b = Book.query.get(book_id)
    db.session().delete(b)
    db.session().commit()

    return redirect(url_for("books_index"))
