import os
from sqla_wrapper import SQLAlchemy

db = SQLAlchemy(os.getenv("DATABASE_URL", "sqlite:///localhost.sqlite"))
# this connects to a database either on Heroku or on localhost


class User(db.Model):
    __tablename__ = "User"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)


class Destiny(db.Model):
    __tablename__ = "Destiny"

    id = db.Column(db.Integer, primary_key=True)
    destinatario = db.Column(db.String, unique=True)
    email_destiny = db.Column(db.String, unique=True)
    message_sent = db.Column(db.String, unique=False)
