from fastapi import FastAPI, Path

from pydantic import BaseModel
from typing import Annotated
app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/user")
async  def all_users()->dict:
    return users

@app.post('/user/{username}/{age}' )
async def create_user(username:Annotated[str,Path(min_length=5,max_length=20, description='Enter your username',example="UrbanUser")],age:Annotated[int,Path(ge=18,le=120,description="Enter age",example="24")])-> str:
    new_user_id = str(max(map(int, users.keys())) + 1)
    users[new_user_id] = f"Имя: {username}, возраст: {age}"
    return "Пользователь зарегестрирован"

@app.put('/user/{username}/{age}' )
async def create_user(user_id:Annotated[str,Path(ge=1,le=100000,description="Enter id",example="1")],username:Annotated[str,Path(min_length=5,max_length=20, description='Enter your username',example="UrbanUser")],age:Annotated[int,Path(ge=18,le=120,description="Enter age",example="24")])-> str:
    if user_id in users:
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return f"Данные пользователя {user_id}  обновлены"
    return f"пользователь {user_id} не найден"

@app.delete('/user/{user_id}')
async def delete_user(user_id:Annotated[str,Path(ge=1,le=100000,description="Enter id",example="1")])-> str:
    if user_id in users:
        users.pop(user_id)
        return f"Пользователь {user_id} удален."
    return f"пользователь {user_id} не найден"
    
