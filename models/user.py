from sqlalchemy import Column, Integer, String, TIMESTAMP, text
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True,nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    phone_number = Column(String, nullable=False, unique=True, index=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))