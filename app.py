import os
from functools import wraps

from flask import (Flask, redirect, request, render_template, url_for, session)
from flask_pymongo import PyMongo
from bson import ObjectId

# ./server.sh not working for me on gitpod
if os.path.exists("env.py"):
    import env


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
    # corresponding provisions attached
    # $unwind provision_categories array to create document copy for each element in array
    # $lookup accepts Array type as localField and performs overwrite
    # $group recreates original document structure with provision_categories as an array
    # $first takes value of 'name', 'desc' and 'ui_location' fields from first document in each group
    considerations_data = list(mongo.db.ws_considerations.aggregate([
        {
            "$unwind": {
                "path": "$provision_categories"
            }
        },
        {
            "$lookup": {
                "from": "provisions",
                "localField": "provision_categories.provisions",
                "foreignField": "_id",
                "as": "provision_categories.provisions"
            }
        },
        {
            "$group": {
                "_id": "$_id",
                "name": {"$first": "$name"},
                "desc": {"$first": "$desc"},
                "ui_location": {"$first": "$ui_location"},
                "provision_categories": {
                    "$push": "$provision_categories"
                }
            }
        }
    ]))

    return render_template(
        "index.html",
        page_title="Home",
        considerations=considerations_data,
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
        # We don't want to discriminate against Madonna :)
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
@app.route("/submit/<user_id>", methods=["GET", "POST"])
@requires_user
def submit(user_id=None):
    """
    POST: Receives the user's selections,
    associates with session user and adds to database
    GET: displays summary for user's' selections
    """

    if request.method == "POST":
        provisions = request.form.getlist("provisions")
        # Clean and validate data sent from client
        if provisions:
            # Create new record
            provisions = list(map(lambda i:ObjectId(i), provisions))
            employee = {
                "first_name": session["user"]["firstname"],
                "last_name": session["user"]["lastname"],
                "provisions_ids": provisions,
                "other_info": None
            }
            # Attempt to insert or update document in employees collection
            ret = mongo.db.employees.replace_one(
                {"_id": ObjectId(user_id)},
                employee,
                upsert=True
            )
            _id = user_id
            if ret.upserted_id:
                _id = str(ret.upserted_id)
            return redirect(url_for('submit', user_id=_id))


    # GET
    # try to lookup by employee_id in database
    # display success message and provisions or redirect to 'user/'

    return render_template(
        "submit.html", page_title="Submit"
    )


if __name__ == "__main__":
    app.run(debug=debugging,
            host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")))
