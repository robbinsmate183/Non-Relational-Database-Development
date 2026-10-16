
from db import students


# ==========================================
# WEEK 2 - ORIGINAL QUERIES
# ==========================================

def week2_queries():
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


# ==========================================
# WEEK 3 - TASK 8
# ==========================================

# Find students taking a particular module
def on_module(code):
    return students.find(
        {"modules": code}
    ).sort("name.last", 1)


# Find students with a minimum mark in a module
def mark_at_least(module, minimum):
    return students.find({
        "grades": {
            "$elemMatch": {
                "module": module,
                "mark": {"$gte": minimum}
            }
        }
    }).sort("name.last", 1)


# Find students belonging to all specified societies
def in_all_societies(societies):
    return students.find({
        "societies": {"$all": societies}
    }).sort("name.last", 1)


# Return a page of students sorted by surname
def page_of_students(page, size=4):
    return students.find().sort(
        "name.last", 1
    ).skip(
        (page - 1) * size
    ).limit(size)


# Find students where a specified field is missing
def missing_field(field):
    return students.find({
        field: {"$exists": False}
    }).sort("name.last", 1)


# Only run the original Week 2 examples directly
if __name__ == "__main__":
    week2_queries()
