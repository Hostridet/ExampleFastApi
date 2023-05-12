from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter, Response
import json
from base_models import User
from models.users_model import *
from utils import get_db_connection
router = APIRouter()


@router.get("/user/")
async def get_user_info(user_id: int):
    conn = get_db_connection()
    x = get_one_user(conn, user_id)
    if len(x) == 0:
        return Response("{'message':'Пользователь не найден'}", status_code=401)
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.post("/login/")
async def user_authorization(user: User.UserAuthorization):
    conn = get_db_connection()
    x = authorisation(conn, user.login, user.password)
    if len(x) == 0:
        return Response("{'message':'Неправильный логин или пароль'}", status_code=401)
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.get("/user/all")
async def get_all_users():
    conn = get_db_connection()
    x = get_users(conn)
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.post("/user/create")
async def create_user(user: User.UserRegister):
    conn = get_db_connection()
    x = insert_user(conn, user.login, user.password, user.email)
    return Response("{'message':'Пользователь создан'}", status_code=200)

@router.post("/user/update/name")
async def user_update_name(user_id: int, name: str):
    conn = get_db_connection()
    x = update_user_name(conn, user_id, name)
    return Response("{'message':'Имя обновлено'}", status_code=200)
