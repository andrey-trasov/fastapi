# Модели Pydantic для валидации данных
from datetime import date

from pydantic import BaseModel, EmailStr


class TaskBase(BaseModel):
    name: EmailStr
    description: str
    status: str
    date_of_creation: date = date.today()

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class TaskOut(TaskBase):
    id: int

    class Config:
        orm_mode = True