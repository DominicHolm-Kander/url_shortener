from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
# To actually create the db: open python shell, from app import db, db.create_all()

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    regular_url = db.Column(db.String(120), nullable = False)
    shortened_url = db.Column(db.String(10), nullable = False)


from app import routes