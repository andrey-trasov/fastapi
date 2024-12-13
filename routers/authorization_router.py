from authx import AuthX, AuthXConfig, TokenPayload
from fastapi import Response, Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from config.config_bd import SessionLocal
from schemas.authorization_schema import UserLoginSchema
from services.authorization_service import checking_the_data

from dotenv import load_dotenv
import os

load_dotenv()

# Настройка авторизации
config = AuthXConfig()
config.JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config=config)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/login')
async def login(creds: UserLoginSchema, response: Response, db: Session = Depends(get_db)):
    if await checking_the_data(db, creds):
        access_token = security.create_access_token(creds.username)
        refresh_token = security.create_refresh_token(creds.username)
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, access_token)    #запись токина в куки
        response.set_cookie(config.JWT_REFRESH_COOKIE_NAME, refresh_token)    #запись токина в куки
        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }
    raise HTTPException(401, "Bad username/password")
