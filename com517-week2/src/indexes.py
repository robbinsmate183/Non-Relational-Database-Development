from pymongo.errors import DuplicateKeyError
from db import students

students.create_index("student_id", unique=True)

print("Indexes:", list(students.index_information()))

try:
    students.insert_one({"student_id": "B00912345"})
except DuplicateKeyError:
    print("Rejected: B00912345 is already taken")