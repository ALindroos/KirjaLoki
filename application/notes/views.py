from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.books.models import Book
from application.books.forms import BookForm
from application.auth.models import readBooks
from application.notes.models import Note
from application.notes.forms import NoteForm

@app.route("/notes/new/<book_id>")
@login_required
def note_form(book_id):
    return render_template("notes/new.html", form = NoteForm(), book = Book.query.get(book_id))