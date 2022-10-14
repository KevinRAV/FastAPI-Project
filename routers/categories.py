from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Header

from models.category import *
from sql_app import crud, models
from sqlalchemy.orm import Session
from sql_app.database import get_db
from utils.auth import read_token

router = APIRouter()


@router.get("/categories")
def get_categories(name: str = "", id: int | None = None, db: Session = Depends(get_db)):
    query = []
    if len(name) > 0:
        query = query.append(["name", name])
    if id is not None:
        query = query.append(["id", id])
    return crud.read(models.Category, query, db)


@router.post("/categories", response_model=Category)
def create_categories(category: CategoryCreate,
                      auth_token: str = Header(min_length=1, max_length=50),
                      db: Session = Depends(get_db)
                      ):
    if not read_token(auth_token, db).is_admin:
        raise HTTPException(status_code=401, detail="Only admins can manage categories")
    db_category = crud.read(models.Category, [["name", category.name]], db)
    if not db_category:
        row = models.Category(**category.dict())
        return crud.create(row, db)
    raise HTTPException(status_code=400, detail="Category already registered")
