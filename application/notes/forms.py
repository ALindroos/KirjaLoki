from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class NoteForm(FlaskForm):
    note = TextAreaField("Kommentti:", [validators.Length(max=511)])

    class Meta:
        csrf = False