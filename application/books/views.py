from application import app, db
from flask import render_template, request, redirect, url_for
from application.books.models import Book


@app.route("/books", methods=["GET"])
def books_index():
    return render_template("books/list.html", books = Book.query.all())

@app.route("/books/new/")
def books_form():
    return render_template("books/new.html")

@app.route("/books/edit/<book_id>/", methods=["POST"])
def books_edit(book_id):
    return render_template("books/edit.html", book = Book.query.get(book_id))

@app.route("/books/upd/<book_id>", methods=["POST"])
def books_update(book_id):

    b = Book.query.get(book_id)
    b.title = request.form.get("title")
    b.author = request.form.get("author")
    db.session().commit()

    return redirect(url_for("books_index"))


@app.route("/books/", methods=["POST"])
def books_create():

    b = Book(request.form.get("title"),request.form.get("author"))

    db.session().add(b)
    db.session().commit()

    return redirect(url_for("books_index"))