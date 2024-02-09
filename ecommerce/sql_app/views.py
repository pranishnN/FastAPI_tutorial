from sqlalchemy.orm import Session
from . import models, schemas
from typing import Optional


def get_user(db: Session, user_id: int):
    # The parameter db is actually of type SessionLocal, but this class (created with sessionmaker()) \
    # is a "proxy" of a SQLAlchemy Session, so, the editor doesn't really know what methods are provided.

    # But by declaring the type as Session, the editor now can know the available methods (.add(), \
    # .query(), .commit(), etc) and can provide better support (like completion). The type declaration doesn't affect the actual object.
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password
    # The SQLAlchemy model for User contains a """hashed_password""" that should contain a secure hashed version of the password.
    # But as what the API client provides is the original password, you need to extract it and generate the hashed password in your application.
    # And then pass the """hashed_password""" argument with the value to save.
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)  # "add" that instance object to your database session.
    db.commit()  # "commit" the changes to the database (so that they are saved)., its because of autocommit=False declared in database session maker.
    db.refresh(
        db_user
    )  # "refresh" your instance (so that it contains any new data from the database, like the generated ID).
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def get_a_user_item(db: Session, item: str, owner_id: int):
    return db.query(models.Item).filter(models.Item.owner_id==owner_id, models.Item.title==item).first()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def create_item_item_type(db: Session, itemType: schemas.ItemTypeCreate, item_id: int):
    db_itemtype = models.ItemType(**itemType.dict(), item_id=item_id)
    db.add(db_itemtype)
    db.commit()
    db.refresh(db_itemtype)
    return db_itemtype

from sqlalchemy import select
def get_user_of_item_type_view(item_type_id: int, db: Optional[Session] = None):
    query = select(models.User)\
            .join(models.Item, models.User.id == models.Item.owner_id)\
            .join(models.ItemType, models.Item.id == models.ItemType.item_id)\
            .filter(models.ItemType.id == item_type_id)
    if db:
        result = db.execute(query)
        user = result.scalar()  # Assuming you expect a single User, adjust if needed
        return user

    return query