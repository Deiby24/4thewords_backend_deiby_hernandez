from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas, models
from app.auth import get_current_user
from app.models import User

router = APIRouter()

@router.get("/categories", response_model=list[schemas.Category])
def list_categories(
    db: Session = Depends(get_db),current_user: User = Depends(get_current_user)
    
):
    return crud.get_categories(db)

@router.post("/categoriesCreated", response_model=schemas.Category)
def create_category(
    category: str = Form(...),
    db: Session = Depends(get_db),current_user: User = Depends(get_current_user)
    
):
    return crud.create_category(db, category)