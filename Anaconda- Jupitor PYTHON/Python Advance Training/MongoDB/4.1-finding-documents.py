#Finding the documents from the collection

from pymongo import MongoClient

client=MongoClient()

db=client.mydb #select db

docs=db.mycollection.find() # select documents in mycollection

for doc in docs: # print documents
    print (doc)


#%%
