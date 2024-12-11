# main.py
from fastapi import FastAPI
from config.config_bd import engine, Base, database, SessionLocal

from routers import task_router, user_router, authorization_router

# Создание всех таблиц в базе данных
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(task_router.router)
app.include_router(user_router.router)
app.include_router(authorization_router.router)


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

# авторизация

# from authx import AuthX, AuthXConfig, TokenPayload
# from fastapi import Response
#
# config = AuthXConfig()
# config.JWT_SECRET_KEY = "SECRET_KEY"
# # config.JWT_ACCESS_COOKIE_NAME = "my_access_token"
# config.JWT_TOKEN_LOCATION = ["cookies"]
#
# security = AuthX(config=config)


# class UserLoginSchema(BaseModel):
#     username: str
#     password: str



# def checking_the_data(db: Session, creds: UserLoginSchema):
#     bd_creds = db.query(Users).filter(Users.username == creds.username).first()
#     if not bd_creds is None and bd_creds.password == hash_password(creds.password):
#         return True
#     return False



# @app.post('/login')
# def login(creds: UserLoginSchema, response: Response, db: Session = Depends(get_db)):
#     if checking_the_data(db, creds):
#         access_token = security.create_access_token(creds.username)
#         refresh_token = security.create_refresh_token(creds.username)
#         response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, access_token)
#         response.set_cookie(config.JWT_REFRESH_COOKIE_NAME, refresh_token)
#         return {
#             "access_token": access_token,
#             "refresh_token": refresh_token
#         }
#     raise HTTPException(401, "Bad username/password")





# @app.get("/protected/", dependencies=[Depends(security.access_token_required)])
# def protected():
#     return {"test": "YES"}


