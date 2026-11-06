"""Week 6: aggregation pipelines, one stage at a time.

Run it with:  python src/pipelines.py
Change the last line to run a different pipeline.
"""
from pprint import pprint

from db import books, branches


def show(pipeline, collection=books, limit=5):
    """Run a pipeline. Print how many documents come out, then the first few."""
    results = list(collection.aggregate(pipeline))
    print(f"{len(results)} documents")
    for doc in results[:limit]:
        pprint(doc, sort_dicts=False)
    if len(results) > limit:
        print(f"... and {len(results) - limit} more")


# Task 2: how many books are in each genre?
books_per_genre = [
    {"$unwind": "$genres"},
    {"$group": {"_id": "$genres", "books": {"$sum": 1}}},
    {"$sort": {"books": -1, "_id": 1}},
]

stars_by_genre = [
    {"$match": {"year": {"$gte": 2015}}},
    {"$unwind": "$reviews"},
    {"$unwind": "$genres"},
    {"$group": {
        "_id": "$genres",
        "avg_stars": {"$avg": "$reviews.stars"},
        "review_count": {"$sum": 1}
    }},
    {"$sort": {"avg_stars": -1}}
]

if __name__ == "__main__":
    show(stars_by_genre)
