# main.py
from config.config_bd import engine, Base, database, SessionLocal
from models.models import Task  # Импортируем модель
from routers import task_router
from schemas.task_schema import TaskCreate, TaskOut
from services.task_service import create_task

# Создание всех таблиц в базе данных
Base.metadata.create_all(bind=engine)


from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

app = FastAPI()

app.include_router(task_router.router)


@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# app.include_router(task_router.router)

# # Маршруты для читателей
# @app.post("/readers/", response_model=TaskOut)
# async def create_reader(reader: TaskCreate, db: Session = Depends(get_db)):
#     return await create_task(db, reader)