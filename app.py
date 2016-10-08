from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import sqlalchemy
import os

def connect():
    # We connect with the help of the PostgreSQL URL
    # postgresql://federer:grandestslam@localhost:5432/tennis
    url = 'postgresql://test:123@/localhost:5432/red'

    # The return value of create_engine() is our connection object
    con = sqlalchemy.create_engine(url, client_encoding='utf8')

    # We then bind the connection to MetaData()
    meta = sqlalchemy.MetaData(bind=con, reflect=True)

    return con, meta

con, meta = connect()

from sqlalchemy import Table, Column, Integer, String, ForeignKey

latlng = Table('latlng', meta,
    Column('name', String, primary_key=True),
    Column('lat', Number),
    Column('lng', Number)
) 
meta.create_all(con)

app = Flask(__name__)

@app.route("/")
def outp():
    return "Hey!"

@app.route('/', methods=['POST'])
def inp():
    name=request.form['name']
    lat=request.form['lat']
    lng=request.form['lng']
    clause = slams.insert().values(name='delhi', lat=111, lng=121)
    con.execute(clause)
    return name

if __name__ == "__main__":
    app.run()