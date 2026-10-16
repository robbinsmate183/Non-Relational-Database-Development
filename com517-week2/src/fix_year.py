from db import students

result = students.update_one(
    {"name.last": "Nowak"},
    {"$set": {"year": 2}}
)

print("Matched:", result.matched_count)
print("Modified:", result.modified_count)