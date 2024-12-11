from schemas.user_schema import UserOut, UserCreate
from fastapi import Depends, APIRouter
from config.config_bd import SessionLocal
from sqlalchemy.orm import Session
from services.user_service import create_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# создаение пользователя
@router.post("/user/", response_model=UserOut)
async def post_create_user(reader: UserCreate, db: Session = Depends(get_db)):
    return await create_user(db, reader)