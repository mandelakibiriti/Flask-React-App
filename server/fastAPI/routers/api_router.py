from fastapi import APIRouter, Depends
from ..database import conn_db
from sqlalchemy.orm import Session
from .. import schemas
from . import db_router

# Router = Flask Blueprint
router = APIRouter()

# Data created from Flask
@router.get('/')
@router.get('/data')
async def get_user():
    user_data = conn_db.execute("SELECT * FROM user;").fetchall()
    return {
        'userData': user_data
    }

# Data posted to MySQL from FastAPI
@router.post("/post_items/", response_model=schemas.Item)
def create_item(
    item: schemas.ItemCreate, db: Session = Depends(db_router.get_db)
    ):
    return db_router.create_item(db=db, item=item)

# Get Data from MySQL from FastAPI
@router.get("/get_items", response_model=list[schemas.Item])
def read_item(
    skip: int = 0, limit: int = 100, db: Session = Depends(db_router.get_db)
    ):
    items = db_router.get_items(db, skip=skip, limit=limit)
    return items