from flask import Blueprint, jsonify, request

from services.staff_service import (
    get_all_staff,
    get_staff_by_id,
    add_staff,
    update_staff,
    delete_staff
)

staff_bp = Blueprint("staff", __name__)

#GET ALL
@staff_bp.route("/staff", methods=["GET"])
def get_staff():

    staff = get_all_staff()

    staff_list = []

    for s in staff:
        staff_list.append({
            "staff_id": s[0],
            "name": s[1],
            "contact": s[2],
            "dob": str(s[3]),
            "doj": str(s[4]),
            "role": s[5]
        })

    return jsonify(staff_list), 200

#GET ID
@staff_bp.route("/staff/<int:staff_id>", methods=["GET"])
def get_staff_member(staff_id):

    staff = get_staff_by_id(staff_id)

    if not staff:
        return jsonify({
            "message": "Staff not found"
        }), 404

    return jsonify({
        "staff_id": staff[0],
        "name": staff[1],
        "contact": staff[2],
        "dob": str(staff[3]),
        "doj": str(staff[4]),
        "role": staff[5]
    }), 200

#POST
@staff_bp.route("/staff", methods=["POST"])
def create_staff():

    data = request.get_json()

    required_fields = [
        "name",
        "contact",
        "dob",
        "doj",
        "role"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "message": f"{field} is required"
            }), 400

    staff_id = add_staff(
        data["name"],
        data["contact"],
        data["dob"],
        data["doj"],
        data["role"]
    )

    return jsonify({
        "message": "Staff created successfully",
        "staff_id": staff_id
    }), 201

#PUT
@staff_bp.route("/staff/<int:staff_id>", methods=["PUT"])
def edit_staff(staff_id):

    data = request.get_json()

    required_fields = [
        "name",
        "contact",
        "dob",
        "doj",
        "role"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "message": f"{field} is required"
            }), 400

    rows = update_staff(
        staff_id,
        data["name"],
        data["contact"],
        data["dob"],
        data["doj"],
        data["role"]
    )

    if rows == 0:
        return jsonify({
            "message": "Staff not found"
        }), 404

    return jsonify({
        "message": "Staff updated successfully"
    }), 200

#DELETE
@staff_bp.route("/staff/<int:staff_id>", methods=["DELETE"])
def remove_staff(staff_id):

    rows = delete_staff(staff_id)

    if rows == 0:
        return jsonify({
            "message": "Staff not found"
        }), 404

    return jsonify({
        "message": "Staff deleted successfully"
    }), 200