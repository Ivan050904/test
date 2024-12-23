from fastapi import FastAPI,Path
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

@app.get("/")
async def welcome()-> str:
    return {"message": "главная страница"}
@app.get("/user/admin")
async def admin()-> str:
    return {"message": "Вы вошли как админ"}

@app.get("/user/{user_id}")
async def user_id(user_id:int)-> str:
    return {"message": f"Вы вошли как пользователь {user_id}"}

@app.get("/user/{username}/{age}")
async def news(username:Annotated[str,Path(min_length=5,max_length=20, description='Enter your username',example="UrbanUser")],age:Annotated[int,Path(ge=18,le=120,description="Enter age",example="24")])-> str:
    return{"message": f"Hello, {username} {id}"}
