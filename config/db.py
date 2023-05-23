from pymongo import MongoClient
import os

mongo_url = os.getenv('MONGO_URL', 'localhost')
mongo_port = os.getenv('MONGO_PORT', '27017')

db_connection = MongoClient(f"mongodb://{mongo_url}:{mongo_port}")
db = db_connection.mongo_base
collection = db["mongo_collection"]
