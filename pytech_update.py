from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.pmhbw.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

docs = db.students.find({})

doc = db.students.find_one({"student_id": "1007"})
print(doc)

db.students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Smith"}})
doc = db.students.find_one({"student_id": "1007"})
print(doc)