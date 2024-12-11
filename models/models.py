# Описание моделей базы данных
from sqlalchemy import Column, Integer, Date, String, ForeignKey
from sqlalchemy.orm import relationship

from config.config_bd import Base


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    status = Column(String, index=True)
    date_of_creation = Column(Date)
    users = Column(Integer, ForeignKey('users.id'))


# from datetime import date
#
# from pydantic import BaseModel, EmailStr, Field
#
#
# class TaskSchema(BaseModel):
#     id: int
#     name: EmailStr
#     description: str = Field(max_length=1000)   #максимум 1000 символов
#     status: str
#     date_of_creation: date = date()
