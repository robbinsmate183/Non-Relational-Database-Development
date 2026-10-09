from db import students

result = students.delete_one(
    {"student_id": "B00999999"}
)

print("Students deleted:", result.deleted_count)
print("Students remaining:", students.count_documents({}))