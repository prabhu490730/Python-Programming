#Drop a Collection
from pymongo import MongoClient
import random
client = MongoClient()                ## Connecting to client
db = client.test                      ## Connect to db

db.coll1.insert_one({"name":"mongodb"}) #Collection1
db.coll2.insert_one({"name":"mongodb"}) #Collection2

print(db.list_collection_names())

#Drop a Collection
db.coll1.drop()
print(db.list_collection_names())

db.coll2.drop()
print(db.list_collection_names())

#%%
