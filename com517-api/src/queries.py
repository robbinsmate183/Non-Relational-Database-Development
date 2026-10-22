
from db import students

NAME_ONLY = {"_id": 0, "name": 1}


def on_module(code):
    """Students taking a module, sorted by surname."""
    return list(
        students.find(
            {"modules": code},
            NAME_ONLY
        ).sort("name.last", 1)
    )


def mark_at_least(module, minimum):
    """Students with at least this mark in this module."""
    query = {
        "grades": {
            "$elemMatch": {
                "module": module,
                "mark": {"$gte": minimum}
            }
        }
    }

    return list(
        students.find(
            query,
            NAME_ONLY
        ).sort("name.last", 1)
    )
