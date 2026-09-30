from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
students = client["com517"]["students"]

students.insert_one({"name": "Dara Quinn", "course": "BSc Data Science", "year": 1})
print("Added Dara")

dara = students.find_one({"name": "Dara Quinn"})
print("Found:", dara["name"], "in year", dara["year"])

students.update_one({"name": "Dara Quinn"}, {"$set": {"year": 2}})
print("Now in year", students.find_one({"name": "Dara Quinn"})["year"])

students.delete_one({"name": "Dara Quinn"})
print("Students left:", students.count_documents({}))