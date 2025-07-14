from sqlalchemy import Column, Integer, String, ForeignKey,DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)

    legends = relationship("Legend", back_populates="category")


class Province(Base):
    __tablename__ = "province"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)

    cantons = relationship("Canton", back_populates="province")


class Canton(Base):
    __tablename__ = "canton"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    province_id = Column(Integer, ForeignKey("province.id"), nullable=False)

    province = relationship("Province", back_populates="cantons")
    districts = relationship("District", back_populates="canton")

class District(Base):
    __tablename__ = "district"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    canton_id = Column(Integer, ForeignKey("canton.id"), nullable=False)

    canton = relationship("Canton", back_populates="districts")
    legends = relationship("Legend", back_populates="district")

class Legend(Base):
    __tablename__ = "legend"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    image_url = Column(String(1000), nullable=True)
    description = Column(String(1000), nullable=False)
    category_id = Column(Integer, ForeignKey("category.id"), nullable=False)
    district_id = Column(Integer, ForeignKey("district.id"), nullable=False)

    category = relationship("Category", back_populates="legends")
    district = relationship("District", back_populates="legends")
    created_at = Column(DateTime, default=datetime.now)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
