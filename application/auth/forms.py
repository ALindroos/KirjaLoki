from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus:", [validators.Length(min=4)])
    password = PasswordField("Salasana:", [validators.Length(min=4)])

    class Meta:
        csrf = False
