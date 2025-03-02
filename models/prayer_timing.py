from sqlalchemy import Column, Integer, Time, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.init_db import Base

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