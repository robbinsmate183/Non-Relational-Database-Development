
from flask import Flask, jsonify, request

from db import students
from queries import mark_at_least

app = Flask(__name__)

# Exclude MongoDB ObjectIds from JSON responses
PUBLIC = {"_id": 0}


# HOME PAGE
@app.get("/")
def index():
    return jsonify({"message": "COM517 student API"})


# GET STUDENTS WITH A MINIMUM MARK IN A MODULE
@app.get("/students/with-mark")
def students_with_mark():
    module = request.args.get("module")

    if not module:
        return jsonify({
            "error": "module is required"
        }), 400

    minimum = request.args.get("min", "70")

    try:
        minimum = int(minimum)
    except ValueError:
        return jsonify({
            "error": "min must be a whole number"
        }), 400

    if minimum < 0 or minimum > 100:
        return jsonify({
            "error": "min must be between 0 and 100"
        }), 400

    found = mark_at_least(module, minimum)

    return jsonify({
        "count": len(found),
        "results": found
    })


# GET STUDENTS IN A SOCIETY
@app.get("/students/in-society/<name>")
def students_in_society(name):
    found = list(
        students.find(
            {"societies": name},
            PUBLIC
        ).sort("name.last", 1)
    )

    return jsonify({
        "count": len(found),
        "results": found
    })


# GET ONE STUDENT BY ID
@app.get("/students/<student_id>")
def get_student(student_id):
    student = students.find_one(
        {"student_id": student_id},
        PUBLIC
    )

    if student is None:
        return jsonify({
            "error": "student not found"
        }), 404

    return jsonify(student)


# LIST ALL STUDENTS WITH OPTIONAL FILTERS
@app.get("/students")
def list_students():
    query = {}

    course = request.args.get("course")

    if course:
        query["course"] = course

    year = request.args.get("year")

    if year is not None:
        if not year.isdigit():
            return jsonify({
                "error": "year must be a whole number"
            }), 400

        query["year"] = int(year)

    found = list(
        students.find(query, PUBLIC).sort("name.last", 1)
    )

    return jsonify({
        "count": len(found),
        "results": found
    })


if __name__ == "__main__":
    app.run(debug=True, port=5001)
