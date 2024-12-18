from fastapi import FastAPI
from pydantic import BaseModel

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

@app.get("/user")
async  def id_registrator(username:str, age:int)->dict:
    return{"User":{username}, "age": {age}}
