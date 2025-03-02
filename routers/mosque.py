from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db.init_db import SessionLocal
from models.mosque import Mosque

router = APIRouter()

@router.post("/mosques/")
async def add_mosque(name: str, latitude: float, longitude: float, address: str, user_id: str, db: AsyncSession = Depends(SessionLocal)):
    mosque = Mosque(
        name=name, 
        location=f'POINT({longitude} {latitude})', 
        address=address, 
        added_by=user_id
    )
    db.add(mosque)
    await db.commit()
    return {"message": "Mosque added!", "mosque_id": mosque.id}

@router.get("/users/{user_id}/mosques")
async def get_mosques_by_user(user_id: str, db: AsyncSession = Depends(SessionLocal)):
    result = await db.execute(f"SELECT * FROM mosques WHERE added_by = '{user_id}'")
    return result.fetchall()