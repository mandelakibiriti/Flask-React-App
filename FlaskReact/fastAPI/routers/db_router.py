from fastapi import APIRouter
from sqlalchemy.orm import Session
from ..database import SessionLocal,engine
from .. import models, schemas

# Router = Flask Blueprint
router = APIRouter()

# Creates Db
models.Base.metadata.create_all(bind=engine)

# DB Dependancy
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Post and Get functions
def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()
