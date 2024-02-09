from fastapi import Depends, FastAPI, HTTPException, Request
import uvicorn

# Python
from typing import (Optional)

# SQLAlchemy
from sqlalchemy.orm import Session

from . import views, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db # also called as dependency
    finally:
        db.close()


@app.post('/users/', response_model=schemas.User) # path operations
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = views.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail='Email already exists')
    return views.create_user(db=db, user=user)
    

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = views.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User) 
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = views.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    item_name =  item.title
    item_value = views.get_a_user_item(db, item_name, user_id)
    if item_value is not {}:
        raise HTTPException(status_code=404, detail="Item already exists against this user")
    return views.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = views.get_items(db, skip=skip, limit=limit)
    return items


# """Alembic Note"""
# Normally you would probably initialize your database (create tables, etc) with Alembic.
# And you would also use Alembic for "migrations" (that's its main job).

@app.post("/item/{item_id}/itemtype/", response_model=schemas.ItemType)
def create_item_item_type(item_id: int, itemType: schemas.ItemTypeCreate, db: Session = Depends(get_db)):
    # itemType_name = itemType.itemType
    return views.create_item_item_type(db=db, itemType=itemType, item_id=item_id)


@app.get("/itemtypeuser/")
def get_user_of_item_type(request: Request, item_type: Optional[int] = None, db: Session = Depends(get_db)):
    # param = request.query_params
    session = Session()
    query = views.get_user_of_item_type_view(item_type_id=item_type, db=db)
    # user_data = session.execute(query).first()
    print('===user_data=====', type(query), dir(query))
    return {'email':query.__dict__.pop('email')}

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)