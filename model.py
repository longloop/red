from flask.ext.sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
db = SQLAlchemy(app)
 
 
class Todo (db.Model):
    __tablename__ = "latlng"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.Unicode)
    lat = db.Column('lat', db.Integer)
    lng = db.Column('lng', db.Integer) 