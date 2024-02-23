from pymongo import MongoClient
from config import DATABASE_URI, DATABASE_NAME, COLLECTION_NAME

def load_data():
    client = MongoClient(DATABASE_URI)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
    data = collection.find({})
    return list(data)

