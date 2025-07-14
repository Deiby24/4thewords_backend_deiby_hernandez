from pydantic import BaseModel
from datetime import datetime,date
from typing import Optional

class UserCreate(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class Category(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class Province(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class Canton(BaseModel):
    id: int
    name: str
    province_id: int

    class Config:
        from_attributes = True


class District(BaseModel):
    id: int
    name: str
    canton_id: int

    class Config:
        from_attributes = True

class LegendBase(BaseModel):
    title: str
    image_url: str  
    description: str
    date: date
    category_id: int
    province_id: int
    canton_id: int
    district_id: int


class LegendCreate(LegendBase):
    pass


class LegendRead(BaseModel):
    id: int
    title: str
    image_url: Optional[str]
    description: str
    created_at: datetime
    category_id: int
    category_name: Optional[str]
    district_id: int
    district_name: Optional[str]
    canton_name: Optional[str]
    province_name: Optional[str]
    province_id: Optional[int]= None
    canton_id: Optional[int] = None

    class Config:
        from_attributes = True

class LegendUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    category_id: Optional[int]
    province_id: Optional[int]
    canton_id: Optional[int]
    district_id: Optional[int]
    created_at: Optional[datetime] = None

class LegendResponse(BaseModel):
    id: int
    title: str
    description: str
    image_url: str
    created_at: datetime
    category_name: str
    district_name: str
    canton_name: str
    province_name: str

    class Config:
        orm_mode = True


class LegendMini(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        from_attributes = True
