# Асинхронные API эндпоинты
from typing import List

from config.config_bd import SessionLocal
from schemas.task_schema import TaskCreate, TaskOut, TaskUpdate
from services.task_service import create_task, read_task, read_tasks, update_task, delete_task
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, HTTPException

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# создаение задач
@router.post("/task/", response_model=TaskOut)
async def post_create_task(reader: TaskCreate, db: Session = Depends(get_db)):
    return await create_task(db, reader)

# просмотр 1 задачи
@router.get("/task/{task_id}", response_model=TaskOut)
async def get_read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = await read_task(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

# просмотр списка задач
@router.get("/task/", response_model=List[TaskOut])
async def get_read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    task = await read_tasks(db, skip, limit)
    return task

# редакторование задачи
@router.put("/task/{task_id}", response_model=TaskOut)
async def put_update_task(task_id: int, reader: TaskUpdate, db: Session = Depends(get_db)):
    return await update_task(db, task_id, reader)

# удаление задачи
@router.delete("/task/{task}", response_model=TaskOut)
async def delete_delete_task(task_id: int, db: Session = Depends(get_db)):
    return await delete_task(db, task_id)

