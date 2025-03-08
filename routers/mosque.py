from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db.init_db import SessionLocal
from models.mosque import Mosque
from pydantic import BaseModel
from database import get_db
router = APIRouter()
class req(BaseModel):
    name: str
    latitude: float
    longitude: float
    address: str
    user_id: int

@router.post("/mosques/")
async def add_mosque(req:req, db: AsyncSession = Depends(get_db)):
    mosque = Mosque(
        name=req.name, 
        location=f'POINT({req.longitude} {req.latitude})', 
        address=req.address, 
        added_by=req.user_id
    )
    print(mosque)
    print(db)
    db.add(mosque)
    await db.commit()
    return {"message": "Mosque added!", "mosque_id": mosque.id}
    # Dummy data for testing
    dummy_data = [
        {"name": "Mosque A", "latitude": 40.712776, "longitude": -74.005974, "address": "123 Main St, New York, NY", "user_id": "user1"},
        {"name": "Mosque B", "latitude": 34.052235, "longitude": -118.243683, "address": "456 Elm St, Los Angeles, CA", "user_id": "user2"},
        {"name": "Mosque C", "latitude": 41.878113, "longitude": -87.629799, "address": "789 Oak St, Chicago, IL", "user_id": "user3"}
    ]

@router.get("/users/{user_id}/mosques")
async def get_mosques_by_user(user_id: str, db: AsyncSession = Depends(SessionLocal)):
    result = await db.execute(f"SELECT * FROM mosques WHERE added_by = '{user_id}'")
    return result.fetchall()