import os

from flask import Flask
from dotenv import load_dotenv

# MY_ENV_VAR = os.getenv('MY_ENV_VAR')
load_dotenv()


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Server running!</p>"
