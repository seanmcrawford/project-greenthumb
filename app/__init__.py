from random import randint
from time import sleep

from flask import Flask, render_template

from blink1.blink1 import blink1

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


@app.route("/blink")
def blink():
    with blink1() as b1:
        b1.fade_to_color(100, 'navy')
        sleep(5)
    return "Light activated for 5 seconds"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
