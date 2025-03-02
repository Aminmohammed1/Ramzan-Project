from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geometry
from sqlalchemy.orm import relationship
from db.init_db import Base

class Mosque(Base):
    __tablename__ = "mosques"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(Geometry("POINT"), nullable=False)
    address = Column(String)
    prayer_timings = relationship("PrayerTiming", back_populates="mosque", cascade="all, delete-orphan")