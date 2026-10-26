from db import students 

result = students.update_many(
    {"year": {"$in": [1, 3]}},
    {"$inc": {"year": 1}}
)

print("Matched:", result.matched_count)
print("Modified:", result.modified_count)