from fastapi import APIRouter
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from app.backend.db import Base
from sqlalchemy.orm import relationship
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import insert, select, update, delete
from typing import List, Annotated
from app.backend.db_depends import get_db
from app.schemas import CreateUser, UpdateUser,UserResponse
from slugify import slugify

router = APIRouter(prefix="/user", tags=["user"])

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    slug = Column(String, unique=True, index=True)
    age = Column(Integer)
    tasks = relationship("Task", back_populates='user')

@router.get("/", response_model=List[UserResponse])
def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users

@router.get("/user/{user_id}", response_model=UserResponse)
def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    return user

@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_user(new_user: CreateUser, db: Annotated[Session, Depends(get_db)]):
    slug = slugify(new_user.username)  # Создание slug для username
    stmt = insert(User).values(
        username=new_user.username,
        firstname=new_user.firstname,
        lastname=new_user.lastname,
        age=new_user.age,
        slug=slug
    )
    try:
        db.execute(stmt)
        db.commit()
        return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/update/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id: int, updated_user: UpdateUser, db: Annotated[Session, Depends(get_db)]):
    stmt = update(User).where(User.id == user_id).values(
        firstname=updated_user.firstname,
        lastname=updated_user.lastname,
        age=updated_user.age
    )
    result = db.execute(stmt)
    db.commit()
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="User was not found")
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}

@router.delete("/delete/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    stmt = delete(User).where(User.id == user_id)
    result = db.execute(stmt)
    db.commit()
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="User was not found")
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User deletion'}

from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))