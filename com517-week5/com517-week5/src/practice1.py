from db import students

result = students.update_one(
    {"name.last": "Kerr"},
    {"$addToSet": {"societies": "Film"}}
)

print("Matched:", result.matched_count)
print("Modified:", result.modified_count)