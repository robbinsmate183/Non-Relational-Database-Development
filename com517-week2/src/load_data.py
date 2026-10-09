from pathlib import Path
from bson import json_util
from db import students

ROOT = Path(__file__).parent.parent
DATA_FILE = ROOT / "data" / "students.json"

text = DATA_FILE.read_text(encoding="utf-8")
docs = json_util.loads(text)

students.drop()
result = students.insert_many(docs)

print(f"Loaded {len(result.inserted_ids)} students from {DATA_FILE.name}")