from bson import ObjectId

from src.modules.database import Database


database = Database().get_db()

class BaseDocument:
    meta = {}
    
    @classmethod
    def get_collection(cls):
        collection_name = cls.meta.get("collection", None)
        if collection_name is None:
            raise Exception("No collection name provided")
        
        return database[collection_name]
    
    @classmethod
    def create(cls, doc, **kwargs):
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
    def update(cls, id, **kwargs):
        doc = cls.get(id=id)
        updated_doc = doc.update(kwargs)
        result = cls.get_collection().update_one({"_id": ObjectId(id)}, {"$set": updated_doc})
        return cls.get(id=id) if result.acknowledged else None
        
    @classmethod
    def delete(cls, id):
        cls.get_collection().delete_one({"_id": id})