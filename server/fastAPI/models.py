from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String
from .database import Base

# Create models accessible to FastAPI
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    description = Column(String(255), index=True)