#inserting a document in to collection
from pymongo import MongoClient

client=MongoClient() # create connection

db=client.mydb #create/select database

#inserting a doc in to collection mycollection

db.mycollection.insert_one({"Name":"Ram","Age":10,"Gender":"M"})

print("Successfully inserted record")


#%%
