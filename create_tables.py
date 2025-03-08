from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from models.mosque import Mosque
from models.prayer_timing import PrayerTiming
from models.user import User
from db.init_db import Base

DATABASE_URL = "postgresql+asyncpg://admin:secret@localhost/mosque_db"

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

import asyncio
asyncio.run(init_db())