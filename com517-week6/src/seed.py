"""Rebuild the books and branches collections from the files in data/."""
from pathlib import Path

from bson import json_util

from db import books, branches

ROOT = Path(__file__).resolve().parents[1]
BOOKS = ROOT / "data" / "books.json"
BRANCHES = ROOT / "data" / "branches.json"


def seed():
    docs = json_util.loads(BOOKS.read_text(encoding="utf-8"))
    books.drop()
    books.insert_many(docs)
    books.create_index("book_id", unique=True)
    books.create_index([("title", "text"), ("summary", "text")])
    print(f"Seeded {len(docs)} books")
    places = json_util.loads(BRANCHES.read_text(encoding="utf-8"))
    branches.drop()
    branches.insert_many(places)
    branches.create_index("code", unique=True)
    print(f"Seeded {len(places)} branches")


if __name__ == "__main__":
    seed()
