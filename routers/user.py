from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db.init_db import SessionLocal
from models.user import User

router = APIRouter()

@router.get("/users/phone/{phone_number}")
async def get_user_by_phone(phone_number: str, db: AsyncSession = Depends(SessionLocal)):
    result = await db.execute(f"SELECT * FROM users WHERE phone_number = '{phone_number}'")
    return result.fetchone()

@router.post("/users/")
async def create_user(name: str, email: str, phone_number: str, db: AsyncSession = Depends(SessionLocal)):
    user = User(name=name, email=email, phone_number=phone_number)
    db.add(user)
    await db.commit()
    return {"message": "User created!", "user_id": user.id}