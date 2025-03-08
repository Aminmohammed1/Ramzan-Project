from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.init_db import SessionLocal
from models.mosque import Mosque
from models.prayer_timing import PrayerTiming
from pydantic import BaseModel
from database import get_db
from datetime import time, date

router = APIRouter()

class MosqueCreateRequest(BaseModel):
    name: str
    latitude: float
    longitude: float
    address: str
    user_id: int

@router.post("/mosques/")
async def add_mosque(req: MosqueCreateRequest, db: AsyncSession = Depends(get_db)):
    # Create a new PrayerTiming instance with default values
    prayer_timings = PrayerTiming(
        fajr=time(5, 0),
        dhuhr=time(12, 0),
        asr=time(15, 0),
        maghrib=time(18, 0),
        isha=time(20, 0),
        date=date.today()  # Use Python's date.today() for the current date
    )
    
    # Create a new Mosque instance
    mosque = Mosque(
        name=req.name,
        location=f'POINT({req.longitude} {req.latitude})',
        address=req.address,
        # added_by=req.user_id,
        prayer_timings=[prayer_timings]  # Add the prayer timings to the mosque
    )
    
    # Add the new mosque to the session and commit the transaction
    db.add(mosque)
    await db.commit()
    await db.refresh(mosque)  # Refresh the instance to get the generated ID
    
    return {"message": "Mosque added!", "mosque_id": mosque.id}

@router.get("/users/{user_id}/mosques")
async def get_mosques_by_user(user_id: str, db: AsyncSession = Depends(SessionLocal)):
    result = await db.execute(f"SELECT * FROM mosques WHERE added_by = '{user_id}'")
    return result.fetchall()