from flask import Flask, jsonify, request

import queries
from db import students

app = Flask(__name__)

PUBLIC = {"_id": 0}  # never send ObjectIds to the client


# ---------------- Read ----------------

@app.get("/")
def index():
    return jsonify({"message": "COM517 student API"})


@app.get("/students")
def list_students():
    query = {}
    course = request.args.get("course")
    if course:
        query["course"] = course
    year = request.args.get("year")
    if year is not None:
        if not year.isdigit():
            return jsonify({"error": "year must be a whole number"}), 400
        query["year"] = int(year)
    found = list(students.find(query, PUBLIC).sort("name.last", 1))
    return jsonify({"count": len(found), "results": found})


@app.get("/students/<student_id>")
def get_student(student_id):
    student = students.find_one({"student_id": student_id}, PUBLIC)
    if student is None:
        return jsonify({"error": "student not found"}), 404
    return jsonify(student)


@app.get("/students/with-mark")
def with_mark():
    module = request.args.get("module")
    minimum = request.args.get("min", "70")
    if not module:
        return jsonify({"error": "module is required"}), 400
    if not minimum.isdigit() or int(minimum) > 100:
        return jsonify({"error": "min must be a whole number from 0 to 100"}), 400
    found = queries.mark_at_least(module, int(minimum))
    return jsonify({"count": len(found), "results": found})


@app.get("/students/in-society/<name>")
def in_society(name):
    found = list(students.find({"societies": name}, PUBLIC).sort("name.last", 1))
    return jsonify({"count": len(found), "results": found})


# ---------------- Create, update, delete: Week 5 ----------------


if __name__ == "__main__":
    app.run(debug=True, port=5001)
