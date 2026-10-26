from db import students 

result = students.count_documents(
    {"course": "BSc Data Science"}
)

deleted_count = students.delete_many(
    {"course": "BSc Data Science"}
)

print("Matched:", result)
print("Deleted:", deleted_count.deleted_count)