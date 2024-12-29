from fastapi import FastAPI, Path, HTTPException, Request, Form
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Annotated, List

app = FastAPI()

templates = Jinja2Templates(directory="templates")

users = []

class User:
    id: int
    username: str
    age: int

@app.get("/")
async def all_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get("/user/{user_id}")
async def get_user(request: Request, user_id: Annotated[int, Path(ge=1, le=100, description="Enter user id", example="1")]):
    user = next((user for user in users if user.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User Not Found")
    return templates.TemplateResponse("users.html", {"request": request, "user": user})

@app.post('/user/{username}/{age}')
async def create_user(
    username: Annotated[str, Path(min_length=5, max_length=20, description='Enter your username', example="UrbanUser")],
    age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]
) -> User:
    new_id = users[-1].id + 1 if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user

@app.put('/user/{user_id}')
async def update_user(
    user_id: Annotated[int, Path(ge=1, le=100, description="Enter user id", example="1")],
    username: Annotated[str, Path(min_length=5, max_length=20, description='Enter your username', example="UrbanUser")],
    age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]
) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User Not Found")

@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter id", example="1")]) -> dict:
    for i, user in enumerate(users):
        if user.id == user_id:
            users.pop(i)
            return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User Not Found")
