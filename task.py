from fastapi import APIRouter
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from app.backend.db import Base
from sqlalchemy.orm import relationship

router = APIRouter(prefix="/task", tags=["task"])

class Task(Base):
    __tablename__ = "tasks"
    __table_args__ = {"keep_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    title = Column(String)
    slug = Column(String, unique=True, index=True)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=True,index=True)
    user = relationship("User", back_populates='tasks')

@router.get("/")
async  def all_tasks():
    pass

@router.get("/task_id")
async  def task_by_id():
    pass

@router.post("/create")
async  def create_task():
    pass

@router.put("/update")
async def update_task():
    pass

@router.delete("/delete")
async  def del_task():
    pass

from sqlalchemy.schema import CreateTable
print(CreateTable(Task.__table__))