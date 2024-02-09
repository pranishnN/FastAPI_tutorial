from pymongo import MongoClient

# from motor.motor_asyncio import AsyncIOMotorClient
# client = AsyncIOMotorClient(f"mongodb+srv://pranis_h:test1234!@cluster0.8cynpkp.mongodb.net/?retryWrites=true&w=majority")


client = MongoClient(f"mongodb+srv://pranis_h:test1234!@cluster0.8cynpkp.mongodb.net/?retryWrites=true&w=majority")

db = client.test_db

collection_name = db["test_collection"]

address_collection = db["address_collection"]