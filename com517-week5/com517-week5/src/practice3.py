from db import students

result = students.update_many(
    {"year": 1},
    {"$inc": {"year": 1}}
)

print("Matched:", result.matched_count)
print("Modified:", result.modified_count)