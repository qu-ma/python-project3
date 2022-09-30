#!/usr/bin/python3

import sqlite3
from urllib import request
from flask import Flask
from flask import jsonify
from flask import render_template
from fruitBasket import basket
from flask import request

app = Flask(__name__)

# Starting Endpoint that doesn't take a name
@app.route("/")
def index_no_name():
    return render_template("index_no_name.html")

@app.route("/create_basket")
def create_basket():
    return render_template("create_basket.html")

@app.route('/add_fruit', methods=['POST'])
def add_fruit():
    fruit = request.form['fruit']
    quantity = request.form['quantity']

    with sqlite3.connect("fruit.db") as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO fruitbasket (fruit, quantity) VALUES (?,?)", (fruit, quantity))
        conn.commit()
        # conn.close()
    return render_template("create_basket.html")

@app.route('/view_basket')
def view_basket():
    con = sqlite3.connect("fruit.db")
    con.row_factory = sqlite3.Row
    
    cur = con.cursor()
    cur.execute("SELECT * from fruitbasket")           # pull all information from the table "students"
    
    rows = cur.fetchall()
    return render_template("view_basket.html", rows=rows)



# Endpoint that takes a name
@app.route("/<name>")
def index_with_name(name):
    return render_template("index_with_name.html", username = name)

# Fruits Endpoint
@app.route("/fruits")
def fruit():
    return jsonify(basket())

def fruitDB():
    con = sqlite3.connect('fruit.db')
    print("Opened database successfully")
    # ensure that the table students is ready to be written to
    con.execute('CREATE TABLE IF NOT EXISTS fruitbasket (fruit TEXT, quantity TEXT)')
    print("Table created successfully")
    con.close()

if __name__ == "__main__":
   fruitDB()
   app.run(host="0.0.0.0", port=2224)