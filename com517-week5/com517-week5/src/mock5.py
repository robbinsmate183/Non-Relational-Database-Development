from db import students

for student in students.find({"year": 3}):
    print(student["name"])