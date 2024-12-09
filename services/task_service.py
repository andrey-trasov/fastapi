# Бизнес логика работы с задачами
from sqlalchemy.orm import Session

from models.models import Task
from schemas.task_schema import TaskCreate, TaskUpdate


# создаение задач
async def create_task(db: Session, task: TaskCreate):
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# просмотр 1 задачи
async def read_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

# просмотр списка задач
async def read_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Task).offset(skip).limit(limit).all()

# редакторование задачи
async def update_task(db: Session, task_id: int, task: TaskUpdate):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    for var, value in vars(task).items():
        setattr(db_task, var, value) if value else None
    db.commit()
    db.refresh(db_task)
    return db_task

# удаление задачи
async def delete_task(db: Session, task_id: int):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    db.delete(db_task)
    db.commit()
    return db_task
