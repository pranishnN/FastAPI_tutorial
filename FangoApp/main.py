from fastapi import FastAPI
from router.router import router

import urllib.parse 

app = FastAPI()

app.include_router(router=router)

from pymongo.mongo_client import MongoClient


# FOR CHECKING MONGO DB CONNECTION:::


# # mongo_user = urllib.parse.quote_plus("pranish_h")
# # mongo_pwd = urllib.parse.quote_plus("test1234!")


# uri = f"mongodb+srv://pranis_h:test1234!@cluster0.8cynpkp.mongodb.net/?retryWrites=true&w=majority"

# # Create a new client and connect to the server
# client = MongoClient(uri)

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)