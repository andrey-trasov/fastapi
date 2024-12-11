from sqlalchemy.orm import Session

from schemas.user_schema import UserCreate
from models.users import Users

import hashlib

#хешируем пароль
async def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# создаение задач
async def create_user(db: Session, task: UserCreate):
    task.password = await hash_password(task.password)
    db_task = Users(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task