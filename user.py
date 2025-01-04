from fastapi import APIRouter
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from app.backend.db import Base
from sqlalchemy.orm import relationship

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

@router.get("/")
async  def all_users():
    pass

@router.get("/user_id")
async  def user_by_id():
    pass

@router.post("/create")
async  def create_user():
    pass

@router.put("/update")
async def update_user():
    pass

@router.delete("/delete")
async  def del_user():
    pass

from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))