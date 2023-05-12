from pydantic import BaseModel
from typing import Optional

class UserInBD(BaseModel):
    login: str
    password: str
    name: Optional[str] = None
    surname: Optional[str] = None
    fatherName: Optional[str] = None
    emal: str

class UserRegister(BaseModel):
    login: str
    password: str
    email: str

class UserAuthorization(BaseModel):
    login: str
    password: str

