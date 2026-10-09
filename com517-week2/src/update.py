from db import students

result = students.update_one(
    {"student_id": "B00999999"},
    {"$set": {"year": 2}}
)

print("Students updated:", result.modified_count)

student = students.find_one(
    {"student_id": "B00999999"},
    {"_id": 0}
)
print("Updated student:", student)