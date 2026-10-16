
from queries import (
    on_module,
    mark_at_least,
    in_all_societies,
    page_of_students,
    missing_field
)


def show(label, cursor):
    names = [student["name"]["last"] for student in cursor]
    print(label, names)


show("on_module COM521:", on_module("COM521"))

show("mark_at_least COM517 80:", mark_at_least("COM517", 80))

show(
    "in_all_societies:",
    in_all_societies(["Chess", "Computing Society"])
)

show("page_of_students 2:", page_of_students(2))

show("missing_field societies:", missing_field("societies"))

print("\nTASK 8 FINISHED")
