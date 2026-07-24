from flask import Blueprint, jsonify, request
from services.lab_test_service import *

lab_test_bp = Blueprint("lab_test", __name__)

@lab_test_bp.route("/labtests", methods=["GET"])
def get_lab_tests():

    tests = get_all_lab_tests()

    return jsonify(tests)

@lab_test_bp.route("/labtests/<int:test_id>", methods=["GET"])
def get_lab_test(test_id):

    test = get_lab_test_by_id(test_id)

    if not test:
        return jsonify({
            "message": "Lab test not found"
        }),404

    return jsonify(test)

@lab_test_bp.route("/labtests", methods=["POST"])
def create_lab_test():

    data = request.get_json()

    required_fields = [
        "prescription_id",
        "test_type",
        "test_date",
        "status",
        "result"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "message": f"{field} is required"
            }),400

    test_id = add_lab_test(
        data["prescription_id"],
        data["test_type"],
        data["test_date"],
        data["status"],
        data["result"]
    )

    return jsonify({
        "message":"Lab test created successfully",
        "test_id":test_id
    }),201

@lab_test_bp.route("/labtests/<int:test_id>", methods=["PUT"])
def edit_lab_test(test_id):

    data = request.get_json()

    required_fields = [
        "prescription_id",
        "test_type",
        "test_date",
        "status",
        "result"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "message":f"{field} is required"
            }),400

    rows = update_lab_test(
        test_id,
        data["prescription_id"],
        data["test_type"],
        data["test_date"],
        data["status"],
        data["result"]
    )

    if rows == 0:
        return jsonify({
            "message":"Lab test not found"
        }),404

    return jsonify({
        "message":"Lab test updated successfully"
    }),200


@lab_test_bp.route("/labtests/<int:test_id>", methods=["DELETE"])
def remove_lab_test(test_id):

    rows = delete_lab_test(test_id)

    if rows == 0:
        return jsonify({
            "message":"Lab test not found"
        }),404

    return jsonify({
        "message":"Lab test deleted successfully"
    }),200