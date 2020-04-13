from flask import Flask, render_template
from random import randint

app = Flask(__name__)


def get_sensor_reading():
    return randint(1, 100)


@app.route("/")
@app.route("/index")
def index():
    return "Hello, world"


@app.route("/<username>")
def hello(username):
    return render_template("index.html", username = username)


@app.route("/sensor")
def sensor():
    return render_template("sensor.html", value = get_sensor_reading())
