from flask import Blueprint, jsonify, request
from services.dispenses_service import *
dispense_bp = Blueprint("dispense", __name__)

#GET ALL
@dispense_bp.route("/dispenses", methods=["GET"])
def get_dispenses():

    dispenses = get_all_dispenses()

    return jsonify(dispenses)

#GET BY ID 
@dispense_bp.route("/dispenses/<int:dispense_id>", methods=["GET"])
def get_dispense(dispense_id):

    dispense = get_dispense_by_id(dispense_id)

    if not dispense:
        return jsonify({
            "message": "Dispense not found"
        }),404

    return jsonify(dispense)

#POST
@dispense_bp.route("/dispenses", methods=["POST"])
def create_dispense():

    data = request.get_json()

    required_fields = [
        "prescription_id",
        "staff_id",
        "dispense_date"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "message": f"{field} is required"
            }),400

    dispense_id = add_dispense(
        data["prescription_id"],
        data["staff_id"],
        data["dispense_date"]
    )

    return jsonify({
        "message":"Dispense created successfully",
        "dispense_id":dispense_id
    }),201

#PUT
@dispense_bp.route("/dispenses/<int:dispense_id>", methods=["PUT"])
def edit_dispense(dispense_id):

    data = request.get_json()

    required_fields = [
        "prescription_id",
        "staff_id",
        "dispense_date"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "message":f"{field} is required"
            }),400

    rows = update_dispense(
        dispense_id,
        data["prescription_id"],
        data["staff_id"],
        data["dispense_date"]
    )

    if rows == 0:
        return jsonify({
            "message":"Dispense not found"
        }),404

    return jsonify({
        "message":"Dispense updated successfully"
    }),200

#DELETE
@dispense_bp.route("/dispenses/<int:dispense_id>", methods=["DELETE"])
def remove_dispense(dispense_id):

    rows = delete_dispense(dispense_id)

    if rows == 0:
        return jsonify({
            "message":"Dispense not found"
        }),404

    return jsonify({
        "message":"Dispense deleted successfully"
    }),200