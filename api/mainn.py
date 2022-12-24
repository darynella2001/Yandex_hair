from datetime import datetime
import os
from tokenize import String
import json
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate
from sqlalchemy import DateTime
import requests
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my.db"
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)


class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=False, nullable=False)
    surname = db.Column(db.String(15), unique=False, nullable=False)
    date_of_birth = db.Column(db.Date, unique=False, nullable=False)
    telephone = db.Column(db.String(15), unique=False, nullable=False)
    mail = db.Column(db.String(35), unique=True, nullable=False)
    client = db.Column(db.Integer, unique=False, nullable=False)
    password = db.Column(db.String(25), unique=False, nullable=False)


class Appontents(db.Model):
    __tablename__ = "appointments"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    service = db.Column(db.String(35), unique=True, nullable=False)
    date = db.Column(db.Date, unique=False, nullable=False)
    time = db.Column(db.Time, unique=False, nullable=False)
    hair_length = db.Column(db.String(35), unique=True, nullable=False)
    loc_lat = db.Column(db.String(35), unique=True, nullable=False)
    loc_long = db.Column(db.String(35), unique=True, nullable=False)


class Confirmations(db.Model):
    __tablename__ = "confirmations"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    master_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointments.id'))
    price = db.Column(db.Integer, unique=False, nullable=False)


class Accepts(db.Model):
    __tablename__ = "accepts"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    master_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointments.id'))

    # datetime = db.Column(DateTime, default=datetime.datetime.utcnow)


@app.before_first_request
def create_tables():
    db.create_all()


@app.route("/signup", methods=["POST", "GET"])
def save_record():
    if request.method == "POST":
        json_d = request.data.decode('utf-8')
        json_data = json.loads(json_d)
        print(json_data)
        print(json_data["name"])
        UsersRecord = Users(
            name=json_data["name"],
            surname=json_data["surname"],
            date_of_birth=datetime.strptime(
                json_data["date_of_birth"], "%Y-%m-%d"),
            telephone=json_data["telephone"],
            mail=json_data["mail"],
            client=json_data["client"],
            password=json_data["password"]
        )

        db.session.add(UsersRecord)
        db.session.commit()
        return {
            "status": 200
        }, 200


@app.route("/order", methods=["POST", "GET"])
def create_order():
    if request.method == "POST":
        json_d = request.data.decode('utf-8')
        json_data = json.loads(json_d)
        print(json_data)
        # print(json_data["name"])
        UsersRecord = Users(
            service=json_data["service"],
            date=datetime.strptime(
                json_data["date"], "%Y-%m-%d"),
            time=datetime.strptime(
                json_data["time"], "%H:%M"),
            loc_lat=json_data["loc_lat"],
            loc_long=json_data["loc_long"]
        )

        db.session.add(UsersRecord)
        db.session.commit()
        return {
            "status": 200
        }, 200


if __name__ == '__main__':

    app.run(host='localhost', port=8000)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
