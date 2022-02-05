import pymongo
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.pmhbw.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
docs = db.students.find({})

for doc in docs:
    print (doc)
print("Example of find one")
doc = db.students.find_one({"student_id": "1007"})
print(doc)