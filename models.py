from sqlalchemy import Column, Integer, String, Time, Date, ForeignKey, TIMESTAMP, text
from geoalchemy2 import Geometry
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.init_db import Base

class Mosque(Base):
    __tablename__ = "mosques"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(Geometry("POINT"), nullable=False)
    address = Column(String)
    prayer_timings = relationship("PrayerTiming", back_populates="mosque", cascade="all, delete-orphan")

class PrayerTiming(Base):
    __tablename__ = "prayer_timings"
    id = Column(Integer, primary_key=True, index=True)
    mosque_id = Column(Integer, ForeignKey("mosques.id"))
    fajr = Column(Time, nullable=False)
    dhuhr = Column(Time, nullable=False)
    asr = Column(Time, nullable=False)
    maghrib = Column(Time, nullable=False)
    isha = Column(Time, nullable=False)
    date = Column(Date, default=func.current_date)
    mosque = relationship("Mosque", back_populates="prayer_timings")

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True,nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    phone_number = Column(String, nullable=False, unique=True, index=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))