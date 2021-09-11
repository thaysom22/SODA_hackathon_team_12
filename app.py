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
        page_title="Home",
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


@app.route("/submit", methods=["GET", "POST"])
@requires_user
def submit():
    """
    Submits the user's selections
    """
    return "<p>Submit success goes here</p>"


if __name__ == "__main__":
    app.run(debug=debugging)
