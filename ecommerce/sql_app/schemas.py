from pydantic import BaseModel


# ---------Item Type Model Schemas-----------
class ItemTypeBase(BaseModel):
    itemType: str
    description: str
    # item_id: int


class ItemTypeCreate(ItemTypeBase):
    pass


class ItemType(ItemTypeBase):
    id: int
    item_id: int

    class Config:
        from_attributes = True


# -----------Item Model Schemas--------
class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int
    itemType: list[ItemType] = []

    class Config:
        """'orm_mode' has been renamed to 'from_attributes'"""

        from_attributes = True


# ---------User Model Schemas---------
class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        # Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict,
        # but an ORM model (or any other arbitrary object with attributes).

        # Without orm_mode, if you returned a SQLAlchemy model from your path operation,
        # it wouldn't include the relationship data.

        from_attributes = True
