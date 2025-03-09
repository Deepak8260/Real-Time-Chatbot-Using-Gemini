import pymongo
from pymongo import MongoClient
import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get MongoDB credentials from .env
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

client=MongoClient(MONGO_URI)
db=client[DB_NAME]
collection = db[COLLECTION_NAME]

def insert_data(user_input,response):
    chat = {
        "user_input" : user_input,
        "response" : response,
        "timestamp": datetime.datetime.now()
    }
    collection.insert_one(chat)