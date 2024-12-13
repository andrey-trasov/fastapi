# файл конфигурации для подключения к базе данных и настройте движок

from dotenv import load_dotenv
import os

load_dotenv()


# Настройка базы данных
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database

DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}/{os.getenv('POSTGRES_DB')}"

# Движок для синхронного использования
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Движок для асинхронного использования
database = Database(DATABASE_URL)

# Создание базового класса
Base = declarative_base()

# Создание фабрики сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)