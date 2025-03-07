from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text
from database import get_db
from models.user import User
from pydantic import BaseModel
import json
router = APIRouter()

class req(BaseModel):
    name: str
    email: str
    phone_number: str

@router.get("/users/phone/{phone_number}")
async def get_user_by_phone(phone_number: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT * FROM users WHERE phone_number = :phone_number"), {'phone_number': phone_number})
    user = result.fetchone()
    if user:
        return dict(user._mapping)
    return {"message": "User not found"}

@router.post("/users/")
async def create_user(req: req, db: AsyncSession = Depends(get_db)):
    user = User(name=req.name, email=req.email, phone_number=req.phone_number)
    db.add(user)
    await db.commit()
    return {"message": "User created!", "user_id": user.id}