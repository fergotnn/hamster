from fastapi import APIRouter
from models.data_model import Data
from schemas.data_schema import data_serializer
from bson import ObjectId
from config.db import collection

router = APIRouter()


@router.post("/push")
async def push(data: Data):
    result = collection.insert_one(dict(data))
    return {"status": "Ok", "id": str(result.inserted_id)}


@router.get("/pull/{id}")
async def pull(id: str):
    document = collection.find_one({"_id": ObjectId(id)})
    json_data = data_serializer(document)
    return {"status": "Ok", "data": json_data}

