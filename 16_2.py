from fastapi import FastAPI,Path
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "главная страница"}
@app.get("/user/admin")
async def admin():
    return {"message": "Вы вошли как админ"}

@app.get("/user/{user_id}")
async def user_id(user_id:int)->dict:
    return {"message": f"Вы вошли как пользователь {user_id}"}

@app.get("/user/admin")
async def admin():
    return {"message": "Вы вошли как админ"}

@app.get("/user/{username}/{age}")
async def news(username:str = Path(min_length=5,max_length=20, description='Enter your username',example="UrbanUser"),id:int = Path(ge=18,le=120,description="Enter age",example="24"))->dict:
    return{"message": f"Hello, {username} {id}"}
