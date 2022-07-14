# Insert 1000 random documents

from pymongo import MongoClient
import random

client = MongoClient()                          ## Connecting to client

db = client.marks                      ## Connect to db

class5 = db.class5                                ## Collection

print("Total documents in 'emps' collection: ", class5.count_documents({}))
class5.delete_many({"maths":55})
print("Total documents in 'emps' collection: ", class5.count_documents({}))

#%%
