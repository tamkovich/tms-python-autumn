from flask import render_template, redirect, flash, url_for

from werkzeug.exceptions import abort

from app import app
from app.entities import User
from app.forms import LoginForm


@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)


@app.route('/user/<int:user_id>')
def get_user(user_id: int):
    user = User.query.get(user_id)
    if user is None:
        abort(404)
    return render_template('user.html', user=user)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            f"Welcome {form.username.data} with password {form.password.data}"
        )
        return redirect(url_for("index"))
    return render_template('login.html', form=form)
