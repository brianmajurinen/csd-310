from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.pmhbw.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech.students
fred = {
    "first_name": "Fred",
    "last_name": "Fake",
    "student_id": "1007"
}
brian = {
    "first_name": "Brian",
    "last_name": "Majurinen",
    "student_id": "1008"
}
kelsey = {
    "first_name": "Kelsey",
    "last_name": "Majurinen",
    "student_id": "1009"
}

fred_student_id = db.insert_one(fred).inserted_id
brian_student_id = db.insert_one(brian).inserted_id
kelsey_student_id = db.insert_one(kelsey).inserted_id

print(fred_student_id)
print(brian_student_id)
print(kelsey_student_id)
