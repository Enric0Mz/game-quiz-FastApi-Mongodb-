from fastapi import Path
from bson.errors import InvalidId
from bson import ObjectId



def validate_object_id(id: str = Path(...)) -> str:
    try:
        ObjectId(id)
    except InvalidId:
        raise "Invalid id format" #TODO add custom exc
    return id
