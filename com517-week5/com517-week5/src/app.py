
from flask import Flask, jsonify, request

import queries
from db import students

app = Flask(__name__)

PUBLIC = {"_id": 0}  # Never send MongoDB ObjectIds to the client


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
        return jsonify({
            "error": "min must be a whole number from 0 to 100"
        }), 400

    found = queries.mark_at_least(module, int(minimum))

    return jsonify({"count": len(found), "results": found})


@app.get("/students/in-society/<name>")
def in_society(name):
    found = list(
        students.find({"societies": name}, PUBLIC).sort("name.last", 1)
    )

    return jsonify({"count": len(found), "results": found})


# ---------------- Create: Week 5 ----------------

@app.post("/students")
def create_student():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "error": "Student data must be a JSON object"
        }), 400

    required = ["student_id", "name", "course", "year"]

    for field in required:
        if field not in data:
            return jsonify({
                "error": f"Missing required field: {field}"
            }), 400

    if (
        not isinstance(data["student_id"], str)
        or not data["student_id"].strip()
        or not isinstance(data["name"], dict)
        or not isinstance(data["name"].get("first"), str)
        or not isinstance(data["name"].get("last"), str)
        or not data["name"]["first"].strip()
        or not data["name"]["last"].strip()
        or not isinstance(data["course"], str)
        or not data["course"].strip()
        or type(data["year"]) is not int
        or not 1 <= data["year"] <= 4
        or "_id" in data
    ):
        return jsonify({"error": "Invalid student data"}), 400

    if students.find_one({"student_id": data["student_id"]}):
        return jsonify({"error": "Student ID already exists"}), 409

    students.insert_one(data)

    return jsonify({
        "message": "Student created successfully"
    }), 201


# ---------------- Update: Week 5 ----------------

@app.patch("/students/<student_id>")
def update_student(student_id):
    data = request.get_json(silent=True)

    if not isinstance(data, dict) or not data:
        return jsonify({
            "error": "Valid JSON data is required"
        }), 400

    if "student_id" in data or "_id" in data:
        return jsonify({
            "error": "Student ID cannot be changed"
        }), 400

    if "year" in data:
        if type(data["year"]) is not int or not 1 <= data["year"] <= 4:
            return jsonify({"error": "Invalid year"}), 400

    result = students.update_one(
        {"student_id": student_id},
        {"$set": data}
    )

    if result.matched_count == 0:
        return jsonify({"error": "Student not found"}), 404

    return jsonify({
        "message": "Student updated successfully"
    }), 200


# ---------------- Add Society: Week 5 ----------------

@app.post("/students/<student_id>/societies")
def add_society(student_id):
    data = request.get_json(silent=True)

    if (
        not isinstance(data, dict)
        or not isinstance(data.get("society"), str)
        or not data["society"].strip()
    ):
        return jsonify({
            "error": "A society name is required"
        }), 400

    result = students.update_one(
        {"student_id": student_id},
        {"$addToSet": {"societies": data["society"]}}
    )

    if result.matched_count == 0:
        return jsonify({"error": "Student not found"}), 404

    return jsonify({
        "message": "Society added successfully"
    }), 200


# ---------------- Remove Society: Week 5 ----------------

@app.delete("/students/<student_id>/societies/<name>")
def remove_society(student_id, name):
    result = students.update_one(
        {"student_id": student_id},
        {"$pull": {"societies": name}}
    )

    if result.matched_count == 0:
        return jsonify({"error": "Student not found"}), 404

    return jsonify({
        "message": "Society removed successfully"
    }), 200


# ---------------- Delete Student: Week 5 ----------------

@app.delete("/students/<student_id>")
def delete_student(student_id):
    result = students.delete_one(
        {"student_id": student_id}
    )

    if result.deleted_count == 0:
        return jsonify({"error": "Student not found"}), 404

    return jsonify({
        "message": "Student deleted successfully"
    }), 200


# ---------------- Promote Students: Week 5 ----------------

@app.post("/students/promote")
def promote_students():
    result = students.update_many(
        {"year": {"$gte": 1, "$lt": 4}},
        {"$inc": {"year": 1}}
    )

    return jsonify({
        "message": "Students promoted successfully",
        "promoted": result.modified_count
    }), 200


# ---------------- Run Flask ----------------

if __name__ == "__main__":
    app.run(debug=True, port=5001)
