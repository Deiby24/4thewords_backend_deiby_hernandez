from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form
from sqlalchemy.orm import Session, joinedload
from datetime import datetime
from uuid import uuid4
import os

from app.database import get_db
from app.models import Legend, User
from app import crud, schemas, models
from app.auth import get_current_user
from app.schemas import LegendResponse

router = APIRouter()

@router.get("/legends", response_model=list[schemas.LegendRead])
def list_legends(db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return crud.get_legends_with_names(db)

@router.get("/legends/{legend_id}", response_model=LegendResponse)
def get_legend(legend_id: int, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    legend = db.query(Legend).filter(Legend.id == legend_id).first()
    if not legend:
        raise HTTPException(status_code=404, detail="Legend not found")

    return LegendResponse(
        id=legend.id,
        title=legend.title,
        description=legend.description,
        category_name=legend.category.name,
        district_name=legend.district.name,
        canton_name=legend.district.canton.name,
        province_name=legend.district.canton.province.name,
        image_url=legend.image_url,
        created_at=legend.created_at
    )

@router.post("/createLegends", response_model=schemas.LegendResponse)
async def create_legend_with_image(
    title: str = Form(...),
    description: str = Form(...),
    category_id: int = Form(...),
    district_id: int = Form(...),
    image: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    
    extension = image.filename.split(".")[-1].lower()
    if extension not in ["jpg", "jpeg", "png", "webp"]:
        raise HTTPException(
            status_code=400, 
            detail="Formato de imagen no permitido"
        )

    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    images_dir = os.path.join(BASE_DIR, "static", "images")
    os.makedirs(images_dir, exist_ok=True)
    
    
    filename = f"{uuid4().hex}.{extension}"
    image_path = os.path.join(images_dir, filename)


    with open(image_path, "wb") as buffer:
        buffer.write(await image.read())


    legend = models.Legend(
        title=title,
        description=description,
        category_id=category_id,
        district_id=district_id,
        image_url=f"/static/images/{filename}",
        created_at=datetime.now()
    )
    db.add(legend)
    db.commit()
    
   
    legend = (
        db.query(models.Legend)
        .options(
            joinedload(models.Legend.category),
            joinedload(models.Legend.district).joinedload(models.District.canton).joinedload(models.Canton.province)
        )
        .filter(models.Legend.id == legend.id)
        .first()
    )

    response = schemas.LegendResponse(
        id=legend.id,
        title=legend.title,
        description=legend.description,
        image_url=legend.image_url,
        created_at=legend.created_at,
        category_name=legend.category.name,
        district_name=legend.district.name,
        canton_name=legend.district.canton.name,
        province_name=legend.district.canton.province.name,
    )

    return response

@router.put("/legends/{legend_id}", response_model=schemas.LegendUpdate)
def update_legend(
    legend_id: int, 
    legend: schemas.LegendUpdate, 
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    legend.created_at = datetime.now()
    updated = crud.update_legend(db, legend_id, legend)
    if not updated:
        raise HTTPException(status_code=404, detail="Leyenda no encontrada")
    return updated

@router.delete("/legends/{legend_id}")
def delete_legend(
    legend_id: int, 
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    deleted = crud.delete_legend(db, legend_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Leyenda no encontrada")
    return {"message": "Leyenda eliminada correctamente"}