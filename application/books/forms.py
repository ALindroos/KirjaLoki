from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class BookForm(FlaskForm):
    title = StringField("Kirjan nimi:", [validators.Length(min=2)])
    author = StringField("Kirjailija:", [validators.Length(min=2)])
    description = TextAreaField("Kuvaus:", [validators.Length(max=525)])

    class Meta:
        csrf = False