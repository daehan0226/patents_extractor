from bson import ObjectId
import asyncio
from pymongo.common import validate

from src.modules.database import Database, AsyncDatabase


database = Database().get_db()
async_database = AsyncDatabase().get_async_db()

class BaseDocument:
    meta = {}

    @classmethod
    def validate_schema(cls, params):
        schema = cls.meta.get("schema")
        for k , v in params.items():
            if not isinstance(v,schema[k]):
                raise Exception(f"Schema Validation Error, check {k}")
        return params

    @classmethod
    def get_collection(cls):
        if collection_name := cls.meta.get("collection"):        
            return database[collection_name]
        raise Exception("No collection name provided")
        
    
    @classmethod
    def get_async_db_collection(cls):
        if collection_name := cls.meta.get("collection"):
            return async_database[collection_name]
        raise Exception("No collection name provided")
        

    @classmethod
    def create(cls, **kwargs):
        doc = cls.validate_schema(kwargs)
        result = cls.get_collection().insert_one(doc)
        return cls.get(id=result.inserted_id)
        
    @classmethod
    def get(cls, **kwargs):
        if "id" in kwargs:
            kwargs["_id"] = (
                ObjectId(kwargs.pop("id")) if type(kwargs["id"]) is str else kwargs.pop("id")
            )
        result = cls.get_collection().find_one(kwargs)
        return result
    
    
    @classmethod
    def get_all(cls):
        result = cls.get_collection().find({})
        return result


    @classmethod
    def get_all(cls):
        result = cls.get_collection().find({})
        for doc in result:
            print(doc)
        return result

        
    @classmethod
    async def _async_insert_one(cls, patent):
        result = await cls.get_async_db_collection().insert_one(patent)
        return result
        

    @classmethod
    async def insert_patents(cls, patents):
        future_list = []
        for patent in patents:
            future = asyncio.ensure_future(cls._async_insert_one(patent))
            future_list.append(future)
        await asyncio.gather(*future_list, return_exceptions=True)

    @classmethod
    def update(cls, id, **kwargs):
        doc = cls.get(id=id)
        updated_doc = doc.update(kwargs)
        result = cls.get_collection().update_one({"_id": ObjectId(id)}, {"$set": updated_doc})
        return cls.get(id=id) if result.acknowledged else None
        
    @classmethod
    def delete(cls, id):
        cls.get_collection().delete_one({"_id": id})

    @classmethod
    def delete_all(cls):
        cls.get_collection().delete_many({})