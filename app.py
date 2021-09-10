import os
from functools import wraps
from flask import (Flask, redirect, url_for, session)

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


def requires_user(func):
    """
    Redirects wrapped route to user log in if no user in session.
    """
    @wraps(func)
    def route(*args, **kwargs):
        if session.get("user") is None:
            # Display flash message?
            return redirect(url_for("user"))
        else:
            return func(*args, **kwargs)

    return route


@app.route("/")
def hello_world():
    return "<p>Server running!</p>"
