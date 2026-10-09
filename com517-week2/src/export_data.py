from pathlib import Path
from bson import json_util
from db import students

ROOT = Path(__file__).parent.parent
OUTPUT_FILE = ROOT / "data" / "students_export.json"

docs = list(students.find({}))

OUTPUT_FILE.write_text(
    json_util.dumps(docs, indent=2),
    encoding="utf-8"
)

print(f"Exported {len(docs)} students to {OUTPUT_FILE.name}")