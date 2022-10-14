from fastapi import APIRouter, Depends, HTTPException

from models.category import *
from sql_app import crud, models
from sqlalchemy.orm import Session
from sql_app.database import get_db

router = APIRouter()


@router.get("/categories")
def get_categories(search: str = "", sort: str = ""):
    categories = {"searching": search, "sorting": sort}
    return categories


@router.post("/categories", response_model=Category)
def create_categories(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = crud.get_category_name(db, name=category.name)
    if not db_category:
        row = models.User(**category.dict())
        return crud.create(row, db)
    raise HTTPException(status_code=400, detail="Category already registered")
