import pymongo
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.pmhbw.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
docs = db.students.find({})
#New student record
jade = {
    "first_name": "Jade",
    "last_name": "Cat",
    "student_id": "1010"
}
jade_student_id = db.insert_one(jade).inserted_id
print("Adding new student")
print(jade_student_id)

print("Find the new record")
doc = db.students.find_one({"student_id": "1010"})
print(doc)
print("Delete the record")
db.students.delete_one({"student_id": "1010"})
print("Search for the deleted record")
doc = db.students.find_one({"student_id": "1010"})
print(doc)