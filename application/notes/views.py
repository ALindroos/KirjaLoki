from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.books.models import Book
from application.books.forms import BookForm
from application.auth.models import read_books
from application.notes.models import Note
from application.notes.forms import NoteForm

@app.route("/notes/new/<book_id>")
@login_required
def note_form(book_id):
    return render_template("notes/new.html", form = NoteForm(), book = Book.query.get(book_id))

@app.route("/notes/create/<book_id>", methods=["POST"])
@login_required
def note_create(book_id):
    form = NoteForm(request.form)

    if not form.validate():
        return render_template("notes/new.html", form = NoteForm(), book = Book.query.get())

    n = Note(form.note.data)
    n.account_id = current_user.id
    n.book_id = book_id

    db.session.add(n)
    db.session().commit()

    return redirect(url_for('book_show', book_id=book_id))

@app.route("/notes/edit/<book_id>", methods=["POST","GET"])
@login_required
def note_edit(book_id):
    note = Note.query.filter_by(book_id=book_id, account_id=current_user.id).first()
    book = Book.query.get(book_id)
    if request.method == "GET":
        return render_template("notes/edit.html" , form=NoteForm, note=note, book=book)
    
    form = NoteForm(request.form)

    if not form.validate():
        return render_template("note/edit.html",form=form)

    note.note = form.note.data
    db.session().commit()

    return redirect(url_for('book_show', book_id=book_id))

@app.route("/notes/del/<note_id>", methods=["POST"])
@login_required
def note_delete(note_id):
    n = Note.query.get(note_id)
    db.session().delete(n)
    db.session().commit()

    return redirect(url_for("books_index"))


@app.route("/notes/common_notes")
@login_required
def common_notes():
    common_notes = Note.communal_comments(current_user.id)

    return render_template("notes/commonnotes.html", common_notes=common_notes)
