from db import students

for student in students.find(
    {"year": 3},
    {"name": 1, "email": 1, "_id": 0}
):
    print(student)