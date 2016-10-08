#
#
#        Use app.py instead
#
#
#

from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/red'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route("/")
def outp():
    return "Hey!"

@app.route('/', methods=['POST'])
def inp():
    name=request.form['name']
    lat=request.form['lat']
    lng=request.form['lng']
    data = User('name', 111, 222)
    db.session.add(data)
    return name

if __name__ == "__main__":
    app.run()