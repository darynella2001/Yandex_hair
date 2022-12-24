import asyncio

import fastapi as _fastapi
from typing import List
import sqlalchemy.orm as _orm
import schemas as _schemas
import services as _services
import uvicorn
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
import datetime as _dt

app = _fastapi.FastAPI()

security = HTTPBasic()
_services.create_database()

HOST = "localhost"
PORT = 8000


@app.post("/signup/", response_model=_schemas.Users)
def create_user(user: _schemas.UsersCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    print(user.dict())
    return _services.create_user(db=db, user=user)

# @app.post("/login/",response_model=_schemas.Users)
# async def login(username: str, password:str):

#     return users


@app.get("/user/", response_model=List[_schemas.Users])
async def read_users(db: _orm.Session = _fastapi.Depends(_services.get_db)):
    users = _services.get_users(db=db)
    return users


@app.get("/user/{id}", response_model=_schemas.Users)
async def read_specific_user(id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    db_user = _services.get_users_by_id(db=db, id=id)
    return db_user


@app.post("/order/", response_model=_schemas.Appointments)
def create_appointment(appointment: _schemas.AppointmentsCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)):

    return _services.create_appointment(db=db, appointment=appointment)


@app.get("/appointment/", response_model=List[_schemas.Appointments])
async def read_appointments(db: _orm.Session = _fastapi.Depends(_services.get_db)):
    appointments = _services.get_appointments(db=db)
    return appointments


@app.get("/appointment/{id}", response_model=_schemas.Appointments)
async def read_specific_appointment(id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    db_appointment = _services.get_appointments_by_id(db=db, id=id)
    return db_appointment


# @app.get("/patient/doctor/{doctor_id}", response_model=List[_schemas.Patients])
# async def read_patients(doctor_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
#     patients = _services.get_patients_by_doctor_id(db=db, doctor_id = doctor_id)
#     await counter_function()
#     return patients

# @app.delete("/patient/", response_model=_schemas.Patients)
# async def delete_patients(id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
#     db_patients = _services.get_patients_by_id(db=db, id=id)
#     if db_patients is None:
#         raise _fastapi.HTTPException(
#             status_code=400, detail="woops this patient doesn't exists"
#         )

#     await counter_function()
#     return _services.delete_patient_and_its_analysis(db=db, id=id)


# @app.post("/doctor/", response_model=_schemas.Doctors)
# async def create_doctor(doctor: _schemas.DoctorsCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)):
#     # db_patient = _services.get_patients_by_id(db=db, id=patient.id)
#     # if db_patient:
#     #     raise _fastapi.HTTPException(
#     #         status_code=400, detail="woops "
#     #     )

#     await counter_function()
#     return _services.create_doctor(db=db, doctor=doctor)


# @app.get("/doctors/", response_model=List[_schemas.Doctors])
# async def read_doctors(db: _orm.Session = _fastapi.Depends(_services.get_db)):
#     doctors = _services.get_doctors(db=db)
#     await counter_function()
#     return doctors


# @app.delete("/doctors/", response_model=_schemas.Doctors)
# async def delete_doctors(id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
#     db_doctors = _services.get_doctors_by_id(db=db, id=id)
#     if db_doctors is None:
#         raise _fastapi.HTTPException(
#             status_code=400, detail="woops this doctor doesn't exists"
#         )
#     await counter_function()

#     return _services.delete_doctor_and_its_users(db=db, id=id)


# @app.post("/analysis/{id}", response_model=_schemas.Analysis)
# async def create_analysis(id: int, analysis: _schemas.AnalysisCreate,
#                       db: _orm.Session = _fastapi.Depends(_services.get_db)):
#     db_analysis = _services.get_patients_by_id(db=db, id=id)
#     if db_analysis is None:
#         raise _fastapi.HTTPException(
#             status_code=400, detail="woops this patient doesn't exists"
#         )

#     await counter_function()
#     return _services.create_analysis(db=db, analysis=analysis, id=id)


# @app.get('/delete_patient_analysis/{id}')
# async def delete_patient_analysis_permission(id:int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
#     analysis = _services.get_analysis(db=db, id=id)
#     if analysis:
#         return 1
#     else:
#         return 0

# @app.get("/analysis/{id}", response_model=List[_schemas.Analysis])
# async def read_analysis(id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
#     db_analysis = _services.get_patients_by_id(db=db, id=id)
#     if db_analysis is None:
#         raise _fastapi.HTTPException(
#             status_code=400, detail="woops this patient doesn't exists"
#         )
#     analysis= _services.get_analysis(db=db, id=id)
#     await counter_function()
#     return analysis


# @app.delete("/analysis/{user_id}/{id}", response_model=List[_schemas.Analysis])
# async def delete_analysis(user_id:int ,id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
#     db_analysis = _services.get_patients_by_id(db=db, id=user_id)
#     if db_analysis is None:
#         raise _fastapi.HTTPException(
#             status_code=400, detail="woops this patient doesn't exists"
#         )
#     await counter_function()
#     return _services.delete_analysis(db=db, user_id=user_id, id=id)


# @app.delete("/analysis/{user_id}", response_model=List[_schemas.Analysis])
# async def delete_analysis_2(user_id:int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
#     db_analysis = _services.get_patients_by_id(db=db, id=user_id)
#     if db_analysis is None:
#         raise _fastapi.HTTPException(
#             status_code=400, detail="woops this patient doesn't exists"
#         )
#     await counter_function()
#     return _services.delete_analysis_by_userid(db=db, user_id=user_id)


if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST, port=PORT,
                log_level="info", reload=True)
