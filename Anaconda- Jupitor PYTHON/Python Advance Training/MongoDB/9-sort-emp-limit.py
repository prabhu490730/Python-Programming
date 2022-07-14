# sorting and limiting

from pymongo import MongoClient
import datetime

client = MongoClient()                 ## Connecting to client

db = client.mydb                       ## Connect to db

emps = db.emps                         ## Collection

print("Total documents in 'emps' collection: ", emps.count_documents({}))

"""
emps.insert_one({"eid":223,"name":"ramesh"})
emps.insert_one({"eid":123,"name":"sagar"})
emps.insert_one({"eid":23,"name":"ranga"})
emps.insert_one({"eid":298,"name":"joydeep"})
emps.insert_one({"eid":333,"name":"ashok"})
emps.insert_one({"eid":423,"name":"gangadhar"})
"""

for emp in emps.find():
    print(emp)

print("Total documents in 'emps' collection: ", emps.count_documents({}))

for emp in emps.find().sort('eid'):
    print(emp)

print("limit")

for emp in emps.find().sort('eid').limit(4):
    print(emp)

print("skip")
for emp in emps.find().sort('eid').skip(2).limit(4):
    print(emp)


