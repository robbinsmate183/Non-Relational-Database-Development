
from datetime import datetime
import math
from db import students


def surnames(label, cursor):
    """Print the label, number of results and student surnames."""
    names = [s["name"]["last"] for s in cursor]
    print(label, len(names), names)


# ==========================================
# TASK 1 - BASIC QUERIES
# ==========================================

surnames(
    "YEAR 1",
    students.find({"year": 1}).sort("name.last", 1)
)


# ==========================================
# TASK 2 - PROJECTIONS
# ==========================================

print("\nTASK 2 - YEAR 3 STUDENTS")

for s in students.find(
    {"year": 3},
    {"name": 1, "email": 1, "_id": 0}
):
    print(s)


# P1 - Aoife Byrne without grades, address or _id
print("\nP1 - AOIFE BYRNE")

for s in students.find(
    {"student_id": "B00912345"},
    {"grades": 0, "address": 0, "_id": 0}
):
    print(s)


# P2 - First names and cities of Belfast students
print("\nP2 - BELFAST STUDENTS")

for s in students.find(
    {"address.city": "Belfast"},
    {"name.first": 1, "address.city": 1, "_id": 0}
):
    print(s)


# P3 - Surname and first grade
print("\nP3 - FIRST GRADE")

for s in students.find(
    {},
    {"name.last": 1, "grades": {"$slice": 1}, "_id": 0}
):
    print(s)


# ==========================================
# TASK 3 - EMBEDDED DOCUMENTS
# ==========================================

surnames(
    "LISBURN",
    students.find({"address.city": "Lisburn"}).sort("name.last", 1)
)

# E1 - Placement in Belfast
surnames(
    "E1 - BELFAST PLACEMENT",
    students.find({"placement.city": "Belfast"}).sort("name.last", 1)
)

# E2 - Students living in Newry
surnames(
    "E2 - NEWRY",
    students.find({"address.city": "Newry"}).sort("name.last", 1)
)

# E3 - Exact embedded document in original order
surnames(
    "E3 - ORIGINAL ORDER",
    students.find({
        "address": {
            "city": "Lisburn",
            "postcode": "BT28 1AA"
        }
    }).sort("name.last", 1)
)

# E3 - Same document with reversed field order
surnames(
    "E3 - REVERSED ORDER",
    students.find({
        "address": {
            "postcode": "BT28 1AA",
            "city": "Lisburn"
        }
    }).sort("name.last", 1)
)


# ==========================================
# TASK 4 - ARRAYS
# ==========================================

# Worked example - Chess society
surnames(
    "CHESS",
    students.find({"societies": "Chess"}).sort("name.last", 1)
)

# A1 - Taking both COM517 and COM521
surnames(
    "A1 - BOTH MODULES",
    students.find({
        "modules": {"$all": ["COM517", "COM521"]}
    }).sort("name.last", 1)
)

# A2 - Taking COM520 or COM521
surnames(
    "A2 - EITHER MODULE",
    students.find({
        "modules": {"$in": ["COM520", "COM521"]}
    }).sort("name.last", 1)
)

# A3 - Not taking COM517
surnames(
    "A3 - NOT COM517",
    students.find({
        "modules": {"$nin": ["COM517"]}
    }).sort("name.last", 1)
)

# A4 - Exactly two societies
surnames(
    "A4 - TWO SOCIETIES",
    students.find({
        "societies": {"$size": 2}
    }).sort("name.last", 1)
)

# A5 - Empty societies array
surnames(
    "A5 - EMPTY SOCIETIES",
    students.find({
        "societies": []
    }).sort("name.last", 1)
)

# A6 - Exact array comparison
surnames(
    "A6 - ORIGINAL ORDER",
    students.find({
        "modules": ["COM517", "COM519"]
    }).sort("name.last", 1)
)

surnames(
    "A6 - REVERSED ORDER",
    students.find({
        "modules": ["COM519", "COM517"]
    }).sort("name.last", 1)
)


# ==========================================
# TASK 5 - GRADES AND ELEMMATCH
# ==========================================

# Worked example - Failed at least one module
surnames(
    "FAILED",
    students.find({
        "grades.mark": {"$lt": 50}
    }).sort("name.last", 1)
)

# D1 - Without elemMatch
surnames(
    "D1 - WITHOUT ELEMMATCH",
    students.find({
        "grades.module": "COM517",
        "grades.mark": {"$gte": 70}
    }).sort("name.last", 1)
)

# D1 - With elemMatch
surnames(
    "D1 - WITH ELEMMATCH",
    students.find({
        "grades": {
            "$elemMatch": {
                "module": "COM517",
                "mark": {"$gte": 70}
            }
        }
    }).sort("name.last", 1)
)

# D2 - Marks in the 50s without elemMatch
surnames(
    "D2 - WITHOUT ELEMMATCH",
    students.find({
        "grades.mark": {"$gte": 50, "$lt": 60}
    }).sort("name.last", 1)
)

# D2 - Marks in the 50s with elemMatch
surnames(
    "D2 - WITH ELEMMATCH",
    students.find({
        "grades": {
            "$elemMatch": {
                "mark": {"$gte": 50, "$lt": 60}
            }
        }
    }).sort("name.last", 1)
)

# D3 - Show surname and COM517 grade only
print("\nD3 - COM517 GRADES")

for s in students.find(
    {"grades.module": "COM517"},
    {
        "name.last": 1,
        "grades": {
            "$elemMatch": {"module": "COM517"}
        },
        "_id": 0
    }
).sort("name.last", 1):
    print(s)


# ==========================================
# TASK 6 - MISSING FIELDS AND TYPES
# ==========================================

# Worked example - Placement field exists
surnames(
    "HAS PLACEMENT FIELD",
    students.find({
        "placement": {"$exists": True}
    }).sort("name.last", 1)
)

# F1 - Placement is null or missing
surnames(
    "F1 - NULL OR MISSING PLACEMENT",
    students.find({
        "placement": None
    }).sort("name.last", 1)
)

# F2 - Real placements only
surnames(
    "F2 - REAL PLACEMENTS",
    students.find({
        "placement": {"$ne": None}
    }).sort("name.last", 1)
)

# F3 - Missing societies field
surnames(
    "F3 - MISSING SOCIETIES",
    students.find({
        "societies": {"$exists": False}
    }).sort("name.last", 1)
)

# F4 - Year stored as a string
surnames(
    "F4 - YEAR IS STRING",
    students.find({
        "year": {"$type": "string"}
    }).sort("name.last", 1)
)

print("\nYEAR 2 COUNT")
print("YEAR 2", students.count_documents({"year": 2}))

# Kasia Nowak's year was already fixed using fix_year.py.
# F4 should now return zero students.


# ==========================================
# TASK 7 - SORTING AND PAGINATION
# ==========================================

# Worked example - Page 2, four students per page
page, size = 2, 4

surnames(
    "PAGE 2",
    students.find()
    .sort("name.last", 1)
    .skip((page - 1) * size)
    .limit(size)
)

# R1 - Page 3, four students per page
page, size = 3, 4

surnames(
    "R1 - PAGE 3",
    students.find()
    .sort("name.last", 1)
    .skip((page - 1) * size)
    .limit(size)
)

# R2 - COM517 mark >= 70 OR Year 1
surnames(
    "R2 - COM517 HIGH MARK OR YEAR 1",
    students.find({
        "$or": [
            {
                "grades": {
                    "$elemMatch": {
                        "module": "COM517",
                        "mark": {"$gte": 70}
                    }
                }
            },
            {"year": 1}
        ]
    }).sort("name.last", 1)
)

# R3 - Enrolled in 2025 OR Year 1
surnames(
    "R3 - ENROLLED 2025 OR YEAR 1",
    students.find({
        "$or": [
            {
                "enrolled": {
                    "$gte": datetime(2025, 1, 1),
                    "$lt": datetime(2026, 1, 1)
                }
            },
            {"year": 1}
        ]
    }).sort("name.last", 1)
)

# R4 - First five sorted by course and surname
surnames(
    "R4 - FIRST FIVE BY COURSE AND SURNAME",
    students.find()
    .sort([("course", 1), ("name.last", 1)])
    .limit(5)
)

# R5 - Number of pages for five students per page
size = 5
total_students = students.count_documents({})
total_pages = math.ceil(total_students / size)

print("\nR5 - PAGINATION")
print("Total students:", total_students)
print("Page size:", size)
print("Total pages:", total_pages)


print("\n==========================================")
print("WEEK 3 TASKS 1-7 FINISHED")
print("==========================================")
