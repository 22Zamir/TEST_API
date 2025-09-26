# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set")

# --- Асинхронный движок (для FastAPI) ---
async_engine = create_async_engine(
    DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://"),
    echo=True,
)

AsyncSessionLocal = sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)

# --- Синхронный движок (для Alembic) ---
sync_engine = create_engine(
    DATABASE_URL.replace("postgresql://", "postgresql+psycopg2://"),
    echo=True,
)

# Сессия для Alembic и синхронных операций
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=sync_engine)

Base = declarative_base()


# Функция зависимости для FastAPI
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session