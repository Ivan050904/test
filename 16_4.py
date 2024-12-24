from fastapi import FastAPI, Path,HTTPException

from pydantic import BaseModel
from typing import Annotated,List
app = FastAPI()

users = []

class User:
    id:int
    username: str
    age:int

@app.get("/user")
async  def all_users()->List:
    return users

@app.post('/user/{username}/{age}' )
async def create_user(username:str,age:int):
    new_id = users[-1].id+1 if users else 1
    new_user = User(id=new_id,username= username,age=age)
    users.append((new_user))
    return new_user

@app.put('/user/{username}/{age}' )
async def create_user(user_id:int,username:str,age:int):
    try:
        for user in users:
            if user.id == user_id:
                user.username = username
                user.age = age
                return user
    except:
        raise HTTPException(status_code=404, detail="User Not Found")


@app.delete('/user/{user_id}')
async def delete_user(user_id:int) -> dict:
    try:
        for i,user in enumerate (users):
            if user.id == user_id :
                users.pop(i)
    except:
        raise HTTPException(status_code=404, detail="User Not Found")


