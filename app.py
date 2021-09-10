from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", page_title="Home")


@app.route('/about')
def about():
    return render_template("about.html", page_title="About")


@app.route('/faq')
def faq():
    return render_template("faq.html", page_title="FAQ")


if __name__ == "__main__":
    app.run(debug=True)
