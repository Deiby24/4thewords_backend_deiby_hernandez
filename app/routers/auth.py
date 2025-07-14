from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta


from app.database import get_db
from app.models import User
from app.auth import (
    authenticate_user,
    create_access_token,
    get_password_hash,
    get_current_user,
    SECRET_KEY,
    ALGORITHM,
    verify_password,
    ACCESS_TOKEN_EXPIRE_MINUTES
)

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register")
def register_user(email: str, password: str, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        raise HTTPException(
            status_code=400, 
            detail="Usuario ya existe"
        )
    
    hashed_password = get_password_hash(password)
    user = User(email=email, password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"msg": "Usuario creado exitosamente"}

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    user = db.query(User).filter(User.email == form_data.username).first()
    

    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.email},
        expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me")
def get_current_user_info(current_user: User = Depends(get_current_user)):
    return {"email": current_user.email, "id": current_user.id}