from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base 

# Base obj act as a python Inheritance. we create the model classes using Base obj properties.  
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
    itemType = relationship("ItemType", back_populates="main_item")


class ItemType(Base):
    __tablename__ = "item_type"

    id = Column(Integer, primary_key=True, index=True)
    itemType = Column(String, index=True)
    description = Column(String, index=True)
    item_id = Column(Integer, ForeignKey("items.id"))

    main_item = relationship("Item", back_populates="itemType")