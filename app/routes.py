from flask import render_template

from werkzeug.exceptions import abort

from app import app
from app.entities import User


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
