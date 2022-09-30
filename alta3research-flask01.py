#!/usr/bin/python3

import sqlite3
from flask import Flask
from flask import jsonify
from flask import render_template
from fruitBasket import basket
from flask import request

app = Flask(__name__)

# Endpoint that doesn't take a name
@app.route("/")
def index_no_name():
    return render_template("index_no_name.html")

# Endpoint that takes a name
@app.route("/<name>")
def index_with_name(name):
    return render_template("index_with_name.html", username = name)

# Endpoint with user input options
@app.route("/create_basket")
def create_basket():
    return render_template("create_basket.html")

# Endpoint that adds fruits to SQL table
@app.route('/add_fruit', methods=['POST'])
def add_fruit():
    fruit = request.form['fruit']
    quantity = request.form['quantity']

    with sqlite3.connect("fruit.db") as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO fruitbasket (fruit, quantity) VALUES (?,?)", (fruit, quantity))
        conn.commit()
    conn.close()
    return render_template("create_basket.html")

# Endpoint to view fruit basket
@app.route('/view_basket')
def view_basket():
    con = sqlite3.connect("fruit.db")
    con.row_factory = sqlite3.Row
    
    cur = con.cursor()
    cur.execute("SELECT * from fruitbasket")
    
    rows = cur.fetchall()
    return render_template("view_basket.html", rows=rows)

# Endpoint that returns json fruit basket data
@app.route("/fruits")
def fruit():
    return jsonify(basket())

# Connect to fruitDB and create fruitbasket table
def fruitDB():
    con = sqlite3.connect('fruit.db')
    con.execute('CREATE TABLE IF NOT EXISTS fruitbasket (fruit TEXT, quantity TEXT)')
    con.close()

if __name__ == "__main__":
   fruitDB()
   app.run(host="0.0.0.0", port=2224)