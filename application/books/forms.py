from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class BookForm(FlaskForm):
    title = StringField("Kirjan nimi:", [validators.Length(min=2), validators.Length(max=144)])
    author = StringField("Kirjailija:", [validators.Length(min=2), validators.Length(max=144)])
    description = TextAreaField("Kuvaus:", [validators.Length(max=525)])
    isbn = StringField("ISBN:", [validators.Length(min=10)])


    class Meta:
        csrf = False