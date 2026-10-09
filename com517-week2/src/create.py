from db import students

new_student = {
    "student_id": "B00999999",
    "name": "Test Student",
    "year": 1,
    "course": "Computing"
}

result = students.insert_one(new_student)
print("Student created:", result.inserted_id)