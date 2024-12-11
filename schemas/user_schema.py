from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    password: str

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True