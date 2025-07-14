# app/crud.py

from sqlalchemy.orm import Session,joinedload
from app import models, schemas
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from .auth import SECRET_KEY, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_legends_with_names(db: Session):
    legends = db.query(models.Legend).options(
        joinedload(models.Legend.category),
        joinedload(models.Legend.district).joinedload(models.District.canton).joinedload(models.Canton.province)
    ).all()

    result = []
    for legend in legends:
        result.append({
            "id": legend.id,
            "title": legend.title,
            "description": legend.description,
            "category_id": legend.category_id,
            "category_name": legend.category.name if legend.category else None,
            "district_id": legend.district_id,
            "district_name": legend.district.name if legend.district else None,
            "canton_name": legend.district.canton.name if legend.district and legend.district.canton else None,
            "canton_id": legend.district.canton.id if legend.district and legend.district.canton else None,
            "province_id": legend.district.canton.province.id if legend.district and legend.district.canton and legend.district.canton.province else None,
            "province_name": legend.district.canton.province.name if legend.district and legend.district.canton and legend.district.canton.province else None,
            "image_url": legend.image_url,
            "created_at": legend.created_at
        })
    return result

def get_legend(db: Session, legend_id: int):
    return db.query(models.Legend).filter(models.Legend.id == legend_id).first()

def update_legend(db: Session, legend_id: int, data: schemas.LegendUpdate):
    legend = get_legend(db, legend_id)
    if not legend:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(legend, key, value)
    db.commit()
    db.refresh(legend)
    return legend


def delete_legend(db: Session, legend_id: int):
    legend = get_legend(db, legend_id)
    if legend:
        db.delete(legend)
        db.commit()
        return True
    return False


def get_categories(db: Session):
    return db.query(models.Category).all()

def create_category(db: Session, category : str):
    db_category = models.Category(name=category)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_provinces(db: Session):
    return db.query(models.Province).all()

def create_province(db: Session, province: str):
    db_province = models.Province(name=province)
    db.add(db_province)
    db.commit()
    db.refresh(db_province)
    return db_province


def get_cantons_by_province(db: Session, province_id: int):
    return db.query(models.Canton).filter(models.Canton.province_id == province_id).all()

def create_canton(db: Session, canton: str, province_id: int):
    db_canton = models.Canton(name=canton, province_id=province_id)
    db.add(db_canton)
    db.commit()
    db.refresh(db_canton)
    return db_canton

def get_districts_by_canton(db: Session, canton_id: int):
    return db.query(models.District).filter(models.District.canton_id == canton_id).all()


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_email = payload.get("sub")
        if user_email is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        return user_email
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")


