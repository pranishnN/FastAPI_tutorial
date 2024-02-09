from fastapi import APIRouter, HTTPException, Response
from bson import ObjectId

# project paths
from schema.schema import *
from models.test import TestModel, AddressModel
from config.db import collection_name, address_collection

router = APIRouter()

@router.get("/")
async def get_data_view():
    data = get_all_data(collection_name.find())
    return data


@router.get("/get_data_by_name/{name}")
async def get_data_by_name(name:str):
    print("======================", name)
    data = collection_name.find_one({name:name})
    print(dict(data), ")))))))))))))))))))))))))))")
    # return get_data(data, is_id=False)
    return data


@router.post("/", status_code=201)
async def post_data_view(data: TestModel):
    data = collection_name.insert_one(dict(data))
    print(data, "SAVING DATA")
    # return Response("Saved successfully", status_code=200)


@router.put("/{id}")
async def update_data_view(id:str, data: TestModel):
    collection_name.find_one_and_update({"_id":ObjectId(id)}, {"$set": dict(data)})


@router.delete("/{id}")
async def delete_data_view(id:str):
    collection_name.find_one_and_delete({"_id":ObjectId(id)})
    return "Delete successfully"


@router.get("/address")
async def get_all_address_view():
    data = get_all_address(address_collection.find())
    return data

@router.post("/address", status_code=201)
async def post_address_view(address: AddressModel):
    data = address_collection.insert_one(dict(address))
    print(data, "SAVING DATA")
