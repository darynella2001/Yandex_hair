import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import datetime as _dt

import database as _database


class Users(_database.Base):
    __tablename__ = "users"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.Text)
    surname = _sql.Column(_sql.Text)
    date_of_birth = _sql.Column(_sql.Date)
    telephone = _sql.Column(_sql.Text)
    mail = _sql.Column(_sql.Text, unique=True)
    client = _sql.Column(_sql.Integer)
    password = _sql.Column(_sql.Text)


class Appointments(_database.Base):
    __tablename__ = "appointments"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    user_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))
    service = _sql.Column(_sql.String)
    date = _sql.Column(_sql.Date)
    time = _sql.Column(_sql.Time)
    hair_length = _sql.Column(_sql.Text)
    loc_lat = _sql.Column(_sql.Text)
    loc_long = _sql.Column(_sql.Text)


# class Credentials(_database.Base):
#     __tablename__= "credentials"
#     id = _sql.Column(_sql.Integer, primary_key=True, index=True)
#     user_id = _sql.Column(_sql.Integer,_sql.ForeignKey("users.id"))
#     master_id = _sql.Column(_sql.Integer,_sql.ForeignKey("users.id"))

    # owner = _orm.relationship("Patients", back_populates="analysis")

class Confirmations(_database.Base):
    __tablename__ = "confirmations"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    user_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))
    master_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))
    appointment_id = _sql.Column(
        _sql.Integer, _sql.ForeignKey("appointments.id"))
    price = _sql.Column(_sql.Integer)


class Accepts(_database.Base):
    __tablename__ = "accepts"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    user_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))
    master_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))
    appointment = _sql.Column(_sql.Integer, _sql.ForeignKey("appointments.id"))
