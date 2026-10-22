
"""Rebuild the students collection from data/students.json."""

from pathlib import Path
from bson import json_util
from db import students

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "students.json"


def seed():
    docs = json_util.loads(DATA.read_text(encoding="utf-8"))

    # Make sure every student's year is stored as a number
    for doc in docs:
        doc["year"] = int(doc["year"])

    students.drop()
    students.insert_many(docs)
    students.create_index("student_id", unique=True)

    print(f"Seeded {len(docs)} students")


if __name__ == "__main__":
    seed()
