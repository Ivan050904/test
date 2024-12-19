from fastapi import FastAPI, Path

from pydantic import BaseModel
from typing import Annotated
app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/user")
async  def all_users()->dict:
    return users

@app.post('/user/{username}/{age}' )
async def create_user(username:str,age:int):
    new_user_id = str(max(map(int, users.keys())) + 1)
    users[new_user_id] = f"Имя: {username}, возраст: {age}"
    return "Пользователь зарегестрирован"

@app.put('/user/{username}/{age}' )
async def create_user(user_id:int,username:str,age:int):
    if user_id in users:
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return f"Данные пользователя {user_id}  обновлены"
    return f"пользователь {user_id} не найден"

@app.delete('/user/{user_id}')
async def delete_user(user_id:int) -> dict:
    users.pop(user_id)
    return f"Пользователь {user_id} удален."
