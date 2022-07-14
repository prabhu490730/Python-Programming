# Insert 1000 random documents

from pymongo import MongoClient
import random

client = MongoClient()                          ## Connecting to client

db = client.marks                      ## Connect to db

class5 = db.class5                                ## Collection

print("Total documents in 'emps' collection: ", class5.count_documents({}))

for i in range(1000):
    maths_marks = random.randint(25,100)
    science_marks = random.randint(25,100)
    social_marks = random.randint(25,100)

    doc = {"maths":maths_marks,
           "science":science_marks,
           "social":social_marks}

    class5.insert_one(doc)

print("Total documents in 'emps' collection: ", class5.count_documents({}))
#%%
