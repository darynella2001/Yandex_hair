import sqlalchemy.orm as _orm
import models as _models, schemas as _schemas, database as _database


def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_users_by_id(db: _orm.Session, id: int):
    return db.query(_models.Users).filter(_models.Users.id == id).first()


# def get_patients_by_doctor_id(db: _orm.Session, doctor_id: int):
#     return db.query(_models.Patients).filter( _models.Patients.doctor_id == doctor_id).all()

def get_users(db: _orm.Session):
    return db.query(_models.Users).all()

def get_appointments(db: _orm.Session):
    return db.query(_models.Appointments).all()

def get_appointments_by_id(db: _orm.Session, id: int):
    return db.query(_models.Appointments).filter(_models.Appointments.id == id).first()


def create_user(db: _orm.Session, user:_schemas.UsersCreate):
    db_user=_models.Users(name=user.name, surname=user.surname, date_of_birth=user.date_of_birth, telephone=user.telephone, mail=user.mail, client=user.client, password = user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_appointment(db: _orm.Session, appointment:_schemas.AppointmentsCreate):
    db_appointment=_models.Appointments(user_id=appointment.user_id, service=appointment.service, date=appointment.date, time=appointment.time, hair_length=appointment.hair_length, loc_lat=appointment.loc_lat, loc_long=appointment.loc_long)
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment


# def delete_patient_and_its_analysis(db:_orm.Session, id: int):
#     db.query(_models.Patients).filter(_models.Patients.id == id).delete()
#     db.query(_models.Analysis).filter(_models.Analysis.user_id == id).delete()
#     db.commit()


# def create_doctor(db: _orm.Session, doctor:_schemas.DoctorsCreate):
#     db_doctor=_models.Doctors(name=doctor.name,surname=doctor.surname,date_of_birth=doctor.date_of_birth,specialization=doctor.specialization, email=doctor.email)
#     db.add(db_doctor)
#     db.commit()
#     db.refresh(db_doctor)
#     return db_doctor


# def get_doctors(db: _orm.Session):
#     return db.query(_models.Doctors).all()


# def get_doctors_by_id(db: _orm.Session, id: int):
#     return db.query(_models.Doctors).filter(_models.Doctors.id == id).first()


# def delete_doctor_and_its_users(db: _orm.Session, id: int):
#     db.query(_models.Doctors).filter(_models.Doctors.id == id).delete()
#     db.query(_models.Patients).filter(_models.Patients.doctor_id == id).delete()
#     db.commit()


# def delete_duplicates(db:_orm.Session, user_id: int):
#     db.query(_models.Analysis).filter(_models.Analysis.user_id == user_id).delete()


# def create_analysis(db: _orm.Session, analysis:_schemas.AnalysisCreate, id:int):
#     # delete_duplicates(db=db, user_id=id)
#     db_analysis=_models.Analysis(systolic=analysis.systolic, diastolic= analysis.diastolic, cholesterol=analysis.cholesterol, glucose=analysis.glucose,date=analysis.date, user_id=id)

#     db.add(db_analysis)
#     db.commit()
#     db.refresh(db_analysis)
#     return db_analysis


# def get_analysis(db: _orm.Session, id:int):
#  return db.query(_models.Analysis).filter(_models.Analysis.user_id == id).all()

# def delete_analysis(db:_orm.Session, user_id: int, id:int):
#     db.query(_models.Analysis).filter(_models.Analysis.user_id == user_id, _models.Analysis.id == id).delete()
#     db.commit()


# def delete_analysis_by_userid(db:_orm.Session, user_id: int):
#     db.query(_models.Analysis).filter(_models.Analysis.user_id == user_id).delete()
#     db.commit()

