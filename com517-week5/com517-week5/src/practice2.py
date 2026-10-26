from db import students 

result = students.update_many(
    {"societies": "Chess"},
    {"$pull": {"societies": "Chess"}}
)

print("Matched:", result.matched_count)
print("Modified:", result.modified_count)