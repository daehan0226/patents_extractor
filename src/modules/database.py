from pymongo import MongoClient
from motor import motor_asyncio
from config.config import config

def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper
  
@singleton
class Database:
    db = None
    client = None
    
    def __init__(self):
        self.client = MongoClient(config["mongodb_url"])
        self.db = self.client["patent_test"]
      
    def get_db(self):
        return self.db
  

@singleton
class AsyncDatabase:
    async_db = None
    async_client = None
  
    def __init__(self):
        self.async_client = motor_asyncio.AsyncIOMotorClient(config["mongodb_url"])
        self.async_db = self.async_client['patent_test']
      
    def get_async_db(self):
      return self.async_db