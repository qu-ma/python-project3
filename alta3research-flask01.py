#!/usr/bin/python3

from flask import Flask
from flask import jsonify
from flask import render_template
from fruitBasket import basket

app = Flask(__name__)

# Starting Endpoint that doesn't take a name
@app.route("/")
def index_no_name():
    return render_template("index_no_name.html")

# Endpoint that takes a name
@app.route("/<name>")
def index_with_name(name):
    return render_template("index_with_name.html", username = name)

# Fruits Endpoint
@app.route("/fruits")
def fruit():
    return jsonify(basket())

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)