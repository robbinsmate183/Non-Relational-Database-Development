from db import students

# Find one student
print("One student:")
print(students.find_one({}, {"_id": 0}))

# Count all students
print("\nTotal students:")
print(students.count_documents({}))

# Find students in year 2 or above
print("\nStudents in year 2 or above:")
for student in students.find(
    {"year": {"$gte": 2}},
    {"_id": 0, "name": 1, "year": 1}
):
    print(student)

# Sort students by name
print("\nStudents sorted by name:")
for student in students.find(
    {},
    {"_id": 0, "name": 1}
).sort("name", 1).limit(5):
    print(student)