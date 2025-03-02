from fastapi import FastAPI
from db.init_db import init_db
from routers import mosque, user
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from config.settings import DATABASE_URL
app = FastAPI()

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

@app.on_event("startup")
async def startup_event():
    await init_db()

app.include_router(mosque.router)
app.include_router(user.router)