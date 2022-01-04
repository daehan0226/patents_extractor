from pymongo import MongoClient

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