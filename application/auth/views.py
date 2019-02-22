from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm

#login
@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                                error = "Salasana tai käyttäjätunnus on väärin")
    
    login_user(user)
    return redirect(url_for("index"))

#logout
@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

#shows user page
@app.route("/user/<user_id>", methods=["GET"])
def user_page(user_id):
    return render_template("auth/userpage.html", user=User.query.get(user_id))

# register new account
@app.route("/auth/register/", methods = ["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("auth/registerform.html", form = RegisterForm())

    form = RegisterForm(request.form)
    
    if not form.validate():
        return render_template("auth/registerform.html", form = form)

    if User.query.filter_by(username=form.username.data).first():
        return render_template("auth/registerform.html", form=form,
                                error = "Käyttäjätunnus on jo olemassa")

    user = User(form.dispname.data,form.username.data,form.password.data)
    db.session().add(user)
    db.session().commit()

    login_user(User.query.filter_by(username=form.username.data, password=form.password.data).first())

    return redirect(url_for("index"))
    