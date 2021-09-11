import os
from functools import wraps

from flask import (Flask, redirect, 
    render_template, url_for, session)
from flask_pymongo import PyMongo


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
# connect app as mongodb client
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
# 'main' database is exposed as mongo.db

mongo = PyMongo(app)

debugging = "DEBUG" in os.environ


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
# @requires_user - uncomment once /user route is implemented
def home():
    """
    Shows the home page/default route and main app page
    Loads all provisions from mongodb collection
    """

    # read all workspace considerations with associated provisions into list
    all_ws_considerations = list(
        mongo.db.ws_considerations.find()
    )

    return render_template(
        "index.html",
        all_ws_considerations=all_ws_considerations
    )


@app.route('/about')
def about():
    """
    About Page
    """
    return render_template("about.html", page_title="About")


@app.route('/faq')
def faq():
    """
    FAQ Page
    """
    return render_template("faq.html", page_title="FAQ")


@app.route("/user")
def user():
    """
    User log in page
    Landing page for users not in session
    """
    return "<p>User log in goes here</p>"


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


# Temporary test route to generate a user session
@app.route("/test_user")
def test_user():
    session["user"] = {"firstname": "test", "lastname": "test"}
    return redirect(url_for("home"))


@app.route("/show_test_user")
def show_test_user():
    if session.get("user") is None:
        return "No test user defined"

    return f"<p>User = {session['user']['firstname']} {session['user']['lastname']}</p>"


if __name__ == "__main__":
    app.run(debug=debugging)
