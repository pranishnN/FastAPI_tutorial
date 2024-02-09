from pydantic import BaseModel

class TestModel(BaseModel):
    name : str
    description : str
    is_active : bool


class AddressModel(BaseModel):
    street : str
    city : str