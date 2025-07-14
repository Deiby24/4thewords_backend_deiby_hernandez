from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas
from app.auth import get_current_user
from app.models import User

router = APIRouter()

@router.get("/provinces", response_model=list[schemas.Province])
def list_provinces(db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return crud.get_provinces(db)

@router.post("/provinces", response_model=schemas.Province)
def create_province(
    province: str = Form(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud.create_province(db, province)

@router.get("/cantons/{province_id}", response_model=list[schemas.Canton])
def list_cantons_by_province(province_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud.get_cantons_by_province(db, province_id)

@router.post("/cantons", response_model=schemas.Canton)
def create_canton(
    canton: str = Form(...), 
    province_id: int = Form(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud.create_canton(db, canton, province_id)


@router.get("/districts/{canton_id}", response_model=list[schemas.District])
def list_districts_by_canton(canton_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud.get_districts_by_canton(db, canton_id)