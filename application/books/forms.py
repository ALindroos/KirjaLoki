from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class BookForm(FlaskForm):
    title = StringField("Kirjan nimi:")
    author = StringField("Kirjailija:")
    description = TextAreaField("Kuvaus:")

    class Meta:
        csrf = False