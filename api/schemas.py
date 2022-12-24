import pydantic as _pydantic
import datetime as _dt


class _UsersBase(_pydantic.BaseModel):
    name: str
    surname: str
    date_of_birth: _dt.date
    telephone: str
    mail: str
    client: int
    password: str


class UsersCreate(_UsersBase):
    pass


class Users(_UsersBase):
    id: int

    class Config:
        orm_mode = True


class _AppointmentsBase(_pydantic.BaseModel):
    user_id: int
    service: str
    date: _dt.date
    time: _dt.time
    hair_length: str
    loc_lat: str
    loc_long: str


class AppointmentsCreate(_AppointmentsBase):
    pass


class Appointments(_AppointmentsBase):
    id: int

    class Config:
        orm_mode = True


class _CredentialsBase(_pydantic.BaseModel):
    user_id: int
    master_id: int


class CredentialsCreate(_CredentialsBase):
    pass


class Credentials(_CredentialsBase):
    id: int

    class Config:
        orm_mode = True


class _ConfirmationsBase(_pydantic.BaseModel):
    user_id: int
    master_id: int
    appointment_id: int
    price: int


class ConfirmationsCreate(_ConfirmationsBase):
    pass


class Confirmations(_ConfirmationsBase):
    id: int

    class Config:
        orm_mode = True


class _AcceptsBase(_pydantic.BaseModel):
    user_id: int
    master_id: int
    appointment_id: int
    price: int


class AcceptsCreate(_AcceptsBase):
    pass


class Accepts(_AcceptsBase):
    id: int

    class Config:
        orm_mode = True
