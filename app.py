from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)

@app.route('/')
def index():
    connect = sqlite3.connect('catalog.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM CATALOG')
    data = cursor.fetchall()
    return render_template("catalog.html", data=data)


