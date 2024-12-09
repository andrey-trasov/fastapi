# # database.py
# from databases import Database
# from sqlalchemy import create_engine, MetaData
# from sqlalchemy.ext.declarative import declarative_base
#
# DATABASE_URL = "postgresql+asyncpg://postgres:12345@localhost/fastapi_z2"
#
# database = Database(DATABASE_URL)
# metadata = MetaData()
# engine = create_engine(DATABASE_URL)
# Base = declarative_base()
#
# async def init_db():
#     async with database:
#         await database.connect()
