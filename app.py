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
@requires_user
def home():
    """
    Shows the home page
    """
    return "<p>Home page goes here</p>"




@app.route("/get_data")
@requires_user
def get_data(dataid):
    """
    Returns the requested data from the database
    """
    return None


@app.route("/submit", methods=["GET", "POST"])
@requires_user
def submit():
    """
    Submits the user's selections
    """
    return "<p>Submit success goes here</p>"

