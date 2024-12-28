from fastapi import FastAPI, Path, HTTPException

from pydantic import BaseModel
from typing import Annotated,List
app = FastAPI()

users = []

class User:
    id: int
    username: str
    age: int

@app.get("/user")
async  def all_users() -> List:
    return users

@app.post('/user/{username}/{age}' )
async def create_user(username:Annotated[str,Path(min_length=5,max_length=20, description='Enter your username',example="UrbanUser")],age:Annotated[int,Path(ge=18,le=120,description="Enter age",example="24")])-> str:
    new_id = users[-1].id+1 if users else 1
    new_user = User(id=new_id,username= username,age=age)
    users.append((new_user))
    return new_user

@app.put('/user/{username}/{age}' )
async def create_user(user_id:Annotated[str,Path(ge=1,le=100,description="Enter user id",example="1")],username:Annotated[str,Path(min_length=5,max_length=20, description='Enter your username',example="UrbanUser")],age:Annotated[int,Path(ge=18,le=120,description="Enter age",example="24")])-> str:
    try:
        for user in users:
            if user.id == user_id:
                user.username = username
                user.age = age
                return user
    except:
        raise HTTPException(status_code=404, detail="User Not Found")


@app.delete('/user/{user_id}')
async def delete_user(user_id:Annotated[str,Path(ge=1,le=100,description="Enter id",example="1")]) -> dict:
    try:
        for i,user in enumerate (users):
            if user.id == user_id :
                users.pop(i)
    except:
        raise HTTPException(status_code=404, detail="User Not Found")


