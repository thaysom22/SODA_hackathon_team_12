import os
from functools import wraps

from flask import (Flask, redirect, request, render_template, url_for, session)
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
    Redirects wrapped route to user definition if no user in session.
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
    Shows the home page/default route and main app page
    Loads all provisions from mongodb collection
    """

    # Performs an join like query to get all values of ws_considerations with
    # Corrosponding provisions attached
    considerations = list(mongo.db.ws_considerations.aggregate([
        {
            "$lookup": {
                "from": "provisions",
                "localField": "_id",
                "foreignField": "ws_consideration",
                "as": "provisions"
            }
        }
    ]))

    return render_template(
        "index.html",
        page_title="Home",
        considerations=considerations,
        fname=session["user"]["firstname"]
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


@app.route("/user", methods=["GET", "POST"])
def user():
    """
    User log in page
    Landing page for users not in session
    """
    if request.method == 'POST':
        # Ensure firstname provided, but allow lastname to be blank.
        # We don't want to discriminate against Madonna
        if "firstname" in request.form and request.form["firstname"]:
            session["user"] = {
                "firstname": request.form["firstname"],
                "lastname": None
            }
            if "lastname" in request.form:
                session["user"]["lastname"] = request.form["lastname"]

            return redirect(url_for("home"))

    return render_template("user.html", page_title="Welcome")


@app.route("/submit", methods=["GET", "POST"])
@requires_user
def submit():
    """
    Submits the user's selections
    """
    return "<p>Submit success goes here</p>"


if __name__ == "__main__":
    app.run(debug=debugging)
